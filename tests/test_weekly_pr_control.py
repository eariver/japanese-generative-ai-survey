from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import weekly_pr_control as control


class WeeklyPrControlTests(unittest.TestCase):
    def test_metadata_uses_canonical_work_branch_and_safe_gate_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            value = control.build("2026-W33", root)
            self.assertEqual(value["branch"], "weekly/2026-W33-work")
            self.assertIn("Draft PR", value["body"])
            self.assertIn("Release publication is a separate workflow", value["body"])
            self.assertIn("not initialized", value["body"])
            self.assertTrue(any("never force-update" in rule for rule in value["rules"]))
            self.assertTrue(any("no unique commits" in rule and "fast-forwarded" in rule for rule in value["rules"]))
            self.assertTrue(any("Never rewrite" in rule and "unique weekly commits" in rule for rule in value["rules"]))
            self.assertTrue(any("Never merge" in rule for rule in value["rules"]))

    def test_pipeline_lifecycle_state_is_reported_but_not_interpreted_as_gate_approval(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state = root / "sources" / "2026-W33" / "pipeline-state.json"
            state.parent.mkdir(parents=True)
            state.write_text(
                json.dumps({"issue_id": "2026-W33", "lifecycle_state": "EVIDENCE_REVIEWED"}),
                encoding="utf-8",
            )
            value = control.build("2026-W33", root)
            self.assertEqual(value["pipeline_state_status"], "EVIDENCE_REVIEWED")
            self.assertIn("`EVIDENCE_REVIEWED`", value["body"])
            # Gate checklist stays explicit/unapproved regardless of the lifecycle state.
            self.assertIn("- [ ] Candidate Selection explicitly `APPROVED`", value["body"])
            self.assertIn("- [ ] Freeze decision recorded", value["body"])

    def test_legacy_status_field_does_not_masquerade_as_canonical_lifecycle_state(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state = root / "sources" / "2026-W33" / "pipeline-state.json"
            state.parent.mkdir(parents=True)
            state.write_text(json.dumps({"issue_id": "2026-W33", "status": "evidence-reviewed"}), encoding="utf-8")
            value = control.build("2026-W33", root)
            self.assertIsNone(value["pipeline_state_status"])
            self.assertIn("not initialized", value["body"])

    def test_invalid_issue_id_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                control.build("W33", Path(tmp))
            with self.assertRaises(ValueError):
                control.build("2026-W3", Path(tmp))


if __name__ == "__main__":
    unittest.main()
