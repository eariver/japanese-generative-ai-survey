#!/usr/bin/env python3
from __future__ import annotations

import unittest

from scripts import run_drafting_synthesis_v2_interactive as interactive


def _card(task_id: str, statement_id: str, subject_id: str) -> dict:
    return {
        "evidence_task_id": task_id,
        "claims": [
            {
                "statement_id": statement_id,
                "subject_id": subject_id,
                "subject_role": "PRIMARY_SUBJECT",
                "evidence_class": "AUTHOR_CLAIM",
            }
        ],
        "temporal": {"events": []},
        "limitations": [],
    }


def _input(candidate_id: str, task_id: str, statement_id: str, subject_id: str) -> dict:
    return {
        "candidate_id": candidate_id,
        "evidence_task_id": task_id,
        "evidence_card": _card(task_id, statement_id, subject_id),
    }


class InteractiveDraftingCrossPackageRefsTests(unittest.TestCase):
    def test_ordinary_package_resolves_from_its_evidence_inputs(self) -> None:
        package = {
            "package_id": "PKG-ORDINARY",
            "package": {
                "primary_candidate_ids": ["candidate:a"],
                "supporting_candidate_ids": [],
            },
            "candidate_matrix": {
                "rows": [
                    {"candidate_id": "candidate:a", "discovery_ids": ["D001"]},
                ]
            },
            "evidence_inputs": [
                _input("candidate:a", "task:a", "claim:a", "model-a"),
            ],
        }

        refs = interactive._refs(package, ["D001"], "CLAIMS")

        self.assertEqual(
            refs,
            [
                {
                    "evidence_task_id": "task:a",
                    "kind": "CLAIM",
                    "evidence_id": "claim:a",
                    "subject_id": "model-a",
                    "subject_role": "PRIMARY_SUBJECT",
                }
            ],
        )

    def test_final_cross_package_synthesis_resolves_supporting_evidence_inputs(self) -> None:
        package = {
            "package_id": "PKG-FINAL-SYNTHESIS",
            "package": {
                "primary_candidate_ids": [],
                "supporting_candidate_ids": [],
            },
            "candidate_matrix": {
                "rows": [
                    {"candidate_id": "candidate:a", "discovery_ids": ["D001"]},
                    {"candidate_id": "candidate:b", "discovery_ids": ["D002"]},
                ]
            },
            "evidence_inputs": [
                _input("candidate:a", "task:a", "claim:a", "model-a"),
                _input("candidate:b", "task:b", "claim:b", "model-b"),
            ],
        }

        refs = interactive._refs(package, ["D002"], "CLAIMS")

        self.assertEqual(refs[0]["evidence_task_id"], "task:b")
        self.assertEqual(refs[0]["evidence_id"], "claim:b")
        self.assertEqual(refs[0]["subject_id"], "model-b")

    def test_matrix_candidate_without_evidence_input_is_not_authorized(self) -> None:
        package = {
            "package_id": "PKG-FINAL-SYNTHESIS",
            "package": {
                "primary_candidate_ids": [],
                "supporting_candidate_ids": [],
            },
            "candidate_matrix": {
                "rows": [
                    {"candidate_id": "candidate:a", "discovery_ids": ["D001"]},
                    {"candidate_id": "candidate:unauthorized", "discovery_ids": ["D999"]},
                ]
            },
            "evidence_inputs": [
                _input("candidate:a", "task:a", "claim:a", "model-a"),
            ],
        }

        with self.assertRaisesRegex(ValueError, "Discovery ID must resolve exactly once"):
            interactive._refs(package, ["D999"], "CLAIMS")

    def test_duplicate_discovery_resolution_fails_closed(self) -> None:
        package = {
            "package_id": "PKG-FINAL-SYNTHESIS",
            "package": {
                "primary_candidate_ids": [],
                "supporting_candidate_ids": [],
            },
            "candidate_matrix": {
                "rows": [
                    {"candidate_id": "candidate:a", "discovery_ids": ["D001"]},
                    {"candidate_id": "candidate:b", "discovery_ids": ["D001"]},
                ]
            },
            "evidence_inputs": [
                _input("candidate:a", "task:a", "claim:a", "model-a"),
                _input("candidate:b", "task:b", "claim:b", "model-b"),
            ],
        }

        with self.assertRaisesRegex(ValueError, "Discovery ID must resolve exactly once"):
            interactive._refs(package, ["D001"], "CLAIMS")

    def test_duplicate_evidence_input_candidate_fails_closed(self) -> None:
        package = {
            "package_id": "PKG-FINAL-SYNTHESIS",
            "package": {
                "primary_candidate_ids": [],
                "supporting_candidate_ids": [],
            },
            "candidate_matrix": {
                "rows": [
                    {"candidate_id": "candidate:a", "discovery_ids": ["D001"]},
                ]
            },
            "evidence_inputs": [
                _input("candidate:a", "task:a", "claim:a", "model-a"),
                _input("candidate:a", "task:b", "claim:b", "model-b"),
            ],
        }

        with self.assertRaisesRegex(ValueError, "duplicate candidate_id"):
            interactive._refs(package, ["D001"], "CLAIMS")


if __name__ == "__main__":
    unittest.main()
