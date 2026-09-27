#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED.

Runs the real Screening stage validator, builds the Core stage checkpoint
binding the accepted Screening result set, and advances Production State.
Screening decisions are operator judgments under the Core screening contract
(134 KEEP / 3 MAYBE / 2 INSPECT / 0 DROP over 139 records); Sol reviews the
Evidence outcome via the fresh Evidence Semantic Review. Evidence is not
entered here.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
ACCEPTANCE_REL = "sources/SP-beyond-text-2026/screening/v2/accepted/2a3e28dacadf9496db9109ff5dde58663767f280766c56b08c7bc03e72689966/screening-accepted.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924"
VALIDATION_REL = f"{EXEC_REL}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    acceptance_path = root / ACCEPTANCE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    if not acceptance_path.is_file():
        raise ValueError("Screening acceptance missing")

    now = datetime.now(timezone.utc)
    validation_path = root / f"{VALIDATION_REL}/screening-stage-validation.json"
    reviews_path = root / f"{VALIDATION_REL}/screening-stage-reviews.json"
    for path in (validation_path, reviews_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")

    stage_validation.validate_stage(
        root, cfg, state_path,
        {"screening-acceptance": acceptance_path},
        validation_path, now,
    )
    core.write_json(reviews_path, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT",
        "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Current Core Screening stage-contract validation passed against the 139-record Screening acceptance (134 KEEP / 3 MAYBE / 2 INSPECT / 0 DROP; non-DROP 139) over canonical Discovery 139 (128 BASE + 10 GAP_FILL + 1 X-bound BT-D139). Machine validation only; fresh Sol Evidence Semantic Review is the required next supervisory boundary before Materiality/Completeness/Selection/Architecture.",
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path,
        {"screening-acceptance": acceptance_path},
        reviews_path,
        "TS-002 Screening complete over 139-record canonical Discovery (128 BASE + 10 GAP_FILL + 1 X-bound BT-D139): 134 KEEP / 3 MAYBE / 2 INSPECT / 0 DROP; non-DROP 139. Primary authorities, X reception, LOW_SIGNAL lanes, modality balance, and TS-002/TS-003 boundary preserved; closed products retained as capability cases. Proceed to Evidence, then stop for Sol Evidence Semantic Review.",
        now,
    )
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    if updated.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("advance did not reach CANDIDATES_NORMALIZED")
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
