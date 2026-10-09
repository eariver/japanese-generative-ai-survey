#!/usr/bin/env python3
"""TS-003 Phase B (r3 re-entry): formal Screening (112) + advance to CANDIDATES_NORMALIZED.

- Fresh screening package over canonical 112-record Discovery.
- Decisions: 111 carried byte-identical objects + VM-D112 formal evaluation.
  VM-D112 verdict KEEP is NOT forced: it answers each §8 question genuinely —
  cutoff ✓ (2026-09-01 within 2026-09-30, official sources verified read-only);
  TS-003 relevance ✓; P09 token-acquisition-economics materiality ✓ (fixed
  1-FPS ingest → query-driven selective acquisition changes token acquisition,
  processing strategy, and economics); P11 third-contract materiality ✓
  (stored-timeline on-demand navigation distinct from offline full-context AND
  streaming stateful processing); non-duplicate vs Flash-VStream ✓ (model-side
  streaming memory vs API-side acquisition loop); vendor-ceiling boundaries ✓.
- Canonical accept + advance (advance_screening pattern). Frozen Core only +
  documented post-gate adaptation. Sol review owed.
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
EDIR = f"{SRC}/execution/architecture-r3-intake-20261003"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
R1ACC = ("71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67")
R1DIR = f"{SRC}/screening/v2/accepted/{R1ACC}"
PKGDIR = f"{EDIR}/screening-package-112"
VALIDATION_REL = f"{EDIR}/validation"

VM_D112_DECISION = {
    "discovery_id": "VM-D112",
    "decision": "KEEP",
    "reason": ("Official Google release 2026-09-01 (in-cutoff; static 1-FPS ingest "
               "vs query-driven on-demand timeline navigation verified against "
               "official blog + docs 2026-10-03): distinct token-acquisition "
               "mechanism material to P09 context/token economics (fixed-rate "
               "tokenization → selective acquisition changes acquisition, strategy, "
               "economics) and a third video-processing contract material to P11 "
               "(stored-timeline navigation distinct from offline full-video context "
               "and streaming stateful processing); non-duplicate of Flash-VStream "
               "(model-side streaming memory vs API-side acquisition loop); figures "
               "vendor-reported ceilings requiring Evidence-stage benchmark binding."),
    "scope_tags": ["VM-O10", "VM-O12"],
    "duplicate_group": None,
    "verification_targets": [
        "Evidence-stage full-body verification of official docs pages (bind access date)",
        "Benchmark list/split binding incl. LongVideoBench scope",
        "Static-vs-agentic token-math worked example",
    ],
    "confidence": "medium",
}


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    impl = core.repository_commit_sha(root)
    assert screening.validate_decision(VM_D112_DECISION) == []

    with agent_tool.current_stage_basis_override():
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL, root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 112, package["input"]

        carried = {}
        for res in sorted((root / R1DIR / "results").glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 111 and "VM-D112" not in carried

        results_dir = root / EDIR / "screening-results-112"
        results_dir.mkdir(parents=True, exist_ok=True)
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            decs = [VM_D112_DECISION if did == "VM-D112" else carried[did] for did in ids]
            core.write_json(results_dir / f"{b['batch_id']}.json", {
                "schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                "batch_id": b["batch_id"],
                "basis": screening.expected_result_basis(
                    Path("."), root / PKGDIR / "package.json", package, b),
                "decisions": decs})

        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 112
        counts = {}
        for d in acceptance["decisions"]:
            counts[d["decision"]] = counts.get(d["decision"], 0) + 1
        print("screening acceptance:", acceptance_path.relative_to(root), counts)

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-112.json"
        reviews_path = vdir / "screening-stage-reviews-112.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Screening stage-contract validation passed over canonical "
                         "112-record acceptance (111 carried + VM-D112 KEEP per formal "
                         "§8 evaluation). Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete over 112-record canonical Discovery (111 carried "
             "+ VM-D112 KEEP: in-cutoff official release, P09/P11 material, "
             "non-duplicate, vendor ceilings). Proceed to Evidence; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
