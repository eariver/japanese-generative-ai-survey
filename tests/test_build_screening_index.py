from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_screening_index as si


class ScreeningIndexTests(unittest.TestCase):
    def _json(self, path: Path, data) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_builds_candidate_level_records_and_bounded_batches(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "intake"
            issue = "2026-W32"

            arxiv_dir = root / f"sources/{issue}/collectors/arxiv/runs/20260810T000000Z"
            self._json(
                arxiv_dir / "collector-run.json",
                {
                    "issue_id": issue,
                    "run_id": "arxiv-api-w32-test",
                    "collector": {"id": "arxiv-api"},
                    "time": {
                        "observed_at": "2026-08-10T00:00:00Z",
                        "collection_window_start": "2026-08-01T04:00:00Z",
                        "collection_window_end": "2026-08-10T14:40:00Z",
                    },
                },
            )
            self._json(
                arxiv_dir / "summary.json",
                {
                    "queries": [{"id": "cs-ai", "raw_path": f"sources/{issue}/collectors/arxiv/runs/20260810T000000Z/raw/cs-ai.atom"}],
                    "entries": [
                        {
                            "id": "http://arxiv.org/abs/2608.00001v1",
                            "title": "Paper One",
                            "summary": "First abstract",
                            "published": "2026-08-05T00:00:00Z",
                            "updated": "2026-08-05T00:00:00Z",
                            "authors": ["A"],
                            "categories": ["cs.AI"],
                            "primary_category": "cs.AI",
                            "links": [],
                        },
                        {
                            "id": "http://arxiv.org/abs/2608.00002v1",
                            "title": "Paper Two",
                            "summary": "Second abstract",
                            "published": "2026-08-06T00:00:00Z",
                            "updated": "2026-08-06T00:00:00Z",
                            "authors": ["B"],
                            "categories": ["cs.CL"],
                            "primary_category": "cs.CL",
                            "links": [],
                        },
                    ],
                },
            )

            gh_dir = root / f"sources/{issue}/collectors/github-releases/runs/20260810T000100Z"
            raw_path = f"sources/{issue}/collectors/github-releases/runs/20260810T000100Z/raw/example__repo.json"
            self._json(
                gh_dir / "collector-run.json",
                {
                    "issue_id": issue,
                    "run_id": "github-releases-w32-test",
                    "collector": {"id": "github-releases"},
                    "time": {"observed_at": "2026-08-10T00:01:00Z"},
                },
            )
            self._json(
                root / raw_path,
                [
                    {
                        "id": 123,
                        "tag_name": "v1.0.0",
                        "name": "Release One",
                        "html_url": "https://github.com/example/repo/releases/tag/v1.0.0",
                        "body": "Important serving changes",
                    }
                ],
            )
            self._json(
                gh_dir / "summary.json",
                {
                    "repositories": [{"repository": "example/repo", "raw_path": raw_path}],
                    "matching_releases": [
                        {
                            "repository": "example/repo",
                            "id": 123,
                            "tag_name": "v1.0.0",
                            "name": "Release One",
                            "html_url": "https://github.com/example/repo/releases/tag/v1.0.0",
                            "published_at": "2026-08-07T00:00:00Z",
                            "created_at": "2026-08-07T00:00:00Z",
                            "prerelease": False,
                        }
                    ],
                },
            )

            official_dir = root / f"sources/{issue}/collectors/official-pages/runs/20260810T000200Z"
            official_raw = f"sources/{issue}/collectors/official-pages/runs/20260810T000200Z/raw/vendor-rss.xml"
            official_full = root / official_raw
            official_full.parent.mkdir(parents=True, exist_ok=True)
            official_full.write_text(
                """<?xml version='1.0'?><rss><channel>
                <item><title>In Window</title><link>https://example.com/in</link><guid>in</guid><pubDate>Wed, 05 Aug 2026 12:00:00 GMT</pubDate><description>News</description></item>
                <item><title>Old</title><link>https://example.com/old</link><guid>old</guid><pubDate>Wed, 01 Jul 2026 12:00:00 GMT</pubDate><description>Old news</description></item>
                </channel></rss>""",
                encoding="utf-8",
            )
            self._json(
                official_dir / "collector-run.json",
                {
                    "issue_id": issue,
                    "run_id": "official-pages-w32-test",
                    "collector": {"id": "official-pages"},
                    "time": {
                        "observed_at": "2026-08-10T00:02:00Z",
                        "collection_window_start": "2026-08-01T04:00:00Z",
                        "collection_window_end": "2026-08-10T14:40:00Z",
                    },
                },
            )
            self._json(
                official_dir / "summary.json",
                {
                    "pages": [
                        {
                            "id": "vendor-rss",
                            "url": "https://example.com/rss.xml",
                            "raw_path": official_raw,
                            "bytes": official_full.stat().st_size,
                            "request": {"content_type": "text/xml"},
                        }
                    ]
                },
            )

            out = Path(tmp) / "screening"
            manifest = si.build(root, out, issue, max_records=2, max_chars=100000)

            self.assertEqual(manifest["record_count"], 4)
            self.assertEqual(manifest["counts_by_source_type"]["paper"], 2)
            self.assertEqual(manifest["counts_by_source_type"]["github-release"], 1)
            self.assertEqual(manifest["counts_by_source_type"]["official-feed-item"], 1)
            self.assertEqual(manifest["batch_count"], 2)

            records = [json.loads(line) for line in (out / "screening-index.jsonl").read_text(encoding="utf-8").splitlines()]
            ids = {record["screening_id"] for record in records}
            self.assertIn("arxiv:2608.00001v1", ids)
            self.assertIn("github-release:example/repo@v1.0.0", ids)
            self.assertNotIn("Old", {record["title"] for record in records})
            gh = next(record for record in records if record["source_type"] == "github-release")
            self.assertEqual(gh["summary_text"], "Important serving changes")
            self.assertEqual(gh["raw_paths"], [raw_path])

    def test_html_official_page_becomes_index_snapshot_not_fake_article(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "intake"
            issue = "2026-W32"
            run_dir = root / f"sources/{issue}/collectors/official-pages/runs/20260810T010000Z"
            raw_path = f"sources/{issue}/collectors/official-pages/runs/20260810T010000Z/raw/vendor.html"
            full = root / raw_path
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text("<html><title>Vendor News</title></html>", encoding="utf-8")
            self._json(
                run_dir / "collector-run.json",
                {
                    "issue_id": issue,
                    "run_id": "official-html-test",
                    "collector": {"id": "official-pages"},
                    "time": {"observed_at": "2026-08-10T01:00:00Z"},
                },
            )
            self._json(
                run_dir / "summary.json",
                {"pages": [{"id": "vendor", "url": "https://example.com/news", "raw_path": raw_path, "request": {"content_type": "text/html"}}]},
            )
            records = si.build_records(root, issue)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["source_type"], "official-index-snapshot")
            self.assertTrue(records[0]["metadata"]["requires_page_item_extraction"])


if __name__ == "__main__":
    unittest.main()
