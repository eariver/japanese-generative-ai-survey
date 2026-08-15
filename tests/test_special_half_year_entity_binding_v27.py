from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v24 as audit_base
from scripts import revise_special_half_year_review_repairs_v27 as repair


class HalfYearEntityBindingV27Tests(unittest.TestCase):
    def setUp(self) -> None:
        audit_base._AUDIT_ROWS = []

    def _signals(self, summary: str, title: str) -> list[str]:
        old_static = set(audit_base._ENTITY_BOUND_STATIC_SIGNALS)
        audit_base._ENTITY_BOUND_STATIC_SIGNALS = old_static | repair._SCOPE_SENSITIVE_STATIC_SIGNALS
        audit_base._AUDIT_ROWS = []
        try:
            return repair._entity_aware_technical_signals(summary, [], title)
        finally:
            audit_base._ENTITY_BOUND_STATIC_SIGNALS = old_static

    def test_qwen25_exception_qualified_family_license_is_not_flattened(self) -> None:
        summary = (
            "Qwen2.5 models are available in 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B sizes. "
            "All our open-source models, except for the 3B and 72B variants, are licensed under Apache 2.0."
        )
        signals = self._signals(summary, "Qwen2.5")
        self.assertNotIn("Apache 2.0", signals)
        self.assertIn("Apache 2.0", audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"])

    def test_qwen25_coder_heterogeneous_table_license_is_not_flattened(self) -> None:
        summary = (
            "Qwen2.5-Coder 0.5B Apache 2.0\n"
            "Qwen2.5-Coder 1.5B Apache 2.0\n"
            "Qwen2.5-Coder 3B Qwen Research\n"
            "Qwen2.5-Coder 7B Apache 2.0\n"
            "Qwen2.5-Coder 14B Apache 2.0\n"
            "Qwen2.5-Coder 32B Apache 2.0"
        )
        signals = self._signals(summary, "Qwen2.5-Coder family")
        self.assertNotIn("Apache 2.0", signals)
        self.assertIn("Apache 2.0", audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"])

    def test_llama32_does_not_absorb_llama_stack_rag(self) -> None:
        summary = (
            "Llama 3.2 includes 11B and 90B vision models with 128K context. "
            "Llama Stack Distributions enable turnkey deployment of Retrieval-Augmented Generation (RAG) applications."
        )
        signals = self._signals(summary, "Llama 3.2")
        self.assertNotIn("Retrieval-Augmented Generation (RAG)", signals)
        self.assertIn(
            "Retrieval-Augmented Generation (RAG)",
            audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"],
        )

    def test_ambiguous_component_property_stays_fail_closed_for_explicit_override(self) -> None:
        summary = "Llama Stack Distributions provide Retrieval-Augmented Generation (RAG) deployment APIs."
        signals = self._signals(summary, "Llama Stack")
        self.assertNotIn("Retrieval-Augmented Generation (RAG)", signals)
        self.assertIn(
            "Retrieval-Augmented Generation (RAG)",
            audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"],
        )

    def test_unqualified_single_model_license_remains_eligible(self) -> None:
        summary = "Mistral Large 2 is released under the Mistral Research License with a 128K context window."
        signals = self._signals(summary, "Mistral Large 2")
        self.assertIn("Mistral Research License", signals)


if __name__ == "__main__":
    unittest.main()
