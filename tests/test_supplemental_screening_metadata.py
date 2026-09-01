from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_screening_index as si


class SupplementalScreeningMetadataTests(unittest.TestCase):
    def _json(self, path: Path, data) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_supplemental_item_retains_identity_date_and_derived_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "intake"
            issue = "SP-2024-H2"
            run_dir = root / f"sources/{issue}/collectors/official-pages/runs/20260814T130000Z"
            raw_path = f"sources/{issue}/collectors/official-pages/runs/20260814T130000Z/raw/supplemental-example.html"
            full = root / raw_path
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text(
                "<html><head><title>Example Release</title><style>ignore me</style></head>"
                "<body><h1>Example Release</h1><p>Important model and deployment details.</p>"
                "<script>ignore()</script></body></html>",
                encoding="utf-8",
            )
            self._json(
                run_dir / "collector-run.json",
                {
                    "issue_id": issue,
                    "run_id": "official-pages-supplemental-test",
                    "collector": {"id": "official-pages"},
                    "time": {
                        "observed_at": "2026-08-14T13:00:00Z",
                        "collection_window_start": "2024-07-01T00:00:00Z",
                        "collection_window_end": "2024-12-31T23:59:59Z",
                    },
                },
            )
            self._json(
                run_dir / "summary.json",
                {
                    "collection_mode": "SUPPLEMENTAL_COVERAGE_GAP_FILL",
                    "pages": [
                        {
                            "id": "supplemental-example",
                            "title": "Example Release",
                            "publisher": "Example Vendor",
                            "url": "https://example.com/release",
                            "published_at": "2024-08-22T00:00:00Z",
                            "coverage_gap_reason": "Missing from base watchlist.",
                            "supplemental": True,
                            "raw_path": raw_path,
                            "bytes": full.stat().st_size,
                            "request": {"content_type": "text/html"},
                            "metadata": {"source_kind": "release"},
                        }
                    ],
                },
            )

            records = si.build_records(root, issue)
            self.assertEqual(len(records), 1)
            record = records[0]
            self.assertEqual(record["screening_id"], "official-index:supplemental-example")
            self.assertEqual(record["title"], "Example Release")
            self.assertEqual(record["published_at"], "2024-08-22T00:00:00Z")
            self.assertIn("Important model and deployment details.", record["summary_text"])
            self.assertNotIn("ignore()", record["summary_text"])
            self.assertTrue(record["metadata"]["supplemental"])
            self.assertFalse(record["metadata"]["requires_page_item_extraction"])
            self.assertEqual(record["metadata"]["publisher"], "Example Vendor")
            self.assertEqual(record["metadata"]["coverage_gap_reason"], "Missing from base watchlist.")


if __name__ == "__main__":
    unittest.main()
