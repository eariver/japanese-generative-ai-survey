from __future__ import annotations

import unittest

from scripts.special_publication_layout_check import declared_non_narrative_multicols


class PublicationLayoutReferenceRaggedRightTests(unittest.TestCase):
    def test_declared_raggedright_reference_multicol_counts_as_one_reader_block(self) -> None:
        manifest = {
            "layout_revision": {
                "half_year_reference_multicol_compaction": True,
                "half_year_reference_raggedright_compaction": True,
                "references_columns": 2,
                "references_raggedright": True,
            }
        }
        main = (
            "\\section*{References / Source Notes}\n"
            "\\addcontentsline{toc}{section}{References / Source Notes}\n"
            "\\begin{multicols}{2}\n"
            "% half-year References ragged-right compaction\n"
            "\\raggedright\n"
            "\\printbibliography[heading=none]\n"
            "\\end{multicols}\n"
        )
        count, errors = declared_non_narrative_multicols(manifest, main)
        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_raggedright_source_requires_explicit_manifest_declaration(self) -> None:
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
            "% half-year References ragged-right compaction\n"
            "\\raggedright\n"
            "\\printbibliography[heading=none]\n"
            "\\end{multicols}\n"
        )
        count, errors = declared_non_narrative_multicols(manifest, main)
        self.assertEqual(count, 0)
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
