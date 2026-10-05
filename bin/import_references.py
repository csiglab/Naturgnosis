#!/usr/bin/env python3
"""Import academic references (papers, books, chapters) into the Research Space.

Reads a references export (list of records with title/authors/year/type/
container/publisher/volume/issue/pages/doi/url/source_file) and appends one
node per record to ``app/research/data/data.json`` in the Naturgnosis node
model, with ``name`` regenerated as a single-line APA 7th-edition reference
(see "Title format (APA)" in ``spec/research/README.md``) and
``metadata.topics`` inferred by ``bin/topics.py``.

Scope: types article/chapter/book that carry a parseable author and year
(the spec skips records without them). Records lacking a venue still
import with the venue omitted -- never faked. Titles that are not plain
ASCII, or that do not start with an ASCII letter, keep their original
casing: sentence case is an English convention and lowercases Spanish,
French and German capitalisation incorrectly.

Idempotent: re-running skips records already present (by id or by
normalized title).

Usage::

    python bin/import_references.py --input /tmp/references.json
    python bin/import_references.py --input /tmp/references.json --dry-run
"""

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topics import classify  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DEFAULT_DATA = REPO / "app" / "research" / "data" / "data.json"

# In-scope record types -> (category, kind). The default scope is the
# papers/books/chapters set; --types widens it (e.g. to "report" for
# government papers, which are institutional rather than authored works).
TYPE_MAP = {
    "article": ("Article", "journal-article"),
    "chapter": ("Article", "book-chapter"),
    "book": ("Book", "monograph"),
    "report": ("Report", "tech-report"),
}
DEFAULT_TYPES = ("article", "chapter", "book")

SOURCE = "arbitriologia-references-import"
MAX_ID = 80

# Last-token suffixes marking a no-comma author string as a corporate body
# (bibtex "Intel Corporation" style), rendered literally per APA.
CORPORATE_SUFFIX = frozenset(
    "corporation corp incorporated inc ltd limited llc gmbh organization organisation "
    "association institute institution university college school press committee commission "
    "group team laboratory laboratories labs lab consortium foundation society company agency "
    "bureau office department administration council board center centre service bank fund "
    "union authority library museum archive observatory network project program programme "
    "initiative collective cooperative federation alliance coalition movement court tribunal".split()
)

# Institutional bodies whose name reads as a corporate author even when its
# last token is a common noun ("Ministry of Health and Agriculture and
# Fisheries" ends in "Fisheries"). Without this the suffix heuristic would
# render such bodies as "Fisheries, M. O. H. A. A. F.".
CORPORATE_BODY = re.compile(
    r"\b(ministry|department|committee|board|council|office|government|treasury|"
    r"parliament|cabinet|house|stationery|admiralty|service|commission|"
    r"administration|association|society|university|institute|laborator\w*|labs?|"
    r"corporation|inc|ltd|organization|organisation|bureau|agency|foundation|"
    r"trust|institution|society|corps|army|navy|force)\b",
    re.IGNORECASE,
)


def slugify(text):
    s = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def latex_unescape(value):
    v = (value or "").replace(r"\&", "&").replace(r"\_", "_").replace(r"\%", "%")
    v = v.replace(r"\#", "#").replace(r"\$", "$").replace(r"\{", "{").replace(r"\}", "}")
    v = v.replace("~", " ")
    return re.sub(r"\s+", " ", v).strip()


def normalize(value):
    """Fold to a comparison key: accents dropped, punctuation -> space."""
    s = unicodedata.normalize("NFKD", str(value or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\W+", " ", s.lower()).strip()


def initials(given):
    out = []
    for part in re.split(r"[\s.\-]+", given):
        part = part.strip()
        if part:
            out.append(part[0].upper() + ".")
    return " ".join(out)


HONORIFICS = frozenset("mr mrs miss ms dr prof professor sir dame lord lady rev "
                      "st sjr jr capt col gen".split())


def strip_honorific(given):
    parts = given.split()
    while parts and parts[0].lower().strip(".") in HONORIFICS:
        parts.pop(0)
    return " ".join(parts)


def apa_author(raw):
    a = (raw or "").strip().strip("{}")
    if not a:
        return ""
    # Corporate bodies render literally per APA. Tested before the comma
    # split, which would otherwise mangle "Nuffield College, University of
    # Oxford" into "Nuffield College, U. O. O.".
    parts = a.split()
    if len(parts) == 1 or CORPORATE_BODY.search(a) or \
            parts[-1].lower().strip(".") in CORPORATE_SUFFIX:
        return a
    if "," in a:
        surname, given = [s.strip() for s in a.split(",", 1)]
        if not given:
            return surname
        given = strip_honorific(given)
        if not given:
            return surname
        return "%s, %s" % (surname, initials(given))
    return "%s, %s" % (parts[-1], initials(" ".join(parts[:-1])))


def apa_authors(authors):
    parts = [a.strip(" {}") for a in authors if (a or "").strip(" {}")]
    if not parts:
        return ""
    rendered = [apa_author(a) for a in parts]
    rendered = [a for a in rendered if a]
    if len(rendered) > 20:
        return ", ".join(rendered[:19]) + ", … " + rendered[-1]
    if len(rendered) > 1:
        return ", ".join(rendered[:-1]) + ", & " + rendered[-1]
    return rendered[0]


def full_name(raw):
    a = (raw or "").strip().strip("{}")
    if "," in a:
        surname, given = [s.strip() for s in a.split(",", 1)]
        return ("%s %s" % (strip_honorific(given), surname)).strip() or surname
    return a


def sentence_case(title):
    """English sentence case, preserving acronyms and internal capitals."""
    t = re.sub(r"\s+", " ", title.strip().strip("*").strip())
    if t.endswith("."):
        t = t[:-1]
    words = re.split(r"(\s+|[:—–-])", t)
    out, first, after_colon = [], True, False
    for w in words:
        if not w.strip() or re.fullmatch(r"\s+|[:—–-]", w):
            if ":" in w or "—" in w:
                after_colon = True
            out.append(w)
            continue
        if first or after_colon:
            if re.fullmatch(r"[A-Z][A-Z]+", w) or re.search(r"[a-z][A-Z]|[A-Z][a-z]*[A-Z]", w):
                tail = w
            elif w[0].isalpha():
                tail = w[0].upper() + w[1:].lower()
            else:
                tail = w
            out.append(tail)
            first, after_colon = False, False
        elif re.fullmatch(r"[A-Z][a-z]+", w):
            out.append(w.lower())
        else:
            out.append(w)
    text = "".join(out)
    return text[0].upper() + text[1:] if text else text


def work_title(raw):
    """APA work title: sentence case for plain-ASCII titles, original
    casing for anything else (non-ASCII, or punctuation-initial such as
    Spanish inverted marks), since case conventions are language-specific."""
    t = re.sub(r"\s+", " ", latex_unescape(raw)).strip().strip("*").strip()
    t = t.strip('"“”')
    if not t:
        return ""
    if t.endswith("."):
        t = t[:-1]
    if not t[:1].isascii() or not t[:1].isalpha() or re.search(r"[^\x00-\x7F]", t):
        return t
    return sentence_case(t)


def pages_dash(pages):
    p = str(pages or "").replace("--", "–").replace("—", "–")
    return re.sub(r"(\d)\s*-\s*(\d)", r"\1–\2", p)


def venue_case(venue):
    v = re.sub(r"\s+", " ", latex_unescape(venue))
    return v[0].upper() + v[1:] if v else v


def build_name(kind, rec, title, no_author=False):
    authors = apa_authors(rec.get("authors"))
    year = str(rec.get("year") or "")
    if not (year and title) or (not authors and not no_author):
        return ""
    # APA 7th: a work with no personal author takes the title in the author
    # position ("Title. (Year). Source.").
    head = ("%s (%s). %s." % (authors, year, title) if authors
            else "%s. (%s)." % (title, year))
    container = venue_case(rec.get("container"))
    publisher = venue_case(rec.get("publisher"))
    volume = str(rec.get("volume") or "").strip()
    issue = str(rec.get("issue") or "").strip()
    pages = pages_dash(rec.get("pages")).strip()

    if kind == "journal-article":
        if not container:
            return head
        tail = container
        if volume and issue:
            tail += ", %s(%s)" % (volume, issue)
        elif volume:
            tail += ", %s" % volume
        if pages:
            tail += ", %s" % pages
        return "%s %s." % (head, tail)

    if kind == "monograph":
        return "%s %s." % (head, publisher) if publisher else head

    if kind == "book-chapter":
        if not container:
            return head
        tail = "In %s" % container
        if pages:
            tail += " (pp. %s)" % pages
        if publisher:
            tail += ". %s" % publisher
        return "%s %s." % (head, tail)

    if kind == "tech-report":
        issuer = publisher or container
        return "%s %s." % (head, issuer) if issuer else head

    return head


def build_identifier(rec):
    doi = latex_unescape(rec.get("doi"))
    if doi:
        if doi.lower().startswith("http"):
            return doi
        return "https://doi.org/%s" % re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    url = latex_unescape(rec.get("url"))
    return url if url.startswith("http") else ""


def existing_keys(nodes):
    """Id set + normalized title set of nodes already present, so re-runs
    are idempotent and genuine duplicates are not duplicated."""
    ids = {n["id"] for n in nodes if isinstance(n, dict) and n.get("id")}
    titles = set()
    for n in nodes:
        name = n.get("name") or ""
        titles.add(normalize(name))
        # explicit dedupe key, set by this importer (title-span recovery from
        # a rendered APA name is ambiguous when the venue is omitted)
        key = (n.get("metadata") or {}).get("titleKey")
        if key:
            titles.add(normalize(key))
        m = re.search(r"\(\d{4}[a-z]?\)\.\s+(.*)\.\s+[^.]+\.?$", name)
        if m:
            titles.add(normalize(m.group(1)))
        if n.get("specific", {}).get("identifier"):
            titles.add(normalize(n["specific"]["identifier"]))
    return ids, titles


def convert(rec, taken_ids, taken_titles, seen_keys, scope, source, allow_no_author=False):
    """Return (node, skip_reason)."""
    rtype = rec.get("type")
    if rtype not in scope:
        return None, "type %r out of scope" % rtype
    title = work_title(rec.get("title"))
    if not title:
        return None, "no title"
    authors = [a for a in (rec.get("authors") or []) if (a or "").strip()]
    year = rec.get("year")
    if not year:
        return None, "lacks a year"
    if not authors and not allow_no_author:
        return None, "lacks an author (use --allow-no-author for unsigned works)"

    category, kind = TYPE_MAP[rtype]
    name = build_name(kind, rec, title, no_author=not authors)
    if not name:
        return None, "could not build APA name"

    ident = build_identifier(rec)
    first_author = (authors[0] or "").split(",")[0] if authors else ""
    key = (normalize(title), normalize(first_author), str(year))
    if key in seen_keys:
        return None, "duplicate of an earlier record"
    title_key = normalize(title)
    if title_key in taken_titles:
        return None, "already present in the dataset"
    if ident and normalize(ident) in taken_titles:
        return None, "identifier already present in the dataset"
    seen_keys.add(key)

    surname = slugify(first_author) or "anon"
    nid = slugify("%s-%s-%s" % (surname, year, title))[:MAX_ID].strip("-")
    if not nid:
        nid = slugify(title)[:MAX_ID].strip("-") or "reference"
    base, n = nid, 2
    while nid in taken_ids:
        suffix = "-%d" % n
        nid = base[: MAX_ID - len(suffix)] + suffix
        n += 1
    taken_ids.add(nid)

    venue = venue_case(rec.get("container") or rec.get("publisher"))
    node = {
        "id": nid,
        "name": name,
        "tags": [kind],
        "layer": "Research",
        "category": category,
        "description": latex_unescape(rec.get("note") or ""),
        "longDescription": "",
        "chronology": {
            "summary": "",
            "events": [
                {"year": int(year) if str(year).isdigit() else year,
                 "event": "Published by %s" % venue if venue else "Published",
                 "context": ""}
            ],
        },
        "relationships": [],
        "specific": {
            "kind": kind,
            "creators": [full_name(a) for a in authors if full_name(a)],
            "year": int(year) if str(year).isdigit() else year,
            "venue": venue,
            "identifier": ident,
        },
        "metadata": {
            "source": source,
            "imported": date.today().isoformat(),
            "sourceReference": rec.get("source_file") or "",
            "titleKey": normalize(title),
            "topics": classify(title, venue),
        },
        "references": (
            [{"title": name, "link": ident, "description": "Canonical record."}]
            if ident else []
        ),
    }
    return node, ""


def main(argv=None):
    p = argparse.ArgumentParser(prog="import_references.py")
    p.add_argument("--input", default="/tmp/references.json")
    p.add_argument("--data", default=str(DEFAULT_DATA))
    p.add_argument("--skipped-out", default="/tmp/research-references-skipped.json")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--types", default=",".join(DEFAULT_TYPES),
                   help="record types to import (default: %s)" % ",".join(DEFAULT_TYPES))
    p.add_argument("--source", default=SOURCE,
                   help="value written to metadata.source")
    p.add_argument("--allow-no-author", action="store_true",
                   help="import unsigned works (title takes the APA author position)")
    args = p.parse_args(argv)

    src = Path(args.input)
    if not src.is_file():
        print("ERROR: input not found: %s" % src, file=sys.stderr)
        return 1
    out = Path(args.data)

    records = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        print("ERROR: expected a JSON list of records", file=sys.stderr)
        return 1

    scope = {t.strip() for t in args.types.split(",") if t.strip()}
    unknown = scope - set(TYPE_MAP)
    if unknown:
        print("ERROR: unknown type(s): %s" % ", ".join(sorted(unknown)), file=sys.stderr)
        return 1

    existing = json.loads(out.read_text(encoding="utf-8")) if out.is_file() else []
    taken_ids, taken_titles = existing_keys(existing)

    fresh, skipped = [], []
    seen_keys = set()
    for rec in records:
        if not isinstance(rec, dict):
            skipped.append({"title": str(rec)[:80], "reason": "not a record"})
            continue
        node, reason = convert(rec, taken_ids, taken_titles, seen_keys, scope, args.source,
                                args.allow_no_author)
        if node is None:
            skipped.append({
                "title": (rec.get("title") or "")[:120],
                "type": rec.get("type"),
                "source_file": rec.get("source_file"),
                "reason": reason,
            })
        else:
            fresh.append(node)

    from collections import Counter
    kinds = Counter(n["specific"]["kind"] for n in fresh)
    with_topic = sum(1 for n in fresh if n["metadata"]["topics"])
    print("input: %d records (%s) | types: %s | source: %s"
          % (len(records), src, args.types, args.source))
    print("new nodes: %d | already present/skipped: %d" % (len(fresh), len(skipped)))
    print("kinds: %s" % ", ".join("%s=%d" % kv for kv in kinds.most_common()))
    print("topics inferred: %d/%d (%.0f%%)" % (
        with_topic, len(fresh), 100.0 * with_topic / max(len(fresh), 1)))
    reasons = Counter(s["reason"] for s in skipped)
    print("skip reasons: %s" % ", ".join("%s=%d" % kv for kv in reasons.most_common()))

    if args.dry_run:
        for n in fresh[:5]:
            print("  + [%s] %s" % (n["specific"]["kind"], n["name"][:110]))
        return 0

    Path(args.skipped_out).write_text(
        json.dumps({"generated": date.today().isoformat(), "input": str(src),
                    "imported": len(fresh), "skipped": skipped},
                   indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    out.write_text(json.dumps(existing + fresh, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print("wrote %d nodes -> %s (skipped report -> %s)"
          % (len(existing) + len(fresh), out, args.skipped_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())