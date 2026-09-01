from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v24 as repair


class HalfYearEntityBindingV24Tests(unittest.TestCase):
    def setUp(self) -> None:
        repair._AUDIT_ROWS = []

    def test_jamba_rejects_llama_comparison_parameter_scales(self):
        summary = (
            "Jamba 1.5 Mini and Jamba 1.5 Large use an SSM-Transformer architecture with Mamba "
            "and provide a 256K context window. "
            + ("Jamba deployment details remain the subject of this paragraph. " * 3)
            + "For quality comparison, Llama 3.1 70B and Llama 3.1 405B are listed as competitors."
        )
        signals = repair._entity_aware_technical_signals(summary, [], "Jamba 1.5 Mini and Large")
        self.assertIn("SSM-Transformer", signals)
        self.assertIn("Mamba", signals)
        self.assertIn("256K context", signals)
        self.assertNotIn("70B parameter scale", signals)
        self.assertNotIn("405B parameter scale", signals)
        rejected = repair._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("70B parameter scale", rejected)
        self.assertIn("405B parameter scale", rejected)

    def test_ministral_keeps_own_sizes_and_rejects_gemma_comparison_sizes(self):
        summary = (
            "Ministral 3B and Ministral 8B are the two release variants. "
            + ("The release page then discusses deployment and evaluation methodology. " * 3)
            + "A comparison table also lists Gemma 10B and Gemma 2B."
        )
        signals = repair._entity_aware_technical_signals(summary, [], "Ministral 3B/8B")
        self.assertIn("3B parameter scale", signals)
        self.assertIn("8B parameter scale", signals)
        self.assertNotIn("10B parameter scale", signals)
        self.assertNotIn("2B parameter scale", signals)
        rejected = repair._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("10B parameter scale", rejected)
        self.assertIn("2B parameter scale", rejected)

    def test_mistral_large_rejects_codestral_llama_and_jamba_features(self):
        summary = (
            "Mistral Large 2 is the selected artifact and is described here. "
            + ("The announcement continues with product positioning and availability. " * 3)
            + "Elsewhere on the page, Codestral 22B is referenced, Llama 3.1 405B is compared, "
            "and Jamba is described as using Mamba."
        )
        signals = repair._entity_aware_technical_signals(summary, [], "Mistral Large 2")
        self.assertNotIn("22B parameter scale", signals)
        self.assertNotIn("405B parameter scale", signals)
        self.assertNotIn("Mamba", signals)
        rejected = repair._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("22B parameter scale", rejected)
        self.assertIn("405B parameter scale", rejected)
        self.assertIn("Mamba", rejected)

    def test_high_risk_signal_without_artifact_anchor_fails_closed(self):
        signals = repair._entity_aware_technical_signals(
            "A comparison row says Llama 405B and uses a Mamba architecture.",
            [],
            "Unrelated Selected Model",
        )
        self.assertNotIn("405B parameter scale", signals)
        self.assertNotIn("Mamba", signals)

    def test_audit_coverage_uses_unique_rendered_titles_not_card_placements(self):
        manifest = {
            "reader_facing_technical_notes": {
                "source_specific_detail_visible_card_count": 49,
                "source_specific_detail_override_count": 23,
            },
            "_technical_note_enrichment_scope": {
                "rendered_title_count": 34,
            },
        }
        population, visible_cards, overrides, basis = repair._audit_coverage_population(manifest)
        self.assertEqual(population, 34)
        self.assertEqual(visible_cards, 49)
        self.assertEqual(overrides, 23)
        self.assertEqual(basis, "UNIQUE_RENDERED_TITLE_COUNT")
        self.assertEqual(population - overrides, 11)

    def test_audit_coverage_fails_when_overrides_exceed_unique_titles(self):
        manifest = {
            "reader_facing_technical_notes": {
                "source_specific_detail_visible_card_count": 49,
                "source_specific_detail_override_count": 35,
            },
            "_technical_note_enrichment_scope": {
                "rendered_title_count": 34,
            },
        }
        with self.assertRaisesRegex(ValueError, "override count exceeds"):
            repair._audit_coverage_population(manifest)

    def test_audit_coverage_retains_legacy_visible_card_fallback(self):
        manifest = {
            "reader_facing_technical_notes": {
                "source_specific_detail_visible_card_count": 5,
                "source_specific_detail_override_count": 2,
            },
        }
        population, visible_cards, overrides, basis = repair._audit_coverage_population(manifest)
        self.assertEqual((population, visible_cards, overrides), (5, 5, 2))
        self.assertEqual(basis, "VISIBLE_CARD_COUNT_LEGACY_FALLBACK")


if __name__ == "__main__":
    unittest.main()
