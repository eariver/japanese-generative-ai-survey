from __future__ import annotations

import unittest

from scripts import survey_reader_fidelity_v2 as fidelity


class SurveyReaderFidelityV2Tests(unittest.TestCase):
    @staticmethod
    def _architecture(requirements: list[str] | None = None, target_pages: int = 18) -> dict[str, object]:
        return {
            "page_plan": {"target_pages": target_pages, "max_pages": 24},
            "packages": [
                {
                    "package_id": "PKG-1",
                    "title": "Approved final synthesis package",
                    "must_cover_requirements": requirements or ["R1", "R2"],
                }
            ],
        }

    @staticmethod
    def _body(seed: str) -> str:
        return (seed + "は一次資料に基づいて技術的転換、実装上の意味、残る境界を読者向けに説明する。") * 45

    def _source(self, title: str = "総括：Frontier構造") -> str:
        return (
            f"\\section{{{title}}}\n"
            "\\subsection{技術的転換}\n"
            + self._body("転換A")
            + "\\autocite{sourceA}\n"
            "\\subsection{残る境界}\n"
            + self._body("境界B")
            + "\\autocite{sourceB}\n"
        )

    @staticmethod
    def _coverage(title: str = "総括：Frontier構造") -> list[dict[str, object]]:
        return [
            {
                "package_id": "PKG-1",
                "requirement": "R1",
                "status": "FULFILLED",
                "reader_locations": ["Subsection 1.1 — 技術的転換"],
            },
            {
                "package_id": "PKG-1",
                "requirement": "R2",
                "status": "FULFILLED",
                "reader_locations": ["Subsection 1.2 — 残る境界"],
            },
        ]

    @staticmethod
    def _reader_requirements(title: str = "総括：Frontier構造") -> list[dict[str, object]]:
        return [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": [f"Section 1 — {title}"],
            }
        ]

    def test_longform_accepts_distinct_substantive_source_backed_blocks(self) -> None:
        result = fidelity.validate_reader_fidelity(
            self._source(),
            self._architecture(),
            self._coverage(),
            self._reader_requirements(),
            "LONGFORM_SPECIAL",
        )
        self.assertEqual(result["status"], "PASS")
        self.assertGreaterEqual(result["package_metrics"][0]["mapped_block_count"], 2)
        self.assertGreaterEqual(result["package_metrics"][0]["citation_key_count"], 2)

    def test_single_requirement_may_use_one_authoritative_source(self) -> None:
        source = (
            "\\section{Final synthesis}\n"
            "\\subsection{Single authoritative transition}\n"
            + self._body("単一の一次資料で確認できる転換")
            + "\\autocite{authoritativeSource}\n"
        )
        result = fidelity.validate_reader_fidelity(
            source,
            self._architecture(["R1"]),
            [
                {
                    "package_id": "PKG-1",
                    "requirement": "R1",
                    "status": "FULFILLED",
                    "reader_locations": ["Subsection 1.1 — Single authoritative transition"],
                }
            ],
            self._reader_requirements("Final synthesis"),
            "LONGFORM_SPECIAL",
        )
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["package_metrics"][0]["mapped_block_count"], 1)
        self.assertEqual(result["package_metrics"][0]["citation_key_count"], 1)

    def test_longform_rejects_topic_presence_collapsed_into_one_section(self) -> None:
        architecture = self._architecture(["R1", "R2", "R3"])
        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": requirement,
                "status": "FULFILLED",
                "reader_locations": ["Section 1 — 総括：Frontier構造"],
            }
            for requirement in ["R1", "R2", "R3"]
        ]
        with self.assertRaisesRegex(ValueError, "at most two Architecture requirements"):
            fidelity.validate_reader_fidelity(
                self._source(),
                architecture,
                coverage,
                self._reader_requirements(),
                "LONGFORM_SPECIAL",
            )

    def test_longform_rejects_thin_reader_block_even_when_requirement_is_named(self) -> None:
        source = (
            "\\section{総括：Frontier構造}\n"
            "\\subsection{技術的転換}\n短い説明。\\autocite{sourceA}\n"
            "\\subsection{残る境界}\n"
            + self._body("境界B")
            + "\\autocite{sourceB}\n"
        )
        with self.assertRaisesRegex(ValueError, "too thin for substantive Architecture coverage"):
            fidelity.validate_reader_fidelity(
                source,
                self._architecture(),
                self._coverage(),
                self._reader_requirements(),
                "LONGFORM_SPECIAL",
            )

    def test_final_architecture_package_keeps_reader_visible_synthesis_role(self) -> None:
        title = "2026年のFrontier構造"
        with self.assertRaisesRegex(ValueError, "reader-visible as a synthesis/conclusion role"):
            fidelity.validate_reader_fidelity(
                self._source(title),
                self._architecture(),
                self._coverage(title),
                self._reader_requirements(title),
                "LONGFORM_SPECIAL",
            )

    def test_severely_below_target_review_requires_exact_density_observation(self) -> None:
        profile = {"publication_profile": "LONGFORM_SPECIAL"}
        architecture = self._architecture(target_pages=18)
        checks = [
            {
                "check_id": "ARCHITECTURE_CONTENT_FIDELITY",
                "status": "PASS",
                "detail": "Package treatment was reviewed.",
                "evidence_locations": ["package:PKG-1"],
            },
            {
                "check_id": "FINAL_SYNTHESIS_QUALITY",
                "status": "PASS",
                "detail": "Final synthesis role was reviewed.",
                "evidence_locations": ["package:PKG-1", "reader-role:final-synthesis"],
            },
            {
                "check_id": "LONGFORM_TECHNICAL_DEPTH",
                "status": "PASS",
                "detail": "各packageの技術的転換と一次資料の結び付きを個別に確認し、ページ数の少なさが単なるtopic presenceへの圧縮ではないかを検証した。" * 3,
                "evidence_locations": ["package:PKG-1"],
            },
        ]
        with self.assertRaisesRegex(ValueError, "page-plan:7/18"):
            fidelity.validate_review_depth(profile, architecture, 7, checks, "SEMANTIC_EDITORIAL")

        checks[-1]["evidence_locations"].append("page-plan:7/18")
        fidelity.validate_review_depth(profile, architecture, 7, checks, "SEMANTIC_EDITORIAL")

    def test_weekly_profile_is_not_subject_to_longform_block_accounting(self) -> None:
        result = fidelity.validate_reader_fidelity(
            "weekly reader source",
            {"packages": []},
            [],
            [],
            "WEEKLY_MAGAZINE",
        )
        self.assertEqual(result["status"], "NOT_APPLICABLE")


if __name__ == "__main__":
    unittest.main()
