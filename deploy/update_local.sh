#!/usr/bin/env bash
# Local update: refresh the RUNNING app container without rebuilding the image.
#
# Copies the deployed surface (bin/ + app/, minus .dockerignore excludes)
# into container `naturgnosis`, restarts it, and waits for health.
# No image build, no CouchDB provisioning, and by default no seeding either
# (SEED=1 opts into `bin/seed_couchdb.py`, the same command deploy_local.sh
# uses after a full deploy).
#
# Still needs `make deploy-local`: Dockerfile/.dockerignore changes, .env or
# credential changes (env is baked at container creation — a restart will not
# pick it up), and any new system dependencies.
#
# CouchDB is a persistent dependency of the execution environment — this
# script never provisions it.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CONTAINER="naturgnosis"

cd "${ROOT}"

if ! docker inspect "${CONTAINER}" >/dev/null 2>&1; then
  echo "[update] ERROR: container '${CONTAINER}' does not exist — run \`make deploy-local\` first." >&2
  exit 1
fi
if [ "$(docker inspect -f '{{.State.Running}}' "${CONTAINER}")" != "true" ]; then
  echo "[update] ERROR: container '${CONTAINER}' is not running — run \`make deploy-local\` first." >&2
  exit 1
fi

# .env only for the PORT display below; never committed, never required here.
if [ -f "${ROOT}/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "${ROOT}/.env"
  set +a
fi

echo "[update] Syncing bin/ + app/ into '${CONTAINER}' (honoring .dockerignore)…"
if docker exec "${CONTAINER}" tar --version >/dev/null 2>&1; then
  tar -C "${ROOT}" \
    --exclude='app/*/entries' --exclude='app/*/view' --exclude='app/*/import' \
    -cf - app bin | docker exec -i "${CONTAINER}" tar -xf - -C /srv
else
  echo "[update] NOTE: no tar in container — falling back to docker cp + cleanup." >&2
  docker cp "${ROOT}/app/." "${CONTAINER}:/srv/app/"
  docker cp "${ROOT}/bin/." "${CONTAINER}:/srv/bin/"
  docker exec "${CONTAINER}" sh -c 'rm -rf /srv/app/*/entries /srv/app/*/view /srv/app/*/import'
fi

if [ "${SEED:-0}" = "1" ]; then
  echo "[update] Seeding datasets from the freshly synced mirrors…"
  docker exec -T "${CONTAINER}" python bin/seed_couchdb.py
fi

echo "[update] Restarting '${CONTAINER}'…"
docker restart "${CONTAINER}" >/dev/null

PORT="${NATURGNOSIS_PORT:-8011}"
echo "[update] Waiting for health…"
for _ in $(seq 1 30); do
  if curl -sf "http://localhost:${PORT}/api/health" >/dev/null 2>&1; then
    echo
    echo "[update] Naturgnosis updated:  http://localhost:${PORT}/"
    exit 0
  fi
  sleep 1
done
echo "[update] ERROR: container did not become healthy in 30s — check \`docker logs naturgnosis\`." >&2
exit 1
