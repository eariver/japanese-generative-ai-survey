from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v21 as repair
from scripts import revise_special_half_year_review_repairs_v16 as event_layer


class HalfYearEmu3SignalsV21Tests(unittest.TestCase):
    def test_emu3_abstract_exposes_next_token_multimodal_method(self) -> None:
        impl = event_layer.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS_V21 + previous
        try:
            abstract = (
                "We introduce Emu3, a new suite of multimodal models trained solely with next-token prediction. "
                "By tokenizing images, text, and videos into a discrete space, we train a single transformer from scratch "
                "on a mixture of multimodal sequences. The approach eliminates the need for diffusion or compositional "
                "architectures. Emu3 can generate high-fidelity video via predicting the next token in a video sequence. "
                "The paper also reports comparisons against several task-specific systems."
            )
            signals = event_layer._safe_technical_signals(
                abstract,
                [("2024-09-27", "PAPER_FIRST_SUBMISSION")],
                "Emu3: Next-Token Prediction is All You Need",
            )
        finally:
            impl._SIGNAL_PATTERNS = previous
        rendered = " / ".join(signals)
        self.assertIn("next-token predictionのみでmultimodal training", rendered)
        self.assertIn("image / text / videoをdiscrete token spaceへ統一", rendered)
        self.assertIn("single Transformer over mixed multimodal sequences", rendered)
        self.assertIn("diffusion / compositional architectureを不要化", rendered)
        self.assertIn("video sequenceのnext-token predictionによるvideo生成", rendered)
        self.assertNotIn("outperforms", rendered)


if __name__ == "__main__":
    unittest.main()
