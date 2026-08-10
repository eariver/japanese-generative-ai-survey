from __future__ import annotations

import unittest

from scripts.run_special_interactive_screening import make_decision, validate_overrides


class SpecialInteractiveScreeningTests(unittest.TestCase):
    def test_omitted_record_becomes_explicit_drop(self):
        decision = make_decision({"screening_id": "x"}, None, "not selected for retrospective verification")
        self.assertEqual(decision["decision"], "DROP")
        self.assertEqual(decision["screening_id"], "x")
        self.assertEqual(decision["verification_targets"], [])

    def test_retained_override_is_preserved(self):
        override = {
            "decision": "KEEP",
            "reason": "technically material July model release",
            "why_now": "July retrospective release event",
            "topic_lanes": ["A"],
            "duplicate_group": None,
            "verification_targets": ["verify release date"],
            "confidence": "high",
        }
        decision = make_decision({"screening_id": "x"}, override, "default")
        self.assertEqual(decision["decision"], "KEEP")
        self.assertEqual(decision["verification_targets"], ["verify release date"])

    def test_override_document_rejects_explicit_drop_entries(self):
        value = {
            "schema_version": "1.0",
            "issue_id": "SP-2026-M07",
            "runner": {"provider": "OpenAI", "model": "GPT-5.6 Sol", "invocation": "interactive", "generated_at": "2026-08-10T00:00:00Z"},
            "default_drop": {"reason": "default"},
            "overrides": [{"screening_id": "x", "decision": "DROP", "reason": "x", "topic_lanes": [], "verification_targets": [], "confidence": "high"}],
        }
        with self.assertRaisesRegex(ValueError, "KEEP/MAYBE/INSPECT"):
            validate_overrides(value, "SP-2026-M07")


if __name__ == "__main__":
    unittest.main()
