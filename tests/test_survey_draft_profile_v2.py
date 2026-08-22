from __future__ import annotations

import copy
import unittest

from scripts import survey_draft_profile_v2 as profile_draft
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from tests import test_survey_drafting_v2 as drafting_tests


class SurveyDraftProfileV2Tests(unittest.TestCase):
    def helper(self) -> drafting_tests.SurveyDraftingV2Tests:
        case = drafting_tests.SurveyDraftingV2Tests(
            methodName="test_weekly_and_thematic_share_generic_draft_contract_without_dummy_fields"
        )
        self.addCleanup(case.doCleanups)
        return case

    def test_profile_and_publication_extensions_must_survive_exactly(self) -> None:
        for research_profile in ("WEEKLY", "THEMATIC"):
            with self.subTest(research_profile=research_profile):
                helper = self.helper()
                chain = helper.build_authorized_chain(research_profile)
                package = helper.derive_package(chain)
                package_path = chain["root"] / f"profile-package-{research_profile}.json"
                core.write_json(package_path, package)
                result = helper.valid_result(
                    package, package_path, chain["root"] / drafting.DRAFT_PROMPT
                )
                result["profile_extensions"] = copy.deepcopy(package["profile_extensions"])
                result["publication_extensions"] = copy.deepcopy(
                    package["publication_extensions"]
                )
                self.assertEqual(
                    profile_draft.validate_extension_propagation(result, package), []
                )

                dropped = copy.deepcopy(result)
                dropped["profile_extensions"] = {}
                errors = profile_draft.validate_extension_propagation(dropped, package)
                self.assertTrue(
                    any("Research Profile" in error for error in errors), errors
                )

                invented = copy.deepcopy(result)
                invented["profile_extensions"]["cross_profile_dummy"] = "forbidden"
                errors = profile_draft.validate_extension_propagation(invented, package)
                self.assertTrue(
                    any("Research Profile" in error for error in errors), errors
                )

    def test_generic_core_does_not_interpret_profile_extension_vocabulary(self) -> None:
        helper = self.helper()
        weekly = helper.build_authorized_chain("WEEKLY")
        thematic = helper.build_authorized_chain("THEMATIC")
        weekly_package = helper.derive_package(weekly)
        thematic_package = helper.derive_package(thematic)
        self.assertIn("weekly_package_role", weekly_package["profile_extensions"])
        self.assertNotIn("weekly_package_role", thematic_package["profile_extensions"])
        self.assertIn("lineage_package_role", thematic_package["profile_extensions"])
        self.assertNotIn("lineage_package_role", weekly_package["profile_extensions"])


if __name__ == "__main__":
    unittest.main()
