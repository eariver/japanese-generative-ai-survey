from __future__ import annotations

import unittest

from scripts import apply_special_selection_and_propose_architecture as special_gate


class SpecialSelectionArchitectureTests(unittest.TestCase):
    def test_union_boundaries_is_stable_and_deduplicated(self) -> None:
        architecture_input = {
            "selected_by_role": {
                "SECTION_CORE": [
                    {"evidence_task_id": "a", "remaining_boundaries": ["alpha", "shared"]},
                    {"evidence_task_id": "b", "remaining_boundaries": ["shared", "beta"]},
                ]
            }
        }
        self.assertEqual(special_gate.union_boundaries(architecture_input, ["a", "b"]), ["alpha", "shared", "beta"])

    def test_union_boundaries_rejects_unselected_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-selected Evidence Task"):
            special_gate.union_boundaries({"selected_by_role": {}}, ["missing"])


if __name__ == "__main__":
    unittest.main()
