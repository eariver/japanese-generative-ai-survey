#!/usr/bin/env python3
"""TS-003 Phase F (P02 bounded bridge intake): Architecture r9 candidate +
advance to ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: HEAD-committed r8 PROPOSED architecture-v2.json + refreshed
  basis + PROPOSED status + TARGETED P02 semantic change only:
  + 2 primary transition nodes (Deformable DETR, DN-DETR),
  + 1 supporting brief node (DAB-DETR),
  + explicit bridge must-cover requirements + DINO-convergence requirement,
  + boundary repair (small-object/convergence now inside via Deformable;
    parallel/convergent branches, not linear genealogy),
  + depth classes (TRANSITION x2, BRIEF x1). Page budget unchanged (6).
- All other 15 packages byte-identical (delta guard enforced).
- Fresh review-summary-v2 + attention-v2, canonical validate, advance
  SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED with gates pending. STOP THERE.
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
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

CID_DEFORMABLE = "candidate:SP-vision-multimodal-2026:6018779ae64eed93"
CID_DAB = "candidate:SP-vision-multimodal-2026:d277a60ff2531b80"
CID_DN = "candidate:SP-vision-multimodal-2026:c7fd3834cd4f0ee2"

MC_DEFORMABLE = ("Deformable DETR bridge: multi-scale sparse deformable attention with "
                 "reference-point sampling; faster convergence and small-object repair "
                 "(transition node; not a general deformable-attention survey)")
MC_DAB = ("DAB-DETR bridge: dynamic anchor-box queries with layer-by-layer updates and "
          "explicit positional priors (brief supporting treatment; feeds DINO anchor-query "
          "formulation)")
MC_DN = ("DN-DETR bridge: query denoising training against bipartite-matching instability "
         "(transition node; not diffusion denoising)")
MC_DINO_CONV = ("DINO as convergence of DETR-successor techniques (DN-style denoising improved, "
                "DAB-style dynamic anchors, deformable-style attention/query selection); "
                "parallel/convergent branches, not a one-hop vanilla-DETR succession")

B_NEW_BRANCH = ("DETR-successor branches are parallel/convergent (deformable attention, "
                "dynamic anchors, denoising training), not a single strictly linear "
                "genealogy; DINO integrates them.")
# Evidence limitation strings must appear VERBATIM in package boundaries
# (Core validate_architecture: matrix remaining_boundaries ⊆ boundaries).
LIM_DEFORMABLE = ("Single-scale vs multi-scale variant scope; two-stage query-selection "
                  "and iterative refinement are optional extensions; FPN-general survey "
                  "stays outside this bridge role.")
LIM_DAB = ("Single-scale DETR-baseline scope; Anchor/Conditional DETR taxonomy stays "
           "outside; brief supporting treatment only.")
LIM_DN = ("Uniform-distribution noise sampling only; query-denoising training, not "
          "diffusion-model denoising; transition-node treatment only.")


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


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

        # --- P02: bounded DETR-successor bridge (only Architecture semantic change) ---
        p02 = _package(arch, "P02")
        assert p02["primary_candidate_ids"][-1] == "candidate:SP-vision-multimodal-2026:0491441302a2203a"
        p02["primary_candidate_ids"] = [*p02["primary_candidate_ids"], CID_DEFORMABLE, CID_DN]
        p02["supporting_candidate_ids"] = [*p02["supporting_candidate_ids"], CID_DAB]
        assert "VM-O02 lineage complete incl. DINO-name disambiguation" in p02["must_cover_requirements"]
        p02["must_cover_requirements"] = [*p02["must_cover_requirements"],
                                         MC_DEFORMABLE, MC_DAB, MC_DN, MC_DINO_CONV]
        # B6 (DETR limitation, verbatim) is kept: Core requires Evidence limitation
        # strings verbatim in boundaries; the repair role lives in must-cover.
        assert ("Small-object deficit and training cost are paper-stated open challenges; "
                "FPN-style successors address them outside this source.") in p02["boundaries"]
        for _lim in (LIM_DEFORMABLE, LIM_DAB, LIM_DN, B_NEW_BRANCH):
            assert _lim not in p02["boundaries"]
        p02["boundaries"] = [*p02["boundaries"], LIM_DEFORMABLE, LIM_DAB, LIM_DN, B_NEW_BRANCH]
        depth = p02["publication_extensions"]["depth_classes"]
        depth["TRANSITION_NODE_TREATMENT"] = [*depth["TRANSITION_NODE_TREATMENT"], "VM-D123", "VM-D125"]
        depth["BRIEF_CONTEXT_OR_AUTHORITY"] = [*depth["BRIEF_CONTEXT_OR_AUTHORITY"], "VM-D124"]
        assert p02["publication_extensions"]["page_budget_body_pages"] == 6

        # --- invariants ---
        assert len(arch["packages"]) == 16
        for hp, np in zip(head_v2["packages"], arch["packages"]):
            assert hp["package_id"] == np["package_id"]
            assert hp["drafting_order"] == np["drafting_order"]
            assert hp["title"] == np["title"] and hp["purpose"] == np["purpose"], np["package_id"]
        assert arch["page_plan"] == head_v2["page_plan"]
        assert arch["editorial_thesis"] == head_v2["editorial_thesis"]
        assert arch["architecture_goals"] == head_v2["architecture_goals"]
        pe = arch["publication_extensions"]
        assert len({i for v in pe["p15_cross_package_synthesis_map"].values() for i in v}) == 40
        old_ids = {i for v in head_v2["publication_extensions"]["p15_cross_package_synthesis_map"].values() for i in v}
        new_ids = {i for v in pe["p15_cross_package_synthesis_map"].values() for i in v}
        assert old_ids == new_ids and len(new_ids) == 40
        assert list(pe["p15_cross_package_synthesis_map"]) == list(head_v2["publication_extensions"]["p15_cross_package_synthesis_map"])
        blob = json.dumps(arch, ensure_ascii=False)
        assert "VM-D122" not in blob
        assert "DETR + denoising" not in blob and "one-hop" not in blob or "not a one-hop" in blob
        assert "author/developer self-reported" in blob, "r8 taxonomy lost"
        assert "not a paper-measured contamination rate" in blob, "r8 DocVQA wording lost"

        # --- delta guard: only P02 (+ basis/status/review) ---
        pkgs_old = {p["package_id"]: p for p in head_v2["packages"]}
        pkgs_new = {p["package_id"]: p for p in arch["packages"]}
        for pid in pkgs_old:
            if pkgs_old[pid] != pkgs_new[pid]:
                assert pid in ("P02",), pid
        print("delta guard: only P02 bridge change + basis/status/review")

        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED r9 candidate, P02 bridge, 40-map preserved)")

        disc_rel = root / f"{SRC}/discovery/discovery-v2.jsonl"
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
        assert summary.get("readiness", {}).get("status") == "READY_FOR_ARCHITECTURE_REVIEW", summary.get("readiness")
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
            fromfile="architecture-v2.json@r8-approved", tofile="architecture-v2.json@r9-pending-regen", n=1))
        (root / EDIR / "architecture-r8approved-to-r9regen.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-124.json"
        reviews_path = vdir / "architecture-stage-reviews-124.json"
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
            "evidence": ("Architecture stage-contract validation passed over 124-record "
                         "canonical authority (fresh PROPOSED r9 candidate with P02 DETR-successor "
                         "bridge, 40-map preserved). Machine validation only; Sol Architecture "
                         "review + Human r9 decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture r9 candidate over 124-record canonical authority (P02 bridge: "
             "Deformable/DAB/DN transition nodes, DINO convergence). "
             "STOP at fresh pending Human Architecture Review r9; Sol review + Human "
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
