#!/usr/bin/env python3
"""Validate one Evidence Record against its promoted screening queue item.

The validator is stdlib-only and focuses on provenance/evidence-boundary invariants
that JSON Schema alone cannot express.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

TOP_FIELDS = {
    "schema_version",
    "issue_id",
    "evidence_id",
    "screening_id",
    "artifact",
    "verification_status",
    "primary_sources",
    "claims",
    "metrics",
    "limitations",
    "open_questions",
    "safe_editorial_core",
    "provenance",
}
EVIDENCE_CLASSES = {
    "VERIFIED_PRIMARY",
    "VENDOR_CLAIM",
    "AUTHOR_RESULT",
    "INDEPENDENT_EVALUATION",
    "SOCIAL_OBSERVATION",
    "INFERENCE",
    "PENDING",
}
VERIFICATION_STATUSES = {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_REVIEW"}
PROMOTED_SCREENING = {"KEEP", "MAYBE", "INSPECT"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: each JSONL line must be an object")
            rows.append(value)
    return rows


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def find_queue_item(queue_path: Path, screening_id: str) -> dict[str, Any] | None:
    matches = [row for row in load_jsonl(queue_path) if row.get("screening_id") == screening_id]
    if len(matches) > 1:
        raise ValueError(f"verification queue contains duplicate screening_id: {screening_id}")
    return matches[0] if matches else None


def validate(queue_path: Path, evidence_path: Path) -> tuple[dict[str, Any], bool]:
    errors: list[str] = []
    data = load_json(evidence_path)
    if not isinstance(data, dict):
        raise ValueError("evidence record must be a JSON object")

    missing = sorted(TOP_FIELDS - data.keys())
    extra = sorted(data.keys() - TOP_FIELDS)
    if missing:
        errors.append(f"evidence record missing fields: {missing}")
    if extra:
        errors.append(f"evidence record has unexpected fields: {extra}")
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")

    screening_id = data.get("screening_id")
    if not isinstance(screening_id, str) or not screening_id:
        errors.append("screening_id must be a non-empty string")
        queue_item = None
    else:
        queue_item = find_queue_item(queue_path, screening_id)
        if queue_item is None:
            errors.append(f"screening_id is not present in verification queue: {screening_id}")

    if queue_item is not None:
        if data.get("issue_id") != queue_item.get("issue_id"):
            errors.append("issue_id does not match verification queue item")
        screening = queue_item.get("screening") or {}
        decision = screening.get("decision")
        if decision not in PROMOTED_SCREENING:
            errors.append(f"queue item is not promoted for verification: {decision!r}")
        provenance = data.get("provenance")
        if not isinstance(provenance, dict):
            errors.append("provenance must be an object")
        else:
            if provenance.get("screening_batch_id") != queue_item.get("batch_id"):
                errors.append("provenance.screening_batch_id does not match queue batch_id")
            if provenance.get("screening_decision") != decision:
                errors.append("provenance.screening_decision does not match queue screening decision")
            expected_targets = screening.get("verification_targets") or []
            actual_targets = provenance.get("verification_targets")
            if actual_targets != expected_targets:
                errors.append("provenance.verification_targets must preserve the queue targets exactly")
            if not valid_datetime(provenance.get("generated_at")):
                errors.append("provenance.generated_at must be an ISO-8601 date-time with timezone")
            runner = provenance.get("runner")
            if not isinstance(runner, dict):
                errors.append("provenance.runner must be an object")
            else:
                for field in ("provider", "model", "invocation"):
                    value = runner.get(field)
                    if not isinstance(value, str) or not value.strip():
                        errors.append(f"provenance.runner.{field} must be a non-empty string")

    status = data.get("verification_status")
    if status not in VERIFICATION_STATUSES:
        errors.append(f"verification_status must be one of {sorted(VERIFICATION_STATUSES)}")

    sources = data.get("primary_sources")
    source_ids: list[str] = []
    if not isinstance(sources, list) or not sources:
        errors.append("primary_sources must be a non-empty array")
        sources = []
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"primary_sources[{index}] must be an object")
            continue
        sid = source.get("source_id")
        if not isinstance(sid, str) or not sid:
            errors.append(f"primary_sources[{index}].source_id must be a non-empty string")
        else:
            source_ids.append(sid)
        if not valid_datetime(source.get("observed_at")):
            errors.append(f"primary_sources[{index}].observed_at must be an ISO-8601 date-time with timezone")
    if len(source_ids) != len(set(source_ids)):
        errors.append("primary_sources source_id values must be unique")
    source_id_set = set(source_ids)

    claims = data.get("claims")
    if not isinstance(claims, list):
        errors.append("claims must be an array")
        claims = []
    claim_ids: list[str] = []
    publishable_count = 0
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"claims[{index}] must be an object")
            continue
        cid = claim.get("claim_id")
        if not isinstance(cid, str) or not cid:
            errors.append(f"claims[{index}].claim_id must be a non-empty string")
        else:
            claim_ids.append(cid)
        cls = claim.get("evidence_class")
        if cls not in EVIDENCE_CLASSES:
            errors.append(f"claims[{index}].evidence_class is invalid: {cls!r}")
        refs = claim.get("source_ids")
        if not isinstance(refs, list):
            errors.append(f"claims[{index}].source_ids must be an array")
            refs = []
        unknown = sorted(set(refs) - source_id_set)
        if unknown:
            errors.append(f"claims[{index}] references unknown source_ids: {unknown}")
        publishable = claim.get("publishable")
        if not isinstance(publishable, bool):
            errors.append(f"claims[{index}].publishable must be boolean")
        elif publishable:
            publishable_count += 1
            if not refs:
                errors.append(f"claims[{index}] is publishable but has no supporting source_ids")
            if cls == "PENDING":
                errors.append(f"claims[{index}] is PENDING and must not be publishable")
        if cls == "PENDING" and refs:
            # A pending question may cite sources that fail to resolve it, but the record
            # should keep that ambiguity in caveats/open_questions rather than imply support.
            caveats = claim.get("caveats") or []
            if not caveats:
                errors.append(f"claims[{index}] is PENDING with source_ids but has no caveat explaining the unresolved boundary")
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("claim_id values must be unique")

    metrics = data.get("metrics")
    if not isinstance(metrics, list):
        errors.append("metrics must be an array")
        metrics = []
    for index, metric in enumerate(metrics):
        if not isinstance(metric, dict):
            errors.append(f"metrics[{index}] must be an object")
            continue
        refs = metric.get("source_ids")
        if not isinstance(refs, list) or not refs:
            errors.append(f"metrics[{index}].source_ids must be a non-empty array")
            refs = []
        unknown = sorted(set(refs) - source_id_set)
        if unknown:
            errors.append(f"metrics[{index}] references unknown source_ids: {unknown}")
        if metric.get("evidence_class") == "PENDING":
            errors.append(f"metrics[{index}] must not encode an unresolved numeric claim as PENDING; move it to claims/open_questions")

    safe_core = data.get("safe_editorial_core")
    if status in {"VERIFIED", "PARTIAL"}:
        if not isinstance(safe_core, str) or not safe_core.strip():
            errors.append("VERIFIED/PARTIAL evidence requires a non-empty safe_editorial_core")
        if publishable_count == 0:
            errors.append("VERIFIED/PARTIAL evidence requires at least one publishable claim")
    if status == "REJECTED" and safe_core is not None:
        if not isinstance(safe_core, str) or not safe_core.strip():
            errors.append("REJECTED safe_editorial_core must be null or a non-empty string")

    for field in ("limitations", "open_questions"):
        value = data.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be an array")
        elif any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{field} must contain only non-empty strings")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": data.get("issue_id"),
        "evidence_id": data.get("evidence_id"),
        "screening_id": screening_id,
        "verification_status": status,
        "primary_source_count": len(sources),
        "claim_count": len(claims),
        "publishable_claim_count": publishable_count,
        "metric_count": len(metrics),
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", required=True, help="verification-queue.jsonl")
    parser.add_argument("--evidence", required=True, help="one evidence record JSON")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.queue), Path(args.evidence))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
