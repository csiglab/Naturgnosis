#!/usr/bin/env python3
"""
Import Epistecnica documents into the Research Space as graph nodes.

Reads the Epistecnica documents corpus (markdown entries under
``src/document/app/documents/{articles,books,papers}/``), turns each into a
research node matching the existing `epistecnica-document-import` schema, and
appends it to ``app/research/data/data.json``. Every imported node carries a
``references`` entry pointing at the original document (absolute path).

Existing nodes are matched by the work itself, never by source path:

1. definitive: same ``id`` (filename stem) or ``metadata.sourceReference`` /
   ``metadata.document`` (already linked);
2. similarity: Jaccard overlap of the normalized title's word tokens against
   every existing node name (inverted index, stopwords dropped). A score above
   ``--threshold`` (0-100, default 60) means "the same work already exists" and
   the document is **linked** to that node: ``metadata.document`` is set to the
   document and a ``references`` entry pointing at the original file is added —
   no node is created. This covers a node authored in Naturgnosis first whose
   Epistecnica document appears later (its source paths never corresponded).

A document with no match becomes a new node.

This script never writes to CouchDB and never creates notes. It stages the local
mirror only; run ``bin/layout.py`` + ``make build`` afterwards, and a human runs
``make seed`` to go live.

Usage
-----
    python bin/import_epistecnica_documents.py --dry-run
    python bin/import_epistecnica_documents.py --threshold 60
    python bin/import_epistecnica_documents.py --approve ids.txt
    python bin/import_epistecnica_documents.py --source /path/to/documents

``--approve FILE`` is a whitelist of documents to force-import even when a
similar node exists (ids or ``<section>/<slug>.md``, one per line; blanks and
``#`` comments ignored).
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

MIRROR = Path(__file__).resolve().parent.parent / "app" / "research" / "data" / "data.json"
DEFAULT_SOURCE = Path(
    "/home/dbremont/Code/Epistecnica/src/document/app/documents"
)

SECTION_CATEGORY = {"articles": "Article", "books": "Book", "papers": "Document"}
KIND_BY_BIBTEX = {
    "article": "journal-article",
    "book": "monograph",
    "inbook": "book-chapter",
    "incollection": "book-chapter",
    "inproceedings": "inproceedings",
    "conference": "inproceedings",
    "proceedings": "inproceedings",
    "techreport": "tech-report",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "manual": "manual",
    "unpublished": "unpublished",
    "misc": "misc",
}

FIELD_RE = re.compile(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", re.DOTALL)
ENTRY_RE = re.compile(r"@(\w+)\s*\{")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
TAGS_RE = re.compile(r"^tags:\s*\[(.*?)\]", re.MULTILINE)
FENCE_RE = re.compile(r"```[a-zA-Z]*\s*\n(.*?)```", re.DOTALL)
YEAR_RE = re.compile(r"\((1[0-9]{3}|20[0-9]{2})\)")


def clean(value: str) -> str:
    return value.replace("{", "").replace("}", "").replace("*", "").strip().strip(",")


def parse_bibtex(text: str):
    """Return (bibtex_type, fields) from the first code fence containing '@'."""
    for block in FENCE_RE.findall(text):
        m = ENTRY_RE.search(block)
        if not m:
            continue
        fields = {}
        for key, val in FIELD_RE.findall(block):
            fields.setdefault(key.lower(), clean(val))
        return m.group(1).lower(), fields
    return "", {}


def parse_authors(raw: str):
    if not raw:
        return []
    parts = re.split(r"\s+and\s+", raw)
    out = []
    for part in parts:
        part = clean(part)
        if not part or part.lower() in ("others", "et al"):
            continue
        if "," in part:
            last, first = part.split(",", 1)
            part = f"{first.strip()} {last.strip()}".strip()
        out.append(part)
    return out


def parse_year(fields, heading):
    y = fields.get("year", "")
    m = re.search(r"\d{4}", y)
    if m:
        return int(m.group(0))
    m = YEAR_RE.search(heading or "")
    return int(m.group(1)) if m else None


def parse_identifier(fields):
    if fields.get("doi"):
        doi = fields["doi"]
        return doi if doi.startswith("http") else f"https://doi.org/{doi}"
    if fields.get("url"):
        return fields["url"]
    if fields.get("eprint") and fields.get("archiveprefix", "").lower() == "arxiv":
        return f"https://arxiv.org/abs/{fields['eprint']}"
    return ""


def first_notes_quote(text: str) -> str:
    m = re.search(r"^##\s+Notes\s*$", text, re.MULTILINE)
    if not m:
        return ""
    for line in text[m.end():].splitlines():
        line = line.strip()
        if line.startswith("## "):
            break
        if line.startswith(">"):
            quote = line.lstrip(">").strip()
            if quote and quote != "---":
                return quote
    return ""


STOPWORDS = set(
    "a an and are as at be by for from has in into is it its of on or that the "
    "their these this those to was were with".split()
)


def normalize(value: str) -> str:
    value = (value or "").lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def tokens(value: str):
    return {
        t for t in normalize(value).split() if len(t) > 1 and t not in STOPWORDS
    }


def jaccard(a, b) -> float:
    if not a or not b:
        return 0.0
    return 100.0 * len(a & b) / len(a | b)


def load_approve(path):
    ids = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        ids.add(line)
    return ids


def build_node(section, filename, text, source_root):
    slug = Path(filename).stem
    heading_m = HEADING_RE.search(text)
    heading = heading_m.group(1).strip() if heading_m else slug.replace("-", " ")
    tags_m = TAGS_RE.search(text)
    fm_tags = (
        [t.strip().strip("'\"") for t in tags_m.group(1).split(",") if t.strip()]
        if tags_m
        else []
    )

    bib_type, fields = parse_bibtex(text)
    kind = KIND_BY_BIBTEX.get(bib_type, "misc")
    creators = parse_authors(fields.get("author", ""))
    year = parse_year(fields, heading)
    venue = (
        fields.get("journal")
        or fields.get("booktitle")
        or fields.get("publisher")
        or ""
    )
    identifier = parse_identifier(fields)

    tags = list(fm_tags)
    if kind not in tags:
        tags.append(kind)

    event = f"Published by {venue}" if venue else "Published"
    origin = str((source_root / section / filename).resolve())

    return {
        "id": slug,
        "name": heading,
        "tags": tags,
        "layer": "Research",
        "category": SECTION_CATEGORY.get(section, "Document"),
        "description": first_notes_quote(text),
        "longDescription": "",
        "chronology": {
            "summary": "",
            "events": ([{"year": year, "event": event, "context": ""}] if year else []),
        },
        "relationships": [],
        "specific": {
            "kind": kind,
            "creators": creators,
            "year": year or "",
            "venue": venue,
            "identifier": identifier,
        },
        "metadata": {
            "source": "epistecnica-document-import",
            "imported": date.today().isoformat(),
            "sourceReference": f"{section}/{filename}",
            "topics": [],
        },
        "references": [
            {
                "title": heading,
                "link": origin,
                "description": "Original document in Epistecnica.",
            }
        ],
    }


def main(argv=None):
    p = argparse.ArgumentParser(prog="import_epistecnica_documents.py")
    p.add_argument("--source", default=str(DEFAULT_SOURCE), help="Epistecnica documents root.")
    p.add_argument("--data", default=str(MIRROR), help="Research data.json mirror.")
    p.add_argument("--threshold", type=float, default=60.0, help="Similarity link threshold (0-100).")
    p.add_argument("--approve", default=None, help="Force-import file: ids or <section>/<slug>.md (skip linking).")
    p.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")
    args = p.parse_args(argv)

    source_root = Path(args.source).resolve()
    data_path = Path(args.data).resolve()
    if not source_root.is_dir():
        print(f"ERROR: source not found: {source_root}", file=sys.stderr)
        return 1
    if not data_path.is_file():
        print(f"ERROR: data mirror not found: {data_path}", file=sys.stderr)
        return 1

    nodes = json.loads(data_path.read_text(encoding="utf-8"))
    ids = {n.get("id") for n in nodes if isinstance(n, dict)}
    refs = {
        (n.get("metadata") or {}).get("sourceReference")
        for n in nodes
        if isinstance(n, dict)
    }
    indexed = []
    inverted = defaultdict(list)
    for n in nodes:
        if isinstance(n, dict) and n.get("name"):
            toks = tokens(n["name"])
            idx = len(indexed)
            indexed.append((toks, n))
            for tok in toks:
                inverted[tok].append(idx)

    approve = load_approve(args.approve) if args.approve else None
    files = sorted(
        f
        for section in ("articles", "books", "papers")
        for f in (source_root / section).glob("*.md")
    )
    node_by_id = {n["id"]: n for n in nodes if isinstance(n, dict) and n.get("id")}
    documented = {
        (n.get("metadata") or {}).get("document")
        for n in nodes
        if isinstance(n, dict)
    }

    linked, imported = [], []
    for path in files:
        section = path.parent.name
        filename = path.name
        ref = f"{section}/{filename}"
        slug = path.stem
        if slug in ids or ref in refs or ref in documented:
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        heading_m = HEADING_RE.search(text)
        heading = heading_m.group(1).strip() if heading_m else slug.replace("-", " ")
        doc_toks = tokens(heading)
        candidate_ids = set()
        for tok in doc_toks:
            candidate_ids.update(inverted.get(tok, ()))
        score = 0.0
        matched = None
        for idx in candidate_ids:
            s = jaccard(doc_toks, indexed[idx][0])
            if s > score:
                score = s
                matched = indexed[idx][1]

        whitelisted = approve is not None and (slug in approve or ref in approve)
        if score > args.threshold and score > 0 and not whitelisted:
            linked.append((ref, score, matched, path))
            continue

        imported.append(build_node(section, filename, text, source_root))

    if linked:
        print(f"linked (source fixed): {len(linked)}")
        for ref, score, matched, _ in sorted(linked, key=lambda x: -x[1])[:50]:
            print(f"  {score:5.1f}  {ref}  ->  {matched.get('id')}")
        if len(linked) > 50:
            print(f"  … {len(linked) - 50} more")
    if imported:
        suffix = " (dry-run)" if args.dry_run else ""
        print(f"to import: {len(imported)}{suffix}")
        for node in imported[:50]:
            print(f"  + {node['id']}  [{node['category']}]")
        if len(imported) > 50:
            print(f"  … {len(imported) - 50} more")
    elif not linked:
        print("nothing to import")

    if args.dry_run:
        return 0

    changed = False
    for ref, score, matched, path in linked:
        node = node_by_id.get(matched.get("id"))
        if not node:
            continue
        abs_path = str(path.resolve())
        node.setdefault("metadata", {})["document"] = ref
        refs_list = node.setdefault("references", [])
        if not any(
            isinstance(r, dict) and r.get("link") == abs_path for r in refs_list
        ):
            refs_list.append(
                {
                    "title": node.get("name", ""),
                    "link": abs_path,
                    "description": "Epistecnica document.",
                }
            )
        changed = True
    if imported:
        nodes.extend(imported)
        changed = True
    if changed:
        data_path.write_text(
            json.dumps(nodes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
