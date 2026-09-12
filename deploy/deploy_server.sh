#!/bin/sh
# Server deployment: pull the published image from GHCR and (re)start the app
# container with host networking.
#
# CouchDB is a persistent dependency of the execution environment — this
# script never provisions it; it only verifies it is reachable (preflight).
# Credentials come from the repo-root .env (never committed).
set -eu

IMAGE="ghcr.io/csiglab/naturgnosis:latest"
CONTAINER="naturgnosis"
PORT="${NATURGNOSIS_PORT:-8011}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "${SCRIPT_DIR}/.."

# Load .env so the preflight can verify CouchDB connectivity.
if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
else
  echo "[deploy] ERROR: no .env in the repository root." >&2
  echo "[deploy] Without COUCHDB_* credentials the app cannot connect to CouchDB." >&2
  echo "[deploy] See deploy/README.md for the required variables." >&2
  exit 1
fi

# shellcheck disable=SC1091
. "${SCRIPT_DIR}/preflight.sh"
preflight_couchdb

# Mount the repo's .env into the container (CouchDB credentials etc.).
ENV_MOUNT="-v ${PWD}/.env:/srv/.env:ro"

docker pull "$IMAGE"
docker rm -f "$CONTAINER" 2>/dev/null || true
# shellcheck disable=SC2086
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  --network host \
  $ENV_MOUNT \
  "$IMAGE" \
  python bin/sync.py --app-root /srv/app --port "$PORT"
