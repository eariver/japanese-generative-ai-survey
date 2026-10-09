#!/usr/bin/env python3
"""TS-003 sync replay (exception-authorized, run sync-repair-r5): EVIDENCE_REVIEWED ->
SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED. STOP at r5 PENDING.

- Matrix: canonical re-derive (expect byte-identical to HEAD: inputs unchanged).
- Selection: 112 carried assignments + 1 rationale-only sync + basis recompute.
- EVIDENCE_REVIEWED checkpoint rebuild + advance.
- Architecture: HEAD base + P06 must_cover sync + P09 scoped companion + basis refresh.
- Summaries fresh rebuild; stage validation + checkpoint + advance. Frozen Core only.
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
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/sync-repair-r5-20261004"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
VALIDATION_REL = f"{EDIR}/validation"

SEL_OLD = "SigLIP sigmoid-loss alignment + encoder-reuse lineage into Qwen (G06 citation residual)."
SEL_NEW = "SigLIP sigmoid-loss alignment + encoder-reuse lineage into Qwen; SigLIP2 reuse bound via VM-D065 claim-3."
P06_OLD = "VM-O06 lineage complete; G06 SigLIP2 citation residual bounded"
P06_NEW = "VM-O06 lineage complete; SigLIP2 encoder reuse bound via VM-D065 claim-3"
P09_ADD = "Qwen3-Omni repository (VM-D075): weight/code license status remains unresolved in canonical Evidence."


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

        # 1. Matrix re-derive (inputs unchanged -> expect HEAD-identical bytes)
        matrix = archbase.derive_candidate_matrix(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, impl)
        assert archbase.validate_candidate_matrix(
            matrix, root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            view_acc, ledger_path, comp_path, impl) == []
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        assert not matrix_path.exists()
        core.write_json(matrix_path, matrix)
        head_matrix = subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-matrix-v2.json"],
            cwd=root, check=True, capture_output=True).stdout
        assert matrix_path.read_bytes() == head_matrix, "matrix must be byte-identical (inputs unchanged)"
        print("matrix: re-derived byte-identical, 112 rows")

        # 2. Selection: carried + 1 rationale sync
        head_sel = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/candidate-selection-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        assert len(head_sel["assignments"]) == 112
        sel = dict(head_sel)
        sel["assignments"] = [dict(a) for a in head_sel["assignments"]]
        edited = 0
        for a in sel["assignments"]:
            if a["candidate_id"].endswith("c9e9f8f71019"):
                assert a["rationale"] == SEL_OLD, a["rationale"]
                a["rationale"] = SEL_NEW
                edited += 1
        assert edited == 1
        sel["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        }
        sel["summary"] = dict(head_sel["summary"])
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        assert not sel_path.exists()
        core.write_json(sel_path, sel)
        errs = archbase.validate_selection(
            root, sel, profile_path, matrix_path, comp_path, ledger_path)
        assert not errs, errs[:5]
        print("selection: 112 carried + 1 rationale sync, PASS")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        vp1 = vdir / "selection-stage-validation.json"
        rp1 = vdir / "selection-stage-reviews.json"
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path}, vp1, now)
        core.write_json(rp1, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Human/Sol decision)",
            "evidence": ("Selection stage-contract validation passed (matrix byte-identical, "
                         "112 assignments carried + 1 rationale sync). Machine validation only."),
            "result_path": str(vp1.relative_to(root))}]})
        gen1 = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"candidate-matrix": matrix_path, "candidate-selection": sel_path}, rp1,
            "TS-003 Selection synced (rationale-only). Proceed to Architecture.", now)
        upd = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, gen1)
        assert upd["lifecycle_state"] == "SELECTION_COMPLETE"
        print("advanced:", upd["lifecycle_state"])

        # 3. Architecture: HEAD base + P06/P09 sync + basis
        head_arch = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        arch = json.loads(json.dumps(head_arch))
        pkgs = {p["package_id"]: p for p in arch["packages"]}
        p06 = pkgs["P06"]
        assert P06_OLD in p06["must_cover_requirements"]
        p06["must_cover_requirements"] = [
            P06_NEW if m == P06_OLD else m for m in p06["must_cover_requirements"]]
        p09 = pkgs["P09"]
        assert P09_ADD not in p09["boundaries"]
        p09["boundaries"].append(P09_ADD)
        assert len(arch["packages"]) == 16
        mmap = arch["publication_extensions"]["p15_cross_package_synthesis_map"]
        assert len({i for v in mmap.values() for i in v}) == 39
        arch["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(sel_path),
        }
        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists()
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture: P06/P09 synced, PASS")

        # 4. Summaries fresh
        summary = archbase.build_architecture_review_summary(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, matrix_path, sel_path, arch_path, impl)
        sum_path = root / f"{SRC}/architecture-review-summary-v2.json"
        assert not sum_path.exists()
        core.write_json(sum_path, summary)
        attn_path = root / f"{SRC}/architecture-review-attention-v2.json"
        assert not attn_path.exists()
        review_attention.build_attention(root, scr_acc, ledger_path, sel_path, attn_path)
        review_attention.validate_attention(root, attn_path)
        print("summaries rebuilt")

        now2 = datetime.now(timezone.utc)
        vp2 = vdir / "architecture-stage-validation.json"
        rp2 = vdir / "architecture-stage-reviews.json"
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, vp2, now2)
        core.write_json(rp2, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Human/Sol decision)",
            "evidence": ("Architecture stage-contract validation passed (P06/P09 synced, "
                         "skeleton preserved). Machine validation only; Human decision owed."),
            "result_path": str(vp2.relative_to(root))}]})
        gen2 = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, rp2,
            "TS-003 Architecture synced (G06 resolved wording, P09 scoped companion, skeleton preserved). STOP at fresh pending Human Architecture Review r5.", now2)
        upd2 = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, gen2)
        assert upd2["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED"
        assert upd2["human_gates"]["architecture_review"] == "pending"
        errors = agent.validate_agent_state(root, cfg, upd2)
        assert not errors, errors
    print("lifecycle:", upd2["lifecycle_state"], "| gates:", upd2["human_gates"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
