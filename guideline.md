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
  (which emits `_`) on the corpus; see `app/note/data/readme.md` and
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

2. **Type the root; record ambiguity, never guess.** When the instance is readable under
   several grammars (a quarry is a landform *and* a worksite *and* a facility), declare one
   default root and keep the others as `readable as …` prose cross-links. One tree per
   type (multi-root forest — never two types on one row). When the root typing is
   ambiguous, ask the user instead of guessing.
3. **Single home.** Every node lives in exactly one owning dataset; other spaces compute
   views over it, never duplicate it (see "Derived views" above).
4. **Node, note, or both.** A note carries decomposition and argument (corpus home
   `app/note/data/`, kebab-case paths, new top-level sections allowed — e.g. `nature/`);
   a node carries graph addressability (edges, tags, search). First-class topics usually
   need both; note-first is fine. New nodes ship their local mirror plus seed/bootstrap
   coverage in the same change set (`data.json` is what `bin/seed_couchdb.py` and server
   startup read).
5. **Derived-view check.** If the topic plays a production role, tag the owning Social
   node `<space>-view` at creation time and regenerate (`make <space>-view`). Nature and
   technique nodes never carry view tags.
6. **Verify.** Rebuild the notes index (`python bin/build_note_index.py`, commit the
   result); pull the server mirror before committing dataset edits; smoke-test every
   touched route (`/, /<module>/, /<module>/edit.html`, note viewer path). One module
   (or one concern) per change set.

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
