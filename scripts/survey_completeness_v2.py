#!/usr/bin/env python3
"""Authoritative Profile Completeness guard for Survey Production Core v2.

The base validator in survey_evidence_v2 checks Profile dimensions, exact
Materiality basis, and Thematic closure/saturation. This final guard additionally
proves that every named research obligation emitted by Discovery is represented
and traceable back to the Discovery records that created it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import survey_evidence_v2 as evidence
from scripts import survey_screening_v2 as screening


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
    named: dict[str, set[str]] = {}
    for discovery in discoveries:
        provenance = discovery.get("provenance")
        if not isinstance(provenance, dict):
            continue
        for obligation_id in provenance.get("obligation_ids", []):
            if isinstance(obligation_id, str) and obligation_id:
                named.setdefault(obligation_id, set()).add(discovery.get("discovery_id"))

    obligations = result.get("obligations")
    if not isinstance(obligations, list):
        return errors
    by_id = {
        row.get("obligation_id"): row
        for row in obligations
        if isinstance(row, dict) and isinstance(row.get("obligation_id"), str)
    }
    missing = sorted(set(named) - set(by_id))
    if missing:
        errors.append(f"Completeness silently dropped named Discovery obligations: {missing}")

    for obligation_id, discovery_ids in named.items():
        row = by_id.get(obligation_id)
        if row is None:
            continue
        refs = row.get("discovery_ids")
        if not isinstance(refs, list):
            errors.append(f"named obligation {obligation_id} has invalid discovery_ids")
            continue
        missing_refs = sorted(discovery_ids - set(refs))
        if missing_refs:
            errors.append(
                f"named obligation {obligation_id} does not trace back to declaring Discovery records: {missing_refs}"
            )
    return errors
