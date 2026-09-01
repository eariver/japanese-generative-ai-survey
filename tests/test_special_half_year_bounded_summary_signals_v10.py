from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v10 as repair


class HalfYearBoundedSummarySignalsV10Tests(unittest.TestCase):
    def _signals(self, text: str) -> str:
        impl = repair.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS_V10 + previous
        try:
            return " / ".join(impl._technical_signals(text, [("2024-12-20", "RESEARCH_PUBLICATION")]))
        finally:
            impl._SIGNAL_PATTERNS = previous

    def test_deliberative_alignment_summary_is_specific(self) -> None:
        rendered = self._signals(
            "Introducing our new alignment strategy for o1 models, which are directly taught "
            "safety specifications and how to reason over them."
        )
        self.assertIn("safety specificationを直接教示", rendered)

    def test_sora_summary_is_specific(self) -> None:
        rendered = self._signals(
            "Our video generation model, Sora, is now available to use at sora.com. Users can "
            "generate videos up to 1080p resolution, up to 20 sec long. You can bring your own "
            "assets to extend, remix, and blend."
        )
        self.assertIn("sora.comでのvideo生成提供", rendered)
        self.assertIn("最大1080p video", rendered)
        self.assertIn("最大20秒video", rendered)
        self.assertIn("extend / remix / blend", rendered)

    def test_moshi_summary_is_specific(self) -> None:
        rendered = self._signals("Meet Moshi, the first real-time voice AI")
        self.assertIn("real-time voice AI", rendered)

    def test_human_validated_swe_bench_summary_is_specific(self) -> None:
        rendered = self._signals("We’re releasing a human-validated subset of SWE-bench for real-world software issues.")
        self.assertIn("human-validated SWE-bench subset", rendered)


if __name__ == "__main__":
    unittest.main()
