from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_reference_common_urldate as repair


class HalfYearReferenceCommonUrldateTests(unittest.TestCase):
    def test_common_urldate_requires_every_entry_and_one_value(self) -> None:
        bib = (
            "@online{a,\n  title = {A},\n  urldate = {2026-08-15},\n}\n\n"
            "@online{b,\n  title = {B},\n  urldate = {2026-08-15},\n}\n"
        )
        date, count = repair.common_urldate(bib)
        self.assertEqual(date, "2026-08-15")
        self.assertEqual(count, 2)

    def test_mixed_or_missing_urldate_fails_closed(self) -> None:
        mixed = (
            "@online{a,\n  urldate = {2026-08-15},\n}\n"
            "@online{b,\n  urldate = {2026-08-16},\n}\n"
        )
        with self.assertRaisesRegex(ValueError, "not common"):
            repair.common_urldate(mixed)
        with self.assertRaisesRegex(ValueError, "has no urldate"):
            repair.common_urldate("@online{a,\n  title = {A},\n}\n")

    def test_main_rewrite_states_date_once_and_suppresses_rendered_fields(self) -> None:
        source = (
            repair.OLD_INTRO
            + "\n\\smallskip\n"
            + "% half-year References two-column compaction\n"
            + "\\section*{References / Source Notes}\n"
            + "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            + "\\begingroup\n\\scriptsize\n\\setlength{\\bibitemsep}{0pt}\n"
            + "\\begin{multicols}{2}\n"
            + "% half-year References ragged-right compaction\n\\raggedright\n"
            + repair.PRINT_BIB
            + "\n\\end{multicols}\n\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            self.assertTrue(repair.rewrite_main(path, "2026-08-15"))
            revised = path.read_text(encoding="utf-8")
        self.assertIn("全URLの参照日は2026-08-15である", revised)
        self.assertIn(repair.HOOK_MARKER, revised)
        self.assertIn(r"\clearfield{urlyear}", revised)
        self.assertEqual(revised.count(repair.PRINT_BIB), 1)
        self.assertNotIn("URL、参照日を示す", revised)


if __name__ == "__main__":
    unittest.main()
