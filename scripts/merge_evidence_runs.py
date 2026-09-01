#!/usr/bin/env python3
"""Merge validated Evidence Runs into pre-selection editorial queues.

This is not Candidate Selection. It validates each completed Evidence Run against
its exact task and prompt, supports resumable partial progress, and routes cards
by the Evidence Runner's recommendation for later human/LLM comparison.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from scripts import validate_evidence_run as evidence_validator


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for value in values:
            fh.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def task_paths(tasks_dir: Path) -> list[Path]:
    paths = sorted(path for path in tasks_dir.glob("*.json") if path.is_file())
    if not paths:
        raise ValueError(f"no Evidence Task JSON files found in {tasks_dir}")
    return paths


def merge(
    tasks_dir: Path,
    runs_dir: Path,
    prompt: Path,
    output_dir: Path,
    require_complete: bool,
) -> tuple[dict[str, Any], bool]:
    tasks = task_paths(tasks_dir)
    completed: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    missing: list[str] = []
    issue_ids: set[str] = set()

    for task_path in tasks:
        task = read_json(task_path)
        task_id = task.get("evidence_task_id")
        issue_id = task.get("issue_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError(f"{task_path}: evidence_task_id is missing")
        if not isinstance(issue_id, str) or not issue_id:
            raise ValueError(f"{task_path}: issue_id is missing")
        issue_ids.add(issue_id)

        run_path = runs_dir / task_path.name
        if not run_path.is_file():
            missing.append(task_path.name)
            continue

        report, passed = evidence_validator.validate(task_path, run_path, prompt)
        if not passed:
            invalid.append(
                {
                    "evidence_task_id": task_id,
                    "task_file": task_path.name,
                    "run_file": run_path.name,
                    "errors": report.get("errors", []),
                }
            )
            continue

        run = read_json(run_path)
        card = run["card"]
        completed.append(
            {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "evidence_task_id": task_id,
                "task_file": task_path.name,
                "run_file": run_path.name,
                "runner": run["runner"],
                "evidence_task_sha256": run["evidence_task_sha256"],
                "prompt_id": run["prompt_id"],
                "prompt_sha256": run["prompt_sha256"],
                "card": card,
            }
        )

    if len(issue_ids) != 1:
        raise ValueError(f"Evidence Tasks must belong to exactly one issue: {sorted(issue_ids)}")
    issue_id = next(iter(issue_ids))

    completed.sort(key=lambda value: value["evidence_task_id"])
    candidate_ready: list[dict[str, Any]] = []
    hold: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    recommendation_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    for value in completed:
        card = value["card"]
        recommendation = card["editorial"]["candidate_recommendation"]
        status = card["status"]
        recommendation_counts[recommendation] += 1
        status_counts[status] += 1
        if recommendation == "CANDIDATE":
            candidate_ready.append(value)
        elif recommendation in {"HOLD", "INSPECT_MORE"}:
            hold.append(value)
        elif recommendation == "REJECT":
            rejected.append(value)
        else:  # defensive; validator should already prevent this
            invalid.append(
                {
                    "evidence_task_id": value["evidence_task_id"],
                    "task_file": value["task_file"],
                    "run_file": value["run_file"],
                    "errors": [f"unsupported recommendation: {recommendation!r}"],
                }
            )

    complete = not missing and not invalid and len(completed) == len(tasks)
    passed = not invalid and (complete or not require_complete)

    write_jsonl(output_dir / "evidence-reviewed.jsonl", completed)
    write_jsonl(output_dir / "candidate-ready.jsonl", candidate_ready)
    write_jsonl(output_dir / "evidence-hold.jsonl", hold)
    write_jsonl(output_dir / "evidence-rejected.jsonl", rejected)

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": passed,
        "complete": complete,
        "require_complete": require_complete,
        "evidence_task_count": len(tasks),
        "validated_run_count": len(completed),
        "missing_run_files": missing,
        "invalid_runs": invalid,
        "recommendation_counts": {
            key: recommendation_counts.get(key, 0)
            for key in ["CANDIDATE", "HOLD", "INSPECT_MORE", "REJECT"]
        },
        "card_status_counts": {
            key: status_counts.get(key, 0)
            for key in ["VERIFIED", "PARTIAL", "NEEDS_MORE", "REJECTED"]
        },
        "candidate_ready_count": len(candidate_ready),
        "hold_count": len(hold),
        "rejected_count": len(rejected),
        "outputs": {
            "reviewed": "evidence-reviewed.jsonl",
            "candidate_ready": "candidate-ready.jsonl",
            "hold": "evidence-hold.jsonl",
            "rejected": "evidence-rejected.jsonl",
        },
        "note": "candidate-ready means eligible for the later Candidate Selection comparison. It is not automatic editorial selection.",
    }
    write_json(output_dir / "evidence-progress.json", manifest)
    return manifest, passed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks-dir", required=True)
    parser.add_argument("--runs-dir", required=True)
    parser.add_argument("--prompt", default="config/prompts/evidence/primary-source-verification-v0.1.md")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--require-complete", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = merge(
        Path(args.tasks_dir),
        Path(args.runs_dir),
        Path(args.prompt),
        Path(args.output_dir),
        args.require_complete,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
