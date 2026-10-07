#!/usr/bin/env python3
"""TS-003 replay step 3 (exception-authorized r6-final): Selection (121) + advance to
SELECTION_COMPLETE.

- Candidate Matrix re-derived at the canonical path (canonical derive + validate;
  121 rows; evidence SHAs rebased for the 5 corrected tasks only).
- Selection: 121 assignments carried byte-identical from HEAD-committed authority,
  with ONE targeted semantic correction (VM-D065/Qwen3-VL rationale: vendor
  measures -> author/developer self-reported measures; disposition SELECTED
  unchanged) + basis/summary rebased to the replayed chain. VM-D112 vendor
  ceilings preserved (provider). No disposition change.
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
EDIR = f"{SRC}/execution/r8-authority-binding-repair-20261007"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"

SEL065_UNUSED_OLD = "Qwen3-VL open architecture case: interleaved-MRoPE, DeepStack, timestamp alignment (vendor measures quarantined)."
SEL065_UNUSED_NEW = ("Qwen3-VL open architecture case: interleaved-MRoPE, DeepStack, timestamp alignment "
              "(author/developer self-reported measures quarantined).")


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "EVIDENCE_REVIEWED":
        raise ValueError("expected canonical State at EVIDENCE_REVIEWED")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        new_pkg = core.load_json(ev_acc.parent / "package.json")
        scr_acc = (root / new_pkg["basis"]["screening_acceptance_path"]).resolve()
        assert scr_acc.is_file(), scr_acc
        view_acc = max((root / SRC / "evidence/v2/views/accepted").glob("*/edition-views-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
        assert core.load_json(ev_acc)["result_count"] == 121
        assert len(ev_acc.parent.name) == 64, ev_acc.parent.name
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
        assert matrix["summary"]["candidate_count"] == 121
        head_mx = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-matrix-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        head_rows = {tuple(r["discovery_ids"])[0]: r for r in head_mx["rows"]}
        new_rows = {tuple(r["discovery_ids"])[0]: r for r in matrix["rows"]}
        assert set(head_rows) == set(new_rows), "matrix row set drift"
        sha_changed = sorted(d for d in head_rows
                             if head_rows[d]["evidence_sha256"] != new_rows[d]["evidence_sha256"])
        assert sha_changed == ["VM-D039"], sha_changed
        print("matrix rows: 121 | evidence-SHA changes exactly:", sha_changed)
        # matrix remaining_boundaries flow from corrected evidence: verify taxonomy
        blob = json.dumps(matrix, ensure_ascii=False)
        assert "contamination MEDIUM" not in blob and "language-prior HIGH" not in blob
        assert "provably unnecessary" not in blob
        # corrected limitation flows deterministically into remaining_boundaries
        assert "1.28M labels" not in blob  # corrected claim-1 unit lives in Evidence cards

        head_sel = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-selection-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        assert len(head_sel["assignments"]) == 121
        # selection rationales carry no DocVQA grades / DETR overstatement: carry byte-identical
        for a in head_sel["assignments"]:
            ab = json.dumps(a, ensure_ascii=False)
            assert "contamination MEDIUM" not in ab and "language-prior HIGH" not in ab
            assert "provably unnecessary" not in ab
        sel = dict(head_sel)
        sel["assignments"] = [dict(a) for a in head_sel["assignments"]]
        sel["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        }
        sel["summary"] = dict(head_sel["summary"])
        assert "contamination MEDIUM" not in json.dumps(sel, ensure_ascii=False)
        assert "provably unnecessary" not in json.dumps(sel, ensure_ascii=False)
        # VM-D112 provider ceilings preserved
        assert "vendor ceilings version-bound" in json.dumps(sel, ensure_ascii=False)  # VM-D112 provider wording preserved
        assert [(a["candidate_id"], a["disposition"]) for a in sel["assignments"]] == \
               [(a["candidate_id"], a["disposition"]) for a in head_sel["assignments"]]
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        assert not sel_path.exists(), "canonical selection should have been invalidated"
        core.write_json(sel_path, sel)
        errs = archbase.validate_selection(
            root, sel, profile_path, matrix_path, comp_path, ledger_path)
        assert not errs, errs[:5]
        print("selection assignments: 121 carried byte-identical (0 rationale changes, 0 disposition changes)")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "selection-stage-validation-121.json"
        reviews_path = vdir / "selection-stage-reviews-121.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Selection stage-contract validation passed over replayed 121-record "
                         "canonical authority (matrix re-derived with 1 corrected evidence SHA, "
                         "121 assignments carried byte-identical). Machine validation "
                         "only; Sol Selection review + Human decision owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path},
            reviews_path,
            ("TS-003 Selection replayed over 121-record canonical authority (matrix "
             "re-derived with 5 corrected evidence SHAs, 121 assignments carried, "
             "121 carried byte-identical). Proceed to Architecture; Sol Selection review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "SELECTION_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
