from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_review_repairs_v16 as repair


class HalfYearEventBoundedNotesV14Tests(unittest.TestCase):
    def _signals(self, text: str, date: str, title: str) -> str:
        event = repair.event
        impl = repair.impl
        previous_patterns = impl._SIGNAL_PATTERNS
        previous_dynamic = impl._DYNAMIC_PATTERNS
        impl._SIGNAL_PATTERNS = event._EVENT_BOUNDED_SIGNALS + tuple(
            (name, pattern)
            for name, pattern in previous_patterns
            if name not in event._UNSAFE_SIGNAL_NAMES
        )
        impl._DYNAMIC_PATTERNS = tuple(
            item
            for item in previous_dynamic
            if item[0] not in event._UNSAFE_DYNAMIC_PREFIXES
        )
        try:
            return " / ".join(
                repair._safe_technical_signals(
                    text,
                    [(date, "MODEL_RELEASE")],
                    title,
                )
            )
        finally:
            impl._SIGNAL_PATTERNS = previous_patterns
            impl._DYNAMIC_PATTERNS = previous_dynamic

    def test_arxiv_uses_abstract_not_html_experimental_chrome(self) -> None:
        summary = (
            "arXiv page View PDF HTML (experimental) Submitted on 6 Aug 2024 "
            "Abstract: We study test-time compute and a compute-optimal scaling strategy. "
            "Subjects: Machine Learning Submission history"
        )
        window = repair._safe_event_window(
            summary,
            [("2024-08-06", "PAPER_FIRST_SUBMISSION")],
            "Scaling LLM Test-Time Compute Optimally",
        )
        self.assertNotIn("HTML (experimental)", window)
        self.assertIn("test-time compute", window)
        rendered = self._signals(summary, "2024-08-06", "Scaling LLM Test-Time Compute Optimally")
        self.assertNotIn("experimental release", rendered)
        self.assertIn("test-time compute", rendered)
        self.assertIn("compute-optimal scaling", rendered)

    def test_qwen_redirect_seconds_are_outside_event_window(self) -> None:
        summary = (
            "We have a new blog. This page will automatically redirect in 5 seconds. "
            "November 28, 2024 QwQ-32B-Preview is an experimental research model focused on reasoning. "
            "QwQ-32B-Preview has 32B parameters."
        )
        window = repair._safe_event_window(
            summary,
            [("2024-11-28", "MODEL_PREVIEW")],
            "QwQ-32B-Preview",
        )
        self.assertNotIn("5 seconds", window)
        rendered = self._signals(summary, "2024-11-28", "QwQ-32B-Preview")
        self.assertIn("32B parameter scale", rendered)
        self.assertNotIn("5s generation", rendered)
        self.assertNotIn("experimental release", rendered)

    def test_cogvideox_living_readme_uses_only_last_target_date_slice(self) -> None:
        summary = (
            "Project Updates News: 2025/03/24 new toolkit. "
            "2024/8/27 released CogVideoX-5B with FP8 and INT8 options. "
            "2024/8/6 open-sourced 3D Causal VAE. "
            "2024/8/6 open-sourced the first CogVideoX series model, CogVideoX-2B, for text-to-video generation. "
            "Current model table: CogVideoX-5B FP8 INT8."
        )
        window = repair._safe_event_window(
            summary,
            [("2024-08-06", "MODEL_RELEASE")],
            "CogVideoX",
        )
        self.assertIn("CogVideoX-2B", window)
        self.assertNotIn("2024/8/27", window)
        self.assertNotIn("Current model table", window)
        rendered = self._signals(summary, "2024-08-06", "CogVideoX")
        self.assertIn("2B parameter scale", rendered)
        self.assertNotIn("5B parameter scale", rendered)
        self.assertNotIn("FP8", rendered)
        self.assertNotIn("INT8", rendered)

    def test_ltx_living_readme_excludes_later_13b_fp8_updates(self) -> None:
        summary = (
            "News October 23, 2025: LTX-2 announced with 13B and FP8. "
            "July 16, 2025: released 13B distilled FP8 models. "
            "November 21, 2024: Initial release v0.9.0. Initial release of LTX-Video. "
            "Support text-to-video and image-to-video generation. "
            "Current model table now lists 13B FP8 variants."
        )
        window = repair._safe_event_window(
            summary,
            [("2024-11-21", "MODEL_RELEASE")],
            "LTX-Video",
        )
        self.assertIn("text-to-video", window)
        self.assertNotIn("July 16, 2025", window)
        self.assertNotIn("Current model table", window)
        rendered = self._signals(summary, "2024-11-21", "LTX-Video")
        self.assertIn("text-to-video", rendered)
        self.assertIn("image-to-video", rendered)
        self.assertNotIn("13B parameter scale", rendered)
        self.assertNotIn("FP8", rendered)

    def test_navigation_ocr_does_not_bind_to_moderation_api(self) -> None:
        summary = (
            "Navigation Latest models Mistral OCR 4. November 7, 2024 Mistral Moderation API. "
            "Our model is an LLM classifier trained to classify text inputs into 9 categories."
        )
        window = repair._safe_event_window(
            summary,
            [("2024-11-07", "API_AVAILABILITY")],
            "Mistral Moderation API",
        )
        self.assertNotIn("Mistral OCR 4", window)
        rendered = self._signals(summary, "2024-11-07", "Mistral Moderation API")
        self.assertIn("9 content categories", rendered)
        self.assertIn("content moderation classifier", rendered)
        self.assertNotIn("OCR", rendered)

    def test_olmo2_anchor_skips_olmoe_background(self) -> None:
        summary = (
            "November 26, 2024 Ai2. Since the first OLMo release, in September we released OLMoE, "
            "a mixture-of-experts model. Announcing OLMo 2. We introduce OLMo 2, a new family of 7B "
            "and 13B models trained on up to 5T tokens. We release weights, data, code, recipes and "
            "intermediate checkpoints."
        )
        window = repair._safe_event_window(
            summary,
            [("2024-11-26", "MODEL_RELEASE")],
            "OLMo 2",
        )
        self.assertTrue(window.startswith("OLMo 2") or window.startswith("Announcing OLMo 2"))
        self.assertNotIn("OLMoE", window)
        rendered = self._signals(summary, "2024-11-26", "OLMo 2")
        self.assertIn("7B parameter scale", rendered)
        self.assertIn("13B parameter scale", rendered)
        self.assertIn("5T training tokens", rendered)
        self.assertNotIn("Mixture-of-Experts", rendered)

    def test_existing_technical_clause_is_reset_before_reenrichment(self) -> None:
        note = (
            "\\begin{technicalnote}{Artifact}{主要資料}\n"
            "\\item \\textbf{一次情報で確認できる事実}: 組織の一次資料により、Artifactについて2024-10-01にモデル公開を確認した。 "
            "一次資料の技術範囲として OLD FALSE POSITIVE を確認できる。\n"
            "\\end{technicalnote}\n"
        )
        info = {
            "canonical_title": "Artifact",
            "organization": "組織",
            "events": [("2024-10-01", "MODEL_RELEASE")],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.tex"
            path.write_text(note, encoding="utf-8")
            repair._reset_existing_fact_lines(path, {"Artifact": info})
            revised = path.read_text(encoding="utf-8")
        self.assertNotIn("OLD FALSE POSITIVE", revised)
        self.assertIn("2024-10-01", revised)
        self.assertEqual(revised.count("一次情報で確認できる事実"), 1)


if __name__ == "__main__":
    unittest.main()
