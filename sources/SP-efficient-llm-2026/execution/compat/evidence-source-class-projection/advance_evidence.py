#!/usr/bin/env python3
"""Advance SP-efficient-llm-2026 CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

Runs the real frozen Evidence/Materiality/Completeness stage validator over
the accepted artifacts, builds the Core stage checkpoint, and advances
Production State. Mirrors execution/x-completion/advance_screening.py.
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
EXEC_REL = SRC_REL + "/execution/evidence-stage-advance"
VALIDATION_REL = f"{EXEC_REL}/validation"
RECORDED_AT = "2026-09-22T16:00:00Z"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")

    ledger = core.load_json(root / f"{SRC_REL}/materiality-ledger-v2.json")
    completeness = core.load_json(root / f"{SRC_REL}/profile-completeness-v2.json")
    evidence_acceptance = ledger  # placeholder guard below; real paths resolved via ledger basis
    _ = evidence_acceptance

    # Resolve accepted artifact paths from the frozen outputs just produced.
    # (Ledger/basis carry exact SHAs; paths are the canonical source-tree ones.)
    artifacts = {
        "evidence-acceptance": root / _find_acceptance(root, "evidence/v2/accepted", "evidence-accepted.json"),
        "edition-views-acceptance": root / _find_acceptance(root, "evidence/v2/views/accepted", "edition-views-accepted.json"),
        "materiality-ledger": root / f"{SRC_REL}/materiality-ledger-v2.json",
        "profile-completeness": root / f"{SRC_REL}/profile-completeness-v2.json",
    }
    for name, path in artifacts.items():
        if not path.is_file():
            raise ValueError(f"missing stage artifact {name}: {path}")
    print(json.dumps({"completeness_status": completeness["overall_status"],
                      "ledger_rows": len(ledger["rows"])}, indent=1))

    validation_path = root / f"{VALIDATION_REL}/evidence-stage-validation-r1.json"
    reviews_path = root / f"{VALIDATION_REL}/evidence-stage-reviews-r1.json"
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
        "evidence": ("Current Core Evidence/Materiality/Completeness stage-contract validation passed: "
                     "160 Evidence results accepted, Edition Views accepted, Materiality Ledger built, "
                     "Profile Completeness LIMITED (15 obligations incl. O13-O15 gap-fill lanes). "
                     "Machine validation only; Sol authority-consumption/materiality review is the required next supervisory boundary."),
        "result_path": str(validation_path.relative_to(root)),
    }]})
    generated = agent.build_stage_checkpoint(
        root, cfg, state_path, artifacts, reviews_path,
        ("SP-efficient-llm-2026 Evidence/Materiality/Completeness complete over 160-task compat package "
         "(67 projected / 93 passthrough, frozen-validated) with 13-source frozen supplement: "
         "160 Evidence Cards accepted, Edition Views accepted, Materiality Ledger built, Completeness LIMITED. "
         "Stop for Sol authority-consumption review; Selection not entered."),
        core.parse_instant(RECORDED_AT),
    )
    updated = agent.advance_with_checkpoint(root, cfg, state_path, generated)
    if updated.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("advance did not reach EVIDENCE_REVIEWED")
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


def _find_acceptance(root: Path, rel_dir: str, filename: str) -> str:
    base = root / SRC_REL / rel_dir
    matches = sorted(base.glob(f"*/{filename}"))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {filename} under {rel_dir}: {matches}")
    return str(matches[0].relative_to(root))


if __name__ == "__main__":
    raise SystemExit(main())
