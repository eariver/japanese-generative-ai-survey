import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "build-special-pdf.yml"
LAYOUT_POLICY = ROOT / "docs" / "special-layout-policy.md"
MONTHLY_MANIFEST = ROOT / "specials" / "2026-M07" / "edition.json"
HALF_YEAR_MANIFEST = ROOT / "specials" / "2025-H2" / "edition.json"


class SpecialPageBudgetContractTests(unittest.TestCase):
    def test_reproducible_build_does_not_enforce_editorial_page_budget(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("['page_budget']['target']", text)
        self.assertNotIn("['page_budget']['max']", text)
        self.assertNotIn('test "$PAGE_COUNT" -ge "$PAGE_TARGET"', text)
        self.assertNotIn('test "$PAGE_COUNT" -le "$PAGE_MAX"', text)
        self.assertNotIn("::warning title=Special page target::", text)
        self.assertIn("page_count", text)
        self.assertIn("layout_log_findings", text)

    def test_reproducible_build_is_read_only_and_reports_exact_build_evidence(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", text)
        self.assertNotIn("pipeline-state.json", text)
        self.assertNotIn("git push", text)
        self.assertNotIn("github-actions[bot]", text)
        self.assertIn("profile_sha256", text)
        self.assertIn("source_sha256", text)
        self.assertIn("pdf_sha256", text)
        self.assertIn("byte_count", text)
        self.assertIn("special-pdf-build-audit.json", text)

    def test_monthly_manifest_preserves_default_32_40_budget(self):
        data = json.loads(MONTHLY_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["page_budget"]["target"], 32)
        self.assertEqual(data["page_budget"]["max"], 40)

    def test_half_year_manifest_can_raise_budget_without_changing_monthly_default(self):
        data = json.loads(HALF_YEAR_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["page_budget"]["target"], 64)
        self.assertEqual(data["page_budget"]["max"], 96)

    def test_layout_policy_keeps_page_budget_as_editorial_authority(self):
        text = LAYOUT_POLICY.read_text(encoding="utf-8")
        self.assertIn("32 pages as the default soft editorial target", text)
        self.assertIn("40 pages as the default hard ceiling", text)
        self.assertIn("edition manifest may define a different page budget", text)
        self.assertIn("must not fail for page count alone", text)
        self.assertIn("must not be invoked solely to satisfy the soft target", text)


if __name__ == "__main__":
    unittest.main()
