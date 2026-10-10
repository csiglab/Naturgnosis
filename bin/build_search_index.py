#!/usr/bin/env python3
"""
Universal search index builder (Naturgnosis hub).

Merges the notes corpus index plus a snapshot of the six graph datasets
(social owns the production nodes; production is a derived view, not a dataset)
into one committed file, app/data/search-index.json, consumed by the hub
search box (/). Stdlib only. Ported from Epistecnica's
bin/build_search_index.py; machinery only, no content carried over.

- Notes (no backend needed): trimmed to {surface, kind, type, title,
  path, tags, excerpt} so the page fetches one small file instead of the
  full-text index. Ranking beyond the excerpt stays in the note catalog;
  the universal box links out to it.
- Graph nodes: read from the committed app/*/data/data.json mirrors (the
  sync server mirrors CouchDB to these files on every save, so they are
  current enough for a build-time snapshot), trimmed to {surface,
  kind "node", type category|layer, title name, path id, excerpt
  description}. The payload records "snapshot_source": "seed" so the
  build-time nature is visible.

The notes index must exist first (make notes-index); a missing index
aborts the build with a hint. Regenerate deliberately before
build/deploy — the file is committed, like the per-corpus index.

Usage: python3 bin/build_search_index.py
"""

import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "app" / "data" / "search-index.json"

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


def load_json(path: Path, hint: str):
    if not path.is_file():
        print(f"ERROR: missing index {path} — run: {hint}", file=sys.stderr)
        raise SystemExit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def note_entries() -> list:
    idx = load_json(REPO / "app" / "note" / "data" / "index.json", "make notes-index")
    entries = []
    for n in idx.get("notes", []):
        entries.append(
            {
                "surface": "note",
                "kind": n.get("kind", "note"),
                "type": n.get("section", ""),
                "title": n.get("title", ""),
                "path": n.get("path", ""),
                "tags": n.get("tags", []),
                "excerpt": excerpt(n.get("text", "")),
            }
        )
    return entries


def qa_entries() -> list:
    path = REPO / "app" / "qa" / "data" / "qa-index.json"
    if not path.is_file():
        print(f"search-index: skip qa (no app/qa/data/qa-index.json — run: make qa-index)")
        return []
    idx = load_json(path, "make qa-index")
    entries = []
    for n in idx.get("entries", []):
        entries.append(
            {
                "surface": "qa",
                "kind": "qa",
                "type": n.get("status", ""),
                "title": n.get("question", ""),
                "path": n.get("id", ""),
                "tags": n.get("tags", []),
                "excerpt": excerpt(n.get("excerpt", "")),
            }
        )
    return entries


def glossarium_entries() -> list:
    path = REPO / "app" / "glossarium" / "data" / "index.json"
    if not path.is_file():
        print("search-index: skip glossarium (no app/glossarium/data/index.json — run: make glossarium-index)")
        return []
    idx = load_json(path, "make glossarium-index")
    entries = []
    for t in idx.get("terms", []):
        entries.append(
            {
                "surface": "glossarium",
                "kind": "term",
                "type": "",
                "title": t.get("name", ""),
                "path": t.get("slug", ""),
                "tags": [a for a in (t.get("aliases") or []) if isinstance(a, str)][:5],
                "excerpt": excerpt(t.get("excerpt", "")),
            }
        )
    return entries


def node_entries() -> list:
    entries = []
    for surface in GRAPH_MODULES:
        data_file = REPO / "app" / surface / "data" / "data.json"
        if not data_file.is_file():
            print(f"search-index: skip {surface} (no {data_file.relative_to(REPO)})")
            continue
        raw = json.loads(data_file.read_text(encoding="utf-8"))
        docs = raw if isinstance(raw, list) else raw.get("nodes", [])
        for doc in docs:
            if not isinstance(doc, dict):
                continue
            if doc.get("_id") == "layout" or doc.get("type") == "layout":
                continue
            node = {k: v for k, v in doc.items() if k not in ("_id", "_rev")}
            if not node.get("id"):
                continue
            tags = node.get("tags") or []
            entries.append(
                {
                    "surface": surface,
                    "kind": "node",
                    "type": node.get("category") or node.get("layer") or "",
                    "title": node.get("name") or node.get("id") or "",
                    "path": node.get("id") or "",
                    "tags": [t for t in tags if isinstance(t, str)][:5],
                    "excerpt": excerpt(node.get("description") or ""),
                }
            )
    return entries


def live_entries() -> list:
    """Live-catalog items (HS, NAICS, product taxonomy, good producers).

    Each entry points at its catalog page; the hub box deep-links to the
    item (hash anchor for the shared catalog viewer, ?id= for the
    good-producers grid). Item id rides in "path", catalog page in "page".
    """
    catalogs = [
        {
            "surface": "live-hs",
            "file": REPO / "app" / "note" / "data" / "social" / "coordinator" / "product" / "hs-2022.json",
            "page": "social/coordinator/product/hs-explorer.html",
            "items": lambda raw: raw if isinstance(raw, list) else [],
            "title": lambda x: ((x.get("code") or "") + " — " + (x.get("title") or "")).strip(" — "),
            "type": lambda x: x.get("level") or "",
            "tags": lambda x: [x.get("section")] if x.get("section") else [],
            "excerpt": lambda x: x.get("description") or x.get("title") or "",
            "id": lambda x: x.get("code") or "",
        },
        {
            "surface": "live-naics",
            "file": REPO / "app" / "note" / "data" / "social" / "actor" / "action" / "activity" / "economic" / "naics-2022.json",
            "page": "social/actor/action/activity/economic/naics-explorer.html",
            "items": lambda raw: raw if isinstance(raw, list) else [],
            "title": lambda x: ((x.get("code") or "") + " — " + (x.get("title") or "")).strip(" — "),
            "type": lambda x: x.get("level") or "",
            "tags": lambda x: [t for t in (x.get("keywords") or []) if isinstance(t, str)][:5],
            "excerpt": lambda x: x.get("description") or "",
            "id": lambda x: x.get("code") or "",
        },
        {
            "surface": "live-taxonomy",
            "file": REPO / "app" / "note" / "data" / "social" / "coordinator" / "product" / "product-taxonomy.json",
            "page": "social/coordinator/product/product-taxonomy.html",
            "items": lambda raw: raw if isinstance(raw, list) else [],
            "title": lambda x: x.get("label") or x.get("id") or "",
            "type": lambda x: x.get("level") or "",
            "tags": lambda x: [x.get("hs")] if x.get("hs") else [],
            "excerpt": lambda x: x.get("desc") or "",
            "id": lambda x: x.get("id") or "",
        },
        {
            "surface": "live-gp",
            "file": REPO / "app" / "note" / "data" / "technique" / "good-producers-entries.json",
            "page": "technique/good-producers.html",
            "items": lambda raw: raw.get("entries", []) if isinstance(raw, dict) else [],
            "title": lambda x: x.get("name") or "",
            "type": lambda x: " / ".join([t for t in (x.get("kind"), x.get("role")) if t]),
            "tags": lambda x: [t for t in (x.get("kind"), x.get("role"), x.get("domain")) if t],
            "excerpt": lambda x: x.get("description") or "",
            "id": lambda x: x.get("id") or "",
        },
    ]
    entries = []
    for cat in catalogs:
        if not cat["file"].is_file():
            print(f"search-index: skip {cat['surface']} (no {cat['file'].relative_to(REPO)})")
            continue
        raw = json.loads(cat["file"].read_text(encoding="utf-8"))
        n = 0
        for x in cat["items"](raw):
            if not isinstance(x, dict):
                continue
            item_id = cat["id"](x)
            if not item_id:
                continue
            entries.append(
                {
                    "surface": cat["surface"],
                    "kind": "live-item",
                    "type": cat["type"](x),
                    "title": cat["title"](x),
                    "path": item_id,
                    "page": cat["page"],
                    "tags": cat["tags"](x),
                    "excerpt": excerpt(cat["excerpt"](x)),
                }
            )
            n += 1
        print(f"search-index: {cat['surface']}: {n} items")
    return entries


def main() -> int:
    entries = note_entries()
    entries.extend(qa_entries())
    entries.extend(glossarium_entries())
    entries.extend(node_entries())
    entries.extend(live_entries())

    counts = {}
    for e in entries:
        counts[e["surface"]] = counts.get(e["surface"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "generated": date.today().isoformat(),
                "snapshot_source": "seed",
                "counts": counts,
                "entries": entries,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )

    kb = OUT.stat().st_size / 1024
    print(f"search-index: {len(entries)} entries (seed nodes) -> app/data/search-index.json ({kb:.0f} KB)")
    for surface, count in sorted(counts.items()):
        print(f"  {surface}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
