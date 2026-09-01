#!/usr/bin/env python3
"""Run a complete Core v2 Screening pass from explicit interactive decisions.

The runner is profile-neutral. It requires one explicit Screening decision for
exactly every accepted Discovery record, regenerates the canonical Core v2
Screening package from the current agent-first Production State, materializes
one exact result per generated batch, validates/accepts the result set through
``survey_screening_v2``, and archives the interactive decision bytes alongside
the content-addressed accepted run.

This runner does not advance Production State and cannot resolve a Human Gate.
"""
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

INPUT_NAME = "interactive-decisions.json"
AUDIT_NAME = "interactive-audit.json"


def load_json(path: Path) -> dict[str, Any]:
    value = core.load_json(path)
    return value


def _rel(repo_root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(repo_root.resolve()))


def validate_interactive_input(
    value: dict[str, Any], issue_id: str, expected_ids: set[str]
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    if set(value) != {"schema_version", "issue_id", "runner", "decisions"}:
        raise ValueError("interactive Screening input fields invalid")
    if value.get("schema_version") != "2.0-rc1" or value.get("issue_id") != issue_id:
        raise ValueError("interactive Screening input identity mismatch")

    runner = value.get("runner")
    if not isinstance(runner, dict) or set(runner) != {"provider", "model", "invocation", "generated_at"}:
        raise ValueError("interactive Screening runner fields invalid")
    normalized_runner: dict[str, str] = {}
    for key in ("provider", "model", "invocation", "generated_at"):
        item = runner.get(key)
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"interactive Screening runner.{key} required")
        normalized_runner[key] = item
    core.parse_instant(normalized_runner["generated_at"])

    decisions = value.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("interactive Screening decisions must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(decisions):
        if not isinstance(row, dict):
            raise ValueError(f"interactive Screening decisions[{index}] must be an object")
        errors = screening.validate_decision(row)
        if errors:
            raise ValueError(
                f"interactive Screening decision {row.get('discovery_id')!r} invalid: "
                + "; ".join(errors)
            )
        discovery_id = row["discovery_id"]
        if discovery_id in by_id:
            raise ValueError(f"duplicate interactive Screening decision: {discovery_id}")
        by_id[discovery_id] = row

    actual_ids = set(by_id)
    if actual_ids != expected_ids:
        raise ValueError(
            "interactive Screening decisions must cover exactly accepted Discovery IDs: "
            f"missing={sorted(expected_ids - actual_ids)} extra={sorted(actual_ids - expected_ids)}"
        )
    return by_id, normalized_runner


def _archive_auxiliary_bytes(
    repo_root: Path,
    acceptance_path: Path,
    decisions_path: Path,
    runner: dict[str, str],
    decision_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    run_dir = acceptance_path.parent
    archived_input = run_dir / INPUT_NAME
    if archived_input.exists():
        if core.sha256_file(archived_input) != core.sha256_file(decisions_path):
            raise ValueError("accepted Screening run has conflicting interactive decision bytes")
    else:
        shutil.copy2(decisions_path, archived_input)

    counts = Counter(row["decision"] for row in decision_rows)
    audit = {
        "schema_version": "2.0-rc1",
        "issue_id": core.load_json(acceptance_path)["issue_id"],
        "acceptance": {
            "path": _rel(repo_root, acceptance_path),
            "sha256": core.sha256_file(acceptance_path),
        },
        "interactive_decisions": {
            "path": _rel(repo_root, archived_input),
            "sha256": core.sha256_file(archived_input),
        },
        "runner": runner,
        "decision_counts": {
            key: counts.get(key, 0) for key in ("KEEP", "MAYBE", "INSPECT", "DROP")
        },
    }
    audit_path = run_dir / AUDIT_NAME
    if audit_path.exists():
        if core.load_json(audit_path) != audit:
            raise ValueError("accepted Screening run has conflicting interactive audit bytes")
    else:
        core.write_json(audit_path, audit)
    return audit


def run(repo_root: Path, state_path: Path, decisions_path: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    state_path = state_path.resolve()
    decisions_path = decisions_path.resolve()

    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before interactive Screening: " + "; ".join(errors))
    if state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("interactive Screening requires DISCOVERY_COLLECTED Production State")

    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    accepted_discovery_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(repo_root, accepted_discovery_path)
    if accepted_discovery.get("issue_id") != state["issue_id"]:
        raise ValueError("accepted Discovery/Production State issue identity mismatch")
    discovery_path = core.repo_local_path(
        repo_root, accepted_discovery["discovery_path"], "accepted Discovery JSONL"
    )

    expected_ids = {row["discovery_id"] for row in accepted_discovery["records"]}
    decision_doc = load_json(decisions_path)
    decisions_by_id, runner = validate_interactive_input(
        decision_doc, state["issue_id"], expected_ids
    )

    implementation_sha = core.repository_commit_sha(repo_root)
    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        package_root = temp_root / "package"
        with agent_tool.current_stage_basis_override():
            package_path = screening.prepare_package(
                repo_root,
                state_path,
                discovery_path,
                package_root,
                implementation_sha,
            )
        package = core.load_json(package_path)
        results_dir = temp_root / "results"
        results_dir.mkdir()
        seen: set[str] = set()
        for batch in package["input"]["batches"]:
            batch_path = package_path.parent / batch["path"]
            records = screening.read_jsonl(batch_path)
            rows: list[dict[str, Any]] = []
            for record in records:
                discovery_id = record["discovery_id"]
                if discovery_id in seen:
                    raise ValueError(f"generated Screening package duplicated {discovery_id}")
                seen.add(discovery_id)
                rows.append(decisions_by_id[discovery_id])
            result = {
                "schema_version": "2.0-rc1",
                "issue_id": state["issue_id"],
                "batch_id": batch["batch_id"],
                "basis": screening.expected_result_basis(
                    repo_root, package_path, package, batch
                ),
                "decisions": rows,
            }
            core.write_json(results_dir / f"{batch['batch_id']}.json", result)
        if seen != expected_ids:
            raise ValueError("generated Screening package did not cover accepted Discovery exactly")

        accepted_root = source_root / "screening/v2/accepted"
        with agent_tool.current_stage_basis_override():
            acceptance_path = screening.accept_results(
                repo_root,
                package_path,
                results_dir,
                accepted_root,
                implementation_sha,
            )

    ordered_decisions = [decisions_by_id[key] for key in sorted(decisions_by_id)]
    audit = _archive_auxiliary_bytes(
        repo_root, acceptance_path, decisions_path, runner, ordered_decisions
    )
    return {
        "acceptance_path": _rel(repo_root, acceptance_path),
        "acceptance_sha256": core.sha256_file(acceptance_path),
        "result_set_sha256": core.load_json(acceptance_path)["result_set_sha256"],
        "record_count": len(ordered_decisions),
        "decision_counts": audit["decision_counts"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--state", required=True)
    parser.add_argument("--decisions", required=True)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    state = Path(args.state)
    decisions = Path(args.decisions)
    if not state.is_absolute():
        state = root / state
    if not decisions.is_absolute():
        decisions = root / decisions
    try:
        print(json.dumps(run(root, state, decisions), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=__import__("sys").stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
