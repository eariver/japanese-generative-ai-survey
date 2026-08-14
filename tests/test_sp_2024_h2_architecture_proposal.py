from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts import validate_issue_architecture as via


class SP2024H2ArchitectureProposalTests(unittest.TestCase):
    def test_current_proposal_is_contract_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        architecture_input = root / "sources/SP-2024-H2/architecture/architecture-input-v0.1.json"
        plan_path = root / "sources/SP-2024-H2/architecture/issue-architecture-v0.1.json"

        report, passed = via.validate(architecture_input, plan_path, require_approved=False)
        self.assertTrue(passed, report)

        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertEqual(plan["architecture_version"], "v0.2")
        self.assertEqual(plan["status"], "PROPOSED")
        self.assertEqual(plan["page_budget"]["target"], 64)
        self.assertEqual(plan["page_budget"]["planned"], 64)
        self.assertTrue(plan["this_week_summary_written_last"])
        self.assertTrue(all(package["page_target"] <= 8 for package in plan["packages"]))
        self.assertEqual(sum(package["page_target"] for package in plan["packages"]), 64)


if __name__ == "__main__":
    unittest.main()
