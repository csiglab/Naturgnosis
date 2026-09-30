#!/usr/bin/env python3
"""
Q/A log index builder (Naturgnosis qa module).

Reads app/qa/data/qa.json (source of truth, hand-normalized) and emits
app/qa/data/qa-index.json, the search corpus for the Q/A catalog (/qa/).
Stdlib only.

Entry schema: {id, question, answer, agent, run, date, source, tags, status}.
Index per entry: {id, question, agent, run, date, tags, status, excerpt,
text (lowercased question + answer), words}.

Usage: python3 bin/build_qa_index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "app" / "qa" / "data" / "qa.json"
OUT = REPO / "app" / "qa" / "data" / "qa-index.json"

ID_RE = re.compile(r"^qa-\d{5}$")
TAG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EXCERPT_LEN = 300


def excerpt(text: str) -> str:
    text = " ".join((text or "").split())
    if len(text) <= EXCERPT_LEN:
        return text
    cut = text[:EXCERPT_LEN]
    space = cut.rfind(" ")
    return (cut[:space] if space > 40 else cut).rstrip() + " …"


def main() -> int:
    if not DATA.is_file():
        print(f"ERROR: missing {DATA.relative_to(REPO)}", file=sys.stderr)
        return 1
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    rows = raw if isinstance(raw, list) else raw.get("entries", [])
    warnings: list = []
    entries: list = []
    for n, row in enumerate(rows):
        if not isinstance(row, dict):
            warnings.append(f"row {n}: not an object, skipped")
            continue
        qid = row.get("id", "")
        if not isinstance(qid, str) or not ID_RE.match(qid):
            warnings.append(f"row {n}: bad id {qid!r} (want qa-NNNNN), skipped")
            continue
        question = str(row.get("question") or "").strip()
        if not question:
            warnings.append(f"{qid}: empty question")
        answer = str(row.get("answer") or "")
        tags = [t for t in (row.get("tags") or []) if isinstance(t, str)]
        for t in tags:
            if not TAG_RE.match(t):
                warnings.append(f"{qid}: bad tag {t!r}")
        tags = [t for t in tags if TAG_RE.match(t)]
        text = f"{question}\n{answer}".strip().lower()
        entries.append(
            {
                "id": qid,
                "question": question,
                "agent": str(row.get("agent") or ""),
                "run": str(row.get("run") or ""),
                "date": str(row.get("date") or ""),
                "tags": tags,
                "status": str(row.get("status") or "open"),
                "excerpt": excerpt(answer or question),
                "text": re.sub(r"\s+", " ", text),
                "words": len(text.split()),
            }
        )

    agents: dict = {}
    runs: dict = {}
    for e in entries:
        if e["agent"]:
            agents[e["agent"]] = agents.get(e["agent"], 0) + 1
        if e["run"]:
            runs[e["run"]] = runs.get(e["run"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "generated": date.today().isoformat(),
                "count": len(entries),
                "agents": agents,
                "runs": runs,
                "entries": entries,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
    kb = OUT.stat().st_size / 1024
    print(f"qa-index: {len(entries)} entries -> app/qa/data/qa-index.json ({kb:.0f} KB)")
    for w in warnings:
        print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
