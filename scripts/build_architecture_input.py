#!/usr/bin/env python3
"""Build a deterministic Issue Architecture input package from an approved Selection.

The package is the only material an architecture-generation runner should need
from the selection stage. It preserves Evidence boundaries and role assignments
but does not decide packages, page allocation, or editorial thesis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from scripts import candidate_selection_gate as selection_gate

ARCHITECTURE_ROLES = {
    "FEATURE_CORE",
    "SECTION_CORE",
    "PAPER_WATCH",
    "SUPPORTING_EVIDENCE",
    "LATE_BREAKING",
    "CHRONOLOGY",
    "WATCHLIST",
}
NON_ARCHITECTURE_ROLES = {"HOLD_OUT", "EXCLUDE"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(selection_path: Path, matrix_path: Path) -> dict[str, Any]:
    validation, passed = selection_gate.validate(selection_path, matrix_path, require_approved=True)
    if not passed:
        raise ValueError(f"selection is not architecture-ready: {validation['errors']}")

    selection = load_json(selection_path)
    matrix = load_json(matrix_path)
    row_by_id = {row["evidence_task_id"]: row for row in matrix["rows"]}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    excluded: list[dict[str, Any]] = []

    for assignment in selection["assignments"]:
        role = assignment["role"]
        row = row_by_id[assignment["evidence_task_id"]]
        entry = {
            "evidence_task_id": assignment["evidence_task_id"],
            "title": assignment["title"],
            "role": role,
            "selection_rationale": assignment["rationale"],
            "artifact_type": row.get("artifact_type"),
            "organization": row.get("organization"),
            "timing_relation": row.get("timing_relation"),
            "event_dates": row.get("event_dates") or [],
            "evidence_status": row.get("evidence_status"),
            "comparison_readiness": row.get("comparison_readiness"),
            "why_now_confirmed": row.get("why_now_confirmed"),
            "remaining_boundaries": row.get("remaining_boundaries") or [],
            "evidence_class_counts": row.get("evidence_class_counts") or {},
            "source_class_counts": row.get("source_class_counts") or {},
        }
        if role in ARCHITECTURE_ROLES:
            grouped[role].append(entry)
        elif role in NON_ARCHITECTURE_ROLES:
            excluded.append(entry)
        else:
            raise ValueError(f"unsupported approved selection role: {role}")

    for values in grouped.values():
        values.sort(key=lambda value: (value["title"].lower(), value["evidence_task_id"]))
    excluded.sort(key=lambda value: (value["role"], value["title"].lower()))

    return {
        "schema_version": "1.0",
        "issue_id": selection["issue_id"],
        "status": "architecture-input-ready",
        "basis": {
            "selection_path": selection_path.as_posix(),
            "selection_sha256": sha256_file(selection_path),
            "matrix_path": matrix_path.as_posix(),
            "matrix_sha256": sha256_file(matrix_path),
            "selection_version": selection["selection_version"],
            "approval": selection["approval"],
        },
        "editorial_constraints": {
            "page_target": 16,
            "page_max": 24,
            "forced_section_balance": False,
            "cover_headline_deferred_until_drafts_stable": True,
            "this_week_summary_written_last": True,
            "late_breaking_must_remain_post_cutoff": True,
            "hold_or_excluded_items_must_not_be_drafted": True,
        },
        "selected_by_role": {role: grouped.get(role, []) for role in sorted(ARCHITECTURE_ROLES)},
        "not_selected_for_architecture": excluded,
        "selected_item_count": sum(len(values) for values in grouped.values()),
        "excluded_item_count": len(excluded),
        "rules": [
            "Issue Architecture may group several selected items into one comparison package.",
            "Supporting evidence is not a duplicate story and need not receive its own article package.",
            "Do not add HOLD_OUT or EXCLUDE items without a new Selection revision bound to an updated matrix.",
            "No section quota is required; weak sections may be omitted.",
            "Article drafting begins only after the Architecture Plan validates successfully.",
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", required=True)
    parser.add_argument("--matrix", required=True)
    parser.add_argument("--output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    value = build(Path(args.selection), Path(args.matrix))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"issue_id": value["issue_id"], "selected_item_count": value["selected_item_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
