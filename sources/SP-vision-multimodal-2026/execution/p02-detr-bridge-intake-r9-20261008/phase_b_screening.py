#!/usr/bin/env python3
"""TS-003 Phase B (P02 bounded bridge intake): Screening (125) + advance to
CANDIDATES_NORMALIZED.

- Decisions: 122 carried byte-identical + VM-D123/VM-D124/VM-D125 KEEP (genuinely
  evaluated: pre-cutoff primaries, VM-O02 materiality, non-duplicate, bounded
  bridge roles per DINO's explicit build-on statement).
- Canonical accept + advance. Frozen Core only.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/screening-package-125"
VALIDATION_REL = f"{EDIR}/validation"

NEW_DECISIONS = [
    {"discovery_id": "VM-D123", "decision": "KEEP",
     "reason": ("Deformable DETR (ICLR 2021 Oral, pre-cutoff primary): DETR slow-convergence / "
                "limited-resolution motivation; deformable attention over a small sampling set "
                "around a reference point; multi-scale handling without FPN; 10x fewer epochs "
                "with better small-object behavior. DINO explicitly builds on this branch. "
                "Bounded P02 transition node; not a general deformable-attention survey."),
     "scope_tags": ["VM-O02"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (motivation/mechanism/convergence/small-object)"],
     "confidence": "high"},
    {"discovery_id": "VM-D124", "decision": "KEEP",
     "reason": ("DAB-DETR (ICLR 2022, pre-cutoff primary): 4D box-coordinate queries with "
                "layer-by-layer dynamic anchor updates and explicit positional priors; soft "
                "ROI-pooling cascade reading; 45.7 AP R50-DC5 at 50 epochs. DINO explicitly "
                "formulates queries this way. Brief supporting treatment only; no Anchor/ "
                "Conditional DETR taxonomy expansion."),
     "scope_tags": ["VM-O02"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (query formulation/updates/results)"],
     "confidence": "high"},
    {"discovery_id": "VM-D125", "decision": "KEEP",
     "reason": ("DN-DETR (CVPR 2022 Oral, pre-cutoff primary): bipartite-matching instability "
                "diagnosis; noised GT boxes/labels reconstructed via a denoising decoder part; "
                "built on DAB-DETR 4D anchors; +1.9 AP over DAB-DETR with parity at ~50% epochs; "
                "also applied to Deformable DETR. DINO explicitly builds on this branch. "
                "Query-denoising training only, not diffusion denoising."),
     "scope_tags": ["VM-O02"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification (instability diagnosis/mechanism/DAB-based results/generality)"],
     "confidence": "high"},
]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    impl = core.repository_commit_sha(root)
    for dec in NEW_DECISIONS:
        assert screening.validate_decision(dec) == [], dec["discovery_id"]
    by_new = {d["discovery_id"]: d for d in NEW_DECISIONS}

    with agent_tool.current_stage_basis_override():
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL, root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 125, package["input"]

        carried = {}
        prev_dirs = sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                           key=lambda p: p.stat().st_mtime)
        prev = None
        for cand in prev_dirs:
            if core.load_json(cand)["record_count"] == 122:
                prev = cand  # newest wins (no break): r8-era DROP-carrying basis, not stale KEEP one
        assert prev is not None
        _prev_check = core.load_json(prev)
        _prev_dec = {d["discovery_id"]: d["decision"] for d in _prev_check["decisions"]}
        assert _prev_dec.get("VM-D122") == "DROP", "carry basis must be the current DROP-carrying 122-acceptance"
        for res in sorted((prev.parent / "results").glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 122 and not any(d in carried for d in by_new)

        results_dir = root / EDIR / "screening-results-125"
        results_dir.mkdir(parents=True, exist_ok=True)
        total = 0
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            decs = [by_new[did] if did in by_new else carried[did] for did in ids]
            total += len(decs)
            core.write_json(results_dir / f"{b['batch_id']}.json", {
                "schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                "batch_id": b["batch_id"],
                "basis": screening.expected_result_basis(
                    Path("."), root / PKGDIR / "package.json", package, b),
                "decisions": decs})
        assert total == 125, total

        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 125
        counts = {}
        for d in acceptance["decisions"]:
            counts[d["decision"]] = counts.get(d["decision"], 0) + 1
        print("screening acceptance:", acceptance_path.relative_to(root), counts)

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-125.json"
        reviews_path = vdir / "screening-stage-reviews-125.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Screening stage-contract validation passed over canonical 125-record "
                         "acceptance (122 carried + VM-D123/VM-D124/VM-D125 KEEP). Machine validation only."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete over 125-record Discovery (122 carried + 3 P02 bridge KEEP). "
             "Proceed to Evidence."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
