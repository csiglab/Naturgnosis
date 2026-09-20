#!/usr/bin/env python3
"""
Bootstrap the Epistemic Space dataset from the Epistecnica epistemica export.

Reads app/epistemica/import/epistemica_data.json (122 nodes in the
epistemica app's schema) and writes app/epistemica/data/data.json — nodes in
the Naturgnosis node model. Re-runnable: regenerates from the import.

Mapping (source -> Naturgnosis):

    id, name, category, description    kept
    relationships                      relationships (same shape)
    specific (+functionalRoles,
             realityDomains)           specific
    metadata.tags                      tags (with humanized category)
    historicalContext                  chronology
    metadata.inheritanceLevel          metadata
    layer                              fixed to "Epistemic"

Usage:

    python bin/import_epistemica.py
"""

import json
import sys
from datetime import date
from pathlib import Path


def humanize(camel):
    out = ""
    for ch in camel:
        if ch.isupper() and out:
            out += " "
        out += ch
    return out.lower().strip()


def convert(src):
    meta = dict(src.get("metadata") or {})
    tags = list(meta.get("tags") or [])
    cat = humanize(src.get("category", ""))
    if cat and cat not in tags:
        tags = [cat] + tags

    hist = src.get("historicalContext") or {}
    chronology = {
        "summary": hist.get("summary", "") if isinstance(hist, dict) else "",
        "events": hist.get("chronology", []) if isinstance(hist, dict) else [],
    }

    specific = dict(src.get("specific") or {})
    for key in ("functionalRoles", "realityDomains"):
        if src.get(key):
            specific[key] = src[key]

    metadata = {
        k: v for k, v in meta.items() if k != "tags"
    }
    metadata["inheritanceLevel"] = src.get("inheritanceLevel", 0)
    metadata.setdefault("source", "epistecnica-import")
    metadata.setdefault("imported", date.today().isoformat())

    return {
        "id": src.get("id"),
        "name": src.get("name"),
        "tags": tags,
        "layer": "Epistemic",
        "category": src.get("category", ""),
        "description": src.get("description", ""),
        "longDescription": "",
        "chronology": chronology,
        "relationships": src.get("relationships", []) or [],
        "specific": specific,
        "metadata": metadata,
        "references": src.get("references", []) or [],
    }


def main(argv=None):
    here = Path(__file__).resolve().parent
    repo = here.parent
    src = repo / "app" / "epistemica" / "import" / "epistemica_data.json"
    out = repo / "app" / "epistemica" / "data" / "data.json"

    if not src.exists():
        print(f"ERROR: import file not found: {src}", file=sys.stderr)
        return 1

    raw = json.loads(src.read_text(encoding="utf-8"))
    nodes = [convert(n) for n in raw if isinstance(n, dict) and n.get("id")]
    nodes = [n for n in nodes if n["id"] and n["name"]]

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(nodes, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"[epistemica] imported {len(nodes)} nodes -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
