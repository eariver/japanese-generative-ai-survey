import json
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_weekly_layout_v2 as layout


OLD_TEX = r"""\documentclass{jlreq}
\addbibresource{references.bib}
\begin{document}
\twocolumn
\section{OSS Watch}
body
\clearpage
\onecolumn
\section{今週の総括}
\label{sec:issue-summary}
\sectionkicker{WEEKLY SYNTHESIS}
summary
\clearpage
\onecolumn
\printbibliography[title={References / Source Notes}]
\end{document}
"""


class WeeklyLayoutTransformTests(unittest.TestCase):
    def _fixture(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        main = root / "surveys/weekly/2026-W33/main.tex"
        manifest = root / "sources/2026-W33/publication/v2/validated-source-manifest.json"
        main.parent.mkdir(parents=True)
        manifest.parent.mkdir(parents=True)
        main.write_text(OLD_TEX, encoding="utf-8")
        payload = {
            "schema_version": "2.0-rc1",
            "issue_id": "2026-W33",
            "rendered_source": {
                "path": "surveys/weekly/2026-W33/main.tex",
                "sha256": core.sha256_file(main),
            },
        }
        core.write_json(manifest, payload)
        return td, root, main, manifest

    def test_compacts_summary_and_source_notes_and_rebinds_manifest(self):
        td, root, main, manifest = self._fixture()
        self.addCleanup(td.cleanup)

        before = core.sha256_file(main)
        result = layout.compact_closing_summary(root, main, manifest)
        text = main.read_text(encoding="utf-8")
        updated = json.loads(manifest.read_text(encoding="utf-8"))

        self.assertEqual(result["status"], "PASS")
        self.assertNotEqual(core.sha256_file(main), before)
        self.assertIn(
            "\\newpage\n\\section{今週の総括}\n\\label{sec:issue-summary}",
            text,
        )
        self.assertNotIn(
            "\\clearpage\n\\onecolumn\n\\section{今週の総括}",
            text,
        )
        self.assertIn("\\AtEveryBibitem", text)
        self.assertLess(text.index("\\AtEveryBibitem"), text.index("\\begin{document}"))
        self.assertIn("\\clearfield{urlyear}", text)
        self.assertIn(
            f"\\footnotesize\n\\linespread{{{layout.REFERENCE_LINE_SPREAD}}}\\selectfont\n"
            "\\setlength{\\bibitemsep}{0pt}",
            text,
        )
        self.assertIn("prenote=corev2legend", text)
        self.assertIn("References / Source Notes", text)
        self.assertIn("TIGHT_REFERENCE_LEADING_094", result["transformations"])
        self.assertEqual(updated["rendered_source"]["sha256"], core.sha256_file(main))
        result_path = root / result["result_path"]
        self.assertTrue(result_path.is_file())
        self.assertEqual(core.sha256_file(result_path), result["result_sha256"])

    def test_biblatex_entry_hook_is_defined_by_preamble_transform(self):
        self.assertIn("\\AtEveryBibitem", layout.BIBRESOURCE_REPLACEMENT)
        self.assertNotIn("\\AtEveryBibitem", layout.REFERENCE_REPLACEMENT)
        self.assertTrue(layout.BIBRESOURCE_REPLACEMENT.startswith("\\addbibresource{references.bib}\n"))

    def test_reference_density_preserves_font_size_and_uses_modest_leading(self):
        self.assertEqual(layout.REFERENCE_LINE_SPREAD, "0.94")
        self.assertIn("\\footnotesize", layout.REFERENCE_REPLACEMENT)
        self.assertIn("\\linespread{0.94}\\selectfont", layout.REFERENCE_REPLACEMENT)
        self.assertNotIn("\\scriptsize", layout.REFERENCE_REPLACEMENT)
        self.assertNotIn("\\tiny", layout.REFERENCE_REPLACEMENT)

    def test_rejects_manifest_source_sha_drift(self):
        td, root, main, manifest = self._fixture()
        self.addCleanup(td.cleanup)
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        payload["rendered_source"]["sha256"] = "0" * 64
        core.write_json(manifest, payload)

        with self.assertRaisesRegex(ValueError, "SHA drift"):
            layout.compact_closing_summary(root, main, manifest)

    def test_rejects_missing_canonical_summary_boundary(self):
        td, root, main, manifest = self._fixture()
        self.addCleanup(td.cleanup)
        main.write_text(OLD_TEX.replace("\\label{sec:issue-summary}", "\\label{other}"), encoding="utf-8")
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        payload["rendered_source"]["sha256"] = core.sha256_file(main)
        core.write_json(manifest, payload)

        with self.assertRaisesRegex(ValueError, "exactly one canonical summary boundary"):
            layout.compact_closing_summary(root, main, manifest)


if __name__ == "__main__":
    unittest.main()
