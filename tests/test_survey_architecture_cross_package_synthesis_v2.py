#!/usr/bin/env python3
"""Architecture-layer regressions for bounded cross-package synthesis packages."""

from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_architecture_v2 as architecture
from scripts import survey_drafting_v2 as drafting


class ArchitectureCrossPackageSynthesisContractTests(unittest.TestCase):
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
    def validate(plan: dict) -> list[str]:
        with patch.object(
            architecture,
            "_ORIGINAL_VALIDATE_ARCHITECTURE",
            return_value=[],
        ):
            return architecture.validate_architecture(
                Path("."),
                plan,
                Path("profile.json"),
                Path("completeness.json"),
                Path("ledger.json"),
                Path("matrix.json"),
                Path("selection.json"),
            )

    def test_architecture_accepts_no_empty_package(self) -> None:
        plan = {
            "packages": [
                self.package("PKG-1", 1, primary=["c1"]),
                self.package("PKG-2", 2, supporting=["c2"]),
            ]
        }
        self.assertEqual(self.validate(plan), [])

    def test_architecture_accepts_exactly_one_final_empty_synthesis_package(self) -> None:
        synthesis = self.package("PKG-3-SYNTHESIS", 3)
        plan = {
            "packages": [
                self.package("PKG-1", 1, primary=["c1"], supporting=["c2"]),
                self.package("PKG-2", 2, primary=["c3"]),
                synthesis,
            ]
        }
        self.assertEqual(self.validate(plan), [])
        self.assertEqual(
            drafting._cross_package_reference_ids(plan, synthesis),
            ["c1", "c2", "c3"],
        )

    def test_architecture_rejects_non_final_empty_package_before_human_gate(self) -> None:
        plan = {
            "packages": [
                self.package("PKG-1-SYNTHESIS", 1),
                self.package("PKG-2", 2, primary=["c1"]),
            ]
        }
        errors = self.validate(plan)
        self.assertTrue(any("must be last in drafting order" in error for error in errors), errors)

    def test_architecture_rejects_multiple_empty_packages_before_human_gate(self) -> None:
        plan = {
            "packages": [
                self.package("PKG-1", 1, primary=["c1"]),
                self.package("PKG-2-A", 2),
                self.package("PKG-3-B", 3),
            ]
        }
        errors = self.validate(plan)
        self.assertTrue(any("at most one empty-placement" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
