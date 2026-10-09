#!/usr/bin/env python3
"""TS-003 screening replay (post-freeze integrity): 121 KEEP (+5 INSPECT/3 MAYBE carried)
+ VM-D122 DROP (temporal disqualification) + advance to CANDIDATES_NORMALIZED.

- Fresh screening package over canonical 122-record Discovery.
- Decisions: 121 carried byte-identical + D122 DROP with OUT_OF_WINDOW reason.
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
EDIR = f"{SRC}/execution/post-freeze-integrity-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/screening-package-122"
VALIDATION_REL = f"{EDIR}/validation"
PREV_ACC = "43c55814ecc09369e4ef283f7d0f21060d8c6756e93570c605d4b607a7b84831"

D122_DROP = {
    "discovery_id": "VM-D122",
    "decision": "DROP",
    "reason": ("OUT_OF_WINDOW temporal disqualification: first published 2026-09-30T08:05:32Z, "
               "after the exact cutoff 2026-09-30T00:31:34Z (OPEN_HISTORY_AS_OF, not calendar-day "
               "end). Authority-quality paper, but inadmissible for this edition; record retained "
               "as deferred/future-edition context."),
    "scope_tags": ["VM-O15"],
    "duplicate_group": None,
    "verification_targets": [],
    "confidence": "high",
}


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    impl = core.repository_commit_sha(root)
    assert screening.validate_decision(D122_DROP) == []

    with agent_tool.current_stage_basis_override():
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL, root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 122, package["input"]

        carried = {}
        r1dir = root / SRC / "screening/v2/accepted" / PREV_ACC / "results"
        for res in sorted(r1dir.glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                if dec["discovery_id"] == "VM-D122":
                    continue
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 121, len(carried)

        results_dir = root / EDIR / "screening-results-122"
        results_dir.mkdir(parents=True, exist_ok=True)
        total = 0
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            decs = [D122_DROP if did == "VM-D122" else carried[did] for did in ids]
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
        assert counts.get("DROP", 0) == 1

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
            "evidence": ("Screening stage-contract validation passed (121 carried + VM-D122 DROP "
                         "on OUT_OF_WINDOW temporal disqualification). Machine validation only."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete: 121 carried decisions + VM-D122 DROP (first published "
             "after the exact cutoff; deferred context). Proceed to Evidence."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
