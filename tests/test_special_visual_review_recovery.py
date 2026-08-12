from __future__ import annotations

import unittest

from scripts.revise_special_visual_review_recovery import EMPTY_ITEMIZE_RE


class SpecialVisualReviewRecoveryTests(unittest.TestCase):
    def test_empty_itemize_after_selective_tail_grouping_is_removed(self):
        text = (
            "{\\bfseries 一次資料から整理したtechnical points}\n"
            "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n"
            "\\end{itemize}\n"
            "\\begin{minipage}{\\linewidth}\n"
            "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n"
            "\\item \\textbf{Vendor claim}: claim\n"
            "\\end{itemize}\n"
            "\\end{minipage}\n"
        )
        revised, count = EMPTY_ITEMIZE_RE.subn("", text)
        self.assertEqual(count, 1)
        self.assertNotIn("\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n\\end{itemize}", revised)
        self.assertIn("\\item \\textbf{Vendor claim}: claim", revised)

    def test_nonempty_itemize_is_preserved(self):
        text = "\\begin{itemize}\n\\item fact\n\\end{itemize}\n"
        revised, count = EMPTY_ITEMIZE_RE.subn("", text)
        self.assertEqual(count, 0)
        self.assertEqual(revised, text)


if __name__ == "__main__":
    unittest.main()
