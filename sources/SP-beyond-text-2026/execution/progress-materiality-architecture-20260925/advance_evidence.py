#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED."""

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
    state = core.load_json(state_path)
    assert state.get("issue_id") == ISSUE_ID and state.get("lifecycle_state") == "CANDIDATES_NORMALIZED"
    now = datetime.now(timezone.utc)
    arts = {
        "evidence-acceptance": root / "sources/SP-beyond-text-2026/evidence/v2/accepted/29804dcfe7d9a1e1045c1b5c93d8d708e9890445afbb0f57b061ca555a178426/evidence-accepted.json",
        "edition-views-acceptance": root / "sources/SP-beyond-text-2026/evidence/v2/views/accepted/336f93d2e91aa52fe983271068be3227b0589fe9fa0e3c4f645aae0ae7823a73/edition-views-accepted.json",
        "materiality-ledger": root / f"{SRC}/materiality-ledger-v2.json",
        "profile-completeness": root / f"{SRC}/profile-completeness-v2.json",
    }
    for n, p in arts.items():
        assert p.is_file(), n
    v = root / f"{EXEC}/validation/evidence-stage-validation.json"
    r = root / f"{EXEC}/validation/evidence-stage-reviews.json"
    v.parent.mkdir(parents=True, exist_ok=True)
    for p in (v, r):
        assert not p.exists(), p
    stage_validation.validate_stage(root, cfg, state_path, arts, v, now)
    core.write_json(r, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Evidence/Materiality/Completeness stage-contract validation passed: rebound Evidence 139 (126 VERIFIED/8 PARTIAL/5 NEEDS_MORE), 139 Views, Materiality Ledger 139 rows (109/5/25), Completeness LIMITED (4 SATISFIED/8 LIMITATION). Machine validation only; Human Architecture Review pending downstream.",
        "result_path": str(v.relative_to(root))}]})
    gen = agent.build_stage_checkpoint(
        root, cfg, state_path, arts, r,
        "TS-002 Evidence/Materiality/Completeness complete over rebound Evidence (126/8/5): 139 Cards+Views accepted, Ledger 109/5/25, Completeness LIMITED with declared barriers. Proceed to Selection; Architecture Review pending.",
        now)
    upd = agent.advance_with_checkpoint(root, cfg, state_path, gen)
    assert upd.get("lifecycle_state") == "EVIDENCE_REVIEWED", upd.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, upd)
    print(json.dumps({"lifecycle": upd["lifecycle_state"], "next": upd["next_action"],
                      "checkpoint": str(gen.relative_to(root))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
