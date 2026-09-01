from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import prepare_screening_run as prepare


class PrepareScreeningRunTests(unittest.TestCase):
    ISSUE = "2026-W33"
    COMMIT = "1" * 40

    def _write_json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def _fixture(self, root: Path) -> None:
        self._write_json(
            root / "sources" / self.ISSUE / "pipeline-state.json",
            {"schema_version": "1.0", "issue_id": self.ISSUE},
        )
        self._write_json(
            root / "sources" / self.ISSUE / "raw-index.json",
            {"schema_version": "1.0", "issue_id": self.ISSUE, "entries": []},
        )
        prompt = root / "config" / "prompts" / "screening" / "source-screening-v0.1.md"
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text("screen only supplied records\n", encoding="utf-8")
        self._write_json(root / "schemas" / "screening-batch-result.schema.json", {"type": "object"})

        run_dir = (
            root
            / "sources"
            / self.ISSUE
            / "collectors"
            / "official-pages"
            / "runs"
            / "2026-08-15T09-00-00Z"
        )
        raw = run_dir / "raw" / "openai-news.xml"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text(
            "<?xml version='1.0'?><rss><channel><item>"
            "<title>Example model release</title>"
            "<link>https://example.com/release</link>"
            "<guid>example-release</guid>"
            "<pubDate>Sat, 15 Aug 2026 00:30:00 GMT</pubDate>"
            "<description>Technical release details.</description>"
            "</item></channel></rss>",
            encoding="utf-8",
        )
        self._write_json(
            run_dir / "collector-run.json",
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "run_id": "official-pages:2026-08-15T09-00-00Z",
                "collector": {"id": "official-pages"},
                "time": {
                    "observed_at": "2026-08-15T09:00:00Z",
                    "collection_window_start": "2026-08-09T14:40:00Z",
                    "collection_window_end": "2026-08-15T09:00:00Z",
                },
            },
        )
        self._write_json(
            run_dir / "summary.json",
            {
                "pages": [
                    {
                        "id": "openai-news",
                        "url": "https://example.com/news",
                        "raw_path": raw.relative_to(root).as_posix(),
                        "bytes": raw.stat().st_size,
                        "request": {"content_type": "application/rss+xml"},
                    }
                ]
            },
        )

    def test_builds_deterministic_pinned_screening_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            first = prepare.build_package(
                repo_root=root,
                output_root=root / "out1",
                issue_id=self.ISSUE,
                source_ref=f"weekly/{self.ISSUE}-work",
                source_commit=self.COMMIT,
            )
            second = prepare.build_package(
                repo_root=root,
                output_root=root / "out2",
                issue_id=self.ISSUE,
                source_ref=f"weekly/{self.ISSUE}-work",
                source_commit=self.COMMIT,
            )
            self.assertEqual(first, second)
            self.assertEqual(first["source"]["commit_sha"], self.COMMIT)
            self.assertEqual(first["screening_input"]["record_count"], 1)
            self.assertEqual(len(first["screening_input"]["batches"]), 1)
            batch = first["screening_input"]["batches"][0]
            self.assertEqual(batch["batch_id"], "batch-001")
            self.assertEqual(batch["path"], "input/batches/batch-001.jsonl")
            self.assertTrue((root / "out1" / batch["path"]).is_file())
            self.assertTrue((root / "out1" / first["prompt"]["path"]).is_file())
            self.assertTrue((root / "out1" / first["result_contract"]["path"]).is_file())

    def test_rejects_pipeline_state_or_raw_index_issue_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            state = root / "sources" / self.ISSUE / "pipeline-state.json"
            self._write_json(state, {"issue_id": "2026-W32"})
            with self.assertRaisesRegex(ValueError, "pipeline state issue_id mismatch"):
                prepare.build_package(
                    repo_root=root,
                    output_root=root / "out",
                    issue_id=self.ISSUE,
                    source_ref="main",
                    source_commit=self.COMMIT,
                )

            self._write_json(state, {"issue_id": self.ISSUE})
            raw_index = root / "sources" / self.ISSUE / "raw-index.json"
            self._write_json(raw_index, {"issue_id": "2026-W32"})
            with self.assertRaisesRegex(ValueError, "raw index issue_id mismatch"):
                prepare.build_package(
                    repo_root=root,
                    output_root=root / "out",
                    issue_id=self.ISSUE,
                    source_ref="main",
                    source_commit=self.COMMIT,
                )

    def test_rejects_empty_normalized_screening_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            collectors = root / "sources" / self.ISSUE / "collectors"
            shutil.rmtree(collectors)
            collectors.mkdir(parents=True, exist_ok=True)
            with self.assertRaisesRegex(ValueError, "produced no records/batches"):
                prepare.build_package(
                    repo_root=root,
                    output_root=root / "out",
                    issue_id=self.ISSUE,
                    source_ref="main",
                    source_commit=self.COMMIT,
                )


if __name__ == "__main__":
    unittest.main()
