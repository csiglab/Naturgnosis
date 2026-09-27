# AGENTS.md — Universal Index (Graphive, hub-level, read-only)

## Purpose

View-only graph aggregating all seven graph spaces (social, production, research, nation,
technique, epistemica, nature) on one canvas. No editing, no backend writes. Route `/graph/`
(served from `web/` by `bin/sync.py`'s module redirect); data is hub-level
(`app/data/universal-graph.json` + `app/data/universal-layout.json`), deliberately NOT
`app/graph/data/data.json` so the sync server never treats it as an editable dataset.

## Layout

- `web/index.html` — viewer (deck.gl renderer in `web/vendor/`, shared copies of
  `deck.min.js` + `socio-graph.js`; color groups by source space, not category).
  Boots with all spaces deselected; sidebar has Select-all / Deselect-all; search
  and `?node=` deep links auto-enable the hit's space. Corpus stats live in the
  Overview modal (bottom-right button), not the sidebar.
- `web/vendor/` — third-party/shipped renderer copies (keep names as-is).
- No `data/` directory here: nodes come from `app/data/universal-graph.json`
  (built by `bin/build_universal_index.py` from the seven `app/*/data/data.json` mirrors).

## Commands

```sh
make universal-index             # recompute graph + layout (commit both JSONs)
python bin/build_universal_index.py
python bin/sync.py --no-couch   # static smoke test: /graph/ + /data/universal-*.json → 200
```

## Invariants

- Node ids are namespaced `uid = "{source}:{id}"` (26 raw collisions exist, e.g. `N1`
  social↔production) — never match on bare `id` here.
- Edges are intra-dataset only; dangling targets are dropped at build time (see
  `dropped_edges` in the JSON) — the viewer never resolves cross-dataset links.
- Minimal record per node: name, source, category/layer, tags, description excerpt,
  references `[{title, link}]`, `deep_link` (`/{source}/?node={id}`, nation →
  `/nation/entry.html?code={id}`). Full text lives in the source space.
- `app/data/universal-*.json` are generated — never edit by hand (rebuild).
