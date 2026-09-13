#!/usr/bin/env python3
"""Complete canonical Materiality + Completeness from persisted acceptances.

Resume-run driver step B (edition-side orchestration). Calls ONLY reviewed-Core
functions in the SAME order/arguments as scripts/run_evidence_v2_interactive.py
run() lines 715-769. Prerequisite: step A views acceptance persisted.
Does NOT advance state.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(".").resolve()
sys.path.insert(0, str(REPO))
from scripts import survey_agent_control_v2 as agent  # noqa: E402
from scripts import survey_agent_tool_v2 as agent_tool  # noqa: E402
from scripts import survey_completeness_v2 as completeness  # noqa: E402
from scripts import survey_discovery_v2 as discovery  # noqa: E402
from scripts import survey_evidence_v2 as evidence  # noqa: E402
from scripts import survey_production_v2 as core  # noqa: E402
from scripts import survey_schema_v2 as schema_gate  # noqa: E402
from scripts import survey_screening_v2 as screening  # noqa: E402
from scripts import run_evidence_v2_interactive as runner  # noqa: E402

EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
EVIDENCE_ACCEPTANCE_REL = (
    "sources/2026-W34/evidence/v2/accepted/"
    "647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/"
    "evidence-accepted.json"
)
VIEWS_ACCEPTANCE_REL = (
    "sources/2026-W34/evidence/v2/views/accepted/"
    "e2e644bcc97ac664949b272fca919923385af6192c65b5a3566e30382b0ca7ba/"
    "edition-views-accepted.json"
)

def main() -> int:
    repo_root = REPO
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state_path = repo_root / "sources/2026-W34/production-state.json"
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("Production State invalid: " + "; ".join(errors))
    if state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("requires CANDIDATES_NORMALIZED")
    implementation_sha = core.repository_commit_sha(repo_root)
    print(f"implementation_sha={implementation_sha}", flush=True)

    with agent_tool.current_stage_basis_override():
        out = _complete(repo_root, state_path, state, implementation_sha)
    print(f"MATERIALITY_LEDGER={out['materiality_ledger']}", flush=True)
    print(f"PROFILE_COMPLETENESS={out['profile_completeness']}", flush=True)
    print(f"COMPLETENESS_STATUS={out['completeness_status']}", flush=True)
    return 0

def _complete(repo_root: Path, state_path: Path, state: dict, implementation_sha: str) -> dict:
    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    discovery_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(repo_root, discovery_acceptance_path)
    root_discovery_path = core.repo_local_path(repo_root, accepted_discovery["discovery_path"], "accepted Discovery JSONL")

    active_screening = screening.resolve_active_screening_acceptance(repo_root, state_path, implementation_sha)
    screening_acceptance_path = active_screening["path"]
    effective = screening.resolve_effective_discovery_basis(
        repo_root, screening_acceptance_path.parent / "package.json",
        implementation_sha, accepted_root_path=root_discovery_path,
    )
    discovery_path = effective["path"]
    discovery_records = effective["records"]
    print(f"discovery basis records={len(discovery_records)}", flush=True)

    evidence_acceptance_path = repo_root / EVIDENCE_ACCEPTANCE_REL
    evidence_acceptance, package = evidence.validate_evidence_acceptance(
        repo_root, evidence_acceptance_path, implementation_sha
    )
    views_acceptance_path = repo_root / VIEWS_ACCEPTANCE_REL

    ledger_path = source_root / "materiality-ledger-v2.json"
    if ledger_path.exists():
        raise ValueError(f"refusing to overwrite Materiality Ledger: {ledger_path}")
    ledger = evidence.build_materiality_ledger(
        repo_root, profile_path, discovery_path, screening_acceptance_path,
        evidence_acceptance_path, views_acceptance_path, implementation_sha,
    )
    evidence.write_materiality_ledger(ledger_path, ledger)
    print("materiality ledger written", flush=True)

    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    persisted_package = core.load_json(evidence_acceptance_path.parent / "package.json")
    task_source_ids = {
        did: set(evidence.task_authority_sources(
            repo_root,
            core.load_json(evidence_acceptance_path.parent / "tasks" / Path(meta["path"]).name),
            persisted_package,
        ))
        for did, meta in sorted(task_meta.items())
    }
    interactive_doc = core.load_json(repo_root / EXEC_REL / "interactive-evidence.json")
    _, runner_meta, completeness_input = runner.validate_interactive_input(
        interactive_doc, profile, set(task_meta), task_source_ids
    )

    completeness_path = source_root / "profile-completeness-v2.json"
    if completeness_path.exists():
        raise ValueError(f"refusing to overwrite Profile Completeness: {completeness_path}")
    result = runner._build_completeness(
        repo_root, profile, profile_path, discovery_records,
        ledger_path, ledger, completeness_input,
    )
    schema_gate.validate_instance(
        result, repo_root / "schemas/profile-completeness-result.schema.json",
        label="Profile Completeness",
    )
    errs = completeness.validate_profile_completeness(
        result, repo_root, profile_path, discovery_path, screening_acceptance_path,
        evidence_acceptance_path, views_acceptance_path, ledger_path, implementation_sha,
    )
    if errs:
        raise ValueError("Profile Completeness invalid: " + "; ".join(errs))
    core.write_json(completeness_path, result)
    print("profile completeness written", flush=True)

    outputs = {
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(repo_root)),
        "edition_views_acceptance": str(views_acceptance_path.relative_to(repo_root)),
        "materiality_ledger": str(ledger_path.relative_to(repo_root)),
        "profile_completeness": str(completeness_path.relative_to(repo_root)),
    }
    runner._archive_input(
        repo_root, evidence_acceptance_path, repo_root / EXEC_REL / "interactive-evidence.json",
        runner_meta, outputs,
    )
    print("interactive input archived", flush=True)
    return {
        **outputs,
        "evidence_result_count": core.load_json(evidence_acceptance_path)["result_count"],
        "completeness_status": core.load_json(completeness_path)["overall_status"],
    }

if __name__ == "__main__":
    raise SystemExit(main())
