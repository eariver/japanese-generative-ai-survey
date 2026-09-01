#!/usr/bin/env python3
"""Initialize the next Weekly carry-over ledger from approved prior selection.

This is intentionally conservative: the script never overwrites an existing
ledger and refuses to initialize from a prior Candidate Selection that is not
APPROVED. Each inherited HOLD_OUT/WATCHLIST/LATE_BREAKING assignment begins in
PENDING_RECHECK and must be resolved before the current Candidate Selection gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts.validate_weekly_carryover_ledger import CARRYOVER_ROLES, previous_issue_id


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def initialize(repo_root: Path, issue_id: str, output_path: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    output_path = output_path.resolve()
    source_issue_id = previous_issue_id(issue_id)
    previous_selection = repo_root / "sources" / source_issue_id / "selection" / "candidate-selection-v0.1.json"
    if output_path.is_file():
        existing = load_json(output_path)
        if existing.get("issue_id") != issue_id or existing.get("source_issue_id") != source_issue_id:
            raise ValueError("existing carry-over ledger has the wrong issue boundary")
        return {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "source_issue_id": source_issue_id,
            "status": "EXISTING_LEDGER_PRESERVED",
            "output_path": output_path.relative_to(repo_root).as_posix(),
            "entry_count": len(existing.get("entries") or []),
        }

    if not previous_selection.is_file():
        raise ValueError(
            f"previous approved Candidate Selection is missing: "
            f"{previous_selection.relative_to(repo_root).as_posix()}"
        )
    selection = load_json(previous_selection)
    if selection.get("issue_id") != source_issue_id:
        raise ValueError("previous Candidate Selection issue mismatch")
    if selection.get("status") != "APPROVED":
        raise ValueError("previous Candidate Selection must be APPROVED before next-issue carry-over initialization")

    entries: list[dict[str, Any]] = []
    for assignment in selection.get("assignments") or []:
        role = assignment.get("role")
        if role not in CARRYOVER_ROLES:
            continue
        task_id = assignment.get("evidence_task_id")
        title = assignment.get("title")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("carry-over assignment is missing evidence_task_id")
        if not isinstance(title, str) or not title:
            raise ValueError(f"{task_id}: carry-over assignment is missing title")
        entries.append({
            "prior_evidence_task_id": task_id,
            "title": title,
            "prior_role": role,
            "status": "PENDING_RECHECK",
            "resolution_note": f"Inherited from {source_issue_id} {role}; recheck against current primary sources before Candidate Selection.",
            "current_evidence_task_ids": [],
        })

    entries.sort(key=lambda item: item["prior_evidence_task_id"])
    document = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_issue_id": source_issue_id,
        "basis": {
            "previous_selection_path": previous_selection.relative_to(repo_root).as_posix(),
            "previous_selection_sha256": sha256(previous_selection),
        },
        "entries": entries,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_issue_id": source_issue_id,
        "status": "INITIALIZED",
        "output_path": output_path.relative_to(repo_root).as_posix(),
        "entry_count": len(entries),
        "previous_selection_sha256": document["basis"]["previous_selection_sha256"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--output")
    parser.add_argument("--report")
    args = parser.parse_args()
    repo_root = Path(args.repo_root)
    output = Path(args.output) if args.output else repo_root / "sources" / args.issue_id / "carryover" / "carryover-ledger-v0.1.json"
    result = initialize(repo_root, args.issue_id, output)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        report = Path(args.report)
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
