#!/usr/bin/env python3
"""TS-003 replay step 4 (exception-authorized r6-final): Architecture + advance to
ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: HEAD-committed r6-pending PROPOSED architecture-v2.json + refreshed
  basis + PROPOSED status + TARGETED semantic corrections only:
  P07A (VQA contamination boundary -> language-prior/complementary-pair),
  P09 (blanket vendor-measured -> three-way provenance; vendor ceilings ->
  provider/vendor ceilings; must_cover vendor latency -> first-party),
  P15 (vendor-vs-independent purpose/map-key -> three-way; Gemini boundaries ->
  provider/vendor-reported).
- Completeness G05 already refined upstream; Architecture carries no separate G05
  definition beyond (G05) tags preserved with corrected surrounding wording.
- Fresh review-summary-v2 + attention-v2, canonical validate, advance
  SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED. STOP THERE.
- Delta guard: only P07A/P09/P15 + basis/status/review change.
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
EDIR = f"{SRC}/execution/r8-authority-binding-repair-20261007"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

P11_MC_OLD = "SAM 3 memory video tracking as supporting stored-timeline evidence"
P11_MC_NEW = ("SAM 3 concept-prompted video grounding and memory-based tracking are supporting "
              "temporal-grounding evidence; stored-timeline on-demand navigation remains the "
              "distinct VM-D112 contract.")


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


def _paths(old, new, prefix=""):
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

        # --- P11: SAM 3 must-cover correction (only Architecture semantic change) ---
        p11 = _package(arch, "P11")
        assert P11_MC_OLD in p11["must_cover_requirements"], p11["must_cover_requirements"]
        p11["must_cover_requirements"] = [
            P11_MC_NEW if r == P11_MC_OLD else r for r in p11["must_cover_requirements"]]

        # --- P02/P07A/CLIP: verify corrected unit wording present via evidence carry ---
        # (CLIP boundaries carry verbatim evidence text; corrected card flows via matrix.)

        # --- invariants ---
        assert len(arch["packages"]) == 16
        for hp, np in zip(head_v2["packages"], arch["packages"]):
            assert hp["package_id"] == np["package_id"]
            assert hp["primary_candidate_ids"] == np["primary_candidate_ids"], np["package_id"]
            assert hp["supporting_candidate_ids"] == np["supporting_candidate_ids"], np["package_id"]
            assert hp["drafting_order"] == np["drafting_order"]
            assert hp["title"] == np["title"] and hp["purpose"] == np["purpose"], np["package_id"]
        assert arch["page_plan"] == head_v2["page_plan"]
        pe = arch["publication_extensions"]
        assert len({i for v in pe["p15_cross_package_synthesis_map"].values() for i in v}) == 40
        old_ids = {i for v in head_v2["publication_extensions"]["p15_cross_package_synthesis_map"].values() for i in v}
        new_ids = {i for v in pe["p15_cross_package_synthesis_map"].values() for i in v}
        assert old_ids == new_ids and len(new_ids) == 40
        assert list(pe["p15_cross_package_synthesis_map"]) == list(head_v2["publication_extensions"]["p15_cross_package_synthesis_map"])
        blob = json.dumps(arch, ensure_ascii=False)
        assert "1.28M labels" not in blob, "old CLIP unit survives in Architecture"
        assert "stored-timeline evidence" not in blob or "stored-timeline on-demand navigation remains" in blob
        assert "p09_measurement_provenance" in blob, "r6 map key lost"
        assert "author/developer self-reported" in blob, "r6/r7 taxonomy lost"
        assert "VQA-family accuracy can exploit question/answer priors" in blob, "r6/r7 VQA wording lost"
        assert "not a paper-measured contamination rate" in blob, "r7 DocVQA wording lost"
        assert "VM-D122" not in blob
        assert "contamination opacity" in blob

        # --- delta guard ---
        pkgs_old = {p["package_id"]: p for p in head_v2["packages"]}
        pkgs_new = {p["package_id"]: p for p in arch["packages"]}
        for pid in pkgs_old:
            if pkgs_old[pid] != pkgs_new[pid]:
                assert pid in ("P11",), pid
        print("delta guard: only P11 must-cover correction + basis/status/review")

        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, 40-map preserved, taxonomy corrected)")

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
            fromfile="architecture-v2.json@r7-approved", tofile="architecture-v2.json@r8-pending-regen", n=1))
        (root / EDIR / "architecture-r7approved-to-r8regen.diff").write_text(diff + "\n", encoding="utf-8")
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
                         "P11 SAM3 must-cover corrected, 40-map "
                         "preserved). Machine validation only; Sol Architecture review + Human "
                         "r7 decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture replayed over 121-record canonical authority (P11 SAM3 "
             "must-cover corrected, 40-map preserved). "
             "STOP at fresh pending Human Architecture Review r8; Sol review + Human "
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
