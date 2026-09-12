# AGENTS.md — Social Space (main module)

## Purpose

The core Naturgnosis space: an ontic–agentic–epistemic graph of social reality (actors, institutions,
roles, norms, beliefs, relationships) with a read-only explorer and a full editor.
Spec: `spec/social/README.md`.

## Layout

- `web/index.html` — explorer (deck.gl renderer in `web/vendor/`).
- `web/edit.html` — editor (`const DATASET = 'social'`).
- `data/data.json` — server-written mirror; `data/layout.json` — precomputed layout.
- `data/schema/` — JSON Schema + `notes` context used by the editor.
- `view/` — long-form markdown notes for actors (seed corpus; also feeds Research Space).

## Commands

```sh
python bin/sync.py                    # serve + CouchDB sync (dataset=social)
python bin/sync.py --no-couch         # static-only
curl /api/graph?dataset=social        # nodes
```

## Invariants

- Dataset id is `social` — appears in `web/edit.html`, CouchDB keys (`social:<node>`), API calls.
- `data/data.json` is server-written: pull from the server before committing manual edits.
- `index.html` and `edit.html` share the inline `:root` tokens; keep identical to
  `app/shared/theme.css`.
- `view/` notes describe social actors; do not mix in production/research content.
