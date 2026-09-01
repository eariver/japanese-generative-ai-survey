from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v11 as repair


class HalfYearTechnicalNoteSuppressionV11Tests(unittest.TestCase):
    def test_suppression_requires_exact_urls_and_reason(self) -> None:
        info = {"urls": ["https://example.com/item"]}
        with self.assertRaisesRegex(ValueError, "requires suppression_reason"):
            repair._validate_override_with_suppression(
                "Thin item",
                {"source_urls": ["https://example.com/item"], "suppress_reader_facing_card": True},
                info,
            )
        with self.assertRaisesRegex(ValueError, "URL mismatch"):
            repair._validate_override_with_suppression(
                "Thin item",
                {
                    "source_urls": ["https://example.com/other"],
                    "suppress_reader_facing_card": True,
                    "suppression_reason": "Accepted raw has bibliographic identity only.",
                },
                info,
            )

    def test_suppression_removes_card_and_glance_row_only(self) -> None:
        text = (
            "\\begin{tabularx}{\\linewidth}{X X}\n"
            "Thin item & 主要資料 & モデル & 2024-07-18 \\\\\n"
            "Rich item & 主要資料 & API & 2024-10-01 \\\\\n"
            "\\end{tabularx}\n"
            "\\begin{technicalnote}{Thin item}{主要資料}\n"
            "\\item \\textbf{一次情報で確認できる事実}: title/date only\n"
            "\\end{technicalnote}\n"
            "\\begin{technicalnote}{Rich item}{主要資料}\n"
            "\\item \\textbf{一次情報で確認できる事実}: concrete\n"
            "\\end{technicalnote}\n"
        )
        thin = {"suppress_reader_facing_card": True}
        rich = {"suppress_reader_facing_card": False}
        revised, count = repair._strip_suppressed_cards(text, {"Thin item": thin, "Rich item": rich})
        self.assertEqual(count, 1)
        self.assertNotIn("Thin item", revised)
        self.assertIn("Rich item", revised)
        self.assertEqual(revised.count("\\begin{technicalnote}"), 1)

    def test_suppression_cannot_mix_with_technical_points(self) -> None:
        info = {"urls": ["https://example.com/item"]}
        with self.assertRaisesRegex(ValueError, "must not also provide"):
            repair._validate_override_with_suppression(
                "Thin item",
                {
                    "source_urls": ["https://example.com/item"],
                    "suppress_reader_facing_card": True,
                    "suppression_reason": "Accepted raw has bibliographic identity only.",
                    "technical_points": ["invented"],
                },
                info,
            )


if __name__ == "__main__":
    unittest.main()
