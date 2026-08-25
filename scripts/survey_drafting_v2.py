#!/usr/bin/env python3
"""Compatibility wrapper adding bounded cross-package synthesis Draft support.

The canonical v2 Architecture permits a package with no direct PRIMARY or
SUPPORTING candidate destinations, while the original Draft builder rejected
all such packages. A single final empty-placement package is interpreted as an
explicit cross-package synthesis package: it may cite Evidence already
authorized by candidate placements in the other Architecture packages without
creating a second Architecture destination for those candidates.

Draft Package validation also remains upgrade-safe across reviewed Core JSON
serializer changes. Historical Matrix / Evidence Acceptance / Evidence Card
SHA-256 values bind their exact accepted raw bytes; the validator verifies those
raw files first and then compares their parsed objects to the embedded package
objects. It never attempts to reconstruct historical bytes by reserializing an
old parsed object with the current serializer.

All ordinary evidence-owning packages otherwise delegate unchanged to the
frozen base implementation. Cross-package references are Draft-time SUPPORTING
inputs only; they do not mutate Selection or Architecture destination semantics.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

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
    may have no direct candidates, and it must be last in drafting order. Its
    references are the de-duplicated candidates already placed in all other
    packages. These references do not count as Architecture destinations.
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


def _record_raw_hash(
    raw_hashes: dict[str, str],
    value: dict[str, Any],
    raw_sha256: str,
    label: str,
    errors: list[str],
) -> None:
    semantic = core.sha256_object(value)
    previous = raw_hashes.get(semantic)
    if previous is not None and previous != raw_sha256:
        errors.append(f"{label} semantic object maps to divergent accepted raw hashes")
        return
    raw_hashes[semantic] = raw_sha256


def _historical_raw_authority_hashes(
    package: dict[str, Any],
    profile_path: Path,
) -> tuple[list[str], dict[str, str]]:
    """Verify exact canonical upstream bytes and map parsed objects to raw hashes.

    Core v2 production keeps the Candidate Matrix at the edition source root and
    accepted Evidence in its content-addressed ``evidence/v2/accepted`` tree.
    Older accepted JSON may use a serializer different from current
    ``core.json_bytes``. When canonical authority is present, validate exact raw
    SHA-256 first and require parsed-object equality with the Draft Package.

    Lightweight isolated unit fixtures that do not materialize the canonical
    accepted-Evidence tree retain the frozen validator's historical behavior.
    Once that tree exists, missing/drifted canonical files fail closed.
    """
    errors: list[str] = []
    raw_hashes: dict[str, str] = {}
    basis = package.get("basis")
    matrix = package.get("candidate_matrix")
    acceptance = package.get("evidence_acceptance")
    inputs = package.get("evidence_inputs")
    if not isinstance(basis, dict) or not isinstance(matrix, dict) or not isinstance(acceptance, dict):
        return errors, raw_hashes
    if not isinstance(inputs, list):
        return errors, raw_hashes

    source_root = profile_path.parent
    matrix_path = source_root / "candidate-matrix-v2.json"
    accepted_root = source_root / "evidence" / "v2" / "accepted"
    matrix_exists = matrix_path.is_file()
    accepted_root_exists = accepted_root.is_dir()
    if not matrix_exists and not accepted_root_exists:
        # Compatibility is limited to isolated legacy/unit fixtures that never
        # materialized either canonical production authority component.
        return errors, raw_hashes
    if not matrix_exists:
        return ["Draft Package canonical Candidate Matrix is missing"], {}
    if not accepted_root_exists:
        return ["Draft Package canonical accepted Evidence authority is missing"], {}

    matrix_sha = basis.get("candidate_matrix_sha256")
    if not isinstance(matrix_sha, str) or core.sha256_file(matrix_path) != matrix_sha:
        errors.append("Draft Package canonical Candidate Matrix raw bytes drifted")
    else:
        raw_matrix = core.load_json(matrix_path)
        if raw_matrix != matrix:
            errors.append("Draft Package embedded Candidate Matrix differs from canonical accepted object")
        else:
            _record_raw_hash(raw_hashes, matrix, matrix_sha, "Candidate Matrix", errors)

    result_set = acceptance.get("result_set_sha256")
    if not isinstance(result_set, str) or not result_set:
        errors.append("Draft Package embedded Evidence acceptance lacks result_set_sha256")
        return errors, raw_hashes
    acceptance_path = accepted_root / result_set / "evidence-accepted.json"
    acceptance_sha = basis.get("evidence_acceptance_sha256")
    if (
        not acceptance_path.is_file()
        or not isinstance(acceptance_sha, str)
        or core.sha256_file(acceptance_path) != acceptance_sha
    ):
        errors.append("Draft Package canonical Evidence Acceptance raw bytes drifted or are missing")
        return errors, raw_hashes
    raw_acceptance = core.load_json(acceptance_path)
    if raw_acceptance != acceptance:
        errors.append("Draft Package embedded Evidence Acceptance differs from canonical accepted object")
        return errors, raw_hashes
    _record_raw_hash(raw_hashes, acceptance, acceptance_sha, "Evidence Acceptance", errors)

    results = acceptance.get("results")
    if not isinstance(results, list):
        errors.append("Draft Package embedded Evidence Acceptance results must be an array")
        return errors, raw_hashes
    by_task = {
        row.get("evidence_task_id"): row
        for row in results
        if isinstance(row, dict) and isinstance(row.get("evidence_task_id"), str)
    }
    for offset, item in enumerate(inputs):
        prefix = f"evidence_inputs[{offset}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        task_id = item.get("evidence_task_id")
        meta = by_task.get(task_id)
        if meta is None:
            errors.append(f"{prefix} has no canonical Evidence Acceptance result")
            continue
        filename = meta.get("filename")
        expected_sha = item.get("evidence_sha256")
        if (
            not isinstance(filename, str)
            or not filename
            or not isinstance(expected_sha, str)
            or meta.get("sha256") != expected_sha
        ):
            errors.append(f"{prefix} Evidence Acceptance metadata mismatch")
            continue
        card_path = acceptance_path.parent / "results" / filename
        if not card_path.is_file() or core.sha256_file(card_path) != expected_sha:
            errors.append(f"{prefix} canonical Evidence Card raw bytes drifted or are missing")
            continue
        raw_card = core.load_json(card_path)
        embedded_card = item.get("evidence_card")
        if not isinstance(embedded_card, dict) or raw_card != embedded_card:
            errors.append(f"{prefix} embedded Evidence Card differs from canonical accepted object")
            continue
        _record_raw_hash(raw_hashes, embedded_card, expected_sha, prefix, errors)
    return errors, raw_hashes


def _run_with_authoritative_raw_hashes(
    callback: Callable[[], list[str]],
    raw_hashes: dict[str, str],
) -> list[str]:
    """Let the frozen semantic validator consume verified historical raw hashes."""
    if not raw_hashes:
        return callback()
    original = _base._object_sha

    def authority_aware_object_sha(value: Any) -> str:
        if isinstance(value, dict):
            accepted = raw_hashes.get(core.sha256_object(value))
            if accepted is not None:
                return accepted
        return original(value)

    _base._object_sha = authority_aware_object_sha
    try:
        return callback()
    finally:
        _base._object_sha = original


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
    raw_errors, raw_hashes = _historical_raw_authority_hashes(package, profile_path)
    if raw_errors:
        return raw_errors

    plan = core.load_json(architecture_path)
    matching = [
        row for row in plan.get("packages", [])
        if row.get("package_id") == package.get("package_id")
    ]
    if len(matching) != 1:
        return ["Draft Package package_id does not resolve exactly once in Architecture"]
    plan_package = matching[0]
    if _direct_candidate_ids(plan_package):
        return _run_with_authoritative_raw_hashes(
            lambda: _ORIGINAL_VALIDATE_SELF_CONTAINED(
                package, profile_path, architecture_path, review_summary_path, approval_path
            ),
            raw_hashes,
        )

    try:
        reference_ids = _cross_package_reference_ids(plan, plan_package)
    except ValueError as exc:
        return [str(exc)]

    # Let the frozen validator verify the ordinary envelope/editorial package
    # with the cross-package reference list removed, while historical raw
    # Matrix/Acceptance SHA values are supplied from already verified authority.
    stripped = deepcopy(package)
    stripped["evidence_inputs"] = []
    errors = _run_with_authoritative_raw_hashes(
        lambda: _ORIGINAL_VALIDATE_SELF_CONTAINED(
            stripped, profile_path, architecture_path, review_summary_path, approval_path
        ),
        raw_hashes,
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
        if isinstance(card, dict) and raw_hashes:
            authoritative_sha = raw_hashes.get(core.sha256_object(card))
        elif isinstance(card, dict):
            authoritative_sha = _base._object_sha(card)
        else:
            authoritative_sha = None
        if authoritative_sha != item.get("evidence_sha256"):
            errors.append(f"{prefix} embedded Evidence Card does not match exact accepted raw authority")
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
