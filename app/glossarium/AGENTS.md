# AGENTS.md — Glossarium Space

## Purpose

Lexical corpus for Naturgnosis: terms and definitions behind the ontologies, as a searchable
catalog plus a single-term reader, with select-a-word lookup on the note pages. No graph
dataset — entries render from physical files.
Spec: `spec/glossarium/README.md`. Viewer machinery ported from Epistecnica's
glossarium system; the term corpus was imported from there under explicit intent.

## Layout

- `web/index.html` — catalog (search, letter facets, pagination) + term view (`?t=<slug>`,
  looks the slug up in `../data/terms.json` and renders `body` via vendored `marked`, alias
  chips; no per-term `.md` fetch).
- `web/glossarium.css` — markdown typography (Oxford Common Room tokens).
- `web/js/glossarium-lookup.js` — select-a-word popup (also wired into the note pages via
  `data-glossarium`; index path stays relative per the prefix-mount contract).
- `web/vendor/` — third-party `marked.min.js` (keeps upstream name).
- `data/terms.json` — **source of truth**: hand-maintained `[{slug, name, aliases, body}]`,
  committed; add/replace entries with `bin/add_glossarium_term.py` (or edit by hand).
- `data/index.json` — **generated** from `terms.json` by `bin/build_glossarium_index.py`
  (slug/name/aliases/excerpt/text/words); committed but never hand-edited.

## Commands

```sh
python bin/add_glossarium_term.py path/to/term.md [--slug <code>]  # add/replace one term
python bin/build_glossarium_index.py  # rebuild data/index.json from data/terms.json (commit it)
python bin/sync.py --no-couch         # static smoke test: /glossarium/ → 200
```

## Invariants

- `data/terms.json` is the term source of truth; `data/index.json` is generated from it.
- Term bodies are served from `data/terms.json` keyed by slug (the term code); there are
  no per-term `.md` files in the module.
- Term slugs are kebab-case, Epistecnica slug rule (accent-folded, lowercase, runs of
  non-alphanumerics to `-`); the builder warns with the suggested form. Never run
  `bin/slugify_files.py` (underscore rule) here.
- Terms carry the name in the first `# ` heading; optional `aliases: [...]` front matter
  lists alternative spellings and translations used by the lookup.
- Not a graph dataset: no `data/data.json`, no `layout.json`, no CouchDB docs,
  invisible to seeding/layout tooling (same rule as Note Space and Q/A Log).
- Viewer + catalog must stay free of cross-repo residue (no Epistecnica
  brand or tokens in the corpus; provenance comments in code/docs are the
  documented exception — see spec "Non-goals").
- Tokens: Oxford Common Room (`app/shared/theme.css`); inline `:root`
  blocks mirror it (graph-module precedent).
- Feed the hub universal search (`bin/build_search_index.py`) and landing
  metrics (`bin/build_landing_metrics.py`) like the note corpus.
