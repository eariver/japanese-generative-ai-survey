#!/usr/bin/env python3
"""Bounded TS-002 Evidence build over the compat package: evidence + views only.

Uses the canonical Core v2 evidence machinery against the reproducible
edition-local compat package (frozen prepare + source_type-only projection +
frozen basis validation; see compat/build_compat_evidence_package.py and the
defect record). Builds cards/views with the canonical builders/validators and
accepts via the canonical append-only acceptors. Intentionally stops before
the Materiality Ledger, Profile Completeness, and any Production State
advance. Lifecycle remains CANDIDATES_NORMALIZED with Screening passed,
Evidence built and validated, and Materiality/Completeness/Selection/
Architecture pending, awaiting the fresh Sol Evidence Semantic Review.
"""

from __future__ import annotations

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
INPUT_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/evidence-interactive-input.json"
COMPAT_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/compat-package/package.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924"
VALIDATION_REL = f"{EXEC_REL}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    input_path = root / INPUT_REL
    compat_path = root / COMPAT_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("bounded Evidence build requires CANDIDATES_NORMALIZED Production State")
    errors = agent.validate_agent_state(root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before Evidence: " + "; ".join(errors))

    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    implementation_sha = core.repository_commit_sha(root)
    package = core.load_json(compat_path)
    if package.get("issue_id") != ISSUE_ID:
        raise ValueError("compat package issue identity mismatch")
    with agent_tool.current_stage_basis_override():
        evidence.validate_evidence_package_basis(root, compat_path, package, implementation_sha)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    expected_ids = set(task_meta)
    task_source_ids = {did: set(evidence.task_authority_sources(
        root, core.load_json(compat_path.parent / meta["path"]), package))
        for did, meta in task_meta.items()}

    doc = core.load_json(input_path)
    runner = inter._validate_runner(doc.get("runner"))
    rows = doc.get("records")
    if not isinstance(rows, list):
        raise ValueError("evidence input records must be an array")
    by_id = {}
    for raw in rows:
        row = inter._validate_record(raw, profile)
        did = row["discovery_id"]
        if did in by_id:
            raise ValueError(f"duplicate evidence discovery_id: {did}")
        allowed = task_source_ids.get(did)
        if allowed is None:
            raise ValueError(f"{did}: no evidence task")
        b = row.get("source_bindings")
        if b is None:
            if len(allowed) > 1:
                raise ValueError(f"{did}: source_bindings required")
        elif not set(b).issubset(allowed):
            raise ValueError(f"{did}: unbound source_bindings")
        by_id[did] = row
    if set(by_id) != expected_ids:
        raise ValueError(f"evidence input must cover exact tasks: missing={sorted(expected_ids-set(by_id))} extra={sorted(set(by_id)-expected_ids)}")

    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        results_dir = temp_root / "evidence-results"
        results_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task = core.load_json(compat_path.parent / meta["path"])
            card = inter._build_card(root, task, meta, package, by_id[did], runner)
            errs = evidence.validate_evidence_card(card, task, meta["sha256"], package, repo_root=root)
            if errs:
                raise ValueError(f"Evidence Card {did} invalid: {'; '.join(errs)}")
            core.write_json(results_dir / Path(meta["path"]).name, card)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, compat_path, results_dir, evidence_root, implementation_sha)
            evidence.validate_evidence_acceptance(root, evidence_acceptance_path, implementation_sha)

        evidence_acceptance = core.load_json(evidence_acceptance_path)
        by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
        views_dir = temp_root / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = by_task[task_id]
            view = inter._build_view(profile, task_id, entry["sha256"], by_id[did])
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

    now = datetime.now(timezone.utc)
    active_screening = screening.resolve_active_screening_acceptance(root, state_path, implementation_sha)
    report = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "method": "CANONICAL_EVIDENCE_ONLY_OVER_COMPAT_THEN_STOP",
        "compat_package": str(compat_path.relative_to(root)),
        "compat_package_sha256": core.sha256_file(compat_path),
        "lifecycle_state": core.load_json(state_path)["lifecycle_state"],
        "screening_acceptance": str(Path(active_screening["artifact_path"]).relative_to(root)),
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "evidence_sha256": core.sha256_file(evidence_acceptance_path),
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "views_sha256": core.sha256_file(views_acceptance_path),
        "evidence_results": len(evidence_acceptance["results"]),
        "materiality_ledger": "NOT_BUILT (boundary; see defect record)",
        "profile_completeness": "NOT_BUILT (pending Sol Evidence Semantic Review)",
        "state_advanced": False,
        "built_at": now.isoformat(),
    }
    validation_path = root / f"{VALIDATION_REL}/evidence-only-build-report.json"
    if validation_path.exists():
        raise ValueError("refusing to overwrite evidence build report")
    core.write_json(validation_path, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
