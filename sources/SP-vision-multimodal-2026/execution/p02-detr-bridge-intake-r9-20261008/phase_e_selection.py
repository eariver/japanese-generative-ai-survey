#!/usr/bin/env python3
"""TS-003 Phase E (P02 bounded bridge intake): Selection (124) + advance to
SELECTION_COMPLETE.

- Matrix re-derived (canonical derive + validate; 124 rows: 121 carried
  candidate_ids stable + 3 new bridge rows).
- Selection: 121 assignments carried byte-identical from HEAD-committed authority
  (basis/summary rebased) + 3 new SELECTED assignments (VM-D123/VM-D125 PRIMARY
  transition-anchor; VM-D124 SUPPORTING brief supporting role).
- Stage validation + checkpoint + advance. Frozen Core only.
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
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
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
        assert core.load_json(ev_acc)["result_count"] == 124

        matrix = archbase.derive_candidate_matrix(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, impl)
        assert archbase.validate_candidate_matrix(
            matrix, root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            view_acc, ledger_path, comp_path, impl) == []
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        assert not matrix_path.exists(), "canonical matrix should have been invalidated"
        core.write_json(matrix_path, matrix)
        assert matrix["summary"]["candidate_count"] == 124
        by_disc = {}
        for r in matrix["rows"]:
            for d in r["discovery_ids"]:
                by_disc[d] = r["candidate_id"]
        for did in ("VM-D123", "VM-D124", "VM-D125"):
            assert did in by_disc, did
        assert "VM-D122" not in by_disc
        print("matrix rows:", matrix["summary"]["candidate_count"])

        head_sel = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-selection-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        assert len(head_sel["assignments"]) == 121
        new_assignments = [
            {"candidate_id": by_disc["VM-D123"],
             "disposition": "SELECTED",
             "rationale": ("Deformable DETR efficient multi-scale sparse-attention bridge "
                           "(convergence/small-object repair); P02 transition node feeding "
                           "DINO deformable-attention/query-selection use."),
             "architecture_usage": "PRIMARY",
             "publication_role": "LONGFORM_SPECIAL:primary-narrative",
             "architecture_role": "THEMATIC:transition-anchor",
             "profile_extensions": {}},
            {"candidate_id": by_disc["VM-D124"],
             "disposition": "SELECTED",
             "rationale": ("DAB-DETR dynamic anchor-box query bridge (brief supporting "
                           "treatment); feeds DINO anchor-query formulation directly."),
             "architecture_usage": "SUPPORTING",
             "publication_role": "LONGFORM_SPECIAL:primary-narrative",
             "architecture_role": "THEMATIC:transition-anchor",
             "profile_extensions": {}},
            {"candidate_id": by_disc["VM-D125"],
             "disposition": "SELECTED",
             "rationale": ("DN-DETR denoising-training bridge (matching-instability repair); "
                           "P02 transition node feeding DINO contrastive denoising."),
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
            "candidate_count": 124,
            "disposition_counts": {"SELECTED": 124},
            "selected_count": 124,
        }
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        assert not sel_path.exists(), "canonical selection should have been invalidated"
        core.write_json(sel_path, sel)
        errs = archbase.validate_selection(
            root, sel, profile_path, matrix_path, comp_path, ledger_path)
        assert not errs, errs[:5]
        print("selection assignments:", len(sel["assignments"]), "(121 carried + 3 new SELECTED)")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "selection-stage-validation-124.json"
        reviews_path = vdir / "selection-stage-reviews-124.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Selection stage-contract validation passed over 124-record canonical "
                         "authority (121 carried + VM-D123 PRIMARY / VM-D124 SUPPORTING / VM-D125 "
                         "PRIMARY). Machine validation only; Sol Selection review + Human decision owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            reviews_path,
            ("TS-003 Selection complete over 124-record canonical authority (121 carried, "
             "3 P02 bridge admissions SELECTED). Proceed to Architecture."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "SELECTION_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
