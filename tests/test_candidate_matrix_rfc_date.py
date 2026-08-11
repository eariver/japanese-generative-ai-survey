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

    def test_month_precision_event_remains_timing_unresolved(self) -> None:
        card = {
            "temporal": {
                "events": [
                    {"event_date": "2026-06-10"},
                    {"event_date": "2026-06-18"},
                    {"event_date": "2026-06"},
                ]
            },
            "editorial": {"why_now_confirmed": True},
        }
        relation, raw_dates = build_candidate_matrix.timing_relation(
            card,
            "2026-06-01T00:00:00Z",
            "2026-06-30T23:59:59Z",
        )
        self.assertEqual(relation, "TIMING_UNRESOLVED")
        self.assertEqual(raw_dates, ["2026-06", "2026-06-10", "2026-06-18"])


if __name__ == "__main__":
    unittest.main()
