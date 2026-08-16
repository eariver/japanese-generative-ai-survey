from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_reference_common_urldate as base
from scripts import revise_special_half_year_reference_common_urldate_v2 as repair


class HalfYearReferenceCommonUrldateV2Tests(unittest.TestCase):
    def test_moves_existing_hook_before_references_multicols(self) -> None:
        intro = (
            r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。"
            r"各entryでは識別・追跡に必要な資料名、組織、URLを示す。全URLの参照日は2026-08-15である。}}\par"
        )
        source = (
            intro + "\n"
            "% half-year References two-column compaction\n"
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begingroup\n\\scriptsize\n\\setlength{\\bibitemsep}{0pt}\n"
            "\\begin{multicols}{2}\n"
            "% half-year References ragged-right compaction\n\\raggedright\n"
            + base.HOOK_MARKER + "\n" + repair.HOOK + "\n"
            + base.PRINT_BIB + "\n\\end{multicols}\n\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            repair.normalized_rewrite_main(path, "2026-08-15")
            revised = path.read_text(encoding="utf-8")
        hook_at = revised.index(repair.HOOK)
        begin_at = revised.index(r"\begin{multicols}{2}")
        self.assertLess(hook_at, begin_at)
        exact_body = (
            r"\begin{multicols}{2}" + "\n"
            + repair.RAGGED_MARKER + "\n"
            + r"\raggedright" + "\n"
            + base.PRINT_BIB + "\n"
            + r"\end{multicols}"
        )
        self.assertIn(exact_body, revised)
        self.assertEqual(revised.count(repair.HOOK), 1)

    def test_legacy_intro_is_still_consolidated(self) -> None:
        source = (
            base.OLD_INTRO + "\n"
            "% half-year References two-column compaction\n"
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begingroup\n\\scriptsize\n\\setlength{\\bibitemsep}{0pt}\n"
            "\\begin{multicols}{2}\n"
            "% half-year References ragged-right compaction\n\\raggedright\n"
            + base.PRINT_BIB + "\n\\end{multicols}\n\\endgroup\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            repair.normalized_rewrite_main(path, "2026-08-15")
            revised = path.read_text(encoding="utf-8")
        self.assertIn("全URLの参照日は2026-08-15である", revised)
        self.assertNotIn("URL、参照日を示す", revised)


if __name__ == "__main__":
    unittest.main()
