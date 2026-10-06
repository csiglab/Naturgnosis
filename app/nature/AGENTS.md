# AGENTS.md — Nature Space

## Purpose

The space of nature: physical and living phenomena that exist independently of inquiry —
the ontic counterpart to Epistemic Space's scaffolding. Seeded with the ontic nodes moved
out of `epistemica` (`em-wave-ontic-001`, `process_decision_making`) plus stubs resolving
their edges. Spec: `spec/nature/README.md`.

## Layout

- `web/index.html` — explorer; `web/edit.html` — editor (`const DATASET = 'nature'`).
- `web/vendor/` — shipped renderer copies (`deck.min.js`, `socio-graph.js`; keep names as-is).
- `data/data.json` — server-written mirror (seed: 2 moved nodes + 3 `*-ontic-001` stubs);
  `data/layout.json` — precomputed layout.
- `data/schema/` — JSON Schema + `notes` context, copied from epistemica at bootstrap.

## Commands

```sh
python bin/sync.py                    # serve (dataset=nature is auto-discovered)
python bin/seed_couchdb.py --dataset nature   # push seed into CouchDB
curl /api/graph?dataset=nature        # nodes
```

## Invariants

- Dataset id is `nature` — appears in `web/edit.html`, CouchDB keys (`nature:<node>`), API calls.
- `data/data.json` is server-written: pull from the server before committing manual edits.
- Moved-from-epistemica provenance is recorded in each moved node's
  `metadata.auditTrail` (the `import/` archives stay untouched).
- The web app is a copy of the epistemica one: propagate shared fixes from the other
  graph modules.
