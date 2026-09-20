# AGENTS.md — Note Space

## Purpose

Long-form markdown notes for Naturgnosis: a searchable catalog plus a
single-note reader. No graph dataset — entries render from physical files.
Spec: `spec/note/README.md`. Viewer machinery ported from Epistecnica's
note system (code only; none of its personal content).

## Layout

- `web/index.html` — catalog (search, section facets, pins, pagination).
- `web/note.html` — single-note viewer (`?n=<path>`; fetches `../notes/`).
- `web/notes.css` — markdown typography (Oxford Common Room tokens).
- `web/vendor/` — third-party `marked.min.js` (keeps upstream name).
- `notes/` — source of truth (hand-edited markdown + live HTML; kebab-case).
- `data/index.json` — **generated** by `bin/build_note_index.py`; committed
  but never hand-edited.

## Commands

```sh
python bin/build_note_index.py    # rebuild data/index.json (commit it)
python bin/sync.py                # serve + pins API (no dataset needed)
curl /note/api/pins               # pinned paths
```

## Invariants

- `notes/` is hand-edited source of truth; `data/index.json` is generated.
- Note paths are kebab-case (see `notes/readme.md`); the builder warns.
- Pins live in CouchDB doc `pins` inside the `naturgnosis` database
  (`GET/POST /note/api/pins`); the catalog hides pin UI when unreachable.
- Viewer + catalog must stay free of cross-repo residue (no Epistecnica
  brand, tokens, or content — see spec "Non-goals").
- Tokens: Oxford Common Room (`app/shared/theme.css`); inline `:root`
  blocks mirror it (graph-module precedent).
