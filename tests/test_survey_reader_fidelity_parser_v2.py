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


if __name__ == "__main__":
    unittest.main()
