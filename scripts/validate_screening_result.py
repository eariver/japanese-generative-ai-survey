#!/usr/bin/env python3
"""Validate one provider-agnostic LLM screening batch result.

The validator is intentionally stdlib-only so it can run in GitHub Actions without
additional packages. It verifies provenance hashes, result field shape, and the
critical one-input/one-decision completeness invariant.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

DECISIONS = {"KEEP", "MAYBE", "DROP", "INSPECT"}
CONFIDENCE = {"low", "medium", "high"}
LANES = set("ABCDEFGHIJKL")
REQUIRED_DECISION_FIELDS = {
    "screening_id",
    "decision",
    "reason",
    "why_now",
    "topic_lanes",
    "duplicate_group",
    "verification_targets",
    "confidence",
}
REQUIRED_TOP_FIELDS = {
    "schema_version",
    "issue_id",
    "batch_id",
    "input_batch_sha256",
    "prompt_id",
    "prompt_sha256",
    "runner",
    "decisions",
}
REQUIRED_RUNNER_FIELDS = {"provider", "model", "invocation", "generated_at"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: each JSONL line must be an object")
            records.append(value)
    return records


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def validate_decision(item: Any, index: int) -> list[str]:
    errors: list[str] = []
    prefix = f"decisions[{index}]"
    if not isinstance(item, dict):
        return [f"{prefix} must be an object"]
    missing = sorted(REQUIRED_DECISION_FIELDS - item.keys())
    extra = sorted(item.keys() - REQUIRED_DECISION_FIELDS)
    if missing:
        errors.append(f"{prefix} missing fields: {missing}")
    if extra:
        errors.append(f"{prefix} has unexpected fields: {extra}")

    screening_id = item.get("screening_id")
    if not isinstance(screening_id, str) or not screening_id:
        errors.append(f"{prefix}.screening_id must be a non-empty string")
    if item.get("decision") not in DECISIONS:
        errors.append(f"{prefix}.decision must be one of {sorted(DECISIONS)}")
    reason = item.get("reason")
    if not isinstance(reason, str) or not reason.strip():
        errors.append(f"{prefix}.reason must be a non-empty string")
    why_now = item.get("why_now")
    if why_now is not None and (not isinstance(why_now, str) or not why_now.strip()):
        errors.append(f"{prefix}.why_now must be null or a non-empty string")

    lanes = item.get("topic_lanes")
    if not isinstance(lanes, list):
        errors.append(f"{prefix}.topic_lanes must be an array")
    else:
        invalid = [lane for lane in lanes if lane not in LANES]
        if invalid:
            errors.append(f"{prefix}.topic_lanes contains invalid lanes: {invalid}")
        if len(lanes) != len(set(lanes)):
            errors.append(f"{prefix}.topic_lanes must not contain duplicates")

    duplicate_group = item.get("duplicate_group")
    if duplicate_group is not None and (not isinstance(duplicate_group, str) or not duplicate_group.strip()):
        errors.append(f"{prefix}.duplicate_group must be null or a non-empty string")

    targets = item.get("verification_targets")
    if not isinstance(targets, list):
        errors.append(f"{prefix}.verification_targets must be an array")
    elif any(not isinstance(value, str) or not value.strip() for value in targets):
        errors.append(f"{prefix}.verification_targets must contain only non-empty strings")

    if item.get("confidence") not in CONFIDENCE:
        errors.append(f"{prefix}.confidence must be one of {sorted(CONFIDENCE)}")
    return errors


def validate(batch: Path, result: Path, prompt: Path) -> tuple[dict[str, Any], bool]:
    errors: list[str] = []
    input_records = load_jsonl(batch)
    data = load_json(result)
    if not isinstance(data, dict):
        raise ValueError("screening result must be a JSON object")

    missing_top = sorted(REQUIRED_TOP_FIELDS - data.keys())
    extra_top = sorted(data.keys() - REQUIRED_TOP_FIELDS)
    if missing_top:
        errors.append(f"result missing fields: {missing_top}")
    if extra_top:
        errors.append(f"result has unexpected fields: {extra_top}")

    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")

    issue_ids = {record.get("issue_id") for record in input_records}
    if len(issue_ids) != 1:
        errors.append(f"input batch must contain exactly one issue_id, found {sorted(str(v) for v in issue_ids)}")
    expected_issue = next(iter(issue_ids)) if len(issue_ids) == 1 else None
    if data.get("issue_id") != expected_issue:
        errors.append(f"result issue_id {data.get('issue_id')!r} does not match input {expected_issue!r}")

    expected_batch_id = batch.stem
    if data.get("batch_id") != expected_batch_id:
        errors.append(f"batch_id must be {expected_batch_id!r}")

    actual_batch_sha = sha256_file(batch)
    actual_prompt_sha = sha256_file(prompt)
    if data.get("input_batch_sha256") != actual_batch_sha:
        errors.append("input_batch_sha256 does not match the exact input batch bytes")
    if data.get("prompt_sha256") != actual_prompt_sha:
        errors.append("prompt_sha256 does not match the exact prompt bytes")
    if data.get("prompt_id") != "source-screening-v0.1":
        errors.append("prompt_id must be source-screening-v0.1 for this validator version")

    runner = data.get("runner")
    if not isinstance(runner, dict):
        errors.append("runner must be an object")
    else:
        missing_runner = sorted(REQUIRED_RUNNER_FIELDS - runner.keys())
        allowed_runner = REQUIRED_RUNNER_FIELDS | {"run_reference"}
        extra_runner = sorted(runner.keys() - allowed_runner)
        if missing_runner:
            errors.append(f"runner missing fields: {missing_runner}")
        if extra_runner:
            errors.append(f"runner has unexpected fields: {extra_runner}")
        for field in ("provider", "model", "invocation"):
            value = runner.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"runner.{field} must be a non-empty string")
        if not valid_datetime(runner.get("generated_at")):
            errors.append("runner.generated_at must be an ISO-8601 date-time with timezone")
        ref = runner.get("run_reference")
        if ref is not None and (not isinstance(ref, str) or not ref.strip()):
            errors.append("runner.run_reference must be null or a non-empty string")

    decisions = data.get("decisions")
    if not isinstance(decisions, list):
        errors.append("decisions must be an array")
        decisions = []
    for index, item in enumerate(decisions):
        errors.extend(validate_decision(item, index))

    input_ids = [record.get("screening_id") for record in input_records]
    if any(not isinstance(value, str) or not value for value in input_ids):
        errors.append("every input record must contain a non-empty screening_id")
    input_counts = Counter(input_ids)
    duplicate_input = sorted(key for key, count in input_counts.items() if count > 1)
    if duplicate_input:
        errors.append(f"input batch contains duplicate screening_id values: {duplicate_input}")

    output_ids = [item.get("screening_id") for item in decisions if isinstance(item, dict)]
    output_counts = Counter(output_ids)
    duplicate_output = sorted(str(key) for key, count in output_counts.items() if count > 1)
    if duplicate_output:
        errors.append(f"result contains duplicate screening_id values: {duplicate_output}")

    input_set = set(input_ids)
    output_set = set(output_ids)
    missing_ids = sorted(str(value) for value in input_set - output_set)
    unexpected_ids = sorted(str(value) for value in output_set - input_set)
    if missing_ids:
        errors.append(f"result is missing decisions for: {missing_ids}")
    if unexpected_ids:
        errors.append(f"result contains decisions for unknown inputs: {unexpected_ids}")
    if len(decisions) != len(input_records):
        errors.append(f"decision count {len(decisions)} does not equal input count {len(input_records)}")

    decision_counts = Counter(
        item.get("decision") for item in decisions if isinstance(item, dict) and item.get("decision") in DECISIONS
    )
    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": expected_issue,
        "batch_id": expected_batch_id,
        "input_record_count": len(input_records),
        "decision_count": len(decisions),
        "decision_counts": {key: decision_counts.get(key, 0) for key in sorted(DECISIONS)},
        "input_batch_sha256": actual_batch_sha,
        "prompt_sha256": actual_prompt_sha,
        "missing_screening_ids": missing_ids,
        "unexpected_screening_ids": unexpected_ids,
        "duplicate_output_screening_ids": duplicate_output,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--prompt", default="config/prompts/screening/source-screening-v0.1.md")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.batch), Path(args.result), Path(args.prompt))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
