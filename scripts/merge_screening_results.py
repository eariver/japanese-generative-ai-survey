#!/usr/bin/env python3
"""Merge validated screening batch results and build the verification queue.

Partial progress is allowed by default so screening can resume batch-by-batch.
Use --require-complete before promoting the screening stage to complete.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from scripts import validate_screening_result as validator

PROMOTED = {"KEEP", "MAYBE", "INSPECT"}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def batch_number(path: Path) -> int:
    try:
        return int(path.stem.split("-")[-1])
    except ValueError as exc:
        raise ValueError(f"unexpected batch filename: {path.name}") from exc


def merge(
    batches_dir: Path,
    results_dir: Path,
    prompt: Path,
    output_dir: Path,
    require_complete: bool,
) -> tuple[dict[str, Any], bool]:
    batch_paths = sorted(batches_dir.glob("batch-*.jsonl"), key=batch_number)
    if not batch_paths:
        raise ValueError(f"no batch-*.jsonl files found in {batches_dir}")

    input_by_id: dict[str, dict[str, Any]] = {}
    batch_by_id: dict[str, str] = {}
    for batch in batch_paths:
        for record in read_jsonl(batch):
            screening_id = record["screening_id"]
            if screening_id in input_by_id:
                raise ValueError(f"screening_id appears in more than one input batch: {screening_id}")
            input_by_id[screening_id] = record
            batch_by_id[screening_id] = batch.stem

    processed_batches: list[str] = []
    invalid_batches: list[dict[str, Any]] = []
    decision_by_id: dict[str, dict[str, Any]] = {}
    runner_by_batch: dict[str, dict[str, Any]] = {}

    for batch in batch_paths:
        result_path = results_dir / f"{batch.stem}.json"
        if not result_path.is_file():
            continue
        report, passed = validator.validate(batch, result_path, prompt)
        if not passed:
            invalid_batches.append({"batch_id": batch.stem, "errors": report["errors"]})
            continue
        result = json.loads(result_path.read_text(encoding="utf-8"))
        processed_batches.append(batch.stem)
        runner_by_batch[batch.stem] = result["runner"]
        for decision in result["decisions"]:
            screening_id = decision["screening_id"]
            if screening_id in decision_by_id:
                raise ValueError(f"duplicate decision across result batches: {screening_id}")
            decision_by_id[screening_id] = decision

    reviewed: list[dict[str, Any]] = []
    verification_queue: list[dict[str, Any]] = []
    for screening_id, decision in sorted(decision_by_id.items()):
        record = input_by_id[screening_id]
        combined = {
            "schema_version": "1.0",
            "issue_id": record["issue_id"],
            "batch_id": batch_by_id[screening_id],
            "screening_id": screening_id,
            "record": record,
            "screening": decision,
        }
        reviewed.append(combined)
        if decision["decision"] in PROMOTED:
            verification_queue.append(combined)

    expected_batches = [path.stem for path in batch_paths]
    missing_batches = sorted(set(expected_batches) - set(processed_batches))
    counts = Counter(item["screening"]["decision"] for item in reviewed)
    issue_ids = {item["record"]["issue_id"] for item in reviewed} or {
        record["issue_id"] for record in input_by_id.values()
    }
    issue_id = next(iter(issue_ids)) if len(issue_ids) == 1 else None

    complete = not missing_batches and not invalid_batches
    passed = not invalid_batches and (complete or not require_complete)
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": passed,
        "complete": complete,
        "require_complete": require_complete,
        "input_batch_count": len(batch_paths),
        "processed_batch_count": len(processed_batches),
        "processed_batches": processed_batches,
        "missing_batches": missing_batches,
        "invalid_batches": invalid_batches,
        "input_record_count": len(input_by_id),
        "reviewed_record_count": len(reviewed),
        "decision_counts": {key: counts.get(key, 0) for key in ["KEEP", "MAYBE", "DROP", "INSPECT"]},
        "verification_queue_count": len(verification_queue),
        "runner_by_batch": runner_by_batch,
        "outputs": {
            "reviewed": "screening-reviewed.jsonl",
            "verification_queue": "verification-queue.jsonl",
        },
    }

    write_jsonl(output_dir / "screening-reviewed.jsonl", reviewed)
    write_jsonl(output_dir / "verification-queue.jsonl", verification_queue)
    write_json(output_dir / "screening-progress.json", manifest)
    return manifest, passed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batches-dir", required=True)
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--prompt", default="config/prompts/screening/source-screening-v0.1.md")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--require-complete", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = merge(
        Path(args.batches_dir),
        Path(args.results_dir),
        Path(args.prompt),
        Path(args.output_dir),
        args.require_complete,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
