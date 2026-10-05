#!/usr/bin/env python3
"""Extract Epistecnica graph changes to migrate into Naturgnosis.

Given a starting commit in the Epistecnica repo, diffs the tecnica and
epistemica graph datasets (`data.json`, ID-indexed) between that commit
and the Epistecnica working tree, and emits one JSON bundle with the
Added + Modified nodes converted to the Naturgnosis node model plus a
note-bundle stub per node for hand-authoring
(`app/note/data/technique|epistemica/*.md`).

Read-only on Epistecnica (uses `git show <since>:<path>`; never checks
anything out). Stdlib only. Converter logic is reused from
`bin/import_technique.py` / `bin/import_epistemica.py` so the emitted
nodes match the `import/` -> `data/` mapping exactly.

Usage:

    python bin/extract_migration.py --since <commit>
    python bin/extract_migration.py --since <commit> --dataset epistemica --out /tmp/mig.json
    make epistecnica-export SINCE=<commit>

Output shape:

    {"generated": ..., "since": ..., "head": ..., "datasets": {...},
     "items": [{"dataset": "tecnica"|"epistemica", "status": "added"|"modified",
                "id": ..., "naturgnosis_node": {...},
                "note": {"suggested_path": ..., "title": ..., "tags": [...],
                         "body_skeleton": ...}}]}
"""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import import_epistemica  # noqa: E402
import import_technique  # noqa: E402

# Candidate paths, newest first. 720b94a moved subprojects under src/,
# so pre-move commits keep the same subtree without the src/ prefix.
CANDIDATES = {
    "tecnica": ["src/tecnica/app/data/data.json", "tecnica/app/data/data.json"],
    "epistemica": ["src/epistemica/app/data/data.json", "epistemica/app/data/data.json"],
}

DATASETS = ("tecnica", "epistemica")

TECH_GUIDE = "[How to decompose any technical instance?](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)"
EPI_GUIDE = "[How to decompose any epistemical instance?](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "untitled"


def clean_tag(tag):
    t = slugify(str(tag))
    return t if t and NAME_RE.match(t) else ""


def git(args, cwd):
    r = subprocess.run(
        ["git", "-C", str(cwd)] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return r


def resolve_commit(epi, since):
    r = git(["rev-parse", "--verify", "--quiet", since + "^{commit}"], epi)
    if r.returncode != 0:
        print(f"ERROR: unknown commit '{since}' in {epi}", file=sys.stderr)
        return None
    return r.stdout.strip()


def blob_at(epi, commit, candidates):
    """Return (relpath, parsed JSON) for the first candidate found at commit."""
    for rel in candidates:
        r = git(["show", f"{commit}:{rel}"], epi)
        if r.returncode == 0:
            try:
                return rel, json.loads(r.stdout)
            except json.JSONDecodeError as e:
                print(f"ERROR: cannot parse {commit}:{rel}: {e}", file=sys.stderr)
                return rel, None
    return None, []


def current(epi, candidates):
    for rel in candidates:
        p = epi / rel
        if p.is_file():
            return rel, json.loads(p.read_text(encoding="utf-8"))
    return None, []


def index(nodes):
    out = {}
    for n in nodes:
        if isinstance(n, dict) and n.get("id"):
            out[str(n["id"])] = n
    return out


def same(a, b):
    return json.dumps(a, sort_keys=True, ensure_ascii=False) == json.dumps(
        b, sort_keys=True, ensure_ascii=False
    )


def note_stub(dataset, node):
    """Suggested hand-authored note for one converted node."""
    title = node.get("name") or node.get("id")
    tags = [t for t in (clean_tag(t) for t in (node.get("tags") or [])) if t]
    section = "technique" if dataset == "tecnica" else "epistemica"
    guide = TECH_GUIDE if dataset == "tecnica" else EPI_GUIDE
    element = "technical" if dataset == "tecnica" else "epistemic"
    desc = (node.get("description") or "").strip().splitlines()
    desc = desc[0] if desc else ""
    lines = [
        "---",
        "tags: [%s]" % ", ".join(tags),
        "---",
        "",
        "# %s" % title,
        "",
    ]
    if desc:
        lines += ["> %s" % desc, ">"]
    lines += [
        "> A %s element migrated from Epistecnica (`%s`), read per %s."
        % (element, node.get("id"), guide),
        "",
        "## Formulation",
        "",
        "### What %s element type does this %s instance belong to?"
        % (element, element),
        "",
        "`%s` (`%s`), per the Tabular view."
        % (node.get("category") or "TBD", node.get("layer") or "TBD"),
        "",
        "### What is this %s instance?" % element,
        "",
        "TODO: restate the definition in one paragraph (presupposed guides are not restated).",
        "",
        "### What is the recursive instance decomposition of this %s instance?" % element,
        "",
        "TODO: work the instance tree (one type per row; multi-root forest when ambiguous).",
        "",
        "| Instance Tree Path | Description |",
        "| --- | --- |",
        "| **%s** | Imported instance; decomposition pending. |" % title,
        "",
        "## References",
        "",
        "- %s (workflow, grammar, limitation checklist)" % guide,
        "- Epistecnica provenance: `%s`" % node.get("id"),
        "",
    ]
    return {
        "suggested_path": "app/note/data/%s/%s.md" % (section, slugify(str(title))),
        "title": title,
        "tags": tags,
        "body_skeleton": "\n".join(lines),
    }


def extract(epi, since, datasets):
    commit = resolve_commit(epi, since)
    if commit is None:
        return None
    head_r = git(["rev-parse", "HEAD"], epi)
    head = head_r.stdout.strip() if head_r.returncode == 0 else ""
    items = []
    summary = {}
    for ds in datasets:
        old_rel, old_raw = blob_at(epi, commit, CANDIDATES[ds])
        if old_raw is None:
            return None
        cur_rel, cur_raw = current(epi, CANDIDATES[ds])
        if cur_rel is None:
            print(
                f"ERROR: no working-tree dataset found for '{ds}' "
                f"(tried {CANDIDATES[ds]})",
                file=sys.stderr,
            )
            return None
        old, cur = index(old_raw), index(cur_raw)
        convert = (
            import_technique.convert
            if ds == "tecnica"
            else import_epistemica.convert
        )
        skip = (
            set()
            if ds == "tecnica"
            else set(import_epistemica.MOVED_TO_NATURE)
        )
        added = modified = 0
        for nid in sorted(cur):
            if nid in skip:
                continue
            if nid not in old:
                status = "added"
                added += 1
            elif same(old[nid], cur[nid]):
                continue
            else:
                status = "modified"
                modified += 1
            node = convert(cur[nid])
            items.append(
                {
                    "dataset": ds,
                    "status": status,
                    "id": nid,
                    "naturgnosis_node": node,
                    "note": note_stub(ds, node),
                }
            )
        summary[ds] = {
            "added": added,
            "modified": modified,
            "at_commit": old_rel,
            "at_worktree": cur_rel,
        }
        print(
            f"[{ds}] {added} added, {modified} modified "
            f"(since {commit[:8]}:{old_rel} -> worktree:{cur_rel})"
        )
    return {
        "generated": date.today().isoformat(),
        "since": commit,
        "head": head,
        "datasets": summary,
        "items": items,
    }


def main(argv=None):
    p = argparse.ArgumentParser(prog="extract_migration.py")
    p.add_argument("--since", required=True, help="starting commit in the Epistecnica repo")
    p.add_argument(
        "--epistecnica",
        default=str(REPO.parent / "Epistecnica"),
        help="path to the Epistecnica checkout (default: ../Epistecnica)",
    )
    p.add_argument(
        "--dataset",
        choices=("all", "tecnica", "epistemica"),
        default="all",
    )
    p.add_argument(
        "--out",
        default="-",
        help="output JSON path ('-' for stdout, default)",
    )
    args = p.parse_args(argv)

    epi = Path(args.epistecnica)
    if not (epi / ".git").is_dir():
        print(f"ERROR: not a git repo: {epi}", file=sys.stderr)
        return 1

    datasets = DATASETS if args.dataset == "all" else (args.dataset,)
    bundle = extract(epi, args.since, datasets)
    if bundle is None:
        return 1

    text = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {len(bundle['items'])} nodes -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
