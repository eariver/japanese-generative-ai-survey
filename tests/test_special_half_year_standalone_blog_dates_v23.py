from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v23 as repair
from scripts import revise_special_half_year_review_repairs_v16 as news_layer
from scripts import revise_special_half_year_review_repairs_v22 as flash_layer


class HalfYearStandaloneBlogDatesV23Tests(unittest.TestCase):
    def test_flashattention_blog_news_navigation_is_not_a_living_history(self) -> None:
        summary = (
            "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision – PyTorch "
            "Skip to main content Blog & News Blog Announcements Case Studies. "
            "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision "
            "By Authors July 11, 2024 November 12th, 2024 No Comments "
            "Attention is a bottleneck. We describe three main techniques to speed up attention on Hopper GPUs: "
            "exploiting asynchrony of the Tensor Cores and TMA to overlap overall computation and data movement "
            "via warp-specialization, interleave block-wise matmul and softmax operations, and incoherent processing "
            "that leverages hardware support for FP8 low-precision. We are excited to release FlashAttention-3. "
            "New hardware features on Hopper GPUs – WGMMA, TMA, FP8. FlashAttention-3 makes use of all of these features."
        )
        self.assertFalse(repair._strict_is_living_changelog(summary))

        previous_classifier = news_layer._is_living_changelog
        previous_patterns = news_layer.impl._SIGNAL_PATTERNS
        news_layer._is_living_changelog = repair._strict_is_living_changelog
        news_layer.impl._SIGNAL_PATTERNS = flash_layer._EXTRA_SIGNAL_PATTERNS_V22 + previous_patterns
        try:
            window = news_layer._safe_event_window(
                summary,
                [("2024-07-11", "SOFTWARE_RELEASE")],
                "FlashAttention-3",
            )
            signals = news_layer._safe_technical_signals(
                summary,
                [("2024-07-11", "SOFTWARE_RELEASE")],
                "FlashAttention-3",
            )
        finally:
            news_layer._is_living_changelog = previous_classifier
            news_layer.impl._SIGNAL_PATTERNS = previous_patterns

        self.assertIn("Hopper", window)
        self.assertIn("TMA", window)
        self.assertIn("Hopper TMA / WGMMA活用", " / ".join(signals))

    def test_ltx_dated_news_block_remains_a_living_history(self) -> None:
        summary = (
            "LTX-Video Table of Contents Introduction. "
            "News October 23, 2025: LTX-2 announced. July 16, 2025: later release. "
            "November 21, 2024: Initial release v0.9.0. Initial release of LTX-Video. "
            "Support text-to-video and image-to-video generation. Models Name current table."
        )
        self.assertTrue(repair._strict_is_living_changelog(summary))

    def test_project_updates_and_change_log_remain_living_histories(self) -> None:
        cog = (
            "Project Updates News : 2024/8/27 : CogVideoX-5B. "
            "2024/8/6 : CogVideoX-2B. Table of Contents Model Introduction."
        )
        deepseek = (
            "Change Log On this page Change Log Date: 2025-01-20 DeepSeek-R1. "
            "Date: 2024-12-26 DeepSeek-V3."
        )
        self.assertTrue(repair._strict_is_living_changelog(cog))
        self.assertTrue(repair._strict_is_living_changelog(deepseek))


if __name__ == "__main__":
    unittest.main()
