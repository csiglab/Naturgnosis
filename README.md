# Naturgnosis

> **Naturgnosis** aims to identify and formalize the set of epistemic elements that enable an agent to
> effectively navigate (understanding and action) reality — especially social reality.

> **Naturgnosis** will serve as the main index of the world's **technique** and **episteme**, while
> **Epistecnica** will focus on what man intentionally pursues through deep study and some level of
> mastery, specifically for **@dbremont**.

Goals:

- We aim to stabilize a generative system that produces a **Domain Epistemic Artifact Set (DESA)**
  representing social reality and rendering it intelligible as a structured domain of analysis and
  action.
- We aim to study, **refine, and improve the underlying generative system** that produces and
  organizes the DESA, with emphasis on consistency, expressiveness, and explanatory power.
- We aim to connect the DESA to practical **activity systems**, such that epistemic artifacts are
  systematically linked to real-world actions, interventions, and decision-making processes within
  social domains.

## Modules

Every module is a complete app under `app/<module>/` (views + data + spec + AGENTS.md), served by one
server (`bin/sync.py`) and shipped as one image.

| Module | Route | Editor | Storage |
| ------ | ----- | ------ | ------- |
| Social Space (main) | `/social/` | `/social/edit.html` | CouchDB `dataset=social` + mirror |
| Production Space | `/production/` | `/production/edit.html` | CouchDB `dataset=production` + mirror |
| Research Space | `/research/` | `/research/edit.html` | CouchDB `dataset=research` + mirror |
| Nation Space | `/nation/` | `/nation/edit.html` | CouchDB `dataset=nation` + mirror |

See `spec/README.md` for the global specification and `spec/<module>/README.md` per module.

## Deployment

One image (`ghcr.io/csiglab/naturgnosis:latest`, built by GitHub Actions on push to `main`), two
targets. **CouchDB is a persistent dependency of the execution environment — no workflow ever
provisions, redeploys, or removes it.** Both targets only connect to it via `COUCHDB_*` variables
and preflight-check it before deploying; see `deploy/README.md` for the full contract.

### Local

```sh
cp .env.example .env            # set COUCHDB_* credentials of the running CouchDB
./deploy/deploy_local.sh
```

`deploy/deploy_local.sh` verifies CouchDB is reachable (clear failure log if not), builds and
starts the app (compose, host network), and seeds all datasets. App: <http://localhost:8011/>.
Override the port with `NATURGNOSIS_PORT`.

### Server

CouchDB must already run on the host; put credentials in a repo-root `.env`:

```sh
COUCHDB_URL=http://127.0.0.1:5984
COUCHDB_DB=naturgnosis
COUCHDB_USER=...
COUCHDB_PASSWORD=...
```

Then:

```sh
./deploy/deploy_server.sh       # preflights CouchDB, pulls the GHCR image, runs with --network host on :8011
```

### Development

```sh
python bin/sync.py --no-couch   # offline: static serving only (API returns 503)
python bin/sync.py              # full: needs CouchDB + .env
make build                      # regenerate graph layouts
make seed                       # push mirrors into CouchDB
```

## Data Sync

> Changes are stored on the server (CouchDB), which is not connected to GitHub. Therefore, download
> the latest mirror before committing dataset updates.

```bash
# on the server, after editors have saved:
rsync server:naturgnosis/app/social/data/data.json   app/social/data/data.json
git add app && git commit -m "feat(data): update mirrors"
```

(`bin/sync.py` rewrites `app/<module>/data/data.json` after every editor save; never edit those
files by hand.)

## API

- `GET  /api/health` — service + CouchDB status
- `GET  /api/graph?dataset=social|production|research|nation` — nodes
- `POST /api/graph/save` — `{dataset, nodes[], delete_ids?[]}` (upsert/delete + mirror)
- `POST /api/layout/recompute?dataset=…` — regenerate `layout.json`

## Notes

- **Social Space** will support market analysis — not the direct analysis of production processes or
  technology (that is Production Space).
- The served root is `app/`; there is no `docs/` directory anymore.

## References

- [Actor](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Noetic/Actor/)
- [Actor Space](https://www.bremontix.xyz/lab/ar/Locus-Instrumentorum/Toolset/Representation/Space/Actor/Actor/)
- [Representation](https://www.bremontix.xyz/lab/ar/Locus-Instrumentorum/Toolset/Representation/)
- [Interaction Unit](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Guide/Unit/)
- [Social Ontology](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Guide/)
- [Section of Reality Template](https://app.notion.com/p/Section-of-Reality-Template-334c0f5171ec804b8115c177dbc245a8?source=copy_link)
- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?source=copy_link)
- [Graphify](https://github.com/safishamsi/graphify)
- [Index Gentium](https://github.com/csiglab/research-CountryIndex)
