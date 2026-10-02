#!/usr/bin/env python3
"""
Good-Producing Technical Element -> Technique Space node projector (Naturgnosis).

Projects the market catalog
(app/note/data/live/technique/good-producers/entries.json) into the Technique
Space graph index (app/technique/data/data.json) as first-class technical
element nodes, so every catalog type is graph-addressable and searchable.

Node shape follows the shared Naturgnosis node model
(app/technique/data/schema/schema.json): category "Technical Element",
layer "Artifact Space". The projection is idempotent — an existing id is never
overwritten, and only nodes whose id is not already present are added.

Node ids:
  good_producing_technical_element_001        branch root
  gpe_kind_<kind>_001                          one per Good kind
  gpe_<kind>_<slug(name)>                      one per catalog entry

Relationship: each entry -> its kind node -> branch root (subtype_of).

Usage: python3 bin/build_good_producer_nodes.py  (make good-producer-nodes)
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENTRIES = REPO / "app" / "note" / "data" / "live" / "technique" / "good-producers" / "entries.json"
NODES = REPO / "app" / "technique" / "data" / "data.json"

ROOT_ID = "good_producing_technical_element_001"
ROOT_NAME = "Good-Producing Technical Element"
KINDS = [
    ("material", "Material Good Producer", "Transforms matter into a delivered material good."),
    ("energy", "Energy Good Producer", "Transforms energy into delivered power, force, or conditioned energy."),
    ("information", "Information Good Producer", "Transforms information into a delivered informational or computational artifact."),
    ("service", "Service Good Producer", "Transforms reality by performing a service, where the performed service is the good."),
]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def kind_node_id(kind: str) -> str:
    return f"gpe_kind_{kind}_001"


def entry_node_id(kind: str, name: str) -> str:
    return f"gpe_{kind}_{slug(name)}"


def base_node(node_id, name, description, tags, wikidata=None):
    return {
        "id": node_id,
        "name": name,
        "tags": tags,
        "layer": "Artifact Space",
        "category": "Technical Element",
        "description": description,
        "longDescription": "",
        "chronology": {},
        "relationships": [],
        "specific": {},
        "metadata": {
            "tags": tags,
            "confidenceScore": 0.9,
            "sourceReference": "Wikidata (CC0)" if wikidata else "Philosophia Artium Technicarum et Operis",
            "source": "wikidata-import" if wikidata else "curated",
            "imported": date.today().isoformat(),
        },
        "references": [],
    }


def main() -> int:
    if not ENTRIES.is_file():
        print(f"ERROR: missing catalog {ENTRIES.relative_to(REPO)}", file=sys.stderr)
        return 1
    if not NODES.is_file():
        print(f"ERROR: missing technique index {NODES.relative_to(REPO)}", file=sys.stderr)
        return 1

    catalog = json.loads(ENTRIES.read_text(encoding="utf-8"))
    entries = catalog.get("entries", [])
    nodes = json.loads(NODES.read_text(encoding="utf-8"))
    if not isinstance(nodes, list):
        print("ERROR: technique data.json is not a node list", file=sys.stderr)
        return 1

    existing = {n.get("id") for n in nodes}
    added = 0

    def add(node):
        nonlocal added
        if node["id"] in existing:
            return False
        nodes.append(node)
        existing.add(node["id"])
        added += 1
        return True

    root = base_node(
        ROOT_ID,
        ROOT_NAME,
        "A technical element whose primary function is to transform reality itself, yielding a Good. "
        "Market-offered types are split by the kind of Good they deliver (material, energy, information, service).",
        ["good-producing technical element", "technical element", "producer", "taxonomy"],
    )
    add(root)

    for kind, name, desc in KINDS:
        node = base_node(
            kind_node_id(kind), name, desc,
            ["good-producing technical element", kind, "kind"],
        )
        node["relationships"] = [{
            "relationshipFamily": "classification",
            "relationshipType": "subtype_of",
            "targetNodeId": ROOT_ID,
            "description": f"{name} is a kind of {ROOT_NAME}.",
        }]
        add(node)

    for e in entries:
        name, kind = e.get("name", "").strip(), e.get("kind", "")
        if not name or kind not in {k for k, _, _ in KINDS}:
            continue
        node = base_node(
            entry_node_id(kind, name),
            name,
            e.get("description", ""),
            ["good-producing technical element", kind, e.get("role", ""), e.get("domain", "")],
            wikidata=e.get("wikidata"),
        )
        node["specific"] = {
            "type_path": f"(root) -> <<Technical Element>> -> Technical Order -> Production Technical System -> "
                         f"Good-Producing Technical Element -> {kind.capitalize()} Good Producer",
            "kind": kind,
            "role": e.get("role"),
            "domain": e.get("domain"),
            "transforms": e.get("transforms") or None,
            "wikidata": e.get("wikidata"),
        }
        node["relationships"] = [{
            "relationshipFamily": "classification",
            "relationshipType": "subtype_of",
            "targetNodeId": kind_node_id(kind),
            "description": f"{name} is an instance type of {kind.capitalize()} Good Producer.",
        }]
        if e.get("sources"):
            node["references"] = [{"title": "Source", "link": s} for s in e["sources"][:3]]
        add(node)

    NODES.write_text(json.dumps(nodes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"good-producer nodes: +{added} added, {len(nodes)} total -> {NODES.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
