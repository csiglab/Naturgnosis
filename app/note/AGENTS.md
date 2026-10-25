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
  with the generated `index.json` beside it. Top-level sections include
  `nature/` (natural elements; the Modelo import is mirrored under
  `nature/conceptual-model-natural-system/`, and `nature/construction/` holds
  epistemic constructions about natural targets), `human/`, `miscellanea/`,
  `data-collection/`, plus the pre-existing `social/`, `technique/`,
  `epistemica/`, `history/`, `general/`, and `meta/` sections.
- `data/index.json` — **generated** by `bin/build_note_index.py`; gitignored,
  never hand-edited, never committed.
- `data/backlinks.json` — **generated** by `bin/build_note_index.py`
  (`{target: [{path, title}]}` for cited notes only, from inline
  `note.html?n=` body links); gitignored, never hand-edited. Powers the
  cited-by chip in `web/note.html`.
- `data/links.json` — the single hand-maintained support-links registry
  (`{from, to, label, kind}` directed pairs; endpoints are note paths,
  `dir/` scopes, or `{EPISTENICA}/...` external targets with
  `kind: "external"`). External cards show the resolved route on hover and
  resolve the base from `EPISTENICA_URL` via `GET /note/api/config`; unset
  means disabled. The builder validates
  and embeds it into `index.json`; rebuild the index after editing
  links (the index itself stays gitignored).
- `data/pins.json` is the committed local mirror of the CouchDB `pins` doc
  (server-written; never hand-edit). Until the server writes it directly,
  keep it in sync via the `/tmp` pins script; rebuild/commit it after any
  pin change like `index.json`.
- `data/changelog.json` (+ `changelog.schema.json`) — hand-edited per-file
  edit history for markdown notes; agents append one entry per touched
  `data/**/*.md` file per change set (see Invariants).

## Commands

```sh
python bin/build_note_index.py    # rebuild data/index.json (gitignored)
python bin/sync.py                # serve + pins API (no dataset needed)
curl /note/api/pins               # pinned paths
```

## Invariants

- `data/` holds the hand-edited corpus; `data/index.json` is generated.
- Do not create `app/note/import/`; third-party material is integrated as
  normalized notes and assets under `data/`.
- Schema-backed JSON in the corpus keeps its object key order identical to the
  corresponding schema's `properties` order; reorder the schema first, then
  conform the data (e.g. `data/social/state/action/atlas/atlas.json` follows
  its `atlas.schema.json`).
- Note paths are kebab-case, Epistecnica slug rule (see
  `spec/note/authoring.md`
  and `bin/build_note_index.py:slugify_segment()`); the builder warns with
  the suggested form. Never run `bin/slugify_files.py` (underscore rule) here.
- Filing vs typing: an epistemic construction about a natural target — a
  model, law, representation, or dataset describing something in nature —
  fill it under (`nature/construction/`).
- Per-file edit history lives in `data/changelog.json` (array of
  `{file_path, logs[]}` over markdown notes only; object key order follows
  `changelog.schema.json`). Every agent change set touching `data/**/*.md`
  appends one log per file (`{date: YYYY-MM-DD, summary; optional kind}`).
  The index builder ignores `*.json`, so changelog edits need no index rebuild.
- When committing changed notes, every touched `data/**/*.md` file must
  already be reflected in `data/changelog.json` in the same commit:
  compare the staged file list against changelog `file_path` entries and
  append any missing logs before committing.
- Commit links are filled **post-commit**: the introducing sha is unknowable
  when the entry is authored. After the change-set commit, run
  `python bin/link_changelog_commits.py` to stamp `commit` (and `before` when
  the note existed at the parent) on the logs it introduced, then commit the
  json-only annotation. Entries without these fields render plain; see
  `spec/note/authoring.md`.
- Note paths keyed by country use ISO 3166-1 alpha-3, lowercase
  (`social/actor/public/catalog/research/usa/…`, `social/actor/public/polity/grc/region/…`); never alpha-2
  or country names. Entities without an alpha-3 code (devolved nations,
  defunct states) are explicit exceptions.
- Tags are optional `--- tags: [...]` front matter; `data/index.json`
  carries them and feeds the hub universal search (`bin/build_search_index.py`).
- Reference links are bare `[Name](target)` with no trailing parenthetical
  description; for external links `Name` is the entry title derived from
  the URL. Put any gloss in the surrounding prose, never after the link.
  Applies to newly added links; existing corpus links are left as-is.
- Pins live in CouchDB doc `pins` inside the `naturgnosis` database
  (`GET/POST /note/api/pins`); the catalog hides pin UI when unreachable.
- Viewer + catalog must stay free of cross-repo residue (no Epistecnica
  brand, tokens, or content — see spec "Non-goals").
- Tokens: Oxford Common Room (`app/shared/theme.css`); inline `:root`
  blocks mirror it (graph-module precedent).
