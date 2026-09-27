#!/usr/bin/env python3
"""
Universal graph index builder (Naturgnosis hub).

Aggregates the six graph dataset mirrors
(app/{social,research,nation,technique,epistemica,nature}/data/data.json).
Production is a derived view over social, not a dataset, so its nodes enter
here once, under their social uids.
into one view-only universal graph consumed by the hub-level viewer
(app/graph/web/index.html). Stdlib only.

For each source node it keeps a minimal display record:

    {uid, source, source_id, name, category, layer, tags,
     description (excerpt), references [{title, link}], deep_link}

plus intra-dataset edges remapped onto namespaced uids
("{source}:{id}"). Cross-dataset edges are dropped by design (no shared
id space); dangling intra-dataset targets are dropped and counted.

Outputs (hub-level, like app/data/search-index.json — deliberately NOT
app/*/data/data.json so sync.py never mistakes the universal graph for
an editable dataset):

    app/data/universal-graph.json   {generated, snapshot_source,
                                     counts, nodes:[{... , targets:[uid]}]}
    app/data/universal-layout.json  {uid: [x, y]} via bin/layout.py machinery

The nation dataset is included as ordinary nodes; each nation's deep
link points at its Index Gentium entry page
(/nation/entry.html?code=<id>), all others at the source explorer
(/<source>/?node=<id>).

Usage: python3 bin/build_universal_index.py
"""

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
GRAPH_OUT = REPO / "app" / "data" / "universal-graph.json"
LAYOUT_OUT = REPO / "app" / "data" / "universal-layout.json"

EXCERPT_LEN = 500

GRAPH_MODULES = (
    "social",
    "research",
    "nation",
    "technique",
    "epistemica",
    "nature",
)


def excerpt(text: str) -> str:
    text = " ".join((text or "").split())
    if len(text) <= EXCERPT_LEN:
        return text
    cut = text[:EXCERPT_LEN]
    space = cut.rfind(" ")
    return (cut[:space] if space > 40 else cut).rstrip() + " …"


def deep_link(source: str, node_id: str) -> str:
    if source == "nation":
        return "/nation/entry.html?code=" + quote(str(node_id), safe="")
    return "/" + source + "/?node=" + quote(str(node_id), safe="")


def load_nodes(source: str):
    data_file = REPO / "app" / source / "data" / "data.json"
    if not data_file.is_file():
        print(f"universal-index: skip {source} (no {data_file.relative_to(REPO)})")
        return []
    raw = json.loads(data_file.read_text(encoding="utf-8"))
    docs = raw if isinstance(raw, list) else raw.get("nodes", [])
    nodes = []
    for doc in docs:
        if not isinstance(doc, dict):
            continue
        if doc.get("_id") == "layout" or doc.get("type") == "layout":
            continue
        if not doc.get("id"):
            continue
        nodes.append(doc)
    return nodes


def build() -> dict:
    nodes_out = []
    counts = {}
    edge_counts = {}
    dropped_counts = {}
    seen_uids = set()

    for source in GRAPH_MODULES:
        raw_nodes = load_nodes(source)
        # uid namespace for this source (intra-dataset edge resolution)
        ids = {n["id"] for n in raw_nodes if isinstance(n.get("id"), str)}
        made = 0
        edges = 0
        dropped = 0
        for doc in raw_nodes:
            nid = doc.get("id")
            if not isinstance(nid, str):
                continue
            uid = f"{source}:{nid}"
            if uid in seen_uids:
                continue
            seen_uids.add(uid)
            tags = [t for t in (doc.get("tags") or []) if isinstance(t, str)][:5]
            refs = []
            for r in doc.get("references") or []:
                if not isinstance(r, dict):
                    continue
                title = r.get("title")
                link = r.get("link")
                if not title and not link:
                    continue
                refs.append(
                    {
                        "title": str(title or link or "")[:200],
                        "link": str(link or "")[:500],
                    }
                )
            targets = []
            for rel in doc.get("relationships") or []:
                if not isinstance(rel, dict):
                    continue
                t = rel.get("targetNodeId")
                if not isinstance(t, str) or t == nid:
                    continue
                if t in ids:
                    targets.append(f"{source}:{t}")
                    edges += 1
                else:
                    dropped += 1
            nodes_out.append(
                {
                    "uid": uid,
                    "source": source,
                    "source_id": nid,
                    "name": str(doc.get("name") or nid),
                    "category": str(doc.get("category") or doc.get("layer") or ""),
                    "layer": str(doc.get("layer") or ""),
                    "tags": tags,
                    "description": excerpt(str(doc.get("description") or "")),
                    "references": refs[:8],
                    "deep_link": deep_link(source, nid),
                    "targets": sorted(set(targets)),
                }
            )
            made += 1
        counts[source] = made
        edge_counts[source] = edges
        dropped_counts[source] = dropped

    return {
        "generated": date.today().isoformat(),
        "snapshot_source": "seed",
        "counts": counts,
        "edge_counts": edge_counts,
        "dropped_edges": dropped_counts,
        "nodes": nodes_out,
    }


def write_layout(payload: dict):
    """Compute {uid:[x,y]} with bin/layout.py machinery (no import of data)."""
    sys.path.insert(0, str(REPO / "bin"))
    import layout as layout_mod

    # layout.compute_layout needs {id, relationships:[{targetNodeId}]} rows
    rows = [
        {
            "id": n["uid"],
            "relationships": [{"targetNodeId": t} for t in n["targets"]],
        }
        for n in payload["nodes"]
    ]
    computed = layout_mod.compute_layout(rows)
    layout_mod.write_layout_atomically(computed, LAYOUT_OUT)
    return len(computed)


def main() -> int:
    payload = build()
    total = len(payload["nodes"])
    if not total:
        print("ERROR: no nodes aggregated — missing mirrors?", file=sys.stderr)
        return 1

    GRAPH_OUT.parent.mkdir(parents=True, exist_ok=True)
    GRAPH_OUT.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    laid = write_layout(payload)

    gkb = GRAPH_OUT.stat().st_size / 1024
    lkb = LAYOUT_OUT.stat().st_size / 1024
    print(
        f"universal-index: {total} nodes -> "
        f"app/data/universal-graph.json ({gkb:.0f} KB) + "
        f"app/data/universal-layout.json ({lkb:.0f} KB, {laid} positioned)"
    )
    for source in GRAPH_MODULES:
        print(
            f"  {source}: {payload['counts'].get(source, 0)} nodes, "
            f"{payload['edge_counts'].get(source, 0)} edges "
            f"({payload['dropped_edges'].get(source, 0)} dangling dropped)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
