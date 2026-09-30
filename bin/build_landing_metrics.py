"""Build landing-page metrics: per-module node/edge counts baked at build time.

Reads graph mirrors + notes index, writes committed app/data/landing-metrics.json
(fetched by app/index.html; renders em-dash when absent).
Stdlib only. Never fails the build: missing inputs degrade to nulls.
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "app", "data", "landing-metrics.json")

GRAPH_MODULES = ("social", "research", "nation", "technique", "epistemica", "nature")


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def count_graph(mod):
    data = load_json(os.path.join(ROOT, "app", mod, "data", "data.json"))
    if not isinstance(data, list):
        return {"nodes": None, "edges": None}
    edges = sum(len(n.get("relationships", []) or []) for n in data
                if isinstance(n, dict))
    return {"nodes": len(data), "edges": edges}


def main():
    modules = {m: count_graph(m) for m in GRAPH_MODULES}

    view = load_json(os.path.join(ROOT, "app", "production", "data", "view.json"))
    if isinstance(view, dict):
        view = view.get("nodes", view)
    modules["production"] = {
        "nodes": len(view) if isinstance(view, list) else None,
        "edges": (sum(len(n.get("relationships", []) or []) for n in view
                       if isinstance(n, dict))
                  if isinstance(view, list) else None),
    }

    notes = load_json(os.path.join(ROOT, "app", "note", "data", "index.json"))
    modules["note"] = {
        "nodes": (notes.get("count")
                  if isinstance(notes, dict) and isinstance(notes.get("count"), int)
                  else (len(notes.get("notes", [])) if isinstance(notes, dict) else None)),
        "edges": None,
    }

    qa = load_json(os.path.join(ROOT, "app", "qa", "data", "qa-index.json"))
    modules["qa"] = {
        "nodes": (qa.get("count")
                  if isinstance(qa, dict) and isinstance(qa.get("count"), int)
                  else (len(qa.get("entries", [])) if isinstance(qa, dict) else None)),
        "edges": None,
    }

    payload = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "modules": modules,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    shown = ", ".join(
        f"{m}={v['nodes']}" for m, v in modules.items())
    print(f"landing-metrics: {shown} -> app/data/landing-metrics.json")


if __name__ == "__main__":
    main()
