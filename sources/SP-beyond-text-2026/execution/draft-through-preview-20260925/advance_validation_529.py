#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 DRAFT_COMPLETE -> VALIDATED_DRAFT."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

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
    assert state.get("lifecycle_state") == "DRAFT_COMPLETE", state.get("lifecycle_state")

    arts = {
        "reader-manuscript": root / f"{SRC}/publication/v2/reader-manuscript-v2.json",
        "validated-source": root / "surveys/special/beyond-text-2026/main.tex",
        "publication-pdf": root / "surveys/special/beyond-text-2026/main.pdf",
        "quality-regression-bundle": root / f"{SRC}/publication/v2/quality-regression-bundle-v2.json",
        "semantic-review": root / f"{SRC}/publication/v2/semantic-editorial-review-v2.json",
        "visual-review": root / f"{SRC}/publication/v2/visual-review-v2.json",
        "reader-surface-gate": root / f"{SRC}/publication/v2/reader-surface-gate-v2.json",
    }
    v1 = outdir / "reader-publication-stage-validation-529.json"
    r1 = outdir / "reader-publication-stage-reviews-529.json"
    for p in (v1, r1):
        assert not p.exists(), p
    with agent_tool.current_stage_basis_override():
        stage_validation.validate_stage(root, cfg, state_path, arts, v1, now)
    core.write_json(r1, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Reader-publication stage-contract validation passed: 68-page validated source/PDF with quality bundle, semantic/visual reviews, and reader-surface gate. Machine validation only; Human Publication Preview decision pending downstream.",
        "result_path": str(v1.relative_to(root))}]})
    with agent_tool.current_stage_basis_override():
        gen1 = agent.build_stage_checkpoint(
            root, cfg, state_path, arts, r1,
            "TS-002 Validated draft: 68-page reader-facing source/PDF validated (deterministic QA + semantic/editorial + visual QA of exact rendered PDF). Proceed to Publication Candidate; Human Publication Preview pending.",
            now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen1)
    assert upd.get("lifecycle_state") == "VALIDATED_DRAFT", upd.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, upd)
    print(json.dumps({"lifecycle": upd["lifecycle_state"], "next": upd["next_action"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
