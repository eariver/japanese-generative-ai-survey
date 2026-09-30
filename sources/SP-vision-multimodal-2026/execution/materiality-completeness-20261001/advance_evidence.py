#!/usr/bin/env python3
"""Advance SP-vision-multimodal-2026 CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

Runs the real combined Evidence/Materiality/Completeness stage validator over
the exact r5 authority, builds the Core stage checkpoint binding all six
authorities, and advances Production State. Sol reviews Materiality/
Completeness outcome via the fresh Sol review. Selection/Architecture not entered.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
STATE_REL = f"{SRC}/production-state.json"
ARTIFACTS = {
    # REQUIRED_CURRENT for CANDIDATES_NORMALIZED: exactly these four.
    # discovery-acceptance + screening-acceptance arrive via prior checkpoint provenance.
    "evidence-acceptance": f"{SRC}/evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34/evidence-accepted.json",
    "edition-views-acceptance": f"{SRC}/evidence/v2/views/accepted/e3d0b3b33588b235e1c9be41259fb5bb5e07cbd1105ac0ff31a7bf7b34bfd0c5/edition-views-accepted.json",
    "materiality-ledger": f"{SRC}/materiality-ledger-v2.json",
    "profile-completeness": f"{SRC}/profile-completeness-v2.json",
}
EXEC_REL = f"{SRC}/execution/materiality-completeness-20261001"
VALIDATION_REL = f"{EXEC_REL}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    artifacts = {k: root / v for k, v in ARTIFACTS.items()}
    for key, path in artifacts.items():
        if not path.is_file():
            raise ValueError(f"stage artifact missing: {key} -> {path}")

    now = datetime.now(timezone.utc)
    validation_path = root / f"{VALIDATION_REL}/evidence-materiality-completeness-validation.json"
    reviews_path = root / f"{VALIDATION_REL}/evidence-materiality-completeness-reviews.json"
    for path in (validation_path, reviews_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")

    stage_validation.validate_stage(root, cfg, state_path, artifacts, validation_path, now)
    core.write_json(reviews_path, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT",
        "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Current Core combined Evidence/Materiality/Completeness stage-contract validation passed over r5 Evidence (111 Cards, 106/5), r5 Views (111, 101/10), Materiality Ledger (111 rows, 101/10) and Profile Completeness (LIMITED, 13 SATISFIED / 3 LIMITATION, 0 NEEDS_RESEARCH). Machine validation only; fresh Sol Materiality/Completeness Review is the required next supervisory boundary before Selection/Architecture.",
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path, artifacts, reviews_path,
        "TS-003 Evidence/Materiality/Completeness complete over r5 authority: 111 Cards + 111 Views validated; Materiality Ledger 101 MATERIAL / 10 CONTEXT with D04 cap, D07A/D07B separation, endpoint bounds and role discipline; Profile Completeness LIMITED (O06/O14/O15 bounded residuals G06/G01/G02; G03/G04/G05 carried). Proceed to Sol Materiality/Completeness Review; Selection and Architecture not entered.",
        now,
    )
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    if updated.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("advance did not reach EVIDENCE_REVIEWED")
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
