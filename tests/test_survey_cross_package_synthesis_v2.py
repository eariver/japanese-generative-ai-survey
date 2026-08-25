#!/usr/bin/env python3
"""Regression coverage for bounded cross-package synthesis Draft references."""

from __future__ import annotations

import unittest

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
