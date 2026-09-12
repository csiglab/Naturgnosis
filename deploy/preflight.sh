#!/bin/sh
# Shared preflight for deployment scripts: verify the execution environment
# provides CouchDB. This repo NEVER provisions, redeploys, or removes CouchDB —
# it is a persistent, data-bearing dependency; we only connect to it.
#
# Usage: source this file, then call `preflight_couchdb`.
# Expects COUCHDB_URL / COUCHDB_USER / COUCHDB_PASSWORD in the environment
# (the caller loads .env first when present).
#
# See deploy/README.md ("Execution Environment") for the full contract.

preflight_couchdb() {
  if [ -z "${COUCHDB_URL:-}" ]; then
    echo "[deploy] ERROR: COUCHDB_URL is not set." >&2
    echo "[deploy] CouchDB is a persistent dependency of the execution environment" >&2
    echo "[deploy] and is NOT provisioned by this workflow — start it or fix" >&2
    echo "[deploy] COUCHDB_* in .env (see deploy/README.md)." >&2
    return 1
  fi

  if [ -z "${COUCHDB_USER:-}" ] || [ -z "${COUCHDB_PASSWORD:-}" ]; then
    echo "[deploy] ERROR: COUCHDB_USER/COUCHDB_PASSWORD are not set." >&2
    echo "[deploy] Without credentials the app cannot connect to CouchDB." >&2
    echo "[deploy] Fix them in .env (see deploy/README.md)." >&2
    return 1
  fi

  echo "[deploy] Checking CouchDB at ${COUCHDB_URL} …"
  if ! curl -sf -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" "${COUCHDB_URL}/_up" >/dev/null 2>&1; then
    echo "[deploy] ERROR: CouchDB unreachable at ${COUCHDB_URL}." >&2
    echo "[deploy] CouchDB is a persistent dependency of the execution environment" >&2
    echo "[deploy] and is NOT provisioned by this workflow — start it or fix" >&2
    echo "[deploy] COUCHDB_* in .env (see deploy/README.md)." >&2
    return 1
  fi
  echo "[deploy] CouchDB is up."
}
