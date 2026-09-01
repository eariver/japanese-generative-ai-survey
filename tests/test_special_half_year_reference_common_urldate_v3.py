from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_reference_common_urldate as base
from scripts import revise_special_half_year_reference_common_urldate_v2 as v2
from scripts import revise_special_half_year_reference_common_urldate_v3 as repair


class HalfYearReferenceCommonUrldateV3Tests(unittest.TestCase):
    def source(self, hook_in_body: bool = True) -> str:
        intro = (
            r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。"
            r"各entryでは識別・追跡に必要な資料名、組織、URLを示す。全URLの参照日は2026-08-15である。}}\par"
        )
        hook = (base.HOOK_MARKER + "\n" + repair.HOOK + "\n") if hook_in_body else ""
        return (
            "\\documentclass{article}\n"
            "\\usepackage{biblatex}\n"
            "\\addbibresource{references.bib}\n"
            "\\begin{document}\n"
            + intro + "\n"
            + "% half-year References two-column compaction\n"
            + "\\section*{References / Source Notes}\n"
            + "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            + "\\begingroup\n\\scriptsize\n\\setlength{\\bibitemsep}{0pt}\n"
            + hook
            + "\\begin{multicols}{2}\n"
            + v2.RAGGED_MARKER + "\n\\raggedright\n"
            + base.PRINT_BIB + "\n\\end{multicols}\n\\endgroup\n"
            + "\\end{document}\n"
        )

    def test_moves_body_hook_into_preamble(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(self.source(True), encoding="utf-8")
            self.assertTrue(repair.preamble_rewrite_main(path, "2026-08-15"))
            revised = path.read_text(encoding="utf-8")
        hook_at = revised.index(repair.HOOK)
        begin_document_at = revised.index(repair.BEGIN_DOCUMENT)
        self.assertLess(hook_at, begin_document_at)
        self.assertIn(repair.PREAMBLE_ANCHOR + "\n" + base.HOOK_MARKER + "\n" + repair.HOOK, revised)
        body = revised[begin_document_at:]
        self.assertNotIn(repair.HOOK, body)
        expected_refs = (
            r"\begin{multicols}{2}" + "\n"
            + v2.RAGGED_MARKER + "\n"
            + r"\raggedright" + "\n"
            + base.PRINT_BIB + "\n"
            + r"\end{multicols}"
        )
        self.assertIn(expected_refs, revised)

    def test_fresh_consolidation_also_places_hook_in_preamble(self) -> None:
        source = self.source(False).replace(
            r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。各entryでは識別・追跡に必要な資料名、組織、URLを示す。全URLの参照日は2026-08-15である。}}\par",
            base.OLD_INTRO,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tex"
            path.write_text(source, encoding="utf-8")
            repair.preamble_rewrite_main(path, "2026-08-15")
            revised = path.read_text(encoding="utf-8")
        self.assertIn("全URLの参照日は2026-08-15である", revised)
        self.assertLess(revised.index(repair.HOOK), revised.index(repair.BEGIN_DOCUMENT))


if __name__ == "__main__":
    unittest.main()
