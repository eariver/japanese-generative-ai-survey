#!/usr/bin/env python3
"""TS-003 formal Screening (112 records) under Human-gated re-entry.

- New screening package via canonical prepare_package (state DISCOVERY_COLLECTED).
- Decisions: 111 carried byte-identical decision objects from the r1 acceptance
  results + VM-D112 KEEP (genuine §9 evaluation recorded in the turn record:
  cutoff/relevance/P09+P11 materiality/distinctness/authority/boundaries all pass).
- Results materialized with canonical basis; accepted via canonical
  accept_results into screening/v2/accepted/<sha>/ (content-addressed, append-only).
- Advances DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED (advance_screening pattern).
- Frozen Core only. Post-gate adaptation (documented, edition precedent):
  current_stage_basis_override + implementation_sha == current HEAD, because the
  state's pinned implementation SHA predates this governed run; all content
  validators run in full. Sol re-review owed on all judgments.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/vm-d112-formal-intake-20261003"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
R1ACC = ("71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67")
R1DIR = f"{SRC}/screening/v2/accepted/{R1ACC}"
PKGDIR = f"{EDIR}/screening-package-112"
VALIDATION_REL = f"{EDIR}/validation"

VM_D112_DECISION = {
    "discovery_id": "VM-D112",
    "decision": "KEEP",
    "reason": ("Official Google release 2026-09-01 (in-cutoff, verified against "
               "official blog + docs 2026-10-03): query-driven on-demand timeline "
               "navigation replacing static 1-FPS ingest; distinct token-acquisition "
               "mechanism (P09/VM-O10) and third video-processing contract distinct "
               "from offline ingest and streaming state (P11/VM-O12); non-duplicate "
               "of Flash-VStream (model-side streaming memory vs API-side server "
               "tool loop); figures vendor-reported ceilings requiring "
               "Evidence-stage benchmark binding."),
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
        # 1. Fresh screening package over canonical 112-record Discovery.
        pkg_path = screening.prepare_package(
            root, root / STATE_REL, root / DISC_REL,
            root / PKGDIR, impl)
        package = core.load_json(pkg_path)
        assert package["input"]["record_count"] == 112, package["input"]
        batches = {b["batch_id"]: b for b in package["input"]["batches"]}
        print("batches:", {k: v["record_count"] for k, v in batches.items()})

        # 2. Decisions: carried 111 + VM-D112.
        carried = {}
        for i in (1, 2, 3):
            res = core.load_json(root / R1DIR / f"results/batch-00{i}.json")
            for dec in res["decisions"]:
                assert dec["discovery_id"] not in carried
                carried[dec["discovery_id"]] = dec
        assert len(carried) == 111 and "VM-D112" not in carried
        by_batch = {}
        for b in package["input"]["batches"]:
            recs = screening.read_jsonl(root / PKGDIR / b["path"])
            ids = [r["discovery_id"] for r in recs]
            decs = []
            for did in ids:
                if did == "VM-D112":
                    decs.append(VM_D112_DECISION)
                else:
                    decs.append(carried[did])
            by_batch[b["batch_id"]] = (b, decs)

        # 3. Materialize results with canonical basis.
        results_dir = root / EDIR / "screening-results-112"
        results_dir.mkdir(parents=True, exist_ok=True)
        for bid, (b, decs) in by_batch.items():
            res = {"schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                   "batch_id": bid,
                   "basis": screening.expected_result_basis(
                       Path("."), root / PKGDIR / "package.json", package, b),
                   "decisions": decs}
            core.write_json(results_dir / f"{bid}.json", res)

        # 4. Accept (canonical, content-addressed).
        acceptance_path = screening.accept_results(
            root, root / PKGDIR / "package.json", results_dir,
            root / f"{SRC}/screening/v2/accepted", impl)
        acceptance = screening.validate_acceptance(root, acceptance_path, impl)
        assert acceptance["record_count"] == 112
        print("screening acceptance:", acceptance_path.relative_to(root))
        print("result_set:", acceptance["result_set_sha256"][:12])

        # 5. Advance to CANDIDATES_NORMALIZED (advance_screening pattern).
        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "screening-stage-validation-112.json"
        reviews_path = vdir / "screening-stage-reviews-112.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": ("Current Core Screening stage-contract validation passed over the "
                         "112-record canonical Screening acceptance (111 carried decisions + "
                         "VM-D112 KEEP per genuine §9 evaluation). Machine validation only; "
                         "Sol Screening-through-Evidence review owed before Evidence use."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"screening-acceptance": acceptance_path}, reviews_path,
            ("TS-003 Screening complete over 112-record canonical Discovery (111 BASE + "
             "VM-D112 GAP_FILL): 111 carried decisions + VM-D112 KEEP (official 2026-09-01 "
             "release, query-driven acquisition transition, third video-processing contract, "
             "non-duplicate of Flash-VStream, vendor ceilings). Proceed to Evidence; Sol "
             "Screening-through-Evidence review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "CANDIDATES_NORMALIZED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    print("checkpoint:", str(generated.relative_to(root)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
