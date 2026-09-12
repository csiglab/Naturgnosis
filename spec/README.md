# Naturgnosis — Global Specification

> **Naturgnosis** aims to identify and formalize the set of epistemic elements that enable an agent to
> effectively navigate — understanding and action — reality, especially social reality.

> Naturgnosis is the main index of the world's **technique** and **episteme**. Its sibling project,
> **Epistecnica**, records what man intentionally pursues through deep study and some level of mastery —
> specifically for **@dbremont**. Epistecnica is a separate repository; nothing of it is built here,
> and content must not leak between the two without explicit intent.

## Goals

- Stabilize a generative system that produces a **Domain Epistemic Artifact Set (DESA)** representing
  social reality and rendering it intelligible as a structured domain of analysis and action.
- Study, refine, and improve the underlying generative system that produces and organizes the DESA,
  with emphasis on consistency, expressiveness, and explanatory power.
- Connect the DESA to practical **activity systems**, such that epistemic artifacts are systematically
  linked to real-world actions, interventions, and decision-making processes within social domains.

## Module Registry

Every module is a self-contained app under `app/<module>/` (code + views + data + spec + AGENTS.md),
served by the single sync server (`bin/sync.py`) and deployed as one image.

| # | Module | Path | Kind | Storage | Status |
|---|--------|------|------|---------|--------|
| 1 | Social Space (main) | `app/social/` | Graph explorer + editor | CouchDB (`dataset=social`) + disk mirror | active |
| 2 | Production Space | `app/production/` | Graph explorer + editor | CouchDB (`dataset=production`) + disk mirror | active |
| 3 | Research Space | `app/research/` | Graph explorer + editor | CouchDB (`dataset=research`) + disk mirror | scaffold |
| 4 | Epistemic Space | `app/epistemica/` | Graph explorer + editor | CouchDB (`dataset=epistemica`) + disk mirror | bootstrapped |
| 5 | Technique Space | `app/technique/` | Graph explorer + editor | CouchDB (`dataset=technique`) + disk mirror | bootstrapped |
| 6 | Glossary | `app/glossary/` | Entry index + search + reader | Physical markdown (`entries/*.md`) + generated `data/index.json` | active |
| 7 | Phrases Catalog | `app/phrases/` | Catalog UI + form editor | CouchDB (`dataset=phrases`) + disk mirror | active |
| 8 | Nation Space | `app/nation/` | Entry index + entry pages (Index Gentium style) + editor | CouchDB (`dataset=nation`) + disk mirror | bootstrapped |

## Architecture

```
app/                      the product — one directory per module
  <module>/web/           views (static html/js)
  <module>/data/          dataset mirror + schema (graph modules); generated index (glossary)
  <module>/entries/       source-of-truth markdown (glossary only)
  <module>/import/        raw third-party exports kept for provenance
  <module>/view/          long-form notes attached to the module (social only, today)
  shared/theme.css        Oxford Common Room tokens (source of truth: spec/theme)
bin/                      shared tooling: sync server, seeders, importers, index builders
deploy/                   Dockerfile, docker-compose.yml, deploy scripts (local + server)
spec/                     this spec + per-module specs + theme spec
```

### Server (`bin/sync.py`)

One process serves everything:

- **Static**: `/` → `app/index.html`; `/<module>/x` 301-redirects to `app/<module>/web/x` so
  relative fetches inside pages resolve at the correct depth; physical subdirectories `web/`,
  `data/`, `view/`, `entries/`, `import/` are served as-is.
- **Graph API** (same origin):
  - `GET  /api/graph?dataset=<id>` — nodes from CouchDB
  - `POST /api/graph/save` — `{dataset, nodes[], delete_ids?[]}` upsert/delete; mirrors the full
    dataset back to `app/<module>/data/data.json`
  - `POST /api/layout/recompute?dataset=<id>` — regenerate `layout.json`
  - `GET  /api/health` — service + CouchDB status
- **Offline mode**: `--no-couch` serves statically and answers the API with 503 — for development and CI.
- **Bootstrap**: on start, a dataset whose CouchDB range is empty is seeded from its `data.json`.

### Data policy

| Kind | Source of truth | Derived | Notes |
|------|-----------------|---------|-------|
| Graph modules | CouchDB docs (`{dataset}:{node_id}`) | `data.json` mirror, `layout.json` | Download server data before committing (see README). |
| Phrases | CouchDB (`dataset=phrases`) | `data.json` mirror | Seed from Notion exports via `bin/import_phrases.py` (one-shot). |
| Glossary | Physical markdown (`app/glossary/entries/`) | `data/index.json` | Rebuild with `bin/build_glossary_index.py`; index is committed so the static viewer works without a backend. |

### Node model

Graph datasets (social, production, research, technique) and phrases share the Naturgnosis node model:
`id, name, tags, category, description, chronology, relationships, specific, metadata, references`.
Canonical JSON Schema: `app/social/data/schema/schema.json` (per-module copies under
`app/<module>/data/schema/`). Changes to the model must be mirrored in every module schema and noted
in the module spec.

## Deployment

Single image, two targets. **CouchDB is a persistent dependency of the execution environment —
never provisioned, redeployed, or removed by any workflow here**; deployments preflight-check it
and fail with a clear log when unreachable. Contract and failure modes: `deploy/README.md`.

- **Local**: `deploy/docker-compose.yml` (app only, host network) via `deploy/deploy_local.sh`
  (preflight → build/up → seed).
- **Server**: `deploy/deploy_server.sh` (preflight →) pulls `ghcr.io/csiglab/naturgnosis:latest`
  (built by GitHub Actions on push to `main`) and runs it with `--network host`, mounting `.env`.
  Port: `NATURGNOSIS_PORT` (default 8011).

Configuration (`.env`, never committed): `COUCHDB_URL`, `COUCHDB_DB=naturgnosis`, `COUCHDB_USER`,
`COUCHDB_PASSWORD`.

## Conventions

- **Commits**: follow `~/configs/global/git/guideline.md` — `<type>(<optional scope>): <description>`
  with types `feat, fix, docs, style, refactor, test, chore`. Global hooks are active.
- **Style**: all pages derive from the Oxford Common Room tokens (`spec/theme`, `app/shared/theme.css`);
  never hardcode colors.
- **Data sync**: the server is the write path; before committing dataset changes, pull the server
  mirror (see README "Data Sync").
- **Naming**: module directories are lowercase ASCII (`social`, `production`, `research`, `technique`,
  `glossary`, `phrases`); dataset id = module name.
