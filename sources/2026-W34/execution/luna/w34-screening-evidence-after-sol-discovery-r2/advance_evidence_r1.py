#!/usr/bin/env python3
"""Advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED for fresh 409 evidence.

Mirrors advance_screening_r3.py: exact Core stage validation, deterministic
review record, canonical checkpoint build, checkpoint advance. No Selection,
no Architecture.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(".").resolve()
sys.path.insert(0, str(REPO))
from scripts import survey_agent_control_v2 as agent  # noqa: E402
from scripts import survey_production_v2 as core  # noqa: E402
from scripts import survey_stage_validation_v2 as stage_validation  # noqa: E402

ISSUE_ID = "2026-W34"
STATE_REL = "sources/2026-W34/production-state.json"
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
SCREENING_REL = "sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json"
EVIDENCE_REL = (
    "sources/2026-W34/evidence/v2/accepted/"
    "647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/"
    "evidence-accepted.json"
)
VIEWS_REL = (
    "sources/2026-W34/evidence/v2/views/accepted/"
    "e2e644bcc97ac664949b272fca919923385af6192c65b5a3566e30382b0ca7ba/"
    "edition-views-accepted.json"
)
LEDGER_REL = "sources/2026-W34/materiality-ledger-v2.json"
COMPLETENESS_REL = "sources/2026-W34/profile-completeness-v2.json"
VALIDATION_REL = f"{EXEC_REL}/validation/evidence-stage-validation-r1.json"
REVIEWS_REL = f"{EXEC_REL}/validation/evidence-stage-reviews-r1.json"
RECORDED_AT = "2026-09-09T04:30:00Z"

def main():
    root = REPO
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    val_path = root / VALIDATION_REL
    rev_path = root / REVIEWS_REL
    for p in (val_path, rev_path):
        if p.exists():
            raise ValueError(f"refusing overwrite {p}")
    state = core.load_json(state_path)
    assert state["lifecycle_state"] == "CANDIDATES_NORMALIZED", state["lifecycle_state"]
    artifacts = {
        "evidence-acceptance": root / EVIDENCE_REL,
        "edition-views-acceptance": root / VIEWS_REL,
        "materiality-ledger": root / LEDGER_REL,
        "profile-completeness": root / COMPLETENESS_REL,
    }
    print("stage validation start", flush=True)
    stage_validation.validate_stage(root, cfg, state_path, artifacts, val_path, core.parse_instant(RECORDED_AT))
    print(f"validation PASS {val_path}", flush=True)
    rev_path.parent.mkdir(parents=True, exist_ok=True)
    core.write_json(rev_path, {"reviews": [{"check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC", "executor": "Survey Production Core v2 survey_stage_validation_v2.py", "evidence": "Fresh 409-task Evidence (401 CONSUMED / 2 CAPTURED_BUT_UNCONSUMED / 5 NOT_FOUND / 1 RETRIEVAL_FAILED) with 428-source Authority Supplement, 409 Edition Views, provisional Materiality ledger, and LIMITED Profile Completeness. Machine validation only; Sol Evidence review still required; shared-Core source-map repair pending Sol ruling.", "result_path": VALIDATION_REL}]})
    checkpoint_path = agent.canonical_checkpoint_path(root, cfg, state)
    print(f"canonical checkpoint {checkpoint_path.relative_to(root)}", flush=True)
    if checkpoint_path.exists():
        raise ValueError(f"checkpoint already exists {checkpoint_path}")
    generated = agent.build_stage_checkpoint(root, cfg, state_path, artifacts, rev_path, "Fresh W34 Evidence 409 (Muse Spark 1.3 EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION) validated; advance to Sol Evidence Review.", core.parse_instant(RECORDED_AT))
    print(f"built {generated}", flush=True)
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    print(json.dumps({"lifecycle": updated["lifecycle_state"], "next": updated["next_action"], "evidence": updated["machine_checkpoints"]["evidence"], "materiality": updated["machine_checkpoints"]["materiality"], "completeness": updated["machine_checkpoints"]["completeness"], "selection": updated["machine_checkpoints"]["selection"], "architecture": updated["machine_checkpoints"]["architecture"]}, indent=2))
    assert updated["lifecycle_state"] == "EVIDENCE_REVIEWED"
    assert updated["machine_checkpoints"]["selection"] == "pending"
    assert updated["machine_checkpoints"]["architecture"] == "pending"
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
