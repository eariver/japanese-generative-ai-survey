from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import materialize_candidate_records as mcr


class CandidateMaterializationTests(unittest.TestCase):
    def _item(self, recommendation: str = "CANDIDATE", status: str = "VERIFIED", split: bool = False) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": "evidence:2026-W32:example-12345678",
            "task_file": "example.json",
            "run_file": "example.json",
            "runner": {"provider": "test", "model": "model", "invocation": "unit", "generated_at": "2026-08-10T00:00:00Z"},
            "evidence_task_sha256": "0" * 64,
            "prompt_id": "primary-source-verification-v0.1",
            "prompt_sha256": "1" * 64,
            "card": {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "evidence_task_id": "evidence:2026-W32:example-12345678",
                "status": status,
                "grouping_resolution": {"accepted": not split, "split_recommended": split, "note": None},
                "artifact": {
                    "canonical_name": "Example Model Update",
                    "artifact_type": "MODEL_UPDATE",
                    "organization": "Example Org",
                    "canonical_url": "https://example.com/update",
                },
                "temporal": {
                    "artifact_first_announced": "2026-08-07",
                    "observed_at": "2026-08-10T00:00:00Z",
                    "events": [
                        {
                            "event_type": "MODEL_UPDATE",
                            "event_date": "2026-08-07",
                            "source_published_at": "2026-08-07",
                            "source_ids": ["s1"],
                        }
                    ],
                },
                "sources": [
                    {
                        "source_id": "s1",
                        "url": "https://example.com/update",
                        "source_class": "PRIMARY_OFFICIAL",
                        "title": "Example update",
                        "published_at": "2026-08-07",
                        "accessed_at": "2026-08-10T00:00:00Z",
                        "role": "official release note",
                    }
                ],
                "claims": [
                    {
                        "claim_id": "c1",
                        "text": "A new update exists.",
                        "evidence_class": "PRIMARY_FACT",
                        "source_ids": ["s1"],
                        "context": None,
                    }
                ],
                "metrics": [
                    {
                        "metric_id": "m1",
                        "name": "throughput",
                        "value": "2",
                        "unit": "x",
                        "context": "project benchmark",
                        "evidence_class": "PROJECT_CLAIM",
                        "source_ids": ["s1"],
                    }
                ],
                "limitations": [
                    {
                        "limitation_id": "l1",
                        "text": "No independent reproduction.",
                        "evidence_class": "INFERENCE",
                        "source_ids": ["s1"],
                    }
                ],
                "verification": {
                    "targets": [
                        {
                            "target": "Verify release.",
                            "status": "VERIFIED",
                            "finding": "Official note confirms it.",
                            "source_ids": ["s1"],
                        }
                    ],
                    "unresolved_questions": ["Independent performance remains unresolved."],
                    "contradictions": [],
                },
                "editorial": {
                    "why_now_confirmed": True,
                    "why_now_note": "in-window update",
                    "candidate_recommendation": recommendation,
                    "rationale": "Technically relevant update.",
                },
            },
        }

    def _write_jsonl(self, path: Path, items: list[dict]) -> None:
        path.write_text("".join(json.dumps(item) + "\n" for item in items), encoding="utf-8")

    def test_candidate_record_is_materialized_with_evidence_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "candidate-ready.jsonl"
            self._write_jsonl(source, [self._item()])
            out = root / "out"
            index, passed = mcr.materialize(source, out)
            self.assertTrue(passed, index)
            self.assertEqual(index["record_count"], 1)
            record = index["records"][0]
            text = (out / record["file"]).read_text(encoding="utf-8")
            self.assertIn("record_type: pre-selection-candidate", text)
            self.assertIn("Candidate-ready does not mean selected", text)
            self.assertIn("**PROJECT_CLAIM**", text)
            self.assertIn("Independent performance remains unresolved.", text)

    def test_non_candidate_recommendation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "candidate-ready.jsonl"
            self._write_jsonl(source, [self._item(recommendation="HOLD")])
            index, passed = mcr.materialize(source, root / "out")
            self.assertFalse(passed)
            self.assertEqual(index["record_count"], 0)

    def test_split_recommended_is_rejected_before_materialization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "candidate-ready.jsonl"
            self._write_jsonl(source, [self._item(split=True)])
            index, passed = mcr.materialize(source, root / "out")
            self.assertFalse(passed)
            self.assertTrue(any("grouping split" in error for error in index["errors"]))


if __name__ == "__main__":
    unittest.main()
