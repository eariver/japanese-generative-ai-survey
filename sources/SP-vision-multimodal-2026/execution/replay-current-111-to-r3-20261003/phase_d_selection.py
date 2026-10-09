#!/usr/bin/env python3
"""TS-003 replay Phase D: Selection (111) + advance to SELECTION_COMPLETE.

- Candidate matrix re-derived at the canonical path (deleted by re-entry) via
  canonical derive + validate (111 rows; D084 title V1 via carried Evidence).
- Selection re-emitted at the canonical path: 111 carried byte-identical
  assignments + refreshed basis. No Agentic candidate selected.
- SSv2/entity check on matrix + selection.
- Advance EVIDENCE_REVIEWED -> SELECTION_COMPLETE (edition pattern).
- Frozen Core only + documented post-gate adaptation. Sol review owed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2_base as archbase
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/replay-current-111-to-r3-20261003"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"

R8SEL = f"{SRC}/candidate-selection-v2-r8.json"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("expected canonical State at EVIDENCE_REVIEWED")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        view_acc = max((root / SRC / "evidence/v2/views/accepted").glob("*/edition-views-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        for p in (ledger_path, comp_path):
            assert p.is_file(), p

        matrix = archbase.derive_candidate_matrix(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, impl)
        assert archbase.validate_candidate_matrix(
            matrix, root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            view_acc, ledger_path, comp_path, impl) == []
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        assert not matrix_path.exists(), "canonical matrix should have been invalidated"
        core.write_json(matrix_path, matrix)
        assert matrix["summary"]["candidate_count"] == 111
        d084 = [r for r in matrix["rows"] if "VM-D084" in r["discovery_ids"]]
        assert len(d084) == 1 and d084[0]["title"] == "Something-Something V1", d084
        assert "Something-Something V2" not in json.dumps(matrix, ensure_ascii=False)
        print("matrix rows:", matrix["summary"]["candidate_count"], "| D084:", d084[0]["title"])

        old_sel = core.load_json(root / R8SEL)
        assert len(old_sel["assignments"]) == 111
        assert not any("VM-D112" in json.dumps(a, ensure_ascii=False) for a in old_sel["assignments"])
        sel = dict(old_sel)
        sel["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        }
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        assert not sel_path.exists(), "canonical selection should have been invalidated"
        core.write_json(sel_path, sel)
        errs = archbase.validate_selection(
            root, sel, profile_path, matrix_path, comp_path, ledger_path)
        assert not errs, errs[:5]
        print("selection assignments:", len(sel["assignments"]))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "selection-stage-validation-111.json"
        reviews_path = vdir / "selection-stage-reviews-111.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Selection stage-contract validation passed over replayed 111 "
                         "authority (matrix 111 rows, 111 carried assignments, no Agentic "
                         "candidate). Machine validation only; Sol Selection review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            reviews_path,
            ("TS-003 Selection replay complete over 111-record canonical authority "
             "(matrix re-derived, 111 assignments carried, V1 identity held, no Agentic "
             "selection). Proceed to Architecture; Sol Selection review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "SELECTION_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
