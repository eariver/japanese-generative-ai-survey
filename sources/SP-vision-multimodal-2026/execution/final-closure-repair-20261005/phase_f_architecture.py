#!/usr/bin/env python3
"""TS-003 Phase F (final closure): Architecture (122) + advance to ARCHITECTURE_ESTABLISHED.

- Content base: HEAD-committed architecture (all prior repairs) + targeted additions:
  P14: VM-D121 PRIMARY+TRANSITION (JEPA intra-pole transition) + JEPA-pole must_cover
  distinction + VM-D122 control-use synthesis direction (no placement: single-kind rule).
  P15: VM-D122 PRIMARY+FULL (second methodology anchor) + planning-limits must_cover.
- Boundaries: ensure CURRENT matrix remaining_boundaries for all placed candidates.
- P15 map: UNCHANGED (VM-D122 placed, not cross-consumed; old 40 kept, no maximization).
- 16 packages, placements otherwise untouched. Status PROPOSED, null review.
- Fresh summaries + validation + checkpoint + advance. STOP THERE. Frozen Core only.
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
EDIR = f"{SRC}/execution/final-closure-repair-20261005"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

CID121 = None  # resolved from the replayed matrix at runtime
CID122 = None

P14_JEPA_LINE = ("JEPA pole intra-pole transition: V-JEPA action-free predictive representation vs "
                 "V-JEPA 2 / 2-AC action-free pretraining plus action-conditioned latent world-model "
                 "post-training and planning use; four-pole taxonomy unchanged.")
P14_D122_LINE = ("Planning-limits evidence as control-use limitation synthesis (P15 methodology home): "
                 "usable planning horizon bounds, not a transferable benchmark; G02 preserved.")
P15_D122_LINE = ("Planning-limits evaluation discipline as second methodology anchor: plannable-range "
                 "metric, horizon/scaling/perfect-prediction limits, imagination/MPC/subgoal matrix.")


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


def _place(pkg: dict, cid: str, kind: str) -> None:
    key = "primary_candidate_ids" if kind == "PRIMARY" else "supporting_candidate_ids"
    assert cid not in pkg["primary_candidate_ids"] and cid not in pkg["supporting_candidate_ids"], cid
    pkg[key].append(cid)


def _depth(pkg: dict, did: str, depth: str) -> None:
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
        rows121 = [r for r in matrix["rows"] if "VM-D121" in r["discovery_ids"]]
        rows122 = [r for r in matrix["rows"] if "VM-D122" in r["discovery_ids"]]
        assert len(rows121) == 1 and len(rows122) == 1, (rows121, rows122)
        globals()["CID121"], globals()["CID122"] = rows121[0]["candidate_id"], rows122[0]["candidate_id"]

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

        p14 = _package(arch, "P14")
        _place(p14, CID121, "PRIMARY"); _depth(p14, "VM-D121", "TRANSITION_NODE_TREATMENT")
        for line in (P14_JEPA_LINE, P14_D122_LINE):
            assert line not in p14["must_cover_requirements"]
            p14["must_cover_requirements"].append(line)

        p15 = _package(arch, "P15")
        _place(p15, CID122, "PRIMARY"); _depth(p15, "VM-D122", "FULL_MECHANISM_TREATMENT")
        assert P15_D122_LINE not in p15["must_cover_requirements"]
        p15["must_cover_requirements"].append(P15_D122_LINE)

        # Ensure CURRENT matrix remaining_boundaries for all placed candidates.
        mx_by_id = {r["candidate_id"]: r for r in matrix["rows"]}
        ensured = 0
        for pkg in arch["packages"]:
            placed = [mx_by_id[c] for c in
                      (*pkg.get("primary_candidate_ids", []), *pkg.get("supporting_candidate_ids", []))
                      if c in mx_by_id]
            for t in sorted({x for r in placed for x in r.get("remaining_boundaries", [])}):
                if t not in pkg["boundaries"]:
                    pkg["boundaries"].append(t)
                    ensured += 1
        print("boundary ensure:", ensured)

        pe = arch["publication_extensions"]
        mmap = pe["p15_cross_package_synthesis_map"]
        assert len({i for v in mmap.values() for i in v}) == 40, "P15 map must stay 40 (no additions)"
        assert "VM-D112" not in {i for v in mmap.values() for i in v}
        assert len(arch["packages"]) == 16

        blob = json.dumps(arch, ensure_ascii=False)
        assert "Something-Something V2" not in blob
        for did in ("VM-D121", "VM-D122"):
            assert did in blob, did
        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 recreated (PROPOSED, P14/P15 integration, map 40)")

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
            fromfile="architecture-v2.json@HEAD-pre-repair",
            tofile="architecture-v2.json@fresh-122", n=1))
        (root / EDIR / "architecture-head-to-fresh-122.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-122.json"
        reviews_path = vdir / "architecture-stage-reviews-122.json"
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
            "evidence": ("Architecture stage-contract validation passed over 122-record canonical "
                         "authority (P14/P15 integration, skeleton preserved, map 40). Machine "
                         "validation only; Sol review + Human decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture complete over 122-record canonical authority (P14 intra-pole "
             "transition, P15 methodology anchor, skeleton stable). STOP at fresh pending Human "
             "Architecture Review; Sol review owed."),
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
