from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_screening_result as vsr


class ScreeningResultValidationTests(unittest.TestCase):
    def _write_batch(self, root: Path) -> Path:
        batch = root / "batch-001.jsonl"
        records = [
            {"schema_version": "1.0", "issue_id": "2026-W32", "screening_id": "a"},
            {"schema_version": "1.0", "issue_id": "2026-W32", "screening_id": "b"},
        ]
        batch.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
        return batch

    def _decision(self, screening_id: str, decision: str = "KEEP") -> dict:
        return {
            "screening_id": screening_id,
            "decision": decision,
            "reason": "Supported by supplied metadata.",
            "why_now": None,
            "topic_lanes": ["A"] if decision != "DROP" else [],
            "duplicate_group": None,
            "verification_targets": ["Verify primary source."] if decision != "DROP" else [],
            "confidence": "medium",
        }

    def _result(self, batch: Path, prompt: Path, decisions: list[dict]) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "batch_id": "batch-001",
            "input_batch_sha256": hashlib.sha256(batch.read_bytes()).hexdigest(),
            "prompt_id": "source-screening-v0.1",
            "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
            "runner": {
                "provider": "test",
                "model": "test-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T06:00:00Z",
                "run_reference": None,
            },
            "decisions": decisions,
        }

    def test_complete_result_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = self._write_batch(root)
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            result_path = root / "result.json"
            result_path.write_text(
                json.dumps(self._result(batch, prompt, [self._decision("a"), self._decision("b", "DROP")])),
                encoding="utf-8",
            )
            report, passed = vsr.validate(batch, result_path, prompt)
            self.assertTrue(passed, report)
            self.assertEqual(report["decision_count"], 2)
            self.assertEqual(report["decision_counts"]["KEEP"], 1)
            self.assertEqual(report["decision_counts"]["DROP"], 1)

    def test_missing_and_duplicate_decisions_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = self._write_batch(root)
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            result_path = root / "result.json"
            result_path.write_text(
                json.dumps(self._result(batch, prompt, [self._decision("a"), self._decision("a")])),
                encoding="utf-8",
            )
            report, passed = vsr.validate(batch, result_path, prompt)
            self.assertFalse(passed)
            self.assertEqual(report["missing_screening_ids"], ["b"])
            self.assertEqual(report["duplicate_output_screening_ids"], ["a"])

    def test_hash_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = self._write_batch(root)
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            data = self._result(batch, prompt, [self._decision("a"), self._decision("b")])
            data["input_batch_sha256"] = "0" * 64
            result_path = root / "result.json"
            result_path.write_text(json.dumps(data), encoding="utf-8")
            report, passed = vsr.validate(batch, result_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("input_batch_sha256" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
