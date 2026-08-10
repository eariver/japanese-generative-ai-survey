#!/usr/bin/env python3
"""Validate one Evidence Runner output against its exact task and prompt.

This stdlib validator focuses on invariants that are easy to violate silently:
provenance hashes, task/issue identity, verification-target coverage, unique
source/event IDs, and referential integrity for every claim/metric/limitation/event.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {"PRIMARY_FACT", "VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM", "SOCIAL_OBSERVATION", "INFERENCE"}
SOURCE_CLASSES = {"PRIMARY_OFFICIAL", "PRIMARY_PAPER", "PRIMARY_REPOSITORY", "SOCIAL", "SECONDARY"}
CARD_STATUS = {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_MORE"}
TARGET_STATUS = {"VERIFIED", "UNRESOLVED", "CONTRADICTED", "NOT_APPLICABLE"}
RECOMMENDATIONS = {"CANDIDATE", "HOLD", "REJECT", "INSPECT_MORE"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def source_ref_errors(items: Any, known: set[str], label: str, *, require_nonempty: bool = True) -> list[str]:
    errors: list[str] = []
    if not isinstance(items, list):
        return [f"{label} must be an array"]
    if require_nonempty and not items:
        errors.append(f"{label} must contain at least one source_id")
    unknown = sorted({str(value) for value in items if value not in known})
    if unknown:
        errors.append(f"{label} references unknown source IDs: {unknown}")
    if len(items) != len(set(items)):
        errors.append(f"{label} contains duplicate source IDs")
    return errors


def validate(task_path: Path, run_path: Path, prompt_path: Path) -> tuple[dict[str, Any], bool]:
    task = load_json(task_path)
    run = load_json(run_path)
    errors: list[str] = []

    if not isinstance(task, dict) or not isinstance(run, dict):
        raise ValueError("task and run must be JSON objects")

    if run.get("schema_version") != "1.0":
        errors.append("run.schema_version must be 1.0")
    if run.get("issue_id") != task.get("issue_id"):
        errors.append("run.issue_id does not match Evidence Task")
    if run.get("evidence_task_id") != task.get("evidence_task_id"):
        errors.append("run.evidence_task_id does not match Evidence Task")
    if run.get("evidence_task_sha256") != sha256_file(task_path):
        errors.append("run.evidence_task_sha256 does not match exact task bytes")
    if run.get("prompt_id") != "primary-source-verification-v0.1":
        errors.append("run.prompt_id must be primary-source-verification-v0.1")
    if run.get("prompt_sha256") != sha256_file(prompt_path):
        errors.append("run.prompt_sha256 does not match exact prompt bytes")

    runner = run.get("runner")
    if not isinstance(runner, dict):
        errors.append("run.runner must be an object")
    else:
        for field in ("provider", "model", "invocation"):
            if not nonempty(runner.get(field)):
                errors.append(f"run.runner.{field} must be non-empty")
        if not valid_datetime(runner.get("generated_at")):
            errors.append("run.runner.generated_at must be timezone-aware ISO-8601")

    card = run.get("card")
    if not isinstance(card, dict):
        return {
            "schema_version": "1.0",
            "passed": False,
            "issue_id": task.get("issue_id"),
            "evidence_task_id": task.get("evidence_task_id"),
            "errors": errors + ["run.card must be an object"],
        }, False

    if card.get("schema_version") != "1.0":
        errors.append("card.schema_version must be 1.0")
    if card.get("issue_id") != task.get("issue_id"):
        errors.append("card.issue_id does not match Evidence Task")
    if card.get("evidence_task_id") != task.get("evidence_task_id"):
        errors.append("card.evidence_task_id does not match Evidence Task")
    if card.get("status") not in CARD_STATUS:
        errors.append(f"card.status must be one of {sorted(CARD_STATUS)}")

    grouping = card.get("grouping_resolution")
    if not isinstance(grouping, dict):
        errors.append("card.grouping_resolution must be an object")
    else:
        if not isinstance(grouping.get("accepted"), bool) or not isinstance(grouping.get("split_recommended"), bool):
            errors.append("grouping accepted/split_recommended must be booleans")
        if grouping.get("accepted") and grouping.get("split_recommended"):
            errors.append("grouping cannot be accepted and split_recommended simultaneously")

    sources = card.get("sources")
    source_ids: list[str] = []
    if not isinstance(sources, list) or not sources:
        errors.append("card.sources must be a non-empty array")
        sources = []
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"sources[{index}] must be an object")
            continue
        source_id = source.get("source_id")
        if not nonempty(source_id):
            errors.append(f"sources[{index}].source_id must be non-empty")
        else:
            source_ids.append(source_id)
        if source.get("source_class") not in SOURCE_CLASSES:
            errors.append(f"sources[{index}].source_class is invalid")
        if not nonempty(source.get("url")) or not nonempty(source.get("title")) or not nonempty(source.get("role")):
            errors.append(f"sources[{index}] url/title/role must be non-empty")
        if not valid_datetime(source.get("accessed_at")):
            errors.append(f"sources[{index}].accessed_at must be timezone-aware ISO-8601")
    duplicate_source_ids = sorted(key for key, count in Counter(source_ids).items() if count > 1)
    if duplicate_source_ids:
        errors.append(f"duplicate source_id values: {duplicate_source_ids}")
    known_sources = set(source_ids)

    temporal = card.get("temporal")
    event_ids: list[str] = []
    if not isinstance(temporal, dict):
        errors.append("card.temporal must be an object")
    else:
        if not valid_datetime(temporal.get("observed_at")):
            errors.append("card.temporal.observed_at must be timezone-aware ISO-8601")
        events = temporal.get("events")
        if not isinstance(events, list):
            errors.append("card.temporal.events must be an array")
        else:
            for index, event in enumerate(events):
                if not isinstance(event, dict):
                    errors.append(f"events[{index}] must be an object")
                    continue
                event_id = event.get("event_id")
                if not nonempty(event_id):
                    errors.append(f"events[{index}].event_id must be non-empty")
                else:
                    event_ids.append(event_id)
                if not nonempty(event.get("event_type")):
                    errors.append(f"events[{index}].event_type must be non-empty")
                errors.extend(source_ref_errors(event.get("source_ids"), known_sources, f"events[{index}].source_ids"))
            duplicate_event_ids = sorted(key for key, count in Counter(event_ids).items() if count > 1)
            if duplicate_event_ids:
                errors.append(f"duplicate event_id values: {duplicate_event_ids}")

    for field, id_field in (("claims", "claim_id"), ("metrics", "metric_id"), ("limitations", "limitation_id")):
        items = card.get(field)
        if not isinstance(items, list):
            errors.append(f"card.{field} must be an array")
            continue
        ids: list[str] = []
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"{field}[{index}] must be an object")
                continue
            if not nonempty(item.get(id_field)):
                errors.append(f"{field}[{index}].{id_field} must be non-empty")
            else:
                ids.append(item[id_field])
            if item.get("evidence_class") not in EVIDENCE_CLASSES:
                errors.append(f"{field}[{index}].evidence_class is invalid")
            errors.extend(source_ref_errors(item.get("source_ids"), known_sources, f"{field}[{index}].source_ids"))
        duplicate_ids = sorted(key for key, count in Counter(ids).items() if count > 1)
        if duplicate_ids:
            errors.append(f"duplicate {id_field} values: {duplicate_ids}")

    verification = card.get("verification")
    task_targets = [value for value in task.get("verification_targets", []) if isinstance(value, str) and value.strip()]
    seen_targets: list[str] = []
    if not isinstance(verification, dict):
        errors.append("card.verification must be an object")
    else:
        targets = verification.get("targets")
        if not isinstance(targets, list):
            errors.append("card.verification.targets must be an array")
            targets = []
        for index, target in enumerate(targets):
            if not isinstance(target, dict):
                errors.append(f"verification.targets[{index}] must be an object")
                continue
            label = target.get("target")
            if not nonempty(label):
                errors.append(f"verification.targets[{index}].target must be non-empty")
            else:
                seen_targets.append(label)
            if target.get("status") not in TARGET_STATUS:
                errors.append(f"verification.targets[{index}].status is invalid")
            if not nonempty(target.get("finding")):
                errors.append(f"verification.targets[{index}].finding must be non-empty")
            errors.extend(
                source_ref_errors(
                    target.get("source_ids"),
                    known_sources,
                    f"verification.targets[{index}].source_ids",
                    require_nonempty=target.get("status") == "VERIFIED",
                )
            )
        duplicate_targets = sorted(key for key, count in Counter(seen_targets).items() if count > 1)
        if duplicate_targets:
            errors.append(f"verification targets repeated: {duplicate_targets}")
        missing_targets = sorted(set(task_targets) - set(seen_targets))
        if missing_targets:
            errors.append(f"Evidence Task verification targets not addressed: {missing_targets}")

    editorial = card.get("editorial")
    if not isinstance(editorial, dict):
        errors.append("card.editorial must be an object")
    else:
        if not isinstance(editorial.get("why_now_confirmed"), bool):
            errors.append("card.editorial.why_now_confirmed must be boolean")
        if editorial.get("candidate_recommendation") not in RECOMMENDATIONS:
            errors.append("card.editorial.candidate_recommendation is invalid")
        if not nonempty(editorial.get("rationale")):
            errors.append("card.editorial.rationale must be non-empty")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": task.get("issue_id"),
        "evidence_task_id": task.get("evidence_task_id"),
        "evidence_task_sha256": sha256_file(task_path),
        "prompt_sha256": sha256_file(prompt_path),
        "source_count": len(sources),
        "event_count": len(event_ids),
        "claim_count": len(card.get("claims", [])) if isinstance(card.get("claims"), list) else 0,
        "metric_count": len(card.get("metrics", [])) if isinstance(card.get("metrics"), list) else 0,
        "limitation_count": len(card.get("limitations", [])) if isinstance(card.get("limitations"), list) else 0,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--prompt", default="config/prompts/evidence/primary-source-verification-v0.1.md")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.task), Path(args.run), Path(args.prompt))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
