#!/usr/bin/env python3
"""
Bootstrap the Technique Space dataset from the Epistecnica tecnica export.

Reads app/technique/import/tecnica_data.json (40 nodes in the tecnica app's
schema) and writes app/technique/data/data.json — nodes in the Naturgnosis
node model. Re-runnable: regenerates the file from the import.

Mapping (source -> Naturgnosis):

    id, name, category, layer          kept
    short_description                  description
    long_description                   longDescription
    relationship_set                   relationships (same shape)
    references                         references
    evolution_history / lifecycle      chronology
    tecnica-only fields                specific
    metadata                           metadata (+ source: epistecnica-import)

Usage:

    python bin/import_technique.py
"""

import json
import sys
from datetime import date
from pathlib import Path

SPECIFIC_FIELDS = [
    "functional_role_set",
    "interface_specification",
    "operation",
    "implementation_specification",
    "scope_specification",
    "limitation_set",
    "resource_use",
    "failure_mode_specification",
    "type_hierarchy_level",
    "particular_characterization",
]


def humanize(camel):
    out = ""
    for ch in camel:
        if ch.isupper() and out:
            out += " "
        out += ch
    return out.lower()


def convert(src):
    tags = [humanize(src.get("category", "")), humanize(src.get("layer", ""))]
    tags = [t for t in tags if t]

    chronology = {}
    evo = src.get("evolution_history")
    if isinstance(evo, list) and evo:
        events = []
        for item in evo:
            if isinstance(item, dict):
                events.append(
                    {
                        "year": item.get("year") or item.get("period") or "",
                        "event": item.get("event") or item.get("title") or "",
                        "context": item.get("description") or item.get("context") or "",
                    }
                )
            elif isinstance(item, str):
                events.append({"year": "", "event": item, "context": ""})
        chronology = {"summary": "", "events": events}
    elif isinstance(src.get("lifecycle"), str) and src["lifecycle"]:
        chronology = {"summary": src["lifecycle"], "events": []}

    metadata = dict(src.get("metadata") or {})
    metadata.setdefault("source", "epistecnica-import")
    metadata.setdefault("imported", date.today().isoformat())

    return {
        "id": src.get("id"),
        "name": src.get("name"),
        "tags": tags,
        "layer": src.get("layer", ""),
        "category": src.get("category", ""),
        "description": src.get("short_description", ""),
        "longDescription": src.get("long_description", ""),
        "chronology": chronology,
        "relationships": src.get("relationship_set", []) or [],
        "specific": {k: src.get(k) for k in SPECIFIC_FIELDS if src.get(k) not in (None, "", [])},
        "metadata": metadata,
        "references": src.get("references", []) or [],
    }


def main(argv=None):
    here = Path(__file__).resolve().parent
    repo = here.parent
    src = repo / "app" / "technique" / "import" / "tecnica_data.json"
    out = repo / "app" / "technique" / "data" / "data.json"

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

    print(f"[technique] imported {len(nodes)} nodes -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
