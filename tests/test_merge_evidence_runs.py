from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import merge_evidence_runs as mer


class MergeEvidenceRunsTests(unittest.TestCase):
    def _task(self, task_id: str, target: str) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": task_id,
            "task_type": "VERIFY_ITEM",
            "grouping": {"basis": "single-screening-item", "duplicate_group": None, "requires_confirmation": False},
            "screening_ids": [task_id],
            "screening_decisions": ["KEEP"],
            "source_types": ["official-feed-item"],
            "locators": ["https://example.com/release"],
            "topic_lanes": ["A"],
            "why_now": ["new release"],
            "verification_targets": [target],
            "status": "PENDING_VERIFICATION",
        }

    def _card(self, task: dict, recommendation: str, status: str = "VERIFIED") -> dict:
        target = task["verification_targets"][0]
        return {
            "schema_version": "1.0",
            "issue_id": task["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "status": status,
            "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
            "artifact": {
                "canonical_name": task["evidence_task_id"],
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
                    "text": "The release exists.",
                    "evidence_class": "PRIMARY_FACT",
                    "source_ids": ["s1"],
                    "context": None,
                }
            ],
            "metrics": [
                {
                    "metric_id": "m1",
                    "name": "project measurement",
                    "value": "42",
                    "unit": "points",
                    "context": "project-provided test setup",
                    "evidence_class": "PROJECT_CLAIM",
                    "source_ids": ["s1"],
                }
            ],
            "limitations": [],
            "verification": {
                "targets": [
                    {
                        "target": target,
                        "status": "VERIFIED",
                        "finding": "Primary source addressed the target.",
                        "source_ids": ["s1"],
                    }
                ],
                "unresolved_questions": [],
                "contradictions": [],
            },
            "editorial": {
                "why_now_confirmed": recommendation == "CANDIDATE",
                "why_now_note": "in-window" if recommendation == "CANDIDATE" else None,
                "candidate_recommendation": recommendation,
                "rationale": "routing test",
            },
        }

    def _write_task(self, tasks: Path, filename: str, task: dict) -> Path:
        path = tasks / filename
        tasks.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(task), encoding="utf-8")
        return path

    def _write_run(self, runs: Path, task_path: Path, prompt: Path, card: dict) -> None:
        task = json.loads(task_path.read_text())
        value = {
            "schema_version": "1.0",
            "issue_id": task["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "evidence_task_sha256": hashlib.sha256(task_path.read_bytes()).hexdigest(),
            "prompt_id": "primary-source-verification-v0.1",
            "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
            "runner": {
                "provider": "test",
                "model": "test-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T00:00:00Z",
                "run_reference": None,
            },
            "card": card,
        }
        runs.mkdir(parents=True, exist_ok=True)
        (runs / task_path.name).write_text(json.dumps(value), encoding="utf-8")

    def test_partial_merge_routes_candidate_and_hold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = root / "tasks"
            runs = root / "runs"
            out = root / "out"
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")

            t1 = self._task("evidence:2026-W32:candidate-12345678", "Verify candidate.")
            t2 = self._task("evidence:2026-W32:hold-12345678", "Verify hold.")
            t3 = self._task("evidence:2026-W32:missing-12345678", "Verify missing.")
            p1 = self._write_task(tasks, "candidate.json", t1)
            p2 = self._write_task(tasks, "hold.json", t2)
            self._write_task(tasks, "missing.json", t3)
            self._write_run(runs, p1, prompt, self._card(t1, "CANDIDATE"))
            self._write_run(runs, p2, prompt, self._card(t2, "HOLD", status="PARTIAL"))

            manifest, passed = mer.merge(tasks, runs, prompt, out, require_complete=False)
            self.assertTrue(passed, manifest)
            self.assertFalse(manifest["complete"])
            self.assertEqual(manifest["validated_run_count"], 2)
            self.assertEqual(manifest["candidate_ready_count"], 1)
            self.assertEqual(manifest["hold_count"], 1)
            self.assertEqual(manifest["missing_run_files"], ["missing.json"])
            candidate = [json.loads(line) for line in (out / "candidate-ready.jsonl").read_text().splitlines()]
            self.assertEqual(candidate[0]["evidence_task_id"], t1["evidence_task_id"])

    def test_require_complete_fails_with_missing_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = root / "tasks"
            runs = root / "runs"
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            self._write_task(tasks, "missing.json", self._task("evidence:2026-W32:missing-12345678", "Verify."))
            manifest, passed = mer.merge(tasks, runs, prompt, root / "out", require_complete=True)
            self.assertFalse(passed)
            self.assertEqual(manifest["validated_run_count"], 0)

    def test_invalid_run_blocks_even_partial_merge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = root / "tasks"
            runs = root / "runs"
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            task = self._task("evidence:2026-W32:invalid-12345678", "Verify invalid.")
            task_path = self._write_task(tasks, "invalid.json", task)
            self._write_run(runs, task_path, prompt, self._card(task, "CANDIDATE"))
            value = json.loads((runs / "invalid.json").read_text())
            value["evidence_task_sha256"] = "0" * 64
            (runs / "invalid.json").write_text(json.dumps(value), encoding="utf-8")
            manifest, passed = mer.merge(tasks, runs, prompt, root / "out", require_complete=False)
            self.assertFalse(passed)
            self.assertEqual(len(manifest["invalid_runs"]), 1)


if __name__ == "__main__":
    unittest.main()
