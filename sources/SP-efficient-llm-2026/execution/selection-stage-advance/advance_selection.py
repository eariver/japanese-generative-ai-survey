#!/usr/bin/env python3
"""Advance SP-efficient-llm-2026 EVIDENCE_REVIEWED -> SELECTION_COMPLETE.

Edition-local operator script (NOT shared Core). Runs the real frozen
Selection stage validator over the runner-produced Matrix/Selection, builds
the Core stage checkpoint, and advances Production State. Mirrors
execution/compat/evidence-source-class-projection/advance_evidence.py.
"""
from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-efficient-llm-2026"
SRC_REL = "sources/SP-efficient-llm-2026"
STATE_REL = SRC_REL + "/production-state.json"
EXEC_REL = SRC_REL + "/execution/selection-stage-advance"
VALIDATION_REL = f"{EXEC_REL}/validation"
RECORDED_AT = "2026-09-22T17:30:00Z"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("expected canonical State at EVIDENCE_REVIEWED")

    artifacts = {
        "candidate-matrix": root / f"{SRC_REL}/candidate-matrix-v2.json",
        "candidate-selection": root / f"{SRC_REL}/candidate-selection-v2.json",
    }
    for name, path in artifacts.items():
        if not path.is_file():
            raise ValueError(f"missing stage artifact {name}: {path}")
    selection = core.load_json(artifacts["candidate-selection"])
    print(json.dumps({"selection_summary": selection["summary"]}, indent=1))

    validation_path = root / f"{VALIDATION_REL}/selection-stage-validation-r1.json"
    reviews_path = root / f"{VALIDATION_REL}/selection-stage-reviews-r1.json"
    for path in (validation_path, reviews_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")
    validation_path.parent.mkdir(parents=True, exist_ok=True)

    stage_validation.validate_stage(
        root, cfg, state_path, artifacts, validation_path, core.parse_instant(RECORDED_AT))
    core.write_json(reviews_path, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT",
        "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": ("Current Core Selection stage-contract validation passed: 160 Matrix candidates assigned "
                     "(SELECTED 112 / HOLD 12 / REJECT 33 / INSPECT 3) under Sol-reviewed Selection semantics; "
                     "no fixed-count requirement triggered (selected_count 112 within [40, 120]). "
                     "Machine validation only; Sol Architecture review and the Human-facing dossier remain due."),
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path, artifacts, reviews_path,
        ("SP-efficient-llm-2026 Selection complete over 160-candidate Matrix under Sol Evidence PASS boundaries "
         "(D128 abstract-scope correction propagated; X/D164 bounded; Jev mandatory case; DROP continuity kept): "
         "112 SELECTED (53 PRIMARY / 59 SUPPORTING), 12 HOLD, 33 REJECT, 3 INSPECT. Architecture proposed next."),
        core.parse_instant(RECORDED_AT),
    )
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    if updated.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("advance did not reach SELECTION_COMPLETE")
    errors = agent.validate_agent_state(root, cfg, updated)
    if errors:
        raise ValueError("final State not resumable: " + "; ".join(errors))
    print(json.dumps({
        "lifecycle_state": updated["lifecycle_state"],
        "next_action": updated["next_action"],
        "checkpoint": str(generated.relative_to(root)),
        "checkpoint_sha256": core.sha256_file(generated),
        "state_sha256": core.sha256_file(state_path),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
