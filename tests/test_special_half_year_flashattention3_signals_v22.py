from __future__ import annotations
import unittest
from scripts import revise_special_half_year_review_repairs_v22 as repair
from scripts import revise_special_half_year_review_repairs_v16 as event_layer

class HalfYearFlashAttention3SignalsV22Tests(unittest.TestCase):
    def test_flashattention3_source_exposes_hopper_kernel_scope(self) -> None:
        impl=event_layer.impl; prev=impl._SIGNAL_PATTERNS; impl._SIGNAL_PATTERNS=repair._EXTRA_SIGNAL_PATTERNS_V22+prev
        try:
            text=("We describe techniques to speed up attention on Hopper GPUs: exploiting asynchrony of Tensor Cores and TMA to overlap overall computation and data movement via warp-specialization, interleave block-wise matmul and softmax operations, and incoherent processing that leverages hardware support for FP8 low-precision. WGMMA and TMA are Hopper features.")
            signals=event_layer._safe_technical_signals(text,[("2024-07-11","SOFTWARE_RELEASE")],"FlashAttention-3")
        finally: impl._SIGNAL_PATTERNS=prev
        rendered=" / ".join(signals)
        self.assertIn("Hopper TMA / WGMMA活用",rendered)
        self.assertIn("warp-specializationでcomputeとdata movementをoverlap",rendered)
        self.assertIn("block-wise matmulとsoftmaxをinterleave",rendered)
        self.assertIn("FP8向けincoherent processing",rendered)

if __name__ == "__main__": unittest.main()
