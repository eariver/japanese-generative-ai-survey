from __future__ import annotations

import unittest

from scripts import run_weekly_interactive_evidence as runner


class WeeklyInteractiveEvidenceTests(unittest.TestCase):
    def test_weekly_identity_boundary(self):
        self.assertIsNotNone(runner.WEEKLY_RE.fullmatch("2026-W33"))
        self.assertIsNone(runner.WEEKLY_RE.fullmatch("SP-2026-M07"))

    def test_default_paper_is_partial_hold(self):
        task = {
            "evidence_task_id": "evidence:2026-W33:item-arxiv-test-0123456789",
            "task_type": "VERIFY_ITEM",
            "screening_ids": ["arxiv:test"],
            "source_types": ["paper"],
            "verification_targets": ["verify claims"],
        }
        queue = {
            "arxiv:test": {
                "title": "Example Paper",
                "published_at": "2026-08-10T00:00:00Z",
            }
        }
        entry = runner.default_entry(task, queue, "2026-W33")
        self.assertEqual(entry["status"], "PARTIAL")
        self.assertEqual(entry["candidate_recommendation"], "HOLD")
        self.assertEqual(entry["claims"][1]["evidence_class"], "AUTHOR_CLAIM")
        self.assertEqual(entry["target_findings"]["verify claims"]["status"], "UNRESOLVED")

    def test_default_index_requires_more_inspection(self):
        task = {
            "evidence_task_id": "evidence:2026-W33:item-index-test-0123456789",
            "task_type": "INSPECT_INDEX",
            "screening_ids": ["official-index:test"],
            "source_types": ["official-index-snapshot"],
            "verification_targets": ["inspect item"],
        }
        queue = {"official-index:test": {"title": "Example News Index"}}
        entry = runner.default_entry(task, queue, "2026-W33")
        self.assertEqual(entry["status"], "NEEDS_MORE")
        self.assertEqual(entry["candidate_recommendation"], "INSPECT_MORE")
        self.assertFalse(entry["why_now_confirmed"])

    def test_override_merge_promotes_without_losing_default_artifact(self):
        base = {
            "artifact": {"canonical_name": "Example", "artifact_type": "PAPER", "organization": None},
            "candidate_recommendation": "HOLD",
            "status": "PARTIAL",
            "target_findings": {"a": {"status": "UNRESOLVED", "finding": "pending"}},
        }
        override = {
            "artifact": {"organization": "Example Lab"},
            "candidate_recommendation": "CANDIDATE",
            "status": "VERIFIED",
            "target_findings": {"a": {"status": "VERIFIED", "finding": "checked", "source_indexes": [1]}},
        }
        merged = runner.merge_entry(base, override)
        self.assertEqual(merged["artifact"]["canonical_name"], "Example")
        self.assertEqual(merged["artifact"]["organization"], "Example Lab")
        self.assertEqual(merged["candidate_recommendation"], "CANDIDATE")
        self.assertEqual(merged["target_findings"]["a"]["status"], "VERIFIED")


if __name__ == "__main__":
    unittest.main()
