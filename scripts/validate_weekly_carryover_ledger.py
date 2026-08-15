#!/usr/bin/env python3
"""Validate explicit Weekly carry-over coverage across issue boundaries.

The ledger prevents unresolved/late items from disappearing between Weekly issues.
It supports two stages:

- screening: every expected prior-issue carry-over item must be present in the
  current issue ledger, but it may still be PENDING_RECHECK;
- selection: the same coverage is required and no item may remain pending.

For modern Weekly issues, expected carry-over items are derived from the previous
issue's structured Candidate Selection assignments. For the legacy W32 issue, a
curated seed file is used because W32 predates the structured selection contract.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ISSUE_RE = re.compile(r"^(\d{4})-W(\d{2})$")
CARRYOVER_ROLES = {"HOLD_OUT", "WATCHLIST", "LATE_BREAKING"}
STATUSES = {
    "PENDING_RECHECK",
    "RECHECKED_UNRESOLVED",
    "RESOLVED_PROMOTED_CURRENT",
    "RESOLVED_SUPPORT_CURRENT",
    "BACKFILL_PREVIOUS_ISSUE",
    "NO_CURRENT_ACTION",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def previous_issue_id(issue_id: str) -> str:
    m = ISSUE_RE.fullmatch(issue_id)
    if not m:
        raise ValueError("issue_id must use YYYY-Www form")
    year, week = int(m.group(1)), int(m.group(2))
    monday = dt.date.fromisocalendar(year, week, 1) - dt.timedelta(days=7)
    py, pw, _ = monday.isocalendar()
    return f"{py:04d}-W{pw:02d}"


def normalize_expected(entry: dict[str, Any]) -> tuple[str, str, str]:
    key = entry.get("prior_evidence_task_id") or entry.get("prior_item_id")
    title = entry.get("title")
    role = entry.get("prior_role")
    if not isinstance(key, str) or not key.strip():
        raise ValueError("carry-over basis entry requires prior_evidence_task_id or prior_item_id")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"{key}: title is required")
    if role not in CARRYOVER_ROLES:
        raise ValueError(f"{key}: unsupported carry-over role {role!r}")
    return key, title, role


def expected_from_structured_selection(path: Path) -> list[dict[str, Any]]:
    doc = load_json(path)
    if doc.get("status") != "APPROVED":
        raise ValueError(f"{path}: previous Candidate Selection must be APPROVED")
    result: list[dict[str, Any]] = []
    for assignment in doc.get("assignments") or []:
        if assignment.get("role") not in CARRYOVER_ROLES:
            continue
        result.append({
            "prior_evidence_task_id": assignment.get("evidence_task_id"),
            "title": assignment.get("title"),
            "prior_role": assignment.get("role"),
        })
    return result


def expected_from_seed(path: Path, source_issue_id: str, issue_id: str) -> list[dict[str, Any]]:
    doc = load_json(path)
    if doc.get("schema_version") != "1.0":
        raise ValueError(f"{path}: unsupported seed schema")
    if doc.get("source_issue_id") != source_issue_id or doc.get("target_issue_id") != issue_id:
        raise ValueError(f"{path}: seed issue boundary mismatch")
    entries = doc.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"{path}: entries must be an array")
    return entries


def validate(repo_root: Path, issue_id: str, ledger_path: Path, stage: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    ledger_path = ledger_path.resolve()
    source_issue_id = previous_issue_id(issue_id)
    ledger = load_json(ledger_path)
    errors: list[str] = []

    if ledger.get("schema_version") != "1.0":
        errors.append("unsupported ledger schema_version")
    if ledger.get("issue_id") != issue_id:
        errors.append("ledger issue_id mismatch")
    if ledger.get("source_issue_id") != source_issue_id:
        errors.append("ledger source_issue_id mismatch")

    previous_selection = repo_root / "sources" / source_issue_id / "selection" / "candidate-selection-v0.1.json"
    basis_mode: str
    basis_path: Path
    if previous_selection.is_file():
        basis_mode = "structured-selection"
        basis_path = previous_selection
        try:
            expected = expected_from_structured_selection(previous_selection)
        except ValueError as exc:
            errors.append(str(exc))
            expected = []
    else:
        basis = ledger.get("basis") or {}
        seed_rel = basis.get("legacy_seed_path")
        if not isinstance(seed_rel, str) or not seed_rel:
            errors.append("legacy previous issue requires basis.legacy_seed_path")
            expected = []
            basis_mode = "legacy-seed"
            basis_path = Path("missing")
        else:
            basis_mode = "legacy-seed"
            basis_path = repo_root / seed_rel
            if not basis_path.is_file():
                errors.append(f"legacy seed missing: {seed_rel}")
                expected = []
            else:
                expected_sha = basis.get("legacy_seed_sha256")
                actual_sha = sha256(basis_path)
                if expected_sha != actual_sha:
                    errors.append("legacy seed SHA-256 mismatch")
                try:
                    expected = expected_from_seed(basis_path, source_issue_id, issue_id)
                except ValueError as exc:
                    errors.append(str(exc))
                    expected = []

    expected_map: dict[str, tuple[str, str]] = {}
    for raw in expected:
        try:
            key, title, role = normalize_expected(raw)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if key in expected_map:
            errors.append(f"duplicate expected carry-over key: {key}")
        expected_map[key] = (title, role)

    entries = ledger.get("entries")
    if not isinstance(entries, list):
        errors.append("ledger entries must be an array")
        entries = []
    actual_map: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("ledger entry must be an object")
            continue
        key = entry.get("prior_evidence_task_id") or entry.get("prior_item_id")
        if not isinstance(key, str) or not key.strip():
            errors.append("ledger entry missing prior key")
            continue
        if key in actual_map:
            errors.append(f"duplicate ledger carry-over key: {key}")
            continue
        if entry.get("prior_role") not in CARRYOVER_ROLES:
            errors.append(f"{key}: invalid prior_role")
        if entry.get("status") not in STATUSES:
            errors.append(f"{key}: invalid status")
        if not isinstance(entry.get("resolution_note"), str) or not entry["resolution_note"].strip():
            errors.append(f"{key}: resolution_note is required")
        current_ids = entry.get("current_evidence_task_ids", [])
        if not isinstance(current_ids, list) or any(not isinstance(x, str) or not x for x in current_ids):
            errors.append(f"{key}: current_evidence_task_ids must be an array of strings")
        actual_map[key] = entry

    missing = sorted(set(expected_map) - set(actual_map))
    extra = sorted(set(actual_map) - set(expected_map))
    if missing:
        errors.append(f"missing carry-over entries: {missing}")
    if extra:
        errors.append(f"unexpected carry-over entries: {extra}")
    for key in sorted(set(expected_map) & set(actual_map)):
        expected_title, expected_role = expected_map[key]
        entry = actual_map[key]
        if entry.get("title") != expected_title:
            errors.append(f"{key}: title mismatch against carry-over basis")
        if entry.get("prior_role") != expected_role:
            errors.append(f"{key}: prior_role mismatch against carry-over basis")

    pending = sorted(key for key, entry in actual_map.items() if entry.get("status") == "PENDING_RECHECK")
    if stage == "selection" and pending:
        errors.append(f"carry-over rechecks still pending at Candidate Selection: {pending}")

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_issue_id": source_issue_id,
        "stage": stage,
        "basis_mode": basis_mode,
        "basis_path": basis_path.relative_to(repo_root).as_posix() if basis_path.is_absolute() and repo_root in basis_path.parents else str(basis_path),
        "expected_count": len(expected_map),
        "ledger_count": len(actual_map),
        "pending_count": len(pending),
        "pending_keys": pending,
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--stage", choices=("screening", "selection"), required=True)
    parser.add_argument("--report")
    args = parser.parse_args()
    report = validate(Path(args.repo_root), args.issue_id, Path(args.ledger), args.stage)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
