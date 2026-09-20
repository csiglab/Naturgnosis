# Guideline

Repository conventions for Naturgnosis. Binding for all contributors and agents; global commit hooks
(`~/configs/global/git`) enforce the commit rules.

## File Naming

> Semantic name, semantic path, semantic URL. Lowercase, ASCII, `_` separates words.

Rules for files and directories we author:

- **Lowercase ASCII only** — no uppercase, spaces, parentheses, or diacritics in file or directory
  names.
- **`_` separates words** — `deploy_server.sh`, `build_glossary_index.py`, `aceleradoras_cientificas.md`.
- **Semantic names** — the name should say what the thing is (`seed_couchdb.py`, not `s.py`).
- **Extensions lowercase** — always `.md`, `.py`, `.sh`, `.json`, `.html`, `.png`.
- **Content slugs** — glossary entries (`app/glossary/entries/`) and long-form notes
  (`app/social/view/`) are named after their content, slugified by `bin/slugify_files.py`. The
  canonical human term lives inside the file (H1), never in the file name.

### Exemptions

- **Canonical tool names** — convention wins and cannot be changed: `Dockerfile`, `Makefile`,
  `docker-compose.yml`, `README.md`, `LICENSE`, `AGENTS.md`, `guideline.md`, `.gitignore`,
  `.dockerignore`, `.github/workflows/deploy.yml`.
- **`app/*/import/`** — raw third-party exports are archival; never rename or edit (provenance).
- **`app/*/web/vendor/`** — third-party code keeps its upstream name.

## Paths & URLs

- URLs mirror paths; both are semantic: module directory = URL segment = dataset id
   (`/social/`, `/production/`, `/research/`, `/glossary/`, `/nation/`).
- Fixed data file names inside a module: `data.json` (dataset mirror/seed), `layout.json`
  (precomputed layout), `index.json` (generated search index), `schema.json` + `notes`
  (schema context).
- Module directories, dataset ids, and CouchDB doc keys are one and the same string; renaming one
  renames all three (breaking change — ask first).

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

Scope, when used, is the module or concern: `feat(glossary): …`, `fix(sync): …`.

## Branches

- `main` is the default and deployment branch.
- Working branches: `<type>/<slug>` — lowercase ASCII with `-` word separation
  (e.g. `feat/glossary-search`, `fix/sync-mirror`).
