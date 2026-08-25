#!/usr/bin/env python3
"""Compatibility wrapper adding bounded cross-package synthesis Draft support.

The canonical v2 Architecture permits a package with no direct PRIMARY or
SUPPORTING candidate destinations, while the original Draft builder rejected
all such packages.  A single final empty-placement package is now interpreted
as an explicit cross-package synthesis package: it may cite the Evidence that
is already authorized by candidate placements in the other Architecture
packages without creating a second Architecture destination for those
candidates.

All ordinary evidence-owning packages delegate unchanged to the frozen base
implementation.  Cross-package references are Draft-time SUPPORTING inputs
only; they do not mutate Selection or Architecture destination semantics.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import survey_drafting_v2_base as _base
from scripts import survey_production_v2 as core

_ORIGINAL_DERIVE_DRAFT_PACKAGE = _base.derive_draft_package
_ORIGINAL_VALIDATE_SELF_CONTAINED = _base.validate_self_contained_draft_package


def _direct_candidate_ids(package: dict[str, Any]) -> list[str]:
    return [
        *list(package.get("primary_candidate_ids", [])),
        *list(package.get("supporting_candidate_ids", [])),
    ]


def _cross_package_reference_ids(
    plan: dict[str, Any],
    plan_package: dict[str, Any],
) -> list[str]:
    """Return ordered Evidence references for one final synthesis-only package.

    Empty placement is intentionally narrow: exactly one Architecture package
    may have no direct candidates, and it must be last in drafting order.  Its
    references are the de-duplicated candidates already placed in all other
    packages.  These references do not count as Architecture destinations.
    """
    if _direct_candidate_ids(plan_package):
        return []
    packages = plan.get("packages")
    if not isinstance(packages, list) or not packages:
        raise ValueError("Architecture packages must be a non-empty array")
    empty_packages = [
        row for row in packages
        if isinstance(row, dict) and not _direct_candidate_ids(row)
    ]
    if len(empty_packages) != 1 or empty_packages[0].get("package_id") != plan_package.get("package_id"):
        raise ValueError(
            "Architecture may contain exactly one empty-placement cross-package synthesis package"
        )
    orders = [row.get("drafting_order") for row in packages if isinstance(row, dict)]
    if not orders or any(not isinstance(value, int) for value in orders):
        raise ValueError("Architecture drafting_order values must be integers")
    if plan_package.get("drafting_order") != max(orders):
        raise ValueError("cross-package synthesis package must be last in drafting order")

    references: list[str] = []
    seen: set[str] = set()
    for row in sorted(packages, key=lambda value: (value["drafting_order"], value["package_id"])):
        if row.get("package_id") == plan_package.get("package_id"):
            continue
        for candidate_id in _direct_candidate_ids(row):
            if candidate_id not in seen:
                seen.add(candidate_id)
                references.append(candidate_id)
    if not references:
        raise ValueError("cross-package synthesis package has no authorized Evidence references")
    return references


def derive_draft_package(
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_path: Path,
    evidence_path: Path,
    views_path: Path,
    ledger_path: Path,
    completeness_path: Path,
    matrix_path: Path,
    selection_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
    package_id: str,
    implementation_sha: str,
) -> dict[str, Any]:
    plan = core.load_json(architecture_path)
    packages = [row for row in plan.get("packages", []) if row.get("package_id") == package_id]
    if len(packages) != 1:
        raise ValueError(f"Draft package_id must resolve exactly once in Architecture: {package_id}")
    plan_package = packages[0]
    if _direct_candidate_ids(plan_package):
        return _ORIGINAL_DERIVE_DRAFT_PACKAGE(
            repo_root, profile_path, discovery_path, screening_path, evidence_path,
            views_path, ledger_path, completeness_path, matrix_path, selection_path,
            architecture_path, review_summary_path, approval_path, package_id,
            implementation_sha,
        )

    reference_ids = _cross_package_reference_ids(plan, plan_package)
    upstream = _base._load_drafting_basis(
        repo_root, profile_path, discovery_path, screening_path, evidence_path,
        views_path, ledger_path, completeness_path, matrix_path, selection_path,
        architecture_path, review_summary_path, approval_path, implementation_sha,
    )
    profile = upstream["profile"]
    matrix = upstream["matrix"]
    evidence_acceptance = upstream["evidence"]
    matrix_by_id = {row["candidate_id"]: row for row in matrix["rows"]}
    evidence_by_task = {
        row["evidence_task_id"]: row for row in evidence_acceptance["results"]
    }

    inputs: list[dict[str, Any]] = []
    for candidate_id in reference_ids:
        row = matrix_by_id.get(candidate_id)
        if row is None:
            raise ValueError(
                f"cross-package synthesis references unknown Matrix candidate: {candidate_id}"
            )
        task_id = row["evidence_task_id"]
        result_meta = evidence_by_task.get(task_id)
        if result_meta is None or result_meta["sha256"] != row["evidence_sha256"]:
            raise ValueError(f"Draft Evidence/Matrix identity mismatch: {task_id}")
        card_path = evidence_path.parent / "results" / result_meta["filename"]
        if core.sha256_file(card_path) != result_meta["sha256"]:
            raise ValueError(f"Draft Evidence bytes changed: {task_id}")
        inputs.append({
            "candidate_id": candidate_id,
            "architecture_usage": "SUPPORTING",
            "evidence_task_id": task_id,
            "evidence_sha256": result_meta["sha256"],
            "evidence_card": core.load_json(card_path),
        })

    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "package_id": package_id,
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "architecture_sha256": core.sha256_file(architecture_path),
            "architecture_review_summary_sha256": core.sha256_file(review_summary_path),
            "architecture_approval_sha256": core.sha256_file(approval_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
            "evidence_acceptance_sha256": core.sha256_file(evidence_path),
        },
        "package": {
            "title": plan_package["title"],
            "purpose": plan_package["purpose"],
            "drafting_order": plan_package["drafting_order"],
            "primary_candidate_ids": list(plan_package["primary_candidate_ids"]),
            "supporting_candidate_ids": list(plan_package["supporting_candidate_ids"]),
            "must_cover_requirements": list(plan_package["must_cover_requirements"]),
            "boundaries": list(plan_package["boundaries"]),
        },
        "candidate_matrix": matrix,
        "evidence_acceptance": evidence_acceptance,
        "evidence_inputs": inputs,
        "drafting_constraints": {
            "language": "ja",
            "raw_sources_forbidden": True,
            "unknowns_remain_unknown": True,
            "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
        },
        "profile_extensions": dict(plan_package["profile_extensions"]),
        "publication_extensions": dict(plan_package["publication_extensions"]),
    }


def validate_self_contained_draft_package(
    package: dict[str, Any],
    profile_path: Path,
    architecture_path: Path,
    review_summary_path: Path,
    approval_path: Path,
) -> list[str]:
    plan = core.load_json(architecture_path)
    matching = [
        row for row in plan.get("packages", [])
        if row.get("package_id") == package.get("package_id")
    ]
    if len(matching) != 1:
        return ["Draft Package package_id does not resolve exactly once in Architecture"]
    plan_package = matching[0]
    if _direct_candidate_ids(plan_package):
        return _ORIGINAL_VALIDATE_SELF_CONTAINED(
            package, profile_path, architecture_path, review_summary_path, approval_path
        )

    try:
        reference_ids = _cross_package_reference_ids(plan, plan_package)
    except ValueError as exc:
        return [str(exc)]

    # Let the frozen validator verify the entire ordinary envelope/editorial
    # package with the reference list removed; empty direct placement is valid
    # at the Architecture layer.  Then validate the cross-package Evidence
    # references below against the embedded Matrix and accepted Evidence bytes.
    stripped = deepcopy(package)
    stripped["evidence_inputs"] = []
    errors = _ORIGINAL_VALIDATE_SELF_CONTAINED(
        stripped, profile_path, architecture_path, review_summary_path, approval_path
    )

    matrix = package.get("candidate_matrix")
    acceptance = package.get("evidence_acceptance")
    inputs = package.get("evidence_inputs")
    if not isinstance(matrix, dict) or not isinstance(acceptance, dict) or not isinstance(inputs, list):
        return errors + ["Draft Package Matrix/Evidence acceptance/inputs must be valid objects/array"]
    matrix_rows = matrix.get("rows")
    acceptance_results = acceptance.get("results")
    if not isinstance(matrix_rows, list) or not isinstance(acceptance_results, list):
        return errors + ["Draft Package Matrix rows/Evidence results must be arrays"]
    matrix_by_id = {
        row.get("candidate_id"): row for row in matrix_rows
        if isinstance(row, dict) and _base._nonempty(row.get("candidate_id"))
    }
    evidence_by_task = {
        row.get("evidence_task_id"): row for row in acceptance_results
        if isinstance(row, dict) and _base._nonempty(row.get("evidence_task_id"))
    }
    expected = set(reference_ids)
    seen: set[str] = set()
    for offset, item in enumerate(inputs):
        prefix = f"evidence_inputs[{offset}]"
        if not isinstance(item, dict) or set(item) != {
            "candidate_id", "architecture_usage", "evidence_task_id",
            "evidence_sha256", "evidence_card",
        }:
            errors.append(f"{prefix} fields invalid")
            continue
        candidate_id = item.get("candidate_id")
        if candidate_id in seen:
            errors.append(f"Draft Package duplicates candidate Evidence input: {candidate_id}")
            continue
        seen.add(candidate_id)
        row = matrix_by_id.get(candidate_id)
        if row is None or candidate_id not in expected:
            errors.append(
                f"{prefix} references candidate outside authorized cross-package synthesis basis: {candidate_id}"
            )
            continue
        if item.get("architecture_usage") != "SUPPORTING":
            errors.append(f"{prefix} cross-package reference must use SUPPORTING Draft usage")
        task_id = item.get("evidence_task_id")
        if task_id != row.get("evidence_task_id") or item.get("evidence_sha256") != row.get("evidence_sha256"):
            errors.append(f"{prefix} Candidate Matrix Evidence binding mismatch")
            continue
        meta = evidence_by_task.get(task_id)
        if meta is None or meta.get("sha256") != item.get("evidence_sha256"):
            errors.append(f"{prefix} Evidence acceptance binding mismatch")
        card = item.get("evidence_card")
        if not isinstance(card, dict) or _base._object_sha(card) != item.get("evidence_sha256"):
            errors.append(f"{prefix} embedded Evidence Card bytes do not match accepted Evidence SHA")
        elif card.get("evidence_task_id") != task_id or card.get("issue_id") != package.get("issue_id"):
            errors.append(f"{prefix} embedded Evidence Card identity mismatch")
    if seen != expected:
        errors.append(
            "cross-package synthesis Draft Package must contain exactly one reference to every candidate already placed by the other Architecture packages"
        )
    return errors


# Patch the frozen implementation's globals so its generic helpers and CLI use
# the repaired behavior while retaining all unrelated v2 logic byte-for-byte.
_base.derive_draft_package = derive_draft_package
_base.validate_self_contained_draft_package = validate_self_contained_draft_package


def __getattr__(name: str) -> Any:
    return getattr(_base, name)


def main() -> int:
    return _base.main()


if __name__ == "__main__":
    raise SystemExit(main())
