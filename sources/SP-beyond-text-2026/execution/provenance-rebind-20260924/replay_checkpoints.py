#!/usr/bin/env python3
"""Rebind Discovery + Screening checkpoints after provenance rebind (replay).

Mirrors the CURRENT_CORE_DISCOVERY_STAGE_BUILDER_REPLAY precedent: validated
in-memory fixtures advance one forward step through the real Core validator +
checkpoint builder. Two chained replays (prior bytes snapshotted, restored on
failure; shared Core untouched; no Screening semantics change):

1. fixture ISSUE_INITIALIZED -> DISCOVERY_COLLECTED (fresh 139-record acceptance)
2. fixture DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED (same 139 decisions)
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
DISC_ACC_REL = "sources/SP-beyond-text-2026/discovery/discovery-accepted-v2.json"
CP_INIT_REL = "sources/SP-beyond-text-2026/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json"
CP_DISC_REL = "sources/SP-beyond-text-2026/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    cp_init = root / CP_INIT_REL
    cp_disc = root / CP_DISC_REL
    state_before = state_path.read_bytes()
    init_before = cp_init.read_bytes()
    disc_before = cp_disc.read_bytes()
    state = core.load_json(state_path)
    assert state.get("issue_id") == ISSUE_ID and state.get("lifecycle_state") == "CANDIDATES_NORMALIZED", state.get("lifecycle_state")
    now = datetime.now(timezone.utc)
    outdir = root / EXEC_REL / "validation"
    outdir.mkdir(parents=True, exist_ok=True)

    succeeded = False
    try:
        # ---- Replay 1: discovery ----
        fix = copy.deepcopy(state)
        fix["lifecycle_state"] = "ISSUE_INITIALIZED"
        fix["machine_checkpoints"] = {n: "pending" for n in core.CHECKPOINTS}
        fix["checkpoint_provenance"] = {n: None for n in core.CHECKPOINTS}
        fix["history"] = fix["history"][:1]
        fix = core.refresh_state_control(fix, cfg)
        errs = agent.validate_agent_state(root, cfg, fix)
        assert not errs, errs
        core.write_json(state_path, fix)
        v1 = outdir / "discovery-stage-validation-rebind.json"
        r1 = outdir / "discovery-stage-reviews-rebind.json"
        stage_validation.validate_stage(root, cfg, state_path,
                                        {"discovery-acceptance": root / DISC_ACC_REL}, v1, now)
        core.write_json(r1, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": "Discovery stage-contract validation passed against the rebound 139-record canonical acceptance (24 locator/title/published_at provenance rebinds; counts and obligations unchanged). Machine validation only.",
            "result_path": str(v1.relative_to(root))}]})
        cp_init.unlink()
        gen1 = agent.build_stage_checkpoint(
            root, cfg, state_path, {"discovery-acceptance": root / DISC_ACC_REL}, r1,
            "Provenance rebind adopted: 24 verified locator/title/published_at corrections (21 arXiv + D062 v2 + D089 IEEE + D024 CompVis); canonical Discovery still 139 records; Screening not rerun.", now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen1)
        assert upd.get("lifecycle_state") == "DISCOVERY_COLLECTED", upd.get("lifecycle_state")

        # ---- Replay 2: screening (same decisions, rebound basis) ----
        from scripts import run_screening_v2_interactive as rscreen
        dec = root / "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/interactive-decisions.json"
        rep = rscreen.run(root, state_path, dec)
        import re as _re
        acc_path = root / rep["acceptance_path"]
        v2 = outdir / "screening-stage-validation-rebind.json"
        r2 = outdir / "screening-stage-reviews-rebind.json"
        stage_validation.validate_stage(root, cfg, state_path,
                                        {"screening-acceptance": acc_path}, v2, now)
        core.write_json(r2, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": "Screening stage-contract validation passed against the replayed 139-decision acceptance (semantics unchanged: 134/3/2/0) over rebound Discovery basis. Machine validation only.",
            "result_path": str(v2.relative_to(root))}]})
        if cp_disc.is_symlink() or not cp_disc.is_file():
            raise ValueError("screening checkpoint path missing or unsafe")
        cp_disc.unlink()
        gen2 = agent.build_stage_checkpoint(
            root, cfg, state_path, {"screening-acceptance": acc_path}, r2,
            "Screening replayed over rebound Discovery (same 139 decisions 134/3/2/0); rebased to CANDIDATES_NORMALIZED for Evidence rebind. Evidence not yet rebuilt.", now)
        upd2 = agent.advance_with_checkpoint(root, cfg, state_path, gen2)
        assert upd2.get("lifecycle_state") == "CANDIDATES_NORMALIZED", upd2.get("lifecycle_state")
        errs = agent.validate_agent_state(root, cfg, upd2)
        assert not errs, errs
        core.write_json(outdir / "checkpoint-rebind-record.json", {
            "schema_version": "1.0", "issue_id": ISSUE_ID,
            "screening_acceptance": str(acc_path.relative_to(root)),
            "screening_counts": rep["decision_counts"],
            "state": STATE_REL, "lifecycle_state": upd2["lifecycle_state"],
            "next_action": upd2["next_action"]})
        succeeded = True
        print(json.dumps({"lifecycle": upd2["lifecycle_state"], "next": upd2["next_action"],
                          "screening": str(acc_path.relative_to(root)),
                          "counts": rep["decision_counts"]}, indent=2))
        return 0
    finally:
        if not succeeded:
            state_path.write_bytes(state_before)
            cp_init.write_bytes(init_before)
            cp_disc.write_bytes(disc_before)


if __name__ == "__main__":
    raise SystemExit(main())
