#!/usr/bin/env python3
"""TS-003 replay Phase A: formal Screening (111) + advance to CANDIDATES_NORMALIZED.

- Canonical 111-record Discovery (untouched) -> fresh screening package.
- Decisions: 111 carried byte-identical decision objects from the r1 acceptance
  (same Discovery bytes; deterministic regeneration; Sol review owed).
- NO VM-D112 content anywhere in this run (staged artifacts read-only, untouched).
- Canonical accept_results -> screening/v2/accepted/<sha>/ (append-only).
- Advance DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED (advance_screening pattern).
- Frozen Core only. Post-gate adaptation (documented edition precedent):
  current_stage_basis_override + implementation_sha == current HEAD (state pin
  predates governed runs; all content validators run in full).
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
EDIR = f"{SRC}/execution/replay-current-111-to-r3-20261003"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
R1ACC = ("71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67")
R1DIR = f"{SRC}/screening/v2/accepted/{R1ACC}"
PKGDIR = f"{EDIR}/screening-package-111"
VALIDATION_REL = f"{EDIR}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "DISCOVERY_COLLECTED":
        raise ValueError("expected canonical State at DISCOVERY_COLLECTED")
    impl = core.repository_commit_sha(root)

    with agent_tool.current_stage_basis_override():
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL, root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 111, package["input"]

        carried = {}
        for res in sorted((root / R1DIR / "results").glob("batch-*.json")):
            for dec in core.load_json(res)["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 111 and not any(
            d["discovery_id"] == "VM-D112" for d in carried.values())

        results_dir = root / EDIR / "screening-results-111"
        results_dir.mkdir(parents=True, exist_ok=True)
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            assert len(ids) == b["record_count"]
            res = {"schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                   "batch_id": b["batch_id"],
                   "basis": screening.expected_result_basis(
                       Path("."), root / PKGDIR / "package.json", package, b),
                   "decisions": [carried[did] for did in ids]}
            core.write_json(results_dir / f"{b['batch_id']}.json", res)

        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 111
        print("screening acceptance:", acceptance_path.relative_to(root))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-111.json"
        reviews_path = vdir / "screening-stage-reviews-111.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Screening stage-contract validation passed over the replayed "
                         "111-record canonical acceptance (111 carried deterministic "
                         "decisions, no VM-D112). Machine validation only; Sol review owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening replay complete over canonical 111-record Discovery: "
             "111 carried decisions (103 KEEP / 3 MAYBE / 5 INSPECT / 0 DROP). "
             "VM-D112 remains staged, not canonical. Proceed to Evidence; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    print("screening acceptance sha:", core.sha256_file(acceptance_path)[:12])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
