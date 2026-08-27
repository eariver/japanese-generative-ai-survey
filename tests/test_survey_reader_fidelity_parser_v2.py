from __future__ import annotations

import unittest

from scripts import survey_reader_fidelity_v2 as fidelity


class SurveyReaderFidelityParserV2Tests(unittest.TestCase):
    def test_starred_subsections_do_not_shift_numbered_reader_locations(self) -> None:
        source = (
            "\\section{Main}\n"
            "Introductory prose.\n"
            "\\subsection*{Unnumbered note}\n"
            "Unnumbered supporting prose.\n"
            "\\subsection{Numbered result}\n"
            "Reader-facing substantive result.\n"
        )
        blocks, by_location = fidelity.parse_longform_blocks(source)
        locations = {block.canonical_location for block in blocks}
        self.assertIn("Section 1 — Main", locations)
        self.assertIn("Subsection 1.1 — Numbered result", locations)
        self.assertNotIn("Subsection 1.1 — Unnumbered note", locations)
        self.assertNotIn("Subsection 1.2 — Numbered result", locations)
        self.assertIn("Subsection 1.1 — Numbered result", by_location)

    def test_starred_headings_terminate_preceding_numbered_blocks(self) -> None:
        source = (
            "\\section{Main}\n"
            "Main prose.\n"
            "\\subsection{First}\n"
            "First prose.\n"
            "\\subsection*{Unnumbered note}\n"
            "Unnumbered subsection prose must not belong to First.\n"
            "\\subsection{Second}\n"
            "Second prose.\n"
            "\\section*{References}\n"
            "Reference prose must not belong to Main or Second.\n"
            "\\section{Next}\n"
            "Next prose.\n"
        )
        _, by_location = fidelity.parse_longform_blocks(source)
        self.assertNotIn(
            "Unnumbered subsection prose",
            by_location["Subsection 1.1 — First"].body,
        )
        self.assertNotIn(
            "Reference prose",
            by_location["Subsection 1.2 — Second"].body,
        )
        self.assertNotIn(
            "Reference prose",
            by_location["Section 1 — Main"].body,
        )
        self.assertEqual(by_location["Section 2 — Next"].body.strip(), "Next prose.")

    def test_heading_labels_alone_do_not_make_reader_block_nonempty(self) -> None:
        source = (
            "\\section{Main}\n"
            "\\subsection{Empty child}\n"
            "\\section*{References}\n"
            "Reference prose.\n"
        )
        _, by_location = fidelity.parse_longform_blocks(source)
        self.assertEqual(by_location["Section 1 — Main"].visible_chars, 0)
        self.assertEqual(by_location["Subsection 1.1 — Empty child"].visible_chars, 0)


if __name__ == "__main__":
    unittest.main()
