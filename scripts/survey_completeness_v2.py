#!/usr/bin/env python3
"""Authoritative Profile Completeness guard for Survey Production Core v2.

The base validator in survey_evidence_v2 checks Profile dimensions, exact
Materiality basis, and the internal consistency of Thematic closure fields. This
final guard additionally proves that:
- every Profile-defined initial research obligation is retained;
- every named research obligation emitted by Discovery is represented and
  traceable back to the Discovery records that created it;
- Completeness obligation rows conform to the machine-readable contract instead
  of relying on permissive ``dict.get`` defaults; and
- Thematic expansion counters are derived from Discovery provenance rather than
  trusted as self-reported saturation evidence.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

OBLIGATION_KEYS = {
    "obligation_id",
    "dimension",
    "description",
    "status",
    "discovery_ids",
    "evidence_task_ids",
    "rationale",
}
OBLIGATION_STATUS = {"SATISFIED", "LIMITATION", "NEEDS_RESEARCH", "NOT_APPLICABLE"}
MATERIAL_OBLIGATION_STATUS = {"SATISFIED", "LIMITATION", "NEEDS_RESEARCH"}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _unique_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(set(value))
        and all(_nonempty(item) for item in value)
    )


def _validate_obligation_shape(
    row: dict[str, Any],
    allowed_dimensions: set[str],
    discovery_ids: set[str],
    evidence_task_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    if set(row) != OBLIGATION_KEYS:
        return [f"Completeness obligation fields must exactly match v2 contract: {row.get('obligation_id')}"]
    obligation_id = row.get("obligation_id")
    if not _nonempty(obligation_id):
        errors.append("Completeness obligation_id must be a non-empty string")
    if not _nonempty(row.get("dimension")) or row.get("dimension") not in allowed_dimensions:
        errors.append(f"Completeness obligation {obligation_id} dimension is not declared by the Production Profile")
    if not _nonempty(row.get("description")):
        errors.append(f"Completeness obligation {obligation_id} description missing")
    if row.get("status") not in OBLIGATION_STATUS:
        errors.append(f"Completeness obligation {obligation_id} status invalid")
    if not _unique_string_list(row.get("discovery_ids")):
        errors.append(f"Completeness obligation {obligation_id} discovery_ids must be a unique string array")
    elif any(value not in discovery_ids for value in row["discovery_ids"]):
        errors.append(f"Completeness obligation {obligation_id} references unknown Discovery")
    if not _unique_string_list(row.get("evidence_task_ids")):
        errors.append(f"Completeness obligation {obligation_id} evidence_task_ids must be a unique string array")
    elif any(value not in evidence_task_ids for value in row["evidence_task_ids"]):
        errors.append(f"Completeness obligation {obligation_id} references unknown Evidence task")
    if not _nonempty(row.get("rationale")):
        errors.append(f"Completeness obligation {obligation_id} rationale missing")
    return errors


def _thematic_closure_errors(
    result: dict[str, Any],
    discoveries: list[dict[str, Any]],
    obligations_by_id: dict[str, dict[str, Any]],
) -> list[str]:
    """Bind self-reported closure counters to Discovery provenance.

    ``research_pass=0`` is the initial/base corpus. Positive values represent
    actual expansion passes. A thematic corpus with no positive-pass Discovery
    still records one completed expansion attempt, but the final pass contains
    zero newly discovered sources.
    """

    errors: list[str] = []
    if result.get("research_profile") != "THEMATIC":
        return errors
    closure = result.get("closure")
    if not isinstance(closure, dict):
        return errors  # base validator reports the missing/invalid closure

    passes = [
        row.get("provenance", {}).get("research_pass")
        for row in discoveries
        if isinstance(row, dict) and isinstance(row.get("provenance"), dict)
    ]
    numeric_passes = [value for value in passes if isinstance(value, int) and value >= 0]
    max_pass = max(numeric_passes, default=0)
    expected_expansion_passes = max(1, max_pass)
    final_records = [
        row
        for row in discoveries
        if max_pass > 0 and row.get("provenance", {}).get("research_pass") == max_pass
    ]
    final_obligation_ids = {
        obligation_id
        for row in final_records
        for obligation_id in row.get("provenance", {}).get("obligation_ids", [])
        if isinstance(obligation_id, str) and obligation_id
    }
    final_material_ids = {
        obligation_id
        for obligation_id in final_obligation_ids
        if obligations_by_id.get(obligation_id, {}).get("status") in MATERIAL_OBLIGATION_STATUS
    }
    final_open_ids = {
        obligation_id
        for obligation_id in final_material_ids
        if obligations_by_id[obligation_id].get("status") == "NEEDS_RESEARCH"
    }

    expected = {
        "expansion_passes": expected_expansion_passes,
        "final_pass_new_sources": len(final_records),
        "final_pass_new_material_obligations": len(final_material_ids),
        "final_pass_new_material_obligations_open": len(final_open_ids),
    }
    for key, value in expected.items():
        if closure.get(key) != value:
            errors.append(
                f"Thematic closure {key} must be derived from Discovery provenance: expected {value}, got {closure.get(key)}"
            )
    return errors


def validate_profile_completeness(
    result: dict[str, Any],
    repo_root: Path,
    profile_path: Path,
    discovery_path: Path,
    screening_acceptance_path: Path,
    evidence_acceptance_path: Path,
    views_acceptance_path: Path,
    ledger_path: Path,
    implementation_sha: str,
) -> list[str]:
    errors = evidence.validate_completeness(
        result,
        repo_root,
        profile_path,
        discovery_path,
        screening_acceptance_path,
        evidence_acceptance_path,
        views_acceptance_path,
        ledger_path,
        implementation_sha,
    )

    discoveries = screening.read_jsonl(discovery_path)
    profile = core.load_json(profile_path)
    ledger = core.load_json(ledger_path)
    discovery_ids = {
        row.get("discovery_id") for row in discoveries if isinstance(row, dict) and _nonempty(row.get("discovery_id"))
    }
    evidence_task_ids = {
        task_id
        for row in ledger.get("rows", [])
        if isinstance(row, dict)
        for task_id in row.get("evidence_task_ids", [])
        if _nonempty(task_id)
    }
    research_scope = profile.get("research_scope", {})
    allowed_dimensions = set(research_scope.get("scope_dimensions", []))

    obligations = result.get("obligations")
    if not isinstance(obligations, list):
        return errors

    obligations_by_id: dict[str, dict[str, Any]] = {}
    for row in obligations:
        if not isinstance(row, dict):
            errors.append("Completeness obligation must be an object")
            continue
        errors.extend(
            _validate_obligation_shape(
                row,
                allowed_dimensions,
                discovery_ids,
                evidence_task_ids,
            )
        )
        obligation_id = row.get("obligation_id")
        if _nonempty(obligation_id):
            if obligation_id in obligations_by_id:
                errors.append(f"Completeness obligation_id duplicated: {obligation_id}")
            obligations_by_id[obligation_id] = row

    initial_obligations = research_scope.get("initial_obligations")
    if not isinstance(initial_obligations, list) or not initial_obligations:
        errors.append("Production Profile initial_obligations are missing")
    else:
        initial_ids: set[str] = set()
        for initial in initial_obligations:
            if not isinstance(initial, dict):
                errors.append("Production Profile initial obligation must be an object")
                continue
            obligation_id = initial.get("obligation_id")
            if not _nonempty(obligation_id):
                errors.append("Production Profile initial obligation_id invalid")
                continue
            if obligation_id in initial_ids:
                errors.append(f"Production Profile initial obligation duplicated: {obligation_id}")
                continue
            initial_ids.add(obligation_id)
            actual = obligations_by_id.get(obligation_id)
            if actual is None:
                errors.append(f"Completeness silently dropped Profile initial obligation: {obligation_id}")
                continue
            if actual.get("dimension") != initial.get("dimension"):
                errors.append(f"Completeness changed Profile initial obligation dimension: {obligation_id}")

    named: dict[str, set[str]] = {}
    for discovery in discoveries:
        provenance = discovery.get("provenance")
        if not isinstance(provenance, dict):
            continue
        for obligation_id in provenance.get("obligation_ids", []):
            if isinstance(obligation_id, str) and obligation_id:
                named.setdefault(obligation_id, set()).add(discovery.get("discovery_id"))

    missing = sorted(set(named) - set(obligations_by_id))
    if missing:
        errors.append(f"Completeness silently dropped named Discovery obligations: {missing}")

    for obligation_id, declaring_discovery_ids in named.items():
        row = obligations_by_id.get(obligation_id)
        if row is None:
            continue
        refs = row.get("discovery_ids")
        if not isinstance(refs, list):
            errors.append(f"named obligation {obligation_id} has invalid discovery_ids")
            continue
        missing_refs = sorted(declaring_discovery_ids - set(refs))
        if missing_refs:
            errors.append(
                f"named obligation {obligation_id} does not trace back to declaring Discovery records: {missing_refs}"
            )

    errors.extend(_thematic_closure_errors(result, discoveries, obligations_by_id))
    return errors
