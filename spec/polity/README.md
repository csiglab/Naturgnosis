# Polity Pages

Per-nation hub pages for the polity corpus (`app/note/data/social/collective/actor/public/polity/<code>/`),
ported from the nation module's views and hydrated at runtime.

## Layout

- `entry.html` — canonical entry original (ports `app/nation/web/entry.html`:
  flag hero, statistics, works, references, footer). Stamped to every
  `polity/<code>/` as `index.html`.
- `actor.html` — canonical actor original (ports `app/nation/web/rep/actor.html`:
  actor-evolution timeline, metadata injection). Stamped to the 30 codes with
  a same-code actor dataset as `actor.html`.
- Runtime behavior lives in shared scripts (`app/shared/polity-entry.js`,
  `app/shared/polity-actors.js`); CSS is inline in the originals. Never edit
  a stamped copy — edit the original and rebuild (`make polity-index`).

## View propagation

`spec/polity/{entry,actor}.html` are the canonical origins; the per-code
`polity/<code>/index.html` and `polity/<code>/actor.html` are copies (never
hand-edited). Only `<title>` is baked per code; bodies stay identical to the
originals. Two entry points:

- `make polity-views` — copy the canonical views to their per-code
  destinations only (`bin/build_polity_index.py --views-only`); no manifest
  rewrite. Use this when you have finished editing the canonical views.
- `make polity-index` — rebuild the manifest (`polity/data.json`) **and**
  copy the views.

The root aggregator (`polity/index.html`) is hand-maintained and is **not**
part of this canonical/copy scheme.

## Data

Each `polity/<code>/` carries its own data under `data/`; the views read
relative `data/` paths only:

- `data/node.json` — the polity's node (identity, statistics, references,
  footer). **Source of truth** (the nation dataset mirror was dissolved into
  these files; codes without a directory keep `polity/<iso>-node.json` at the
  root). Hand-edited.
- `data/actors.json` — the polity's actor dataset (moved from
  `app/nation/data/actors/`; 7 codes without a polity dir keep theirs there).

### Works (derived)

A polity's `works` (the "Representation & Explanation" grid) are **not**
stored in `node.json`; the builder recomputes them from the directory on every
`make polity-index`:

- every representation (`.html`) and explanation (`.md`) in the dir becomes a work;
- `type` by convention on the name (`bin/build_polity_index.py:work_type()`):
  keyword match -> `Network` / `Spatial` / `Temporal` (default `Temporal`);
  explanations are always `note`;
- `status` is direct: a derived work always has a backing file, so `active`;
- `link` is polity-relative (`actor.html`) for representations, a note-viewer
  URL for explanations.

Optional manual type overrides: `polity/dynamics.json`
(`{"social/collective/actor/public/polity/arg/actor.html": {"type": "Spatial"}}`).

## Contract

- The shared scripts derive `<code>` from the page URL (`/polity/<code>/`,
  `?code=` fallback) and hydrate from the per-dir node (`data/node.json`,
  relative path; falls back to the manifest entry when absent) plus the
  sibling manifest (`../data.json`).
- The header identity hydrates at runtime: the brand (logo + "Naturgnosis")
  links to the polity index (`polity/index.html`), and the subtitle carries
  the polity's country name and links to its notes directory view
  (`/note/web/index.html?dir=social/collective/actor/public/polity/<code>`).
- Only `<title>` is baked per code at stamp time (catalog discovery); bodies
  stay identical to the originals.
- Static links must stay checker-clean (`bin/check_note_links.py`) for depth
  `polity/<code>/`: viewer/catalog links use the `../../../../../../web/`
  prefix, cross-module links use absolute served paths.
- Stamped `index.html` files are skipped by the manifest builder (chrome, not
  content); stamped `actor.html` files classify as representations.
