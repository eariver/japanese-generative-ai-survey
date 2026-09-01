from __future__ import annotations

import unittest

from scripts import accept_evidence_results as acceptance


class EvidenceAcceptanceBoundaryTests(unittest.TestCase):
    def test_evidence_acceptance_stops_before_human_selection_gate(self) -> None:
        self.assertEqual(acceptance.ALLOWED_LIFECYCLE, "CANDIDATES_NORMALIZED")
        self.assertEqual(acceptance.TARGET_LIFECYCLE, "EVIDENCE_REVIEWED")
        self.assertNotEqual(acceptance.TARGET_LIFECYCLE, "SELECTION_COMPLETE")


if __name__ == "__main__":
    unittest.main()
