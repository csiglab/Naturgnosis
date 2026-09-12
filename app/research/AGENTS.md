# AGENTS.md — Research Space

## Purpose

Graph of the world's research apparatus: public research institutes, laboratories, funding agencies,
universities, and their intersections. Currently a **scaffold** (empty dataset) copied from the Social
Space app. Spec: `spec/research/README.md`.

## Layout

- `web/index.html` — explorer; `web/edit.html` — editor (`const DATASET = 'research'`).
- `data/data.json` — server-written mirror (currently `[]`); `data/schema/` — scaffold schema.
- Seed corpus: actor notes in `app/social/view/actor/technique/` (Instance/Intersection pages).

## Commands

```sh
python bin/sync.py                    # serve (dataset=research is auto-discovered)
curl /api/graph?dataset=research      # nodes (empty until populated)
```

## Invariants

- Dataset id is `research`.
- The web app is a copy of the social one: propagate shared fixes from the other graph modules, but
  do not add research-specific vocab until the space formulation in the spec is settled.
