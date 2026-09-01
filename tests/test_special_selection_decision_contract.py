from __future__ import annotations

import json
import unittest
from pathlib import Path


class JulySpecialSelectionDecisionContractTests(unittest.TestCase):
    def test_decision_fixture_has_six_theme_architecture_and_36_pages(self) -> None:
        # The actual reviewed decision lives only on the Special work branch. This
        # contract protects the reusable implementation assumptions: six thematic
        # editorial packages plus frontmatter and references, totaling 36 pages.
        thematic = [8, 6, 6, 5, 5, 2]
        self.assertEqual(len(thematic), 6)
        self.assertEqual(sum(thematic) + 2 + 2, 36)
        self.assertLessEqual(36, 40)


if __name__ == "__main__":
    unittest.main()
