from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE_CONFIG = ROOT / "config" / "survey-production-v2.json"
WORKFLOW_ROOT = ROOT / ".github" / "workflows"


class SpecialHumanGatePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CORE_CONFIG.read_text(encoding="utf-8"))

    def test_core_declares_only_architecture_and_publication_preview_as_normal_human_gates(self) -> None:
        operator = self.config["operator_model"]
        self.assertEqual(
            operator["normal_human_gates"],
            ["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"],
        )
        self.assertTrue(operator["autonomous_until_gate"])

    def test_retired_special_human_gate_workflows_are_absent(self) -> None:
        retired = {
            "assistant-control.yml",
            "accept-special-publication-preview-issue-only.yml",
            "accept-special-freeze-issue-only.yml",
            "publish-special-frozen-release-issue-only.yml",
            "accept-special-visual-review-issue-only.yml",
            "apply-special-selection-and-propose-architecture.yml",
            "revise-special-annual-source-specific-notes-v2.yml",
        }
        present = {path.name for path in WORKFLOW_ROOT.glob("*.yml")}
        self.assertTrue(retired.isdisjoint(present))

    def test_publication_preview_export_is_read_only_candidate_transport(self) -> None:
        text = (WORKFLOW_ROOT / "survey-production-v2-export-publication-preview.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("contents: read", text)
        self.assertIn("publication-candidate-v2.json", text)
        self.assertIn("READY_FOR_PUBLICATION_PREVIEW", text)
        self.assertIn("validate_survey_preflight_guard_v2.py", text)
        self.assertNotIn("release_frozen_publication_v2.py", text)
        self.assertNotIn("git push", text)
        self.assertNotIn("--stage released", text)

    def test_release_requires_explicit_confirmation_and_frozen_only_policy(self) -> None:
        text = (WORKFLOW_ROOT / "survey-production-v2-release.yml").read_text(encoding="utf-8")
        self.assertIn("confirmed", text)
        self.assertIn("validate_survey_preflight_guard_v2.py", text)
        self.assertIn("release_frozen_publication_v2.py", text)
        self.assertIn("--release-policy frozen_only", text)


if __name__ == "__main__":
    unittest.main()
