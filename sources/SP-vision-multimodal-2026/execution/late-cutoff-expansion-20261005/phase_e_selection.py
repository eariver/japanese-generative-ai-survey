#!/usr/bin/env python3
"""TS-003 Phase E (late-cutoff expansion): Selection (120) + advance to SELECTION_COMPLETE.

- Candidate matrix re-derived at the canonical path (canonical derive + validate;
  120 rows; V1 held; SSv2-free).
- Selection: 112 carried byte-identical assignments (HEAD-committed authority) + 8 new
  SELECTED assignments (usage matches Architecture placement; no existing disposition
  touched). Basis rebased to the replayed chain.
- SSv2/entity check; stage validation + checkpoint + advance. Frozen Core only.
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
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"


def _assignment(cid_suffix, rationale, usage, pub_role, arch_role):
    return {
        "candidate_id": f"candidate:{ISSUE_ID}:{cid_suffix}",
        "disposition": "SELECTED",
        "rationale": rationale,
        "architecture_usage": usage,
        "publication_role": pub_role,
        "architecture_role": arch_role,
        "profile_extensions": {},
    }


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
        assert matrix["summary"]["candidate_count"] == 120
        d084 = [r for r in matrix["rows"] if "VM-D084" in r["discovery_ids"]]
        assert len(d084) == 1 and d084[0]["title"] == "Something-Something V1", d084
        assert "Something-Something V2" not in json.dumps(matrix, ensure_ascii=False)
        by_disc = {}
        for r in matrix["rows"]:
            for d in r["discovery_ids"]:
                by_disc[d] = r["candidate_id"]
        for did in ("VM-D113", "VM-D114", "VM-D115", "VM-D116",
                    "VM-D117", "VM-D118", "VM-D119", "VM-D120"):
            assert did in by_disc, did
        print("matrix rows:", matrix["summary"]["candidate_count"])

        head_sel = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-selection-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        assert len(head_sel["assignments"]) == 112
        assert head_sel["summary"] == {"candidate_count": 112,
                                       "disposition_counts": {"SELECTED": 112},
                                       "selected_count": 112}
        new_assignments = [
            _assignment(by_disc["VM-D113"].split(":")[-1],
                        "DINOv3 Gram-anchored dense refinement; frozen dense SOTA transition (P06).",
                        "PRIMARY", "LONGFORM_SPECIAL:primary-narrative", "THEMATIC:transition-anchor"),
            _assignment(by_disc["VM-D114"].split(":")[-1],
                        "SigLIP 2 staged alignment recipe; multilingual mixture and localization transfer (P06 home).",
                        "PRIMARY", "LONGFORM_SPECIAL:primary-narrative", "THEMATIC:transition-anchor"),
            _assignment(by_disc["VM-D115"].split(":")[-1],
                        "SAM 3 promptable concept segmentation; late convergence node (P03 home).",
                        "PRIMARY", "LONGFORM_SPECIAL:primary-narrative", "THEMATIC:transition-anchor"),
            _assignment(by_disc["VM-D116"].split(":")[-1],
                        "pi-zero flow-matching action interface; discrete-token vs flow transition (P13).",
                        "PRIMARY", "LONGFORM_SPECIAL:primary-narrative", "THEMATIC:transition-anchor"),
            _assignment(by_disc["VM-D117"].split(":")[-1],
                        "FAST DCT action tokenization transition; representation layer, separate from pi-zero (P13).",
                        "SUPPORTING", "LONGFORM_SPECIAL:supporting-context", "THEMATIC:lineage-context"),
            _assignment(by_disc["VM-D118"].split(":")[-1],
                        "AIMv2 autoregressive objective variant (P06 supporting).",
                        "SUPPORTING", "LONGFORM_SPECIAL:supporting-context", "THEMATIC:lineage-context"),
            _assignment(by_disc["VM-D119"].split(":")[-1],
                        "UGround universal screenshot grounder; vision-only interface transition (P12).",
                        "SUPPORTING", "LONGFORM_SPECIAL:supporting-context", "THEMATIC:lineage-context"),
            _assignment(by_disc["VM-D120"].split(":")[-1],
                        "ScreenSpot-Pro professional grounding evaluation anchor (P12).",
                        "SUPPORTING", "LONGFORM_SPECIAL:supporting-context", "THEMATIC:lineage-context"),
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
            "candidate_count": 120,
            "disposition_counts": {"SELECTED": 120},
            "selected_count": 120,
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
        validation_path = vdir / "selection-stage-validation-120.json"
        reviews_path = vdir / "selection-stage-reviews-120.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Selection stage-contract validation passed over 120-record canonical "
                         "authority (112 carried + 8 late-cutoff SELECTED, V1 held). Machine "
                         "validation only; Sol Selection review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            reviews_path,
            ("TS-003 Selection complete over 120-record canonical authority (112 carried, "
             "8 late-cutoff admitted SELECTED, V1 identity held). Proceed to Architecture; "
             "Sol Selection review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "SELECTION_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
