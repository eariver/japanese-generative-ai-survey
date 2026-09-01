#!/usr/bin/env python3
"""Run a complete Special screening pass from a compact human/interactive override file.

This is the no-paid-provider path. It deterministically regenerates the exact
screening package from the Special work tree, expands explicit retained/inspect
choices plus a default DROP decision into one result per input record, validates
all batches with the existing screening contract, and persists them through the
existing append-only acceptance implementation.

The compact override is an editorial record, not a shortcut around completeness:
every omitted screening_id is materialized as an explicit DROP in the generated
batch result before validation/acceptance.
"""
from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from scripts import accept_screening_results, prepare_screening_run

SPECIAL_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")
ANY_SURVEY_ISSUE_RE = re.compile(r"^(?:[0-9]{4}-W[0-9]{2}|SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63})$")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_no}: expected JSON object")
        result.append(value)
    return result


def validate_overrides(value: dict[str, Any], issue_id: str) -> dict[str, dict[str, Any]]:
    if value.get("schema_version") != "1.0" or value.get("issue_id") != issue_id:
        raise ValueError("override schema/issue_id mismatch")
    runner = value.get("runner")
    if not isinstance(runner, dict):
        raise ValueError("runner metadata is required")
    for key in ("provider", "model", "invocation", "generated_at"):
        if not isinstance(runner.get(key), str) or not runner[key].strip():
            raise ValueError(f"runner.{key} must be non-empty")
    default = value.get("default_drop")
    if not isinstance(default, dict) or not isinstance(default.get("reason"), str) or not default["reason"].strip():
        raise ValueError("default_drop.reason must be non-empty")
    items = value.get("overrides")
    if not isinstance(items, list):
        raise ValueError("overrides must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("override entries must be objects")
        screening_id = item.get("screening_id")
        if not isinstance(screening_id, str) or not screening_id or screening_id in by_id:
            raise ValueError(f"invalid/duplicate override screening_id: {screening_id!r}")
        decision = item.get("decision")
        if decision not in {"KEEP", "MAYBE", "INSPECT"}:
            raise ValueError("explicit overrides may use KEEP/MAYBE/INSPECT only; omitted items become DROP")
        reason = item.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"override reason missing: {screening_id}")
        lanes = item.get("topic_lanes", [])
        if not isinstance(lanes, list) or any(x not in list("ABCDEFGHIJKL") for x in lanes):
            raise ValueError(f"invalid topic_lanes: {screening_id}")
        targets = item.get("verification_targets", [])
        if not isinstance(targets, list) or any(not isinstance(x, str) or not x.strip() for x in targets):
            raise ValueError(f"invalid verification_targets: {screening_id}")
        if item.get("confidence") not in {"low", "medium", "high"}:
            raise ValueError(f"invalid confidence: {screening_id}")
        by_id[screening_id] = item
    return by_id


def make_decision(record: dict[str, Any], override: dict[str, Any] | None, default_reason: str) -> dict[str, Any]:
    sid = record.get("screening_id")
    if not isinstance(sid, str) or not sid:
        raise ValueError("screening record missing screening_id")
    if override is None:
        return {
            "screening_id": sid,
            "decision": "DROP",
            "reason": default_reason,
            "why_now": None,
            "topic_lanes": [],
            "duplicate_group": None,
            "verification_targets": [],
            "confidence": "high",
        }
    return {
        "screening_id": sid,
        "decision": override["decision"],
        "reason": override["reason"],
        "why_now": override.get("why_now"),
        "topic_lanes": override.get("topic_lanes", []),
        "duplicate_group": override.get("duplicate_group"),
        "verification_targets": override.get("verification_targets", []),
        "confidence": override["confidence"],
    }


def run(*, repo_root: Path, issue_id: str, source_ref: str, source_commit: str,
        overrides_path: Path, review_reference: str, audit_output: Path | None = None) -> dict[str, Any]:
    if not SPECIAL_RE.fullmatch(issue_id):
        raise ValueError("interactive Special screening requires SP-* issue_id")
    repo_root = repo_root.resolve()
    overrides_path = overrides_path.resolve()
    override_doc = load_json(overrides_path)
    overrides = validate_overrides(override_doc, issue_id)

    # Keep Weekly's implementation unchanged on disk; widen only this process.
    prepare_screening_run.ISSUE_RE = ANY_SURVEY_ISSUE_RE
    accept_screening_results.ISSUE_RE = ANY_SURVEY_ISSUE_RE

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package_root = root / "package"
        package = prepare_screening_run.build_package(
            repo_root=repo_root,
            output_root=package_root,
            issue_id=issue_id,
            source_ref=source_ref,
            source_commit=source_commit,
        )
        prompt = package["prompt"]
        results_dir = root / "results"
        results_dir.mkdir()
        seen: set[str] = set()
        counts = {"KEEP": 0, "MAYBE": 0, "INSPECT": 0, "DROP": 0}
        runner = override_doc["runner"]
        default_reason = override_doc["default_drop"]["reason"]
        for batch in package["screening_input"]["batches"]:
            records = load_jsonl(package_root / batch["path"])
            decisions = []
            for record in records:
                sid = record["screening_id"]
                if sid in seen:
                    raise ValueError(f"duplicate screening_id in generated package: {sid}")
                seen.add(sid)
                decision = make_decision(record, overrides.get(sid), default_reason)
                counts[decision["decision"]] += 1
                decisions.append(decision)
            result = {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "batch_id": batch["batch_id"],
                "input_batch_sha256": batch["sha256"],
                "prompt_id": prompt["prompt_id"],
                "prompt_sha256": prompt["sha256"],
                "runner": runner,
                "decisions": decisions,
            }
            (results_dir / f"{batch['batch_id']}.json").write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        unknown = sorted(set(overrides) - seen)
        if unknown:
            raise ValueError(f"override screening_ids are absent from regenerated package: {unknown}")
        if len(seen) != package["screening_input"]["record_count"]:
            raise ValueError("generated screening record count mismatch")

        report, passed = accept_screening_results.accept(
            package_root=package_root,
            results_dir=results_dir,
            repo_root=repo_root,
            issue_id=issue_id,
            review_reference=review_reference,
        )
        if not passed:
            raise ValueError(f"screening acceptance failed: {report}")
        report = dict(report)
        report["decision_counts"] = counts
        report["interactive_override_path"] = overrides_path.relative_to(repo_root).as_posix()
        report["runner"] = runner
        if audit_output:
            audit_output.parent.mkdir(parents=True, exist_ok=True)
            audit_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return report


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--issue-id", required=True)
    p.add_argument("--source-ref", required=True)
    p.add_argument("--source-commit", required=True)
    p.add_argument("--overrides", required=True)
    p.add_argument("--review-reference", required=True)
    p.add_argument("--audit-output")
    a = p.parse_args()
    result = run(
        repo_root=Path(a.repo_root), issue_id=a.issue_id, source_ref=a.source_ref,
        source_commit=a.source_commit, overrides_path=Path(a.overrides),
        review_reference=a.review_reference,
        audit_output=Path(a.audit_output) if a.audit_output else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
