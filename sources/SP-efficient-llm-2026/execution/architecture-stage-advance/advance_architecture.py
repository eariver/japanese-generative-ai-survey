#!/usr/bin/env python3
"""Advance SP-efficient-llm-2026 SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED.

Edition-local operator script (NOT shared Core). Runs the real frozen
Architecture stage validator over the runner-produced Architecture package,
builds the Core stage checkpoint, and advances Production State. Mirrors
execution/compat/evidence-source-class-projection/advance_evidence.py.

Records NO Human approval: Architecture stays PROPOSED with null human_review;
Human Architecture Review remains pending.
"""
from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-efficient-llm-2026"
SRC_REL = "sources/SP-efficient-llm-2026"
STATE_REL = SRC_REL + "/production-state.json"
EXEC_REL = SRC_REL + "/execution/architecture-stage-advance"
VALIDATION_REL = f"{EXEC_REL}/validation"
RECORDED_AT = "2026-09-22T18:00:00Z"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("expected canonical State at SELECTION_COMPLETE")

    artifacts = {
        "issue-architecture": root / f"{SRC_REL}/architecture-v2.json",
        "architecture-review-summary": root / f"{SRC_REL}/architecture-review-summary-v2.json",
        "architecture-review-attention": root / f"{SRC_REL}/architecture-review-attention-v2.json",
    }
    for name, path in artifacts.items():
        if not path.is_file():
            raise ValueError(f"missing stage artifact {name}: {path}")
    architecture = core.load_json(artifacts["issue-architecture"])
    if architecture.get("status") != "PROPOSED":
        raise ValueError("expected PROPOSED Architecture (no Human authority)")
    review = architecture.get("human_review") or {}
    if any(review.get(k) is not None for k in ("reviewed_by", "reviewed_at", "review_reference")):
        raise ValueError("PROPOSED Architecture must not carry Human review metadata")
    summary = core.load_json(artifacts["architecture-review-summary"])
    if summary.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("Architecture Review Summary is not READY")
    print(json.dumps({
        "package_count": len(architecture["packages"]),
        "page_plan": architecture["page_plan"],
        "readiness": summary["readiness"]["status"],
    }, ensure_ascii=False, indent=2))

    validation_path = root / f"{VALIDATION_REL}/architecture-stage-validation-r1.json"
    reviews_path = root / f"{VALIDATION_REL}/architecture-stage-reviews-r1.json"
    for path in (validation_path, reviews_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")
    validation_path.parent.mkdir(parents=True, exist_ok=True)

    stage_validation.validate_stage(
        root, cfg, state_path, artifacts, validation_path, core.parse_instant(RECORDED_AT))
    core.write_json(reviews_path, {"reviews": [{
        "check_id": "CORE_STAGE_CONTRACT",
        "kind": "DETERMINISTIC",
        "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
        "evidence": ("Current Core Architecture stage-contract validation passed: 9-package PROPOSED Architecture "
                     "(target 76 / max 96 pages) with READY_FOR_ARCHITECTURE_REVIEW summary and bounded attention surface; "
                     "human_review null, no Human approval recorded. Machine validation only; Sol Architecture review "
                     "and the Human-facing dossier remain due before any Gate presentation."),
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path, artifacts, reviews_path,
        ("SP-efficient-llm-2026 Architecture established as PROPOSED 9-package plan (P1 bottleneck through P9 methodology; "
         "D128 abstract-scope visible in P8; Jev specialization case in P7; X/D164 bounded) with READY review summary. "
         "Human Architecture Review pending; drafting not started."),
        core.parse_instant(RECORDED_AT),
    )
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    if updated.get("lifecycle_state") != "ARCHITECTURE_ESTABLISHED":
        raise ValueError("advance did not reach ARCHITECTURE_ESTABLISHED")
    if updated.get("human_gates", {}).get("architecture_review") != "pending":
        raise ValueError("Architecture Review must remain pending")
    if (updated.get("human_gate_provenance", {}) or {}).get("architecture_review") is not None:
        raise ValueError("no Architecture approval provenance may exist")
    errors = agent.validate_agent_state(root, cfg, updated)
    if errors:
        raise ValueError("final State not resumable: " + "; ".join(errors))
    print(json.dumps({
        "lifecycle_state": updated["lifecycle_state"],
        "next_action": updated["next_action"],
        "human_gates": updated["human_gates"],
        "checkpoint": str(generated.relative_to(root)),
        "checkpoint_sha256": core.sha256_file(generated),
        "state_sha256": core.sha256_file(state_path),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
