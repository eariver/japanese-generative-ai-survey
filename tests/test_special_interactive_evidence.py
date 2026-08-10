from __future__ import annotations

import re
import unittest

from scripts import run_special_interactive_evidence as runner


class SpecialInteractiveEvidenceTests(unittest.TestCase):
    def test_special_identity_boundary(self):
        self.assertIsNotNone(runner.SPECIAL_RE.fullmatch("SP-2026-M07"))
        self.assertIsNone(runner.SPECIAL_RE.fullmatch("2026-W33"))
        self.assertIsNotNone(runner.ANY_RE.fullmatch("2026-W33"))
        self.assertIsNotNone(runner.ANY_RE.fullmatch("SP-2026-M07"))


if __name__ == "__main__":
    unittest.main()
