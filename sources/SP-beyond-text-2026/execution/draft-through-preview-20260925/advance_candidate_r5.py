#!/usr/bin/env python3
"""Advance SP-beyond-text-2026 VALIDATED_DRAFT -> RELEASE_CANDIDATE (Publication Preview gate)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
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
    assert state.get("lifecycle_state") == "VALIDATED_DRAFT", state.get("lifecycle_state")

    candidate_path = root / f"{SRC}/publication/v2/publication-candidate-v2.json"
    assert not candidate_path.exists(), candidate_path
    publication.build_candidate(
        root, "SP-beyond-text-2026", "LONGFORM_SPECIAL",
        root / f"{SRC}/publication/v2/reader-manuscript-v2.json",
        root / "surveys/special/beyond-text-2026/main.tex",
        root / "surveys/special/beyond-text-2026/main.pdf",
        75,
        root / f"{SRC}/publication/v2/quality-regression-bundle-v2.json",
        root / f"{SRC}/publication/v2/semantic-editorial-review-v2.json",
        root / f"{SRC}/publication/v2/visual-review-v2.json",
        candidate_path,
    )
    candidate = publication.validate_candidate(root, candidate_path, issue_id="SP-beyond-text-2026")
    assert candidate["status"] == "READY_FOR_PUBLICATION_PREVIEW", candidate["status"]
    print("candidate OK:", candidate["candidate_sha256"][:16], flush=True)

    arts = {"publication-candidate": candidate_path}
    v1 = outdir / "publication-candidate-stage-validation-r5.json"
    r1 = outdir / "publication-candidate-stage-reviews-r5.json"
    for p in (v1, r1):
        assert not p.exists(), p
    with agent_tool.current_stage_basis_override():
        stage_validation.validate_stage(root, cfg, state_path, arts, v1, now)
    core.write_json(r1, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": "Publication-candidate stage-contract validation passed: READY_FOR_PUBLICATION_PREVIEW candidate binding exact 75-page source/PDF with quality/semantic/visual reviews. Machine validation only; Human Publication Preview decision NOT generated.",
        "result_path": str(v1.relative_to(root))}]})
    with agent_tool.current_stage_basis_override():
        gen1 = agent.build_stage_checkpoint(
            root, cfg, state_path, arts, r1,
            "TS-002 Publication Preview ready: exact Candidate-bound 75-page PDF reviewable; stop for Human Publication Preview decision. Freeze/Release NOT entered.",
            now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen1)
    assert upd.get("lifecycle_state") == "RELEASE_CANDIDATE", upd.get("lifecycle_state")
    assert upd["human_gates"]["publication_preview"] == "pending", upd["human_gates"]
    assert not agent.validate_agent_state(root, cfg, upd)
    print(json.dumps({"lifecycle": upd["lifecycle_state"], "next": upd["next_action"],
                      "pub_gate": upd["human_gates"]["publication_preview"],
                      "terminal": upd["terminal_reason"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
