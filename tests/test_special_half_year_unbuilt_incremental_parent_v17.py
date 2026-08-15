from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts import revise_special_half_year_review_repairs_v17 as repair


class HalfYearUnbuiltIncrementalParentV17Tests(unittest.TestCase):
    def _state(self) -> dict:
        return {
            "lifecycle_state": "VALIDATED_DRAFT",
            "gates": {
                "latex_build": "pending",
                "visual_review": "pending",
                "freeze": "pending",
            },
            "provenance": {},
        }

    def test_explicit_opt_in_temporarily_satisfies_legacy_precondition(self) -> None:
        state = self._state()
        marker = {"layout_changes": {"allow_unbuilt_incremental_parent": True}}

        def fake_original(*args, **kwargs):
            passed_state = args[5]
            self.assertEqual(passed_state["lifecycle_state"], "RELEASE_CANDIDATE")
            self.assertEqual(passed_state["gates"]["latex_build"], "passed")
            # Mirror the legacy builder's persisted terminal state.
            passed_state["lifecycle_state"] = "VALIDATED_DRAFT"
            passed_state["gates"]["latex_build"] = "pending"
            return {"lifecycle_state": "VALIDATED_DRAFT", "latex_build_gate": "pending"}

        with patch.object(repair, "_ORIGINAL_INCREMENTAL_BUILD", side_effect=fake_original):
            result = repair._incremental_build_allow_unbuilt(
                None, "2024-H2", "SP-2024-H2", "v0.8", marker, state, {}, {}
            )

        self.assertEqual(state["lifecycle_state"], "VALIDATED_DRAFT")
        self.assertEqual(state["gates"]["latex_build"], "pending")
        self.assertEqual(result["incremental_parent_build_state"], "UNBUILT_VALIDATED_DRAFT")
        self.assertIs(result["unbuilt_parent_opt_in"], True)

    def test_unbuilt_parent_without_opt_in_is_rejected(self) -> None:
        state = self._state()
        marker = {"layout_changes": {}}
        with self.assertRaisesRegex(ValueError, "explicit allow_unbuilt_incremental_parent"):
            repair._incremental_build_allow_unbuilt(
                None, "2024-H2", "SP-2024-H2", "v0.8", marker, state, {}, {}
            )

    def test_unbuilt_parent_with_existing_build_provenance_is_rejected(self) -> None:
        state = self._state()
        state["provenance"]["latex_build"] = {"workflow_run_id": 123}
        marker = {"layout_changes": {"allow_unbuilt_incremental_parent": True}}
        with self.assertRaisesRegex(ValueError, "must not carry current latex_build provenance"):
            repair._incremental_build_allow_unbuilt(
                None, "2024-H2", "SP-2024-H2", "v0.8", marker, state, {}, {}
            )

    def test_built_parent_uses_legacy_path_unchanged(self) -> None:
        state = self._state()
        state["lifecycle_state"] = "RELEASE_CANDIDATE"
        state["gates"]["latex_build"] = "passed"
        marker = {"layout_changes": {}}
        with patch.object(repair, "_ORIGINAL_INCREMENTAL_BUILD", return_value={"ok": True}) as mocked:
            result = repair._incremental_build_allow_unbuilt(
                None, "2024-H2", "SP-2024-H2", "v0.8", marker, state, {}, {}
            )
        self.assertEqual(result, {"ok": True})
        mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
