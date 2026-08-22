from __future__ import annotations

import unittest

from scripts import run_selection_architecture_v2_interactive as runner


class InteractiveSelectionArchitectureTests(unittest.TestCase):
    def test_matrix_discovery_map_requires_one_discovery_per_candidate(self) -> None:
        with self.assertRaisesRegex(ValueError, "one Discovery per Matrix candidate"):
            runner._matrix_discovery_map({
                "rows": [{"candidate_id": "candidate:x", "discovery_ids": ["D1", "D2"]}]
            })

    def test_input_requires_exact_assignment_coverage(self) -> None:
        doc = {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "runner": {
                "provider": "OpenAI",
                "model": "GPT-5.6 Sol",
                "invocation": "test",
                "generated_at": "2026-08-23T00:00:00Z",
            },
            "assignments": [],
            "architecture": {
                "editorial_thesis": "thesis",
                "architecture_goals": ["goal"],
                "page_plan": {"target_pages": 10, "max_pages": 12, "notes": None},
                "packages": [{
                    "package_id": "p1",
                    "title": "title",
                    "purpose": "purpose",
                    "primary_discovery_ids": [],
                    "supporting_discovery_ids": [],
                    "must_cover_requirements": [],
                    "boundaries": [],
                    "drafting_order": 1,
                    "profile_extensions": {},
                    "publication_extensions": {},
                }],
                "selected_exceptions": [],
                "profile_extensions": {},
                "publication_extensions": {},
            },
        }
        with self.assertRaisesRegex(ValueError, "cover every Matrix Discovery exactly once"):
            runner._validate_input(doc, "SP001", {"D1"})


if __name__ == "__main__":
    unittest.main()
