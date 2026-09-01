from __future__ import annotations

import unittest
from unittest import mock

from scripts import revise_special_half_year_review_repairs_v7 as repair
from scripts import revise_special_half_year_review_repairs_v31 as dedup


class HalfYearSourceSpecificTechnicalNoteTests(unittest.TestCase):
    def test_llama_summary_yields_concrete_engineering_signals(self) -> None:
        summary = (
            "Llama 3.1 includes 405B, 70B and 8B models. "
            "The 8B and 70B models support a 128K context window. "
            "The flagship uses a decoder-only transformer and production inference uses FP8. "
            "Model weights are available for download."
        )
        signals = repair._technical_signals(summary, [("2024-07-23", "MODEL_RELEASE")])
        rendered = " / ".join(signals)
        self.assertIn("405B parameter scale", rendered)
        self.assertIn("128K context", rendered)
        self.assertIn("decoder-only Transformer", rendered)
        self.assertIn("FP8", rendered)

    def test_paper_summary_yields_method_and_evaluation_scope(self) -> None:
        summary = (
            "We built AppWorld Engine with 9 day-to-day apps operable via 457 APIs. "
            "AppWorld Benchmark contains 750 autonomous agent tasks and supports "
            "programmatic evaluation with state-based unit tests."
        )
        signals = repair._technical_signals(summary, [("2024-07-26", "PAPER_FIRST_SUBMISSION")])
        rendered = " / ".join(signals)
        self.assertIn("9 apps", rendered)
        self.assertIn("457 APIs", rendered)
        self.assertIn("750 agent tasks", rendered)
        self.assertIn("state-based unit tests", rendered)

    def test_thin_provenance_does_not_create_a_fake_detail(self) -> None:
        signals = repair._technical_signals(
            "This item was released during the period.",
            [("2024-10-01", "MODEL_RELEASE")],
        )
        self.assertEqual(signals, [])

    def test_detail_override_must_preserve_exact_evidence_urls(self) -> None:
        info = {"urls": ["https://example.com/MODEL_CARD.md"]}
        with self.assertRaisesRegex(ValueError, "URL mismatch"):
            repair._validate_override(
                "Artifact",
                {
                    "source_urls": ["https://example.com/モデル_CARD.md"],
                    "technical_points": ["具体的な技術点。"],
                },
                info,
            )

    def test_chronology_only_fact_is_enriched_exactly_once(self) -> None:
        block = (
            "\\begin{technicalnote}{Artifact}{主要資料}\n"
            "\\item \\textbf{一次情報で確認できる事実}: "
            "組織の一次資料により、Artifactについて2024-10-01にモデル公開を確認した。\n"
            "\\end{technicalnote}"
        )
        info = {
            "canonical_title": "Artifact",
            "organization": "組織",
            "events": [("2024-10-01", "MODEL_RELEASE")],
            "technical_points": ["一次資料の技術範囲として JSON Schema を確認できる。"],
        }
        revised, count = repair._enrich_fact_line(block, "Artifact", info)
        self.assertEqual(count, 1)
        self.assertIn("JSON Schema", revised)

    def test_existing_source_specific_point_is_not_appended_twice(self) -> None:
        point = "MobileLLMはdeep-and-thinなTransformer構成を中心に探索した。"
        inherited = "選定済み一次資料では、" + point
        info = {
            "canonical_title": "MobileLLM",
            "technical_points": [point],
        }
        with mock.patch.object(dedup.detail, "_ORIGINAL_FACT", return_value=inherited):
            rendered = dedup.deduplicated_source_specific_fact("MobileLLM", info)
        self.assertEqual(rendered, inherited)
        self.assertEqual(rendered.count(point), 1)

    def test_new_source_specific_point_is_still_appended(self) -> None:
        info = {
            "canonical_title": "Artifact",
            "technical_points": ["追加の技術点。"],
        }
        with mock.patch.object(dedup.detail, "_ORIGINAL_FACT", return_value="時系列上の事実。"):
            rendered = dedup.deduplicated_source_specific_fact("Artifact", info)
        self.assertEqual(rendered, "時系列上の事実。 追加の技術点。")


if __name__ == "__main__":
    unittest.main()
