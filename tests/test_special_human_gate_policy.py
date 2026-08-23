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
        self.assertEqual(
            self.config["orchestration"]["gate_at_state"],
            {
                "ARCHITECTURE_ESTABLISHED": "ARCHITECTURE_REVIEW",
                "RELEASE_CANDIDATE": "PUBLICATION_PREVIEW",
            },
        )

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

    def test_publication_preview_export_is_read_only_exact_candidate_transport(self) -> None:
        text = (WORKFLOW_ROOT / "survey-production-v2-export-publication-preview.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("contents: read", text)
        self.assertIn("publication-candidate-v2.json", text)
        self.assertIn("publication.validate_candidate", text)
        self.assertIn("READY_FOR_PUBLICATION_PREVIEW", text)
        self.assertIn("REPOSITORY_FILE", text)
        self.assertIn("Publication Candidate PDF authority drift", text)
        self.assertIn("EXACT_PUBLICATION_CANDIDATE_BYTES", text)
        self.assertIn("actions/upload-artifact@v7", text)
        self.assertNotIn("git push", text)
        self.assertNotIn("gh release create", text)

    def test_release_requires_exact_frozen_authority_and_explicit_confirmation(self) -> None:
        text = (WORKFLOW_ROOT / "survey-production-v2-release.yml").read_text(encoding="utf-8")
        self.assertIn("confirmation:", text)
        self.assertIn('test "$CONFIRMATION" = "release:${ISSUE_ID}"', text)
        self.assertIn("production_state_sha256", text)
        self.assertIn("release_manifest_sha256", text)
        self.assertIn("lifecycle_state') != 'FROZEN", text)
        self.assertIn("validate_agent_state", text)
        self.assertIn("VERIFY_EXACT_BYTES_THEN_RESUME", text)
        self.assertIn("gh release download", text)
        self.assertIn("survey_release_checkpoint_v2.py", text)
        self.assertIn("Commit post-release provenance through a normal PR", text)


if __name__ == "__main__":
    unittest.main()
