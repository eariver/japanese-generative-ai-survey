import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_mixed_layout as revision
from scripts.run_revise_special_mixed_layout import (
    inject_synthesis_into_current_layout,
    reader_month_label,
)


class SpecialPrebuildThemeSynthesisTests(unittest.TestCase):
    def test_lead_and_comparison_are_article_synthesis_types(self):
        self.assertIn("LEAD", revision.ARTICLE_TYPES)
        self.assertIn("COMPARISON", revision.ARTICLE_TYPES)

    def test_reader_month_label_comes_from_issue_id(self):
        self.assertEqual(
            reader_month_label({"issue_id": "SP-2026-M01"}),
            "1月の一次資料・論文から読めること",
        )
        self.assertEqual(
            reader_month_label({"issue_id": "SP-2026-M07"}),
            "7月の一次資料・論文から読めること",
        )
        self.assertEqual(
            reader_month_label({"issue_id": "unexpected"}),
            "一次資料・論文から読めること",
        )

    def test_inserts_full_width_synthesis_without_changing_local_multicols(self):
        with tempfile.TemporaryDirectory() as tmp:
            main = Path(tmp) / "main.tex"
            main.write_text(
                "\\section{Example}\n"
                "\\input{layout-standfirsts/example}\n"
                "\\begin{multicols}{2}\n"
                "\\input{layout-bodies/example}\n"
                "\\end{multicols}\n"
                "\\input{technical-notes/example-notes}\n",
                encoding="utf-8",
            )
            manifest = {
                "articles": [{
                    "package_id": "example",
                    "technical_notes_path": "technical-notes/example-notes.tex",
                }]
            }
            revised = inject_synthesis_into_current_layout(
                main,
                manifest,
                {"example": "theme-synthesis/example.tex"},
            )
            self.assertEqual(revised.count(r"\begin{multicols}{2}"), 1)
            self.assertEqual(revised.count(r"\end{multicols}"), 1)
            self.assertNotIn(r"\twocolumn", revised)
            self.assertNotIn(r"\onecolumn", revised)
            self.assertLess(revised.index(r"\end{multicols}"), revised.index(r"\input{theme-synthesis/example}"))
            self.assertLess(revised.index(r"\input{theme-synthesis/example}"), revised.index(r"\input{technical-notes/example-notes}"))

    def test_refreshes_existing_synthesis_without_duplicate_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            main = Path(tmp) / "main.tex"
            main.write_text(
                "\\section{Example}\n"
                "\\begin{multicols}{2}\n"
                "\\input{layout-bodies/example}\n"
                "\\end{multicols}\n"
                "\\input{theme-synthesis/example}\n"
                "\\medskip\n"
                "\\input{technical-notes/example-notes}\n",
                encoding="utf-8",
            )
            manifest = {
                "articles": [{
                    "package_id": "example",
                    "technical_notes_path": "technical-notes/example-notes.tex",
                }],
                "theme_synthesis": [{
                    "package_id": "example",
                    "path": "theme-synthesis/example.tex",
                }],
            }
            revised = inject_synthesis_into_current_layout(
                main,
                manifest,
                {"example": "theme-synthesis/example.tex"},
            )
            self.assertEqual(revised.count(r"\input{theme-synthesis/example}"), 1)
            self.assertEqual(revised.count(r"\input{technical-notes/example-notes}"), 1)

    def test_replaces_existing_synthesis_when_relative_path_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            main = Path(tmp) / "main.tex"
            main.write_text(
                "\\input{theme-synthesis/old-example}\n"
                "\\medskip\n"
                "\\input{technical-notes/example-notes}\n",
                encoding="utf-8",
            )
            manifest = {
                "articles": [{
                    "package_id": "example",
                    "technical_notes_path": "technical-notes/example-notes.tex",
                }],
                "theme_synthesis": [{
                    "package_id": "example",
                    "path": "theme-synthesis/old-example.tex",
                }],
            }
            revised = inject_synthesis_into_current_layout(
                main,
                manifest,
                {"example": "theme-synthesis/new-example.tex"},
            )
            self.assertNotIn(r"\input{theme-synthesis/old-example}", revised)
            self.assertEqual(revised.count(r"\input{theme-synthesis/new-example}"), 1)

    def test_rejects_ambiguous_notes_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            main = Path(tmp) / "main.tex"
            main.write_text(
                "\\input{technical-notes/example-notes}\n"
                "\\input{technical-notes/example-notes}\n",
                encoding="utf-8",
            )
            manifest = {"articles": [{"package_id": "example", "technical_notes_path": "technical-notes/example-notes.tex"}]}
            with self.assertRaises(ValueError):
                inject_synthesis_into_current_layout(main, manifest, {"example": "theme-synthesis/example.tex"})


if __name__ == "__main__":
    unittest.main()
