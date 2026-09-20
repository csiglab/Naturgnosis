# Technique Space

> Fine-grained technique rendered as a navigable graph: technical artifacts, engineering principles,
> methods, and implementation details — the layer beneath the Production Space's coarse description.

## Status: bootstrapped

The module is scaffolded from the Social Space app (explorer + editor, `dataset=technique`) with an
empty dataset. The space formulation below is the working agenda.

## Formulation

> Which are the set of concepts useful to describe technique itself — independent of any particular
> production or market arrangement?

### Candidate layers

| Layer | Core question |
| ----- | ------------- |
| Principle | Which natural regularities are exploited? (physical, chemical, biological) |
| Artifact | Which objects embody technique? (tools, machines, components, materials) |
| Method | Which procedures organize doing? (processes, recipes, standards, practices) |
| Competence | Which skills operate technique? (craft, engineering disciplines, tacit knowledge) |
| Lineage | How does technique evolve? (invention, diffusion, improvement, obsolescence) |

### Candidate categories

Technique, Technical Artifact, Principle, Method, Process, Tool, Machine, Material, Standard,
Competence, Measurement, Technical Constraint.

## Relation to other modules

- **Production Space** describes the economic/production shell; Technique Space describes the
  technical interior it draws upon.
- **Glossary** defines the vocabulary (technique, technicity, technology, technoscience…).


## Data provenance

Bootstrapped from **Epistecnica tecnica app**: 40 nodes. Raw exports are archival in `app/technique/import/`; regenerate `data/data.json` with `bin/import_technique.py` (reads only from `import/`). After edits in the app, the sync server owns `data.json` — do not re-run the import over editor work.

## Editor / Explorer

- Explorer: `/technique/` — read-only graph viewer.
- Editor: `/technique/edit.html` — node editor; syncs to CouchDB `dataset=technique`.
