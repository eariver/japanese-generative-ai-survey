from __future__ import annotations

import unittest

from scripts.revise_special_visual_review_typography_recovery import (
    add_lead_input,
    extract_lead_and_relax_headings,
)


class SpecialVisualReviewTypographyRecoveryTests(unittest.TestCase):
    def test_standfirst_moves_out_and_subsection_becomes_ragged_right(self):
        text = (
            "% generated\n"
            "\\noindent\\textbf{Semantic privilege、cross-application benchmark。}\\autocite{src-x}\n\n"
            "\\subsection{Scepsy — aggregate LLM pipelineをschedulerの単位にする}\n\n"
            "Body paragraph.\\autocite{src-x}\n"
        )
        lead, body, count = extract_lead_and_relax_headings(text)
        self.assertEqual(
            lead,
            "\\noindent\\textbf{Semantic privilege、cross-application benchmark。}\\autocite{src-x}\n",
        )
        self.assertNotIn("Semantic privilege", body)
        self.assertIn("\\begingroup\\raggedright", body)
        self.assertIn("\\subsection{Scepsy", body)
        self.assertIn("\\par\\endgroup", body)
        self.assertEqual(count, 1)

    def test_main_inserts_lead_before_local_multicols(self):
        main = (
            "\\vspace{0.15em}\n"
            "\\begin{multicols}{2}\n"
            "\\input{layout-bodies/04-inference-serving-april-narrative}\n"
            "\\end{multicols}\n"
        )
        revised = add_lead_input(
            main,
            "layout-bodies/04-inference-serving-april-narrative.tex",
            "layout-leads/04-inference-serving-april-lead.tex",
        )
        self.assertIn("\\input{layout-leads/04-inference-serving-april-lead}", revised)
        self.assertLess(revised.index("layout-leads/"), revised.index("\\begin{multicols}{2}"))
        self.assertIn("\\input{layout-bodies/04-inference-serving-april-narrative}", revised)


if __name__ == "__main__":
    unittest.main()
