# Glossarium Space

> The lexical corpus behind Naturgnosis — terms and definitions behind the ontologies,
> indexed and served at `/glossarium/`, with select-a-word lookup on the note pages.

## Status: seeded

Viewer machinery ported from Epistecnica's glossarium system (code only); the
term corpus was then imported from Epistecnica under explicit intent
(`app/glossarium/data/terms.json`, 317 terms) and scrubbed of brand references.
This supersedes the earlier "code only, corpus empty" state.

## Storage model

- **Source of truth: `app/glossarium/data/terms.json`** — a hand-maintained array of
  `{slug, name, aliases, body}` entries (`body` = full markdown, original case/formatting).
  Add or replace a term from a markdown file with
  `python bin/add_glossarium_term.py <file.md> [--slug <code>]` (name from the first
  `# ` heading, `aliases: [...]` front matter, the rest as body) — or edit the JSON directly.
  There are no per-term `.md` files in the module.
- **Derived:** `app/glossarium/data/index.json`, generated from `terms.json` by
  `bin/build_glossarium_index.py` (slug, name, aliases, excerpt, lowercased plain text,
  word count). Powers the catalog, the search/facets, the select-a-word popup, and the hub
  universal search (`bin/build_search_index.py` → `app/data/search-index.json`); the corpus
  count also feeds the landing metrics (`bin/build_landing_metrics.py`). Committed so the
  module works without any backend; rebuild and commit it after any term change.
- **Not a graph dataset.** The glossarium module carries no `data/data.json`,
  needs no CouchDB dataset, and is invisible to seeding/layout tooling.

## UI

- **Catalog** `app/glossarium/web/index.html` — search, letter facets, pagination, stats
  (terms/aliases/words); loads `../data/index.json`.
- **Term view** `?t=<slug>` — looks the slug up in `../data/terms.json` and renders the
  `body` via vendored `marked`, alias chips, breadcrumb back to the catalog.
- **Select-a-word lookup** `app/glossarium/web/js/glossarium-lookup.js` — included by the
  glossarium page (`data-glossarium="../data/index.json"`) and the note pages
  (`data-glossarium="../../glossarium/data/index.json"`). Lazy-loads the index on first
  text selection; matches exact → alias → plural fallback; floating definition card links
  to the full term. Index paths stay relative (prefix-mount contract).

## Operations

```sh
python bin/add_glossarium_term.py path/to/term.md   # add/replace one term (then:)
python bin/build_glossarium_index.py                # rebuild index.json from terms.json
python bin/build_search_index.py                    # rebuild the hub universal index
```

## Conventions

- Slug (term code) is kebab-case (ASCII lowercase, `-` separated, accent-folded); it keys
  the `terms.json` entry and the `?t=<slug>` URL. The human term lives in `name` (from the
  first `# ` heading), never in the file name. The importer rejects non-kebab slugs.
- Optional aliases in the entry's `aliases` list (from `aliases: [...]` front matter when
  importing).
- English preferred; keep original-language terms as aliases in `aliases` or the body.

## Non-goals

- No Epistecnica brand in the imported corpus (verified by grep); provenance comments in
  code and these docs are the documented exception.
