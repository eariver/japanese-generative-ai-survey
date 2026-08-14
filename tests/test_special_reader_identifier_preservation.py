from __future__ import annotations

import unittest

from scripts import postprocess_special_reader_facing_notes_v2 as reader


class SpecialReaderIdentifierPreservationTests(unittest.TestCase):
    def test_url_path_and_code_identifiers_are_byte_preserved(self) -> None:
        source = "\n".join(
            [
                r"時系列 & 2024-12-06 (MODEL_RELEASE) \\",
                r"\item {\scriptsize\url{https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md}}",
                r"raw https://example.com/API_MODEL_ID/MODEL_CARD.md",
                r"code \texttt{API_MODEL_ID}",
            ]
        )
        rendered = reader.translate_machine_labels_preserving_identifiers(source)
        self.assertIn("(モデル公開)", rendered)
        self.assertIn("/MODEL_CARD.md", rendered)
        self.assertIn("/API_MODEL_ID/MODEL_CARD.md", rendered)
        self.assertIn(r"\texttt{API_MODEL_ID}", rendered)
        self.assertNotIn("モデル_CARD.md", rendered)

    def test_compat_translation_inherits_identifier_protection(self) -> None:
        source = r"2024-12-06 (MODEL_RELEASE) \url{https://example.com/MODEL_CARD.md}"
        rendered = reader.translate_machine_labels_compat(source)
        self.assertIn("モデル公開", rendered)
        self.assertIn("https://example.com/MODEL_CARD.md", rendered)
        self.assertNotIn("https://example.com/モデル_CARD.md", rendered)

    def test_nested_opaque_guards_are_composable(self) -> None:
        source = r"MODEL_RELEASE \url{https://example.com/MODEL_CARD.md}"
        outer_text, outer = reader._protect_opaque_identifiers(source)
        inner_text, inner = reader._protect_opaque_identifiers(outer_text)
        restored_inner = reader._restore_opaque_identifiers(inner_text, inner)
        self.assertEqual(restored_inner, outer_text)
        restored = reader._restore_opaque_identifiers(restored_inner, outer)
        self.assertEqual(restored, source)

    def test_safety_material_uses_source_semantic_overrides(self) -> None:
        expected = {
            "Automated Reasoning checks for Amazon Bedrock Guardrails": "安全性手法",
            "Deliberative alignment: reasoning enables safer language models": "Alignment研究",
            "Alignment faking in large language models": "Alignment研究",
        }
        for title, label in expected.items():
            self.assertEqual(reader.core.TYPE_OVERRIDES[title], label)


if __name__ == "__main__":
    unittest.main()
