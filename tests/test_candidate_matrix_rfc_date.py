from __future__ import annotations

import unittest
from datetime import timezone

from scripts import build_candidate_matrix


class CandidateMatrixRfcDateTests(unittest.TestCase):
    def test_rfc_2822_event_timestamp_is_supported(self) -> None:
        value = build_candidate_matrix.parse_instant("Wed, 29 Jul 2026 15:00:00 GMT")
        self.assertIsNotNone(value)
        self.assertEqual(value.tzinfo, timezone.utc)
        self.assertEqual(value.isoformat(), "2026-07-29T15:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
