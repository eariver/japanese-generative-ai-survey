#!/usr/bin/env python3
"""Agent-first entrypoint for Core v2 interactive Evidence.

The accepted Discovery artifact intentionally stores a compact normalized
summary in its ``records`` field, while the canonical Discovery JSONL preserves
the full Core v2 ``provenance`` object. The interactive Evidence runner needs
that full provenance when deriving named-obligation traceability and Thematic
closure counters. This entrypoint preserves the accepted artifact validation,
then substitutes only the already hash-pinned canonical Discovery JSONL records
into the runner's in-memory acceptance view.

The Core v2 Completeness contract also requires every residual limitation to
survive into a LIMITED Thematic closure payload. Interactive input may add
closure-specific wording, but it may not silently omit a residual limitation.
This adapter therefore normalizes the generated in-memory Completeness result by
unioning residual limitations into closure.limitations before the authoritative
schema/completeness validators run.

No repository authority is bypassed: canonical Discovery bytes stay hash-pinned,
and the downstream runner still validates and content-addresses all Evidence,
Edition View, Materiality and Completeness artifacts normally.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import run_evidence_v2_interactive as runner
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


def acceptance_with_canonical_discovery_records(
    original,
    repo_root: Path,
    acceptance_path: Path,
) -> dict[str, Any]:
    accepted = original(repo_root, acceptance_path)
    discovery_path = core.repo_local_path(
        repo_root,
        accepted["discovery_path"],
        "accepted Discovery JSONL",
    )
    if core.sha256_file(discovery_path) != accepted["discovery_sha256"]:
        raise ValueError("accepted Discovery JSONL bytes changed")
    records = screening.read_jsonl(discovery_path)
    screening.validate_discovery_set(records, accepted["issue_id"])
    if len(records) != accepted["record_count"]:
        raise ValueError("accepted Discovery record_count/JSONL divergence")
    result = dict(accepted)
    result["records"] = records
    return result


def completeness_with_preserved_residual_limitations(original, *args, **kwargs) -> dict[str, Any]:
    result = original(*args, **kwargs)
    if result.get("research_profile") != "THEMATIC":
        return result
    closure = result.get("closure")
    residual = result.get("residual_limitations")
    if not isinstance(closure, dict) or not isinstance(residual, list):
        return result
    closure_limitations = closure.get("limitations")
    if not isinstance(closure_limitations, list):
        return result
    normalized = list(closure_limitations)
    for limitation in residual:
        if limitation not in normalized:
            normalized.append(limitation)
    if normalized == closure_limitations:
        return result
    updated = dict(result)
    updated_closure = dict(closure)
    updated_closure["limitations"] = normalized
    updated["closure"] = updated_closure
    return updated


def main() -> int:
    original_discovery = runner.discovery.validate_acceptance
    original_completeness = runner._build_completeness

    def validated(repo_root: Path, acceptance_path: Path) -> dict[str, Any]:
        return acceptance_with_canonical_discovery_records(
            original_discovery, repo_root, acceptance_path
        )

    def complete(*args, **kwargs) -> dict[str, Any]:
        return completeness_with_preserved_residual_limitations(
            original_completeness, *args, **kwargs
        )

    runner.discovery.validate_acceptance = validated
    runner._build_completeness = complete
    try:
        return runner.main()
    finally:
        runner._build_completeness = original_completeness
        runner.discovery.validate_acceptance = original_discovery


if __name__ == "__main__":
    raise SystemExit(main())
