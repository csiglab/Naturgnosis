#!/usr/bin/env python3
"""
Minimal sync server for the Naturgnosis modules.

A single instance serves every module found under the app root
(one directory per module under <app-root>/, e.g. social and production),
exposes a small graph API, and persists nodes to a CouchDB database
(one document per node). A mirror copy of each dataset is also written
to disk so the read-only viewers (index.html) keep working.

Static serving (module-aware):

    /                       -> app/index.html (module registry landing)
    /<module>/              -> 301 /<module>/web/ (relative fetches keep working)
    /<module>/<file>        -> 301 /<module>/web/<file>
    /<module>/web/<file>    -> <app-root>/<module>/web/<file>
    /<module>/data/<file>   -> <app-root>/<module>/data/<file>   (physical path)
    /<module>/view/<file>   -> <app-root>/<module>/view/<file>   (physical path)
    /shared/<file>          -> <app-root>/shared/<file>          (physical path)

API (all same origin):

    GET  /api/graph?dataset=social   -> nodes array for a dataset
    POST /api/graph/save             -> upsert {nodes:[...], dataset} into CouchDB
    POST /api/layout/recompute       -> regenerate layout.json (?dataset= optional)
    GET  /api/health                 -> service + CouchDB status

Usage:

    # Serves every module (web + data + API) from one server:
    python sync.py \
        --app-root app \
        --couch-url http://localhost:5984 \
        --couch-db naturgnosis

    # Legacy single-dataset mode still works:
    python sync.py --data-file app/social/data/data.json

In an editor's Settings -> "Backend Sync" -> "Backend Save URL", enter:

    http://localhost:8000/api/graph/save
"""

import argparse
import base64
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

SAVE_ENDPOINT = "/api/graph/save"


def _load_env():
    """Populate os.environ from <repo>/.env for keys not already set.

    Real environment variables win. Keeps parity with the deployment setup
    where deploy.sh mounts .env into the container.
    """
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return
    with open(env_file, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


_load_env()
LOAD_ENDPOINT = "/api/graph"
HEALTH_ENDPOINT = "/api/health"
LAYOUT_RECOMPUTE_ENDPOINT = "/api/layout/recompute"


class CouchError(Exception):
    """Raised on CouchDB HTTP failures; carries the status code and body."""

    def __init__(self, status, body):
        super().__init__(f"CouchDB HTTP {status}: {body!r}")
        self.status = status
        self.body = body


class CouchClient:
    """Minimal stdlib-only CouchDB client (one dataset <-> many node docs).

    Each graph node is stored as its own CouchDB document. Because a single
    CouchDB database may hold several datasets (e.g. 'prd' and 'idx'), document
    ids are namespaced: '{dataset}:{node_id}'. The node's logical 'id' field is
    preserved verbatim inside each document.
    """

    def __init__(self, base_url, db, user=None, password=None, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.db = db
        self.timeout = timeout
        self._auth = None
        if user and password:
            token = base64.b64encode(
                f"{user}:{password}".encode("utf-8")
            ).decode("ascii")
            self._auth = "Basic " + token

    # ------------------------------------------------------------------
    # Low-level transport
    # ------------------------------------------------------------------
    def _request(self, method, url, body=None):
        data = None
        headers = {"Accept": "application/json"}
        if self._auth:
            headers["Authorization"] = self._auth
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers=headers,
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read()
                return json.loads(raw.decode("utf-8")) if raw else None
        except urllib.error.HTTPError as exc:
            raise CouchError(exc.code, exc.read())
        except urllib.error.URLError as exc:
            raise CouchError(0, str(exc).encode("utf-8"))

    # ------------------------------------------------------------------
    # Database lifecycle
    # ------------------------------------------------------------------
    def db_info(self):
        return self._request("GET", f"{self.base_url}/{self.db}")

    def ensure_db(self):
        """Create the database if it does not exist. Returns True if created."""
        url = f"{self.base_url}/{self.db}"
        try:
            self._request("GET", url)
            return False
        except CouchError as exc:
            if exc.status != 404:
                raise
            self._request("PUT", url)
            return True

    # ------------------------------------------------------------------
    # Dataset read / write
    # ------------------------------------------------------------------
    def get_dataset(self, dataset):
        """Return all node docs for a dataset as a list (node fields only)."""
        startkey = urllib.parse.quote(json.dumps(f"{dataset}:"))
        endkey = urllib.parse.quote(json.dumps(f"{dataset}:\ufff0"))
        url = (
            f"{self.base_url}/{self.db}/_all_docs"
            f"?include_docs=true&startkey={startkey}&endkey={endkey}"
        )
        result = self._request("GET", url)
        nodes = []
        for row in result.get("rows", []):
            doc = row.get("doc")
            if not doc:
                continue
            if str(doc.get("_id", "")).startswith("_design"):
                continue
            doc.pop("_rev", None)
            doc.pop("_id", None)
            nodes.append(doc)
        return nodes

    def _revs(self, dataset, ids):
        """Map 'dataset:node_id' -> current CouchDB rev (for clean upserts)."""
        if not ids:
            return {}
        keys = [f"{dataset}:{i}" for i in ids]
        url = f"{self.base_url}/{self.db}/_all_docs"
        result = self._request("POST", url, {"keys": keys})
        revs = {}
        for row in result.get("rows", []):
            key = row.get("key")
            value = row.get("value") or {}
            if key and value.get("rev"):
                revs[key] = value["rev"]
        return revs

    def bulk_upsert(self, dataset, nodes):
        """Upsert a list of node dicts. Returns the number written."""
        valid = [n for n in nodes if isinstance(n, dict) and n.get("id")]
        if not valid:
            return 0

        revs = self._revs(dataset, [n["id"] for n in valid])

        docs = []
        for node in valid:
            doc = dict(node)  # keeps the node's logical 'id' field verbatim
            couch_id = f"{dataset}:{node['id']}"
            doc["_id"] = couch_id
            if couch_id in revs:
                doc["_rev"] = revs[couch_id]
            docs.append(doc)

        url = f"{self.base_url}/{self.db}/_bulk_docs"
        outcomes = self._request("POST", url, {"docs": docs})

        saved = 0
        for res in outcomes:
            if res.get("ok"):
                saved += 1
        return saved

    def bulk_delete(self, dataset, node_ids):
        """Delete node docs by logical id. Returns the number removed."""
        ids = [i for i in (node_ids or []) if i]
        if not ids:
            return 0

        couch_ids = [f"{dataset}:{i}" for i in ids]
        url = f"{self.base_url}/{self.db}/_all_docs"
        result = self._request("POST", url, {"keys": couch_ids})

        docs = []
        for row in result.get("rows", []):
            value = row.get("value") or {}
            if row.get("id") and value.get("rev"):
                docs.append(
                    {
                        "_id": row["id"],
                        "_rev": value["rev"],
                        "_deleted": True,
                    }
                )

        if not docs:
            return 0

        url = f"{self.base_url}/{self.db}/_bulk_docs"
        outcomes = self._request("POST", url, {"docs": docs})
        return sum(1 for res in outcomes if res.get("ok"))


class SyncHandler(SimpleHTTPRequestHandler):
    """Serves static files and handles graph sync requests.

    A single instance serves every module discovered under the app root
    (one directory per module, each with a data/data.json). Each dataset is
    mirrored to its own data.json so the read-only viewers keep working.
    Module URLs are rewritten: /<module>/x -> /<module>/web/x unless the
    second segment is a non-web subdirectory (data, view, entries, import).
    """

    couch = None                  # CouchClient
    datasets = None               # {module_name: Path(data.json)}
    modules = None                # set of module names (for URL rewriting)

    # Static subdirectories served directly from the module directory
    # (i.e. NOT rewritten into <module>/web/).
    NON_WEB_SUBDIRS = ("web", "data", "view", "entries", "import")

    # ------------------------------------------------------------------
    # CORS
    # ------------------------------------------------------------------

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS",
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type",
        )
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        params = {}
        if "?" in self.path:
            params = urllib.parse.parse_qs(self.path.split("?", 1)[1])

        if path == HEALTH_ENDPOINT:
            self._handle_health()
            return

        if path == LOAD_ENDPOINT:
            self._handle_graph(params)
            return

        # Module URLs redirect to their physical location so that relative
        # fetches inside the pages (e.g. '../data/data.json') resolve at the
        # correct depth. Rewriting content in place would serve pages at a
        # URL depth that does not match the real layout, breaking them.
        if self._is_module_url(self.path):
            target = self._module_redirect_target(self.path)
            if target:
                self.send_response(301)
                self.send_header("Location", target)
                self.send_header("Content-Length", "0")
                self.end_headers()
                return

        super().do_GET()

    # ------------------------------------------------------------------
    # Module-aware static redirects
    # ------------------------------------------------------------------

    def _is_module_url(self, raw):
        """True if the URL's first segment names a known module."""
        seg = raw.split("?", 1)[0].strip("/").split("/", 1)[0]
        return bool(seg) and seg in (self.modules or set())

    def _module_redirect_target(self, raw):
        """301 target for /<module>/... -> /<module>/web/..., or None.

        Paths already at their physical location (web/, data/, view/,
        entries/, import/ subpaths) need no redirect.
        """
        parts = raw.split("?", 1)
        path, query = parts[0], (parts[1] if len(parts) > 1 else "")

        segs = [s for s in path.split("/") if s]
        module, rest = segs[0], segs[1:]

        if not rest:
            new = f"/{module}/web/"
        elif rest[0] in self.NON_WEB_SUBDIRS:
            return None
        else:
            new = "/" + "/".join([module, "web"] + rest)
            if path.endswith("/"):
                new += "/"

        if query:
            new += "?" + query
        return new

    def _default_dataset(self):
        names = sorted(self.datasets or {})
        return names[0] if names else None

    def _handle_graph(self, params):
        """GET /api/graph?dataset=social|production -> nodes from CouchDB."""
        dataset = (params.get("dataset") or [self._default_dataset()])[0]
        if not dataset:
            self._send_json(
                {"status": "error", "message": "No datasets configured."},
                500,
            )
            return
        if self.couch is None:
            self._send_json(
                {
                    "status": "error",
                    "message": "Offline mode (--no-couch): no backend.",
                    "dataset": dataset,
                },
                503,
            )
            return
        try:
            nodes = self.couch.get_dataset(dataset)
            self._send_json(nodes)
        except CouchError as exc:
            sys.stderr.write(f"[sync] couch read error: {exc}\n")
            self._send_json(
                {
                    "status": "error",
                    "message": f"CouchDB: {exc}",
                    "dataset": dataset,
                },
                502,
            )

    def _handle_health(self):
        couch_ok = False
        couch_info = None
        if self.couch is not None:
            try:
                couch_info = self.couch.db_info()
                couch_ok = True
            except Exception as exc:
                couch_info = {"error": str(exc)}
        else:
            couch_info = {"error": "offline mode (--no-couch)"}

        datasets_info = {}
        for name, path in (self.datasets or {}).items():
            datasets_info[name] = {
                "data_file": str(path),
                "exists": path.exists(),
                "size": path.stat().st_size if path.exists() else None,
            }

        self._send_json(
            {
                "status": "ok" if couch_ok else "degraded",
                "service": "naturgnosis-sync",
                "datasets": datasets_info,
                "couchdb": {
                    "url": (
                        f"{self.couch.base_url}/{self.couch.db}"
                        if self.couch is not None
                        else None
                    ),
                    "ok": couch_ok,
                    "info": couch_info,
                },
            }
        )

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        params = {}
        if "?" in self.path:
            params = urllib.parse.parse_qs(self.path.split("?", 1)[1])

        if path == SAVE_ENDPOINT:
            self._handle_save()
        elif path == LAYOUT_RECOMPUTE_ENDPOINT:
            self._handle_layout_recompute(params)
        else:
            self.send_error(404, "Not Found")

    def _handle_save(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"

            patch = json.loads(raw)
            changed = patch.get("nodes", [])
            deleted_ids = patch.get("delete_ids", [])
            dataset = patch.get("dataset") or self._default_dataset()

            if self.couch is None:
                self._send_json(
                    {
                        "status": "error",
                        "message": "Offline mode (--no-couch): saves disabled.",
                    },
                    503,
                )
                return

            if not changed and not deleted_ids:
                self._send_json(
                    {"status": "ok", "saved": 0, "dataset": dataset}
                )
                return

            saved = self.couch.bulk_upsert(dataset, changed)
            deleted = self.couch.bulk_delete(dataset, deleted_ids)

            # Mirror the full dataset to disk so the read-only viewers
            # (index.html) keep working off the static data.json.
            mirrored = False
            data_file = (self.datasets or {}).get(dataset)
            if data_file:
                full = self.couch.get_dataset(dataset)
                self._write_data_file(full, data_file)
                mirrored = True
            else:
                sys.stderr.write(
                    f"[sync] no on-disk mirror for dataset '{dataset}'; "
                    f"saved to CouchDB only.\n"
                )

            self._send_json(
                {
                    "status": "ok",
                    "saved": saved,
                    "deleted": deleted,
                    "timestamp": patch.get("timestamp", ""),
                    "dataset": dataset,
                    "mirrored": mirrored,
                }
            )

        except json.JSONDecodeError as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": f"Invalid JSON: {exc}",
                },
                400,
            )

        except CouchError as exc:
            sys.stderr.write(f"[sync] couch write error: {exc}\n")
            self._send_json(
                {
                    "status": "error",
                    "message": f"CouchDB: {exc}",
                },
                502,
            )

        except Exception as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": str(exc),
                },
                500,
            )

    def _write_data_file(self, data, data_file):
        """Atomically write the full node list to the on-disk mirror."""
        data_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        tmp_fd, tmp_path = tempfile.mkstemp(
            suffix=".tmp",
            dir=str(data_file.parent),
        )

        try:
            with os.fdopen(
                tmp_fd,
                "w",
                encoding="utf-8",
            ) as fh:
                json.dump(
                    data,
                    fh,
                    indent=2,
                    ensure_ascii=False,
                )

                os.replace(tmp_path, data_file)
                os.chmod(data_file, 0o644)  # Owner-writable (safer default).

        except Exception:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise

    # ------------------------------------------------------------------
    # Layout recompute endpoint (on demand from the editor)
    # ------------------------------------------------------------------

    def _handle_layout_recompute(self, params):
        """POST /api/layout/recompute?dataset=social -> regenerate layout.json.

        If no dataset is given, every known dataset is recomputed. Decoupled
        from save so saves stay fast; the editor calls this explicitly (e.g. its
        "Recompute Layout" button). Datasets without a usable layout are skipped.
        """
        try:
            requested = (params.get("dataset") or [None])[0]
            targets = (
                [requested]
                if requested
                else sorted(self.datasets or {})
            )

            results = {}
            had_error = False
            for name in targets:
                data_file = (self.datasets or {}).get(name)
                if not data_file or not data_file.exists():
                    continue
                res = self._recompute_layout(data_file)
                results[name] = res
                if "layout_error" in res:
                    had_error = True

            status = "error" if had_error else "ok"
            code = 500 if had_error else 200
            self._send_json({"status": status, "datasets": results}, code)
        except Exception as exc:  # pragma: no cover - defensive
            self._send_json(
                {"status": "error", "message": str(exc)},
                500,
            )

    # ------------------------------------------------------------------
    # Layout recompute helper
    # ------------------------------------------------------------------

    def _recompute_layout(self, data_file):
        """Recompute layout.json (sibling of data file) via bin/layout.py.

        Best-effort: a layout failure is reported, not raised. Returns a dict
        consumed by the recompute response handler.
        """
        layout_file = data_file.parent / "layout.json"
        try:
            bin_dir = os.path.dirname(os.path.abspath(__file__))
            if bin_dir not in sys.path:
                sys.path.insert(0, bin_dir)
            import layout as layout_mod  # noqa: E402

            node_count, elapsed = layout_mod.recompute(
                data_file,
                layout_file,
            )
            sys.stderr.write(
                f"[sync] layout recomputed: {node_count} nodes "
                f"in {elapsed * 1000:.0f} ms -> {layout_file}\n"
            )
            return {
                "layout": "recomputed",
                "layout_nodes": node_count,
                "layout_ms": int(elapsed * 1000),
            }
        except Exception as exc:  # pragma: no cover - defensive
            sys.stderr.write(f"[sync] layout recompute failed: {exc}\n")
            return {"layout_error": str(exc)}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _send_json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")

        self.send_response(code)
        self.send_header(
            "Content-Type",
            "application/json",
        )
        self.send_header(
            "Content-Length",
            str(len(body)),
        )
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            f"[sync] {self.address_string()} - {fmt % args}\n"
        )


def maybe_bootstrap(couch, dataset, data_file):
    """Seed CouchDB for a dataset from the on-disk data file if it is empty.

    Lets the editor read through the API immediately, without a manual import
    step, the first time sync.py is pointed at a fresh database.
    """
    try:
        existing = couch.get_dataset(dataset)
    except CouchError as exc:
        sys.stderr.write(
            f"[sync] cannot read dataset '{dataset}' from CouchDB: {exc}\n"
        )
        return

    if existing:
        return

    if not data_file.exists():
        return

    try:
        with open(data_file, "r", encoding="utf-8") as fh:
            seed = json.load(fh)
    except Exception as exc:
        sys.stderr.write(
            f"[sync] cannot read seed file {data_file}: {exc}\n"
        )
        return

    if not isinstance(seed, list):
        return

    nodes = [n for n in seed if isinstance(n, dict) and n.get("id")]
    if not nodes:
        return

    written = couch.bulk_upsert(dataset, nodes)
    sys.stderr.write(
        f"[sync] bootstrapped {written} nodes from {data_file} "
        f"into '{couch.db}:{dataset}'\n"
    )


NON_MODULE_DIRS = ("shared",)


def discover_modules(app_root):
    """Return the set of module names: every directory under <app_root>/.

    Used for static URL rewriting (/<module>/... -> <module>/web/...) so that
    modules WITHOUT a graph dataset (e.g. glossary, which serves a generated
    index instead of data.json) still get clean module URLs.
    """
    app_root = Path(app_root)
    modules = set()
    if app_root.is_dir():
        for child in sorted(app_root.iterdir()):
            if child.is_dir() and child.name not in NON_MODULE_DIRS:
                modules.add(child.name)
    return modules


def discover_datasets(app_root):
    """Return {module_name: Path(data.json)} for <app_root>/<module>/data/data.json.

    The subset of modules that carry a graph dataset: these drive the sync
    API (load/save), CouchDB bootstrap, and seeding. The module name doubles
    as the dataset id.
    """
    app_root = Path(app_root)
    datasets = {}
    if app_root.is_dir():
        for child in sorted(app_root.iterdir()):
            if not child.is_dir() or child.name in NON_MODULE_DIRS:
                continue
            data_file = child / "data" / "data.json"
            if data_file.exists():
                datasets[child.name] = data_file.resolve()
    return datasets


def main():
    parser = argparse.ArgumentParser(
        prog="sync.py",
        description=(
            "Sync server for the Naturgnosis modules. Serves every module "
            "under <app-root>/ from a single instance."
        ),
    )

    parser.add_argument(
        "--app-root",
        default=None,
        help=(
            "Directory served statically; contains one directory per module. "
            "Defaults to the repo 'app' dir (or derived from --data-file)."
        ),
    )

    parser.add_argument(
        "--data-file",
        default=None,
        help=(
            "Optional legacy path to a single dataset's data.json. Used to "
            "derive --app-root; modern usage prefers --app-root."
        ),
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8001,
        help="Port to listen on (default: 8001).",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0).",
    )

    parser.add_argument(
        "--couch-url",
        default=os.environ.get("COUCHDB_URL", "http://localhost:5984"),
        help=(
            "CouchDB base URL (default: $COUCHDB_URL or "
            "http://localhost:5984)."
        ),
    )

    parser.add_argument(
        "--couch-db",
        default=os.environ.get("COUCHDB_DB", "naturgnosis"),
        help="CouchDB database name (default: $COUCHDB_DB or naturgnosis).",
    )

    parser.add_argument(
        "--couch-user",
        default=os.environ.get("COUCHDB_USER"),
        help="CouchDB user (optional; default: $COUCHDB_USER).",
    )

    parser.add_argument(
        "--couch-password",
        default=os.environ.get("COUCHDB_PASSWORD"),
        help="CouchDB user (optional; default: $COUCHDB_PASSWORD).",
    )

    parser.add_argument(
        "--no-couch",
        action="store_true",
        help=(
            "Offline mode: skip CouchDB entirely. Static serving works; "
            "graph read/save endpoints answer with an error. Useful for "
            "local development and CI checks."
        ),
    )

    args = parser.parse_args()

    # Resolve the app root (the static-serving directory).
    if args.app_root:
        app_root = Path(args.app_root).resolve()
    elif args.data_file:
        # app/<module>/data/data.json -> app
        app_root = Path(args.data_file).resolve().parents[2]
    else:
        # Default: <repo>/app (bin/ is a sibling of app/).
        app_root = (Path(__file__).resolve().parent.parent / "app").resolve()

    if not app_root.is_dir():
        print(
            f"ERROR: app root not found: {app_root}",
            file=sys.stderr,
        )
        sys.exit(1)

    datasets = discover_datasets(app_root)
    modules = discover_modules(app_root)

    # Legacy --data-file: make sure that specific dataset is included even if
    # it lives outside the discovered tree.
    if args.data_file:
        df = Path(args.data_file).resolve()
        datasets.setdefault(df.parent.parent.name, df)

    if not datasets:
        print(
            f"WARNING: no datasets found under {app_root}/*/data/data.json",
            file=sys.stderr,
        )

    if args.no_couch:
        couch = None
        print(
            "[sync] --no-couch: running offline (static serving only)",
            file=sys.stderr,
        )
    else:
        couch = CouchClient(
            args.couch_url,
            args.couch_db,
            user=args.couch_user,
            password=args.couch_password,
        )

        try:
            created = couch.ensure_db()
            if created:
                print(
                    f"[sync] created CouchDB database '{args.couch_db}'",
                    file=sys.stderr,
                )
        except CouchError as exc:
            print(
                f"ERROR: cannot reach CouchDB at {args.couch_url}: {exc}\n"
                f"       CouchDB is a persistent dependency of the execution "
                f"environment and is NOT provisioned by deployment workflows — "
                f"start it or fix COUCHDB_* in .env (see deploy/README.md).",
                file=sys.stderr,
            )
            sys.exit(1)

        for name, data_file in datasets.items():
            maybe_bootstrap(couch, name, data_file)

    SyncHandler.couch = couch
    SyncHandler.datasets = datasets
    SyncHandler.modules = modules

    handler = partial(
        SyncHandler,
        directory=str(app_root),
    )

    server = HTTPServer(
        (args.host, args.port),
        handler,
    )

    display_host = (
        "localhost"
        if args.host in ("0.0.0.0", "::")
        else args.host
    )

    ds_list = ", ".join(sorted(datasets)) or "(none)"

    print("══════════════════════════════════════════════")
    print("  Naturgnosis Sync Server")
    print("──────────────────────────────────────────────")
    print(f"  Modules:  {ds_list}  (CouchDB: {args.couch_db})")
    print(f"  Root:     {app_root}")
    for name in sorted(datasets):
        print(
            f"  Load:    http://{display_host}:{args.port}{LOAD_ENDPOINT}?dataset={name}"
        )
        print(
            f"  App:     http://{display_host}:{args.port}/{name}/"
        )
    print(
        f"  Save:    http://{display_host}:{args.port}{SAVE_ENDPOINT}"
    )
    print(
        f"  Layout:  http://{display_host}:{args.port}{LAYOUT_RECOMPUTE_ENDPOINT}"
    )
    print(
        f"  Health:  http://{display_host}:{args.port}{HEALTH_ENDPOINT}"
    )
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
