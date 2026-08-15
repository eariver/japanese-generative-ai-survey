from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v9 as repair


class HalfYearConciseSummarySignalTests(unittest.TestCase):
    def _signals(self, text: str) -> str:
        impl = repair.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS + previous
        try:
            return " / ".join(impl._technical_signals(text, [("2024-11-20", "MODEL_PREVIEW")]))
        finally:
            impl._SIGNAL_PATTERNS = previous

    def test_deepseek_preview_summary_is_specific(self) -> None:
        rendered = self._signals(
            "Transparent thought process in real-time. Inference Scaling Laws of DeepSeek-R1-Lite-Preview. "
            "Open-source models & API coming soon! Try it now at http://chat.deepseek.com"
        )
        self.assertIn("transparent reasoning trace", rendered)
        self.assertIn("inference scaling behavior", rendered)
        self.assertIn("open model/API still forthcoming at preview time", rendered)

    def test_realtime_api_feed_summary_is_specific(self) -> None:
        rendered = self._signals("Developers can now build fast speech-to-speech experiences into their applications")
        self.assertIn("speech-to-speech API", rendered)

    def test_prompt_caching_feed_summary_is_specific(self) -> None:
        rendered = self._signals("Offering automatic discounts on inputs that the model has recently seen")
        self.assertIn("recent-input reuse / caching discount", rendered)

    def test_search_feed_summary_is_specific(self) -> None:
        rendered = self._signals("Get fast, timely answers with links to relevant web sources")
        self.assertIn("source links in search answers", rendered)


if __name__ == "__main__":
    unittest.main()
