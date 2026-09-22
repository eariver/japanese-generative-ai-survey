#!/usr/bin/env python3
"""Advance SP-efficient-llm-2026 DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED.

Runs the real Screening stage validator, builds the Core stage checkpoint
binding the accepted Screening result set, and advances Production State.
Screening decisions come from the archived interactive-decisions authority
(operator judgments under the Core screening contract; Sol reviews the
outcome via the screening review package).
"""

from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


ISSUE_ID = "SP-efficient-llm-2026"
STATE_REL = "sources/SP-efficient-llm-2026/production-state.json"
ACCEPTANCE_REL = "sources/SP-efficient-llm-2026/screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json"
EXEC_REL = "sources/SP-efficient-llm-2026/execution/x-completion"
VALIDATION_REL = f"{EXEC_REL}/validation"
RECORDED_AT = "2026-09-22T02:30:00Z"


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

    validation_path = root / f"{VALIDATION_REL}/screening-stage-validation-r1.json"
    reviews_path = root / f"{VALIDATION_REL}/screening-stage-reviews-r1.json"
    for path in (validation_path, reviews_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")

    stage_validation.validate_stage(
        root, cfg, state_path,
        {"screening-acceptance": acceptance_path},
        validation_path, core.parse_instant(RECORDED_AT),
    )
    core.write_json(reviews_path, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT",
        "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Current Core Screening stage-contract validation passed against the 165-record DIRECT-basis Screening acceptance (135 KEEP / 20 MAYBE / 5 INSPECT / 5 DROP). Machine validation only; Sol screening review is the required next supervisory boundary.",
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path,
        {"screening-acceptance": acceptance_path},
        reviews_path,
        "SP-efficient-llm-2026 Screening complete over 165-record canonical Discovery (DIRECT basis): 135 KEEP / 20 MAYBE / 5 INSPECT / 5 DROP; non-DROP 160. Normalized candidates proceed to Evidence. Stop for Sol screening review; Evidence not entered.",
        core.parse_instant(RECORDED_AT),
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
