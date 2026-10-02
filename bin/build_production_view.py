#!/usr/bin/env python3
"""
Production derived-view builder (Naturgnosis).

Production Space is not a dataset: its nodes live in Social Space, marked with
the reserved `production-view` tag when they play a production role (see
"Derived views" in guideline/README.md). This script computes the view:

    app/social/data/data.json  ->  app/production/data/view.json
                                   app/production/data/view-layout.json

Full node records are copied verbatim (ids unchanged, so ?node= deep links keep
working); only edges with both ends in the view are kept, the rest are dropped
and counted. Layout uses the bin/layout.py machinery. Stdlib only.

Usage: python3 bin/build_production_view.py  (or: make production-view)
"""

import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "app" / "social" / "data" / "data.json"
VIEW_OUT = REPO / "app" / "production" / "data" / "view.json"
LAYOUT_OUT = REPO / "app" / "production" / "data" / "view-layout.json"

TAG = "production-view"


def main() -> int:
    if not SRC.is_file():
        print(f"ERROR: missing social mirror {SRC.relative_to(REPO)}", file=sys.stderr)
        return 1
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    docs = raw if isinstance(raw, list) else raw.get("nodes", [])

    in_view = [n for n in docs
               if isinstance(n, dict) and n.get("id")
               and TAG in [str(t).strip().lower() for t in (n.get("tags") or [])]]
    ids = {n["id"] for n in in_view}

    kept_edges = dropped_edges = 0
    for n in in_view:
        kept = []
        for r in n.get("relationships") or []:
            if not isinstance(r, dict):
                continue
            t = r.get("targetNodeId")
            if t == n["id"]:
                continue
            if t in ids:
                kept.append(t)
                kept_edges += 1
            else:
                dropped_edges += 1
        n["_view_targets"] = sorted(set(kept))

    payload = {
        "generated": date.today().isoformat(),
        "snapshot_source": "seed",
        "source_dataset": "social",
        "tag": TAG,
        "node_count": len(in_view),
        "edge_count": kept_edges,
        "dropped_edges": dropped_edges,
        "nodes": in_view,
    }
    VIEW_OUT.parent.mkdir(parents=True, exist_ok=True)
    VIEW_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")

    sys.path.insert(0, str(REPO / "bin"))
    import layout as layout_mod
    rows = [{"id": n["id"],
             "relationships": [{"targetNodeId": t} for t in n.pop("_view_targets")]}
            for n in in_view]
    computed = layout_mod.compute_layout(rows)
    layout_mod.write_layout_atomically(computed, LAYOUT_OUT)

    gkb = VIEW_OUT.stat().st_size / 1024
    lkb = LAYOUT_OUT.stat().st_size / 1024
    print(f"production-view: {len(in_view)} nodes, {kept_edges} edges "
          f"({dropped_edges} dangling dropped) -> "
          f"app/production/data/view.json ({gkb:.0f} KB) + "
          f"app/production/data/view-layout.json ({lkb:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
