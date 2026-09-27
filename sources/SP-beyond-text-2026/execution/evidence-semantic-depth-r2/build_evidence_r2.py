#!/usr/bin/env python3
"""Bounded TS-002 Evidence r2 build over the compat package: evidence + views only.

Layer A source-local factual input (evidence-interactive-input-r2.json) built
from consumed source bodies. Reuses the narrowly-scoped edition-local compat
package (source-type projection only; claims/metrics/limits/status untouched;
unknown vocabulary fail-closed; counts reported). Canonical builders,
validators, and append-only acceptors. The r1 accepted result-set is preserved
untouched (new result-set SHA yields new content-addressed directories).
Materiality Ledger, Profile Completeness, and State advance are NOT performed.
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
INPUT_REL = "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/evidence-interactive-input-r2.json"
COMPAT_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/compat-package/package.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2"
R1_EVIDENCE_SHA = "f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    input_path = root / INPUT_REL
    compat_path = root / COMPAT_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("r2 build requires CANDIDATES_NORMALIZED Production State")
    errors = agent.validate_agent_state(root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before Evidence r2: " + "; ".join(errors))

    # r1 preservation guard: record r1 bytes before, verify unchanged after.
    r1_dir = root / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{R1_EVIDENCE_SHA}"
    if not (r1_dir / "evidence-accepted.json").is_file():
        raise ValueError("r1 Evidence result-set missing; refusing to proceed")
    r1_before = core.sha256_file(r1_dir / "evidence-accepted.json")

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

    if core.sha256_file(r1_dir / "evidence-accepted.json") != r1_before:
        raise ValueError("r1 Evidence result-set mutated; refusing to report success")
    new_sha = core.sha256_file(evidence_acceptance_path)
    if new_sha == R1_EVIDENCE_SHA:
        raise ValueError("new result-set SHA identical to r1; repair produced no new bytes")

    now = datetime.now(timezone.utc)
    active_screening = screening.resolve_active_screening_acceptance(root, state_path, implementation_sha)
    report = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "method": "CANONICAL_EVIDENCE_R2_OVER_COMPAT_THEN_STOP",
        "compat_package": str(compat_path.relative_to(root)),
        "compat_package_sha256": core.sha256_file(compat_path),
        "r1_result_set_sha256": R1_EVIDENCE_SHA,
        "r1_preserved": True,
        "lifecycle_state": core.load_json(state_path)["lifecycle_state"],
        "screening_acceptance": str(Path(active_screening["artifact_path"]).relative_to(root)),
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "evidence_sha256": new_sha,
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "views_sha256": core.sha256_file(views_acceptance_path),
        "evidence_results": len(evidence_acceptance["results"]),
        "materiality_ledger": "NOT_BUILT (boundary)",
        "profile_completeness": "NOT_BUILT (pending Sol r2 review)",
        "state_advanced": False,
        "built_at": now.isoformat(),
    }
    outdir = root / EXEC_REL
    outdir.mkdir(parents=True, exist_ok=True)
    validation_path = outdir / "evidence-r2-build-report.json"
    if validation_path.exists():
        raise ValueError("refusing to overwrite evidence r2 build report")
    core.write_json(validation_path, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
