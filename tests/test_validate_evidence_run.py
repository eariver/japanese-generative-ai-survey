from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_evidence_run as ver


class EvidenceRunValidationTests(unittest.TestCase):
    def _task(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": "evidence:2026-W32:test-task-1234567890",
            "task_type": "VERIFY_ITEM",
            "grouping": {"basis": "single-screening-item", "duplicate_group": None, "requires_confirmation": False},
            "screening_ids": ["screening:test"],
            "screening_decisions": ["KEEP"],
            "source_types": ["official-feed-item"],
            "locators": ["https://example.com/release"],
            "topic_lanes": ["A"],
            "why_now": ["new release"],
            "verification_targets": ["Verify release date.", "Verify benchmark conditions."],
            "status": "PENDING_VERIFICATION",
        }

    def _card(self, task: dict) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": task["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "status": "VERIFIED",
            "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
            "artifact": {
                "canonical_name": "Example Release",
                "artifact_type": "MODEL_UPDATE",
                "organization": "Example",
                "canonical_url": "https://example.com/release",
            },
            "temporal": {
                "artifact_first_announced": "2026-08-07",
                "observed_at": "2026-08-10T00:00:00Z",
                "events": [
                    {
                        "event_id": "event-release",
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
                    "url": "https://example.com/release",
                    "source_class": "PRIMARY_OFFICIAL",
                    "title": "Example Release",
                    "published_at": "2026-08-07",
                    "accessed_at": "2026-08-10T00:00:00Z",
                    "role": "official release note",
                }
            ],
            "claims": [
                {
                    "claim_id": "c1",
                    "text": "The update exists.",
                    "evidence_class": "PRIMARY_FACT",
                    "source_ids": ["s1"],
                    "context": None,
                }
            ],
            "metrics": [
                {
                    "metric_id": "m1",
                    "name": "benchmark",
                    "value": "42",
                    "unit": "points",
                    "context": "vendor benchmark setup",
                    "evidence_class": "VENDOR_CLAIM",
                    "source_ids": ["s1"],
                }
            ],
            "limitations": [
                {
                    "limitation_id": "l1",
                    "text": "No independent reproduction was verified.",
                    "evidence_class": "INFERENCE",
                    "source_ids": ["s1"],
                }
            ],
            "verification": {
                "targets": [
                    {
                        "target": "Verify release date.",
                        "status": "VERIFIED",
                        "finding": "Official release note is dated 2026-08-07.",
                        "source_ids": ["s1"],
                    },
                    {
                        "target": "Verify benchmark conditions.",
                        "status": "VERIFIED",
                        "finding": "Official note provides the benchmark setup.",
                        "source_ids": ["s1"],
                    },
                ],
                "unresolved_questions": [],
                "contradictions": [],
            },
            "editorial": {
                "why_now_confirmed": True,
                "why_now_note": "Official update is in-window.",
                "candidate_recommendation": "CANDIDATE",
                "rationale": "Primary source confirms a technical update.",
            },
        }

    def _run(self, task_path: Path, prompt_path: Path, card: dict) -> dict:
        task = json.loads(task_path.read_text())
        return {
            "schema_version": "1.0",
            "issue_id": task["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "evidence_task_sha256": hashlib.sha256(task_path.read_bytes()).hexdigest(),
            "prompt_id": "primary-source-verification-v0.1",
            "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
            "runner": {
                "provider": "test",
                "model": "test-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T00:00:00Z",
                "run_reference": None,
            },
            "card": card,
        }

    def test_valid_evidence_run_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_path = root / "task.json"
            task = self._task()
            task_path.write_text(json.dumps(task), encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            run_path = root / "run.json"
            run_path.write_text(json.dumps(self._run(task_path, prompt, self._card(task))), encoding="utf-8")
            report, passed = ver.validate(task_path, run_path, prompt)
            self.assertTrue(passed, report)
            self.assertEqual(report["source_count"], 1)
            self.assertEqual(report["event_count"], 1)

    def test_unknown_source_and_missing_target_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_path = root / "task.json"
            task = self._task()
            task_path.write_text(json.dumps(task), encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            card = self._card(task)
            card["claims"][0]["source_ids"] = ["unknown"]
            card["verification"]["targets"] = card["verification"]["targets"][:1]
            run_path = root / "run.json"
            run_path.write_text(json.dumps(self._run(task_path, prompt, card)), encoding="utf-8")
            report, passed = ver.validate(task_path, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("unknown source IDs" in error for error in report["errors"]))
            self.assertTrue(any("not addressed" in error for error in report["errors"]))

    def test_duplicate_event_id_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_path = root / "task.json"
            task = self._task()
            task_path.write_text(json.dumps(task), encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            card = self._card(task)
            card["temporal"]["events"].append(dict(card["temporal"]["events"][0]))
            run_path = root / "run.json"
            run_path.write_text(json.dumps(self._run(task_path, prompt, card)), encoding="utf-8")
            report, passed = ver.validate(task_path, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("duplicate event_id" in error for error in report["errors"]))

    def test_task_hash_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_path = root / "task.json"
            task = self._task()
            task_path.write_text(json.dumps(task), encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            data = self._run(task_path, prompt, self._card(task))
            data["evidence_task_sha256"] = "0" * 64
            run_path = root / "run.json"
            run_path.write_text(json.dumps(data), encoding="utf-8")
            report, passed = ver.validate(task_path, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("evidence_task_sha256" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
