#!/usr/bin/env python3
"""
Import persona notes into the Social Space graph as actor nodes (copy).

Reads app/note/notes/persona/*.md (migrated from Epistecnica's persona
corpus — see Phase 1) and upserts each entry as a Person/Agentic node,
with a references[] link back to its note (actor -> note direction of
the entity-view idea). Re-runnable: id- and name-matching make repeat
runs a no-op for already-imported entries.

Mapping (persona note -> social node):

    <slug>                       id (persona slugs are globally unique kebab;
                                 fallback persona-<slug> on collision)
    H1 (else filename)           name
    note tags                    tags (actor, person, disciplines...)
    Person                       category (new: nothing existing fits people)
    Agentic                      layer
    body text (<=800 chars)      description + longDescription
    []                           chronology.events (H2s are content sections)
    []                           relationships
    {title, /note/note.html?...} references (actor -> note link)
    {persona: {type}}            specific
    provenance                   metadata (sourceReference, importedAt, auditTrail)

Dedup: id assert + case-insensitive name match against the LIVE social
dataset (GET /api/graph?dataset=social, --mirror fallback to data.json).
Matches are skipped and reported (expected: none — personas are people,
social held none).

Usage:
    python bin/import_persona_actors.py              # dry run: report only
    python bin/import_persona_actors.py --apply      # POST new nodes to the sync server
    python bin/import_persona_actors.py --apply --mirror  # merge into data.json directly (offline)

Rollback: --apply prints a manifest of added ids; removal = filter those
ids out and reseed (bin/seed_couchdb.py).
"""

import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PERSONAS = REPO / "app" / "note" / "notes" / "persona"
MIRROR = REPO / "app" / "social" / "data" / "data.json"

LOAD_ENDPOINT = "/api/graph"
SAVE_ENDPOINT = "/api/graph/save"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TYPE_RE = re.compile(r"^type:\s*(\S+)\s*$", re.M)
TAGS_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$", re.M)
H1_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$", re.M)
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")


def parse_note(path: Path, warnings: list) -> dict | None:
    raw = path.read_text(encoding="utf-8", errors="replace")
    fm_match = FM_RE.match(raw)
    ptype, tags = "person", []
    body = raw
    if fm_match:
        for line in fm_match.group(1).splitlines():
            tm = TYPE_RE.match(line.strip())
            if tm:
                ptype = tm.group(1).strip().strip("'\"")
            gm = TAGS_RE.match(line.strip())
            if gm:
                tags = [t.strip().strip("'\"").lower() for t in gm.group(1).split(",") if t.strip()]
        body = raw[fm_match.end():]
    else:
        warnings.append(f"{path.name}: no front matter")
    m = H1_RE.search(body)
    title = m.group(1).strip() if m else path.stem.replace("-", " ")
    text = LINK_RE.sub(r"\1", body)
    text = re.sub(r"[#>*_`|]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return {"slug": path.stem, "title": title, "type": ptype, "tags": tags, "text": text}


def convert(p: dict, today: str) -> dict:
    desc = p["text"][:800] or f"{p['title']} ({p['type']})"
    tags = list(dict.fromkeys(["actor", p["type"]] + p["tags"]))
    return {
        "id": p["slug"],
        "name": p["title"],
        "tags": tags,
        "layer": "Agentic",
        "category": "Person",
        "description": desc,
        "longDescription": desc,
        "chronology": {
            "summary": f"Persona (Epistecnica import, type {p['type']})",
            "events": [],
        },
        "relationships": [],
        "specific": {"persona": {"type": p["type"]}},
        "metadata": {
            "confidenceScore": 0.6,
            "sourceReference": f"epistecnica personas {p['slug']}.md",
            "createdAt": today,
            "auditTrail": ["imported by bin/import_persona_actors.py"],
            "inheritanceLevel": 0,
        },
        "references": [{
            "title": p["title"],
            "link": f"/note/note.html?n=persona/{p['slug']}.md",
            "description": "Persona note in the Note Space.",
        }],
    }


def live_nodes(couch_url: str) -> list | None:
    try:
        with urllib.request.urlopen(f"{couch_url}{LOAD_ENDPOINT}?dataset=social", timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data if isinstance(data, list) else None
    except Exception as exc:
        print(f"[import] live read failed ({exc})", file=sys.stderr)
        return None


def post_nodes(couch_url: str, nodes: list) -> dict:
    body = json.dumps({"nodes": nodes, "dataset": "social"}).encode("utf-8")
    req = urllib.request.Request(
        f"{couch_url}{SAVE_ENDPOINT}", data=body, method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="import_persona_actors.py")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--mirror", action="store_true")
    ap.add_argument("--couch-url", default="http://localhost:8011")
    args = ap.parse_args(argv)

    if not PERSONAS.is_dir():
        print(f"ERROR: persona notes not found: {PERSONAS}", file=sys.stderr)
        return 1

    existing = None if args.mirror else live_nodes(args.couch_url)
    source = "couchdb-live"
    if existing is None:
        existing = json.loads(MIRROR.read_text(encoding="utf-8"))
        source = "data.json-mirror"
    print(f"[import] social baseline: {len(existing)} nodes ({source})")

    have_names = {str(n.get("name", "")).strip().lower() for n in existing if isinstance(n, dict)}
    have_ids = {str(n.get("id")) for n in existing if isinstance(n, dict) and n.get("id")}
    today = date.today().isoformat()
    warnings, new_nodes, skipped = [], [], []
    for path in sorted(PERSONAS.glob("*.md")):
        p = parse_note(path, warnings)
        if p is None:
            continue
        key = p["title"].strip().lower()
        if key in have_names:
            skipped.append((p["slug"], p["title"]))
            continue
        node = convert(p, today)
        if node["id"] in have_ids:
            node["id"] = f"persona-{node['id']}"
            warnings.append(f"{p['slug']}: id collision, namespaced -> {node['id']}")
        have_ids.add(node["id"])
        have_names.add(key)
        new_nodes.append(node)

    print(f"[import] personas evaluated: {len(new_nodes)} new, {len(skipped)} skipped")
    for s in skipped:
        print(f"  skip (already in social): {s[0]} | {s[1][:50]}")
    for w in warnings:
        print(f"  ! {w}")
    print("[import] sample new nodes:")
    for n in new_nodes[:5]:
        print(f"  {n['id']} | {n['name'][:50]} | {n['category']} | {n['tags']}")

    if not args.apply:
        print("[import] dry run — no writes (use --apply)")
        return 0

    if args.mirror:
        merged = existing + new_nodes
        MIRROR.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[import] merged {len(new_nodes)} nodes into {MIRROR.relative_to(REPO)}")
    else:
        print(f"[import] server save: {post_nodes(args.couch_url, new_nodes)}")

    print("[import] manifest (added ids):", len(new_nodes))
    print("[import] next: make build  &&  python bin/build_search_index.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
