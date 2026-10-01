#!/usr/bin/env python3
"""Bulk-import nature notes from the Notion-export instance registry.

Reads the curated registry (/tmp/nature_elements.json: canonical elements
with element_type, source_files, relations evidence) and writes one note
per migratable element into app/note/data/nature/ following the natural
element note schema (see philosophia-naturalis-et-operis.md and the worked
nature/nature.md -> quarry.md precedent).

Migration policy (Phase 0 audit):
  - skip bare grouping-type placeholders (never terminal per the guide)
  - skip needs_human elements (deferred to interactive resolution)
  - skip elements already covered by existing notes (nature, earth,
    mineral, electric field -> enrich-only, never duplicate)
  - quality gate: skip lone bold-only singletons (dates, measurements,
    quoted fragments); keep title-backed, multi-file, or structurally
    evidenced (table/header/relation) elements

Usage:
  python bin/import_nature_notes.py --registry /tmp/nature_elements.json --dry-run --limit 3
  python bin/import_nature_notes.py --registry /tmp/nature_elements.json --wave Building-Block
  python bin/import_nature_notes.py --registry /tmp/nature_elements.json --all --out app/note/data/nature

After any real run: python bin/build_note_index.py && git add the wave.
Stdlib only.
"""

import argparse
import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "app" / "note" / "data" / "nature"

# Registry keys that already have hand-authored notes: enrich-only.
ALREADY_COVERED = {"nature", "earth", "mineral", "electric field"}

GUIDE_LINK = "[How to decompose any natural instance?](note.html?n=meta/philosophia-naturalis-et-operis.md)"
EPIST_LINK = "[Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)"


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "untitled"


def render_note(el):
    name = el["canonical_name"]
    et = el["element_type"]
    typ = et["natural_element_type"]
    cat = et["natural_category"]
    lvl = et.get("level", "meso")
    definition = re.sub(r"\*+", "", el.get("definition", "") or "").strip()
    related = sorted({a for a in el.get("aliases", []) if a.lower() != name.lower()})
    lines = []
    tags = ["nature", slugify(typ)]
    lines.append("---")
    lines.append("tags: [%s]" % ", ".join(tags))
    lines.append("---")
    lines.append("")
    lines.append("# %s" % name)
    lines.append("")
    if definition:
        lines.append("> %s" % definition)
        lines.append(">")
    lines.append("> A natural element read per %s." % GUIDE_LINK)
    lines.append("")
    lines.append("## Formulation")
    lines.append("")
    lines.append("### What natural element type does this natural instance belong to?")
    lines.append("")
    lines.append("`%s` at %s level of organization (%s category), per the Tabular view." % (typ, lvl, cat))
    lines.append("")
    lines.append("### What is this natural instance?")
    lines.append("")
    if definition:
        lines.append("**%s**: %s" % (name, definition))
    else:
        lines.append("**%s**: natural instance imported from the Notion export; definition not yet worked." % name)
    lines.append("")
    lines.append("### What is the recursive instance decomposition of this natural instance?")
    lines.append("")
    lines.append("Instances are styled `**bold**`; bare grouping types `` `code` ``; every leaf resolves to a")
    lines.append("natural instance. Root row below binds the placeholder; expansion not yet worked.")
    lines.append("")
    lines.append("| Instance Tree Path | Description | Natural Category | Natural Element Type Tree Path |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| **%s** | Imported instance; decomposition pending. | %s | `(root) -> %s` |" % (name, cat, typ))
    lines.append("")
    if related:
        lines.append("Imported aliases (same referent, pending merge review): %s." % ", ".join("**%s**" % a for a in related[:12]))
        lines.append("")
    lines.append("Limitation checklist (Complexity, Nonlinearity, Uncertainty, Chaos, Emergence, Scale, Data")
    lines.append("Availability, Computational Complexity, Irreducibility, Partial Observability, Non-Repeatability,")
    lines.append("Measurement Disturbance, Many-Body coupling): not yet worked for this instance.")
    lines.append("")
    lines.append("Secondary readings (kept as prose, never merged into the tree): readable as technique —")
    lines.append("methods transforming or measuring this instance decompose under the technicarum grammar;")
    lines.append("readable as social — actors and institutions drawn around it under the socialium grammar;")
    lines.append("readable as epistemic — models and warrants about it under the epistemicarum grammar.")
    lines.append("")
    lines.append("## References")
    lines.append("")
    lines.append("- %s (workflow, Tabular/Recursive views, Limitation checklist, level gate)" % GUIDE_LINK)
    lines.append("- %s (presupposed definitions; restated nowhere here)" % EPIST_LINK)
    prov = []
    for s in el.get("source_files", [])[:8]:
        md = s.get("md", "")
        base = md.split("/")[-1]
        if base not in prov:
            prov.append(base)
    if prov:
        lines.append("- Notion export provenance: %s" % "; ".join("`%s`" % p for p in prov))
    lines.append("")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(prog="import_nature_notes.py")
    p.add_argument("--registry", default="/tmp/nature_elements.json")
    p.add_argument("--out", default=str(DEFAULT_OUT))
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--wave", default="", help="filter: <Natural Element Type> substring, e.g. 'Building Block'")
    p.add_argument("--all", action="store_true", help="migrate every eligible element")
    p.add_argument("--names", default="", help="comma-separated canonical names to migrate (template review)")
    p.add_argument("--include-needs-human", action="store_true")
    p.add_argument("--no-preview", action="store_true", help="dry-run without writing preview files")
    args = p.parse_args(argv)

    reg = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    # definition backfill from the file index where available
    defs = {}
    try:
        mig = json.loads(Path("/tmp/to_migrate.json").read_text(encoding="utf-8"))
        for it in mig["items"]:
            d = (it.get("reference_files") or {}).get("definition", "")
            if d:
                defs[it["element"].lower()] = d
    except FileNotFoundError:
        pass

    els = reg["elements"]
    plan = []
    skipped = {"placeholder": 0, "needs_human": 0, "covered": 0, "exists": 0, "singleton": 0}
    wanted = {w.strip().lower() for w in args.names.split(",") if w.strip()}
    outdir = Path(args.out)
    used_slugs = set()
    if not args.dry_run and outdir.exists():
        used_slugs = {q.stem for q in outdir.glob("*.md")}
    for el in els:
        if el.get("is_type_placeholder"):
            skipped["placeholder"] += 1
            continue
        if el["element_type"].get("needs_human") and not args.include_needs_human:
            skipped["needs_human"] += 1
            continue
        if el["key"] in ALREADY_COVERED:
            skipped["covered"] += 1
            continue
        if args.wave and args.wave.lower() not in el["element_type"]["natural_element_type"].lower():
            continue
        if wanted and el["canonical_name"].lower() not in wanted:
            continue
        # Quality gate: lone bold-only singletons (dates, measurements, quoted
        # fragments) are not instances. Keep title-backed, multi-file, or
        # structurally evidenced (table/header/relation) elements.
        kinds = {s.get("kind") for s in el.get("source_files", [])}
        has_title = "title" in kinds
        structural = bool(kinds - {"bold"})
        if not (has_title or len(el.get("source_files", [])) >= 2 or structural):
            skipped["singleton"] += 1
            continue
        if not args.all and not args.wave and not args.limit and not wanted and not args.dry_run:
            continue
        plan.append(el)

    if args.limit:
        # deterministic: richest evidence first
        plan = sorted(plan, key=lambda e: (-len(e["source_files"]), e["canonical_name"].lower()))[: args.limit]

    # definition backfill by canonical/alias match
    for el in plan:
        if not el.get("definition"):
            hit = defs.get(el["canonical_name"].lower())
            if not hit:
                for a in el.get("aliases", []):
                    if a.lower() in defs:
                        hit = defs[a.lower()]
                        break
            if hit:
                el["definition"] = hit

    # slug assignment with collision suffixes
    for el in plan:
        base = slugify(el["canonical_name"])
        slug = base
        i = 2
        while slug in used_slugs:
            slug = "%s-%d" % (base, i)
            i += 1
        used_slugs.add(slug)
        el["_slug"] = slug

    if args.dry_run:
        print("dry-run: %d notes planned (skipped=%s)" % (len(plan), skipped))
        for el in plan[:10]:
            print("  %s.md <- %s [%s/%s] nfiles=%d" % (
                el["_slug"], el["canonical_name"],
                el["element_type"]["natural_category"],
                el["element_type"]["natural_element_type"],
                len(el["source_files"])))
        if len(plan) > 10:
            print("  ... (%d more)" % (len(plan) - 10))
        if not args.no_preview:
            prev = Path("/tmp/nature_notes_preview")
            prev.mkdir(exist_ok=True)
            for el in plan:
                (prev / (el["_slug"] + ".md")).write_text(render_note(el), encoding="utf-8")
            print("preview written to %s" % prev)
        return 0

    outdir.mkdir(parents=True, exist_ok=True)
    wrote = 0
    for el in plan:
        target = outdir / (el["_slug"] + ".md")
        if target.exists():
            skipped["exists"] += 1
            continue
        target.write_text(render_note(el), encoding="utf-8")
        wrote += 1
    print("wrote %d notes to %s (skipped=%s)" % (wrote, outdir, skipped))
    print("next: python bin/build_note_index.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
