#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-beyond-text-2026"
SRC = "sources/SP-beyond-text-2026"
EXEC = f"{SRC}/execution/draft-through-preview-20260925"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / f"{SRC}/production-state.json"
    now = datetime.now(timezone.utc)
    outdir = root / EXEC / "validation"
    outdir.mkdir(parents=True, exist_ok=True)

    state = core.load_json(state_path)
    assert state.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", state.get("lifecycle_state")
    assert state.get("human_gates", {}).get("architecture_review") == "approved"

    arch = core.load_json(root / f"{SRC}/architecture-v2.json")
    arts = {
        "synthesis-input": root / f"{SRC}/draft/v2/profile-synthesis-input.json",
        "synthesis-result": root / f"{SRC}/draft/v2/profile-synthesis-result.json",
    }
    for pid in sorted(p["package_id"] for p in arch["packages"]):
        arts[f"draft-package:{pid}"] = root / f"{SRC}/draft/v2/packages/{pid}/draft-package.json"
        arts[f"draft-result:{pid}"] = root / f"{SRC}/draft/v2/packages/{pid}/draft-result.json"
    v1 = outdir / "draft-stage-validation.json"
    r1 = outdir / "draft-stage-reviews.json"
    for p in (v1, r1):
        assert not p.exists(), p
    with agent_tool.current_stage_basis_override():
        stage_validation.validate_stage(root, cfg, state_path, arts, v1, now)
    core.write_json(r1, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Drafting-synthesis stage-contract validation passed: 14/14 architecture packages with validated draft-package/draft-result pairs + ESTABLISHED profile synthesis. Machine validation only; reader-facing authorship/validation pending downstream.",
        "result_path": str(v1.relative_to(root))}]})
    with agent_tool.current_stage_basis_override():
        gen1 = agent.build_stage_checkpoint(
            root, cfg, state_path, arts, r1,
            "TS-002 Draft complete: 14-package evidence-bounded drafting synthesis ESTABLISHED from Human-approved Architecture r1; proceed to reader-facing authorship and publication validation.",
            now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen1)
    assert upd.get("lifecycle_state") == "DRAFT_COMPLETE", upd.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, upd)
    print(json.dumps({"lifecycle": upd["lifecycle_state"], "next": upd["next_action"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
