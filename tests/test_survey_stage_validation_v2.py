from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_production_v2 as core
from scripts import survey_stage_validation_v2 as stage_validation


class SurveyStageValidationV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)

    def initialize(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict]:
        temp = tempfile.TemporaryDirectory(dir=self.root)
        self.addCleanup(temp.cleanup)
        base = Path(temp.name)
        rel = str(base.relative_to(self.root))
        profile = core.thematic_profile(
            self.root,
            self.cfg,
            {
                "issue_id": "SP-STAGE-VALIDATION",
                "question": "Can compact agent checkpoints retain deterministic stage authority?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T09:00:00Z",
                "scope_dimensions": ["stage authority"],
                "source_root": rel,
                "survey_root": f"{rel}/survey",
                "work_branch": "test/stage-validation",
            },
        )
        _, state_path = core.initialize(
            self.root,
            self.cfg,
            profile,
            "1" * 40,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T09:00:00Z"),
        )
        return temp, state_path, profile

    def test_same_named_but_invalid_discovery_authority_is_rejected(self) -> None:
        _, state_path, profile = self.initialize()
        base = self.root / profile["paths"]["source_root"]
        fake = base / "discovery/discovery-accepted-v2.json"
        core.write_json(fake, {"fixture": "same name is not semantic authority"})
        with self.assertRaises(ValueError):
            stage_validation.validate_stage(
                self.root,
                self.cfg,
                state_path,
                {"discovery-acceptance": fake},
                base / "orchestration/v2/stage-validation/ISSUE_INITIALIZED.json",
                core.parse_instant("2026-08-22T09:10:00Z"),
            )

    def test_current_tool_basis_does_not_reuse_initialization_commit_as_execution_identity(self) -> None:
        _, state_path, _ = self.initialize()
        state = core.load_json(state_path)
        current = core.repository_commit_sha(self.root)
        self.assertNotEqual(current, state["implementation"]["repository_commit_sha"])
        runtime_tool.verify_current_stage_basis(self.root, self.cfg, state, current)
        with self.assertRaisesRegex(ValueError, "actual current work-branch implementation"):
            runtime_tool.verify_current_stage_basis(
                self.root,
                self.cfg,
                state,
                state["implementation"]["repository_commit_sha"],
            )

    def test_draft_stage_validator_requires_paired_package_and_result_authorities(self) -> None:
        with tempfile.TemporaryDirectory(dir=self.root) as raw:
            base = Path(raw)
            synthesis_input = base / "synthesis-input.json"
            synthesis_result = base / "synthesis-result.json"
            core.write_json(synthesis_input, {"fixture": "input"})
            core.write_json(synthesis_result, {"fixture": "result"})
            with self.assertRaisesRegex(ValueError, "paired draft-package:/draft-result"):
                stage_validation._current_artifacts(
                    self.root,
                    {"lifecycle_state": "ARCHITECTURE_ESTABLISHED"},
                    {
                        "synthesis-input": synthesis_input,
                        "synthesis-result": synthesis_result,
                    },
                )


if __name__ == "__main__":
    unittest.main()
