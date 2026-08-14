from __future__ import annotations

import unittest

from scripts import postprocess_special_reader_facing_notes as compat


class SpecialReaderTaxonomyCompatTests(unittest.TestCase):
    def test_known_suffixes_become_reader_labels(self) -> None:
        self.assertEqual(compat.readable_taxonomy_label("VEO3_GA"), "VEO3（一般提供）")
        self.assertEqual(compat.readable_taxonomy_label("COMPUTER_USE_PREVIEW"), "COMPUTER USE（Preview）")
        self.assertEqual(compat.readable_taxonomy_label("CODING_Agent_UPGRADE"), "CODING Agent（更新）")

    def test_unknown_compound_label_has_no_machine_underscore(self) -> None:
        value = compat.readable_taxonomy_label("INTERACTIONS_API_AND_DEEP_研究Preview")
        self.assertNotIn("_", value)
        self.assertIn("技術イベント", value)

    def test_chronology_event_field_is_translated(self) -> None:
        text = "2025-10-07 (COMPUTER_USE_PREVIEW)\\\\\n"
        rendered = compat.translate_remaining_taxonomy(text)
        self.assertIn("COMPUTER USE（Preview）", rendered)
        self.assertNotIn("COMPUTER_USE_PREVIEW", rendered)


if __name__ == "__main__":
    unittest.main()
