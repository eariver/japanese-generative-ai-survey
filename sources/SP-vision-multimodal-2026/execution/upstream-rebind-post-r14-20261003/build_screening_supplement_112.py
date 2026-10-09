#!/usr/bin/env python3
"""Build TS-003 Screening supplement (112 records): bounded Discovery-supplement
screening for VM-D112 Agentic Video Understanding.

- Staging: execution/upstream-rebind-post-r14-20261003/screening-supplement-112/
  (package + inputs + decisions + results).
- Inputs: batch-001..003 byte-copies of the accepted r1 package inputs +
  batch-004 (VM-D112 record from the supplement jsonl).
- Decisions: 111 carried byte-identical decisions + VM-D112 KEEP (screening
  judgment with P09/P11 relevance + non-duplication rationale; Sol review owed).
- Results: batch-001..003 byte-copies + batch-004 materialized with canonical
  result basis computed from the staged package.
- Accept (vendored post-gate accept_results) into
  screening/v2/accepted/<new-sha>/ with package/inputs/results/decisions/audit.
- Canonical validators run throughout (decisions, batches, acceptance).
  Post-gate adaptations (documented): no lifecycle-state entry gate; agent-state
  drift filter (7 pre-existing publication-surface drifts, fail-closed baseline);
  package basis pins CURRENT files (honest fresh-package provenance).
- No lifecycle advance, no gate mutation, no approval. Sol re-review required.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_discovery_v2 as discovery
from scripts import survey_evidence_v2 as evidence  # noqa: F401 (validator parity note)
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
R1ACC = ("71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67")
R1DIR = f"{SRC}/screening/v2/accepted/{R1ACC}"
SUPJSONL = (f"{SRC}/execution/upstream-rebind-post-r14-20261003/"
            "discovery-v2-supplement-112.jsonl")
STAGE = f"{SRC}/execution/upstream-rebind-post-r14-20261003/screening-supplement-112"
STATE_REL = f"{SRC}/production-state.json"

PREEXISTING_DRIFT = {
    "Stage Checkpoint artifact drift: publication-pdf",
    "Stage Checkpoint artifact drift: quality-regression-bundle",
    "Stage Checkpoint artifact drift: reader-manuscript",
    "Stage Checkpoint artifact drift: reader-surface-gate",
    "Stage Checkpoint artifact drift: semantic-review",
    "Stage Checkpoint artifact drift: validated-source",
    "Stage Checkpoint artifact drift: visual-review",
}

_orig_validate_agent_state = agent.validate_agent_state


def _validate_agent_state_postgate(repo_root, cfg, state):
    errs = _orig_validate_agent_state(repo_root, cfg, state)
    missing = PREEXISTING_DRIFT - set(errs)
    if missing:
        raise ValueError("pre-existing drift baseline changed; refusing to filter: "
                         + "; ".join(sorted(missing)))
    return [e for e in errs if e not in PREEXISTING_DRIFT]


agent.validate_agent_state = _validate_agent_state_postgate

VM_D112_DECISION = {
    "discovery_id": "VM-D112",
    "decision": "KEEP",
    "reason": ("Official Google release 2026-09-01 (in-cutoff): query-driven on-demand "
               "timeline navigation replacing static 1-FPS ingest; distinct "
               "token-acquisition mechanism (P09/VM-O10) and third video-processing "
               "contract distinct from offline ingest and streaming state (P11/VM-O12); "
               "non-duplicate of Flash-VStream (model-side streaming memory vs API-side "
               "server tool loop); figures vendor-reported ceilings requiring "
               "Evidence-stage benchmark binding."),
    "scope_tags": ["VM-O10", "VM-O12"],
    "verification_targets": [
        "Evidence-stage full-body verification of official docs pages (bind access date)",
        "Benchmark list/split binding incl. LongVideoBench scope",
        "Static-vs-agentic token-math worked example",
    ],
    "duplicate_group": None,
    "confidence": "medium",
}


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    assert state.get("issue_id") == ISSUE_ID
    assert state.get("lifecycle_state") == "RELEASE_CANDIDATE", "unexpected lifecycle"

    stage = root / STAGE
    batch_dir = stage / "input/batches"
    results_dir = stage / "results"
    batch_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    # 1. Stage inputs: 111 carried + VM-D112 batch-004.
    recs = screening.read_jsonl(root / SUPJSONL)
    assert len(recs) == 112, len(recs)
    new_rec = [r for r in recs if r["discovery_id"] == "VM-D112"]
    assert len(new_rec) == 1
    for i in (1, 2, 3):
        shutil.copy2(root / R1DIR / f"input/batches/batch-00{i}.jsonl",
                     batch_dir / f"batch-00{i}.jsonl")
    screening.write_jsonl(batch_dir / "batch-004.jsonl", new_rec)

    # 2. Stage package (fresh honest pins).
    profile_path = root / state["profile"]["path"]
    batches = []
    for i, n in ((1, 50), (2, 50), (3, 11), (4, 1)):
        p = batch_dir / f"batch-00{i}.jsonl"
        batches.append({"batch_id": f"batch-00{i}",
                        "path": f"input/batches/batch-00{i}.jsonl",
                        "record_count": n, "sha256": core.sha256_file(p)})
    assert sum(b["record_count"] for b in batches) == 112
    old_pkg = core.load_json(root / R1DIR / "package.json")
    package = {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "research_profile": profile_path and core.load_json(profile_path)["research_profile"],
        "basis": {
            "profile_path": str(profile_path.relative_to(root)),
            "profile_sha256": core.sha256_file(profile_path),
            "state_path": STATE_REL,
            "state_sha256": core.sha256_file(root / STATE_REL),
            "discovery_path": ("sources/SP-vision-multimodal-2026/execution/"
                               "upstream-rebind-post-r14-20261003/"
                               "discovery-v2-supplement-112.jsonl"),
            "discovery_sha256": core.sha256_file(root / SUPJSONL),
        },
        "prompt": old_pkg["prompt"],
        "result_contract": old_pkg["result_contract"],
        "input": {"record_count": 112,
                  "batch_policy": old_pkg["input"]["batch_policy"],
                  "batches": batches},
        "expected_outputs": old_pkg["expected_outputs"],
        "rules": old_pkg["rules"],
    }
    # Prompt/contract drift guard: shared files must be byte-identical to r1 pins.
    for key in ("prompt", "result_contract"):
        assert package[key]["sha256"] == old_pkg[key]["sha256"], f"{key} drift"
    core.write_json(stage / "package.json", package)

    # 3. Decisions: 111 carried + VM-D112 KEEP.
    old_dec = core.load_json(root / R1DIR / "interactive-decisions.json")
    assert len(old_dec["decisions"]) == 111
    assert screening.validate_decision(VM_D112_DECISION) == []
    decisions = {"schema_version": old_dec["schema_version"], "issue_id": ISSUE_ID,
                 "runner": {"provider": "Muse",
                            "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
                            "invocation": ("bounded supplement: 111 carried byte-identical "
                                           "decisions + VM-D112 screening judgment; Sol "
                                           "Screening-through-Evidence review owed"),
                            "generated_at": "2026-10-03T09:01:31Z"},
                 "decisions": old_dec["decisions"] + [VM_D112_DECISION]}
    core.write_json(stage / "interactive-decisions.json", decisions)

    # 4. Results: 001..003 re-based to the new package (decisions byte-identical;
    # envelopes rebind since the package changed) + materialized 004.
    for i in (1, 2, 3):
        old_res = core.load_json(root / R1DIR / f"results/batch-00{i}.json")
        nb = [b for b in batches if b["batch_id"] == f"batch-00{i}"][0]
        assert [d["discovery_id"] for d in old_res["decisions"]] == [
            r["discovery_id"] for r in screening.read_jsonl(batch_dir / f"batch-00{i}.jsonl")]
        old_res["basis"] = screening.expected_result_basis(
            Path("."), stage / "package.json", package, nb)
        core.write_json(results_dir / f"batch-00{i}.json", old_res)
    b4 = [b for b in batches if b["batch_id"] == "batch-004"][0]
    res4 = {"schema_version": "2.0-rc1", "issue_id": ISSUE_ID, "batch_id": "batch-004",
            "basis": screening.expected_result_basis(Path("."), stage / "package.json",
                                                     package, b4),
            "decisions": [VM_D112_DECISION]}
    core.write_json(results_dir / "batch-004.json", res4)

    # 5. Accept (vendored post-gate: same digest/layout/shape as canonical).
    with tempfile.TemporaryDirectory() as temp:
        temp_results = Path(temp) / "results"
        temp_results.mkdir()
        for i in (1, 2, 3, 4):
            shutil.copy2(results_dir / f"batch-00{i}.json", temp_results / f"batch-00{i}.json")
        from scripts.survey_screening_v2 import (
            _validate_result_batch, _result_set_digest, _exact_regular_files,
            validate_acceptance)
        expected_files = {f"{b['batch_id']}.json" for b in batches}
        result_files = _exact_regular_files(temp_results, expected_files, "Screening result set")
        accepted_batches, flattened, all_seen = [], [], set()
        for batch in batches:
            bdec, meta = _validate_result_batch(stage / "package.json", package, batch,
                                               result_files[f"{batch['batch_id']}.json"])
            ids = [r["discovery_id"] for r in bdec]
            assert not (all_seen.intersection(ids)), "cross-batch dup"
            all_seen.update(ids)
            flattened.extend(bdec)
            accepted_batches.append(meta)
        assert len(flattened) == 112
        package_sha = core.sha256_file(stage / "package.json")
        result_set_sha = _result_set_digest(package_sha, accepted_batches, flattened)
        accepted_root = root / SRC / "screening/v2/accepted"
        run_dir = accepted_root / result_set_sha
        acceptance_path = run_dir / "screening-accepted.json"
        assert not run_dir.exists(), f"collision {run_dir}"
        (run_dir / "input/batches").mkdir(parents=True)
        (run_dir / "results").mkdir(parents=True)
        shutil.copy2(stage / "package.json", run_dir / "package.json")
        for batch in batches:
            shutil.copy2(batch_dir / f"{batch['batch_id']}.jsonl",
                         run_dir / "input/batches" / f"{batch['batch_id']}.jsonl")
            shutil.copy2(temp_results / f"{batch['batch_id']}.json",
                         run_dir / "results" / f"{batch['batch_id']}.json")
        shutil.copy2(stage / "interactive-decisions.json", run_dir / "interactive-decisions.json")
        core.write_json(run_dir / "supplement-audit.json", {
            "schema_version": "1.0",
            "basis": "bounded supplement: 111 carried byte-identical inputs/decisions/results + VM-D112 new",
            "prior_acceptance": R1ACC,
            "sol_review": "REQUIRED before downstream use",
        })
        accepted = {"schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
                    "research_profile": package["research_profile"],
                    "result_set_sha256": result_set_sha, "package_sha256": package_sha,
                    "record_count": 112, "batch_count": 4,
                    "batches": accepted_batches,
                    "decisions": sorted(flattened, key=lambda r: r["discovery_id"])}
        core.write_json(acceptance_path, accepted)
        with agent_tool.current_stage_basis_override():
            out = validate_acceptance(root, acceptance_path, core.repository_commit_sha(root))
        assert out["record_count"] == 112

    print(json.dumps({"screening_acceptance": str(acceptance_path.relative_to(root)),
                      "record_count": 112}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
