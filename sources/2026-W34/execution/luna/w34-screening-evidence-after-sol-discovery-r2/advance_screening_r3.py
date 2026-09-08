#!/usr/bin/env python3
"""Advance DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED for fresh 439 screening."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "2026-W34"
STATE_REL = "sources/2026-W34/production-state.json"
ACCEPTANCE_REL = "sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json"
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
VALIDATION_REL = f"{EXEC_REL}/validation/screening-stage-validation-r3.json"
REVIEWS_REL = f"{EXEC_REL}/validation/screening-stage-reviews-r3.json"
RECORDED_AT = "2026-09-08T23:40:00Z"

def main():
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    acc_path = root / ACCEPTANCE_REL
    val_path = root / VALIDATION_REL
    rev_path = root / REVIEWS_REL
    for p in (val_path, rev_path):
        if p.exists():
            raise ValueError(f"refusing overwrite {p}")
    state = core.load_json(state_path)
    assert state["lifecycle_state"] == "DISCOVERY_COLLECTED", state["lifecycle_state"]
    stage_validation.validate_stage(root, cfg, state_path, {"screening-acceptance": acc_path}, val_path, core.parse_instant(RECORDED_AT))
    print(f"validation PASS {val_path}")
    rev_path.parent.mkdir(parents=True, exist_ok=True)
    core.write_json(rev_path, {"reviews": [{"check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC", "executor": "Survey Production Core v2 survey_stage_validation_v2.py", "evidence": "Fresh 439-record Screening (110 prior +329 new) validated against 369-root Discovery; all roots accounted, 409 non-DROP. Machine validation only; Sol Evidence review still required.", "result_path": VALIDATION_REL}]})
    # Build checkpoint: need canonical checkpoint path for DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED
    # canonical_checkpoint_path resolves from state lifecycle
    checkpoint_path = agent.canonical_checkpoint_path(root, cfg, state)
    print(f"canonical checkpoint {checkpoint_path.relative_to(root)}")
    if checkpoint_path.exists():
        raise ValueError(f"checkpoint already exists {checkpoint_path}")
    generated = agent.build_stage_checkpoint(root, cfg, state_path, {"screening-acceptance": acc_path}, rev_path, "Fresh W34 Screening 439 (Muse Spark 1.3 EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION) validated; advance to Evidence.", core.parse_instant(RECORDED_AT))
    print(f"built {generated}")
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    print(json.dumps({"lifecycle": updated["lifecycle_state"], "next": updated["next_action"], "screening": updated["machine_checkpoints"]["screening"]}, indent=2))
    assert updated["lifecycle_state"] == "CANDIDATES_NORMALIZED"
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
