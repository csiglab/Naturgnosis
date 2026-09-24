#!/usr/bin/env python3
"""
Import nation-space actors into the Social Space graph (copy, not move).

Reads app/nation/data/actors/<iso>.json (34 files, the nation module's
source of truth — never written by this script) and upserts the actors
missing from the social dataset as new nodes. Re-runnable: name-matching
makes repeat runs a no-op (all matches skipped).

Mapping (nation actor -> social node):

    <iso>-<aid>                  id (namespaced; per-country a1 clashes + numeric ids)
    name                         name
    ["actor", Country, type, role] tags
    normalized type              category (Institution|Organization, see TYPE_FOLD)
    Agentic                      layer
    description                  description (fallback: "name (role in Country)")
    events[]                     chronology.events
    []                           relationships (no country nodes in social to link)
    {nationActor: {...}}         specific (country, iso, originalId, type, role, region)
    provenance                   metadata (sourceReference, importedAt, auditTrail)

Dedup: case-insensitive name match against the LIVE social dataset
(GET /api/graph?dataset=social, --mirror fallback to data.json).
Matches are skipped and reported per country (import-only-new policy).

Usage:
    python bin/import_social_actors.py              # dry run: report only
    python bin/import_social_actors.py --apply      # POST new nodes to the sync server
    python bin/import_social_actors.py --apply --mirror  # merge into data.json directly (offline)

Rollback: --apply prints a manifest of added ids; removal = filter those
ids out and reseed (bin/seed_couchdb.py).
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ACTORS = REPO / "app" / "nation" / "data" / "actors"
MIRROR = REPO / "app" / "social" / "data" / "data.json"

API_BASE = "http://localhost:8011"
SAVE_ENDPOINT = "/api/graph/save"
LOAD_ENDPOINT = "/api/graph"

# Raw type variants -> canonical token.
TYPE_FOLD = {
    "non-profit": "nonprofit",
    "nonprofit": "nonprofit",
    "coop": "cooperative",
    "cooperative": "cooperative",
    "edu": "academic",
    "academic": "academic",
    "public-private": "hybrid",
    "public/private hybrid": "hybrid",
    "government / public-private hybrid": "hybrid",
    "public/hybrid": "hybrid",
    "government_research_agency": "research",
    "research_institute": "research",
    "research institution": "research",
    "research institute": "research",
    "scientific research": "research",
    "government technical staff": "government",
    "technical staff": "government",
    "government agency": "government",
    "government office": "government",
    "government board": "government",
    "local government": "government",
    "government ministry": "government",
    "regulatory agency": "government",
    "university faculty": "university",
    "educational institution": "academic",
    "vocational education institution": "academic",
    "vocational training entity": "academic",
    "technical school": "academic",
    "industrial company": "industry",
    "industrial enterprise": "industry",
    "industrial manufacturer": "industry",
    "chemical industrial company": "industry",
    "manufacturing enterprise": "industry",
    "industrial facility": "industry",
    "industry association": "industry",
    "industry board": "industry",
    "professional organization": "professional",
    "professional body": "professional",
    "political party": "political",
}

INSTITUTION_TYPES = {
    "public", "government", "semistate", "institution",
    "research", "academic", "university", "political",
    "legal", "governance", "policy", "legislation", "regulation",
    "infrastructure", "treaty", "intergov",
}


def fold_type(raw: str) -> str:
    t = (raw or "").strip().lower().replace("_", " ")
    t = " ".join(t.split())
    return TYPE_FOLD.get(t, t or "actor")


def category_for(norm: str) -> str:
    return "Institution" if norm in INSTITUTION_TYPES else "Organization"


def live_nodes(couch_url: str) -> list | None:
    """Full social node list from the sync server, or None when offline."""
    url = f"{couch_url}{LOAD_ENDPOINT}?dataset=social"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data if isinstance(data, list) else None
    except Exception as exc:
        print(f"[import] live read failed ({exc})", file=sys.stderr)
        return None


def mirror_nodes() -> list:
    return json.loads(MIRROR.read_text(encoding="utf-8"))


def iter_actors(warnings: list):
    """Yield (iso, country, record) for every actor record."""
    for path in sorted(ACTORS.glob("*.json")):
        iso = path.stem
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            warnings.append(f"{iso}.json: unreadable ({exc})")
            continue
        country = (doc.get("metadata") or {}).get("country", iso.upper())
        actors = doc.get("actors", [])
        for rec in actors:
            items = rec if isinstance(rec, list) else [rec]
            if isinstance(rec, list):
                warnings.append(f"{iso}.json: flattened nested list record")
            for it in items:
                if not isinstance(it, dict) or not it.get("name"):
                    warnings.append(f"{iso}.json: skipped malformed record")
                    continue
                yield iso, country, it


def convert(iso: str, country: str, rec: dict, today: str) -> dict:
    aid = str(rec.get("id", "unknown"))
    name = rec["name"].strip()
    norm = fold_type(rec.get("type"))
    role = (rec.get("role") or "").strip()
    desc = (rec.get("description") or "").strip() or f"{name} ({role or norm} in {country})"
    tags = ["actor", country, norm]
    if role:
        tags.append(role)
    events = []
    for ev in rec.get("events") or []:
        if not isinstance(ev, dict):
            continue
        events.append({
            "date": ev.get("date", ""),
            "category": ev.get("category", ""),
            "description": ev.get("description", ""),
        })
    return {
        "id": f"{iso}-{aid}",
        "name": name,
        "tags": tags,
        "layer": "Agentic",
        "category": category_for(norm),
        "description": desc,
        "longDescription": desc,
        "chronology": {
            "summary": f"Nation actor ({country})",
            "events": events,
        },
        "relationships": [],
        "specific": {
            "nationActor": {
                "country": country,
                "iso": iso,
                "originalId": aid,
                "type": norm,
                "role": role,
                "regionOfActivity": rec.get("regionOfActivity", ""),
            }
        },
        "metadata": {
            "confidenceScore": 0.6,
            "sourceReference": f"nation actors {iso}.json:{aid}",
            "createdAt": today,
            "auditTrail": ["imported by bin/import_social_actors.py"],
            "inheritanceLevel": 0,
        },
        "references": [],
    }


def plan(existing: list) -> tuple:
    """Split nation actors into (new_nodes, skipped, warnings, stats)."""
    have_names = {str(n.get("name", "")).strip().lower() for n in existing if isinstance(n, dict)}
    have_ids = {str(n.get("id")) for n in existing if isinstance(n, dict) and n.get("id")}
    today = date.today().isoformat()
    warnings, new_nodes, skipped = [], [], []
    seen_names = set()
    per_country = {}
    for iso, country, rec in iter_actors(warnings):
        key = rec["name"].strip().lower()
        stat = per_country.setdefault(iso, {"added": 0, "skipped": 0})
        if key in have_names or key in seen_names:
            skipped.append((iso, rec.get("id"), rec["name"].strip()))
            stat["skipped"] += 1
            continue
        node = convert(iso, country, rec, today)
        if node["id"] in have_ids:
            node["id"] = f"{node['id']}-2"
            warnings.append(f"{iso}:{rec.get('id')}: id collision, suffixed -> {node['id']}")
        have_ids.add(node["id"])
        seen_names.add(key)
        new_nodes.append(node)
        stat["added"] += 1
    return new_nodes, skipped, warnings, per_country


def post_nodes(couch_url: str, nodes: list) -> dict:
    body = json.dumps({"nodes": nodes, "dataset": "social"}).encode("utf-8")
    req = urllib.request.Request(
        f"{couch_url}{SAVE_ENDPOINT}", data=body, method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="import_social_actors.py")
    ap.add_argument("--apply", action="store_true", help="POST new nodes to the sync server.")
    ap.add_argument("--mirror", action="store_true", help="With --apply: merge into data.json directly (offline).")
    ap.add_argument("--couch-url", default="http://localhost:8011", help="Sync server base URL.")
    args = ap.parse_args(argv)

    existing = None if args.mirror else live_nodes(args.couch_url)
    source = "couchdb-live"
    if existing is None:
        existing = mirror_nodes()
        source = "data.json-mirror"
    print(f"[import] social baseline: {len(existing)} nodes ({source})")

    new_nodes, skipped, warnings, per_country = plan(existing)
    print(f"[import] nation actors evaluated; new: {len(new_nodes)}, skipped (already in social): {len(skipped)}")
    for iso in sorted(per_country):
        s = per_country[iso]
        print(f"  {iso}: +{s['added']} / skip {s['skipped']}")
    for w in warnings:
        print(f"  ! {w}")
    print("[import] sample new nodes:")
    for n in new_nodes[:5]:
        print(f"  {n['id']} | {n['name'][:55]} | {n['category']} | {n['tags']}")

    if not args.apply:
        print("[import] dry run — no writes (use --apply)")
        return 0

    if args.mirror:
        merged = existing + new_nodes
        MIRROR.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[import] merged {len(new_nodes)} nodes into {MIRROR.relative_to(REPO)}")
    else:
        res = post_nodes(args.couch_url, new_nodes)
        print(f"[import] server save: {res}")

    print("[import] manifest (added ids):")
    for n in new_nodes:
        print(f"  + {n['id']}")
    print("[import] next: make build  &&  python bin/build_search_index.py  &&  python bin/seed_couchdb.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
