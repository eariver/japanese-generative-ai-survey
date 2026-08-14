from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import fill_special_reader_notes_ja as fill_notes
from scripts import postprocess_special_reader_facing_notes as taxonomy
from scripts import revise_special_adaptive_spacing as router
from scripts import revise_special_half_year_review_repairs_v2 as half_year_v2


class HalfYearReviewRepairTests(unittest.TestCase):
    def marker(self, root: Path, changes: dict) -> None:
        path = root / "sources/SP-TEST/editorial/layout-revision-v0.7.json"
        path.parent.mkdir(parents=True)
        path.write_text(
            json.dumps({"issue_id": "SP-TEST", "revision": "v0.7", "layout_changes": changes}),
            encoding="utf-8",
        )

    def test_half_year_marker_routes_to_duplicate_safe_builder(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.marker(root, {"half_year_review_repairs": True})
            expected = {"mode": "half-year"}
            with patch(
                "scripts.revise_special_half_year_review_repairs_v2.build",
                return_value=expected,
            ) as mocked:
                actual = router.build(root, "test", "SP-TEST", "v0.7")
            self.assertEqual(actual, expected)
            mocked.assert_called_once_with(root, "test", "SP-TEST", "v0.7")

    def test_duplicate_generic_fallbacks_replace_in_source_order(self) -> None:
        phrase = half_year_v2.core._GENERIC_FALLBACKS[0]
        old = r"\item \textbf{一次情報で確認できる事実}: Exampleについて、" + phrase + "。"
        block = "\n".join([old, old])
        revised, count = half_year_v2.replace_generic_items(
            block,
            "Example",
            {
                "Example": [
                    {"label": "一次情報で確認できる事実", "text_ja": "一つ目の具体的事実。"},
                    {"label": "一次情報で確認できる事実", "text_ja": "二つ目の具体的事実。"},
                ]
            },
        )
        self.assertEqual(count, 2)
        self.assertIn("一つ目の具体的事実", revised)
        self.assertIn("二つ目の具体的事実", revised)
        self.assertNotIn(phrase, revised)

    def test_h2_taxonomy_examples_are_reader_facing(self) -> None:
        source = "\n".join(
            [
                "時系列 & 2025-08-07 (SAFETY_METHOD_PUBLICATION)",
                "時系列 & 2025-11-19 (CODING_MODEL_RELEASE)",
                "時系列 & 2025-08-05 (GENIE_3_ANNOUNCEMENT)",
                "時系列 & 2025-09-30 (VIDEO_AUDIO_MODEL_RELEASE)",
                "時系列 & 2025-07-24 (RUNTIME_RELEASE)",
                "時系列 & 2025-08-27 (CROSS_LAB_SAFETY_EVALUATION)",
            ]
        )
        rendered = taxonomy.translate_machine_labels_compat(source)
        self.assertIn("安全手法（公開）", rendered)
        self.assertIn("Codingモデル（公開）", rendered)
        self.assertIn("Genie 3（発表）", rendered)
        self.assertIn("映像・音声モデル（公開）", rendered)
        self.assertIn("Runtime（公開）", rendered)
        self.assertIn("複数組織安全性評価", rendered)
        self.assertNotIn("技術イベント", rendered)
        self.assertEqual(taxonomy.reader_taxonomy_findings(rendered), [])

    def test_missing_reader_summary_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            summary = root / "summary.json"
            summary.write_text(
                json.dumps(
                    {
                        "issue_id": "SP-TEST",
                        "records": [
                            {
                                "evidence_task_id": "evidence:test",
                                "artifact_name": "Example",
                                "claims": [
                                    {
                                        "item_id": "claim-1",
                                        "evidence_class": "PRIMARY_FACT",
                                        "source_text_sha256": "unused-before-fail",
                                        "text_ja": "",
                                    }
                                ],
                                "limitations": [],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "missing reviewed Japanese Technical Notes summaries"):
                fill_notes.run(root, "SP-TEST", summary, root / "missing-overrides")


if __name__ == "__main__":
    unittest.main()
