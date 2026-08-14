import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "build-special-pdf.yml"
LAYOUT_POLICY = ROOT / "docs" / "special-layout-policy.md"
MONTHLY_MANIFEST = ROOT / "specials" / "2026-M07" / "edition.json"
HALF_YEAR_MANIFEST = ROOT / "specials" / "2025-H2" / "edition.json"


class SpecialPageBudgetContractTests(unittest.TestCase):
    def test_workflow_uses_manifest_soft_target_not_hard_floor(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn('test "$PAGE_COUNT" -ge "$PAGE_TARGET"', text)
        self.assertIn("['page_budget']['target']", text)
        self.assertIn("'page_target_soft':soft_target", text)
        self.assertIn("'below_soft_target':page_count < soft_target", text)
        self.assertIn("'page_budget_policy':'manifest-soft-target-hard-ceiling'", text)
        self.assertIn("::warning title=Special page target::", text)

    def test_workflow_uses_manifest_hard_ceiling(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("['page_budget']['max']", text)
        self.assertIn('test "$PAGE_COUNT" -le "$PAGE_MAX"', text)
        self.assertIn("'hard_max':hard_max", text)

    def test_successful_build_provenance_records_resolved_budget(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("'page_budget':{", text)
        self.assertIn("'soft_target':soft_target", text)
        self.assertIn("'below_soft_target':page_count < soft_target", text)
        self.assertIn("'policy':'manifest-soft-target-hard-ceiling'", text)

    def test_monthly_manifest_preserves_default_32_40_budget(self):
        data = json.loads(MONTHLY_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["page_budget"]["target"], 32)
        self.assertEqual(data["page_budget"]["max"], 40)

    def test_half_year_manifest_can_raise_budget_without_changing_monthly_default(self):
        data = json.loads(HALF_YEAR_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["page_budget"]["target"], 64)
        self.assertEqual(data["page_budget"]["max"], 96)

    def test_layout_policy_forbids_padding_to_reach_soft_target(self):
        text = LAYOUT_POLICY.read_text(encoding="utf-8")
        self.assertIn("32 pages as the default soft editorial target", text)
        self.assertIn("40 pages as the default hard ceiling", text)
        self.assertIn("edition manifest may define a different page budget", text)
        self.assertIn("must not fail for page count alone", text)
        self.assertIn("must not be invoked solely to satisfy the soft target", text)


if __name__ == "__main__":
    unittest.main()
