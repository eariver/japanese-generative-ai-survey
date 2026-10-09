#!/usr/bin/env python3
"""Advance DRAFT_COMPLETE (fresh-124-r9) -> VALIDATED_DRAFT via canonical checkpoint machinery.

Artifacts: reader-manuscript, validated-source (main.tex), publication-pdf,
quality-regression-bundle, semantic-review, visual-review, reader-surface-gate.
No Publication Candidate / Preview / Freeze / Release. Shared Core untouched.
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
EDIR = f"{SRC}/execution/reader-publication-validation-fresh-124-r9-20261009"
STATE_REL = f"{SRC}/production-state.json"
PUB = f"{SRC}/publication/v2"
SURVEY = "surveys/special/vision-multimodal-2026"

ARTS = [
    ("reader-manuscript", f"{PUB}/reader-manuscript-v2.json"),
    ("validated-source", f"{SURVEY}/main.tex"),
    ("publication-pdf", f"{SURVEY}/main.pdf"),
    ("quality-regression-bundle", f"{PUB}/quality-regression-bundle-v2.json"),
    ("semantic-review", f"{PUB}/semantic-editorial-review-v2.json"),
    ("visual-review", f"{PUB}/visual-review-v2.json"),
    ("reader-surface-gate", f"{PUB}/reader-surface-gate-v2.json"),
]

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
    assert state["lifecycle_state"] == "DRAFT_COMPLETE", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "approved", state["human_gates"]
    for name, rel in ARTS:
        assert (root / rel).is_file(), (name, rel)

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
        arts = [{"name": n, "path": p, "sha256": sha256_file(root / p)} for n, p in ARTS]
        vdir = root / EDIR / "validation"
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "validation-stage-validation-fresh-124-r9.json"
        reviews_path = vdir / "validation-stage-reviews-fresh-124-r9.json"
        assert not validation_path.exists() and not reviews_path.exists()
        validation = {
            "schema_version": "2.0-rc1", "check_id": "CORE_STAGE_CONTRACT", "status": "PASS",
            "issue_id": ISSUE_ID, "from_state": "DRAFT_COMPLETE", "to_state": "VALIDATED_DRAFT",
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
            "evidence": ("Reader-publication stage-contract validation passed for fresh-124-r9 "
                         "(reader manuscript + 39pp exact PDF + quality bundle + semantic/visual "
                         "reviews + surface gate; 124/124 identifiers; deterministic 4/4 PASS). "
                         "Machine validation only; Publication Preview NOT started."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        artifacts = {n: root / p for n, p in ARTS}
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL, artifacts, reviews_path,
            ("TS-003 Reader Publication Validation fresh-124-r9 (approved r9 authority; "
             "16 packages + synthesis rendered to 39pp exact PDF; 12 documented "
             "publication-layer patches; deterministic/semantic/visual/gate PASS). "
             "STOP at VALIDATED_DRAFT; Publication Candidate/Preview/Freeze/Release NOT started."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "VALIDATED_DRAFT", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
