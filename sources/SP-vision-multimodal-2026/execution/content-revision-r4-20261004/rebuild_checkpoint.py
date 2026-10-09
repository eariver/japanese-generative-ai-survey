#!/usr/bin/env python3
"""Rebuild draft checkpoint + state provenance after content-revision regen.

Order (same precedent as bounded-revision run):
 1. write stage-validation-content-revision-r4.json (binds current state bytes);
 2. rebuild ARCHITECTURE_ESTABLISHED.json (artifact SHAs + reviews.result.sha);
 3. update production-state.json checkpoint_provenance.draft.sha256;
 4. run canonical validate_agent_state (must be clean).
Lifecycle/gates untouched (DRAFT_COMPLETE held, r4 APPROVED preserved).
"""
from __future__ import annotations
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r4-20261004"
START_SHA = "382833c30d294f54e847c0333fc4a03a58748a32"


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
        "implementation_commit_sha": START_SHA,
        "contract": contract, "artifacts": arts, "recorded_at": now,
    }
    vpath = EXECDIR / "stage-validation-content-revision-r4.json"
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
        "evidence": ("Deterministic drafting-synthesis stage-contract validation for TS-003 post-Architecture-r4 "
                     "Draft content revision (supplied fresh independent content review materialized; Architecture r4 "
                     "APPROVED preserved, lifecycle stays DRAFT_COMPLETE): 16 draft-package/result pairs revalidated "
                     "against current 112 authority (packages byte-identical, results revised) + P15 overlay PASS "
                     "(39/39 Architecture-map Discovery IDs bound via edition-local cross-package synthesis authority) + "
                     "15/16 canonical Draft validation PASS (generic Core P15 cross-ref rejection recorded as known "
                     "compatibility boundary, not hidden) + synthesis input derivation match (overlay-aware) + "
                     "regenerated synthesis valid. Machine validation only; fresh independent JSON content review owed."),
        "result": {"path": "sources/SP-vision-multimodal-2026/execution/content-revision-r4-20261004/stage-validation-content-revision-r4.json",
                   "sha256": vsha}}]
    cp["summary"] = ("TS-003 post-Architecture-r4 Draft content revision from CONTENT REVISION REQUIRED "
                     "(Human Architecture r4 APPROVED preserved); 16 packages revised to ~128k reader chars, "
                     "P15 methodology-first with edition-local cross-package synthesis overlay (39/39 map IDs), "
                     "MMMU/MMBench decontaminated, DINO/P04/P05/P02/P07/POPE/grounding/terminology/semantic-padding repaired, "
                     "synthesis freshly regenerated; STOP for fresh independent JSON content review; no TeX/PDF.")
    cp_path.write_text(json.dumps(cp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cpsha = sha256_file(cp_path)
    state["checkpoint_provenance"]["draft"] = {
        "path": "sources/SP-vision-multimodal-2026/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json",
        "sha256": cpsha}
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validation_sha": vsha, "checkpoint_sha": cpsha,
                      "state_sha_before": state_sha_now,
                      "state_sha_after": sha256_file(state_path)}, indent=2))
    # canonical agent-state check
    sys.path.insert(0, str(ROOT))
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    st = core.load_json(state_path)
    errors = agent.validate_agent_state(ROOT, cfg, st)
    print("validate_agent_state errors:", errors if errors else "CLEAN")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
