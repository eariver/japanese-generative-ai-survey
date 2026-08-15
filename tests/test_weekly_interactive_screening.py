from __future__ import annotations

import unittest
from pathlib import Path

from scripts.run_special_interactive_screening import make_decision
from scripts.run_weekly_interactive_screening import expand_selection_document, run


class WeeklyInteractiveScreeningTests(unittest.TestCase):
    def test_omitted_record_becomes_explicit_drop(self):
        decision = make_decision({"screening_id": "x"}, None, "not selected for weekly verification")
        self.assertEqual(decision["decision"], "DROP")
        self.assertEqual(decision["screening_id"], "x")
        self.assertEqual(decision["verification_targets"], [])

    def test_compact_selection_expands_to_override_contract(self):
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
            "decision_defaults": {
                "KEEP": {"reason": "keep", "verification_targets": ["verify"], "confidence": "medium"},
                "MAYBE": {"reason": "maybe", "verification_targets": ["verify"], "confidence": "medium"},
                "INSPECT": {"reason": "inspect", "verification_targets": ["inspect"], "confidence": "medium"},
            },
            "selections": [
                {
                    "screening_id": "x",
                    "decision": "KEEP",
                    "topic_lanes": ["A"],
                    "confidence": "high",
                }
            ],
        }
        _, overrides = expand_selection_document(value, "2026-W33")
        self.assertEqual(overrides["x"]["decision"], "KEEP")
        self.assertEqual(overrides["x"]["reason"], "keep")
        self.assertEqual(overrides["x"]["verification_targets"], ["verify"])
        self.assertEqual(overrides["x"]["confidence"], "high")

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
