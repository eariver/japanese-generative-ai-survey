#!/usr/bin/env python3
"""Run the W43 frozen Evidence/Materiality/Completeness chain over the derived r3
compat package (edition-local driver).

Mirrors W42 precedent (adapted for W43; no extra obligations — W43 Discovery
uses the 3 Profile-initial obligations). Every judgment step uses unmodified
frozen Core functions under the native frozen agent-first override. No Core
module modified; no validator weakened.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from scripts import run_evidence_v2_interactive as runner_mod
from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness
from scripts import survey_discovery_v2 as discovery
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening

ISSUE_ID = "2026-W43"
SOURCE_ROOT_REL = "sources/2026-W43"
STATE_REL = SOURCE_ROOT_REL + "/production-state.json"
COMPAT_REL = (SOURCE_ROOT_REL + "/execution/compat/"
              "evidence-source-class-projection/compat-package-r4/package.json")
INPUT_REL = (SOURCE_ROOT_REL + "/execution/compat/"
             "evidence-source-class-projection/interactive-evidence-r4.json")


def main() -> int:
    root = Path(".").resolve()
    state_path = root / STATE_REL
    compat_package_path = root / COMPAT_REL
    input_path = root / INPUT_REL
    for path in (state_path, compat_package_path, input_path):
        if not path.is_file():
            raise ValueError(f"missing driver input: {path}")

    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before Evidence: " + "; ".join(errors))
    if state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("Evidence requires CANDIDATES_NORMALIZED Production State")

    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    discovery_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(root, discovery_acceptance_path)
    root_discovery_path = core.repo_local_path(root, accepted_discovery["discovery_path"], "accepted Discovery JSONL")

    implementation_sha = core.repository_commit_sha(root)
    active_screening = screening.resolve_active_screening_acceptance(root, state_path, implementation_sha)
    screening_acceptance_path = Path(active_screening["path"])
    effective = screening.resolve_effective_discovery_basis(
        root, screening_acceptance_path.parent / "package.json",
        implementation_sha, accepted_root_path=root_discovery_path)
    discovery_path = Path(effective["path"])
    discovery_records = effective["records"]

    initial_obligations = {row["obligation_id"] for row in profile["research_scope"]["initial_obligations"]}
    extra = sorted({oid for row in discovery_records for oid in row.get("provenance", {}).get("obligation_ids", [])} - initial_obligations)
    if extra:
        raise ValueError(f"W43 unexpected non-initial obligations (no silent extension): {extra}")

    package = core.load_json(compat_package_path)
    with agent_tool.current_stage_basis_override():
        evidence.validate_evidence_package_basis(root, compat_package_path, package, implementation_sha)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    expected_ids = set(task_meta)
    with agent_tool.current_stage_basis_override():
        task_source_ids = {
            did: set(evidence.task_authority_sources(
                root, core.load_json(compat_package_path.parent / meta["path"]), package))
            for did, meta in task_meta.items()
        }
    interactive_doc = core.load_json(input_path)
    records_by_id, runner, completeness_input = runner_mod.validate_interactive_input(
        interactive_doc, profile, expected_ids, task_source_ids)

    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        results_dir = temp_root / "evidence-results"
        results_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task = core.load_json(compat_package_path.parent / meta["path"])
            card = runner_mod._build_card(root, task, meta, package, records_by_id[did], runner)
            errs = evidence.validate_evidence_card(card, task, meta["sha256"], package, repo_root=root)
            if errs:
                raise ValueError(f"Evidence Card {did} invalid: {'; '.join(errs)}")
            core.write_json(results_dir / Path(meta["path"]).name, card)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, compat_package_path, results_dir, evidence_root, implementation_sha)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, implementation_sha)

        evidence_by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
        views_dir = temp_root / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = evidence_by_task[task_id]
            view = runner_mod._build_view(profile, task_id, entry["sha256"], records_by_id[did])
            errs = evidence.validate_edition_view(view, profile, entry["sha256"], entry["status"])
            if errs:
                raise ValueError(f"Edition View {did} invalid: {'; '.join(errs)}")
            core.write_json(views_dir / evidence.view_filename(task_id), view)

        views_root = source_root / "evidence/v2/views/accepted"
        with agent_tool.current_stage_basis_override():
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, evidence_acceptance_path, views_dir, views_root, implementation_sha)
            evidence.validate_edition_views_acceptance(
                root, profile_path, evidence_acceptance_path, views_acceptance_path, implementation_sha)

        ledger_path = source_root / "materiality-ledger-v2.json"
        if ledger_path.exists():
            raise ValueError(f"refusing to overwrite Materiality Ledger: {ledger_path}")
        with agent_tool.current_stage_basis_override():
            ledger = evidence.build_materiality_ledger(
                root, profile_path, discovery_path, screening_acceptance_path,
                evidence_acceptance_path, views_acceptance_path, implementation_sha)
        evidence.write_materiality_ledger(ledger_path, ledger)

        completeness_path = source_root / "profile-completeness-v2.json"
        if completeness_path.exists():
            raise ValueError(f"refusing to overwrite Profile Completeness: {completeness_path}")
        result = runner_mod._build_completeness(
            root, profile, profile_path, discovery_records, ledger_path, ledger, completeness_input)
        schema_gate.validate_instance(
            result, root / "schemas/profile-completeness-result.schema.json", label="Profile Completeness")
        with agent_tool.current_stage_basis_override():
            errs = completeness.validate_profile_completeness(
                result, root, profile_path, discovery_path, screening_acceptance_path,
                evidence_acceptance_path, views_acceptance_path, ledger_path, implementation_sha)
            if errs:
                raise ValueError("Profile Completeness invalid: " + "; ".join(errs))
        core.write_json(completeness_path, result)

    print(json.dumps({
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "ledger": str(ledger_path.relative_to(root)),
        "completeness": str(completeness_path.relative_to(root)),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
