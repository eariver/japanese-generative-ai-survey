#!/usr/bin/env python3
"""Rebind the canonical Discovery checkpoint through current Core machinery.

The W34 branch is already at DISCOVERY_COLLECTED, while the current Core only
advances one forward lifecycle step.  This bounded replay uses an in-memory
Core-valid ISSUE_INITIALIZED fixture, runs the real Discovery stage validator
and stage-checkpoint builder, and commits the resulting Core-generated State at
DISCOVERY_COLLECTED.  The pre-existing State and checkpoint are restored on any
failure; their exact bytes are already snapshotted in this execution area.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


ISSUE_ID = "2026-W34"
STATE_REL = "sources/2026-W34/production-state.json"
DISCOVERY_ACCEPTANCE_REL = "sources/2026-W34/discovery/discovery-accepted-v2.json"
CHECKPOINT_REL = "sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json"
EXEC_REL = "sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1"
VALIDATION_REL = f"{EXEC_REL}/validation"
RECORDED_AT = "2026-09-08T01:30:00Z"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    checkpoint_path = root / CHECKPOINT_REL
    acceptance_path = root / DISCOVERY_ACCEPTANCE_REL
    state_before_bytes = state_path.read_bytes()
    checkpoint_before_bytes = checkpoint_path.read_bytes()
    state_before = core.load_json(state_path)
    if state_before.get("issue_id") != ISSUE_ID or state_before.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State to start at DISCOVERY_COLLECTED")
    if not acceptance_path.is_file():
        raise ValueError("fresh canonical Discovery acceptance is missing")

    validation_path = root / f"{VALIDATION_REL}/core-discovery-stage-validation-r2.json"
    reviews_path = root / f"{VALIDATION_REL}/discovery-stage-reviews-r2.json"
    refresh_record_path = root / f"{VALIDATION_REL}/discovery-checkpoint-refresh-r2.json"
    for path in (validation_path, reviews_path, refresh_record_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite refresh output: {path}")

    replay = copy.deepcopy(state_before)
    replay["lifecycle_state"] = "ISSUE_INITIALIZED"
    replay["machine_checkpoints"] = {name: "pending" for name in core.CHECKPOINTS}
    replay["checkpoint_provenance"] = {name: None for name in core.CHECKPOINTS}
    replay["history"] = replay["history"][:1]
    replay = core.refresh_state_control(replay, cfg)
    replay_errors = agent.validate_agent_state(root, cfg, replay)
    if replay_errors:
        raise ValueError("Core replay fixture is not valid: " + "; ".join(replay_errors))

    succeeded = False
    try:
        # The canonical State is temporarily the validated replay input so the
        # Core stage report binds the canonical State path. The final State is
        # written only by agent.advance_with_checkpoint().
        core.write_json(state_path, replay)
        stage_validation.validate_stage(
            root,
            cfg,
            state_path,
            {"discovery-acceptance": acceptance_path},
            validation_path,
            core.parse_instant(RECORDED_AT),
        )
        core.write_json(
            reviews_path,
            {
                "reviews": [
                    {
                        "check_id": "CORE_STAGE_CONTRACT",
                        "kind": "DETERMINISTIC",
                        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
                        "evidence": "Current Core Discovery stage-contract validation passed against the fresh canonical Discovery acceptance. This is a machine validation only; Sol Discovery Review r2 remains required.",
                        "result_path": str(validation_path.relative_to(root)),
                    }
                ]
            },
        )
        if checkpoint_path.is_symlink() or not checkpoint_path.is_file():
            raise ValueError("canonical prior Discovery checkpoint is missing or unsafe")
        checkpoint_path.unlink()
        generated_checkpoint = agent.build_stage_checkpoint(
            root,
            cfg,
            state_path,
            {"discovery-acceptance": acceptance_path},
            reviews_path,
            "Fresh W34 Discovery gap-fill is materialized and validated; stop for independent Sol Discovery Review r2.",
            core.parse_instant(RECORDED_AT),
        )
        updated = agent.advance_with_checkpoint(root, cfg, state_path, generated_checkpoint)
        if updated.get("lifecycle_state") != "DISCOVERY_COLLECTED":
            raise ValueError("Core Discovery replay did not return to DISCOVERY_COLLECTED")
        errors = agent.validate_agent_state(root, cfg, updated)
        if errors:
            raise ValueError("final Core-generated State is not resumable: " + "; ".join(errors))
        core.write_json(
            refresh_record_path,
            {
                "schema_version": "1.0",
                "issue_id": ISSUE_ID,
                "method": "CURRENT_CORE_DISCOVERY_STAGE_BUILDER_REPLAY",
                "reason": "The bounded Sol supervisory loop refreshed Discovery while the current State was already DISCOVERY_COLLECTED; Core's one-step lifecycle contract was honored using a validated ISSUE_INITIALIZED replay fixture.",
                "prior_state": {"path": STATE_REL, "sha256": core.sha256_bytes(state_before_bytes)},
                "prior_checkpoint": {"path": CHECKPOINT_REL, "sha256": core.sha256_bytes(checkpoint_before_bytes)},
                "stage_validation": {"path": str(validation_path.relative_to(root)), "sha256": core.sha256_file(validation_path)},
                "stage_reviews": {"path": str(reviews_path.relative_to(root)), "sha256": core.sha256_file(reviews_path)},
                "new_checkpoint": {"path": str(generated_checkpoint.relative_to(root)), "sha256": core.sha256_file(generated_checkpoint)},
                "new_state": {"path": STATE_REL, "sha256": core.sha256_file(state_path)},
                "from_state": "ISSUE_INITIALIZED",
                "to_state": "DISCOVERY_COLLECTED",
                "screening_executed": False,
                "sol_discovery_review_required": True,
            },
        )
        succeeded = True
        print(json.dumps({
            "state": STATE_REL,
            "lifecycle_state": updated["lifecycle_state"],
            "next_action": updated["next_action"],
            "terminal_reason": updated["terminal_reason"],
            "checkpoint": CHECKPOINT_REL,
            "checkpoint_sha256": core.sha256_file(checkpoint_path),
            "state_sha256": core.sha256_file(state_path),
            "validation": str(validation_path.relative_to(root)),
            "refresh_record": str(refresh_record_path.relative_to(root)),
        }, ensure_ascii=False, indent=2))
        return 0
    finally:
        if not succeeded:
            state_path.write_bytes(state_before_bytes)
            checkpoint_path.write_bytes(checkpoint_before_bytes)


if __name__ == "__main__":
    raise SystemExit(main())
