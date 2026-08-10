#!/usr/bin/env python3
"""Generate an explicit, initially-unassigned Candidate Selection gate file.

The generator intentionally makes no editorial role decisions. Human/LLM-assisted
selection edits the resulting JSON and the separate validator decides whether the
gate is complete and internally consistent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            rows.append(value)
    return rows


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(comparison_input: Path, output: Path, selection_version: str) -> dict[str, Any]:
    records = read_jsonl(comparison_input)
    if not records:
        raise ValueError("candidate comparison input is empty")
    issue_ids = {record.get("issue_id") for record in records}
    if len(issue_ids) != 1 or None in issue_ids:
        raise ValueError(f"comparison input must contain exactly one issue_id: {issue_ids}")
    issue_id = next(iter(issue_ids))

    seen: set[str] = set()
    assignments: list[dict[str, Any]] = []
    for record in records:
        comparison_id = record.get("comparison_id")
        if not isinstance(comparison_id, str) or not comparison_id:
            raise ValueError("every comparison record must have comparison_id")
        if comparison_id in seen:
            raise ValueError(f"duplicate comparison_id: {comparison_id}")
        seen.add(comparison_id)
        assignments.append(
            {
                "comparison_id": comparison_id,
                "candidate_id": record.get("candidate_id"),
                "role": "UNASSIGNED",
                "rationale": None,
                "temporal_override_reason": None,
            }
        )

    value = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "selection-draft",
        "selection_version": selection_version,
        "comparison_input_sha256": sha256_file(comparison_input),
        "assignments": assignments,
        "gate": {
            "approved": False,
            "approved_by": None,
            "approved_at": None,
            "approval_reference": None,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison-input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--selection-version", default="v0.1")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    value = build(Path(args.comparison_input), Path(args.output), args.selection_version)
    print(json.dumps({
        "issue_id": value["issue_id"],
        "status": value["status"],
        "assignment_count": len(value["assignments"]),
        "output": args.output,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
