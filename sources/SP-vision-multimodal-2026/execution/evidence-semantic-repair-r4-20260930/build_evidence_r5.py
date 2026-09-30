#!/usr/bin/env python3
"""Build TS-003 r5 Evidence: r3 baseline with 4-wording-repaired cards.

- 107 unaffected cards: byte-for-byte copies of r3 accepted files.
- D074/D075/D077/D111: r4 semantic wording with r3 provenance timestamps
  (temporal.observed_at + sources[0].accessed_at) restored.
- Views: 107 r3 byte-copies + 4 rebuilt views bound to new card hashes,
  all other view fields preserved from r3.
- Canonical append-only acceptors + validators only. No ledger/completeness,
  no state advance. Same canonical task package.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
R3_RES = f"{SRC}/evidence/v2/accepted/c6763f1c5d3f69cc96c78bab5eccde83c9956fb8c20a71e58b1b57fb3d33c8d7/results"
R4_RES = f"{SRC}/evidence/v2/accepted/94877f9ffac552577c7eeb080add8b05d70f5e21f9e6266a6e7b0211b6991b65/results"
R3_VIEWS = f"{SRC}/evidence/v2/views/accepted/fc8556a310b8bf8d33809e2e40bb08f4867690a38eb4d8b561ab7d999ea499c7/views"
R4_INPUT = (f"{SRC}/execution/evidence-semantic-repair-r3-20260930/"
            "evidence-interactive-input-r4.json")
PKG = (f"{SRC}/execution/screening-evidence-20260930/evidence-package/package.json")
STATE_REL = f"{SRC}/production-state.json"

TARGETS = ["VM-D074", "VM-D075", "VM-D077", "VM-D111"]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("r5 build requires CANDIDATES_NORMALIZED Production State")
    errors = agent.validate_agent_state(root, cfg, state)
    if errors:
        raise ValueError("Production State invalid before r5 build: " + "; ".join(errors))

    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    implementation_sha = core.repository_commit_sha(root)
    package_path = root / PKG
    package = core.load_json(package_path)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    if set(task_meta) != {f"VM-D{i:03d}" for i in range(1, 112)}:
        raise ValueError("task package does not cover 111/111")

    # input records for the 4 rebuilt views (r4 semantics)
    doc = core.load_json(root / R4_INPUT)
    by_id = {r["discovery_id"]: r for r in doc["records"]}

    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        results_dir = temp_root / "evidence-results"
        results_dir.mkdir()
        staged = {}
        for did in sorted(task_meta):
            meta = task_meta[did]
            fname = Path(meta["path"]).name
            if did in TARGETS:
                base = core.load_json(root / R4_RES / fname)  # r4 wording
                ref = core.load_json(root / R3_RES / fname)   # r3 provenance
                base["temporal"]["observed_at"] = ref["temporal"]["observed_at"]
                base["sources"][0]["accessed_at"] = ref["sources"][0]["accessed_at"]
                task = core.load_json(package_path.parent / meta["path"])
                errs = evidence.validate_evidence_card(
                    base, task, meta["sha256"], package, repo_root=root)
                if errs:
                    raise ValueError(f"r5 Card {did} invalid: {'; '.join(errs)}")
                core.write_json(results_dir / fname, base)
                staged[did] = base
            else:
                shutil.copy2(root / R3_RES / fname, results_dir / fname)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, evidence_root, implementation_sha)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, implementation_sha)

        by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
        views_dir = temp_root / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = by_task[task_id]
            if did in TARGETS:
                view = inter._build_view(profile, task_id, entry["sha256"], by_id[did])
                errs = evidence.validate_edition_view(
                    view, profile, entry["sha256"], entry["status"])
                if errs:
                    raise ValueError(f"r5 View {did} invalid: {'; '.join(errs)}")
                core.write_json(views_dir / evidence.view_filename(task_id), view)
            else:
                # byte-for-byte r3 inheritance
                src_view = root / R3_VIEWS / evidence.view_filename(task_id)
                if not src_view.is_file():
                    raise ValueError(f"r3 view missing for {did}")
                shutil.copy2(src_view, views_dir / evidence.view_filename(task_id))

        views_root = source_root / "evidence/v2/views/accepted"
        with agent_tool.current_stage_basis_override():
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, evidence_acceptance_path, views_dir, views_root,
                implementation_sha)
            evidence.validate_edition_views_acceptance(
                root, profile_path, evidence_acceptance_path, views_acceptance_path,
                implementation_sha)

    print(json.dumps({
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance_path),
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "views_acceptance_sha256": core.sha256_file(views_acceptance_path),
        "cards": 111,
        "materiality_ledger": "NOT_BUILT (boundary)",
        "profile_completeness": "NOT_BUILT (pending Sol review)",
        "lifecycle": "CANDIDATES_NORMALIZED (unchanged)",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
