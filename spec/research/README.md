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
| **Document** | Foundational, institutional, or archival record that shapes practice. | *Philosophical Transactions* (founding number); AGI *Relación de méritos y servicios* |
| **Dataset** | Curated, addressable body of research data. | GenBank |
| **Report** | Institutional assessment or programme output. | IPCC AR6 |

### Node specifics (`specific`)

| Field | Description |
| ----- | ----------- |
| `kind` | Finer-grained type within the category (e.g. `monograph`, `journal-article`, `reference-dataset`, `repository`, `assessment`, `reference-work`, `archival-record`). |
| `creators` | List of creators (authors/issuing bodies). |
| `year` | Primary publication year. |
| `venue` | Journal, publisher, or hosting institution. |
| `identifier` | Persistent identifier or canonical URL (DOI/ISBN/URL). |
| `language` | Primary language. |

### Relationship vocabulary

`CITES`, `CITED_BY`, `EXTENDS`, `DOCUMENTS` (artifact records an event/series), `PUBLISHED_IN`,
`PRECEDES`. Keep relationships sparse and evidence-backed; the seed graph carries a few small
components so the layout clusters visibly.

### Title format (APA)

`name` — rendered as the detail-panel title (`.dp-title` in `web/index.html`) — is a
single-line APA 7th-edition reference-list entry, regenerated from the source record's
structured fields (never copied verbatim from hand-written headings). Templates:

| Kind | Template | Example |
| ---- | -------- | ------- |
| `journal-article` | Author, A. A., & Author, B. B. (Year). Sentence case title. Journal Name, Vol(No), pp–pp. | Aalbersberg, I. J., & Rozenberg, G. (1988). Theory of traces. Theoretical Computer Science, 60(1), 1–82. |
| `monograph` | Author, A. A. (Year). Sentence case title. Publisher. | Abelson, H., & Sussman, G. J. (1985). Structure and interpretation of computer programs. MIT Press. |
| `inproceedings` | Author, A. A. (Year). Sentence case title. In Proceedings Title (pp. pp–pp). Publisher. | Abeni, L., & Buttazzo, G. (1998). Integrating multimedia applications in hard real-time systems. In Proceedings 19th IEEE Real-Time Systems Symposium (pp. 4–13). IEEE. |
| `book-chapter` | Author, A. A. (Year). Sentence case title. In Book Title (pp. pp–pp). Publisher. | — |
| `tech-report` / `thesis` / `manual` / `misc` | Author, A. A. (Year). Sentence case title. Issuing institution. | — |
| `reference-work` (no single author) | Title in sentence case (edition, volume span). (Year span). Publisher. | Great Soviet encyclopedia (3rd ed., Vols. 1–31). (1973–1983). Macmillan. |
| `archival-record` | Author, A. A. (Year). Title [Archival record]. Repository, Series, Call number. | Benavides, D. de (1653). Relación de méritos y servicios [Archival record]. Archivo General de Indias, Indiferente, 117, N.21. |

Archival records (category `Document`) follow APA's archival form: the bracketed
`[Archival record]` follows the title, then the holding repository, its series, and the
call number/signatura. Language is recorded in `specific.language` (e.g. `Spanish`). Note
that Spanish and French nobiliary particles stay un-abbreviated in the author initials
(`Benavides, D. de`, not `Benavides, D. D.`).

Rules (applied by `bin/import_research.py`):

- Authors: `Surname, Initials` with spaced single-letter initials and periods (`IJsbrand Jan`
  → `I. J.`); `&` before the last author; 21+ authors collapse to the first 19 + `…` + the
  last (APA 7th); records ending in bibtex `and others` render `, et al.`.
  Corporate authors pass through unchanged (no-comma bodies ending in
  `Corporation`, `Foundation`, `Committee`, … render literally).
- Work title in **sentence case**: first word and post-colon word capitalized; words with
  internal capitals or all-caps (acronyms: `HadoopDB`, `BGP`) keep their form; everything
  else lowercased.
- Venue in title case as recorded; volume/issue as `Vol(No)`; page ranges and compound
  issue numbers joined with an en-dash (`1--82` → `1–82`); LaTeX escapes unescaped
  (`\&` → `&`); missing parts are omitted, never faked.
- `dp-title` is plain text (`textContent`), so venue italics are dropped there; the DOI/URL,
  when known, lives in `specific.identifier`, not in the title.
- Records without a machine-readable source (no parseable author/year/title) are **skipped**,
  never title-guessed: they land in the import's skipped report for hand curation.

### Topics (`metadata.topics`)

Each node carries `metadata.topics`: an ordered list of topic tags, **general → specific** —
the Level-1 domain first, then its Level-2 subfields (e.g.
`["computer-science", "databases", "query-optimization"]`). One node may carry up to 6
topics (1–2 Level-1 + Level-2s); thin records carry 1–2. Topics are inferred from the
source document's semantics (work title ×3, venue ×2, notes prose ×1 when present):
venue priors for domain-specific venues, keyword scoring on titles, disambiguation of
generic words (`policy`, `model`, `system` count only with venue/title reinforcement),
and no prior from multidisciplinary venues (`Nature`, `Science`, `PNAS`, arXiv) or
general publishers. Empty means unclassified — never force-tagged; the review report
lists topic-less nodes.

Level-1 taxonomy (16):

`archival-records`, `artificial-intelligence`, `biology`, `cognitive-science`,
`computer-science`, `economics`, `engineering`, `history`, `management`, `mathematics`,
`philosophy`, `physics`, `political-science`, `psychology`, `sociology`, `statistics`.

Level-2 subfields:

- `archival-records`: `colonial-administration`, `personnel-records`,
  `manuscripts-and-petitions`, `printed-and-published-materials`.
- `artificial-intelligence`: `machine-learning`, `deep-learning`, `natural-language`,
  `vision`, `robotics`, `reasoning-planning`, `multi-agent`.
- `biology`: `genetics-genomics`, `neuroscience`, `ecology-evolution`, `cell-molecular`,
  `epidemiology`, `bioinformatics`.
- `cognitive-science`: `perception`, `memory-learning`, `decision-making`, `language-cognition`.
- `computer-science`: `databases`, `operating-systems`, `networks`, `programming-languages`,
  `distributed-systems`, `computer-architecture`, `security`, `software-engineering`,
  `interaction-design`, `information-retrieval`.
- `economics`: `growth-development`, `trade`, `labor`, `finance`, `game-theory`,
  `econometrics`, `innovation-economics`.
- `engineering`: `control-systems`, `signal-processing`, `power-energy`, `manufacturing`,
  `materials`.
- `history`: `history-of-science`, `economic-history`, `modern-history`.
- `management`: `innovation`, `organization-theory`, `strategy`, `entrepreneurship`,
  `operations`, `marketing`.
- `mathematics`: `algebra`, `analysis`, `geometry-topology`, `probability`, `optimization`,
  `logic-foundations`.
- `philosophy`: `epistemology`, `ethics`, `metaphysics`, `philosophy-of-science`,
  `philosophy-of-mind`.
- `physics`: `quantum`, `relativity-cosmology`, `thermodynamics-statistical`,
  `condensed-matter`, `fluid-dynamics`.
- `political-science`: `democracy-elections`, `governance`, `conflict`, `political-economy`.
- `psychology`: `behavioral`, `developmental`, `social-psychology`, `clinical`.
- `sociology`: `social-networks`, `inequality`, `institutions-culture`, `demography`.
- `statistics`: `inference`, `bayesian`, `time-series`, `experimental-design`.

## Data flow

- `app/research/data/data.json` — seed + Epistecnica-document import (canonical node model;
  `category` restricted to the five artifact categories above; `name` per Title format;
  `metadata.topics` per Topics).
- `python bin/layout.py --data-file app/research/data/data.json --layout-file app/research/data/layout.json --group-by metadata.topics.0 --group-fallback category`
  regenerates the explorer layout (one disk per first-topic group on a ring).
- `python bin/seed_couchdb.py --dataset research` pushes nodes to CouchDB (docs keyed
  `research:<node_id>`).

## Editor / Explorer

- Explorer: `/research/` — read-only graph viewer. Supports `?node=<id>` deep links (selects, pans to, opens the node; unknown ids load normally).
- Editor: `/research/edit.html` — node editor (`const DATASET = 'research'`); syncs to CouchDB.
