import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "build-special-pdf.yml"
LAYOUT_POLICY = ROOT / "docs" / "special-layout-policy.md"


class SpecialPageBudgetContractTests(unittest.TestCase):
    def test_32_pages_is_soft_target_not_hard_floor(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn('test "$PAGE_COUNT" -ge 32', text)
        self.assertIn("page_target_soft':32", text)
        self.assertIn("'below_soft_target':page_count < 32", text)
        self.assertIn("'page_budget_policy':'soft-target-hard-ceiling'", text)
        self.assertIn("::warning title=Special page target::", text)

    def test_40_pages_remains_hard_ceiling(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('test "$PAGE_COUNT" -le 40', text)
        self.assertIn("'hard_max':40", text)

    def test_successful_build_provenance_records_soft_target_status(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("'page_budget':{", text)
        self.assertIn("'soft_target':32", text)
        self.assertIn("'below_soft_target':page_count < 32", text)
        self.assertIn("'policy':'soft-target-hard-ceiling'", text)

    def test_layout_policy_forbids_padding_to_reach_soft_target(self):
        text = LAYOUT_POLICY.read_text(encoding="utf-8")
        self.assertIn("32 pages as a soft editorial target", text)
        self.assertIn("40 pages as a hard ceiling", text)
        self.assertIn("must not fail for page count alone", text)
        self.assertIn("must not be invoked solely to satisfy the soft target", text)


if __name__ == "__main__":
    unittest.main()
