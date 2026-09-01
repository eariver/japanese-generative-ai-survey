from __future__ import annotations

import unittest

from scripts import postprocess_special_reader_facing_notes as taxonomy
from scripts import revise_special_reader_enum_cleanup as cleanup


class SpecialReaderCanonicalCasingTests(unittest.TestCase):
    def test_h2_residual_machine_casing_is_canonicalized(self) -> None:
        source = "\n".join(
            [
                r"時系列 & 2025-07-07 (Batch MODE（公開）); 2025-07-17 (VEO3（Preview）); 2025-07-22 (Gemini 2.5 Flash LITE（公開）); 2025-08-14 (IMAGEN4（一般提供）); 2025-08-26 (Gemini 2.5 IMAGE（Preview）); 2025-09-25 (Robotics ER 1 5（Preview）); 2025-10-07 (COMPUTER USE（Preview）); 2025-10-15 (VEO3 1（Preview）); 2025-11-18 (Gemini 3 PRO（Preview）); 2025-12-17 (Gemini 3 FLASH（Preview）) \\",
                r"時系列 & 2025-07-22 (Qwen3 CODER（公開）); 2025-09-11 (Qwen3 NEXT（公開）); 2025-11-03 (Qwen3 MAX（Preview）); 2025-12-04 (Qwen3 OMNI（更新）); 2025-12-31 (Qwen Image MAX（公開）) \\",
                r"時系列 & 2025-11-06 (Kimi K2 THINKING（公開）); 2025-07-10 (DEVSTRAL（更新）); 2025-07-15 (VOXTRAL（公開）); 2025-07-30 (Codestral 25 08); 2025-07-17 (Le Chat Deep 研究) \\",
                r"時系列 & 2025-10-27 (Minimax M2（公開）); 2025-10-28 (Hailuo 2 3（公開）); 2025-12-22 (Minimax M2 1（公開）) \\",
                r"時系列 & 2025-10-21 (ATLAS（公開）); 2025-10-30 (Owl ARCHITECTURE（公開）) \\",
            ]
        )
        rendered = taxonomy.translate_machine_labels_compat(source)
        expected = [
            "Batch Mode（公開）",
            "Veo 3（Preview）",
            "Gemini 2.5 Flash-Lite（公開）",
            "Imagen 4（一般提供）",
            "Gemini 2.5 Image（Preview）",
            "Robotics-ER 1.5（Preview）",
            "Computer Use（Preview）",
            "Veo 3.1（Preview）",
            "Gemini 3 Pro（Preview）",
            "Gemini 3 Flash（Preview）",
            "Qwen3-Coder（公開）",
            "Qwen3-Next（公開）",
            "Qwen3-Max（Preview）",
            "Qwen3-Omni（更新）",
            "Qwen Image Max（公開）",
            "Kimi K2 Thinking（公開）",
            "Devstral（更新）",
            "Voxtral（公開）",
            "Codestral 25.08",
            "Le Chat Deep Research",
            "MiniMax M2（公開）",
            "Hailuo 2.3（公開）",
            "MiniMax M2.1（公開）",
            "Atlas（公開）",
            "OWL architecture（公開）",
        ]
        for value in expected:
            self.assertIn(value, rendered)
        self.assertEqual(taxonomy.reader_taxonomy_findings(rendered), [])

    def test_guard_flags_machine_casing_but_allows_intentional_acronyms(self) -> None:
        bad = r"時系列 & 2025-11-18 (Gemini 3 FLASH（Preview）); 2025-07-17 (VEO3（Preview）); 2025-10-21 (ATLAS（公開）); 2025-10-30 (Owl ARCHITECTURE（公開）) \\"
        findings = taxonomy.reader_taxonomy_findings(bad)
        self.assertTrue(any("FLASH" in finding for finding in findings))
        self.assertTrue(any("VEO3" in finding for finding in findings))
        self.assertTrue(any("ATLAS" in finding for finding in findings))
        self.assertTrue(any("ARCHITECTURE" in finding for finding in findings))

        good = r"時系列 & 2025-12-22 (GLM 4.7（公開）); 2025-11-13 (SIMA 2（発表）); 2025-08-21 (V3.1 API（更新）); 2025-10-30 (OWL architecture（公開）) \\"
        self.assertEqual(taxonomy.reader_taxonomy_findings(good), [])

    def test_cleanup_route_uses_shared_mapper_and_validator(self) -> None:
        source = r"時系列 & 2025-07-07 (Batch MODE（公開）); 2025-11-06 (Kimi K2 THINKING（公開）); 2025-10-21 (ATLAS（公開）); 2025-10-30 (Owl ARCHITECTURE（公開）) \\"
        rendered, count = cleanup.normalize(source)
        self.assertGreaterEqual(count, 4)
        self.assertIn("Batch Mode（公開）", rendered)
        self.assertIn("Kimi K2 Thinking（公開）", rendered)
        self.assertIn("Atlas（公開）", rendered)
        self.assertIn("OWL architecture（公開）", rendered)
        self.assertEqual(cleanup.remaining_machine_enums(rendered), [])


if __name__ == "__main__":
    unittest.main()
