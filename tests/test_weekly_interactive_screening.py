from __future__ import annotations

import unittest
from pathlib import Path

from scripts.run_special_interactive_screening import make_decision, validate_overrides
from scripts.run_weekly_interactive_screening import run


class WeeklyInteractiveScreeningTests(unittest.TestCase):
    def test_omitted_record_becomes_explicit_drop(self):
        decision = make_decision({"screening_id": "x"}, None, "not selected for weekly verification")
        self.assertEqual(decision["decision"], "DROP")
        self.assertEqual(decision["screening_id"], "x")
        self.assertEqual(decision["verification_targets"], [])

    def test_weekly_override_document_is_accepted(self):
        value = {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "runner": {
                "provider": "OpenAI",
                "model": "GPT-5.6 Sol",
                "invocation": "interactive",
                "generated_at": "2026-08-15T00:00:00Z",
            },
            "default_drop": {"reason": "default"},
            "overrides": [
                {
                    "screening_id": "x",
                    "decision": "KEEP",
                    "reason": "technically material weekly candidate",
                    "topic_lanes": ["A"],
                    "verification_targets": ["verify primary source"],
                    "confidence": "high",
                }
            ],
        }
        overrides = validate_overrides(value, "2026-W33")
        self.assertEqual(overrides["x"]["decision"], "KEEP")

    def test_runner_rejects_special_issue_id_before_io(self):
        with self.assertRaisesRegex(ValueError, "YYYY-Www"):
            run(
                repo_root=Path("."),
                issue_id="SP-2026-M07",
                source_ref="special/SP-2026-M07-work",
                source_commit="0" * 40,
                overrides_path=Path("missing.json"),
                review_reference="test",
            )


if __name__ == "__main__":
    unittest.main()
