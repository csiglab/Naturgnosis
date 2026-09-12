#!/usr/bin/env python3
"""
Build the Glossary search index from the markdown entries.

Scans app/glossary/entries/*.md (recursive) and generates
app/glossary/data/index.json — used by the glossary viewer
(app/glossary/web/index.html) for its entry index, client-side search, and
reader. Each record carries the entry's full markdown as `content`, so the
deployed viewer works from the JSON alone (the entries/ directory is a
development-only source and is not shipped in the Docker image).

For each entry it extracts:

    term     — the first '# ' heading, or the file name if absent
    file     — entry path relative to app/glossary/entries/
    excerpt  — the first meaningful paragraph (blockquote or plain text)
    content  — the raw markdown of the entry

Usage:

    python bin/build_glossary_index.py
    python bin/build_glossary_index.py --entries app/glossary/entries
"""

import argparse
import json
import re
import sys
from pathlib import Path

SKIP_TERMS = {"frase"}  # Notion placeholder pages


def extract_term(text, fallback):
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def extract_excerpt(text):
    """First meaningful paragraph: skip the H1 and Notion property noise
    (lines like ': 10'), then take the first blockquote or paragraph."""
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("# "):
            continue
        if re.fullmatch(r":\s*\S{0,30}", line):
            continue
        lines.append(line.lstrip("> ").strip())
        joined = " ".join(lines)
        if len(joined) >= 60:
            break
    excerpt = " ".join(lines).strip()
    if len(excerpt) > 240:
        excerpt = excerpt[:237].rstrip() + "…"
    return excerpt


def build_index(entries_dir):
    entries_dir = Path(entries_dir)
    index = []
    for path in sorted(entries_dir.rglob("*.md")):
        rel = path.relative_to(entries_dir).as_posix()
        fallback = path.stem
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as exc:
            sys.stderr.write(f"[glossary] cannot read {rel}: {exc}\n")
            continue
        term = extract_term(text, fallback)
        if term.lower() in SKIP_TERMS:
            continue
        index.append(
            {
                "term": term,
                "file": rel,
                "excerpt": extract_excerpt(text),
                "content": text,
            }
        )
    return index


def main(argv=None):
    here = Path(__file__).resolve().parent
    repo = here.parent

    parser = argparse.ArgumentParser(prog="build_glossary_index.py")
    parser.add_argument(
        "--entries",
        default=str(repo / "app" / "glossary" / "entries"),
        help="Directory of markdown entries (default: app/glossary/entries).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output index.json (default: <entries>/../data/index.json).",
    )
    args = parser.parse_args(argv)

    entries_dir = Path(args.entries).resolve()
    out = (
        Path(args.out).resolve()
        if args.out
        else entries_dir.parent / "data" / "index.json"
    )

    if not entries_dir.is_dir():
        print(f"ERROR: entries dir not found: {entries_dir}", file=sys.stderr)
        return 1

    index = build_index(entries_dir)
    index.sort(key=lambda e: e["term"].lower())

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"[glossary] indexed {len(index)} entries -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
