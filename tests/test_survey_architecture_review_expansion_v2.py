from __future__ import annotations

import unittest

from scripts import survey_architecture_v2 as architecture
from scripts import survey_production_v2 as core
from tests import test_survey_architecture_v2 as architecture_tests


IMPLEMENTATION_SHA = "4" * 40


class SurveyArchitectureReviewExpansionV2Tests(unittest.TestCase):
    def test_research_expansion_summary_counts_edges_passes_and_obligations(self) -> None:
        discoveries = [
            {
                "provenance": {
                    "origin": "BASE",
                    "research_pass": 0,
                    "parent_refs": [],
                    "obligation_ids": [],
                }
            },
            {
                "provenance": {
                    "origin": "REFERENCE_EXPANSION",
                    "research_pass": 1,
                    "parent_refs": ["seed"],
                    "obligation_ids": [],
                }
            },
            {
                "provenance": {
                    "origin": "PARALLEL_EXPANSION",
                    "research_pass": 1,
                    "parent_refs": ["seed"],
                    "obligation_ids": ["parallel-coverage"],
                }
            },
            {
                "provenance": {
                    "origin": "GAP_FILL",
                    "research_pass": 2,
                    "parent_refs": [],
                    "obligation_ids": ["parallel-coverage", "bridge-gap"],
                }
            },
        ]
        self.assertEqual(
            architecture._research_expansion_summary(discoveries),
            {
                "max_research_pass": 2,
                "pass_counts": {"0": 1, "1": 2, "2": 1},
                "parent_link_count": 2,
                "obligation_link_count": 3,
                "unique_obligation_count": 2,
                "root_discovery_count": 2,
                "expanded_discovery_count": 3,
            },
        )

    def test_review_summary_exposes_research_expansion(self) -> None:
        helper = architecture_tests.SurveyArchitectureV2Tests(
            methodName="test_weekly_and_thematic_share_core_without_dummy_profile_fields"
        )
        chain = helper.chain("THEMATIC")
        self.addCleanup(helper.doCleanups)
        selection = helper.selection_for(chain)
        selection_path = chain["root"] / "selection-expansion.json"
        core.write_json(selection_path, selection)
        plan = helper.architecture_for(chain, selection_path, research_profile="THEMATIC")
        plan_path = chain["root"] / "architecture-expansion.json"
        core.write_json(plan_path, plan)
        summary = architecture.build_architecture_review_summary(
            chain["root"],
            chain["profile_path"],
            chain["discovery_path"],
            chain["screening"],
            chain["evidence"],
            chain["views"],
            chain["ledger_path"],
            chain["completeness_path"],
            chain["matrix_path"],
            selection_path,
            plan_path,
            IMPLEMENTATION_SHA,
        )
        self.assertEqual(summary["research_expansion"]["max_research_pass"], 0)
        self.assertEqual(summary["research_expansion"]["root_discovery_count"], 1)
        self.assertIn("research_expansion", summary)


if __name__ == "__main__":
    unittest.main()
