from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts import revise_special_half_year_review_repairs_v14 as repair


class HalfYearEventBoundedSuppressionV14Tests(unittest.TestCase):
    def test_event_bounded_merge_propagates_hash_bound_suppression_marker(self) -> None:
        info = {"canonical_title": "Thin item", "urls": ["https://example.com/thin"]}
        previous = repair.impl._ACTIVE_OVERRIDES
        repair.impl._ACTIVE_OVERRIDES = {
            "Thin item": {
                "source_urls": ["https://example.com/thin"],
                "suppress_reader_facing_card": True,
                "suppression_reason": "Accepted raw provenance has bibliographic identity only.",
                "_expected_queue_sha256": "deadbeef",
            }
        }
        try:
            with patch.object(repair.base, "_merge_event_bounded", return_value={"Thin item": info}):
                result = repair._merge_event_bounded_with_suppression(None, {})  # type: ignore[arg-type]
        finally:
            repair.impl._ACTIVE_OVERRIDES = previous
        self.assertIs(result["Thin item"]["suppress_reader_facing_card"], True)
        self.assertEqual(
            result["Thin item"]["technical_point_mode"],
            "HASH_BOUND_READER_CARD_SUPPRESSION",
        )


if __name__ == "__main__":
    unittest.main()
