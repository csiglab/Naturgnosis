# Nature Space

> The space of nature: the physical and living phenomena that exist independently of
> inquiry — electromagnetic waves, fields, pressures, laws, agentic processes — mapped as
> a navigable graph. It is the ontic counterpart to Epistemic Space: epistemica maps the
> scaffolding of knowing, nature maps what the scaffolding is *about*.

## Status: bootstrapped

Seeded with the two `category == reality` nodes moved out of `epistemica`
(`em-wave-ontic-001`, `process_decision_making`) plus three stubs
(`electric-field-ontic-001`, `radiation-pressure-001`, `maxwell-equations-001`) created to
resolve the moved wave node's edges. Stubs carry `confidenceScore 0.6` and an audit note;
expand them into full records.

## Boundary

- **Nature (this module)** holds elements whose referent is observer-independent reality
  (cf. the Ontic Order branch in `/note/note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md`).
  Epistemic scaffolding — operators, standards, frameworks, artifacts, methods — stays in
  `epistemica`, even when it describes natural phenomena.
- New nature content is decomposed per "How to decompose any epistemical instance?"
  (`/note/note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md`), typed under the Ontic Order.

## Data provenance

Moved from the **Epistecnica epistemica export via `app/epistemica`** (2026-09-27):
`process_decision_making` lost its two cross-boundary edges (`uses framework_decision_theory`,
`is_bounded_by constraint_uncertainty`); the two epistemica nodes pointing at it
(`blueprint_decision_problem`, `constraint_uncertainty`) lost their inbound edges.
Provenance is recorded in each moved node's `metadata.auditTrail`.
`bin/import_epistemica.py` excludes the moved ids, so re-running the import cannot
resurrect them in `epistemica`.

## Editor / Explorer

- Explorer: `/nature/` — read-only graph viewer. Supports `?node=<id>` deep links (selects, pans to, opens the node; unknown ids load normally).
- Editor: `/nature/edit.html` — node editor; syncs to CouchDB `dataset=nature`.
