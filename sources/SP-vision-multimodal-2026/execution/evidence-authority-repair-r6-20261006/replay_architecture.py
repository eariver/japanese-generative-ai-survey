#!/usr/bin/env python3
"""TS-003 replay step 4 (exception-authorized r6): Architecture + advance to
ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: HEAD-committed r5-APPROVED architecture-v2.json + refreshed basis
  + PROPOSED status + THREE targeted semantic corrections only:
  P07A (BoW must_cover/boundary replaced), P05 (+LayoutLM v1 contract boundary),
  P13 (+pi-zero H/rate/cadence boundary).
- Fresh review-summary-v2 + attention-v2, canonical validate, advance
  SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED. STOP THERE.
- Delta guard: changed JSON paths must be exactly the allowlisted set.
- Frozen Core only.
"""
from __future__ import annotations

import difflib
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
EDIR = f"{SRC}/execution/evidence-authority-repair-r6-20261006"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

P07A_MC_OLD = ("X01 image-text pair contracts visible; bag-of-words limit recorded "
               "as D07B motivator")
P07A_MC_NEW = ("X01 image-text pair contracts visible; original-paper zero-shot "
               "limitations bounded to reported tasks (no compositionality claim); "
               "D07A/D07B separation kept on distinct evaluation contracts")
P07A_BD_OLD = ("Bag-of-words alignment limits; efficiency/scale critiques need "
               "successor sources (SigLIP record).")
# Verbatim carry of the corrected D039 limitation (validator-required exact text,
# same 1:1 supersession pattern as the prior correction run). Semantic framing
# lives in the must_cover replacement above.
P07A_BD_NEW = ("Original-paper zero-shot limits: weak fine-grained classification (car "
               "models, flower species, aircraft variants), counting (CLEVRCounts), "
               "near-random novel systematic tasks (KITTI distance); out-of-distribution "
               "brittleness (MNIST 88%, below a pixel baseline); ~1000x compute estimated "
               "to reach overall SOTA (infeasible on current hardware).")
P05_BD_NEW = ("LayoutLM v1 pre-trains text + 2D layout (MVLM, optional MDC); Faster R-CNN "
              "image features integrate at downstream fine-tuning; image-embedding "
              "pre-training is stated future work belonging to successors.")
P13_BD_NEW = ("π₀ output contract is an H=50 continuous-action chunk (flow matching); "
              "control rates are platform-dependent (UR5e/Franka 20 Hz, others 50 Hz) with "
              "re-inference after 16/25 actions (≈0.8/0.5 s); horizon, rate, and replan "
              "cadence are distinct quantities.")


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


def _paths(old, new, prefix=""):
    """Changed leaf JSON paths between two structures."""
    out = set()
    if isinstance(old, dict) and isinstance(new, dict):
        for k in set(old) | set(new):
            if k not in old:
                out.add(f"{prefix}/{k}=ADDED")
            elif k not in new:
                out.add(f"{prefix}/{k}=REMOVED")
            else:
                out |= _paths(old[k], new[k], f"{prefix}/{k}")
    elif isinstance(old, list) and isinstance(new, list):
        if old != new:
            out.add(f"{prefix}[{len(old)}->{len(new)}]")
    else:
        if old != new:
            out.add(prefix)
    return out


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("expected canonical State at SELECTION_COMPLETE")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        head_v2 = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        for p in (ledger_path, comp_path, matrix_path, sel_path):
            assert p.is_file(), p

        arch = json.loads(json.dumps(head_v2))
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

        # --- targeted semantic corrections (only) ---
        p07a = _package(arch, "P07A")
        assert P07A_MC_OLD in p07a["must_cover_requirements"], p07a["must_cover_requirements"]
        p07a["must_cover_requirements"] = [
            P07A_MC_NEW if r == P07A_MC_OLD else r for r in p07a["must_cover_requirements"]]
        assert P07A_BD_OLD in p07a["boundaries"], p07a["boundaries"]
        p07a["boundaries"] = [
            P07A_BD_NEW if b == P07A_BD_OLD else b for b in p07a["boundaries"]]

        p05 = _package(arch, "P05")
        assert P05_BD_NEW not in p05["boundaries"]
        p05["boundaries"] = list(p05["boundaries"]) + [P05_BD_NEW]

        p13 = _package(arch, "P13")
        assert P13_BD_NEW not in p13["boundaries"]
        p13["boundaries"] = list(p13["boundaries"]) + [P13_BD_NEW]

        # --- invariants: skeleton, placements, map, freeze ---
        assert len(arch["packages"]) == 16
        for hp, np in zip(head_v2["packages"], arch["packages"]):
            assert hp["package_id"] == np["package_id"]
            assert hp["primary_candidate_ids"] == np["primary_candidate_ids"], np["package_id"]
            assert hp["supporting_candidate_ids"] == np["supporting_candidate_ids"], np["package_id"]
            assert hp["drafting_order"] == np["drafting_order"]
            assert hp["title"] == np["title"] and hp["purpose"] == np["purpose"]
        assert arch["page_plan"] == head_v2["page_plan"] if "page_plan" in head_v2 else True
        pe = arch["publication_extensions"]
        assert "p15_cross_package_synthesis_map" in pe
        assert len({i for v in pe["p15_cross_package_synthesis_map"].values() for i in v}) == 40
        blob = json.dumps(arch, ensure_ascii=False)
        assert "bag-of-words" not in blob, "BoW wording survives in fresh Architecture"
        assert "VM-D122" not in blob
        assert "50Hz 50-step" not in blob

        # --- delta guard: allowlisted changed paths only ---
        changed = _paths(head_v2, arch)
        allowed_substrings = {"/basis", "/status", "/human_review",
                              "/packages", "P07A", "P05", "P13"}
        bad = [c for c in changed if not any(a in c for a in ("/basis", "/status", "/human_review"))]
        # packages diff is Regime expected only via the three targeted edits; verify precisely:
        assert bad == [] or all(c.startswith("/packages") for c in bad), bad
        pkgs_old = {p["package_id"]: p for p in head_v2["packages"]}
        pkgs_new = {p["package_id"]: p for p in arch["packages"]}
        for pid in pkgs_old:
            if pkgs_old[pid] != pkgs_new[pid]:
                assert pid in ("P05", "P07A", "P13"), pid
        p07a_new = pkgs_new["P07A"]
        assert len(p07a_new["must_cover_requirements"]) == len(pkgs_old["P07A"]["must_cover_requirements"])
        assert len(p07a_new["boundaries"]) == len(pkgs_old["P07A"]["boundaries"])
        assert len(pkgs_new["P05"]["boundaries"]) == len(pkgs_old["P05"]["boundaries"]) + 1
        assert len(pkgs_new["P13"]["boundaries"]) == len(pkgs_old["P13"]["boundaries"]) + 1
        print("delta guard: only P05/P07A/P13 targeted edits + basis/status/review")

        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, 40-map preserved, BoW purged)")

        disc_rel = root / f"{SRC}/discovery/discovery-v2.jsonl"
        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: (core.load_json(p)["record_count"], p.stat().st_mtime))
        new_pkg = core.load_json(max(
            (root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
            key=lambda p: p.stat().st_mtime).parent / "package.json")
        scr_acc = (root / new_pkg["basis"]["screening_acceptance_path"]).resolve()
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

        head_text = subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8")
        diff = "\n".join(difflib.unified_diff(
            head_text.splitlines(), arch_path.read_text(encoding="utf-8").splitlines(),
            fromfile="architecture-v2.json@r5-approved", tofile="architecture-v2.json@r6-pending", n=1))
        (root / EDIR / "architecture-r5-to-r6.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-121.json"
        reviews_path = vdir / "architecture-stage-reviews-121.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Architecture stage-contract validation passed over replayed 121-record "
                         "canonical authority (fresh PROPOSED Architecture bound to replayed chain, "
                         "P07A BoW wording replaced, P05/P13 contract boundaries added, 40-map "
                         "preserved). Machine validation only; Sol Architecture review + Human "
                         "r6 decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture replayed over 121-record canonical authority (skeleton "
             "stable, P07A BoW replaced, P05/P13 boundaries added, 40-map preserved). "
             "STOP at fresh pending Human Architecture Review r6; Sol review + Human "
             "decision owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
        assert updated["human_gates"]["architecture_review"] == "pending", updated["human_gates"]
        assert updated["human_gate_provenance"]["architecture_review"] is None
    print("lifecycle:", updated["lifecycle_state"], "| gates:", updated["human_gates"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
