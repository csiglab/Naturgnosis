# Research Space

> The world's research apparatus rendered as a navigable graph: public research institutes (PRIs),
> laboratories, funding agencies, universities, firms' research arms, and their intersections.

## Status: scaffold

The module is scaffolded from the Social Space app (explorer + editor, `dataset=research`) with an
empty dataset. The space formulation below is the working agenda.

## Formulation

> Which are the set of concepts useful to describe the research dimension of reality? Which are the
> main categories?

### Candidate layers

| Layer | Core question |
| ----- | ------------- |
| Institutional | Who performs research? (PRIs, universities, firm labs, institutes) |
| Funding | Who pays, through which instruments? (agencies, foundations, missions) |
| Knowledge | What is produced? (fields, programmes, publications, datasets) |
| Relational | How are actors connected? (consortia, intersections, mobility, co-authorship) |
| Policy | Under which regime? (science policy, evaluation, national systems) |

### Candidate categories

Research Institute, Laboratory, Funding Agency, University, Research Programme, Researcher,
Research Group, Publication, Dataset, Instrument, Intersection (shared appointment/affiliation).

## Sources

- Existing actor notes under `app/social/view/actor/technique/` (Instance/Intersection pages)
  describe national research systems and are the seed corpus for this space.
- Index Gentium (country index) for national-system context.

## Editor / Explorer

- Explorer: `/research/` — read-only graph viewer.
- Editor: `/research/edit.html` — node editor; syncs to CouchDB `dataset=research`.
