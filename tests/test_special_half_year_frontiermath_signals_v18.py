from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v18 as repair
from scripts import revise_special_half_year_review_repairs_v16 as event_layer


class HalfYearFrontierMathSignalsV18Tests(unittest.TestCase):
    def test_frontiermath_abstract_exposes_construction_not_author_score(self) -> None:
        impl = event_layer.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS_V18 + previous
        try:
            abstract = (
                "We introduce FrontierMath, a benchmark of hundreds of original, exceptionally challenging "
                "mathematics problems crafted and vetted by expert mathematicians. The questions cover most major "
                "branches of modern mathematics. FrontierMath uses new, unpublished problems and automated "
                "verification to reliably evaluate models while minimizing risk of data contamination. "
                "Current state-of-the-art AI models solve under 2% of problems."
            )
            signals = event_layer._safe_technical_signals(
                abstract,
                [("2024-11-07", "PAPER_FIRST_SUBMISSION")],
                "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI",
            )
        finally:
            impl._SIGNAL_PATTERNS = previous
        rendered = " / ".join(signals)
        self.assertIn("expert-vetted original mathematics benchmark", rendered)
        self.assertIn("broad modern-mathematics coverage", rendered)
        self.assertIn("unpublished problems for contamination control", rendered)
        self.assertIn("automated verification", rendered)
        self.assertNotIn("2%", rendered)


if __name__ == "__main__":
    unittest.main()
