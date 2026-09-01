from __future__ import annotations

import copy
import unittest

from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from tests import test_survey_drafting_v2 as drafting_tests


class SurveyDraftingIntegrityV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.helper = drafting_tests.SurveyDraftingV2Tests(
            methodName="test_weekly_and_thematic_share_generic_draft_contract_without_dummy_fields"
        )
        self.addCleanup(self.helper.doCleanups)

    def test_synthesis_rejects_forged_embedded_evidence_even_if_result_rebinds_to_package(self) -> None:
        chain = self.helper.build_authorized_chain("THEMATIC")
        package = self.helper.derive_package(chain)
        package_path = chain["root"] / "draft-package-valid.json"
        core.write_json(package_path, package)
        result = self.helper.valid_result(
            package, package_path, chain["root"] / drafting.DRAFT_PROMPT
        )
        result_path = chain["root"] / "draft-result-valid.json"
        core.write_json(result_path, result)

        baseline = drafting.build_synthesis_input(
            chain["root"],
            chain["profile_path"],
            chain["architecture_path"],
            chain["review_summary_path"],
            chain["approval_path"],
            [(package_path, result_path)],
        )
        self.assertEqual(len(baseline["drafts"]), 1)
        self.assertEqual(
            drafting.validate_self_contained_draft_package(
                package,
                chain["profile_path"],
                chain["architecture_path"],
                chain["review_summary_path"],
                chain["approval_path"],
            ),
            [],
        )

        forged = copy.deepcopy(package)
        forged["evidence_inputs"][0]["evidence_card"]["claims"][0]["text"] = (
            "Forged text not present in accepted Evidence bytes."
        )
        forged_path = chain["root"] / "draft-package-forged.json"
        core.write_json(forged_path, forged)

        rebound_result = copy.deepcopy(result)
        rebound_result["basis"]["draft_package_sha256"] = core.sha256_file(forged_path)
        rebound_result_path = chain["root"] / "draft-result-rebound.json"
        core.write_json(rebound_result_path, rebound_result)

        with self.assertRaisesRegex(
            ValueError, "embedded Evidence Card differs from canonical accepted object"
        ):
            drafting.build_synthesis_input(
                chain["root"],
                chain["profile_path"],
                chain["architecture_path"],
                chain["review_summary_path"],
                chain["approval_path"],
                [(forged_path, rebound_result_path)],
            )


if __name__ == "__main__":
    unittest.main()
