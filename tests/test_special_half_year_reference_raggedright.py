from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_reference_raggedright as repair


class HalfYearReferenceRaggedRightTests(unittest.TestCase):
    def test_adds_local_raggedright_before_bibliography(self) -> None:
        source = (
            "% half-year References two-column compaction\n"
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begingroup\n"
            "\\scriptsize\n"
            "\\setlength{\\bibitemsep}{0pt}\n"
            "\\begin{multicols}{2}\n"
            "\\printbibliography[heading=none]\n"
            "\\end{multicols}\n"
            "\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            self.assertTrue(repair._add_raggedright(path))
            revised = path.read_text(encoding="utf-8")
        self.assertIn("% half-year References ragged-right compaction\n\\raggedright\n\\printbibliography[heading=none]", revised)
        self.assertEqual(revised.count(r"\raggedright"), 1)
        self.assertEqual(revised.count(r"\printbibliography"), 1)

    def test_rewrite_is_idempotent(self) -> None:
        source = (
            "% half-year References two-column compaction\n"
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begingroup\n"
            "\\scriptsize\n"
            "\\setlength{\\bibitemsep}{0pt}\n"
            "\\begin{multicols}{2}\n"
            "% half-year References ragged-right compaction\n"
            "\\raggedright\n"
            "\\printbibliography[heading=none]\n"
            "\\end{multicols}\n"
            "\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            self.assertFalse(repair._add_raggedright(path))
            self.assertEqual(path.read_text(encoding="utf-8"), source)


if __name__ == "__main__":
    unittest.main()
