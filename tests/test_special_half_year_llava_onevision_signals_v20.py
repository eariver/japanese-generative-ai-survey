from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v20 as repair
from scripts import revise_special_half_year_review_repairs_v16 as event_layer


class HalfYearLlavaOneVisionSignalsV20Tests(unittest.TestCase):
    def test_llava_onevision_abstract_exposes_multi_scenario_transfer_scope(self) -> None:
        impl = event_layer.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS_V20 + previous
        try:
            abstract = (
                "We present LLaVA-OneVision, a family of open large multimodal models. "
                "The model addresses single-image, multi-image, and video scenarios. "
                "Its design allows strong transfer learning across different modalities/scenarios, "
                "with cross-scenario capabilities demonstrated through task transfer from images to videos."
            )
            signals = event_layer._safe_technical_signals(
                abstract,
                [("2024-08-06", "PAPER_FIRST_SUBMISSION")],
                "LLaVA-OneVision: Easy Visual Task Transfer",
            )
        finally:
            impl._SIGNAL_PATTERNS = previous
        rendered = " / ".join(signals)
        self.assertIn("open large multimodal model family", rendered)
        self.assertIn("single-image / multi-image / videoを単一modelで扱うscope", rendered)
        self.assertIn("cross-scenario visual task transfer", rendered)
        self.assertIn("image→video task transfer", rendered)


if __name__ == "__main__":
    unittest.main()
