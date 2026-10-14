#!/usr/bin/env python3
"""
Polity manifest builder (note corpus).

Scans app/note/data/social/actor/public/polity/** for per-nation content —
markdown (*.md, kind "explanation") and self-contained HTML live notes
(*.html, kind "representation") — and emits polity/data.json, the data
source for the polity aggregator live note (polity/index.html: flag grid +
nation search, each flag opening its polity/<code>/index.html page). Stdlib
only.

For each entry it records: path (relative to the note data dir), title
(markdown: first "# " heading; html: <title>, else first <h1>; fallback:
the filename), and kind. Entries group by first path segment under
polity/ (the country code dir); world.md and international/ get their own
top-level sections. Display names and flags come from each polity's node
file (polity/<code>/data/node.json; see polity_nodes()); otherwise the
title of the shallowest note in the dir, else the uppercased code.

Each polity owns its node under data/node.json (the nation dataset mirror
was dissolved into these files; they are the source of truth). The manifest
does not write or duplicate nodes — but it does recompute each polity's
`works` from its directory: every representation (.html) and explanation
(.md) becomes a work, typed by convention (work_type(): name -> type,
explanations are always `note`), status direct (a derived work always has a
backing file => active), with a polity-relative link. Per-path type
overrides live in the optional polity/dynamics.json.

Usage: python3 bin/build_polity_index.py [--views-only]

After writing the manifest, stamps per-nation pages from the canonical
originals (spec/polity/entry.html -> every polity/<code>/index.html,
spec/polity/actor.html -> polity/<code>/actor.html where a same-code actor
dataset exists). Only <title> is baked per code; see spec/polity/README.md).

With --views-only, the manifest is not rewritten: the canonical views are
simply copied to their per-code destinations (see `make polity-views`).
"""

import argparse
import json
import re
import sys
from datetime import date
from html import unescape
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "app" / "note" / "data"
POLITY = DATA / "social" / "actor" / "public" / "polity"
OUT = POLITY / "data.json"
ENTRY_TEMPLATE = REPO / "spec" / "polity" / "entry.html"
ACTOR_TEMPLATE = REPO / "spec" / "polity" / "actor.html"
SCHEMA_DIR = REPO / "spec" / "polity"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
HTML_H_RE = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
FALLBACK_FLAG = "\U0001F3F3\uFE0F"

# Work-type convention (name -> type). A polity's works are derived from its
# directory (representations + explanations), never hand-listed in node.json.
WORK_TYPE_KEYWORDS = (
    ("Network", ("network", "graph", "chain", "cluster", "corridor")),
    ("Spatial", ("spatial", "map", "region", "geographic", "territor", "urban")),
    ("Temporal", ("actor", "timeline", "evolution", "history", "temporal", "chronolog")),
)


def work_type(kind: str, *names: str) -> str:
    """Convention: derive a work type from the corpus kind and its name.

    Explanations are always `note`. Representations are typed by keyword on
    their title/filename (default `Temporal`). Override per path via
    polity/dynamics.json (see spec/polity/README.md).
    """
    if kind == "explanation":
        return "note"
    blob = " ".join(n for n in names if n).lower()
    for type_name, keys in WORK_TYPE_KEYWORDS:
        if any(k in blob for k in keys):
            return type_name
    return "Temporal"


def md_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line.strip())
        if m:
            return m.group(2).strip()
    return path.stem


def html_title(path: Path) -> str:
    body = path.read_text(encoding="utf-8")
    m = HTML_TITLE_RE.search(body)
    if m:
        return unescape(HTML_TAG_RE.sub("", m.group(1))).strip()
    m = HTML_H_RE.search(body)
    if m:
        return unescape(HTML_TAG_RE.sub("", m.group(2))).strip()
    return path.stem


def polity_nodes() -> dict:
    """Polity source of truth: read every polity node file under polity/.

    Nodes live as raw node objects at polity/<code>/data/node.json (or
    polity/<iso>-node.json for codes without a directory). Returns
    {id: {name, native, flag}}. The nation dataset mirror was dissolved
    into these files; they are the source of truth (spec/polity/README.md).
    """
    reg = {}
    for path in list(POLITY.glob("*/data/node.json")) + list(POLITY.glob("*-node.json")):
        try:
            n = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"polity-index: WARNING: node file unreadable ({path.name}: {exc})")
            continue
        if not isinstance(n, dict) or not n.get("id"):
            continue
        sp = n.get("specific", {}) if isinstance(n.get("specific"), dict) else {}
        reg[n["id"]] = {
            "name": n.get("name") or n["id"].upper(),
            "native": sp.get("nativeName") or "",
            "flag": sp.get("flagEmoji") or FALLBACK_FLAG,
        }
    return reg


def load_overrides() -> dict:
    """Optional manual overrides: polity/dynamics.json {corpus-path: {type}}.

    Lets an author pin a work's type when the name convention guesses wrong.
    Unknown shapes are ignored (the build never fails on it).
    """
    dynamics = POLITY / "dynamics.json"
    if not dynamics.is_file():
        return {}
    try:
        raw = json.loads(dynamics.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"polity-index: WARNING: dynamics.json unreadable ({exc})")
        return {}
    out = {}
    if isinstance(raw, dict):
        for path, spec in raw.items():
            if isinstance(spec, dict) and spec.get("type"):
                out[path] = spec["type"]
    return out


def _resolve(doc: dict, node: dict) -> dict:
    """Follow in-document $ref chains until a concrete node is reached."""
    seen = 0
    while isinstance(node, dict) and "$ref" in node:
        cur = doc
        for part in node["$ref"].split("/")[1:]:
            cur = cur[part.replace("~1", "/").replace("~0", "~")]
        node = cur
        seen += 1
        if seen > 32:
            break
    return node


def _check(data, doc: dict, node: dict, where: str, warns: list):
    """Structural check: required keys, key order, and array/item recursion.

    Stdlib only; never does full JSON-Schema validation. Warn-only contract:
    the caller collects and prints, the build never fails.
    """
    node = _resolve(doc, node)
    if not isinstance(node, dict):
        return
    if isinstance(data, dict):
        props = node.get("properties", {})
        for req in node.get("required", []):
            if req not in data:
                warns.append(f"{where}: missing required key '{req}'")
        known = [k for k in data if k in props]
        order = [k for k in props if k in data]
        if known != order:
            warns.append(f"{where}: key order {known} != schema {order}")
        for k, v in data.items():
            if k in props:
                _check(v, doc, props[k], f"{where}.{k}", warns)
        ap = node.get("additionalProperties")
        if isinstance(ap, dict):
            for k, v in data.items():
                if k not in props:
                    _check(v, doc, ap, f"{where}.{k}", warns)
    elif isinstance(data, list) and isinstance(node.get("items"), dict):
        for i, el in enumerate(data):
            _check(el, doc, node["items"], f"{where}[{i}]", warns)


def validate_schemas(warns: list):
    """Check every polity JSON against its schema in spec/polity/ (warn-only)."""
    pairs = [
        ("data.schema.json", [OUT]),
        ("node.schema.json",
         list(POLITY.glob("*/data/node.json")) + list(POLITY.glob("*-node.json"))),
        ("actors.schema.json", list(POLITY.glob("*/data/actors.json"))),
        ("dynamics.schema.json", [POLITY / "dynamics.json"]),
    ]
    for schema_name, files in pairs:
        schema_path = SCHEMA_DIR / schema_name
        try:
            doc = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"polity-index: WARNING: schema unreadable ({schema_name}: {exc})")
            continue
        for path in files:
            if not path.is_file():
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                warns.append(f"{path.relative_to(REPO)}: unreadable ({exc})")
                continue
            _check(data, doc, doc, str(path.relative_to(REPO)), warns)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the polity manifest and/or stamp per-nation views.")
    parser.add_argument("--views-only", action="store_true",
                        help="copy spec/polity/ canonical views to polity/<code>/ without rewriting the manifest")
    args = parser.parse_args(argv)

    if not POLITY.is_dir():
        print(f"ERROR: polity directory not found: {POLITY}", file=sys.stderr)
        return 1

    reg = polity_nodes()
    overrides = load_overrides()
    codes: dict = {}
    world: list = []
    international: list = []

    for path in sorted(POLITY.rglob("*")):
        if not path.is_file() or path.suffix not in (".md", ".html"):
            continue
        if path.name in ("index.html",):
            continue  # the aggregator itself, not content
        rel = path.relative_to(DATA).as_posix()
        kind = "explanation" if path.suffix == ".md" else "representation"
        title = md_title(path) if kind == "explanation" else html_title(path)
        entry = {"path": rel, "title": title, "kind": kind}
        top = path.relative_to(POLITY).parts[0]
        if top == "world.md":
            world.append(entry)
        elif top == "international":
            international.append(entry)
        else:
            codes.setdefault(top, []).append(entry)

    payload_codes = {}
    for code in sorted(codes):
        notes = sorted(codes[code], key=lambda e: (e["kind"] != "explanation", e["path"]))
        # Works are recomputed from the directory: representations first,
        # then explanations. type by convention; status is direct (a derived
        # work always has a backing file => active).
        works = []
        for e in sorted(notes, key=lambda e: (e["kind"] != "representation", e["path"])):
            rel = e["path"].split("polity/", 1)[1]           # "<code>/<rest>"
            link = rel.split("/", 1)[1] if "/" in rel else rel
            if e["kind"] == "explanation":
                link = "../../../../../../web/note.html?n=" + e["path"]
            works.append({
                "id": e["path"].rsplit("/", 1)[-1].rsplit(".", 1)[0],
                "type": overrides.get(e["path"]) or work_type(e["kind"], e["title"], e["path"]),
                "status": "active",
                "title": e["title"],
                "link": link,
            })
        if code in reg:
            meta = reg[code]
            name, native, flag, has_node = meta["name"], meta["native"], meta["flag"], True
        else:
            shallow = min(notes, key=lambda e: e["path"].count("/"))
            name, native, flag, has_node = shallow["title"], "", FALLBACK_FLAG, False
        payload_codes[code] = {
            "name": name,
            "native": native,
            "flag": flag,
            "has_node": has_node,
            "counts": {
                "explanation": sum(1 for e in notes if e["kind"] == "explanation"),
                "representation": sum(1 for e in notes if e["kind"] == "representation"),
            },
            "works": works,
            "notes": notes,
        }

    payload = {
        "generated": date.today().isoformat(),
        "root": "social/actor/public/polity",
        "count": sum(len(v) for v in codes.values()) + len(world) + len(international),
        "codes": payload_codes,
        "world": sorted(world, key=lambda e: e["path"]),
        "international": sorted(international, key=lambda e: e["path"]),
    }
    if not args.views_only:
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        n_rep = sum(c["counts"]["representation"] for c in payload_codes.values())
        n_exp = sum(c["counts"]["explanation"] for c in payload_codes.values())
        print(f"polity-index: {len(payload_codes)} codes, {n_exp} explanations, {n_rep} representations "
              f"(+{len(world)} world, +{len(international)} international) -> {OUT.relative_to(REPO)}")
        n_node = sum(1 for c in payload_codes.values() if c["has_node"])
        print(f"polity-index: {n_node} codes backed by a polity node file")

    # Stamp per-nation pages from the canonical originals (see
    # spec/polity/README.md). Entry copies land as each dir's index.html;
    # actor copies land beside them where a same-code actor dataset exists.
    # Only <title> is baked per code (catalog discovery); bodies stay
    # identical to the originals and hydrate at runtime via shared scripts.
    try:
        entry_tpl = ENTRY_TEMPLATE.read_text(encoding="utf-8")
        actor_tpl = ACTOR_TEMPLATE.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"polity-index: WARNING: template unreadable ({exc}); copies skipped")
        return 0
    def bake(template, title):
        # Preserve tag attributes (e.g. id="docTitle", depended on by
        # shared scripts); only the text content is baked per code.
        return re.sub(r"<title( [^>]*)?>.*?</title>", lambda m: f"<title{m.group(1) or ''}>{title}</title>",
                      template, count=1, flags=re.DOTALL)

    n_entry = n_actor = 0
    for code in sorted(codes):
        m = payload_codes[code]
        entry_title = f"{m['flag']} {m['name']}"
        dest = POLITY / code / "index.html"
        body = bake(entry_tpl, entry_title)
        if not dest.is_file() or dest.read_text(encoding="utf-8") != body:
            dest.write_text(body, encoding="utf-8")
        n_entry += 1
        if (POLITY / code / "data" / "actors.json").is_file():
            actor_title = f"{m['flag']} {m['name']} Actor Space"
            adest = POLITY / code / "actor.html"
            abody = bake(actor_tpl, actor_title)
            if not adest.is_file() or adest.read_text(encoding="utf-8") != abody:
                adest.write_text(abody, encoding="utf-8")
            n_actor += 1
    print(f"polity-pages: {n_entry} entry copies + {n_actor} actor copies "
          f"(from spec/polity/)")

    # Schema check (warn-only): key order + required keys vs spec/polity/*.schema.json.
    # Skipped in --views-only mode (it validates the manifest/node files, not views).
    if args.views_only:
        return 0
    warns: list = []
    validate_schemas(warns)
    if warns:
        print(f"polity-schema: {len(warns)} warnings")
        for w in warns[:40]:
            print(f"  ! {w}")
    else:
        print("polity-schema: 0 warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
