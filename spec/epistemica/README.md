# Epistemic Space

> The space of episteme: disciplines, fields, and bodies of knowledge that deep study and mastery
> can pursue — mapped as a navigable graph.

## Status: bootstrapped

The module is scaffolded from the Social Space app (explorer + editor, `dataset=epistemica`) with an
empty dataset. The space formulation below is the working agenda.

## Boundary

- **Epistemica (this module, this repo)** maps the episteme itself — the terrain of knowledge and
  practice, at the scale of the world.
- **Epistecnica (separate repository)** records what @dbremont intentionally pursues through deep
  study and mastery — the personal subset. Do not mix personal curricula into this module.

## Formulation

> Which are the set of concepts useful to describe the space of knowledge and practice? Which are
> the main categories?

### Candidate layers

| Layer | Core question |
| ----- | ------------- |
| Disciplinary | Which fields organize inquiry? (disciplines, subfields, programs) |
| Methodological | How is each field practiced? (methods, instruments, standards) |
| Corpus | What has been accumulated? (canons, literatures, data, artifacts) |
| Competence | What does mastery consist of? (skills, curricula, lineages, apprenticeship) |
| Frontier | Where is knowledge moving? (open problems, programs, schools) |

### Candidate categories

Discipline, Field, Subfield, Method, Instrument, Canon, Curriculum, Competence, School,
Open Problem, Practitioner, Lineage.


## Data provenance

Bootstrapped from **Epistecnica epistemica app**: 122 nodes. Raw exports are archival in `app/epistemica/import/`; regenerate `data/data.json` with `bin/import_epistemica.py` (reads only from `import/`). After edits in the app, the sync server owns `data.json` — do not re-run the import over editor work.

## Editor / Explorer

- Explorer: `/epistemica/` — read-only graph viewer.
- Editor: `/epistemica/edit.html` — node editor; syncs to CouchDB `dataset=epistemica`.
