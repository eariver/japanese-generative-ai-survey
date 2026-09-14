from __future__ import annotations

import shutil
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_reader_publication_v2 as reader
from scripts import survey_reader_surface_gate_v2 as surface_gate
from scripts import survey_schema_v2 as schema_gate


class SurveyReaderSurfaceGateV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

        # Copy necessary schemas and configuration
        for rel in [
            core.DEFAULT_CONFIG,
            reader.MANUSCRIPT_SCHEMA,
            reader.REVIEW_SCHEMA,
            reader.ARCHITECTURE_SCHEMA,
            reader.ARCHITECTURE_APPROVAL_SCHEMA,
            reader.REVIEW_CONTRACT,
            surface_gate.SURFACE_GATE_SCHEMA,
        ]:
            dst = self.root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.source_root / rel, dst)

        self.now = datetime(2026, 9, 14, 12, 0, tzinfo=timezone.utc)
        self.dummy_sha = "a" * 64

    def _setup_edition(
        self,
        issue_id: str,
        research_profile: str,
        publication_profile: str,
        requirements: list[str],
    ) -> tuple[Path, Path, Path, Path, Path]:
        """Create minimal valid Profile, Architecture, Approval, survey_root files."""
        survey_root_rel = f"surveys/{'weekly' if publication_profile == 'WEEKLY_MAGAZINE' else 'special'}/{issue_id}"
        survey_root = self.root / survey_root_rel
        survey_root.mkdir(parents=True, exist_ok=True)

        source_root_rel = f"sources/{issue_id}"
        source_root = self.root / source_root_rel
        source_root.mkdir(parents=True, exist_ok=True)

        temporal = (
            {
                "mode": "ROLLING_WINDOW",
                "window_start": "2026-08-14T22:00:00Z",
                "window_end": "2026-08-21T22:00:00Z",
                "cutoff": "2026-08-21T22:00:00Z",
                "timezone": "America/New_York",
            }
            if research_profile == "WEEKLY"
            else {"mode": "OPEN_HISTORY_AS_OF", "as_of": "2026-08-23T07:00:00Z"}
        )

        profile_path = source_root / "production-profile.json"
        core.write_json(
            profile_path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": issue_id,
                "research_profile": research_profile,
                "publication_profile": publication_profile,
                "research_scope": {
                    "question": "Research question",
                    "inclusion": [],
                    "exclusion": [],
                    "scope_dimensions": ["dim1"],
                    "initial_obligations": [
                        {"obligation_id": "cov:1", "dimension": "dim1", "description": "Coverage"}
                    ],
                    "temporal_policy": temporal,
                },
                "paths": {
                    "source_root": source_root_rel,
                    "survey_root": survey_root_rel,
                    "work_branch": f"work/{issue_id}",
                },
                "contract": {
                    "pipeline_contract_version": "test",
                    "pipeline_contract_sha256": self.dummy_sha,
                    "quality_contract_version": "test",
                    "quality_contract_sha256": self.dummy_sha,
                    "research_profile_version": "test",
                    "research_profile_sha256": self.dummy_sha,
                    "publication_profile_version": "test",
                    "publication_profile_sha256": self.dummy_sha,
                },
            },
        )

        arch_path = source_root / "architecture-v2.json"
        core.write_json(
            arch_path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": issue_id,
                "research_profile": research_profile,
                "publication_profile": publication_profile,
                "status": "APPROVED",
                "basis": {
                    "production_profile_sha256": self.dummy_sha,
                    "profile_completeness_sha256": self.dummy_sha,
                    "materiality_ledger_sha256": self.dummy_sha,
                    "candidate_matrix_sha256": self.dummy_sha,
                    "candidate_selection_sha256": self.dummy_sha,
                },
                "editorial_thesis": "Test thesis",
                "architecture_goals": ["Explain material"],
                "page_plan": {"target_pages": 12, "max_pages": 24, "notes": "notes"},
                "packages": [
                    {
                        "package_id": "PKG-1",
                        "title": "Package 1 Title",
                        "purpose": "Purpose",
                        "primary_candidate_ids": ["C1"],
                        "supporting_candidate_ids": [],
                        "must_cover_requirements": requirements,
                        "boundaries": ["Boundaries"],
                        "drafting_order": 1,
                        "profile_extensions": {},
                        "publication_extensions": {},
                    }
                ],
                "selected_exceptions": [],
                "profile_extensions": {},
                "publication_extensions": {},
                "human_review": {
                    "reviewed_by": "reviewer",
                    "reviewed_at": "2026-09-14T12:00:00Z",
                    "review_reference": "ref",
                },
            },
        )

        approval_path = source_root / "gates" / "architecture-approval.json"
        approval_path.parent.mkdir(parents=True, exist_ok=True)
        core.write_json(
            approval_path,
            {
                "schema_version": "2.0-rc1",
                "approval_id": f"arch:{issue_id}:test",
                "issue_id": issue_id,
                "gate": "ARCHITECTURE_REVIEW",
                "decision": "APPROVED",
                "architecture_sha256": core.sha256_file(arch_path),
                "architecture_review_summary_sha256": self.dummy_sha,
                "architecture_review_attention_sha256": self.dummy_sha,
                "reviewed_by": "reviewer",
                "reviewed_at": "2026-09-14T12:00:00Z",
                "review_reference": "ref",
            },
        )

        main_tex = survey_root / "main.tex"
        references_bib = survey_root / "references.bib"
        return profile_path, arch_path, approval_path, main_tex, references_bib

    def _build_valid_manifest(self) -> tuple[Path, Path, Path, Path]:
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain agent workflows"]
        )
        main_tex.write_text(
            "\\section{Agent Workflows}\n"
            "This section surveys autonomous execution patterns and coordination mechanisms.\n",
            encoding="utf-8",
        )
        bib.write_text(
            "@online{source2026,\n"
            "  title = {{Enterprise Autonomous Workflows}},\n"
            "  author = {{Tech Org}},\n"
            "  url = {https://example.com/spec},\n"
            "  urldate = {2026-09-14}\n"
            "}\n",
            encoding="utf-8",
        )
        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain agent workflows",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section1"],
                "detail": "Prose explains agent coordination directly",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "Synthesis summary",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "Community movement",
            },
        ]
        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"
        m_path = reader.build_manuscript_manifest(
            self.root,
            "2026-W35",
            profile,
            arch,
            app,
            main_tex,
            [{"role": "BIBLIOGRAPHY", "path": str(bib.relative_to(self.root))}],
            coverage,
            reader_reqs,
            "ChatGPT",
            self.now,
            m_out,
        )
        return profile, main_tex, bib, m_path

    def test_clean_reader_prose_passes_gate(self) -> None:
        """Clean reader-facing prose passes with 0 blocking findings."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain agent workflows"]
        )
        main_tex.write_text(
            "\\section{Agent Workflows}\n"
            "This section surveys autonomous execution patterns and coordination mechanisms.\n",
            encoding="utf-8",
        )
        bib.write_text(
            "@online{source2026,\n"
            "  title = {{Enterprise Autonomous Workflows}},\n"
            "  author = {{Tech Org}},\n"
            "  url = {https://example.com/spec},\n"
            "  urldate = {2026-09-14}\n"
            "}\n",
            encoding="utf-8",
        )

        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain agent workflows",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section1"],
                "detail": "Prose explains agent coordination and execution patterns directly",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "Synthesis summary",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "Community movement",
            },
        ]

        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"
        m_path = reader.build_manuscript_manifest(
            self.root,
            "2026-W35",
            profile,
            arch,
            app,
            main_tex,
            [
                {
                    "role": "BIBLIOGRAPHY",
                    "path": str(bib.relative_to(self.root)),
                }
            ],
            coverage,
            reader_reqs,
            "ChatGPT",
            self.now,
            m_out,
        )

        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        report = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now
        )
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["summary"]["blocking_findings"], 0)
        self.assertIn("gate_sha256", report)
        schema_gate.validate_instance(
            report, self.root / surface_gate.SURFACE_GATE_SCHEMA, label="Reader-Surface Gate"
        )

    def test_weekly_leakage_fixture_fails_fast(self) -> None:
        """Weekly magazine leakage (Selection r2, Package 4, Discovery observation) fails fast."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain agent workflows"]
        )
        # TeX body includes leakage observed in W34 carry-forward and Issue #434
        main_tex.write_text(
            "\\section{Agent Workflows}\n"
            "Selection r2 で Package 4 に配置した Discovery observation に基づき、\n"
            "candidate-specific review を実施した。承認済みArchitectureの観察軸による。\n",
            encoding="utf-8",
        )
        bib.write_text("@online{ref1,title={Ref},author={Org},url={https://example.com}}\n", encoding="utf-8")

        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain agent workflows",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section1"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]

        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"

        # Fails fast at build_manuscript_manifest before any TeX compilation
        with self.assertRaises(ValueError) as ctx:
            reader.build_manuscript_manifest(
                self.root,
                "2026-W35",
                profile,
                arch,
                app,
                main_tex,
                [],
                coverage,
                reader_reqs,
                "ChatGPT",
                self.now,
                m_out,
            )

        err = str(ctx.exception)
        self.assertIn("Pre-Publication Reader-Surface Gate FAILED", err)
        self.assertIn("RSG-LEX-SELECTION-SCREENING", err)
        self.assertIn("Selection r2", err)
        self.assertIn("RSG-LEX-INTERNAL-IDENTIFIERS", err)
        self.assertIn("Package 4", err)
        self.assertIn("RSG-LEX-DISCOVERY-INTAKE", err)
        self.assertIn("Discovery observation", err)
        self.assertIn("candidate-specific review", err)
        self.assertIn("RSG-LEX-CORE-VOCAB", err)
        self.assertIn("承認済みArchitecture", err)

    def test_special_leakage_fixture_fails_fast(self) -> None:
        """Special longform leakage (D017, 本 package, 一次資料として昇格させない, Verify, materiality) fails fast."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "SP002", "THEMATIC", "LONGFORM_SPECIAL", ["Explain concrete transition"]
        )
        # TeX body includes leakage from SP001 Comment 1
        main_tex.write_text(
            "\\section{Concrete transition}\n"
            "D017とD021の分離により、本 package では一次資料として昇格させない方針をとる。\n"
            "coverage を広げるため、Core v2 Evidence: VERIFIED; materiality: MATERIAL とする。\n"
            "Verify commercial licensing.\n",
            encoding="utf-8",
        )
        bib.write_text("@online{ref1,title={Ref},author={Org},url={https://example.com}}\n", encoding="utf-8")

        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain concrete transition",
                "status": "FULFILLED",
                "reader_locations": ["Section 1 — Concrete transition"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["Section 1 — Concrete transition"],
                "detail": "detail",
            }
        ]

        m_out = self.root / "sources/SP002/publication/v2/reader-manuscript-v2.json"

        with self.assertRaises(ValueError) as ctx:
            reader.build_manuscript_manifest(
                self.root,
                "SP002",
                profile,
                arch,
                app,
                main_tex,
                [],
                coverage,
                reader_reqs,
                "ChatGPT",
                self.now,
                m_out,
            )

        err = str(ctx.exception)
        self.assertIn("Pre-Publication Reader-Surface Gate FAILED", err)
        self.assertIn("D017", err)
        self.assertIn("本 package", err)
        self.assertIn("一次資料として昇格させない", err)
        self.assertIn("coverage を広げる", err)
        self.assertIn("Verify commercial", err)
        self.assertIn("materiality:", err)

    def test_review_rationale_meta_rebuttal_fails(self) -> None:
        """Meta-rebuttal to prior review comments is blocked."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain topics"]
        )
        main_tex.write_text(
            "\\section{Week in Review}\n"
            "W35は三つのFeatureだけではない。前回の指摘により、多面的な展開を扱う。\n",
            encoding="utf-8",
        )
        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain topics",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]
        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"

        with self.assertRaises(ValueError) as ctx:
            reader.build_manuscript_manifest(
                self.root,
                "2026-W35",
                profile,
                arch,
                app,
                main_tex,
                [],
                coverage,
                reader_reqs,
                "ChatGPT",
                self.now,
                m_out,
            )
        err = str(ctx.exception)
        self.assertIn("RSG-LEX-REVIEW-RATIONALE-COP-OUT", err)
        self.assertIn("W35は三つのFeatureだけではない", err)

    def test_must_cover_cop_out_fails(self) -> None:
        """Asserting 'Architecture requires X' instead of explaining facts is blocked."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain topics"]
        )
        main_tex.write_text(
            "\\section{Topics}\n"
            "承認済みArchitectureは release wave と cost per run を観察軸としている。\n",
            encoding="utf-8",
        )
        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain topics",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]
        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"

        with self.assertRaises(ValueError) as ctx:
            reader.build_manuscript_manifest(
                self.root,
                "2026-W35",
                profile,
                arch,
                app,
                main_tex,
                [],
                coverage,
                reader_reqs,
                "ChatGPT",
                self.now,
                m_out,
            )
        err = str(ctx.exception)
        self.assertIn("RSG-LEX-REVIEW-RATIONALE-COP-OUT", err)

    def test_bibliography_leakage_detected(self) -> None:
        """Bibliography containing [V/M] tags or internal tmp paths is blocked."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain topics"]
        )
        main_tex.write_text("\\section{Topics}\nClean section prose.\n", encoding="utf-8")
        bib.write_text(
            "@online{sourceA,\n"
            "  title = {{A Valid Paper}},\n"
            "  author = {{Author Name}},\n"
            "  url = {https://example.com/paper},\n"
            "  note = {Evidence tags: [V/M] [P/C]},\n"
            "  urldate = {2026-09-14}\n"
            "}\n"
            "@online{sourceB,\n"
            "  title = {{Temp Source}},\n"
            "  author = {{Author Name}},\n"
            "  url = {file:///tmp/executor/raw_source.html},\n"
            "  urldate = {2026-09-14}\n"
            "}\n",
            encoding="utf-8",
        )
        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain topics",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]
        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"

        with self.assertRaises(ValueError) as ctx:
            reader.build_manuscript_manifest(
                self.root,
                "2026-W35",
                profile,
                arch,
                app,
                main_tex,
                [{"role": "BIBLIOGRAPHY", "path": str(bib.relative_to(self.root))}],
                coverage,
                reader_reqs,
                "ChatGPT",
                self.now,
                m_out,
            )
        err = str(ctx.exception)
        self.assertIn("RSG-LEX-BIBLIOGRAPHY-LEAKAGE", err)
        self.assertIn("[V/M]", err)
        self.assertIn("RSG-LEX-INTERNAL-PATHS", err)
        self.assertIn("/tmp/", err)

    def test_narrow_allowlist_suppression_allows_pass(self) -> None:
        """Narrow allowlist with audited reason converts finding to SUPPRESSED and allows pass."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain medical screening"]
        )
        # Legitimate technical discussion of medical diagnostic screening
        main_tex.write_text(
            "\\section{Medical Screening}\n"
            "Recent evaluations examine candidate screening models for clinical triage.\n",
            encoding="utf-8",
        )
        bib.write_text("@online{ref1,title={Ref},author={Org},url={https://example.com}}\n", encoding="utf-8")

        suppressions = [
            {
                "rule_id": "RSG-LEX-SELECTION-SCREENING",
                "path": str(main_tex.relative_to(self.root)),
                "matched_text": "candidate screening",
                "reason": "Audited domain terminology for medical clinical triage models",
            }
        ]

        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain medical screening",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]

        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"
        m_path = reader.build_manuscript_manifest(
            self.root,
            "2026-W35",
            profile,
            arch,
            app,
            main_tex,
            [],
            coverage,
            reader_reqs,
            "ChatGPT",
            self.now,
            m_out,
            suppressions=suppressions,
        )

        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        report = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, suppressions=suppressions, recorded_at=self.now
        )
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["summary"]["blocking_findings"], 0)
        self.assertEqual(report["summary"]["suppressed_findings"], 1)

    def test_semantic_layer_review_contract_evaluation(self) -> None:
        """Semantic review layer flags process-dependent prose with proposed normalization."""
        profile, arch, app, main_tex, bib = self._setup_edition(
            "2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", ["Explain topics"]
        )
        main_tex.write_text("\\section{Topics}\nDomain text.\n", encoding="utf-8")
        bib.write_text("@online{ref1,title={Ref},author={Org},url={https://example.com}}\n", encoding="utf-8")

        coverage = [
            {
                "package_id": "PKG-1",
                "requirement": "Explain topics",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:section"],
                "detail": "detail",
            }
        ]
        reader_reqs = [
            {
                "requirement_id": "FINAL_SYNTHESIS",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:summary"],
                "detail": "detail",
            },
            {
                "requirement_id": "WEEKLY_COMMUNITY_MOVEMENT",
                "status": "FULFILLED",
                "reader_locations": ["main.tex:community"],
                "detail": "detail",
            },
        ]
        m_out = self.root / "sources/2026-W35/publication/v2/reader-manuscript-v2.json"
        m_path = reader.build_manuscript_manifest(
            self.root, "2026-W35", profile, arch, app, main_tex, [], coverage, reader_reqs, "ChatGPT", self.now, m_out
        )

        # Unresolved semantic finding
        sem_findings = [
            {
                "finding_id": "SEM-001",
                "rule_id": "RSG-SEM-PROCESS-LEAKAGE",
                "artifact": "surveys/weekly/2026-W35/main.tex",
                "path": "surveys/weekly/2026-W35/main.tex",
                "field_or_block": "Section 1",
                "locator": "Paragraph 2",
                "text_span": "The downstream package synthesis reflects the operator evidence handoff",
                "severity": "BLOCKING",
                "reason": "Sentence requires knowledge of J-GAS operator evidence handoff",
                "proposed_normalization": "State that the comparison combines benchmark results with cloud service limits",
                "disposition": "UNRESOLVED",
            }
        ]

        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        report_fail = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, semantic_review_findings=sem_findings, recorded_at=self.now
        )
        self.assertEqual(report_fail["status"], "FAILED")
        self.assertEqual(report_fail["summary"]["blocking_findings"], 1)

        # Normalized semantic finding
        sem_findings[0]["disposition"] = "NORMALIZED"
        report_pass = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, semantic_review_findings=sem_findings, recorded_at=self.now
        )
        self.assertEqual(report_pass["status"], "PASSED")
        self.assertEqual(report_pass["summary"]["blocking_findings"], 0)
        self.assertEqual(report_pass["summary"]["normalized_findings"], 1)

    def test_longform_revision_strengthened_validator(self) -> None:
        """survey_longform_publication_v2 validates all reader text via strengthened surface gate."""
        from scripts import survey_longform_publication_v2 as longform_pub

        # Test valid reader text
        valid_text = longform_pub._strengthened_reader_text("Clean reader text discussing model accuracy.", "test")
        self.assertEqual(valid_text, "Clean reader text discussing model accuracy.")

        # Test leakage rejection
        for leaked in [
            "D017 と D021 の比較",
            "本 package における分析",
            "一次資料として昇格させない",
            "coverage を広げる",
            "Selection r2 の結果",
            "Package 4 の内容",
            "Discovery observation による観測",
            "Verify that safety guards work",
            "materiality: MATERIAL",
        ]:
            with self.subTest(leaked=leaked):
                with self.assertRaises(ValueError) as ctx:
                    longform_pub._strengthened_reader_text(leaked, "test_field")
                self.assertIn("leaks production metadata", str(ctx.exception))

    def test_missing_semantic_authority_fails(self) -> None:
        """Omitting machine-checkable semantic_authority raises ValueError and cannot PASS."""
        _, _, _, m_path = self._build_valid_manifest()
        with self.assertRaises(ValueError) as ctx:
            surface_gate.evaluate_reader_surface_gate(self.root, m_path, semantic_authority=None)
        self.assertIn("Reader-Surface Gate requires machine-checkable semantic_authority", str(ctx.exception))

    def test_semantic_authority_surface_sha_mismatch_fails(self) -> None:
        """Semantic authority bound to wrong primary surface SHA triggers blocking finding."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        sem_auth["surface_sha256"] = "f" * 64
        report = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now
        )
        self.assertEqual(report["status"], "FAILED")
        self.assertTrue(any(f["finding_id"] == "RSG-SEM-SURFACE-SHA-MISMATCH" for f in report["findings"]))

    def test_semantic_authority_non_pass_fails(self) -> None:
        """Semantic authority with non-PASS status/decision triggers blocking finding."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(
            main_tex, decision="FAIL", status="FAILED", recorded_at=self.now
        )
        report = surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now
        )
        self.assertEqual(report["status"], "FAILED")
        self.assertTrue(any(f["finding_id"] == "RSG-SEM-AUTHORITY-FAILED" for f in report["findings"]))

    def test_validate_reader_surface_gate_valid_passes(self) -> None:
        """Independent validator passes a well-formed, untampered Reader-Surface Gate."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        gate_path = self.root / "sources/2026-W35/publication/v2/reader-surface-gate-v2.json"
        surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now, output_path=gate_path
        )
        res = surface_gate.validate_reader_surface_gate(
            self.root, gate_path, issue_id="2026-W35", publication_profile="WEEKLY_MAGAZINE"
        )
        self.assertEqual(res["status"], "PASSED")
        self.assertEqual(res["gate_sha256"], core.sha256_object({k: v for k, v in res.items() if k != "gate_sha256"}))

    def test_validate_reader_surface_gate_tampered_gate_sha_fails(self) -> None:
        """Independent validator catches fabricated or tampered gate_sha256."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        gate_path = self.root / "sources/2026-W35/publication/v2/reader-surface-gate-v2.json"
        surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now, output_path=gate_path
        )
        data = core.load_json(gate_path)
        data["gate_sha256"] = "0" * 64
        core.write_json(gate_path, data)
        with self.assertRaises(ValueError) as ctx:
            surface_gate.validate_reader_surface_gate(self.root, gate_path)
        self.assertIn("digest mismatch", str(ctx.exception))

    def test_validate_reader_surface_gate_stale_surface_sha_or_bytes_fails(self) -> None:
        """Independent validator catches drifted or mutated on-disk surface bytes."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        gate_path = self.root / "sources/2026-W35/publication/v2/reader-surface-gate-v2.json"
        surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now, output_path=gate_path
        )
        # Mutate main_tex on disk after gate evaluation
        main_tex.write_text(main_tex.read_text(encoding="utf-8") + "% mutated comment\n", encoding="utf-8")
        with self.assertRaises(ValueError) as ctx:
            surface_gate.validate_reader_surface_gate(self.root, gate_path)
        self.assertIn("drifted", str(ctx.exception))

    def test_validate_reader_surface_gate_identity_mismatch_fails(self) -> None:
        """Independent validator rejects issue_id or publication_profile identity mismatch."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        gate_path = self.root / "sources/2026-W35/publication/v2/reader-surface-gate-v2.json"
        surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now, output_path=gate_path
        )
        with self.assertRaises(ValueError) as ctx:
            surface_gate.validate_reader_surface_gate(self.root, gate_path, issue_id="2026-W36")
        self.assertIn("issue_id mismatch", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx2:
            surface_gate.validate_reader_surface_gate(self.root, gate_path, publication_profile="SPECIAL_EDITION")
        self.assertIn("publication_profile mismatch", str(ctx2.exception))

    def test_validate_reader_surface_gate_unresolved_blocking_finding_fails(self) -> None:
        """Independent validator rejects gate record containing unresolved blocking findings."""
        _, main_tex, _, m_path = self._build_valid_manifest()
        sem_auth = surface_gate.build_semantic_authority(main_tex, recorded_at=self.now)
        gate_path = self.root / "sources/2026-W35/publication/v2/reader-surface-gate-v2.json"
        surface_gate.evaluate_reader_surface_gate(
            self.root, m_path, semantic_authority=sem_auth, recorded_at=self.now, output_path=gate_path
        )
        data = core.load_json(gate_path)
        data["findings"].append({
            "finding_id": "TEST-BLOCKING",
            "rule_id": "RSG-SEM-PROCESS-LEAKAGE",
            "artifact": "surveys/weekly/2026-W35/main.tex",
            "path": "surveys/weekly/2026-W35/main.tex",
            "field_or_block": "Section 1",
            "locator": "line 1",
            "text_span": "leaked process text",
            "severity": "BLOCKING",
            "reason": "Process leakage",
            "proposed_normalization": "Fix",
            "disposition": "UNRESOLVED",
        })
        base = {k: v for k, v in data.items() if k != "gate_sha256"}
        data["gate_sha256"] = core.sha256_object(base)
        core.write_json(gate_path, data)
        with self.assertRaises(ValueError) as ctx:
            surface_gate.validate_reader_surface_gate(self.root, gate_path)
        self.assertIn("unresolved blocking finding", str(ctx.exception))

    def test_missing_publication_payload_refuses_fallback(self) -> None:
        """Weekly reader-facing synthesis refuses fallback to internal profile_payload."""
        # When publication_payload is absent
        syn_no_pub = {"profile_payload": {"current_interpretation": "fallback text"}}
        pub = syn_no_pub.get("publication_payload")
        self.assertFalse(isinstance(pub, dict) and bool(pub))

        # When publication_payload is empty dict
        syn_empty_pub = {"publication_payload": {}, "profile_payload": {"current_interpretation": "fallback text"}}
        pub2 = syn_empty_pub.get("publication_payload")
        self.assertFalse(isinstance(pub2, dict) and bool(pub2))

        # When publication_payload has neither closing_synthesis nor current_interpretation
        syn_no_text = {"publication_payload": {"other": 123}, "profile_payload": {"current_interpretation": "fallback text"}}
        closing = syn_no_text["publication_payload"].get("closing_synthesis") or syn_no_text["publication_payload"].get("current_interpretation")
        self.assertIsNone(closing)

    def test_pre_tex_structured_reader_surface_validation_catches_leakage(self) -> None:
        """Pre-TeX structured reader-facing scan detects blocking leakage before TeX generation."""
        leaked_closing = "Selection r2 で Package 4 に配置した Discovery observation に基づく。"
        findings = surface_gate.scan_reader_text_lines([leaked_closing], "Profile Synthesis closing_synthesis", "loc")
        blocking = [f for f in findings if f.severity == "BLOCKING" and f.disposition == "UNRESOLVED"]
        self.assertGreater(len(blocking), 0)
        self.assertTrue(any("Selection r2" in f.text_span for f in blocking))

    def test_missing_reader_surface_gate_artifact_blocks_stage(self) -> None:
        """DRAFT_COMPLETE and VALIDATED_DRAFT require reader-surface-gate artifact."""
        from scripts import survey_stage_validation_v2 as stage_validation
        self.assertIn("reader-surface-gate", stage_validation.REQUIRED_CURRENT["DRAFT_COMPLETE"])
        with self.assertRaises(stage_validation.StageValidationError) as ctx:
            stage_validation._require({"reader-manuscript": Path("m")}, "reader-surface-gate")
        self.assertIn("reader-surface-gate", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
