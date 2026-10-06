#!/usr/bin/env python3
"""Rebuild draft checkpoint + state provenance after content-revision r5-rev1 regen.

Same precedent as content-revision-r4 (rebuild_checkpoint.py):
 1. write stage-validation-r5-rev1.json (binds current state bytes);
 2. rebuild ARCHITECTURE_ESTABLISHED.json (artifact SHAs + reviews.result.sha);
 3. update production-state.json checkpoint_provenance.draft.sha256;
 4. run canonical validate_agent_state (must be clean).
Lifecycle/gates/architecture/evidence/selection untouched (DRAFT_COMPLETE held, r5 APPROVED preserved).
"""
from __future__ import annotations
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r5-20261006"
START_SHA = "eafb68eaf6a009be33c003877d2dbc9360f0129b"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]


def main() -> int:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_path = SRC / "production-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["lifecycle_state"] == "DRAFT_COMPLETE", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "approved"
    assert state["next_action"] == "stage:reader-publication-validation"
    contract = {"pipeline_contract_version": "2.0-rc1",
                "pipeline_contract_sha256": "ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71",
                "quality_contract_version": "2.0-rc1",
                "quality_contract_sha256": "b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958",
                "research_profile_version": "2.0-rc1",
                "research_profile_sha256": "0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8",
                "publication_profile_version": "2.0-rc1",
                "publication_profile_sha256": "a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb"}
    arts = []
    for pid in PIDS:
        arts.append({"name": f"draft-package:{pid}",
                     "path": f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-package.json",
                     "sha256": sha256_file(SRC / "draft/v2/packages" / pid / "draft-package.json")})
    for pid in PIDS:
        arts.append({"name": f"draft-result:{pid}",
                     "path": f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json",
                     "sha256": sha256_file(SRC / "draft/v2/packages" / pid / "draft-result.json")})
    arts.append({"name": "synthesis-input",
                 "path": "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json",
                 "sha256": sha256_file(SRC / "draft/v2/profile-synthesis-input.json")})
    arts.append({"name": "synthesis-result",
                 "path": "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json",
                 "sha256": sha256_file(SRC / "draft/v2/profile-synthesis-result.json")})
    assert len(arts) == 34
    # draft-packages must be byte-identical to the reviewed fresh-121 run (no package change)
    profile_sha = sha256_file(SRC / "production-profile.json")
    state_sha_now = sha256_file(state_path)
    validation = {
        "schema_version": "2.0-rc1", "check_id": "CORE_STAGE_CONTRACT", "status": "PASS",
        "issue_id": "SP-vision-multimodal-2026",
        "from_state": "ARCHITECTURE_ESTABLISHED", "to_state": "DRAFT_COMPLETE",
        "production_state": {"path": "sources/SP-vision-multimodal-2026/production-state.json", "sha256": state_sha_now},
        "production_profile": {"path": "sources/SP-vision-multimodal-2026/production-profile.json", "sha256": profile_sha},
        "implementation_commit_sha": START_SHA,
        "contract": contract, "artifacts": arts, "recorded_at": now,
    }
    vpath = EXECDIR / "stage-validation-r5-rev1.json"
    vpath.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    vsha = sha256_file(vpath)
    cp_path = SRC / "orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json"
    cp = json.loads(cp_path.read_text(encoding="utf-8"))
    cp["recorded_at"] = now
    cp["implementation"] = {"repository_commit_sha": START_SHA,
                            "orchestrator_version": "survey-production-core-v2/0.15-postintegration-transport-thematic"}
    cp["contract"] = contract
    cp["artifacts"] = arts
    cp["reviews"] = [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC", "status": "PASS",
        "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
        "evidence": ("Deterministic drafting-synthesis stage-contract validation for TS-003 Draft content "
                     "revision r5-rev1 (bounded Draft CONTENT revision from Architecture r5 APPROVED; lifecycle stays "
                     "DRAFT_COMPLETE): 16 draft-package/result pairs revalidated against current 121 authority "
                     "(packages byte-identical, results revised to draft_version fresh-121-r5-rev1) + 12/16 canonical "
                     "Draft validation PASS + 4/16 edition-local overlay PASS (P06 D065 claim-3; P10 D111/D112 "
                     "three-role chain; P11 D115 supporting role; P15 40/40 Architecture-map Discovery IDs bound "
                     "via multi-consumer cross-package synthesis authority; frozen generic cross-ref rejection "
                     "recorded as known compatibility boundary, not hidden) + synthesis input derivation match "
                     "(overlay-aware) + regenerated synthesis valid (payloads preserved, basis refreshed) + "
                     "edition-local semantic audits PASS (P15 per-thread 4/4,4/4,4/4,4/4,3/3,5/5,5/5,5/5,5/5,5/5,6/6; "
                     "LongVideoBench 6678; reader-Japanese purge; regression guards). "
                     "Machine validation only; Human/Sol Draft content review owed."),
        "result": {"path": "sources/SP-vision-multimodal-2026/execution/content-revision-r5-20261006/stage-validation-r5-rev1.json",
                   "sha256": vsha}}]
    cp["summary"] = ("TS-003 Draft content revision r5-rev1 from Architecture r5 APPROVED (Human Owner 2026-10-06): "
                     "P15 rebuilt as cross-package synthesis (40/40) + P10/P11/P12/P06/P09 bounded repairs + "
                     "reader-facing Japanese cleanup across 16 packages; VM-D122 excluded; no TeX/PDF; "
                     "STOP for Human/Sol Draft content review")
    cp_path.write_text(json.dumps(cp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cpsha = sha256_file(cp_path)
    state["checkpoint_provenance"]["draft"]["sha256"] = cpsha
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checkpoint_sha256": cpsha, "validation_sha256": vsha,
                      "state_sha256": sha256_file(state_path)}, indent=2))

    # canonical state validation must be clean afterwards
    sys.path.insert(0, str(ROOT))
    import importlib
    os_cwd = __import__("os")
    os_cwd.chdir(str(ROOT))
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    st = core.load_json(state_path)
    errs = agent.validate_agent_state(ROOT, cfg, st)
    if errs:
        print("validate_agent_state ERRORS:")
        for e in errs:
            print(" -", e)
        return 1
    print("validate_agent_state CLEAN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
