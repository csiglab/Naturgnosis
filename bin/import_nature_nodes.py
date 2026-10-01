#!/usr/bin/env python3
"""Bulk-import nature graph nodes from the instance registry.

Reads the curated registry (/tmp/nature_elements.json: canonical elements
with element_type, source_files) plus the file index (/tmp/to_migrate.json:
per-file relation edges) and upserts one node per migratable element into
the `nature` dataset via POST /api/graph/save (server mirrors to
app/nature/data/data.json), or stages them to /tmp/nature_nodes.json first.

Migration policy:
  - skip bare grouping-type placeholders (never terminal per the guide)
  - skip elements already covered by existing nodes
    (nature/earth/mineral/electric-field -> enrich-only, never duplicate)
  - INCLUDE needs_human elements, flagged (confidenceScore 0.5,
    specific.needsHuman, auditTrail note)
  - ids: <kebab-slug>-ontic-001 (-002 on collision); elementKey reuse keeps
    ids stable across runs; ORIGINAL_IDS are never reassigned
  - edges: file-index relation hrefs resolved to node ids in-batch (or to
    the 4 anchor nodes); unresolvable targets dropped with a logged count;
    predicate honest: associated_with / "predicate not yet worked"

Usage:
  python bin/import_nature_nodes.py --stage-only          # /tmp/nature_nodes.json + stats
  python bin/import_nature_nodes.py --push --port 8126    # stage + POST in batches
Stdlib only.
"""

import argparse
import json
import re
import unicodedata
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TODAY = datetime.now(timezone.utc).date().isoformat()
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")

ALREADY_NODED = {"nature", "earth", "mineral", "electric field"}
ANCHOR_IDS = {
    "nature": "nature-ontic-001",
    "earth": "earth-ontic-001",
    "mineral": "mineral-ontic-001",
    "electric field": "electric-field-ontic-001",
}
# Pre-import nodes (seed + moved-from-epistemica); never reassigned.
ORIGINAL_IDS = {
    "em-wave-ontic-001", "process_decision_making", "electric-field-ontic-001",
    "radiation-pressure-001", "maxwell-equations-001", "quarry-ontic-001",
    "nature-ontic-001", "earth-ontic-001", "earth-material-ontic-001",
    "mineral-ontic-001", "natural-material-ontic-001", "biogenic-material-ontic-001",
}


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "untitled"


def nkey(s):
    s = s.lower().strip()
    s = re.sub(r"\s*\(.*?\)\s*", " ", s)
    s = re.sub(r"[^a-z0-9 /+%-]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def split_stem(filename):
    if filename.endswith(".md"):
        filename = filename[:-3]
    parts = filename.rsplit(" ", 1)
    if len(parts) == 2 and re.fullmatch(r"[0-9a-f]{32}", parts[1]):
        return parts[0]
    return filename


def unquote(s):
    import urllib.parse
    try:
        return urllib.parse.unquote(s)
    except Exception:
        return s


def build_nodes():
    reg = json.loads(Path("/tmp/nature_elements.json").read_text(encoding="utf-8"))
    mig = json.loads(Path("/tmp/to_migrate.json").read_text(encoding="utf-8"))
    data = json.loads((REPO / "app/nature/data/data.json").read_text(encoding="utf-8"))
    existing_ids = {n["id"] for n in data if isinstance(n, dict) and n.get("id")}

    # file display-name -> registry key (for edge resolution via hrefs)
    disp2key = {}
    for e in reg["elements"]:
        disp2key[e["canonical_name"]] = e["key"]
        for a in e.get("aliases", []):
            disp2key.setdefault(a, e["key"])
    # relations per registry key, from title files in the file index
    rels_by_key = {}
    for it in mig["items"]:
        key = disp2key.get(it["element"])
        if not key:
            continue
        for r in (it.get("reference_files") or {}).get("relations", []):
            href = r.get("href", "")
            base = unquote(href.split("/")[-1])
            target_disp = split_stem(base)
            rels_by_key.setdefault(key, []).append(
                {"label": r.get("label", ""), "target_disp": target_disp,
                 "target_key": nkey(target_disp)})

    els = [e for e in reg["elements"]
           if not e.get("is_type_placeholder") and e["key"] not in ALREADY_NODED]
    skipped_covered = sum(1 for e in reg["elements"] if e["key"] in ALREADY_NODED)
    skipped_ph = sum(1 for e in reg["elements"] if e.get("is_type_placeholder"))

    # id assignment (deterministic: sorted by key).
    # Idempotency: reuse ids already assigned to an elementKey in a prior
    # run (else our own mirror output collides with itself -> -002 dupes).
    used = set(existing_ids)
    node_id_by_key = dict(ANCHOR_IDS)
    for n in data:
        if not isinstance(n, dict):
            continue
        spec = n.get("specific")
        if isinstance(spec, dict) and spec.get("elementKey"):
            k = spec["elementKey"]
            if k not in node_id_by_key:
                node_id_by_key[k] = n["id"]
                used.add(n["id"])
    for e in sorted(els, key=lambda x: x["key"]):
        if e["key"] in node_id_by_key:
            used.add(node_id_by_key[e["key"]])
            continue
        # Fresh assignment: only ids claimed by another elementKey or in the
        # original set block a candidate; unclaimed legacy/damaged docs
        # (no elementKey) are reusable by the key they naturally belong to.
        blocking = set(used)
        for n in data:
            if not isinstance(n, dict):
                continue
            spec = n.get("specific")
            unclaimed = (not isinstance(spec, dict)) or (not spec.get("elementKey"))
            if unclaimed and n.get("id") not in ORIGINAL_IDS:
                blocking.discard(n.get("id"))
        base = slugify(e["canonical_name"])
        nid, i = "%s-ontic-001" % base, 2
        while nid in blocking:
            nid = "%s-ontic-%03d" % (base, i)
            i += 1
        used.add(nid)
        node_id_by_key[e["key"]] = nid

    # tags per key from file index csv_tags
    tags_by_key = {}
    for it in mig["items"]:
        key = disp2key.get(it["element"])
        if key and key not in tags_by_key:
            tags_by_key[key] = (it.get("reference_files") or {}).get("csv_tags", []) or []
    defs_by_key = {}
    for it in mig["items"]:
        key = disp2key.get(it["element"])
        d = (it.get("reference_files") or {}).get("definition", "")
        if key and d and key not in defs_by_key:
            defs_by_key[key] = re.sub(r"\*+", "", d).strip()

    nodes, resolved, dropped = [], 0, 0
    for e in sorted(els, key=lambda x: x["key"]):
        nid = node_id_by_key[e["key"]]
        et = e["element_type"]
        # confidence from typing origin; needs_human caps at 0.5
        score = 0.5
        origin = et.get("origin", "")
        if origin.startswith("file-title-anchor") and not et.get("needs_human"):
            score = 0.85
        elif origin.startswith("source-majority"):
            m = re.search(r"(\d+)/(\d+)", origin)
            if m and not et.get("needs_human"):
                score = 0.7 if int(m.group(1)) / int(m.group(2)) >= 0.6 else 0.5
        if et.get("needs_human"):
            score = min(score, 0.5)
        definition = defs_by_key.get(e["key"], "")
        desc = definition or "Imported natural instance; description pending."
        tags = sorted({t for t in (tags_by_key.get(e["key"], []) + ["nature", "ontic", slugify(et["natural_element_type"])]) if t})
        rels = []
        seen_t = set()
        for r in rels_by_key.get(e["key"], [])[:24]:
            tk = r["target_key"]
            tid = node_id_by_key.get(tk)
            if not tid or tid == nid or tid in seen_t:
                if not tid:
                    dropped += 1
                continue
            seen_t.add(tid)
            rels.append({
                "relationshipFamily": "structural",
                "relationshipType": "associated_with",
                "targetNodeId": tid,
                "description": "Imported Notion-export association%s; predicate not yet worked." % (
                    " (%s)" % r["label"][:80] if r["label"] else ""),
            })
            resolved += 1
            if len(rels) >= 12:
                break
        prov = []
        for s in e.get("source_files", [])[:6]:
            b = s.get("md", "").split("/")[-1]
            if b not in prov:
                prov.append(b)
        notes = ["Notion-export instance import (bulk wave 1)."]
        if et.get("needs_human"):
            notes.append("Typing/level needs human review (deferred queue).")
        nodes.append({
            "id": nid,
            "name": e["canonical_name"][:120],
            "tags": tags,
            "layer": "Epistemic",
            "category": "reality",
            "description": desc[:600],
            "longDescription": "",
            "chronology": {"summary": "", "events": []},
            "relationships": rels,
            "specific": {
                "ontologicalClass": "%s.%s" % (et["natural_category"], et["natural_element_type"]),
                "naturalCategory": et["natural_category"],
                "naturalElementType": et["natural_element_type"],
                "levelOfExistence": et.get("level", "meso"),
                "elementKey": e["key"],
                "aliases": e.get("aliases", [])[:12],
                "needsHuman": bool(et.get("needs_human")),
                "typingOrigin": et.get("origin", ""),
                "sourceFiles": prov,
            },
            "metadata": {
                "confidenceScore": score,
                "sourceReference": "Notion export Conceptual Model Natural System",
                "createdAt": NOW,
                "auditTrail": [{"reviewDate": TODAY,
                                "reviewNote": " ".join(notes)}],
            },
            "references": [
                {"title": "How to decompose any natural instance? (philosophia-naturalis-et-operis)",
                 "link": None,
                 "description": "Typing workflow for this element."},
                {"title": "Notion export provenance: " + "; ".join(prov[:4]),
                 "link": None,
                 "description": "Source files in the export block."},
            ],
        })
    return nodes, {"skipped_covered": skipped_covered, "skipped_placeholders": skipped_ph,
                   "edges_resolved": resolved, "edges_dropped": dropped,
                   "existing_ids": len(existing_ids)}


def push(nodes, port, batch=200):
    base = "http://localhost:%d" % port
    total = 0
    for i in range(0, len(nodes), batch):
        body = json.dumps({"nodes": nodes[i:i + batch], "dataset": "nature",
                           "timestamp": NOW}).encode()
        req = urllib.request.Request(base + "/api/graph/save", data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            ans = json.load(r)
        total += ans.get("saved", 0)
        print("  batch %d-%d: saved=%s mirrored=%s" % (i, min(i + batch, len(nodes)), ans.get("saved"), ans.get("mirrored")))
    return total


def main(argv=None):
    p = argparse.ArgumentParser(prog="import_nature_nodes.py")
    p.add_argument("--stage-only", action="store_true")
    p.add_argument("--push", action="store_true")
    p.add_argument("--port", type=int, default=8126)
    args = p.parse_args(argv)

    nodes, stats = build_nodes()
    Path("/tmp/nature_nodes.json").write_text(
        json.dumps(nodes, ensure_ascii=False, indent=2), encoding="utf-8")
    print("staged %d nodes -> /tmp/nature_nodes.json" % len(nodes))
    print(json.dumps(stats, indent=2))
    if args.push:
        saved = push(nodes, args.port)
        print("pushed: %d/%d" % (saved, len(nodes)))
    else:
        print("dry stage only; re-run with --push (server must run bin/sync.py)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
