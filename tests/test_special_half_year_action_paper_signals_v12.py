from __future__ import annotations

import unittest

from scripts import revise_special_half_year_review_repairs_v12 as repair


class HalfYearActionPaperSignalsV12Tests(unittest.TestCase):
    def _signals(self, text: str) -> str:
        impl = repair.impl
        previous = impl._SIGNAL_PATTERNS
        impl._SIGNAL_PATTERNS = repair._EXTRA_SIGNAL_PATTERNS_V12 + previous
        try:
            return " / ".join(impl._technical_signals(text, [("2024-10-30", "PAPER_FIRST_SUBMISSION")]))
        finally:
            impl._SIGNAL_PATTERNS = previous

    def test_os_atlas_summary_is_specific(self) -> None:
        rendered = self._signals(
            "We developed OS-Atlas - a foundational GUI action model that excels at GUI grounding. "
            "We are releasing the largest open-source cross-platform GUI grounding corpus to date, "
            "which contains over 13 million GUI elements. Through extensive evaluation across six benchmarks "
            "spanning three different platforms (mobile, desktop, and web), OS-Atlas demonstrates improvements."
        )
        self.assertIn("foundation GUI action model", rendered)
        self.assertIn("GUI grounding", rendered)
        self.assertIn("cross-platform GUI grounding corpus", rendered)
        self.assertIn("13M超のGUI elements", rendered)
        self.assertIn("6 benchmarks / mobile・desktop・web", rendered)

    def test_toolsandbox_summary_is_specific(self) -> None:
        rendered = self._signals(
            "ToolSandbox includes stateful tool execution, implicit state dependencies between tools, "
            "a built-in user simulator supporting on-policy conversational evaluation and a dynamic evaluation "
            "strategy for intermediate and final milestones over an arbitrary trajectory."
        )
        self.assertIn("stateful tool execution", rendered)
        self.assertIn("implicit state dependencies between tools", rendered)
        self.assertIn("on-policy conversational evaluation", rendered)
        self.assertIn("dynamic milestone evaluation", rendered)

    def test_ai_scientist_summary_is_specific(self) -> None:
        rendered = self._signals(
            "This paper presents the first comprehensive framework for fully automatic scientific discovery. "
            "The AI Scientist generates novel research ideas, writes code, executes experiments, visualizes results, "
            "describes its findings by writing a full scientific paper, and then runs a simulated review process."
        )
        self.assertIn("fully automatic scientific discovery framework", rendered)
        self.assertIn("idea→code→experiment→paper workflow", rendered)
        self.assertIn("simulated review process", rendered)


if __name__ == "__main__":
    unittest.main()
