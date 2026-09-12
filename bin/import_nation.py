#!/usr/bin/env python3
"""
Bootstrap the Nation Space dataset from the Index Gentium country exports
(csiglab/research-CountryIndex).

Reads app/nation/import/<code>_country.json (17 country files, one per
nation) and writes app/nation/data/data.json — one node per country in the
Naturgnosis node model. Re-runnable: regenerates from the imports.

Mapping (country.json -> node):

    identity.name                  name
    identity.tags                  tags
    identity.nativeName            specific.nativeName
    definition.text                description
    statistics[]                   specific.{population,gdpNominal,area,capital,governmentType}
    works[]                        specific.works (title/status)
    meta.flagEmoji                 specific.flagEmoji

Usage:

    python bin/import_nation.py
"""

import json
import sys
from datetime import date
from pathlib import Path

def rewrite_work_link(link, code):
    """Point source-relative work links at this module's ported pages.

    'rep/actor.html'            -> rep/actor.html?code=<code>
    '../pending.html?back=...'  -> pending.html?back=entry.html?code=<code>
    """
    if not link:
        return link
    if link.rstrip("/").endswith("rep/actor.html"):
        return f"rep/actor.html?code={code}"
    if "pending.html" in link:
        return f"pending.html?back=entry.html%3Fcode%3D{code}"
    return link


def convert(doc, code):
    identity = doc.get("identity") or {}
    meta = doc.get("meta") or {}
    definition = doc.get("definition") or {}

    specific = {
        "nativeName": identity.get("nativeName", ""),
        "flagEmoji": meta.get("flagEmoji", ""),
        # Verbatim from the source export: the entry page renders indicator
        # bars (hasIndicator/indicatorValue) and works cards from these.
        "statistics": doc.get("statistics", []) or [],
    }

    works = []
    for w in doc.get("works", []) or []:
        if not isinstance(w, dict) or not w.get("title"):
            continue
        entry = dict(w)
        entry["link"] = rewrite_work_link(entry.get("link"), code)
        works.append(entry)
    specific["works"] = works

    footer = doc.get("footer") or {}
    if footer:
        footer = dict(footer)
        footer["links"] = [
            {"label": "About", "href": "/"},
            {"label": "Source", "href": "https://github.com/csiglab/Naturgnosis"},
            {"label": "Editor", "href": "/nation/edit.html"},
        ]
        specific["footer"] = footer

    return {
        "id": code,
        "name": identity.get("name", ""),
        "tags": identity.get("tags", []) or [],
        "layer": "Ontic",
        "category": "Nation-State",
        "description": definition.get("text", ""),
        "longDescription": "",
        "chronology": {},
        "relationships": [],
        "specific": specific,
        "metadata": {
            "source": "research-CountryIndex",
            "imported": date.today().isoformat(),
        },
        "references": [],
    }


def main(argv=None):
    here = Path(__file__).resolve().parent
    repo = here.parent
    import_dir = repo / "app" / "nation" / "import"
    out = repo / "app" / "nation" / "data" / "data.json"

    if not import_dir.is_dir():
        print(f"ERROR: import dir not found: {import_dir}", file=sys.stderr)
        return 1

    nodes = []
    for path in sorted(import_dir.glob("*_country.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            sys.stderr.write(f"[nation] cannot parse {path.name}: {exc}\n")
            continue
        code = path.name.split("_")[0]  # iso code from the file name
        node = convert(doc, code)
        if node["id"] and node["name"]:
            nodes.append(node)

    # Ship the Actor Space datasets (fetched by web/rep/actor.html?code=...).
    actors_dir = import_dir.parent / "data" / "actors"
    actors_dir.mkdir(parents=True, exist_ok=True)
    shipped = 0
    for path in sorted(import_dir.glob("*_actor.json")):
        code = path.name.split("_")[0]
        dest = actors_dir / f"{code}.json"
        dest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        shipped += 1

    nodes.sort(key=lambda n: n["name"])

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(nodes, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"[nation] imported {len(nodes)} countries, shipped {shipped} actor "
          f"datasets -> {actors_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
