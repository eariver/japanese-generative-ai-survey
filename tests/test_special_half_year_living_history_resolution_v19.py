from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v19 as repair
from scripts import revise_special_half_year_review_repairs_v16 as window_layer


class HalfYearLivingHistoryResolutionV19Tests(unittest.TestCase):
    def test_cogvideox_date_is_resolved_inside_project_updates_not_model_table(self) -> None:
        summary = (
            "Navigation Changelog Marketplace. Project Updates "
            "News : 2024/8/27 : We have open-sourced CogVideoX-5B with FP8 and INT8. "
            "2024/8/6 : We have open-sourced 3D Causal VAE used for CogVideoX-2B. "
            "2024/8/6 : We have open-sourced the first model of the CogVideoX series, CogVideoX-2B, "
            "for text-to-video generation. "
            "Source : 2022/5/19 : older CogVideo release. Table of Contents Quick Start Model Introduction "
            "Model Name CogVideoX-2B CogVideoX-5B Release Date August 6, 2024 August 27, 2024 "
            "Inference Precision FP8 INT8."
        )
        pos = repair._last_event_position(summary, [("2024-08-06", "MODEL_RELEASE")])
        self.assertIsNotNone(pos)
        self.assertIn("first model of the CogVideoX series", summary[pos : pos + 220])
        self.assertLess(pos, summary.index("Table of Contents"))

        previous = repair.event._last_event_position
        repair.event._last_event_position = repair._last_event_position
        try:
            window = window_layer._safe_event_window(
                summary,
                [("2024-08-06", "MODEL_RELEASE")],
                "CogVideoX",
            )
        finally:
            repair.event._last_event_position = previous
        self.assertIn("CogVideoX-2B", window)
        self.assertIn("text-to-video", window)
        self.assertNotIn("Model Introduction", window)
        self.assertNotIn("FP8", window)
        self.assertNotIn("INT8", window)

    def test_recognized_history_without_target_date_does_not_fall_through_to_table(self) -> None:
        summary = (
            "Project Updates 2024/8/27 : CogVideoX-5B release. "
            "Table of Contents Model Introduction Release Date August 6, 2024."
        )
        pos = repair._last_event_position(summary, [("2024-08-06", "MODEL_RELEASE")])
        self.assertIsNone(pos)

    def test_ltx_history_can_begin_after_earlier_table_of_contents(self) -> None:
        summary = (
            "Table of Contents Introduction Models. "
            "News October 23, 2025: LTX-2 announced. July 16, 2025: later 13B release. "
            "November 21, 2024: Initial release v0.9.0. Initial release of LTX-Video. "
            "Support text-to-video and image-to-video generation. Models Name current table."
        )
        bounds = repair._history_bounds(summary)
        self.assertIsNotNone(bounds)
        start, end = bounds
        self.assertGreater(start, summary.index("Table of Contents"))
        self.assertLess(end, len(summary))
        pos = repair._last_event_position(summary, [("2024-11-21", "MODEL_RELEASE")])
        self.assertIsNotNone(pos)
        self.assertIn("Initial release v0.9.0", summary[pos : pos + 180])

    def test_deepseek_change_log_target_remains_inside_history(self) -> None:
        summary = (
            "Navigation Quick Start Models. Change Log On this page Change Log Date: 2025-01-20 "
            "DeepSeek-R1 release. Date: 2024-12-26 deepseek-chat The deepseek-chat model has been "
            "upgraded to DeepSeek-V3. The API remains unchanged. Date: 2024-12-10 older update."
        )
        pos = repair._last_event_position(summary, [("2024-12-26", "MODEL_RELEASE")])
        self.assertIsNotNone(pos)
        self.assertIn("DeepSeek-V3", summary[pos : pos + 180])


if __name__ == "__main__":
    unittest.main()
