# AGENTS.md — Q/A Log Space

## Purpose

Static, searchable log of the questions agents worked through (plus answers
where resolved). No graph dataset — entries render from committed JSON.
Spec: `spec/qa/README.md`.

## Layout

- `web/index.html` — catalog (full-text search, agent/run/tag facets, pagination).
- `web/entry.html?id=<qa-id>` — single Q/A viewer (question, answer, meta, prev/next).
- `data/qa.json` — source of truth: hand-normalized `[{id, question, answer, agent, run, date, source, tags, status}]`.
- `data/qa-index.json` — **generated** by `bin/build_qa_index.py`; committed but never hand-edited.
- `import/` — raw third-party log exports, archival; never edit by hand.

## Commands

```sh
python bin/build_qa_index.py    # rebuild data/qa-index.json (commit it)
python bin/sync.py --no-couch   # static smoke test: /qa/ → 200
```

## Invariants

- Not a graph dataset: no `data/data.json`, no `layout.json`, no CouchDB docs,
  invisible to seeding/layout tooling (same rule as Production Space).
- Entry ids are stable (`qa-%05d`), never reused; new imports append.
- Tokens: Oxford Common Room (`app/shared/theme.css`); inline `:root`
  blocks mirror it (graph-module precedent).
- Feed the hub universal search (`bin/build_search_index.py`) and landing
  metrics (`bin/build_landing_metrics.py`) like the note corpus.
