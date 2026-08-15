from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_weekly_interactive_evidence as revision


class WeeklyEvidenceRevisionTests(unittest.TestCase):
    def test_weekly_identity_boundary(self):
        self.assertIsNotNone(revision.WEEKLY_RE.fullmatch("2026-W33"))
        self.assertIsNone(revision.WEEKLY_RE.fullmatch("SP-2026-M07"))

    def test_revision_requires_evidence_reviewed_preselection_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "sources/2026-W33/pipeline-state.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                '{"issue_id":"2026-W33","lifecycle_state":"EVIDENCE_REVIEWED","gates":'
                '{"candidate_inventory":"passed","evidence_normalized":"passed",'
                '"candidate_selection":"pending","issue_architecture":"pending"}}\n',
                encoding="utf-8",
            )
            resolved, state, raw = revision.validate_current_state(root, "2026-W33")
            self.assertEqual(resolved, path)
            self.assertEqual(state["lifecycle_state"], "EVIDENCE_REVIEWED")
            self.assertEqual(raw, path.read_bytes())

    def test_revision_rejects_after_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "sources/2026-W33/pipeline-state.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                '{"issue_id":"2026-W33","lifecycle_state":"EVIDENCE_REVIEWED","gates":'
                '{"candidate_inventory":"passed","evidence_normalized":"passed",'
                '"candidate_selection":"passed","issue_architecture":"pending"}}\n',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "after Candidate Selection"):
                revision.validate_current_state(root, "2026-W33")


if __name__ == "__main__":
    unittest.main()
