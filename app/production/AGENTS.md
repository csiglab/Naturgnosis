# AGENTS.md — Production Space

## Purpose

Coarse-grained graph of the production sphere: techniques, products (raw, intermediate, final,
services), firms, processes, and enabling capabilities. Spec: `spec/production/README.md`.
Fine-grained technique belongs to `app/technique/` — keep the boundary.

## Layout

- `web/index.html` — explorer; `web/edit.html` — editor (`const DATASET = 'production'`).
- `data/data.json` — server-written mirror; `data/layout.json` — precomputed layout.
- `data/schema/` — JSON Schema + notes (production-specific `specific` vocabulary, e.g.
  `artifactType`).

## Commands

```sh
python bin/sync.py                    # serve + CouchDB sync (dataset=production)
curl /api/graph?dataset=production    # nodes
```

## Invariants

- Dataset id is `production` — appears in `web/edit.html`, CouchDB keys, API calls.
- `data/data.json` is server-written: pull from the server before committing.
- Keep `web/` in sync with the other graph modules for shared behavior.
