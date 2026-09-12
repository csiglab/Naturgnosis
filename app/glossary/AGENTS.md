# AGENTS.md — Glossary

## Purpose

The vocabulary of Naturgnosis: one markdown file per term, with an entry index and client-side search.
Spec: `spec/glossary/README.md`.

## Layout

- `entries/` — **source of truth** (`<Term>.md`; collision suffixes `-2`, `-3` until merged).
- `data/index.json` — **generated** by `bin/build_glossary_index.py`; committed but never hand-edited.
- `web/index.html` — index + search + reader (renders entries with a minimal markdown renderer).
- `import/` — raw Notion exports (CSV); archival.

## Commands

```sh
python bin/build_glossary_index.py    # regenerate data/index.json (commit it)
```

## Invariants

- Storage is physical markdown — not CouchDB. Do not introduce a second source of truth.
- After adding/renaming entries, rebuild the index and commit both.
- New UI must use `/shared/theme.css` tokens.
