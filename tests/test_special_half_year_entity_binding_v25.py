from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v24 as audit_base
from scripts import revise_special_half_year_review_repairs_v26 as repair


class HalfYearEntityBindingV25Tests(unittest.TestCase):
    def setUp(self) -> None:
        audit_base._AUDIT_ROWS = []

    def _signals(self, summary: str, title: str) -> list[str]:
        audit_base._AUDIT_ROWS = []
        return repair._entity_aware_technical_signals(summary, [], title)

    def test_jamba_real_release_text_rejects_llama_scales_and_single_gpu_context(self):
        summary = (
            "Today, we are debuting the Jamba 1.5 family of open models: Jamba 1.5 Mini and Jamba 1.5 Large. "
            "Built on our novel SSM-Transformer architecture, these models provide a 256K effective context window. "
            "Jamba 1.5 Large, with a score of 65.4, outpaces both Llama 3.1 70B and 405B. "
            "Jamba 1.5 Large and Mini are built on the novel SSM-Transformer Jamba architecture, which weaves together "
            "Transformer quality with Mamba efficiency. The models can handle context lengths up to 140K tokens on a single GPU "
            "using Jamba 1.5 Mini."
        )
        signals = self._signals(summary, "Jamba 1.5 Mini and Large")
        # Pronoun-carried correct specifications may be conservatively dropped and restored from
        # the hash-bound accepted-Screening override; comparator/deployment values must never pass.
        self.assertNotIn("70B parameter scale", signals)
        self.assertNotIn("405B parameter scale", signals)
        self.assertNotIn("140K context", signals)
        rejected = audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("70B parameter scale", rejected)
        self.assertIn("405B parameter scale", rejected)
        self.assertIn("140K context", rejected)

    def test_directly_bound_jamba_architecture_signals_remain_eligible(self):
        summary = (
            "Jamba 1.5 Mini and Jamba 1.5 Large use an SSM-Transformer architecture with Mamba "
            "and provide a 256K context window."
        )
        signals = self._signals(summary, "Jamba 1.5 Mini and Large")
        self.assertIn("SSM-Transformer", signals)
        self.assertIn("Mamba", signals)
        self.assertIn("256K context", signals)

    def test_mistral_large_2_rejects_codestral_and_llama_values(self):
        summary = (
            "Mistral Large 2 is released with a 128K context window under the Mistral Research License. "
            "Following our experience with Codestral 22B and Codestral Mamba, we trained Mistral Large 2 with a larger code corpus. "
            "A comparison also discusses Llama 3.1 405B."
        )
        signals = self._signals(summary, "Mistral Large 2")
        self.assertNotIn("22B parameter scale", signals)
        self.assertNotIn("405B parameter scale", signals)
        self.assertNotIn("Mamba", signals)
        rejected = audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("22B parameter scale", rejected)
        self.assertIn("405B parameter scale", rejected)
        self.assertIn("Mamba", rejected)

    def test_ministral_rejects_category_and_comparator_sizes(self):
        summary = (
            "We are introducing Ministral 3B and Ministral 8B, both with a 128K context window. "
            "These models target the sub-10B category. A comparison table includes Gemma 2 2B and Mistral 7B."
        )
        signals = self._signals(summary, "Ministral 3B and 8B")
        self.assertIn("3B parameter scale", signals)
        self.assertIn("8B parameter scale", signals)
        self.assertIn("128K context", signals)
        self.assertNotIn("10B parameter scale", signals)
        self.assertNotIn("2B parameter scale", signals)
        self.assertNotIn("7B parameter scale", signals)

    def test_llama_32_does_not_absorb_llama_31_405b(self):
        summary = (
            "Llama 3.2 introduces Llama 3.2 1B and Llama 3.2 3B text models plus Llama 3.2 11B and Llama 3.2 90B vision models. "
            "The announcement compares these releases with the earlier Llama 3.1 405B model."
        )
        signals = self._signals(summary, "Llama 3.2")
        self.assertNotIn("405B parameter scale", signals)
        rejected = audit_base._AUDIT_ROWS[-1]["rejected_entity_bound_signals"]
        self.assertIn("405B parameter scale", rejected)

    def test_comparison_list_continuation_stays_bound_to_foreign_subject(self):
        summary = "SelectedModel 2 is discussed here. For comparison, ForeignModel 70B and 405B are stronger baselines."
        signals = self._signals(summary, "SelectedModel 2")
        self.assertNotIn("70B parameter scale", signals)
        self.assertNotIn("405B parameter scale", signals)


if __name__ == "__main__":
    unittest.main()
