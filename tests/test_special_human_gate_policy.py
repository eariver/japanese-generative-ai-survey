from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / ".github" / "workflows" / "assistant-control.yml"
PUBLICATION = ROOT / ".github" / "workflows" / "accept-special-publication-preview-issue-only.yml"
SELECTION = ROOT / ".github" / "workflows" / "apply-special-selection-and-propose-architecture.yml"


def workflow_block(text: str, name: str) -> str:
    pattern = rf"(?ms)^              '{re.escape(name)}': \{{\n(.*?)(?=^              '[^']+': \{{|^          \}}$)"
    match = re.search(pattern, text)
    if not match:
        raise AssertionError(f"workflow block not found: {name}")
    return match.group(1)


class SpecialHumanGatePolicyTests(unittest.TestCase):
    def test_assistant_control_has_only_architecture_and_publication_preview_as_special_human_stops(self) -> None:
        text = CONTROL.read_text(encoding="utf-8")
        selection = workflow_block(text, "apply-special-selection-and-propose-architecture")
        architecture = workflow_block(text, "approve-special-architecture-and-prepare-drafts")
        preview = workflow_block(text, "accept-special-publication-preview-issue-only")
        freeze = workflow_block(text, "accept-special-freeze-issue-only")
        publish = workflow_block(text, "publish-special-frozen-release-issue-only")

        self.assertNotIn("'human_gate': True", selection)
        self.assertIn("'human_gate': True", architecture)
        self.assertIn("'human_gate': True", preview)
        self.assertNotIn("'human_gate': True", freeze)
        self.assertNotIn("'human_gate': True", publish)
        self.assertNotIn("'accept-special-visual-review-issue-only': {", text)

    def test_selection_checkpoint_uses_internal_not_human_authority(self) -> None:
        text = SELECTION.read_text(encoding="utf-8")
        self.assertIn("special-editorial-pipeline", text)
        self.assertIn("INTERNAL_EDITORIAL_CHECKPOINT_FOR_ARCHITECTURE_PROPOSAL", text)
        self.assertIn("assert selection['approval']['approved_by']!='eariver'", text)
        self.assertIn("this is not a Human Gate approval", text)

    def test_publication_preview_workflow_binds_one_approval_to_finalize_and_publish(self) -> None:
        text = PUBLICATION.read_text(encoding="utf-8")
        self.assertIn("approved_pdf_sha256", text)
        self.assertIn("accept_special_visual_review_issue_only.py", text)
        self.assertIn("accept_special_freeze_issue_only.py", text)
        self.assertIn("gh pr merge", text)
        self.assertIn("publish-special-frozen-release-issue-only.yml", text)
        self.assertIn("test \"$actual\" = \"$APPROVED_PDF_SHA256\"", text)


if __name__ == "__main__":
    unittest.main()
