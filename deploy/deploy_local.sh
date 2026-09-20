#!/usr/bin/env bash
# Local deployment: build the app image and start it with compose, then seed
# CouchDB from the on-disk dataset mirrors.
#
# CouchDB is a persistent dependency of the execution environment — this
# script never provisions it; it only verifies it is reachable (preflight).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${SCRIPT_DIR}"

# Load .env (never committed) so COUCHDB_* / NATURGNOSIS_PORT are available
# to the preflight, to compose variable substitution, and inside the container.
ENV_ARGS=()
if [ -f "${ROOT}/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "${ROOT}/.env"
  set +a
  ENV_ARGS=(--env-file "${ROOT}/.env")
else
  echo "[deploy] NOTE: no ${ROOT}/.env — relying on exported COUCHDB_* variables" >&2
fi

# shellcheck disable=SC1091
. "${SCRIPT_DIR}/preflight.sh"
preflight_couchdb

echo "[deploy] Building and starting the app (compose, host network)…"
docker compose "${ENV_ARGS[@]}" -f docker-compose.yml up -d --build

# Give the app a moment to bootstrap datasets before the explicit seed.
sleep 3

echo "[deploy] Seeding datasets (social, production, research, nation, technique, epistemica)…"
docker compose "${ENV_ARGS[@]}" -f docker-compose.yml exec -T app python bin/seed_couchdb.py

PORT="${NATURGNOSIS_PORT:-8011}"
echo
echo "[deploy] Naturgnosis is up:  http://localhost:${PORT}/"
