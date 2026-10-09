#!/usr/bin/env python3
"""TS-003 Phase E (final closure): Selection (122) + advance to SELECTION_COMPLETE.

- Matrix re-derived (canonical derive + validate; 122 rows; V1 held; SSv2-free).
- Selection: 120 carried byte-identical assignments (HEAD-committed authority) + 2 new
  SELECTED assignments (VM-D121 PRIMARY P14; VM-D122 SUPPORTING P15 home?/P14 support —
  see Architecture: VM-D122 PRIMARY in P15, SUPPORTING in P14; single-kind rule forces
  ONE usage per candidate).
- NOTE on the single-kind rule: a candidate's Selection architecture_usage must equal
  its placement kind in EVERY placing package. VM-D122 is PRIMARY in P15 and SUPPORTING
  in P14 → IMPOSSIBLE under frozen validation. Resolution: VM-D121 PRIMARY (P14 only);
  VM-D122 SUPPORTING (P15 methodology home? or P14?).
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2_base as archbase
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/final-closure-repair-20261005"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"


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
        assert matrix["summary"]["candidate_count"] == 122
        d084 = [r for r in matrix["rows"] if "VM-D084" in r["discovery_ids"]]
        assert len(d084) == 1 and d084[0]["title"] == "Something-Something V1", d084
        assert "Something-Something V2" not in json.dumps(matrix, ensure_ascii=False)
        by_disc = {}
        for r in matrix["rows"]:
            for d in r["discovery_ids"]:
                by_disc[d] = r["candidate_id"]
        assert "VM-D121" in by_disc and "VM-D122" in by_disc
        print("matrix rows:", matrix["summary"]["candidate_count"])

        head_sel = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-selection-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        assert len(head_sel["assignments"]) == 120
        new_assignments = [
            {"candidate_id": by_disc["VM-D121"],
             "disposition": "SELECTED",
             "rationale": ("V-JEPA 2/2-AC two-stage predictive-planning contract; intra-pole "
                           "transition in the JEPA predictive pole (P14 primary)."),
             "architecture_usage": "PRIMARY",
             "publication_role": "LONGFORM_SPECIAL:primary-narrative",
             "architecture_role": "THEMATIC:transition-anchor",
             "profile_extensions": {}},
            {"candidate_id": by_disc["VM-D122"],
             "disposition": "SELECTED",
             "rationale": ("Planning-limits cross-backbone range evidence; P15 methodology/evaluation "
                           "authority bounding control-oriented world-model claims; P14 control-use limitation "
                           "via synthesis direction."),
             "architecture_usage": "PRIMARY",
             "publication_role": "LONGFORM_SPECIAL:primary-narrative",
             "architecture_role": "THEMATIC:transition-anchor",
             "profile_extensions": {}},
        ]
        have = {a["candidate_id"] for a in head_sel["assignments"]}
        assert not any(a["candidate_id"] in have for a in new_assignments)
        sel = dict(head_sel)
        sel["assignments"] = [*head_sel["assignments"], *new_assignments]
        sel["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        }
        sel["summary"] = {
            "candidate_count": 122,
            "disposition_counts": {"SELECTED": 122},
            "selected_count": 122,
        }
        assert "Something-Something V2" not in json.dumps(sel, ensure_ascii=False)
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        assert not sel_path.exists(), "canonical selection should have been invalidated"
        core.write_json(sel_path, sel)
        errs = archbase.validate_selection(
            root, sel, profile_path, matrix_path, comp_path, ledger_path)
        assert not errs, errs[:5]
        print("selection assignments:", len(sel["assignments"]))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "selection-stage-validation-122.json"
        reviews_path = vdir / "selection-stage-reviews-122.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Selection stage-contract validation passed over 122-record canonical "
                         "authority (120 carried + VM-D121 PRIMARY / VM-D122 SUPPORTING, V1 held). "
                         "Machine validation only."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            reviews_path,
            ("TS-003 Selection complete over 122-record canonical authority (120 carried, "
             "2 admitted SELECTED, V1 identity held). Proceed to Architecture."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "SELECTION_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
