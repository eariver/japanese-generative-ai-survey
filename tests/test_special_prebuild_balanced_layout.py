import tempfile
import unittest
from pathlib import Path

from scripts.postprocess_special_prebuild_balanced_layout import build_main_tex
from scripts.special_publication_layout_check import inspect_derived_layout_files, inspect_layout


class SpecialPrebuildBalancedLayoutTests(unittest.TestCase):
    def test_generated_layout_satisfies_publication_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sections").mkdir()
            (root / "technical-notes").mkdir()
            article = root / "sections" / "10-example.tex"
            article.write_text(
                "% generated\n"
                "\\section{Example}\n"
                "\\label{pkg:example}\n"
                "\\noindent\\textbf{Full-width standfirst.}\\autocite{src-one}\n\n"
                "Narrative paragraph.\\autocite{src-one}\n",
                encoding="utf-8",
            )
            notes = root / "technical-notes" / "10-example-notes.tex"
            notes.write_text("Technical notes.\n", encoding="utf-8")
            main = root / "main.tex"
            main.write_text(
                "\\documentclass{article}\n"
                "\\usepackage{jgaisurvey}\n"
                "\\begin{document}\n"
                "\\surveycover\n"
                "\\input{sections/00-frontmatter}\n"
                "\\input{sections/10-example}\n"
                "\\input{technical-notes/10-example-notes}\n"
                "\\end{document}\n",
                encoding="utf-8",
            )
            manifest = {
                "layout": {},
                "frontmatter": {"path": "sections/00-frontmatter.tex"},
                "articles": [{
                    "package_id": "example",
                    "article_section_path": "sections/10-example.tex",
                    "article_section_sha256": __import__("hashlib").sha256(article.read_bytes()).hexdigest(),
                    "technical_notes_path": "technical-notes/10-example-notes.tex",
                    "technical_notes_sha256": __import__("hashlib").sha256(notes.read_bytes()).hexdigest(),
                }],
            }

            revised, records = build_main_tex(main, manifest)
            record = records["example"]
            manifest["layout"] = {
                "body_mode": "local two-column multicol narrative; full-width chapter headings, standfirsts, Technical Notes"
            }
            manifest["articles"][0].update({
                "layout_standfirst_present": True,
                "layout_standfirst_path": record["standfirst_path"],
                "layout_standfirst_sha256": record["standfirst_sha256"],
                "layout_body_path": record["body_path"],
                "layout_body_sha256": record["body_sha256"],
            })

            self.assertEqual(inspect_layout(manifest, revised, {"status": "APPROVED"}), [])
            self.assertEqual(inspect_derived_layout_files(manifest, root), [])
            self.assertEqual(revised.count(r"\begin{multicols}{2}"), 1)
            self.assertNotIn(r"\twocolumn", revised)
            self.assertNotIn(r"\onecolumn", revised)
            self.assertLess(revised.index(r"\input{layout-standfirsts/example}"), revised.index(r"\begin{multicols}{2}"))
            self.assertGreater(revised.index(r"\input{technical-notes/10-example-notes}"), revised.index(r"\end{multicols}"))
            self.assertTrue((root / record["standfirst_path"]).read_text(encoding="utf-8").lstrip().startswith(r"\noindent\textbf{"))
            self.assertNotIn(r"\section{Example}", (root / record["body_path"]).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
