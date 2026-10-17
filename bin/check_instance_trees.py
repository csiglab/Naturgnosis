#!/usr/bin/env python3
"""
Instance-tree convention checker (Naturgnosis notes).

Validates every `| Instance Tree Path |` table against its space's
decomposition grammar:

  - social tables (Philosophia Socialium et Operis) carry an explicit
    `(→ Relationship)` label on every link, drawn from the closed
    relationship vocabulary (bare arrows are not permitted);
  - epistemic tables (Philosophia Artium Epistemicarum et Operis) link
    with a bare `→` and group types with backticks;
  - in both grammars backticks stay on the permitted vocabulary only and
    every full path is unique within its file (identity rule).

A table is read as epistemic when it carries no `(→ …)` label and at least
one backticked segment from the epistemic vocabulary; otherwise the social
rules apply, so a social table that merely drops its labels is still
rejected.

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
# Epistemic-tree grammar (Philosophia Artium Epistemicarum et Operis): types
# are grouped with backticks and links carry a bare `→` with no label. The
# vocabulary is the guide's declared types plus every grouping segment
# realized in its Arithmetic worked case.
EPISTEMIC_VOCAB = {
    "Epistemic Element", "Aggregate",
    "Epistemic Orientation", "Epistemic Purpose", "Epistemic Question",
    "Epistemic Goal", "Epistemic Gap", "Epistemic Role",
    "Epistemic Agency", "Epistemic Agent", "Epistemic Act", "Epistemic Activity",
    "Epistemic Access", "Observation Interface", "Observation Record",
    "Observation Encoding",
    "Epistemic Representation", "Representational System",
    "Representation Element", "Constitutive Substrate",
    "Convention", "Formation", "Foundation", "Interpretation",
    "Epistemic Construction", "Epistemic Operation", "Action", "Organization",
    "Method", "Principle", "Inference", "Deduction", "Procedure",
    "Epistemic Evaluation", "Epistemic Standard", "Epistemic Criterion",
    "Epistemic Constraint", "Error", "Validation", "Feedback",
    "Epistemic Communication", "Epistemic Inscription", "Epistemic Publication",
    "Epistemic Infrastructure", "Epistemic Tool", "Information Repository",
    "Epistemic Institution", "Epistemic Context", "Epistemic Condition",
    "Epistemic Target", "Target Domain", "Target Segment", "Observable",
    "Epistemic Object", "Segment of Reality", "Ontic",
}
EPISTEMIC_ONLY = EPISTEMIC_VOCAB - VOCAB - {"Ontic"}
LABEL_RE = re.compile(r"\(→ ([A-Za-z]+)\)")
BACKTICK_RE = re.compile(r"`([^`]+)`")


def _tables(lines):
    """Group path cells (lineno, cell) by `| Instance Tree Path |` table."""
    tables, cur = [], None
    for i, ln in enumerate(lines, 1):
        if ln.startswith("| Instance Tree Path |"):
            cur = []
            tables.append(cur)
            continue
        if not ln.startswith("|"):
            cur = None
            continue
        if cur is None:
            continue
        cells = ln.split("|")
        if len(cells) < 4:
            continue
        if re.fullmatch(r"\s*-+\s*", cells[1]):
            continue  # separator row
        if not cells[1].strip():
            continue  # blank spacer row
        cur.append((i, cells[1]))
    return tables


def _is_epistemic(rows):
    if any("(→" in cell for _, cell in rows):
        return False
    return any(BACKTICK_RE.findall(cell) and
               set(m.strip() for m in BACKTICK_RE.findall(cell)) & EPISTEMIC_ONLY
               for _, cell in rows)


def check_file(path):
    issues = []
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeError) as e:
        return [f"{path}: unreadable ({e})"]
    seen = {}
    for rows in _tables(lines):
        epistemic = _is_epistemic(rows)
        for i, cell in rows:
            if epistemic:
                # 1. epistemic links are bare arrows, never labeled
                if LABEL_RE.search(cell):
                    issues.append(f"{path}:{i}: labeled link in epistemic path cell")
                # 2. backticks only on epistemic vocabulary segments
                for bt in BACKTICK_RE.findall(cell):
                    if bt.strip() not in EPISTEMIC_VOCAB:
                        issues.append(f"{path}:{i}: backticked non-vocabulary segment `{bt.strip()}`")
            else:
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
                    for bt in BACKTICK_RE.findall(seg):
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
