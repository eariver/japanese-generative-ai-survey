from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import merge_screening_results as merge


class MergeScreeningResultsTests(unittest.TestCase):
    def _batch(self, path: Path, issue: str, ids: list[str]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            for screening_id in ids:
                fh.write(json.dumps({
                    "schema_version": "1.0",
                    "issue_id": issue,
                    "screening_id": screening_id,
                    "source_type": "paper",
                    "collector_id": "test",
                    "collector_run_id": "run",
                    "observed_at": "2026-08-10T00:00:00Z",
                    "title": screening_id,
                    "locator": f"https://example.com/{screening_id}",
                    "raw_paths": ["raw/test"],
                    "published_at": None,
                    "summary_text": "summary",
                    "metadata": {},
                }) + "\n")

    def _result(self, batch: Path, prompt: Path, decisions: list[tuple[str, str]]) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "batch_id": batch.stem,
            "input_batch_sha256": hashlib.sha256(batch.read_bytes()).hexdigest(),
            "prompt_id": "source-screening-v0.1",
            "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
            "runner": {
                "provider": "test",
                "model": "model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T00:00:00Z",
                "run_reference": None,
            },
            "decisions": [
                {
                    "screening_id": screening_id,
                    "decision": decision,
                    "reason": "reason",
                    "why_now": None,
                    "topic_lanes": [],
                    "duplicate_group": None,
                    "verification_targets": [] if decision == "DROP" else ["verify"],
                    "confidence": "medium",
                }
                for screening_id, decision in decisions
            ],
        }

    def test_partial_progress_is_allowed_and_queue_excludes_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batches = root / "batches"
            results = root / "results"
            out = root / "out"
            results.mkdir()
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            b1 = batches / "batch-001.jsonl"
            b2 = batches / "batch-002.jsonl"
            self._batch(b1, "2026-W32", ["a", "b"])
            self._batch(b2, "2026-W32", ["c"])
            (results / "batch-001.json").write_text(
                json.dumps(self._result(b1, prompt, [("a", "KEEP"), ("b", "DROP")])),
                encoding="utf-8",
            )

            manifest, passed = merge.merge(batches, results, prompt, out, require_complete=False)
            self.assertTrue(passed, manifest)
            self.assertFalse(manifest["complete"])
            self.assertEqual(manifest["missing_batches"], ["batch-002"])
            self.assertEqual(manifest["verification_queue_count"], 1)
            queue = [json.loads(line) for line in (out / "verification-queue.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual([item["screening_id"] for item in queue], ["a"])

    def test_require_complete_fails_when_batch_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batches = root / "batches"
            results = root / "results"
            out = root / "out"
            results.mkdir()
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            b1 = batches / "batch-001.jsonl"
            b2 = batches / "batch-002.jsonl"
            self._batch(b1, "2026-W32", ["a"])
            self._batch(b2, "2026-W32", ["b"])
            (results / "batch-001.json").write_text(
                json.dumps(self._result(b1, prompt, [("a", "KEEP")])), encoding="utf-8"
            )
            manifest, passed = merge.merge(batches, results, prompt, out, require_complete=True)
            self.assertFalse(passed)
            self.assertEqual(manifest["missing_batches"], ["batch-002"])


if __name__ == "__main__":
    unittest.main()
