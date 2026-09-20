# AGENTS.md

## Purpose

Instructions for AI agents working in this repository. Follow the conventions below; when a module
directory contains its own `AGENTS.md`, it takes precedence for work inside that module.
`guideline.md` (file naming, paths/URLs, commits, branches) is binding.

## Project Context

### Description

Naturgnosis identifies and formalizes the set of epistemic elements that enable an agent to
effectively navigate — understanding and action — reality, especially social reality. It is the main
index of the world's technique and episteme. Its sibling project Epistecnica (separate repository)
covers what @dbremont intentionally pursues through deep study and mastery; keep the two separate.

### Objectives

- Stabilize and improve the generative system producing the **Domain Epistemic Artifact Set (DESA)**.
- Keep each module (`app/<module>/`) complete: views, data, spec, AGENTS.md.
- One server (`bin/sync.py`), one image, two deploy targets (local compose, server script).

### Scope

- In: the seven modules under `app/` (social, production, research,
  nation, technique, epistemica, note), shared tooling in `bin/`, deployment in `deploy/`, specs in `spec/`.
- Out: the separate **Epistecnica** repository (personal curricula for @dbremont; the in-repo
  `epistemica` module maps the episteme itself, not personal pursuits); market analysis (Social
  Space notes this explicitly); anything requiring a backend other than CouchDB.

## Repository Structure

| Path | Role |
|------|------|
| `app/` | The product. One directory per module; `app/index.html` is the landing/registry. |
| `app/<module>/web/` | Module views (static html/js). |
| `app/<module>/data/` | Dataset mirror + schema (graph modules). |
| `app/*/import/` | Raw third-party exports — archival, never edit by hand. |
| `app/shared/` | Cross-module assets (`theme.css`, `img/`). |
| `bin/` | Shared tooling: `sync.py` (server), `seed_couchdb.py`, `build_note_index.py`, `layout.py`. |
| `deploy/` | Dockerfile, docker-compose.yml (app-only), `deploy_local.sh`, `deploy_server.sh`, `preflight.sh`; `README.md` = execution-environment note. |
| `spec/` | Global spec (`spec/README.md`), per-module specs, theme spec. |
| `docs/` | Does not exist anymore — do not recreate; the served root is `app/`. |

## Agent Operating Principles

### Understand Before Changing

Read `spec/README.md` and the relevant module spec + AGENTS.md before editing. Dataset ids are the
module names (`social`, `production`, `research`, `nation`, `technique`, `epistemica`) — they appear in editor
pages (`const DATASET = '…'`), CouchDB doc keys, and API calls; renaming one is a breaking change
across all three.

### Prefer Existing Solutions

- Reuse `bin/sync.py`'s API; do not add new servers.
- Reuse the tokens in `app/shared/theme.css`; never hardcode colors.
- Reuse the node model (`id, name, tags, category, description, …`) for new datasets.

### Minimize Change

The graph editors (`app/*/web/edit.html`) are large single-file apps with no build step. Make
surgical edits; keep social/production/research/technique copies in sync when changing shared
behavior, or clearly scope a change to one module.

### Preserve Invariants

- CouchDB is a persistent dependency of the execution environment: workflows only connect to it
  (via `COUCHDB_*` in `.env`) and preflight-check it; they never provision, redeploy, or remove it
  (see `deploy/README.md`).
- `data.json` mirrors are server-written — see Data Sync in the README before committing.
- `app/note/notes/` is the notes source of truth; `app/note/data/index.json` is generated — never
  edit it by hand (run `python bin/build_note_index.py`).
- `.env` is never committed.

### Keep Work Scoped

One module (or one concern) per change set; follow the commit guideline in `guideline.md`
(mirrors `~/configs/global/git/guideline.md`: `feat|fix|docs|style|refactor|test|chore(scope): summary`).
New files must satisfy the naming rules in `guideline.md`; run `python bin/slugify_files.py <path>`
when migrating existing names.

## Development Environment

### Requirements

- Python 3.12+ (stdlib only — no pip installs needed to run the server)
- Docker (for deployment); `uv` optional for tooling

### Setup

```sh
python bin/sync.py --no-couch        # offline: static serving, API returns 503
python bin/sync.py                   # full: needs CouchDB + COUCHDB_* env or .env
```

### Common commands

```sh
python bin/build_note_index.py       # regenerate notes index (commit the result)
python bin/seed_couchdb.py           # push all mirrors into CouchDB
make build                           # regenerate graph layouts
make deploy-local                    # compose up couchdb + app, then seed
```

### Verification

Before declaring done: `python bin/sync.py --no-couch` and check every touched module route
returns 200 (`/, /<module>/, /<module>/edit.html`); `curl /api/health` returns JSON. There is no
test suite; the server run + route checks are the smoke test.

## Git Workflow

Global git configuration lives in `~/configs/global/git` (hooks via `core.hooksPath`) and
`~/configs/bin` (helper scripts). Every commit passes through four active hooks.

### Check-in policy (`pre-commit.d/00-authorization-policy.sh`)

A staged file is only accepted if it carries the extended attribute `user.checkin=1` — otherwise
the commit is rejected with "Required check mark is missing".

```sh
mark-for-commit <file>…        # mark files (alias: mfc; ~/configs/bin/mark-for-commit)
mark-for-commit --list         # list marked files
mark-for-commit --unmark <f>…  # remove the mark
git diff --cached --name-only -z --diff-filter=ACM | xargs -0 mark-for-commit   # bulk-mark staged
```

The mark is a filesystem xattr: it survives staging, is not versioned, and must be re-applied on
new files.

### Annotation policy (`pre-commit.d/01-annotation-policy.sh`)

Staged source files (patterns in `annotations.conf`) must not contain BLOCK annotations —
`@WORKING`, `@FIXME`, `@QUESTION`, `@VERIFY` — or the commit is rejected. `@TODO`, `@HACK`,
`@WORKAROUND` only warn; `@TECH-DEBT`, `@NOTE`, etc. are informational.

### Encoding policy (`pre-commit.d/02-encoding-policy.sh`)

Staged text files must be UTF-8, without a BOM, with LF line endings only. Fix with
`dos2unix <file>` / `sed -i '1s/^\xEF\xBB\xBF//' <file>` / `iconv`.

### Commit message hook (`prepare-commit-msg`)

`git commit -m "…"` is **overwritten** by the template `type(<ref>): message` (plus the staged
file list), where `<ref>` is the branch name or the Jira key extracted from it (e.g. branch
`feature/20260624-SGF-11181-login` → scope `SGF-11181`). The intended flow: run `git commit`,
let the editor open with the pre-filled template, replace it with the real message, save.
Amending with `-m` is clobbered the same way (`-m` counts as a message source); to supply a full
message programmatically, use the editor flow:

```sh
GIT_EDITOR='<script that writes your message into $1>' git commit --amend
```

### Signing & branches

- Commits are SSH-signed via 1Password (`gpg.format=ssh`, `commit.gpgsign=true`).
- Branches: `<type>/<slug>` (see `guideline.md`); a Jira key in the branch name becomes the
  commit-message scope automatically.

## When to Ask

- Renaming modules, dataset ids, or the CouchDB database (breaks running deployments).
- Changing the node schema (touches every module).
- Adding a new module (must ship with code + views + data + spec + AGENTS.md).
- Anything touching the running server at bremontix.xyz.
