# Nation Space

> The world's nations rendered as a navigable graph: states, territories, institutions, peoples,
> economies, and the relations between them.

## Status: bootstrapped

The module is scaffolded from the Social Space app (explorer + editor, `dataset=nation`) with an
empty dataset. The space formulation below is the working agenda.

## Formulation

> Which are the set of concepts useful to describe nations? Which are the main categories?

### Candidate layers

| Layer | Core question |
| ----- | ------------- |
| Territorial | What ground does the nation hold? (territory, borders, waters, claims) |
| Institutional | How is it organized? (constitution, government, branches, subdivisions) |
| Demographic | Who composes it? (nations-as-peoples, languages, religions, migration) |
| Economic | What does it produce and exchange? (currency, trade, resources, fiscal system) |
| Sovereign | How does it relate to others? (recognition, treaties, alliances, conflicts) |

### Candidate categories

Nation-State, Nation (people), Territory, Border, Constitution, Government, Administrative
Division, Language, Currency, Treaty, Alliance, Disputed Territory.

## Sources

- Index Gentium (`csiglab/research-CountryIndex`) — country catalog work; natural seed corpus.
- Actor notes under `app/social/view/actor/` (states, central banks, ministries).


## Data provenance

Bootstrapped from **Index Gentium (research-CountryIndex)**: 17 nodes, extended in-repo with hand-authored entries (now 34). Raw exports are archival in `app/nation/import/`; regenerate `data/data.json` with `bin/import_nation.py` (reads only from `import/`). After edits in the app, the sync server owns `data.json` — do not re-run the import over editor work.

## UI

The nation module is a **faithful port of Index Gentium** (research-CountryIndex): the source
stylesheet and Tailwind configuration are carried over verbatim (see `spec/theme` for the variant
notes and its CDN dependency).

- **Index** `/nation/` — institutional hero, search, region tag filters, country card grid
  (flag, name, native name, tags, definition), pagination, institutional footer.
- **Entry** `/nation/entry.html?code=<iso>` — flag hero with name/native name/tags, definition
  lead, diamond dividers, "Overview" `data-card`s with `data-indicator` fill bars, and
  "Representation & Explanation" `entity-card` works (type icon, Active/Pending status badge,
  "Coming MMXXV" CTA when the work has no link) — e.g. *Actor Set Evolution* — with the
  breadcrumb back to the index.
- **Actor Space** `/nation/web/rep/actor.html?code=<iso>` — faithful port of the source's
  Actor Set Evolution representation (timeline of actors, type filters private/hybrid/public,
  search). Present for 8 countries (chn, hkg, ind, irl, mys, nzl, tha, vnm); datasets ship as
  `data/actors/<iso>.json` (e.g. Ireland: 645 actors, 1700–2025).
- **Pending** `/nation/web/pending.html?back=…` — themed placeholder for works without a
  representation yet; honors `?back=` for the return link.
- **Editor** `/nation/edit.html` — graph node editor; syncs to CouchDB `dataset=nation`.
- The graph explorer was removed: the catalog + editor cover the module's needs.
- Works `link` values are rewritten on import (`bin/import_nation.py`) to target the ported
  pages (`rep/actor.html?code=…`, `pending.html?back=…`).

Entries render from `data/data.json` alone (web + json only in the deployed image).
