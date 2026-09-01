from __future__ import annotations

import unittest

from scripts import postprocess_special_reader_facing_notes as compat


class SpecialReaderTaxonomyCompatTests(unittest.TestCase):
    def test_known_suffixes_become_reader_labels(self) -> None:
        self.assertEqual(compat.readable_taxonomy_label("VEO3_GA"), "Veo 3（一般提供）")
        self.assertEqual(compat.readable_taxonomy_label("COMPUTER_USE_PREVIEW"), "Computer Use（Preview）")
        self.assertEqual(compat.readable_taxonomy_label("CODING_Agent_UPGRADE"), "Coding Agent（更新）")

    def test_unknown_compound_label_has_no_machine_underscore_or_generic_fallback(self) -> None:
        value = compat.readable_taxonomy_label("INTERACTIONS_API_AND_DEEP_研究Preview")
        self.assertEqual(value, "Interactions API / Deep Research（Preview）")
        self.assertNotIn("_", value)
        self.assertNotIn("技術イベント", value)

    def test_chronology_event_field_is_translated(self) -> None:
        text = "2025-10-07 (COMPUTER_USE_PREVIEW)\\\\\n"
        rendered = compat.translate_remaining_taxonomy(text)
        self.assertIn("Computer Use（Preview）", rendered)
        self.assertNotIn("COMPUTER_USE_PREVIEW", rendered)

    def test_type_table_row_keeps_latex_row_ending(self) -> None:
        text = "種別 & Agent \\\\\n時系列 & 2025-07-17 (Agent_LAUNCH) \\\\\n"
        rendered = compat.translate_remaining_taxonomy(text)
        lines = rendered.splitlines()
        self.assertTrue(lines[0].endswith(r"\\"), rendered)
        self.assertIn("種別 & Agent", lines[0])
        self.assertIn("Agent（公開）", lines[1])


if __name__ == "__main__":
    unittest.main()
