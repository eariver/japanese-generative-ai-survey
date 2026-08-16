from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_reference_multicol as repair


class HalfYearReferenceMulticolTests(unittest.TestCase):
    def test_rewrite_keeps_full_width_heading_and_two_column_entries(self) -> None:
        source = (
            "prefix\n"
            "% half-year final bibliography compaction\n"
            "\\begingroup\n"
            "\\scriptsize\n"
            "\\setlength{\\bibitemsep}{0pt}\n"
            "\\printbibliography[title={References / Source Notes}]\n"
            "\\endgroup\n"
            "suffix\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            self.assertTrue(repair._rewrite_reference_layout(path))
            revised = path.read_text(encoding="utf-8")
        self.assertIn(r"\section*{References / Source Notes}", revised)
        self.assertIn(r"\addcontentsline{toc}{section}{References / Source Notes}", revised)
        self.assertIn(r"\begin{multicols}{2}", revised)
        self.assertIn(r"\printbibliography[heading=none]", revised)
        self.assertIn(r"\end{multicols}", revised)
        self.assertNotIn(r"\printbibliography[title={References / Source Notes}]", revised)
        self.assertEqual(revised.count(r"\printbibliography"), 1)

    def test_rewrite_is_idempotent(self) -> None:
        source = (
            "% half-year final bibliography compaction\n"
            "\\begingroup\n"
            "\\scriptsize\n"
            "\\setlength{\\bibitemsep}{0pt}\n"
            "\\printbibliography[title={References / Source Notes}]\n"
            "\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            self.assertTrue(repair._rewrite_reference_layout(path))
            once = path.read_text(encoding="utf-8")
            self.assertFalse(repair._rewrite_reference_layout(path))
            self.assertEqual(path.read_text(encoding="utf-8"), once)


if __name__ == "__main__":
    unittest.main()
