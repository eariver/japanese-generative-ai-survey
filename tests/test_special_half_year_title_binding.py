from __future__ import annotations

import unittest
from pathlib import Path

from scripts import revise_special_half_year_review_repairs_v4 as repair


class HalfYearTechnicalNoteTitleBindingTests(unittest.TestCase):
    def test_tex_escaped_title_alias_binds_to_same_evidence(self) -> None:
        original = repair._ORIGINAL_MERGE
        try:
            repair._ORIGINAL_MERGE = lambda _root, _manifest: {
                "Methods & Insights": {
                    "organization": "Example Lab",
                    "artifact_type": "PAPER",
                    "events": [("2024-08-01", "PAPER_RELEASE")],
                    "urls": ["https://example.com/paper"],
                }
            }
            index = repair.merge_evidence_index(Path("."), {})
        finally:
            repair._ORIGINAL_MERGE = original
        self.assertIn(r"Methods \& Insights", index)
        self.assertIs(index["Methods & Insights"], index[r"Methods \& Insights"])
        self.assertEqual(index[r"Methods \& Insights"]["canonical_title"], "Methods & Insights")

    def test_source_specific_fact_uses_canonical_unescaped_title(self) -> None:
        info = {
            "canonical_title": "Methods & Insights",
            "organization": "Example Lab",
            "events": [("2024-08-01", "PAPER_RELEASE")],
        }
        text = repair.source_specific_fact(r"Methods \& Insights", info)
        self.assertIn("Methods & Insights", text)
        self.assertNotIn(r"Methods \& Insights", text)


if __name__ == "__main__":
    unittest.main()
