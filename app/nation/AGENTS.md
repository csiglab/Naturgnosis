# AGENTS.md — Nation Space

## Purpose

Graph of the world's nations: states, territories, institutions, peoples, and the relations between
them. Bootstrapped from an external dataset (see `import/`). Spec: `spec/nation/README.md`.

> **Depleted.** The `nation` graph dataset was dissolved: its nodes now live as per-polity node
> files under the note corpus (`social/collective/actor/public/polity/<code>/data/node.json`), which are the
> source of truth (see `spec/polity/README.md`). There is no `app/nation/data/data.json` and no
> CouchDB `dataset=nation`; the remaining `web/` pages are legacy and no longer have data.

## Layout

- `web/index.html` — legacy nations index (broken: reads the dissolved `data/data.json`).
- `web/entry.html` — legacy nation entry page (broken, same reason).
- `web/rep/actor.html` — Actor Space representation (`?code=<iso>`; fetches the polity
  dataset first (`polity/<code>/data/actors.json`), falls back to `data/actors/<iso>.json`).
- Polity corpus aggregator — live note `social/collective/actor/public/polity/index.html` in the note
  corpus (flag grid + nation search; each flag opens its `polity/<code>/index.html` page;
  `?code=<iso>` prefills the search; data from sibling `polity/data.json`, rebuilt with
  `make polity-index`).
- `web/pending.html` — themed placeholder for pending works (`?back=`).
- `web/edit.html` — legacy editor; inert (no `dataset=nation`).
- `data/actors/` — actor datasets for the codes without a polity dir (7 orphans);
  the rest live at `polity/<code>/data/actors.json` in the note corpus.
- `import/` — raw source exports (archival; never edit).

## Commands

```sh
python bin/sync.py                    # serve (nation is no longer a dataset)
make polity-index                     # rebuild the polity manifest + node-backed pages
```

## Invariants

- The public face is now the polity corpus (`/note/`); this module is legacy.
- Dark mode uses the global Oxford Common Room scheme (`/shared/theme.css`); the toggle's light
  mode is the parchment companion documented in `spec/theme/README.md`. Theme persists under the
  global `localStorage` key `naturgnosis-theme` (default dark).
