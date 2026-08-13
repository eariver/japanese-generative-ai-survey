import tempfile
import unittest
from pathlib import Path

from scripts.run_revise_special_mixed_layout import inject_synthesis_into_current_layout


class SpecialPrebuildThemeSynthesisTests(unittest.TestCase):
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
