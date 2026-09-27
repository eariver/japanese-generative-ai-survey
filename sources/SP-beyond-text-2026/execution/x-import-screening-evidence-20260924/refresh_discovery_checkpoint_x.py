#!/usr/bin/env python3
"""Rebind the TS-002 canonical Discovery checkpoint after accepted X import.

The SP-beyond-text-2026 work branch is at DISCOVERY_COLLECTED (138 records),
while the accepted X reception pass adds BT-D139 (139 records) plus the
REQUIRED/COMPLETE X manifest. The current Core only advances one forward
lifecycle step. This bounded replay uses a Core-valid ISSUE_INITIALIZED
fixture, runs the real Discovery stage validator and stage-checkpoint
builder, and commits the resulting Core-generated State at
DISCOVERY_COLLECTED. Pre-existing State and checkpoint are restored on any
failure; their exact bytes are snapshotted in
execution/x-import-screening-evidence-20260924/prior-authority/.

Follows the TS-001/W34 post-Sol-gap-fill precedent
(CURRENT_CORE_DISCOVERY_STAGE_BUILDER_REPLAY) and the BT r2 repair replay.
Shared Core is not modified. Screening is not executed here.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
DISCOVERY_ACCEPTANCE_REL = "sources/SP-beyond-text-2026/discovery/discovery-accepted-v2.json"
CHECKPOINT_REL = "sources/SP-beyond-text-2026/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924"
VALIDATION_REL = f"{EXEC_REL}/validation"


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

    now = datetime.now(timezone.utc)
    validation_path = root / f"{VALIDATION_REL}/core-discovery-stage-validation-x.json"
    reviews_path = root / f"{VALIDATION_REL}/discovery-stage-reviews-x.json"
    refresh_record_path = root / f"{VALIDATION_REL}/discovery-checkpoint-refresh-x.json"
    for path in (validation_path, reviews_path, refresh_record_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite refresh output: {path}")
    validation_path.parent.mkdir(parents=True, exist_ok=True)

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
        core.write_json(state_path, replay)
        stage_validation.validate_stage(
            root,
            cfg,
            state_path,
            {"discovery-acceptance": acceptance_path},
            validation_path,
            now,
        )
        core.write_json(
            reviews_path,
            {
                "reviews": [
                    {
                        "check_id": "CORE_STAGE_CONTRACT",
                        "kind": "DETERMINISTIC",
                        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
                        "evidence": "Current Core Discovery stage-contract validation passed against the refreshed 139-record canonical Discovery acceptance (128 BASE + 10 GAP_FILL + 1 X-bound BT-D139) after Sol-authorized X import (beyond-text-reception-pass-01 r3, Sol r3 PASS_WITH_SOL_RECONCILIATION) plus BT-D137 CLIP preflight correction. Machine validation only; Sol Evidence Semantic Review is pending and no Human Gate decision is implied.",
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
            "Accepted X import adopted: x-source-intake REQUIRED/COMPLETE (beyond-text-reception-pass-01 r3 SUCCESS, 27/27/27 Sol-audited) + one X-bound Discovery record BT-D139 materialized and validated; canonical Discovery 139 records; BT-D137 CLIP preflight applied. Screening not yet executed.",
            now,
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
                "precedent": "TS-001 discovery-refresh-after-sol-pass (W34 method) + BT r2 repair replay",
                "reason": "The Sol-authorized X import added BT-D139 and flipped the X manifest to REQUIRED/COMPLETE while the State was already DISCOVERY_COLLECTED; Core's one-step lifecycle contract was honored using a validated ISSUE_INITIALIZED replay fixture.",
                "prior_state": {"path": STATE_REL, "sha256": core.sha256_bytes(state_before_bytes)},
                "prior_checkpoint": {"path": CHECKPOINT_REL, "sha256": core.sha256_bytes(checkpoint_before_bytes)},
                "stage_validation": {"path": str(validation_path.relative_to(root)), "sha256": core.sha256_file(validation_path)},
                "stage_reviews": {"path": str(reviews_path.relative_to(root)), "sha256": core.sha256_file(reviews_path)},
                "new_checkpoint": {"path": str(generated_checkpoint.relative_to(root)), "sha256": core.sha256_file(generated_checkpoint)},
                "new_state": {"path": STATE_REL, "sha256": core.sha256_file(state_path)},
                "from_state": "ISSUE_INITIALIZED",
                "to_state": "DISCOVERY_COLLECTED",
                "screening_executed": False,
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
