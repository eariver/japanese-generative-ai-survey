#!/usr/bin/env python3
"""TS-003 replay step 4 (exception-authorized): Architecture (112) + advance to
ARCHITECTURE_ESTABLISHED. STOP — no approval, no gate decision.

- Content base: architecture-v4.json (surviving proposal) + r4 transformations
  (P02 DETR cost/loss boundary; VM-D112 SUPPORTING dual-placed P09+P11 with
  boundaries + depth classes; must_cover requirements) + refreshed basis.
- Status PROPOSED, human_review null. Fresh architecture-v2.json +
  review-summary-v2 + attention-v2, canonical validate, advance
  SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED. STOP THERE.
- Expected semantic diff vs r4-approved v2: basis-hash rebinding ONLY.
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
EDIR = f"{SRC}/execution/evidence-correction-r5-20261004"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

V4_REL = f"{SRC}/architecture-v4.json"
VM112_CANDIDATE_ID = "candidate:SP-vision-multimodal-2026:69b72bb7fcd308ec"
P02_DETR_BOUNDARY = ("Matching cost (assignment) vs matched-pair training loss kept "
                     "distinct; auxiliary decoder losses are standard-recipe, never "
                     "architecture-mandatory.")
P09_MUST_COVER = ("Query-driven selective acquisition economics axis via VM-D112 "
                  "(vendor ceilings, version-bound; token scope only)")
P11_MUST_COVER = ("Third video-processing contract (stored-timeline on-demand "
                  "navigation) via VM-D112; offline breadth vs online state columns unchanged")


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
        v4 = core.load_json(root / V4_REL)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        for p in (ledger_path, comp_path, matrix_path, sel_path):
            assert p.is_file(), p

        matrix = core.load_json(matrix_path)
        vm112_rows = [r for r in matrix["rows"] if "VM-D112" in r["discovery_ids"]]
        assert len(vm112_rows) == 1 and vm112_rows[0]["candidate_id"] == VM112_CANDIDATE_ID
        vm112_boundaries = list(vm112_rows[0]["remaining_boundaries"])
        assert len(vm112_boundaries) == 3, vm112_boundaries

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
        p02 = _package(arch, "P02")
        assert P02_DETR_BOUNDARY not in p02["boundaries"]
        p02["boundaries"].append(P02_DETR_BOUNDARY)

        for pid, must_cover in (("P09", P09_MUST_COVER), ("P11", P11_MUST_COVER)):
            pkg = _package(arch, pid)
            assert VM112_CANDIDATE_ID not in pkg["primary_candidate_ids"]
            assert VM112_CANDIDATE_ID not in pkg["supporting_candidate_ids"]
            pkg["supporting_candidate_ids"].append(VM112_CANDIDATE_ID)
            for boundary in vm112_boundaries:
                assert boundary not in pkg["boundaries"]
                pkg["boundaries"].append(boundary)
            assert must_cover not in pkg["must_cover_requirements"]
            pkg["must_cover_requirements"].append(must_cover)
            depth = pkg["publication_extensions"]["depth_classes"]
            assert "VM-D112" not in depth["TRANSITION_NODE_TREATMENT"]
            depth["TRANSITION_NODE_TREATMENT"].append("VM-D112")

        # Corrected-Evidence limitation propagation (deterministic, validator-required):
        # packages placing a corrected candidate must carry its CURRENT limitation texts.
        # Only limitation texts that actually changed are swapped (old text superseded).
        old_acc = "33ec63cbd5bbe776fb106f57fa64ca448061dfe92cbbfe3684848ddb17010b69"
        new_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        new_acceptance = core.load_json(new_acc)
        new_by_task = {r["evidence_task_id"]: r for r in new_acceptance["results"]}
        swaps = []
        for row in matrix["rows"]:
            tid = row["evidence_task_id"]
            meta = new_by_task[tid]
            new_card = core.load_json(new_acc.parent / "results" / meta["filename"])
            old_card = core.load_json(
                root / SRC / "evidence/v2/accepted" / old_acc / "results" / meta["filename"])
            old_lims = {l["text"] for l in old_card.get("limitations", [])}
            new_lims = {l["text"] for l in new_card.get("limitations", [])}
            gone, fresh = old_lims - new_lims, new_lims - old_lims
            if gone or fresh:
                assert len(gone) == 1 and len(fresh) == 1, (tid, gone, fresh)
                swaps.append((tid, next(iter(gone)), next(iter(fresh))))
        assert len(swaps) == 2, swaps
        for tid, old_text, new_text in swaps:
            placed = False
            for pkg in arch["packages"]:
                if tid in [row["evidence_task_id"] for row in matrix["rows"]
                           if row["candidate_id"] in (*pkg.get("primary_candidate_ids", []),
                                                       *pkg.get("supporting_candidate_ids", []))]:
                    if old_text in pkg["boundaries"]:
                        pkg["boundaries"] = [new_text if b == old_text else b
                                             for b in pkg["boundaries"]]
                        placed = True
            assert placed, tid
        print("limitation swaps:", [(s[0][-12:], len(s[1]), len(s[2])) for s in swaps])

        # P15 39-authority map + skeleton invariants
        pe = arch["publication_extensions"]
        assert "p15_cross_package_synthesis_map" in pe
        mmap = pe["p15_cross_package_synthesis_map"]
        assert len({i for v in mmap.values() for i in v}) == 39
        assert "VM-D112" not in {i for v in mmap.values() for i in v}
        assert len(arch["packages"]) == 16

        blob = json.dumps(arch, ensure_ascii=False)
        assert "VM-D112" in blob and VM112_CANDIDATE_ID in blob
        assert "Something-Something V2" not in blob
        assert "SIMA-agent training use" not in blob
        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, VM-D112 bound P09+P11, map 39)")

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

        # Semantic diff vs r4-approved v2 (HEAD-committed): basis rebinding ONLY expected
        head_v2 = subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8")
        old_lines = head_v2.splitlines()
        new_lines = arch_path.read_text(encoding="utf-8").splitlines()
        diff = "\n".join(difflib.unified_diff(old_lines, new_lines,
                                              fromfile="architecture-v2.json@r4-approved",
                                              tofile="architecture-v2.json@fresh", n=1))
        (root / EDIR / "architecture-r4-to-fresh.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-112.json"
        reviews_path = vdir / "architecture-stage-reviews-112.json"
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
            "evidence": ("Architecture stage-contract validation passed over replayed 112-record "
                         "canonical authority (fresh Architecture bound to replayed chain, "
                         "VM-D112 SUPPORTING dual-placed P09+P11, P02 cost/loss requirement "
                         "carried, P15 39-map preserved). Machine validation only; Sol Architecture "
                         "review + Human decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture replayed over 112-record canonical authority (skeleton "
             "stable, P02 cost/loss requirement carried, VM-D112 admitted SUPPORTING in "
             "P09+P11, P15 39-map preserved). STOP at fresh pending Human Architecture "
             "Review r5; Sol review + Human decision owed."),
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
