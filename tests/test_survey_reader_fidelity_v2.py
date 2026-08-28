from __future__ import annotations

import unittest

from scripts import survey_reader_fidelity_v2 as fidelity


class SurveyReaderFidelityV2Tests(unittest.TestCase):
    @staticmethod
    def _architecture(target_pages: int | float = 18, *, array_order_reversed: bool = False) -> dict[str, object]:
        packages = [
            {
                "package_id": "PKG-1",
                "title": "Family trajectory",
                "must_cover_requirements": ["R1", "R2"],
                "drafting_order": 1,
            },
            {
                "package_id": "PKG-2",
                "title": "Cross-family synthesis",
                "must_cover_requirements": [],
                "drafting_order": 2,
            },
        ]
        if array_order_reversed:
            packages.reverse()
        return {
            "page_plan": {"target_pages": target_pages, "max_pages": 24},
            "packages": packages,
        }

    @staticmethod
    def _source() -> str:
        return (
            "\\section{Family trajectory}\n"
            "\\subsection{Transition}\n"
            "A concrete reader-facing transition is explained here.\\autocite{sourceA}\n"
            "\\subsection{Boundary}\n"
            "A distinct reader-facing limitation is explained here.\\autocite{sourceB}\n"
            "\\section{What converged and what remained different}\n"
            "The closing section synthesizes the two technical paths without a ranking.\\autocite{sourceA,sourceB}\n"
        )

    @staticmethod
    def _coverage(shared: bool = False) -> list[dict[str, object]]:
        second = "Subsection 1.1 — Transition" if shared else "Subsection 1.2 — Boundary"
        return [
            {
                "package_id": "PKG-1",
                "requirement": "R1",
                "status": "FULFILLED",
                "reader_locations": ["Subsection 1.1 — Transition"],
            },
            {
                "package_id": "PKG-1",
                "requirement": "R2",
                "status": "FULFILLED",
                "reader_locations": [second],
            },
        ]

    @staticmethod
    def _reader_requirements() -> list[dict[str, object]]:
        return [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["Section 2 — What converged and what remained different"],
            }
        ]

    @staticmethod
    def _manuscript(shared: bool = False) -> dict[str, object]:
        return {
            "architecture_coverage": SurveyReaderFidelityV2Tests._coverage(shared),
            "reader_requirements": SurveyReaderFidelityV2Tests._reader_requirements(),
        }

    @staticmethod
    def _semantic_checks(shared: bool = False) -> list[dict[str, object]]:
        coverage_locations = {"Subsection 1.1 — Transition"}
        if not shared:
            coverage_locations.add("Subsection 1.2 — Boundary")
        packages = {"package:PKG-1", "package:PKG-2"}
        return [
            {
                "check_id": "ARCHITECTURE_CONTENT_FIDELITY",
                "status": "PASS",
                "detail": "The exact reader blocks were semantically reviewed against both approved packages.",
                "evidence_locations": sorted(packages | coverage_locations),
            },
            {
                "check_id": "FINAL_SYNTHESIS_QUALITY",
                "status": "PASS",
                "detail": "The closing section performs a reader-visible synthesis rather than restating internal Architecture.",
                "evidence_locations": [
                    "package:PKG-2",
                    "reader-role:final-synthesis",
                    "Section 2 — What converged and what remained different",
                ],
            },
            {
                "check_id": "LONGFORM_TECHNICAL_DEPTH",
                "status": "PASS",
                "detail": "Technical depth was reviewed package by package and at each exact coverage block.",
                "evidence_locations": sorted(packages | coverage_locations),
            },
        ]

    def test_longform_traceability_resolves_exact_reader_blocks(self) -> None:
        result = fidelity.validate_reader_fidelity(
            self._source(),
            self._architecture(),
            self._coverage(),
            self._reader_requirements(),
            "LONGFORM_SPECIAL",
        )
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(
            result["coverage_locations"],
            ["Subsection 1.1 — Transition", "Subsection 1.2 — Boundary"],
        )
        self.assertEqual(
            result["final_synthesis_locations"],
            ["Section 2 — What converged and what remained different"],
        )

    def test_deterministic_traceability_does_not_impose_one_package_one_section_or_block_quota(self) -> None:
        result = fidelity.validate_reader_fidelity(
            self._source(),
            self._architecture(),
            self._coverage(shared=True),
            self._reader_requirements(),
            "LONGFORM_SPECIAL",
        )
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["package_locations"]["PKG-1"], ["Subsection 1.1 — Transition"])
        self.assertEqual(result["package_locations"]["PKG-2"], [])

    def test_longform_rejects_abstract_or_nonexistent_location(self) -> None:
        bad = self._coverage()
        bad[0]["reader_locations"] = ["main.tex :: Sections 1-2"]
        with self.assertRaisesRegex(ValueError, "exact TeX content block"):
            fidelity.validate_reader_fidelity(
                self._source(),
                self._architecture(),
                bad,
                self._reader_requirements(),
                "LONGFORM_SPECIAL",
            )

        bad = self._coverage()
        bad[0]["reader_locations"] = ["Subsection 1.1 — Wrong title"]
        with self.assertRaisesRegex(ValueError, "title does not match"):
            fidelity.validate_reader_fidelity(
                self._source(),
                self._architecture(),
                bad,
                self._reader_requirements(),
                "LONGFORM_SPECIAL",
            )

    def test_longform_rejects_empty_exact_block(self) -> None:
        source = (
            "\\section{Family trajectory}\n"
            "\\subsection{Transition}\n"
            "\\subsection{Boundary}\nSome content.\n"
            "\\section{What converged and what remained different}\nClosing content.\n"
        )
        with self.assertRaisesRegex(ValueError, "empty TeX content block"):
            fidelity.validate_reader_fidelity(
                source,
                self._architecture(),
                self._coverage(),
                self._reader_requirements(),
                "LONGFORM_SPECIAL",
            )

    def test_semantic_review_requires_package_and_exact_block_evidence(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = self._semantic_checks()
        fidelity.validate_review_depth(
            profile,
            self._architecture(target_pages=7),
            self._manuscript(),
            7,
            checks,
            "SEMANTIC_EDITORIAL",
        )

        checks = self._semantic_checks()
        architecture_row = next(row for row in checks if row["check_id"] == "ARCHITECTURE_CONTENT_FIDELITY")
        architecture_row["evidence_locations"].remove("Subsection 1.2 — Boundary")
        with self.assertRaisesRegex(ValueError, "ARCHITECTURE_CONTENT_FIDELITY"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=7),
                self._manuscript(),
                7,
                checks,
                "SEMANTIC_EDITORIAL",
            )

    def test_below_target_longform_requires_explicit_density_disposition(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = self._semantic_checks()
        with self.assertRaisesRegex(ValueError, "page-plan:7/18"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=18),
                self._manuscript(),
                7,
                checks,
                "SEMANTIC_EDITORIAL",
            )

        depth = next(row for row in checks if row["check_id"] == "LONGFORM_TECHNICAL_DEPTH")
        depth["evidence_locations"].extend(
            ["page-plan:7/18", "density-review:below-target-substantive"]
        )
        fidelity.validate_review_depth(
            profile,
            self._architecture(target_pages=18),
            self._manuscript(),
            7,
            checks,
            "SEMANTIC_EDITORIAL",
        )

    def test_float_target_pages_still_requires_below_target_density_review(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = self._semantic_checks()
        with self.assertRaisesRegex(ValueError, "page-plan:7/18"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=18.0),
                self._manuscript(),
                7,
                checks,
                "SEMANTIC_EDITORIAL",
            )

        depth = next(row for row in checks if row["check_id"] == "LONGFORM_TECHNICAL_DEPTH")
        depth["evidence_locations"].extend(
            ["page-plan:7/18", "density-review:below-target-substantive"]
        )
        fidelity.validate_review_depth(
            profile,
            self._architecture(target_pages=18.0),
            self._manuscript(),
            7,
            checks,
            "SEMANTIC_EDITORIAL",
        )

    def test_final_synthesis_review_requires_exact_location_and_reader_role(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = self._semantic_checks()
        final = next(row for row in checks if row["check_id"] == "FINAL_SYNTHESIS_QUALITY")
        final["evidence_locations"].remove("reader-role:final-synthesis")
        with self.assertRaisesRegex(ValueError, "FINAL_SYNTHESIS_QUALITY"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=7),
                self._manuscript(),
                7,
                checks,
                "SEMANTIC_EDITORIAL",
            )

    def test_final_synthesis_package_uses_drafting_order_not_array_position(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = self._semantic_checks()
        fidelity.validate_review_depth(
            profile,
            self._architecture(target_pages=7, array_order_reversed=True),
            self._manuscript(),
            7,
            checks,
            "SEMANTIC_EDITORIAL",
        )

        final = next(row for row in checks if row["check_id"] == "FINAL_SYNTHESIS_QUALITY")
        final["evidence_locations"].remove("package:PKG-2")
        final["evidence_locations"].append("package:PKG-1")
        with self.assertRaisesRegex(ValueError, "package:PKG-2"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=7, array_order_reversed=True),
                self._manuscript(),
                7,
                checks,
                "SEMANTIC_EDITORIAL",
            )

    def test_longform_visual_review_requires_explicit_mixed_layout_evidence(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        checks = [
            {
                "check_id": "LONGFORM_MIXED_LAYOUT",
                "status": "PASS",
                "detail": "The exact PDF was reviewed against the Special mixed-layout policy.",
                "evidence_locations": [
                    "reader-layout:balanced-two-column-narrative",
                    "reader-layout:wide-surfaces-full-width",
                    "reader-layout:references-one-column",
                ],
            }
        ]
        fidelity.validate_review_depth(
            profile,
            self._architecture(target_pages=18),
            self._manuscript(),
            13,
            checks,
            "VISUAL",
        )

        checks[0]["evidence_locations"].remove("reader-layout:balanced-two-column-narrative")
        with self.assertRaisesRegex(ValueError, "balanced-two-column-narrative"):
            fidelity.validate_review_depth(
                profile,
                self._architecture(target_pages=18),
                self._manuscript(),
                13,
                checks,
                "VISUAL",
            )

    def test_weekly_profile_is_not_subject_to_longform_traceability(self) -> None:
        result = fidelity.validate_reader_fidelity(
            "weekly reader source",
            {"packages": []},
            [],
            [],
            "WEEKLY_MAGAZINE",
        )
        self.assertEqual(result["status"], "NOT_APPLICABLE")
        fidelity.validate_review_depth(
            {"publication_profile": "WEEKLY_MAGAZINE"},
            {"packages": []},
            {},
            6,
            [],
            "SEMANTIC_EDITORIAL",
        )


if __name__ == "__main__":
    unittest.main()
