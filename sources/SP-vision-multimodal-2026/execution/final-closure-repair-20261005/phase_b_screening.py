#!/usr/bin/env python3
"""TS-003 Phase B (final closure): Screening (122) + advance to CANDIDATES_NORMALIZED.

- Decisions: 120 carried byte-identical + VM-D121/VM-D122 KEEP (genuinely evaluated:
  pre-cutoff primaries, obligation materiality, non-duplicate, vendor boundaries).
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
EDIR = f"{SRC}/execution/final-closure-repair-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/screening-package-122"
VALIDATION_REL = f"{EDIR}/validation"

NEW_DECISIONS = [
    {"discovery_id": "VM-D121", "decision": "KEEP",
     "reason": ("Meta V-JEPA 2/2-AC 2025-06-11 (pre-cutoff paper + blog + code): one two-stage "
                "contract of action-free JEPA pretraining plus action-conditioned latent predictor "
                "with MPC planning; P14 intra-pole transition (predictive pole, not a new taxonomy); "
                "non-duplicate of action-free V-JEPA; prior defer recorded as false-negative."),
     "scope_tags": ["VM-O15"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (two-stage contract/numbers)"],
     "confidence": "high"},
    {"discovery_id": "VM-D122", "decision": "KEEP",
     "reason": ("Planning Limits paper 2026-09-30 (cutoff-day primary): cross-backbone planning-range "
                "evidence bounding control-oriented world-model claims; methodology/evaluation authority "
                "for P15/P14; bounds stronger absence claims without resolving G02."),
     "scope_tags": ["VM-O15"], "duplicate_group": None,
     "verification_targets": ["Evidence-stage full-body verification of arXiv HTML (metric/matrix/limits)"],
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
        assert package["input"]["record_count"] == 122, package["input"]

        carried = {}
        prev_dirs = sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                           key=lambda p: p.stat().st_mtime)
        prev = None
        for cand in prev_dirs:
            if core.load_json(cand)["record_count"] == 120:
                prev = cand
        assert prev is not None
        for res in sorted((prev.parent / "results").glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 120 and not any(d in carried for d in by_new)

        results_dir = root / EDIR / "screening-results-122"
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
        assert total == 122, total

        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 122
        counts = {}
        for d in acceptance["decisions"]:
            counts[d["decision"]] = counts.get(d["decision"], 0) + 1
        print("screening acceptance:", acceptance_path.relative_to(root), counts)

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-122.json"
        reviews_path = vdir / "screening-stage-reviews-122.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Screening stage-contract validation passed over canonical 122-record "
                         "acceptance (120 carried + VM-D121/VM-D122 KEEP). Machine validation only."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete over 122-record Discovery (120 carried + 2 KEEP). "
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
