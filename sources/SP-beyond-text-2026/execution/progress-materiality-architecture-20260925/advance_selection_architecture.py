#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 EVIDENCE_REVIEWED -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-beyond-text-2026"
SRC = "sources/SP-beyond-text-2026"
EXEC = f"{SRC}/execution/progress-materiality-architecture-20260925"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / f"{SRC}/production-state.json"
    now = datetime.now(timezone.utc)
    outdir = root / EXEC / "validation"
    outdir.mkdir(parents=True, exist_ok=True)

    # ---- Selection ----
    state = core.load_json(state_path)
    assert state.get("lifecycle_state") == "EVIDENCE_REVIEWED", state.get("lifecycle_state")
    arts_sel = {
        "candidate-matrix": root / f"{SRC}/candidate-matrix-v2.json",
        "candidate-selection": root / f"{SRC}/candidate-selection-v2.json",
    }
    v1 = outdir / "selection-stage-validation.json"
    r1 = outdir / "selection-stage-reviews.json"
    for p in (v1, r1):
        assert not p.exists(), p
    stage_validation.validate_stage(root, cfg, state_path, arts_sel, v1, now)
    core.write_json(r1, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Selection stage-contract validation passed: 139 candidates, 134 SELECTED (57 PRIMARY / 77 SUPPORTING) / 5 HOLD / 0 REJECT / 0 INSPECT. Machine validation only; Human Architecture Review pending downstream.",
        "result_path": str(v1.relative_to(root))}]})
    gen1 = agent.build_stage_checkpoint(
        root, cfg, state_path, arts_sel, r1,
        "TS-002 Selection complete: anti-thinness selection over 139 candidates (14 packages; transition ledger mapped; closed products as capability context; X as reception context; 5 blocked HOLD). Proceed to Architecture; Human review pending.",
        now)
    upd = agent.advance_with_checkpoint(root, cfg, state_path, gen1)
    assert upd.get("lifecycle_state") == "SELECTION_COMPLETE", upd.get("lifecycle_state")

    # ---- Architecture ----
    arts_arch = {
        "issue-architecture": root / f"{SRC}/architecture-v2.json",
        "architecture-review-summary": root / f"{SRC}/architecture-review-summary-v2.json",
        "architecture-review-attention": root / f"{SRC}/architecture-review-attention-v2.json",
    }
    v2 = outdir / "architecture-stage-validation.json"
    r2 = outdir / "architecture-stage-reviews.json"
    for p in (v2, r2):
        assert not p.exists(), p
    stage_validation.validate_stage(root, cfg, state_path, arts_arch, v2, now)
    core.write_json(r2, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Architecture stage-contract validation passed: 14-package mechanism-led architecture (PROPOSED, page plan 80/96) with READY_FOR_ARCHITECTURE_REVIEW summary. Machine validation only; Human Architecture decision pending.",
        "result_path": str(v2.relative_to(root))}]})
    gen2 = agent.build_stage_checkpoint(
        root, cfg, state_path, arts_arch, r2,
        "TS-002 Architecture established: 14 mechanism-led packages with page budget and coverage maps; READY_FOR_ARCHITECTURE_REVIEW. Stop for fresh Human Architecture Review; Draft not entered.",
        now)
    upd2 = agent.advance_with_checkpoint(root, cfg, state_path, gen2)
    assert upd2.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", upd2.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, upd2)
    assert upd2["human_gates"]["architecture_review"] == "pending", upd2["human_gates"]
    print(json.dumps({"lifecycle": upd2["lifecycle_state"], "next": upd2["next_action"],
                      "arch_gate": upd2["human_gates"]["architecture_review"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
