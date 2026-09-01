from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_evidence_tasks as bet


class EvidenceTaskBuilderTests(unittest.TestCase):
    def _item(
        self,
        screening_id: str,
        decision: str,
        *,
        source_type: str = "github-release",
        duplicate_group: str | None = None,
    ) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "batch_id": "batch-001",
            "screening_id": screening_id,
            "record": {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "screening_id": screening_id,
                "source_type": source_type,
                "collector_id": "test",
                "collector_run_id": "run",
                "observed_at": "2026-08-10T00:00:00Z",
                "title": screening_id,
                "locator": f"https://example.com/{screening_id}",
                "raw_paths": ["raw/test"],
                "published_at": "2026-08-07T00:00:00Z",
                "summary_text": "summary",
                "metadata": {},
            },
            "screening": {
                "screening_id": screening_id,
                "decision": decision,
                "reason": "reason",
                "why_now": "new support" if decision != "INSPECT" else None,
                "topic_lanes": ["H"] if source_type == "github-release" else [],
                "duplicate_group": duplicate_group,
                "verification_targets": ["Verify primary source."],
                "confidence": "medium",
            },
        }

    def _write_queue(self, path: Path, items: list[dict]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            for item in items:
                fh.write(json.dumps(item) + "\n")

    def _assert_task_file_manifest(self, out: Path, manifest: dict) -> None:
        self.assertEqual(len(manifest["task_files"]), manifest["evidence_task_count"])
        for entry in manifest["task_files"]:
            path = out / entry["path"]
            self.assertTrue(path.is_file(), entry)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"])
            self.assertEqual(path.stat().st_size, entry["bytes"])
            task = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(task["evidence_task_id"], entry["evidence_task_id"])

    def test_duplicate_group_becomes_unconfirmed_series_task(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            self._write_queue(
                queue,
                [
                    self._item("a", "KEEP", duplicate_group="llama.cpp-deepseek"),
                    self._item("b", "MAYBE", duplicate_group="llama.cpp-deepseek"),
                    self._item("c", "KEEP"),
                ],
            )
            out = root / "out"
            manifest, passed = bet.build(queue, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["input_queue_count"], 3)
            self.assertEqual(manifest["evidence_task_count"], 2)
            self.assertEqual(manifest["task_type_counts"]["VERIFY_SERIES"], 1)
            tasks = [json.loads(line) for line in (out / "evidence-tasks.jsonl").read_text().splitlines()]
            series = next(task for task in tasks if task["task_type"] == "VERIFY_SERIES")
            self.assertEqual(series["screening_ids"], ["a", "b"])
            self.assertTrue(series["grouping"]["requires_confirmation"])
            self.assertEqual(series["grouping"]["basis"], "llm-duplicate-group")
            self._assert_task_file_manifest(out, manifest)

    def test_singleton_duplicate_hint_stays_verify_item(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            self._write_queue(
                queue,
                [self._item("a", "MAYBE", duplicate_group="series-may-have-more-members")],
            )
            out = root / "out"
            manifest, passed = bet.build(queue, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["task_type_counts"]["VERIFY_SERIES"], 0)
            task = json.loads((out / "evidence-tasks.jsonl").read_text().strip())
            self.assertEqual(task["task_type"], "VERIFY_ITEM")
            self.assertEqual(task["grouping"]["basis"], "llm-duplicate-group")
            self.assertTrue(task["grouping"]["requires_confirmation"])
            self.assertEqual(task["grouping"]["duplicate_group"], "series-may-have-more-members")
            self._assert_task_file_manifest(out, manifest)

    def test_inspect_snapshot_becomes_index_inspection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            self._write_queue(
                queue,
                [self._item("index", "INSPECT", source_type="official-index-snapshot")],
            )
            out = root / "out"
            manifest, passed = bet.build(queue, out)
            self.assertTrue(passed, manifest)
            task = json.loads((out / "evidence-tasks.jsonl").read_text().strip())
            self.assertEqual(task["task_type"], "INSPECT_INDEX")
            self.assertFalse(task["grouping"]["requires_confirmation"])
            self._assert_task_file_manifest(out, manifest)

    def test_non_promoted_decision_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = root / "queue.jsonl"
            self._write_queue(queue, [self._item("drop", "DROP")])
            with self.assertRaises(ValueError):
                bet.build(queue, root / "out")


if __name__ == "__main__":
    unittest.main()
