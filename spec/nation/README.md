# Nation Space

> The world's nations rendered as a navigable graph: states, territories, institutions, peoples,
> economies, and the relations between them.

## Status: depleted (superseded by the polity corpus)

The `nation` graph dataset was **dissolved**: each node now lives as a per-polity node file under
the note corpus (`app/note/data/social/actor/public/polity/<code>/data/node.json`), which is the
source of truth (see `spec/polity/README.md`). There is no `app/nation/data/data.json` and no
CouchDB `dataset=nation`; the module's `web/` pages are legacy. The space formulation below is
retained for reference.

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

Polity, Nation (people), Territory, Border, Constitution, Government, Administrative
Division, Language, Currency, Treaty, Alliance, Disputed Territory.

## Sources

- Index Gentium (`csiglab/research-CountryIndex`) — country catalog work; natural seed corpus.
- Actor notes under `app/note/data/social/actor/` (states, central banks, ministries).


## Data provenance

Bootstrapped from **Index Gentium (research-CountryIndex)** and extended in-repo with hand-authored entries. Raw exports are archival in `app/nation/import/` (provenance only). The dataset was dissolved into per-polity node files under the note corpus; those files are now the source of truth.

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
  search). Present for 8 countries (chn, hkg, ind, irl, mys, nzl, tha, vnm); datasets live as
  `polity/<code>/data/actors.json` in the note corpus (7 codes without a polity dir keep
  `data/actors/<iso>.json`; e.g. Ireland: 645 actors, 1700–2025).
- **Polity Index** `social/actor/public/polity/index.html` (note corpus live note) — flag-grid
  aggregator over the per-nation polity corpus (`polity/<code>/` holds each polity's
  representations (HTML) and explanations (markdown); `?code=<iso>` preselects one polity).
  Data comes from the sibling `polity/data.json` manifest (`make polity-index`); nation ids
  without a same-code directory stay absent (no aliasing).
- **Pending** `/nation/web/pending.html?back=…` — themed placeholder for works without a
  representation yet; honors `?back=` for the return link.
- **Editor** `/nation/edit.html` — legacy editor; inert (no `dataset=nation`).
- The graph explorer was removed. With the dataset dissolved, the module's `web/` pages are
  legacy; the polity corpus (`/note/`) is the public face.
- Works `link` values target the ported pages (`rep/actor.html?code=…`, `pending.html?back=…`).

Legacy entries rendered from the (now dissolved) `data/data.json`; the polity corpus is the
source of truth (`spec/polity/README.md`).
