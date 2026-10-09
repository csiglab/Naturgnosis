# AGENTS.md — Note Space

## Purpose

Long-form markdown notes for Naturgnosis: a searchable catalog plus a
single-note reader. No graph dataset — entries render from physical files.
Spec: `spec/note/README.md`. Viewer machinery ported from Epistecnica's
note system (code only; none of its personal content).

## Layout

- `web/index.html` — catalog (search, section facets, tag facets, pins, pagination).
- `web/note.html` — single-note viewer (`?n=<path>`; fetches `../data/`; strips `--- tags` front matter, renders tag chips).
- `web/notes.css` — markdown typography (Oxford Common Room tokens).
- `web/vendor/` — third-party `marked.min.js` (keeps upstream name).
- `data/` — the corpus home: hand-edited markdown + live HTML (kebab-case),
  with the generated `index.json` beside it.
- `data/index.json` — **generated** by `bin/build_note_index.py`; committed
  but never hand-edited.
- `data/pins.json` is the committed local mirror of the CouchDB `pins` doc
  (server-written; never hand-edit). Until the server writes it directly,
  keep it in sync via the `/tmp` pins script; rebuild/commit it after any
  pin change like `index.json`.

## Commands

```sh
python bin/build_note_index.py    # rebuild data/index.json (commit it)
python bin/sync.py                # serve + pins API (no dataset needed)
curl /note/api/pins               # pinned paths
```

## Invariants

- `data/` holds the hand-edited corpus; `data/index.json` is generated.
- Schema-backed JSON in the corpus keeps its object key order identical to the
  corresponding schema's `properties` order; reorder the schema first, then
  conform the data (e.g. `data/social/state/action/atlas/atlas.json` follows
  its `atlas.schema.json`).
- Note paths are kebab-case, Epistecnica slug rule (see
  `spec/note/authoring.md`
  and `bin/build_note_index.py:slugify_segment()`); the builder warns with
  the suggested form. Never run `bin/slugify_files.py` (underscore rule) here.
- Note paths keyed by country use ISO 3166-1 alpha-3, lowercase
  (`social/actor/research/usa/…`, `social/state/space/grc/region/…`); never alpha-2
  or country names. Entities without an alpha-3 code (devolved nations,
  defunct states) are explicit exceptions.
- Tags are optional `--- tags: [...]` front matter; `data/index.json`
  carries them and feeds the hub universal search (`bin/build_search_index.py`).
- Pins live in CouchDB doc `pins` inside the `naturgnosis` database
  (`GET/POST /note/api/pins`); the catalog hides pin UI when unreachable.
- Viewer + catalog must stay free of cross-repo residue (no Epistecnica
  brand, tokens, or content — see spec "Non-goals").
- Tokens: Oxford Common Room (`app/shared/theme.css`); inline `:root`
  blocks mirror it (graph-module precedent).
