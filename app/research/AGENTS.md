# AGENTS.md — Research Space

## Purpose

Graph of the world's research artifacts: the books, articles, documents, datasets, and reports
through which research is recorded, transmitted, and reused. Bootstrapped from a hand-authored
seed corpus. Spec: `spec/research/README.md`.

## Layout

- `web/index.html` — explorer; `web/edit.html` — editor (`const DATASET = 'research'`).
- `data/data.json` — server-written mirror; seed corpus is hand-authored (categories: Book,
  Article, Document, Dataset, Report — see spec for `specific` fields and relationship vocab).
- `data/layout.json` — pre-computed layout (regenerate with `bin/layout.py`).
- `data/schema/` — node schema (artifact categories).

## Commands

```sh
python bin/sync.py                    # serve (dataset=research is auto-discovered)
python bin/layout.py --data-file app/research/data/data.json --layout-file app/research/data/layout.json
python bin/seed_couchdb.py --dataset research
curl /api/graph?dataset=research      # nodes
```

## Invariants

- Dataset id is `research`.
- The web app is a copy of the social one: propagate shared fixes from the other graph modules.
- `category` values come from the spec's artifact vocabulary; keep the seed corpus curated (no
  bulk imports without an `import/` workflow).
