from __future__ import annotations

import unittest

from scripts import revise_special_half_year_reader_quality_cleanup as cleanup


class HalfYearReaderQualityCleanupTests(unittest.TestCase):
    def test_exact_appended_suffix_is_removed_once(self) -> None:
        point = "MobileLLMはdeep-and-thinなTransformer構成を中心に探索した。"
        payload = "選定済み一次資料では、" + point + " " + point
        revised, count = cleanup._dedup_fact_payload(payload)
        self.assertEqual(count, 1)
        self.assertEqual(revised, "選定済み一次資料では、" + point)

    def test_unrelated_fact_suffix_is_preserved(self) -> None:
        payload = "時系列上の事実。 追加の技術点。"
        revised, count = cleanup._dedup_fact_payload(payload)
        self.assertEqual(count, 0)
        self.assertEqual(revised, payload)

    def test_chronology_dash_and_date_order_are_reader_normalized(self) -> None:
        source = (
            "時系列 & — \\\\\n"
            "Artifact & 2024-06-21, 2024-03-04 \\\\\n"
        )
        revised, dashes, sorted_rows = cleanup._normalize_chronology_metadata(source)
        self.assertEqual(dashes, 1)
        self.assertEqual(sorted_rows, 1)
        self.assertIn("時系列 & 年表対象日付なし", revised)
        self.assertIn("2024-03-04, 2024-06-21", revised)

    def test_one_needspace_guard_per_technical_note(self) -> None:
        source = "\\begin{technicalnote}{A}{x}\n\\end{technicalnote}\n\\begin{technicalnote}{B}{x}\n\\end{technicalnote}\n"
        revised, count = cleanup._guard_cards(source)
        self.assertEqual(count, 2)
        self.assertEqual(revised.count(cleanup.NEEDSPACE), 2)
        revised2, count2 = cleanup._guard_cards(revised)
        self.assertEqual(count2, 2)
        self.assertEqual(revised2, revised)


if __name__ == "__main__":
    unittest.main()
