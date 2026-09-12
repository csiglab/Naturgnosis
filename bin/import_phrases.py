#!/usr/bin/env python3
"""
Import the Phrases Catalog from the raw Notion exports.

Reads app/phrases/import/*.md (one phrase per file, as exported from Notion)
and generates app/phrases/data/data.json — the seed dataset for the phrases
module, shaped like Naturgnosis nodes so it syncs through the same CouchDB
pipeline (bin/sync.py, bin/seed_couchdb.py).

Each phrase node carries:

    id           — slug derived from the phrase
    name         — the phrase itself (first '# ' heading)
    category     — always 'Phrase'
    description  — the first blockquote (meaning, commentary, translation)
    tags         — free-form tags (empty by default; curate in the editor)
    specific     — {language, translation}
    metadata     — {source: 'notion-import', imported: <date>, file: <name>}
    references   — urls listed under '## References'

Usage:

    python bin/import_phrases.py
    python bin/import_phrases.py --import app/phrases/import
"""

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

SKIP_FILES = {"frase.md"}  # Notion placeholder pages


def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "phrase"


def parse_phrase(path):
    """Parse one Notion-exported phrase note into a node dict (or None)."""
    text = path.read_text(encoding="utf-8")

    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if not match:
        return None
    name = match.group(1).strip()

    description_lines = []
    references = []
    in_refs = False
    for raw in text.splitlines():
        line = raw.strip()
        if re.match(r"^#{1,6}\s+", line):
            in_refs = line.lower().startswith("## references")
            continue
        if not line or re.fullmatch(r":\s*\S{0,30}", line):
            continue
        if line.startswith("#"):
            continue
        content = line.lstrip("> ").strip()
        if not content:
            continue
        if in_refs:
            references.append(content.lstrip("- ").strip())
        elif not description_lines:
            description_lines.append(content)

    description = " ".join(description_lines)
    if not description:
        description = name

    return {
        "id": slugify(name),
        "name": name,
        "category": "Phrase",
        "description": description,
        "tags": [],
        "chronology": {},
        "relationships": [],
        "specific": {
            "language": "",
            "translation": "",
        },
        "metadata": {
            "source": "notion-import",
            "imported": date.today().isoformat(),
            "file": path.name,
        },
        "references": [r for r in references if r],
    }


def main(argv=None):
    here = Path(__file__).resolve().parent
    repo = here.parent

    parser = argparse.ArgumentParser(prog="import_phrases.py")
    parser.add_argument(
        "--import-dir",
        default=str(repo / "app" / "phrases" / "import"),
        help="Directory of Notion-exported notes (default: app/phrases/import).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output data.json (default: app/phrases/data/data.json).",
    )
    args = parser.parse_args(argv)

    import_dir = Path(args.import_dir).resolve()
    out = (
        Path(args.out).resolve()
        if args.out
        else import_dir.parent / "data" / "data.json"
    )

    if not import_dir.is_dir():
        print(f"ERROR: import dir not found: {import_dir}", file=sys.stderr)
        return 1

    nodes = {}
    for path in sorted(import_dir.glob("*.md")):
        if path.name.lower() in SKIP_FILES:
            continue
        try:
            node = parse_phrase(path)
        except Exception as exc:
            sys.stderr.write(f"[phrases] cannot parse {path.name}: {exc}\n")
            continue
        if not node:
            sys.stderr.write(f"[phrases] skipped (no heading): {path.name}\n")
            continue
        base_id, n = node["id"], 2
        while node["id"] in nodes:
            node["id"] = f"{base_id}-{n}"
            n += 1
        nodes[node["id"]] = node

    data = list(nodes.values())
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"[phrases] imported {len(data)} phrases -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
