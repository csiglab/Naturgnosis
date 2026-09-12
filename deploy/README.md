# Deployment & Execution Environment

> What the execution environment provides, what this repo deploys, and what happens when a
> dependency is missing. The one rule to remember: **CouchDB is never provisioned here.**

## Dependencies

| Dependency | Version | Provided by | Notes |
| ---------- | ------- | ----------- | ----- |
| Python | 3.12+ | execution environment | stdlib only — no pip installs to run the server |
| Docker | recent (compose v2) | execution environment | builds/runs the app image |
| CouchDB | 3.5 | **execution environment** (persistent) | `http://127.0.0.1:5984`, data-bearing, **never created/redeployed/removed by this repo** |

## CouchDB policy

- CouchDB is a **persistent, data-bearing dependency** of the execution environment. It hosts live
  databases (e.g. `sociognosis`, `tecnica`, `epistemica`, `pais`, …) that outlive any container.
- Every workflow in this repo is **connect-only**: it reads `COUCHDB_URL`, `COUCHDB_DB`,
  `COUCHDB_USER`, `COUCHDB_PASSWORD` and talks to the existing instance.
- The app's database (`naturgnosis` by default) is *created inside CouchDB* on first use by
  `bin/sync.py` or `bin/seed_couchdb.py`. Creating a database is not provisioning the service.
- No workflow stops, recreates, or wipes CouchDB. Its data volume is owned outside this repository.

## Environment variables

Set in a repo-root `.env` (never committed; see `.env.example`):

| Variable | Default | Used by |
| -------- | ------- | ------- |
| `COUCHDB_URL` | `http://127.0.0.1:5984` | `sync.py`, `seed_couchdb.py`, deploy scripts (preflight) |
| `COUCHDB_DB` | `naturgnosis` | `sync.py`, `seed_couchdb.py` |
| `COUCHDB_USER` / `COUCHDB_PASSWORD` | — | CouchDB auth (required) |
| `NATURGNOSIS_PORT` | `8011` | public port of the app (host networking) |
| `PORT` | `8000` | container-internal port (set from `NATURGNOSIS_PORT` by compose) |

## Ports

| Port | Service |
| ---- | ------- |
| `5984` | CouchDB (already running in the execution environment) |
| `8011` | Naturgnosis app (`NATURGNOSIS_PORT`; host networking, both local and server) |

## Image contents

The image carries **only the deployed surface**: `bin/` (server), `app/index.html` (landing),
`app/shared/` (theme, images), and each module's `web/` + `data/` (views + JSON). Development-only
content is excluded via `.dockerignore` and must never be needed at runtime:

| Excluded | Why it's dev-only |
| -------- | ----------------- |
| `app/glossary/entries/` | markdown source of truth; deployed reader renders from `data/index.json` (`content` field) |
| `app/*/view/` | long-form notes (e.g. social actor notes) |
| `app/*/import/` | archival third-party exports (provenance) |

## What each workflow assumes vs. creates

| Workflow | Assumes | Creates / does |
| -------- | ------- | -------------- |
| `deploy/deploy_local.sh` | CouchDB reachable with valid creds (preflight) | builds `naturgnosis:local`, `compose up` (app only, host network) as container **`naturgnosis`**, seeds datasets from `app/*/data/data.json` |
| `deploy/deploy_server.sh` | CouchDB reachable, repo-root `.env` present (preflight) | pulls `ghcr.io/csiglab/naturgnosis:latest`, runs the container (`--network host`, mounts `.env`) |
| `bin/sync.py` | CouchDB reachable | creates the `naturgnosis` DB if missing, bootstraps empty datasets from mirrors, serves app + API |
| `bin/seed_couchdb.py` | CouchDB reachable | upserts dataset mirrors into CouchDB |
| GitHub Actions | — | builds & pushes the image to GHCR (no deployment, no CouchDB access) |

## Failure modes & logs

| Condition | Where | What you see |
| --------- | ----- | ------------ |
| CouchDB unreachable / bad creds | deploy scripts (preflight, before any docker call) | `[deploy] ERROR: CouchDB unreachable at … — it is a persistent dependency of the execution environment and is NOT provisioned by this workflow; start it or fix COUCHDB_* in .env` → exit 1 |
| Missing `.env` (server) | `deploy_server.sh` | `[deploy] ERROR: no .env in the repository root.` → exit 1 |
| Missing `COUCHDB_PASSWORD` (compose) | `docker compose config` | `set COUCHDB_PASSWORD (env or .env)` |
| CouchDB unreachable at server start | `bin/sync.py` | `ERROR: cannot reach CouchDB at …` + hint → exit 1 (with `--restart unless-stopped` the container retry-loops until CouchDB returns) |
| CouchDB OK but degraded features | `GET /api/health` | `"status": "degraded"` with `couchdb.ok: false` |
| Intentional offline mode | `bin/sync.py --no-couch` | static serving works, graph API answers `503` |

## Platform note

Both deploy targets use **host networking** (Linux). The dev machine and the server are Linux; on
macOS/Windows (Docker Desktop) `network_mode: host` and `127.0.0.1` inside containers behave
differently and are not supported by these scripts.
