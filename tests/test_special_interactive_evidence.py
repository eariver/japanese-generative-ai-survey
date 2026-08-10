from __future__ import annotations

import unittest

from scripts import run_special_interactive_evidence as runner


class SpecialInteractiveEvidenceTests(unittest.TestCase):
    def test_special_identity_boundary(self):
        self.assertIsNotNone(runner.SPECIAL_RE.fullmatch("SP-2026-M07"))
        self.assertIsNone(runner.SPECIAL_RE.fullmatch("2026-W33"))
        self.assertIsNotNone(runner.ANY_RE.fullmatch("2026-W33"))
        self.assertIsNotNone(runner.ANY_RE.fullmatch("SP-2026-M07"))

    def test_compact_override_expands_to_complete_card(self):
        task = {
            "evidence_task_id": "evidence:SP-2026-M07:test-task-01234567",
            "locators": ["https://example.com/official"],
            "verification_targets": ["verify release date"],
        }
        entry = {
            "evidence_task_id": task["evidence_task_id"],
            "artifact": {"canonical_name": "Example", "artifact_type": "MODEL", "organization": "Example Org"},
            "candidate_recommendation": "CANDIDATE",
            "why_this_special": "Material July release.",
            "events": [{"event_type": "MODEL_RELEASE", "event_date": "2026-07-10", "source_indexes": [1]}],
            "claims": [{"text": "Example was released in July.", "evidence_class": "PRIMARY_FACT", "source_indexes": [1]}],
            "limitations": ["Capability claims require separate attribution."],
        }
        card = runner.build_card(task, entry, "SP-2026-M07", "2026-08-10T15:35:00Z")
        self.assertEqual(card["artifact"]["canonical_name"], "Example")
        self.assertEqual(card["editorial"]["candidate_recommendation"], "CANDIDATE")
        self.assertEqual(card["verification"]["targets"][0]["status"], "VERIFIED")
        self.assertEqual(card["sources"][0]["source_class"], "PRIMARY_OFFICIAL")

    def test_source_index_out_of_range_fails(self):
        with self.assertRaisesRegex(ValueError, "out of range"):
            runner.source_ids_for_indexes([{"source_id": "src-1"}], [2], "claim")


if __name__ == "__main__":
    unittest.main()
