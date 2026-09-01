from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v24 as audit_base
from scripts import revise_special_half_year_review_repairs_v27 as binding
from scripts import revise_special_half_year_review_repairs_v34 as repair


class HalfYearGenericCapabilityBindingV34Tests(unittest.TestCase):
    def setUp(self) -> None:
        audit_base._AUDIT_ROWS = []

    def _signals(self, summary: str, title: str) -> list[str]:
        old_component = set(binding._COMPONENT_SCOPED_SIGNALS)
        old_scope = set(binding._SCOPE_SENSITIVE_STATIC_SIGNALS)
        old_static = set(audit_base._ENTITY_BOUND_STATIC_SIGNALS)
        binding._COMPONENT_SCOPED_SIGNALS = old_component | repair._ADDITIONAL_COMPONENT_SCOPED_SIGNALS
        binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope | repair._ADDITIONAL_COMPONENT_SCOPED_SIGNALS
        audit_base._ENTITY_BOUND_STATIC_SIGNALS = old_static | binding._SCOPE_SENSITIVE_STATIC_SIGNALS
        audit_base._AUDIT_ROWS = []
        try:
            return binding._entity_aware_technical_signals(summary, [], title)
        finally:
            binding._COMPONENT_SCOPED_SIGNALS = old_component
            binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope
            audit_base._ENTITY_BOUND_STATIC_SIGNALS = old_static

    def test_openelm_does_not_absorb_adjacent_research_navigation_capabilities(self) -> None:
        summary = (
            "OpenELM is an open language model family with a layer-wise scaling strategy. "
            "Explore image generation research. Small model deployment can be cost-efficient."
        )
        signals = self._signals(summary, "OpenELM")
        self.assertNotIn("image generation", signals)
        self.assertNotIn("small model / cost-efficient deployment", signals)
        rejected = audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("image generation", rejected)
        self.assertIn("small model / cost-efficient deployment", rejected)

    def test_command_model_does_not_absorb_adjacent_speculative_decoding_navigation(self) -> None:
        summary = (
            "Command R is a retrieval-augmented generation model for enterprise workloads. "
            "Research navigation also links to speculative decoding."
        )
        signals = self._signals(summary, "Command R")
        self.assertNotIn("speculative decoding", signals)
        self.assertIn("speculative decoding", audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"])

    def test_explicit_subject_can_own_image_generation(self) -> None:
        summary = "Example Image Model provides image generation for creators."
        signals = self._signals(summary, "Example Image Model")
        self.assertIn("image generation", signals)


if __name__ == "__main__":
    unittest.main()
