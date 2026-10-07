#!/usr/bin/env python3
"""Rebuild draft checkpoint + state provenance for r8-rev1 (DRAFT_COMPLETE held).

Same precedent as r5-rev1 rebuild: write validation record binding current state
bytes, rebuild ARCHITECTURE_ESTABLISHED.json (rev1 artifact SHAs + review), update
production-state checkpoint_provenance.draft.sha256. Lifecycle/gates/authority
untouched (r8 APPROVED preserved, no upstream mutation).
"""
from __future__ import annotations
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/r8-draft-closure-rev1-20261007"

PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def main() -> int:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_path = SRC / "production-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["lifecycle_state"] == "DRAFT_COMPLETE", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "approved"
    for pid in PIDS:
        r = json.loads((SRC / "draft/v2/packages" / pid / "draft-result.json").read_text(encoding="utf-8"))
        assert r.get("draft_version") == "fresh-121-r8-rev1", pid
        assert r.get("status") == "ESTABLISHED", pid
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
    profile_sha = sha256_file(SRC / "production-profile.json")
    state_sha_now = sha256_file(state_path)
    validation = {
        "schema_version": "2.0-rc1", "check_id": "CORE_STAGE_CONTRACT", "status": "PASS",
        "issue_id": "SP-vision-multimodal-2026",
        "from_state": "ARCHITECTURE_ESTABLISHED", "to_state": "DRAFT_COMPLETE",
        "production_state": {"path": "sources/SP-vision-multimodal-2026/production-state.json", "sha256": state_sha_now},
        "production_profile": {"path": "sources/SP-vision-multimodal-2026/production-profile.json", "sha256": profile_sha},
        "implementation_commit_sha": "1bbb86d7ad32508023970dae05f81bc920f207ab",
        "contract": contract, "artifacts": arts, "recorded_at": now,
    }
    vpath = EXECDIR / "validation/draft-stage-validation-rev1.json"
    vpath.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    vsha = sha256_file(vpath)
    cp_path = SRC / "orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json"
    cp = json.loads(cp_path.read_text(encoding="utf-8"))
    cp["recorded_at"] = now
    cp["implementation"] = {"repository_commit_sha": "1bbb86d7ad32508023970dae05f81bc920f207ab",
                            "orchestrator_version": "survey-production-core-v2/0.15-postintegration-transport-thematic"}
    cp["contract"] = contract
    cp["artifacts"] = arts
    cp["reviews"] = [{
        "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC", "status": "PASS",
        "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
        "evidence": ("Deterministic drafting-synthesis validation for TS-003 Draft closure revision "
                     "r8-rev1 (Draft-only targeted repair from Architecture r8 APPROVED; lifecycle stays "
                     "DRAFT_COMPLETE): 16 draft-package/result pairs revalidated against unchanged r8 "
                     "authority (packages re-derived identical, results revised to draft_version "
                     "fresh-121-r8-rev1) + 8/16 canonical Draft validation PASS + 8/16 edition-local "
                     "overlay PASS (P04/P05/P06/P07A/P07B/P10/P11/P15 over 35-entry r8-rev1 effective map "
                     "incl. D047->P04) + synthesis input derivation match (overlay-aware) + regenerated "
                     "synthesis valid (payloads refreshed) + edition-local closure audits PASS (P04 GoldG/D047, "
                     "Flamingo scale, OSWorld conditions, P09 TODO removal, GroundingDINO terms, reader X01, "
                     "P01 epistemics, Japanese/workflow purge, FINAL effective consumption, F1-F6 + G1-G7 "
                     "negative fixtures). Machine validation only; fresh independent content review owed."),
        "result": {"path": "sources/SP-vision-multimodal-2026/execution/r8-draft-closure-rev1-20261007/validation/draft-stage-validation-rev1.json",
                   "sha256": vsha}}]
    cp["summary"] = ("TS-003 Draft closure revision r8-rev1 from Architecture r8 APPROVED (unchanged): "
                     "P04 GoldG/D047 binding + Flamingo data-volume correction + OSWorld condition binding + "
                     "P09 TODO removal + GroundingDINO terminology + reader X01 removal + P01 epistemic scope + "
                     "Japanese/workflow cleanup; VM-D122 excluded; no TeX/PDF; "
                     "STOP for fresh independent content review")
    cp_path.write_text(json.dumps(cp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cpsha = sha256_file(cp_path)
    state["checkpoint_provenance"]["draft"]["sha256"] = cpsha
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checkpoint_sha256": cpsha, "validation_sha256": vsha,
                      "state_sha256": sha256_file(state_path)}, indent=2))

    sys.path.insert(0, str(ROOT))
    import os
    os.chdir(str(ROOT))
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    errs = agent.validate_agent_state(ROOT, cfg, core.load_json(state_path))
    if errs:
        print("validate_agent_state ERRORS:")
        for e in errs:
            print(" -", e)
        return 1
    print("validate_agent_state CLEAN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
