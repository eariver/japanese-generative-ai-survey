from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.revise_special_visual_review_repairs import (
    enrich_bibliography_titles,
    fix_frontmatter_toc,
    split_article,
)


class SpecialVisualReviewRepairTests(unittest.TestCase):
    def test_toc_is_section_level(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "front.tex"
            path.write_text(
                "\\setcounter{tocdepth}{0}\n\\tableofcontents\n",
                encoding="utf-8",
            )
            self.assertTrue(fix_frontmatter_toc(path, 7))
            text = path.read_text(encoding="utf-8")
            self.assertIn("\\setcounter{tocdepth}{1}", text)
            self.assertNotIn("\\setcounter{tocdepth}{0}", text)

    def test_reference_title_enrichment_uses_canonical_title(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "references.bib"
            path.write_text(
                "@online{src-x,\n"
                "  title = {Primary source 1: https://example.com/x},\n"
                "  organization = {Example},\n"
                "  url = {https://example.com/x},\n"
                "  urldate = {2026-08-12},\n"
                "  note = {Primary source used for chronology and technical verification}\n"
                "}\n",
                encoding="utf-8",
            )
            changed, count = enrich_bibliography_titles(
                path, {"https://example.com/x": "A Paper & Release"}
            )
            self.assertEqual(changed, 1)
            self.assertEqual(count, 1)
            text = path.read_text(encoding="utf-8")
            self.assertIn("title = {A Paper \\& Release}", text)
            self.assertIn("organization = {Example}", text)
            self.assertIn("urldate = {2026-08-12}", text)
            self.assertNotIn("Primary source 1:", text)

    def test_article_split_keeps_heading_full_width_and_synthesis_wide(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "article.tex"
            body = root / "body.tex"
            wide = root / "wide.tex"
            source.write_text(
                "\\section{Heading}\n"
                "\\label{pkg:x}\n"
                "\\noindent\\textbf{Lead}\n"
                "\\subsection{Narrative}\n"
                "Body.\n"
                "\\subsection{Theme Synthesis — Wide}\n"
                "Synthesis.\n"
                "\\begin{claimboundary}\n"
                "Boundary.\n"
                "\\end{claimboundary}\n",
                encoding="utf-8",
            )
            info = split_article(source, body, wide)
            self.assertEqual(info["section_line"], "\\section{Heading}")
            self.assertEqual(info["label_line"], "\\label{pkg:x}")
            self.assertIn("\\subsection{Narrative}", body.read_text(encoding="utf-8"))
            self.assertNotIn("Theme Synthesis", body.read_text(encoding="utf-8"))
            self.assertIn("Theme Synthesis", wide.read_text(encoding="utf-8"))
            self.assertIn("claimboundary", wide.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
