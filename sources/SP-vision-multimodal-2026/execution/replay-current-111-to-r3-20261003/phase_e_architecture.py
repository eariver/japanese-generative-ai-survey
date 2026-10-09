#!/usr/bin/env python3
"""TS-003 replay Phase E: Architecture (canonical v2 recreation) + advance to
ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: architecture-v4.json packages (surviving proposal; already
  clean of V2/SIMA-training/aux-mandatory staleness) + refreshed basis.
- Sole content change per §11 P02: one boundary making the matching-cost /
  training-loss / auxiliary-recipe distinction an explicit drafting requirement.
- P12/P14/P15 bindings verified already correct (condition binding, vendor caps,
  no training-use language) — carried unchanged.
- No VM-D112 node anywhere (not admitted). Status PROPOSED, human_review null.
- Recreate canonical architecture-v2.json + review-summary-v2 + attention-v2
  (all deleted by re-entry), validate, advance SELECTION_COMPLETE ->
  ARCHITECTURE_ESTABLISHED. STOP THERE.
- Frozen Core only + documented post-gate adaptation. Sol review + Human
  decision owed; neither fabricated.
"""

from __future__ import annotations

import difflib
import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2_base as archbase
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/replay-current-111-to-r3-20261003"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

V4_REL = f"{SRC}/architecture-v4.json"
P02_DETR_BOUNDARY = ("Matching cost (assignment) vs matched-pair training loss kept "
                     "distinct; auxiliary decoder losses are standard-recipe, never "
                     "architecture-mandatory.")


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("expected canonical State at SELECTION_COMPLETE")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        v4 = core.load_json(root / V4_REL)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        for p in (ledger_path, comp_path, matrix_path, sel_path):
            assert p.is_file(), p

        arch = json.loads(json.dumps(v4))
        arch["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(sel_path),
        }
        arch["status"] = "PROPOSED"
        arch["human_review"] = {"reviewed_by": None, "reviewed_at": None,
                                "review_reference": None}
        hit = 0
        for p in arch["packages"]:
            if p["package_id"] == "P02":
                assert P02_DETR_BOUNDARY not in p["boundaries"]
                p["boundaries"].append(P02_DETR_BOUNDARY)
                hit += 1
        assert hit == 1
        # No VM-D112 anywhere in the replayed Architecture.
        assert "VM-D112" not in json.dumps(arch, ensure_ascii=False)
        assert "Something-Something V2" not in json.dumps(arch, ensure_ascii=False)
        assert "SIMA-agent training use" not in json.dumps(arch, ensure_ascii=False)
        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, pending review)")

        disc_rel = root / f"{SRC}/discovery/discovery-v2.jsonl"
        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        view_acc = max((root / SRC / "evidence/v2/views/accepted").glob("*/edition-views-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
        summary = archbase.build_architecture_review_summary(
            root, profile_path, disc_rel, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, matrix_path, sel_path, arch_path, impl)
        sum_path = root / f"{SRC}/architecture-review-summary-v2.json"
        assert not sum_path.exists()
        core.write_json(sum_path, summary)
        attn_path = root / f"{SRC}/architecture-review-attention-v2.json"
        assert not attn_path.exists()
        review_attention.build_attention(
            root, scr_acc, ledger_path, sel_path, attn_path)
        review_attention.validate_attention(root, attn_path)
        print("review summary + attention recreated")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-111.json"
        reviews_path = vdir / "architecture-stage-reviews-111.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Architecture stage-contract validation passed over replayed 111 "
                         "authority (fresh Architecture bound to replayed chain, no Agentic "
                         "node). Machine validation only; Sol Architecture review + Human "
                         "decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture replay complete over 111-record canonical authority "
             "(skeleton stable, P02 cost/loss requirement added, no Agentic admission). "
             "STOP at fresh pending Human Architecture Review r3; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
        assert updated["human_gates"]["architecture_review"] == "pending", updated["human_gates"]
    print("lifecycle:", updated["lifecycle_state"], "| gates:", updated["human_gates"])

    # Review-package diff vs the most recent proposal (v4).
    old_lines = (root / V4_REL).read_text(encoding="utf-8").splitlines()
    new_lines = arch_path.read_text(encoding="utf-8").splitlines()
    diff = "\n".join(difflib.unified_diff(old_lines, new_lines,
                                          fromfile="architecture-v4.json",
                                          tofile="architecture-v2.json", n=2))
    (root / EDIR / "architecture-v4-to-v2replay.diff").write_text(diff + "\n", encoding="utf-8")
    print("diff lines:", len(diff.splitlines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
