from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v2 as repair


class HistoricalH2TaxonomyRepairTests(unittest.TestCase):
    def test_partial_labels_are_normalized_before_final_validation(self) -> None:
        rendered = repair.translate_historical_h2_taxonomy(
            "2025-10-06 (製品 TOOLING（公開）); 2025-09-15 (CODING Agent（更新）)"
        )
        self.assertIn("製品ツール（公開）", rendered)
        self.assertIn("Coding Agent（更新）", rendered)
        self.assertNotIn("TOOLING", rendered)
        self.assertNotIn("CODING Agent", rendered)


if __name__ == "__main__":
    unittest.main()
