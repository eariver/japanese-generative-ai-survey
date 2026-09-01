from __future__ import annotations

import unittest

from scripts.revise_special_prebuild_visual_review_repairs import validate_prebuild_boundary


class SpecialPrebuildVisualReviewRepairTests(unittest.TestCase):
    def test_validated_draft_after_quality_gate_failure_is_allowed(self) -> None:
        validate_prebuild_boundary({
            "lifecycle_state": "VALIDATED_DRAFT",
            "gates": {
                "claim_and_chronology_validation": "passed",
                "latex_build": "pending",
                "visual_review": "pending",
                "freeze": "pending",
            },
        })

    def test_successful_release_candidate_is_not_prebuild_boundary(self) -> None:
        with self.assertRaises(ValueError):
            validate_prebuild_boundary({
                "lifecycle_state": "RELEASE_CANDIDATE",
                "gates": {
                    "claim_and_chronology_validation": "passed",
                    "latex_build": "passed",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
            })

    def test_unvalidated_or_frozen_state_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_prebuild_boundary({
                "lifecycle_state": "VALIDATED_DRAFT",
                "gates": {
                    "claim_and_chronology_validation": "pending",
                    "latex_build": "pending",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
            })
        with self.assertRaises(ValueError):
            validate_prebuild_boundary({
                "lifecycle_state": "VALIDATED_DRAFT",
                "gates": {
                    "claim_and_chronology_validation": "passed",
                    "latex_build": "pending",
                    "visual_review": "pending",
                    "freeze": "passed",
                },
            })


if __name__ == "__main__":
    unittest.main()
