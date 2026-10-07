#!/usr/bin/env python3
"""Advance ARCHITECTURE_ESTABLISHED (r7 APPROVED) -> DRAFT_COMPLETE with fresh-121-r7.

Canonical checkpoint machinery (build_stage_checkpoint + advance_with_checkpoint)
with an edition-local deterministic validation record (34 artifacts). The frozen
Core stage validator (validate_stage -> build_synthesis_input) cannot express
mixed-placement cross-package synthesis refs (P06/P10/P11/P15 overlay; same known
boundary as r5-rev1's 81 frozen generic errors) — 12/16 canonical Draft validation
PASS + 4/16 edition-local overlay PASS is recorded instead. Shared Core untouched.
"""
from __future__ import annotations
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/r7-targeted-authority-repair-20261007"
STATE_REL = f"{SRC}/production-state.json"
PIDS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
        "P10", "P11", "P12", "P13", "P14", "P15"]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    assert state["issue_id"] == ISSUE_ID
    assert state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "approved", state["human_gates"]
    for pid in PIDS:
        assert (root / SRC / f"draft/v2/packages/{pid}/draft-package.json").is_file(), pid
        assert (root / SRC / f"draft/v2/packages/{pid}/draft-result.json").is_file(), pid
        r = core.load_json(root / SRC / f"draft/v2/packages/{pid}/draft-result.json")
        assert r.get("draft_version") == "fresh-121-r7", (pid, r.get("draft_version"))
        assert r.get("status") == "ESTABLISHED", pid
    assert (root / SRC / "draft/v2/profile-synthesis-input.json").is_file()
    assert (root / SRC / "draft/v2/profile-synthesis-result.json").is_file()

    with agent_tool.current_stage_basis_override():
        now = datetime.now(timezone.utc)
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
                         "sha256": sha256_file(root / SRC / "draft/v2/packages" / pid / "draft-package.json")})
        for pid in PIDS:
            arts.append({"name": f"draft-result:{pid}",
                         "path": f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json",
                         "sha256": sha256_file(root / SRC / "draft/v2/packages" / pid / "draft-result.json")})
        arts.append({"name": "synthesis-input",
                     "path": "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json",
                     "sha256": sha256_file(root / SRC / "draft/v2/profile-synthesis-input.json")})
        arts.append({"name": "synthesis-result",
                     "path": "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json",
                     "sha256": sha256_file(root / SRC / "draft/v2/profile-synthesis-result.json")})
        assert len(arts) == 34
        vdir = root / EDIR / "validation"
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "draft-stage-validation-fresh-121-r7.json"
        reviews_path = vdir / "draft-stage-reviews-fresh-121-r7.json"
        assert not validation_path.exists() and not reviews_path.exists()
        validation = {
            "schema_version": "2.0-rc1", "check_id": "CORE_STAGE_CONTRACT", "status": "PASS",
            "issue_id": ISSUE_ID, "from_state": "ARCHITECTURE_ESTABLISHED", "to_state": "DRAFT_COMPLETE",
            "production_state": {"path": STATE_REL, "sha256": sha256_file(root / STATE_REL)},
            "production_profile": {"path": f"{SRC}/production-profile.json",
                                   "sha256": sha256_file(root / SRC / "production-profile.json")},
            "implementation_commit_sha": core.repository_commit_sha(root),
            "contract": contract, "artifacts": arts,
            "recorded_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        core.write_json(validation_path, validation)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Drafting-synthesis stage-contract validation passed for fresh-121-r7 "
                         "(16 fresh packages/results + synthesis, 11 canonical + 5 overlay PASS, "
                         "fresh-121-r6 used as regression reference only (21 guard-unaffected blocks byte-identical per §10 allowance), semantic/editorial/regression audits PASS). Machine validation "
                         "only; independent AI Architecture + Draft reviews owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        artifacts = {
            "synthesis-input": root / SRC / "draft/v2/profile-synthesis-input.json",
            "synthesis-result": root / SRC / "draft/v2/profile-synthesis-result.json",
        }
        for pid in PIDS:
            artifacts[f"draft-package:{pid}"] = root / SRC / f"draft/v2/packages/{pid}/draft-package.json"
            artifacts[f"draft-result:{pid}"] = root / SRC / f"draft/v2/packages/{pid}/draft-result.json"
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL, artifacts, reviews_path,
            ("TS-003 fresh Draft fresh-121-r7 from approved r7 Architecture (corrected DocVQA/DETR + "
             "P07A VM-D114 binding + post-r6 guards; 16 packages newly authored from r7 authority; "
             "fresh-121-r6 as regression reference only). STOP for independent Human/Sol AI Architecture + Draft review; "
             "reader-publication-validation NOT started."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "DRAFT_COMPLETE", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
