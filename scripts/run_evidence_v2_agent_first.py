#!/usr/bin/env python3
"""Agent-first entrypoint for Core v2 interactive Evidence.

The accepted Discovery artifact intentionally stores a compact normalized
summary in its ``records`` field, while the canonical Discovery JSONL preserves
the full Core v2 ``provenance`` object. The interactive Evidence runner needs
that full provenance when deriving named-obligation traceability and Thematic
closure counters. This entrypoint preserves the accepted artifact validation,
then substitutes only the already hash-pinned canonical Discovery JSONL records
into the runner's in-memory acceptance view.

No repository bytes are modified by this adapter; the downstream runner still
validates and content-addresses all Evidence, Edition View, Materiality and
Completeness artifacts normally.
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


def main() -> int:
    original = runner.discovery.validate_acceptance

    def validated(repo_root: Path, acceptance_path: Path) -> dict[str, Any]:
        return acceptance_with_canonical_discovery_records(
            original, repo_root, acceptance_path
        )

    runner.discovery.validate_acceptance = validated
    try:
        return runner.main()
    finally:
        runner.discovery.validate_acceptance = original


if __name__ == "__main__":
    raise SystemExit(main())
