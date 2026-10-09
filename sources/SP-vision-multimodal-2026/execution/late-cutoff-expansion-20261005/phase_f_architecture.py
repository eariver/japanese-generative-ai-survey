#!/usr/bin/env python3
"""TS-003 Phase F (late-cutoff expansion): Architecture (120) + advance to
ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: HEAD-committed architecture (all prior repairs intact) + targeted
  late-cutoff placements (no other semantic change):
  P06: DINOv3/SigLIP 2 PRIMARY+TRANSITION, AIMv2 SUPPORTING+TRANSITION;
  P07A: SigLIP 2 SUPPORTING+BRIEF; P07B: SigLIP 2 + SAM 3 SUPPORTING+TRANSITION;
  P09: SigLIP 2 SUPPORTING+BRIEF; P03: SAM 3 PRIMARY+TRANSITION;
  P11: SAM 3 SUPPORTING+BRIEF; P13: pi-zero PRIMARY+TRANSITION, FAST SUPPORTING+TRANSITION
  (+ bounded purpose branch clause); P12: UGround + ScreenSpot-Pro SUPPORTING+TRANSITION.
- must_cover additions (concise, per-package). P15 map: VM-D120 appended to the
  P12 GUI axis ONLY (old 39 kept; methodology-load-bearing evaluation contract).
- Status PROPOSED, human_review null. Fresh review-summary/attention, validate,
  advance SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED. STOP THERE.
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
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

CID = {
    "VM-D113": "candidate:SP-vision-multimodal-2026:a6b488c3023091d3",
    "VM-D114": "candidate:SP-vision-multimodal-2026:1a72aa57c29bc267",
    "VM-D115": "candidate:SP-vision-multimodal-2026:bcd865fd3ef9f02b",
    "VM-D116": "candidate:SP-vision-multimodal-2026:a8ddfe446424a5d4",
    "VM-D117": "candidate:SP-vision-multimodal-2026:14b04c375155f8ba",
    "VM-D118": "candidate:SP-vision-multimodal-2026:1679e8fef59b1658",
    "VM-D119": "candidate:SP-vision-multimodal-2026:8a740dd7b6642284",
    "VM-D120": "candidate:SP-vision-multimodal-2026:3cea06c11283ca9e",
}

P13_PURPOSE_APPENDIX = (" Discrete language-like action tokens and continuous "
                        "flow-matching generation form a separate action-interface "
                        "branch within the same representation/interface contract.")

NEW_MUST_COVER = {
    "P06": ["DINOv3 Gram-anchored dense refinement as the self-distillation transition; "
            "SigLIP 2 staged alignment recipe as the alignment transition; "
            "AIMv2 autoregressive objective as supporting variant"],
    "P07A": ["SigLIP 2 staged recipe extends the image-level alignment lineage (supporting)"],
    "P07B": ["SigLIP 2 localization transfer and SAM 3 concept grounding extend open-vocabulary perception (supporting)"],
    "P09": ["SigLIP 2 encoder-reuse note extends the fusion encoder lineage (supporting)"],
    "P03": ["SAM 3 promptable concept segmentation as the late convergence transition"],
    "P11": ["SAM 3 memory video tracking as supporting stored-timeline evidence"],
    "P13": ["pi-zero flow-matching interface as the action-interface transition; "
            "FAST tokenization as the supporting representation transition"],
    "P12": ["UGround vision-only grounding interface and ScreenSpot-Pro professional evaluation as supporting endpoint evidence"],
}


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


def _place(pkg: dict, did: str, cid: str, kind: str, depth: str) -> None:
    key = "primary_candidate_ids" if kind == "PRIMARY" else "supporting_candidate_ids"
    assert cid not in pkg["primary_candidate_ids"] and cid not in pkg["supporting_candidate_ids"], cid
    pkg[key].append(cid)
    dc = pkg["publication_extensions"]["depth_classes"]
    for lst in dc.values():
        assert did not in lst, (pkg["package_id"], did)
    assert depth in dc, (pkg["package_id"], depth)
    dc[depth].append(did)


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("expected canonical State at SELECTION_COMPLETE")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        for p in (ledger_path, comp_path, matrix_path, sel_path):
            assert p.is_file(), p
        matrix = core.load_json(matrix_path)
        for did, cid in CID.items():
            rows = [r for r in matrix["rows"] if did in r["discovery_ids"]]
            assert len(rows) == 1 and rows[0]["candidate_id"] == cid, did
        sel = core.load_json(sel_path)
        assert len(sel["assignments"]) == 120

        arch = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
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

        _place(_package(arch, "P06"), "VM-D113", CID["VM-D113"], "PRIMARY", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P06"), "VM-D114", CID["VM-D114"], "PRIMARY", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P06"), "VM-D118", CID["VM-D118"], "SUPPORTING", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P03"), "VM-D115", CID["VM-D115"], "PRIMARY", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P13"), "VM-D116", CID["VM-D116"], "PRIMARY", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P13"), "VM-D117", CID["VM-D117"], "SUPPORTING", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P12"), "VM-D119", CID["VM-D119"], "SUPPORTING", "TRANSITION_NODE_TREATMENT")
        _place(_package(arch, "P12"), "VM-D120", CID["VM-D120"], "SUPPORTING", "TRANSITION_NODE_TREATMENT")
        # Ensure every placed candidate's CURRENT matrix remaining_boundaries is present
        # (validator-required; covers the 8 new cards' limitation texts).
        _mx_by_id = {r["candidate_id"]: r for r in matrix["rows"]}
        _ensured = 0
        for _pkg in arch["packages"]:
            _placed = [_mx_by_id[c] for c in (*_pkg.get("primary_candidate_ids", []), *_pkg.get("supporting_candidate_ids", [])) if c in _mx_by_id]
            for _t in sorted({x for _r in _placed for x in _r.get("remaining_boundaries", [])}):
                if _t not in _pkg["boundaries"]:
                    _pkg["boundaries"].append(_t)
                    _ensured += 1
        print("boundary ensure:", _ensured, "current matrix boundaries propagated")
        # P09 code-license bucket: include Qwen3-Omni alongside Qwen3-VL and Molmo 2
        # (§11: all three correctly included; VM-D075 code is canonical repo-bound).
        p09 = _package(arch, "P09")
        _old_code = next(b for b in p09["boundaries"] if b.startswith("Code licenses canonical:"))
        _new_code = ("Code licenses canonical: Qwen3-VL, Qwen3-Omni and Molmo 2 code Apache 2.0 "
                     "confirmed in canonical Evidence (repo-root LICENSE, repo-bound).")
        assert _old_code != _new_code
        p09["boundaries"] = [_new_code if b == _old_code else b for b in p09["boundaries"]]
        print("P09 code bucket: Qwen3-Omni included")
        p13 = _package(arch, "P13")
        assert P13_PURPOSE_APPENDIX not in p13["purpose"]
        p13["purpose"] = p13["purpose"] + P13_PURPOSE_APPENDIX
        for pid, reqs in NEW_MUST_COVER.items():
            pkg = _package(arch, pid)
            for req in reqs:
                assert req not in pkg["must_cover_requirements"]
                pkg["must_cover_requirements"].append(req)

        pe = arch["publication_extensions"]
        mmap = pe["p15_cross_package_synthesis_map"]
        assert len({i for v in mmap.values() for i in v}) == 39
        assert "p12_gui_computer_use" in mmap and "VM-D120" not in mmap["p12_gui_computer_use"]
        mmap["p12_gui_computer_use"].append("VM-D120")
        assert len({i for v in mmap.values() for i in v}) == 40
        assert "VM-D112" not in {i for v in mmap.values() for i in v}
        assert len(arch["packages"]) == 16

        blob = json.dumps(arch, ensure_ascii=False)
        assert "Something-Something V2" not in blob
        for did in CID:
            assert did in blob, did
        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, 8 placements, P15 map 40)")

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

        head_v2 = subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8")
        diff = "\n".join(difflib.unified_diff(
            head_v2.splitlines(), arch_path.read_text(encoding="utf-8").splitlines(),
            fromfile="architecture-v2.json@HEAD-pre-expansion",
            tofile="architecture-v2.json@fresh-120", n=1))
        (root / EDIR / "architecture-head-to-fresh-120.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-120.json"
        reviews_path = vdir / "architecture-stage-reviews-120.json"
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
            "evidence": ("Architecture stage-contract validation passed over 120-record canonical "
                         "authority (8 late-cutoff placements, skeleton preserved, P15 map 40). "
                         "Machine validation only; Sol Architecture review + Human decision owed; "
                         "nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture complete over 120-record canonical authority (8 placements, "
             "skeleton stable, P15 map 39+1). STOP at fresh pending Human Architecture Review; "
             "Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
        assert updated["human_gates"]["architecture_review"] == "pending", updated["human_gates"]
    print("lifecycle:", updated["lifecycle_state"], "| gates:", updated["human_gates"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
