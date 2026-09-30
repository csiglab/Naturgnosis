# Guideline

Repository conventions for Naturgnosis. Binding for all contributors and agents; global commit hooks
(`~/configs/global/git`) enforce the commit rules.

## File Naming

> Semantic name, semantic path, semantic URL. Lowercase, ASCII, `_` separates words.

Rules for files and directories we author:

- **Lowercase ASCII only** — no uppercase, spaces, parentheses, or diacritics in file or directory
  names.
- **`_` separates words** — `deploy_server.sh`, `seed_couchdb.py`, `aceleradoras_cientificas.md`.
- **Semantic names** — the name should say what the thing is (`seed_couchdb.py`, not `s.py`).
- **Extensions lowercase** — always `.md`, `.py`, `.sh`, `.json`, `.html`, `.png`.
- **Content slugs** — long-form notes (`app/note/data/`, the corpus home) are named after
  their content,
  slugified by the Epistecnica rule (`bin/build_note_index.py:slugify_segment()` —
  never `bin/slugify_files.py`, which emits `_`). The
  canonical human term lives inside the file (H1), never in the file name.

### Exemptions

- **Canonical tool names** — convention wins and cannot be changed: `Dockerfile`, `Makefile`,
  `docker-compose.yml`, `README.md`, `LICENSE`, `AGENTS.md`, `guideline.md`, `.gitignore`,
  `.dockerignore`, `.github/workflows/deploy.yml`.
- **`app/*/import/`** — raw third-party exports are archival; never rename or edit (provenance).
- **`app/note/data/`** — the note corpus lives here (`<section>/<kebab-case>.md`,
  plus the generated `index.json` beside it — never hand-edit the index, rebuild with
  `make notes-index`). Corpus paths follow the Epistecnica slug rule, not the `_`
  rule above: lowercase, fixed transliterations for `æ→ae`, `ø→o`, `œ→oe`,
  `ß→ss` (no NFKD decomposition), then NFKD-normalize to ASCII, every run of
  non-alphanumeric characters becomes a single `-`, trim leading/trailing
  `-` (`my-note.md`).
   Collisions get a `-2`, `-3`, … suffix. Never run `bin/slugify_files.py`
   (which emits `_`) on the corpus; see `spec/note/authoring.md` and
  `bin/build_note_index.py:slugify_segment()` for the canonical form. The viewer
  resolves `note.html?n=<path>` against this directory.
- **`app/*/web/vendor/`** — third-party code keeps its upstream name.

## Paths & URLs

- URLs mirror paths; both are semantic: module directory = URL segment = dataset id
   (`/social/`, `/production/`, `/research/`, `/nation/`, `/technique/`, `/epistemica/`, `/note/`).
- Fixed data file names inside a module: `data.json` (dataset mirror/seed), `layout.json`
  (precomputed layout), `index.json` (generated search index), `schema.json` + `notes`
  (schema context).
- Module directories, dataset ids, and CouchDB doc keys are one and the same string; renaming one
  renames all three (breaking change — ask first).

## Derived views

A space that is a *role-based cut* over another space's nodes is a derived view, not a
dataset: it stores no nodes of its own. (First instance: Production Space is computed from
Social Space; see `app/production/AGENTS.md`.)

- **Single home**: every node lives in exactly one owning dataset. Other spaces never
  duplicate it — they compute views over it.
- **Role tags**: membership in a view is marked on the owning node with a reserved tag of
  the form `<space>-view` (today: `production-view`). The tag is exact-match (case- and
  whitespace-insensitive); ad-hoc lookalikes (`production`, `production chain`) do not
  count. When adding a node that plays a view's role, tag it in the owning editor at
  creation time.
- **Builders**: one script per view (`bin/build_<space>_view.py`, stdlib only) reads the
  owning mirror(s) and writes committed `view.json` + `view-layout.json` into the view
  module's `data/` — never `data.json`/`layout.json` (those names would resurrect the
  module as an editable dataset). Regenerate deliberately (`make <space>-view`); the files
  are committed, like the search index. Only edges with both ends in the view are kept.
- **Viewers**: the view explorer fetches `view.json`; there is no editor (edit in the
  owning space). New views follow this shape; do not invent a second mechanism.

## Topic placement strategy

> Reusable decision procedure for placing any new topic in the right space(s), with the
> right artifacts. First worked instance: Quarry → nature (node `quarry-ontic-001`,
> note `nature/quarry.md`). Follow it before creating nodes or notes.

1. **Cut the segment, name the question.** State what is included/excluded, then match the
   dominant question to a space — that fixes the meta workflow, the note schema, and the
   owning dataset:

   | Dominant question | Space | Meta workflow | Dataset / editor |
   | --- | --- | --- | --- |
   | What observer-independent furniture is here? | nature | "How to decompose any natural instance?" | `nature` (`/nature/edit.html`) |
   | How is transformation organized and performed? | technique | "How to decompose any technical instance?" | `technique` (`/technique/edit.html`) |
   | Which actors, institutions, roles, relations act here? | social | "How to decompose any social instance?" | `social` (`/social/edit.html`) |
   | What scaffolding warrants knowing it? | epistemica | "How to decomposed any epistemical instance?" | `epistemica` (`/epistemica/edit.html`) |

2. **Type the root; ambiguity goes to the human, never guess.** When the instance is readable under
   several grammars (a quarry is a landform *and* a worksite *and* a facility), STOP and ask
   the human which readings to grow trees for (and which is primary) before decomposing.
   One tree per confirmed type (multi-root forest — never two types on one row). Only when
   no answer comes, declare one default root and keep the others as `readable as …` prose
   cross-links.
3. **Fix the depth before decomposing; default to the middle path.** Every decomposition
   request states its level of detail — shallow (root plus direct constituents, no
   intermediaries), middle (full intermediate structure: grouping nodes throughout,
   every branch worked to instance leaves, exemplars only where a branch needs one),
   or deep (exhaustive attributes, fields, schedules, and deployment exemplars).
   When no depth is stated, assume the middle path: satisfy the Well-Expansion Rule
   (rich intermediates, all leaves resolving to instances) without enumerating
   deployment minutiae. E.g. pharmaceutical industry — shallow: sectors and major
   product groups; middle: plus production systems, key artifacts, standards, and
   institutions; deep: plus facility operations, batch records, and validation protocols.
4. **Single home.** Every node lives in exactly one owning dataset; other spaces compute
   views over it, never duplicate it (see "Derived views" above).
5. **Node, note, or both.** A note carries decomposition and argument (corpus home
   `app/note/data/`, kebab-case paths, new top-level sections allowed — e.g. `nature/`);
   a node carries graph addressability (edges, tags, search). First-class topics usually
   need both; note-first is fine. New nodes ship their local mirror plus seed/bootstrap
   coverage in the same change set (`data.json` is what `bin/seed_couchdb.py` and server
   startup read).
6. **Derived-view check.** If the topic plays a production role, tag the owning Social
   node `<space>-view` at creation time and regenerate (`make <space>-view`). Nature and
   technique nodes never carry view tags.
7. **Verify.** Rebuild the notes index (`python bin/build_note_index.py`, commit the
   result); pull the server mirror before committing dataset edits; smoke-test every
   touched route (`/, /<module>/, /<module>/edit.html`, note viewer path). One module
   (or one concern) per change set.

## Task routing: a nature topic → the guidelines that carry it

> Entry point for any task whose topic is a piece of observer-independent reality
> (a landform, a water body, a living system, a physical process). Read the steps in
> order; each note is binding for the step that names it. First worked route: Quarry →
> `nature/quarry.md` (node `quarry-ontic-001`).

0. **Route before you write.** Apply "Topic placement strategy" step 1 above: only the
   question *"what observer-independent furniture is here?"* lands in nature.
   Transformation, actor/institution, and scaffolding questions route to the
   technicarum, socialium, and epistemicarum guides instead. Never force-fit a topic
   into nature to justify a new note there.
1. **Presupposed definitions.**
   [Philosophia Artium Epistemicarum et Operis](/note/note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)
   — `Reality`, segment types, levels of organization (micro/meso/macro), the
   ontology/epistemology dual, DCESA. Read for the definitions; restate none of them
   in a natural note.
2. **Primary workflow.**
   [Philosophia Naturalis et Operis](/note/note.html?n=meta/philosophia-naturalis-et-operis.md)
   — "How to decompose any natural instance?", the Tabular view (6 categories → 17
   element types, with role and instances), the Recursive view with its binding and
   spine expansion rules, and "Which note schema used - in order to document a natural
   element?". Two gates apply to every instance: each element carries its **level of
   organization** (the same name at two levels is two nodes), and the **Limitation
   checklist** (13 items) is recorded as ontic properties of the segment.
3. **Multi-typed instances.**
   [Ambiguity Resolution](/note/note.html?n=meta/ambiguity-resolution.md) plus "How to
   decompose an instance that belongs to multiple element types?" in the
   [technicarum guide](/note/note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
   — one tree per confirmed reading (multi-root forest), never two types on one row;
   when the root typing is ambiguous, ask the human. Naturalis QA: the instrument
   technically, the formation naturally, cross-linked at the Observation Interface;
   secondary readings stay `readable as …` prose.
4. **Artifacts and invariants.** Apply "Topic placement strategy" steps 3–7 unchanged,
   plus: nodes go to dataset `nature` (`/nature/edit.html`), notes to
   `app/note/data/nature/<kebab-case>.md` (worked instance `nature/quarry.md`); nature
   nodes never carry `<space>-view` tags. Rebuild the notes index, pull the server
   mirror, and smoke-test the routes in the same change set.

## Commits

Mirrors `~/configs/global/git/guideline.md`:

```text
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

Allowed `<type>`:

- `feat` — add a new feature
- `fix` — fix a bug
- `docs` — documentation changes
- `style` — formatting or style-only changes; no behavior change
- `refactor` — restructure code without changing behavior
- `test` — add or modify tests
- `chore` — maintenance or other changes that don't affect production behavior

Scope, when used, is the module or concern: `feat(nation): …`, `fix(sync): …`.

## Branches

- `main` is the default and deployment branch.
- Working branches: `<type>/<slug>` — lowercase ASCII with `-` word separation
  (e.g. `feat/nation-index`, `fix/sync-mirror`).

## Task guides (meta notes)

How-to workflows for decomposition and content work live as meta notes in the corpus:

- Technique content — `app/note/data/meta/philosophia-artium-technicarum-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-artium-technicarum-et-operis.md)):
  "How to decompose any technical instance?", multi-type (multi-root forest) rule,
  CRM case study, technical-element note schema.
- Epistemic content — `app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)):
  "How to decomposed any epistemical instance?", epistemic-element note schema.
- Social content — `app/note/data/meta/philosophia-socialium-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-socialium-et-operis.md)):
  "How to decompose any social instance?", layer test (Ontic/Synontic/Noetic/Multi),
  facet assignment, social-element note schema.
- Natural content — `app/note/data/meta/philosophia-naturalis-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-naturalis-et-operis.md)):
  "How to decompose any natural instance?", level of organization, Limitation
  checklist, natural-element note schema. Presupposes the epistemicarum definitions;
  restates nothing from it.

Follow the applicable workflow before decomposing instances or documenting elements; when
the root typing is ambiguous, ask the user instead of guessing.
