import unittest

from scripts.revise_special_preserve_preview_repairs import adapt_current_main, verify_preserved_inputs


class PreservePreviewRepairTests(unittest.TestCase):
    def sample_main(self) -> str:
        return (
            "\\documentclass{article}\n"
            "\\usepackage{jgaisurvey}\n"
            "\\begin{document}\n"
            "\\surveycover\n"
            "\\clearpage\n"
            "\\input{sections/00-frontmatter}\n"
            "\\clearpage\n"
            "\\section{First}\n"
            "\\begin{multicols}{2}\nA\n\\end{multicols}\n"
            "\\input{theme-synthesis/01-first-synthesis}\n"
            "\\input{technical-notes/10-first-notes}\n"
            "\\clearpage\n"
            "\\section{Second}\n"
            "\\begin{multicols}{2}\nB\n\\end{multicols}\n"
            "\\input{theme-synthesis/02-second-synthesis}\n"
            "\\input{technical-notes/20-second-notes}\n"
            "\\clearpage\n"
            "\\printbibliography[title={References / Source Notes}]\n"
            "\\end{document}\n"
        )

    def test_preserves_theme_synthesis_inputs_and_makes_later_starts_adaptive(self):
        before = self.sample_main()
        after, adaptive, refs_changed = adapt_current_main(before)
        self.assertEqual(adaptive, 1)
        self.assertTrue(refs_changed)
        self.assertIn(r"\usepackage{needspace}", after)
        self.assertEqual(after.count(r"\clearpage" + "\n" + r"\section{"), 1)
        self.assertIn(r"\Needspace{0.45\textheight}" + "\n" + r"\bigskip" + "\n" + r"\section{Second}", after)
        self.assertNotIn(r"\clearpage" + "\n" + r"\printbibliography", after)
        self.assertIn(r"\Needspace{0.30\textheight}", after)
        verify_preserved_inputs(
            before,
            after,
            {
                "theme-synthesis/01-first-synthesis.tex": "sha-1",
                "theme-synthesis/02-second-synthesis.tex": "sha-2",
            },
        )

    def test_rejects_dropped_or_duplicated_synthesis_input(self):
        before = self.sample_main()
        after = before.replace(r"\input{theme-synthesis/02-second-synthesis}" + "\n", "")
        with self.assertRaises(ValueError):
            verify_preserved_inputs(
                before,
                after,
                {
                    "theme-synthesis/01-first-synthesis.tex": "sha-1",
                    "theme-synthesis/02-second-synthesis.tex": "sha-2",
                },
            )


if __name__ == "__main__":
    unittest.main()
