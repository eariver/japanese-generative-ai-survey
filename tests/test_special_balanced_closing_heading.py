from pathlib import Path
import unittest


class BalancedClosingHeadingContractTests(unittest.TestCase):
    def test_closing_heading_is_artifact_driven(self) -> None:
        text=Path("scripts/revise_special_balanced_layout.py").read_text(encoding="utf-8")
        self.assertIn('final.get("closing_heading")', text)
        self.assertIn('この月をどう位置づけるか', text)
        self.assertNotIn(r"\subsection*{7月をどう位置づけるか}", text)


if __name__ == "__main__":
    unittest.main()
