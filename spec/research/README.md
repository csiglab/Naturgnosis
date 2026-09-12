# Research Space

> The world's research artifacts rendered as a navigable graph: the documents, books, articles,
> datasets, and reports through which research is recorded, transmitted, and reused.

## Status: bootstrapped

Explorer + editor are copies of the Social Space app (`dataset=research`). The dataset is a
hand-authored seed corpus (`app/research/data/data.json`, ~15 canonical artifacts) seeded to
CouchDB (`research:<id>` docs); the space formulation below is settled for the artifact facet.

## Formulation

> Which artifacts record and carry research? Which kinds matter, and how do they relate?

### Categories

| Category | Description | Instance |
| -------- | ----------- | -------- |
| **Book** | Extended monographic synthesis of a field or theory. | *The Structure of Scientific Revolutions* |
| **Article** | Periodical paper announcing a result or analysis. | Shannon, *A Mathematical Theory of Communication* |
| **Document** | Foundational or institutional record that shapes practice. | *Philosophical Transactions* (founding number) |
| **Dataset** | Curated, addressable body of research data. | GenBank |
| **Report** | Institutional assessment or programme output. | IPCC AR6 |

### Node specifics (`specific`)

| Field | Description |
| ----- | ----------- |
| `kind` | Finer-grained type within the category (e.g. `monograph`, `journal-article`, `reference-dataset`, `repository`, `assessment`). |
| `creators` | List of creators (authors/issuing bodies). |
| `year` | Primary publication year. |
| `venue` | Journal, publisher, or hosting institution. |
| `identifier` | Persistent identifier or canonical URL (DOI/ISBN/URL). |
| `language` | Primary language. |

### Relationship vocabulary

`CITES`, `CITED_BY`, `EXTENDS`, `DOCUMENTS` (artifact records an event/series), `PUBLISHED_IN`,
`PRECEDES`. Keep relationships sparse and evidence-backed; the seed graph carries a few small
components so the layout clusters visibly.

## Data flow

- `app/research/data/data.json` — hand-authored seed (canonical node model; `category` restricted
  to the five artifact categories above).
- `python bin/layout.py --data-file app/research/data/data.json --layout-file app/research/data/layout.json`
  regenerates the explorer layout.
- `python bin/seed_couchdb.py --dataset research` pushes nodes to CouchDB (docs keyed
  `research:<node_id>`).

## Editor / Explorer

- Explorer: `/research/` — read-only graph viewer.
- Editor: `/research/edit.html` — node editor (`const DATASET = 'research'`); syncs to CouchDB.
