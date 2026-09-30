#!/usr/bin/env python3
"""Bounded TS-003 Evidence build over the canonical package: evidence + views only.

Uses the canonical Core v2 evidence machinery against the canonical
prepare_evidence_package output (no compat projection needed: all Discovery
source_types are Evidence-map admissible by intake design). Builds cards/views
with the canonical builders/validators and accepts via the canonical
append-only acceptors. Intentionally stops before the Materiality Ledger,
Profile Completeness, and any Production State advance. Lifecycle remains
CANDIDATES_NORMALIZED with Screening passed, Evidence built and validated,
and Materiality/Completeness/Selection/Architecture pending, awaiting the
fresh Sol Evidence Semantic Review.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
STATE_REL = f"{SRC}/production-state.json"
import os as _os
INPUT_REL = _os.environ.get("TS003_EVIDENCE_INPUT",
    f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json")
PKG_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-package/package.json"
EXEC_REL = f"{SRC}/execution/screening-evidence-20260930"
VALIDATION_REL = f"{EXEC_REL}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    input_path = root / INPUT_REL
    package_path = root / PKG_REL
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
    package = core.load_json(package_path)
    if package.get("issue_id") != ISSUE_ID:
        raise ValueError("evidence package issue identity mismatch")
    with agent_tool.current_stage_basis_override():
        evidence.validate_evidence_package_basis(root, package_path, package, implementation_sha)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    expected_ids = set(task_meta)
    task_source_ids = {did: set(evidence.task_authority_sources(
        root, core.load_json(package_path.parent / meta["path"]), package))
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
            task = core.load_json(package_path.parent / meta["path"])
            card = inter._build_card(root, task, meta, package, by_id[did], runner)
            errs = evidence.validate_evidence_card(card, task, meta["sha256"], package, repo_root=root)
            if errs:
                raise ValueError(f"Evidence Card {did} invalid: {'; '.join(errs)}")
            core.write_json(results_dir / Path(meta["path"]).name, card)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, evidence_root, implementation_sha)
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

    from collections import Counter
    statuses = Counter(r["status"] for r in by_id.values())
    print(json.dumps({
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance_path),
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "views_acceptance_sha256": core.sha256_file(views_acceptance_path),
        "cards": len(by_id),
        "statuses": dict(statuses),
        "materiality_ledger": "NOT_BUILT (boundary)",
        "profile_completeness": "NOT_BUILT (pending Sol Evidence Semantic Review)",
        "lifecycle": "CANDIDATES_NORMALIZED (unchanged)",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
