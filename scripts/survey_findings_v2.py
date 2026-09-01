#!/usr/bin/env python3
"""Review Finding / Repair Set validation for Survey Production Core v2."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core

FINDING_SCHEMA = Path("schemas/review-finding-v2.schema.json")
REPAIR_SCHEMA = Path("schemas/repair-set-v2.schema.json")

SCOPES = {
    "EDITION_LOCAL", "WEEKLY_PROFILE", "PERIOD_PROFILE", "THEMATIC_PROFILE",
    "CORE", "PUBLICATION_PROFILE", "QUALITY_CONTRACT", "SERIES_LAYER",
    "UNCLASSIFIED",
}
DEFECT_KINDS = {
    "CORRECTNESS", "TRACEABILITY", "COVERAGE", "EDITORIAL", "PUBLICATION",
    "ORCHESTRATION", "COMPATIBILITY", "OTHER",
}
CONFIDENCE = {"low", "medium", "high"}
FINDING_STATUS = {"OPEN", "CLASSIFIED", "FIXED_LOCAL", "FIXED_GENERIC", "DEFERRED", "CLOSED"}
REPAIR_LAYERS = SCOPES - {"UNCLASSIFIED"}
REPAIR_DISPOSITIONS = {
    "LOCAL_ONLY", "PROFILE_FIX", "CORE_FIX", "PUBLICATION_FIX",
    "QUALITY_CONTRACT_FIX", "SERIES_FIX", "DEFERRED",
}
REPAIR_STATUS = {"PROPOSED", "IMPLEMENTED", "VALIDATED", "DEFERRED", "CLOSED"}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _sha40(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 40 and all(c in "0123456789abcdef" for c in value)


def _unique_strings(value: Any, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(set(value))
        and (not nonempty or bool(value))
        and all(_nonempty(item) for item in value)
    )


def validate_finding(finding: dict[str, Any], *, repair_set_id: str | None = None) -> list[str]:
    """Validate one Finding.

    CLOSED is not a standalone state. A CLOSED Finding is valid only while it is
    being validated as a member of the exact Repair Set named by
    resolved_by_repair_set_id. This keeps closure authority in the Repair Set.
    """
    errors: list[str] = []
    required = {
        "schema_version", "finding_id", "edition", "stage", "observed_problem",
        "expected_behavior", "actual_behavior", "production_workaround",
        "classification", "requires_regression", "provenance",
        "improvement_action", "regression_fixture", "resolved_by_repair_set_id",
        "status",
    }
    if set(finding) != required:
        return ["Review Finding fields must exactly match v2 contract"]
    if finding.get("schema_version") != "2.0-rc1":
        errors.append("Review Finding schema_version mismatch")
    for key in ("finding_id", "edition", "stage", "observed_problem", "expected_behavior", "actual_behavior"):
        if not _nonempty(finding.get(key)):
            errors.append(f"Review Finding {key} required")
    for key in ("production_workaround", "improvement_action", "regression_fixture", "resolved_by_repair_set_id"):
        value = finding.get(key)
        if value is not None and not _nonempty(value):
            errors.append(f"Review Finding {key} must be non-empty or null")

    classification = finding.get("classification")
    if not isinstance(classification, dict) or set(classification) != {"scope", "defect_kind", "confidence"}:
        errors.append("Review Finding classification fields invalid")
        classification = {}
    if classification.get("scope") not in SCOPES:
        errors.append("Review Finding classification.scope invalid")
    if classification.get("defect_kind") not in DEFECT_KINDS:
        errors.append("Review Finding classification.defect_kind invalid")
    if classification.get("confidence") not in CONFIDENCE:
        errors.append("Review Finding classification.confidence invalid")

    if not isinstance(finding.get("requires_regression"), bool):
        errors.append("Review Finding requires_regression must be boolean")

    provenance = finding.get("provenance")
    if not isinstance(provenance, dict) or set(provenance) != {
        "source_commit", "relevant_artifacts", "human_review_reference"
    }:
        errors.append("Review Finding provenance fields invalid")
        provenance = {}
    if not _sha40(provenance.get("source_commit")):
        errors.append("Review Finding provenance.source_commit must be lowercase 40-hex")
    if not _unique_strings(provenance.get("relevant_artifacts", [])):
        errors.append("Review Finding relevant_artifacts must be unique non-empty strings")
    if provenance.get("human_review_reference") is not None and not _nonempty(provenance.get("human_review_reference")):
        errors.append("Review Finding human_review_reference must be non-empty or null")

    status = finding.get("status")
    if status not in FINDING_STATUS:
        errors.append("Review Finding status invalid")
    if status in {"CLASSIFIED", "FIXED_LOCAL", "FIXED_GENERIC", "CLOSED"} and classification.get("scope") == "UNCLASSIFIED":
        errors.append(f"Review Finding status {status} requires classified scope")
    if status in {"FIXED_LOCAL", "FIXED_GENERIC", "CLOSED"} and not _nonempty(finding.get("improvement_action")):
        errors.append(f"Review Finding status {status} requires improvement_action")
    if finding.get("requires_regression") and status in {"FIXED_LOCAL", "FIXED_GENERIC", "CLOSED"} and not _nonempty(finding.get("regression_fixture")):
        errors.append("fixed Review Finding requiring regression must name regression_fixture")

    resolution = finding.get("resolved_by_repair_set_id")
    if status == "CLOSED":
        if repair_set_id is None:
            errors.append("CLOSED Review Finding requires Repair Set validation context")
        elif resolution != repair_set_id:
            errors.append("CLOSED Review Finding resolved_by_repair_set_id must match validating Repair Set")
    elif resolution is not None:
        errors.append("only CLOSED Review Finding may name resolved_by_repair_set_id")
    return errors


def validate_repair_set(repair: dict[str, Any], findings: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "repair_set_id", "finding_ids", "affected_components",
        "actual_layers_changed", "disposition", "implementation_commits",
        "regression_fixtures", "compatibility_impact", "validation_results",
        "verification_editions", "status",
    }
    if set(repair) != required:
        return ["Repair Set fields must exactly match v2 contract"]
    if repair.get("schema_version") != "2.0-rc1":
        errors.append("Repair Set schema_version mismatch")
    repair_id = repair.get("repair_set_id")
    if not _nonempty(repair_id):
        errors.append("Repair Set repair_set_id required")
    for key in ("finding_ids", "affected_components", "actual_layers_changed"):
        if not _unique_strings(repair.get(key), nonempty=True):
            errors.append(f"Repair Set {key} must be a non-empty unique string array")
    if any(value not in REPAIR_LAYERS for value in repair.get("actual_layers_changed", []) if isinstance(value, str)):
        errors.append("Repair Set actual_layers_changed contains invalid layer")
    if repair.get("disposition") not in REPAIR_DISPOSITIONS:
        errors.append("Repair Set disposition invalid")
    commits = repair.get("implementation_commits")
    if not isinstance(commits, list) or len(commits) != len(set(commits)) or any(not _sha40(value) for value in commits):
        errors.append("Repair Set implementation_commits must be unique lowercase 40-hex SHAs")
    if not _unique_strings(repair.get("regression_fixtures", [])):
        errors.append("Repair Set regression_fixtures must be unique non-empty strings")
    if not _nonempty(repair.get("compatibility_impact")):
        errors.append("Repair Set compatibility_impact required")
    if not _unique_strings(repair.get("verification_editions", [])):
        errors.append("Repair Set verification_editions must be unique non-empty strings")

    validation = repair.get("validation_results")
    if not isinstance(validation, list):
        errors.append("Repair Set validation_results must be an array")
        validation = []
    checks: list[str] = []
    for index, row in enumerate(validation):
        prefix = f"validation_results[{index}]"
        if not isinstance(row, dict) or set(row) != {"check", "status", "reference"}:
            errors.append(f"{prefix} fields invalid")
            continue
        if not _nonempty(row.get("check")) or row.get("status") not in {"PASS", "FAIL", "PENDING"}:
            errors.append(f"{prefix} check/status invalid")
        else:
            checks.append(row["check"])
        if row.get("reference") is not None and not _nonempty(row.get("reference")):
            errors.append(f"{prefix}.reference must be non-empty or null")
    if len(checks) != len(set(checks)):
        errors.append("Repair Set validation check names must be unique")

    status = repair.get("status")
    if status not in REPAIR_STATUS:
        errors.append("Repair Set status invalid")
    if status in {"IMPLEMENTED", "VALIDATED", "CLOSED"} and not commits:
        errors.append(f"Repair Set status {status} requires implementation_commits")
    if status in {"VALIDATED", "CLOSED"}:
        if not validation or any(row.get("status") != "PASS" for row in validation if isinstance(row, dict)):
            errors.append(f"Repair Set status {status} requires non-empty all-PASS validation_results")
        if not repair.get("verification_editions"):
            errors.append(f"Repair Set status {status} requires verification_editions")

    finding_by_id: dict[str, dict[str, Any]] = {}
    closure_context = repair_id if status == "CLOSED" and _nonempty(repair_id) else None
    for finding in findings:
        finding_errors = validate_finding(finding, repair_set_id=closure_context)
        if finding_errors:
            errors.append("Repair Set input Finding invalid: " + "; ".join(finding_errors))
            continue
        fid = finding["finding_id"]
        if fid in finding_by_id:
            errors.append(f"duplicate supplied Finding: {fid}")
        finding_by_id[fid] = finding
    wanted = repair.get("finding_ids") if isinstance(repair.get("finding_ids"), list) else []
    if set(wanted) != set(finding_by_id):
        errors.append(
            "Repair Set must be validated against exactly the Findings it names: "
            f"missing={sorted(set(wanted)-set(finding_by_id))} extra={sorted(set(finding_by_id)-set(wanted))}"
        )
    fixtures = set(repair.get("regression_fixtures", []))
    if status in {"IMPLEMENTED", "VALIDATED", "CLOSED"}:
        for fid, finding in finding_by_id.items():
            if finding.get("requires_regression"):
                fixture = finding.get("regression_fixture")
                if not _nonempty(fixture) or fixture not in fixtures:
                    errors.append(f"Repair Set missing required regression fixture for {fid}")
    if status == "CLOSED":
        for fid, finding in finding_by_id.items():
            if finding.get("status") != "CLOSED":
                errors.append(f"CLOSED Repair Set requires CLOSED Finding: {fid}")
            if finding.get("resolved_by_repair_set_id") != repair_id:
                errors.append(f"CLOSED Repair Set Finding resolution authority mismatch: {fid}")
    else:
        for fid, finding in finding_by_id.items():
            if finding.get("status") == "CLOSED":
                errors.append(f"non-CLOSED Repair Set cannot authorize CLOSED Finding: {fid}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    finding = sub.add_parser("finding-check")
    finding.add_argument("--finding", required=True)
    repair = sub.add_parser("repair-check")
    repair.add_argument("--repair", required=True)
    repair.add_argument("--finding", action="append", default=[])
    args = parser.parse_args()
    try:
        if args.command == "finding-check":
            errors = validate_finding(core.load_json(Path(args.finding)))
        else:
            repair_value = core.load_json(Path(args.repair))
            errors = validate_repair_set(
                repair_value,
                [core.load_json(Path(path)) for path in args.finding],
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
