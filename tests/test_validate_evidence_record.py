from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_evidence_record as ev


class EvidenceRecordValidatorTests(unittest.TestCase):
    def _queue(self, path: Path) -> None:
        item = {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "batch_id": "batch-007",
            "screening_id": "official-feed:test",
            "record": {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "screening_id": "official-feed:test",
                "source_type": "official-feed-item",
                "collector_id": "official-pages",
                "collector_run_id": "run",
                "observed_at": "2026-08-10T00:00:00Z",
                "title": "Test item",
                "locator": "https://example.com/test",
                "raw_paths": ["raw/test.xml"],
                "published_at": "2026-08-07T00:00:00Z",
                "summary_text": "summary",
                "metadata": {},
            },
            "screening": {
                "screening_id": "official-feed:test",
                "decision": "KEEP",
                "reason": "candidate",
                "why_now": "new event",
                "topic_lanes": ["K"],
                "duplicate_group": None,
                "verification_targets": ["verify threshold", "verify date"],
                "confidence": "high",
            },
        }
        path.write_text(json.dumps(item) + "\n", encoding="utf-8")

    def _valid(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_id": "evidence:official-feed:test",
            "screening_id": "official-feed:test",
            "artifact": {
                "title": "Test item",
                "canonical_locator": "https://example.com/test",
                "artifact_type": "MODEL_EVALUATION",
                "artifact_first_announced": "2026-08-07",
                "event_type": "SECURITY_EVALUATION",
                "event_date": "2026-08-07",
            },
            "verification_status": "PARTIAL",
            "primary_sources": [
                {
                    "source_id": "src1",
                    "locator": "https://example.com/test",
                    "source_type": "OFFICIAL_PAGE",
                    "published_at": "2026-08-07T00:00:00Z",
                    "observed_at": "2026-08-10T00:00:00Z",
                    "content_sha256": None,
                    "notes": None,
                }
            ],
            "claims": [
                {
                    "claim_id": "c1",
                    "text": "The official page exists and is dated August 7.",
                    "evidence_class": "VERIFIED_PRIMARY",
                    "source_ids": ["src1"],
                    "publishable": True,
                    "confidence": "high",
                    "caveats": [],
                },
                {
                    "claim_id": "c2",
                    "text": "Independent reproduction remains unresolved.",
                    "evidence_class": "PENDING",
                    "source_ids": [],
                    "publishable": False,
                    "confidence": "medium",
                    "caveats": [],
                },
            ],
            "metrics": [],
            "limitations": ["Only the official page has been checked."],
            "open_questions": ["Independent reproduction remains pending."],
            "safe_editorial_core": "公式ページの存在と公開日は確認できる。性能主張は別途検証が必要。",
            "provenance": {
                "screening_batch_id": "batch-007",
                "screening_decision": "KEEP",
                "verification_targets": ["verify threshold", "verify date"],
                "runner": {
                    "provider": "test",
                    "model": "model",
                    "invocation": "unit-test",
                    "run_reference": None,
                },
                "generated_at": "2026-08-10T00:00:00Z",
            },
        }

    def test_valid_record_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            evidence = root / "evidence.json"
            self._queue(queue)
            evidence.write_text(json.dumps(self._valid()), encoding="utf-8")
            report, passed = ev.validate(queue, evidence)
            self.assertTrue(passed, report)

    def test_pending_publishable_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            evidence = root / "evidence.json"
            self._queue(queue)
            data = self._valid()
            data["claims"][1]["publishable"] = True
            data["claims"][1]["source_ids"] = ["src1"]
            data["claims"][1]["caveats"] = ["Source does not resolve the claim."]
            evidence.write_text(json.dumps(data), encoding="utf-8")
            report, passed = ev.validate(queue, evidence)
            self.assertFalse(passed)
            self.assertTrue(any("PENDING" in error and "must not be publishable" in error for error in report["errors"]))

    def test_unknown_source_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            evidence = root / "evidence.json"
            self._queue(queue)
            data = self._valid()
            data["claims"][0]["source_ids"] = ["missing"]
            evidence.write_text(json.dumps(data), encoding="utf-8")
            report, passed = ev.validate(queue, evidence)
            self.assertFalse(passed)
            self.assertTrue(any("unknown source_ids" in error for error in report["errors"]))

    def test_screening_provenance_must_be_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            evidence = root / "evidence.json"
            self._queue(queue)
            data = self._valid()
            data["provenance"]["screening_decision"] = "MAYBE"
            data["provenance"]["verification_targets"] = ["different"]
            evidence.write_text(json.dumps(data), encoding="utf-8")
            report, passed = ev.validate(queue, evidence)
            self.assertFalse(passed)
            self.assertTrue(any("screening_decision" in error for error in report["errors"]))
            self.assertTrue(any("verification_targets" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
