#!/usr/bin/env python3
"""
Instance-tree convention checker (Naturgnosis social notes).

Validates every `| Instance Tree Path |` table against the labeled-link
convention of Philosophia Socialium et Operis ("How to Create a
Decomposition Tree"):

  - every parent->child link carries an explicit `(→ Relationship)` label
    (bare arrows are not permitted in path cells);
  - every label comes from the closed relationship vocabulary;
  - every full path is unique within its file (identity rule);
  - backticks stay on the permitted link-form vocabulary only;
    all other segments are plain Title-Case instances.

Usage:
  python3 bin/check_instance_trees.py [path ...]   # default: app/note/data/social + general
Exit status: 0 when clean, 1 otherwise.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "app" / "note" / "data"

LABELS = {"Kind", "Part", "Instance", "Member", "Position", "Association",
          "Participation", "Action", "Goal", "Production", "Attribute",
          "Unspecified", "Has", "Component"}
VOCAB = {"Social Compound", "Interaction Unit", "Social Action", "Activity",
         "Social Relation", "Social Event", "Social Process", "Social State",
         "Social Property", "Intention", "Action Guidance",
         "Action Organization", "Action Instrumentation",
         "Ontic", "Synontic", "Noetic", "Multi"}
LABEL_RE = re.compile(r"\(→ ([A-Za-z]+)\)")


def check_file(path):
    issues = []
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeError) as e:
        return [f"{path}: unreadable ({e})"]
    in_tree = False
    seen = {}
    for i, ln in enumerate(lines, 1):
        if ln.startswith("| Instance Tree Path |"):
            in_tree = True
            continue
        if in_tree and not ln.startswith("|"):
            in_tree = False
        if not in_tree or not ln.startswith("|"):
            continue
        cells = ln.split("|")
        if len(cells) < 4:
            continue
        if re.fullmatch(r"\s*-+\s*", cells[1]):
            continue  # separator row
        cell = cells[1]
        # 1. labels from closed vocabulary
        for lab in LABEL_RE.findall(cell):
            if lab not in LABELS:
                issues.append(f"{path}:{i}: unknown relationship label `(→ {lab})`")
        # 2. no bare arrows left
        stripped = LABEL_RE.sub("", cell).replace("->", "\u2192")
        if "\u2192" in stripped:
            issues.append(f"{path}:{i}: bare arrow in path cell")
        # 3. backticks only on vocabulary segments
        for seg in re.split(r"`?\(→ [A-Za-z]+\)`?", cell):
            for bt in re.findall(r"`([^`]+)`", seg):
                if bt.strip() not in VOCAB:
                    issues.append(f"{path}:{i}: backticked non-vocabulary segment `{bt.strip()}`")
        # 4. unique full paths
        key = re.sub(r"\s+", " ", cell).strip()
        if key in seen:
            issues.append(f"{path}:{i}: duplicate path (first at line {seen[key]})")
        else:
            seen[key] = i
    return issues


def main():
    roots = [Path(a) for a in sys.argv[1:]] or [DATA / "social", DATA / "general"]
    targets = []
    for r in roots:
        r = r if r.is_absolute() else REPO / r
        targets.extend(sorted(r.rglob("*.md")) if r.is_dir() else [r])
    all_issues = []
    files_with_trees = 0
    for p in targets:
        try:
            txt = p.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        if "| Instance Tree Path |" not in txt:
            continue
        files_with_trees += 1
        all_issues.extend(check_file(p))
    for issue in all_issues:
        print(issue)
    print(f"instance-trees: {files_with_trees} files with trees, "
          f"{len(all_issues)} violations")
    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
