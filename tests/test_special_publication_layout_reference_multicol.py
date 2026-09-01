from __future__ import annotations

import unittest

from scripts.special_publication_layout_check import declared_non_narrative_multicols


class PublicationLayoutReferenceMulticolTests(unittest.TestCase):
    def test_declared_reference_multicol_counts_as_one_non_narrative_block(self) -> None:
        manifest = {
            "layout_revision": {
                "half_year_reference_multicol_compaction": True,
                "references_columns": 2,
            }
        }
        main = (
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begin{multicols}{2}\n"
            "\\printbibliography[heading=none]\n"
            "\\end{multicols}\n"
        )
        count, errors = declared_non_narrative_multicols(manifest, main)
        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_undeclared_or_malformed_reference_multicol_is_not_allowed(self) -> None:
        manifest = {
            "layout_revision": {
                "half_year_reference_multicol_compaction": True,
                "references_columns": 2,
            }
        }
        count, errors = declared_non_narrative_multicols(manifest, "\\begin{multicols}{2}\n")
        self.assertEqual(count, 0)
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
