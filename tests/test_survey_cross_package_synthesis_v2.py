#!/usr/bin/env python3
"""Regression coverage for bounded cross-package synthesis Draft references."""

from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_drafting_v2 as drafting


class CrossPackageSynthesisReferenceTests(unittest.TestCase):
    @staticmethod
    def package(
        package_id: str,
        order: int,
        *,
        primary: list[str] | None = None,
        supporting: list[str] | None = None,
    ) -> dict:
        return {
            "package_id": package_id,
            "drafting_order": order,
            "primary_candidate_ids": list(primary or []),
            "supporting_candidate_ids": list(supporting or []),
        }

    @staticmethod
    def derive_args(package_id: str) -> tuple:
        return (
            Path("."),
            Path("profile.json"),
            Path("discovery.json"),
            Path("screening.json"),
            Path("evidence/acceptance.json"),
            Path("views.json"),
            Path("ledger.json"),
            Path("completeness.json"),
            Path("matrix.json"),
            Path("selection.json"),
            Path("architecture.json"),
            Path("review-summary.json"),
            Path("approval.json"),
            package_id,
            "implementation-sha",
        )

    def test_final_empty_package_references_all_existing_placements_once(self) -> None:
        conclusion = self.package("PKG-3-SYNTHESIS", 3)
        plan = {
            "packages": [
                self.package("PKG-1", 1, primary=["c1"], supporting=["c2"]),
                self.package("PKG-2", 2, primary=["c3"], supporting=["c2", "c4"]),
                conclusion,
            ]
        }
        self.assertEqual(
            drafting._cross_package_reference_ids(plan, conclusion),
            ["c1", "c2", "c3", "c4"],
        )

    def test_direct_evidence_package_is_not_reclassified(self) -> None:
        direct = self.package("PKG-1", 1, primary=["c1"])
        self.assertEqual(
            drafting._cross_package_reference_ids({"packages": [direct]}, direct),
            [],
        )

    def test_direct_package_delegates_to_frozen_implementation(self) -> None:
        direct = self.package("PKG-1", 1, primary=["c1"])
        sentinel = {"delegated": True}
        with (
            patch.object(drafting.core, "load_json", return_value={"packages": [direct]}),
            patch.object(
                drafting,
                "_ORIGINAL_DERIVE_DRAFT_PACKAGE",
                return_value=sentinel,
            ) as original,
        ):
            result = drafting.derive_draft_package(*self.derive_args("PKG-1"))
        self.assertIs(result, sentinel)
        original.assert_called_once_with(*self.derive_args("PKG-1"))

    def test_empty_package_materializes_supporting_cross_package_inputs(self) -> None:
        source = self.package("PKG-1", 1, primary=["c1"], supporting=["c2"])
        conclusion = self.package("PKG-2-SYNTHESIS", 2)
        conclusion.update(
            {
                "title": "Synthesis",
                "purpose": "Synthesize prior Evidence.",
                "must_cover_requirements": ["Compare established differences."],
                "boundaries": ["Do not create a new benchmark ranking."],
                "profile_extensions": {},
                "publication_extensions": {},
            }
        )
        source.update(
            {
                "title": "Source",
                "purpose": "Source article.",
                "must_cover_requirements": [],
                "boundaries": [],
                "profile_extensions": {},
                "publication_extensions": {},
            }
        )
        plan = {"packages": [source, conclusion]}
        evidence_sha = "a" * 64
        cards = {
            "t1": {"issue_id": "ISSUE", "evidence_task_id": "t1"},
            "t2": {"issue_id": "ISSUE", "evidence_task_id": "t2"},
        }
        matrix = {
            "rows": [
                {"candidate_id": "c1", "evidence_task_id": "t1", "evidence_sha256": evidence_sha},
                {"candidate_id": "c2", "evidence_task_id": "t2", "evidence_sha256": evidence_sha},
            ]
        }
        acceptance = {
            "results": [
                {"evidence_task_id": "t1", "sha256": evidence_sha, "filename": "t1.json"},
                {"evidence_task_id": "t2", "sha256": evidence_sha, "filename": "t2.json"},
            ]
        }
        upstream = {
            "profile": {
                "issue_id": "ISSUE",
                "research_profile": "THEMATIC",
                "publication_profile": "LONGFORM_SPECIAL",
            },
            "matrix": matrix,
            "architecture": plan,
            "evidence": acceptance,
        }
        architecture_path = self.derive_args("PKG-2-SYNTHESIS")[10]

        def fake_load_json(path: Path) -> dict:
            if path == architecture_path:
                return plan
            return cards[path.stem]

        with (
            patch.object(drafting.core, "load_json", side_effect=fake_load_json),
            patch.object(drafting._base, "_load_drafting_basis", return_value=upstream),
            patch.object(drafting.core, "sha256_file", return_value=evidence_sha),
        ):
            package = drafting.derive_draft_package(
                *self.derive_args("PKG-2-SYNTHESIS")
            )

        self.assertEqual(
            [item["candidate_id"] for item in package["evidence_inputs"]],
            ["c1", "c2"],
        )
        self.assertEqual(
            {item["architecture_usage"] for item in package["evidence_inputs"]},
            {"SUPPORTING"},
        )
        self.assertEqual(package["package"]["primary_candidate_ids"], [])
        self.assertEqual(package["package"]["supporting_candidate_ids"], [])

    def test_empty_package_must_be_unique(self) -> None:
        first = self.package("PKG-2-A", 2)
        second = self.package("PKG-3-B", 3)
        plan = {
            "packages": [
                self.package("PKG-1", 1, primary=["c1"]),
                first,
                second,
            ]
        }
        with self.assertRaisesRegex(ValueError, "exactly one empty-placement"):
            drafting._cross_package_reference_ids(plan, second)

    def test_empty_package_must_be_last(self) -> None:
        synthesis = self.package("PKG-1-SYNTHESIS", 1)
        plan = {
            "packages": [
                synthesis,
                self.package("PKG-2", 2, primary=["c1"]),
            ]
        }
        with self.assertRaisesRegex(ValueError, "must be last"):
            drafting._cross_package_reference_ids(plan, synthesis)

    def test_synthesis_requires_prior_factual_placements(self) -> None:
        synthesis = self.package("PKG-1-SYNTHESIS", 1)
        with self.assertRaisesRegex(ValueError, "no authorized Evidence references"):
            drafting._cross_package_reference_ids({"packages": [synthesis]}, synthesis)


if __name__ == "__main__":
    unittest.main()
