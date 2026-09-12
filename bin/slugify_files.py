#!/usr/bin/env python3
"""
Slugify file names to the Naturgnosis naming guideline.

Rule (see guideline.md): NFKD-normalize to ASCII, lowercase, every run of
non-alphanumeric characters becomes a single underscore, trim leading and
trailing underscores. Collisions get a `_2`, `_3`, … suffix.

Renames are applied in place; directories are walked recursively. Use
--dry-run to preview. Git-tracked files are renamed with `git mv` when
possible so history follows the rename.
"""

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path


def slugify(stem):
    text = unicodedata.normalize("NFKD", stem)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="slugify_files.py")
    parser.add_argument("paths", nargs="+", help="Files or directories to rename.")
    parser.add_argument(
        "--dry-run", action="store_true", help="Print planned renames only."
    )
    args = parser.parse_args(argv)

    files = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(path.rglob("*")))
        elif path.is_file():
            files.append(path)

    renames = []
    taken = set()
    for path in files:
        if not path.is_file() or path.stem == path.name:
            # no extension -> not a candidate (or dotfile like .gitkeep)
            if not path.is_file():
                continue
        slug = slugify(path.stem)
        if not slug:
            sys.stderr.write(f"[slugify] skip (empty slug): {path}\n")
            continue
        suffix = path.suffix.lower()
        target = path.with_name(slug + suffix)
        if target == path:
            taken.add(path.resolve())
            continue
        base = target.with_suffix("")
        n = 2
        while target.resolve() in taken or (
            target.exists() and target.resolve() != path.resolve()
        ):
            target = base.with_name(f"{base.name}_{n}{suffix}")
            n += 1
        taken.add(target.resolve())
        renames.append((path, target))

    for src, dst in renames:
        if args.dry_run:
            print(f"{src} -> {dst}")
            continue
        tracked = (
            subprocess.run(
                ["git", "ls-files", "--error-unmatch", str(src)],
                capture_output=True,
            ).returncode
            == 0
        )
        if tracked:
            subprocess.run(["git", "mv", "--", str(src), str(dst)], check=True)
        else:
            src.rename(dst)

    print(
        f"[slugify] {'would rename' if args.dry_run else 'renamed'} "
        f"{len(renames)} file(s)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
