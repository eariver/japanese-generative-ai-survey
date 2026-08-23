from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality
from scripts import survey_reader_publication_v2 as reader
from scripts import survey_review_attention_v2 as review_attention


class SurveyHumanGateV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.cfg = core.load_json(cls.root / core.DEFAULT_CONFIG)
        cls.impl = core.repository_commit_sha(cls.root)

    def setUp(self) -> None:
        sources = self.root / "sources"
        sources.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=sources)
        self.addCleanup(self.temp.cleanup)
        self.source_root = Path(self.temp.name)
        self.source_rel = self.source_root.relative_to(self.root).as_posix()
        self.issue_id = "HG-ROUNDTRIP"
        self.branch = "test/human-gate-roundtrip"
        self.survey_root = self.source_root / "survey"
        self.survey_rel = self.survey_root.relative_to(self.root).as_posix()
        spec = {
            "issue_id": self.issue_id,
            "question": "Can both Human Gates round-trip without losing exact-byte provenance?",
            "temporal_mode": "OPEN_HISTORY_AS_OF",
            "as_of": "2026-08-24T00:00:00Z",
            "scope_dimensions": ["human gate round trip"],
            "source_root": self.source_rel,
            "survey_root": self.survey_rel,
            "work_branch": self.branch,
        }
        profile = core.thematic_profile(self.root, self.cfg, spec)
        self.profile_path, self.state_path = core.initialize(
            self.root,
            self.cfg,
            profile,
            self.impl,
            "PUBLICATION_PREVIEW",
            core.parse_instant("2026-08-24T00:00:00Z"),
        )
        self._last_artifacts: dict[str, Path] = {}

    def _write_json(self, rel: str, payload: dict) -> Path:
        path = self.source_root / rel
        core.write_json(path, payload)
        return path

    def _snapshot_review_commit(self) -> str:
        fd, index_name = tempfile.mkstemp(prefix="survey-human-review-index-")
        os.close(fd)
        index_path = Path(index_name)
        index_path.unlink()
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(index_path)
        try:
            subprocess.run(
                ["git", "read-tree", self.impl],
                cwd=self.root,
                env=env,
                check=True,
                capture_output=True,
            )
            for path in sorted(candidate for candidate in self.source_root.rglob("*") if candidate.is_file()):
                rel = path.relative_to(self.root).as_posix()
                blob = subprocess.run(
                    ["git", "hash-object", "-w", str(path)],
                    cwd=self.root,
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout.strip()
                subprocess.run(
                    ["git", "update-index", "--add", "--cacheinfo", f"100644,{blob},{rel}"],
                    cwd=self.root,
                    env=env,
                    check=True,
                    capture_output=True,
                )
            tree = subprocess.run(
                ["git", "write-tree"],
                cwd=self.root,
                env=env,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            commit = subprocess.run(
                [
                    "git",
                    "-c",
                    "user.name=Survey Human Gate Fixture",
                    "-c",
                    "user.email=survey-human-gate@example.invalid",
                    "commit-tree",
                    tree,
                    "-p",
                    self.impl,
                    "-m",
                    "Human Gate reviewed fixture snapshot",
                ],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
        finally:
            index_path.unlink(missing_ok=True)
        if len(commit) != 40 or any(char not in "0123456789abcdef" for char in commit):
            raise AssertionError(f"invalid fixture review commit SHA: {commit}")
        return commit

    def _artifacts(self, rows: dict[str, str]) -> dict[str, Path]:
        result: dict[str, Path] = {}
        for name, rel in rows.items():
            path = self.source_root / rel
            core.write_json(path, {"fixture": name, "issue_id": self.issue_id})
            result[name] = path
        self._last_artifacts = dict(result)
        return result

    def _review_file(self, check_id: str, recorded_at: str) -> Path:
        state = core.load_json(self.state_path)
        stage = self.cfg["orchestration"]["stage_plan"][state["lifecycle_state"]]
        artifacts = [
            {
                "name": name,
                "path": path.relative_to(self.root).as_posix(),
                "sha256": core.sha256_file(path),
            }
            for name, path in sorted(self._last_artifacts.items())
        ]
        result_path = self.source_root / "review-results" / f"CORE_STAGE_CONTRACT-{state['lifecycle_state']}.json"
        core.write_json(
            result_path,
            {
                "schema_version": "2.0-rc1",
                "check_id": agent.CORE_STAGE_REVIEW_ID,
                "status": "PASS",
                "issue_id": self.issue_id,
                "from_state": state["lifecycle_state"],
                "to_state": stage["next_state"],
                "production_state": {
                    "path": self.state_path.relative_to(self.root).as_posix(),
                    "sha256": core.sha256_file(self.state_path),
                },
                "production_profile": {
                    "path": self.profile_path.relative_to(self.root).as_posix(),
                    "sha256": core.sha256_file(self.profile_path),
                },
                "implementation_commit_sha": self.impl,
                "contract": core.contract_identity(
                    self.root,
                    self.cfg,
                    state["research_profile"],
                    state["publication_profile"],
                ),
                "artifacts": artifacts,
                "recorded_at": recorded_at,
            },
        )
        reviews = self.source_root / "reviews" / f"{check_id}.json"
        core.write_json(
            reviews,
            {
                "reviews": [
                    {
                        "check_id": agent.CORE_STAGE_REVIEW_ID,
                        "kind": "DETERMINISTIC",
                        "executor": "human-gate-fixture",
                        "evidence": "Fixture exact stage contract.",
                        "result_path": result_path.relative_to(self.root).as_posix(),
                    },
                    {
                        "check_id": check_id,
                        "kind": "AGENT_EDITORIAL",
                        "executor": "ChatGPT",
                        "evidence": "Fixture stage reviewed for Human Gate round-trip coverage.",
                    },
                ]
            },
        )
        return reviews

    def _advance(self, artifacts: dict[str, Path], check_id: str, recorded_at: str) -> dict:
        self._last_artifacts = dict(artifacts)
        reviews = self._review_file(check_id, recorded_at)
        checkpoint = agent.build_stage_checkpoint(
            self.root,
            self.cfg,
            self.state_path,
            artifacts,
            reviews,
            f"Advance fixture stage {check_id}.",
            core.parse_instant(recorded_at),
            self.impl,
        )
        return agent.advance_with_checkpoint(self.root, self.cfg, self.state_path, checkpoint)

    def _advance_to_selection(self) -> None:
        self._advance(
            self._artifacts({"discovery-acceptance": "discovery/discovery-accepted-v2.json"}),
            "DISCOVERY_FIXTURE",
            "2026-08-24T00:01:00Z",
        )
        self._advance(
            self._artifacts({"screening-acceptance": "screening/v2/accepted-fixture/screening-accepted.json"}),
            "SCREENING_FIXTURE",
            "2026-08-24T00:02:00Z",
        )
        self._advance(
            self._artifacts(
                {
                    "evidence-acceptance": "evidence/v2/evidence-accepted.json",
                    "edition-views-acceptance": "evidence/v2/edition-views-accepted.json",
                    "materiality-ledger": "materiality-ledger-v2.json",
                    "profile-completeness": "profile-completeness-v2.json",
                }
            ),
            "EVIDENCE_FIXTURE",
            "2026-08-24T00:03:00Z",
        )
        self._advance(
            self._artifacts(
                {
                    "candidate-matrix": "candidate-matrix-v2.json",
                    "candidate-selection": "candidate-selection-v2.json",
                }
            ),
            "SELECTION_FIXTURE",
            "2026-08-24T00:04:00Z",
        )

    def _build_attention(self) -> Path:
        screening = self._write_json("attention/screening.json", {"issue_id": self.issue_id, "decisions": []})
        materiality = self._write_json("attention/materiality.json", {"issue_id": self.issue_id, "rows": []})
        selection = self._write_json("attention/selection.json", {"issue_id": self.issue_id, "assignments": []})
        output = self.source_root / "architecture-review-attention-v2.json"
        if output.exists():
            output.unlink()
        return review_attention.build_attention(self.root, screening, materiality, selection, output)

    def _architecture_files(self, thesis: str) -> dict[str, Path]:
        architecture = self.source_root / "architecture-v2.json"
        core.write_json(
            architecture,
            {
                "schema_version": "2.0-rc1",
                "issue_id": self.issue_id,
                "research_profile": "THEMATIC",
                "publication_profile": "LONGFORM_SPECIAL",
                "status": "PROPOSED",
                "basis": {
                    "production_profile_sha256": core.sha256_file(self.profile_path),
                    "profile_completeness_sha256": "1" * 64,
                    "materiality_ledger_sha256": "2" * 64,
                    "candidate_matrix_sha256": "3" * 64,
                    "candidate_selection_sha256": "4" * 64,
                },
                "editorial_thesis": thesis,
                "architecture_goals": ["Exercise Human Gate round-trip semantics"],
                "page_plan": {"target_pages": 8, "max_pages": 16, "notes": "fixture"},
                "packages": [
                    {
                        "package_id": "PKG-1",
                        "title": "Round-trip package",
                        "purpose": "Exercise exact reviewed-byte authority.",
                        "primary_candidate_ids": ["C-1"],
                        "supporting_candidate_ids": [],
                        "must_cover_requirements": ["Explain the round-trip result"],
                        "boundaries": ["Keep fixture claims bounded"],
                        "drafting_order": 1,
                        "profile_extensions": {},
                        "publication_extensions": {},
                    }
                ],
                "selected_exceptions": [],
                "profile_extensions": {},
                "publication_extensions": {},
                "human_review": {"reviewed_by": None, "reviewed_at": None, "review_reference": None},
            },
        )
        summary = self.source_root / "architecture-review-summary-v2.json"
        core.write_json(
            summary,
            {
                "issue_id": self.issue_id,
                "readiness": {"status": "READY_FOR_ARCHITECTURE_REVIEW"},
                "basis": {"architecture_sha256": core.sha256_file(architecture)},
            },
        )
        attention = self.source_root / "architecture-review-attention-v2.json"
        if not attention.exists():
            self._build_attention()
        return {
            "issue-architecture": architecture,
            "architecture-review-summary": summary,
            "architecture-review-attention": attention,
        }

    def _reach_architecture_gate(self, thesis: str, recorded_at: str) -> dict:
        files = self._architecture_files(thesis)
        state = self._advance(files, "ARCHITECTURE_FIXTURE", recorded_at)
        self.assertEqual(state["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["terminal_reason"], "HUMAN_GATE_REACHED")
        return state

    def _deterministic_checks(self, publication_dir: Path) -> list[dict[str, object]]:
        expected = quality.expected_checks_by_kind(
            self.cfg,
            "THEMATIC",
            "LONGFORM_SPECIAL",
            {"DETERMINISTIC"},
        )
        rows: list[dict[str, object]] = []
        for check_id in sorted(expected):
            result_path = publication_dir / "quality-results" / f"{check_id}.json"
            core.write_json(result_path, {"check_id": check_id, "status": "PASS"})
            rows.append(
                {
                    "check_id": check_id,
                    "kind": "DETERMINISTIC",
                    "status": "PASS",
                    "executor": "human-gate-fixture",
                    "evidence": f"fixture:{check_id}",
                    "recorded_at": "2026-08-24T00:20:00Z",
                    "result": {
                        "path": result_path.relative_to(self.root).as_posix(),
                        "sha256": core.sha256_file(result_path),
                    },
                }
            )
        return rows

    def _review_checks(self, kind: str) -> list[dict[str, object]]:
        profile = core.load_json(self.profile_path)
        return [
            {
                "check_id": check_id,
                "status": "PASS",
                "detail": f"Fixture {kind} review passed {check_id}",
                "evidence_locations": ["main.tex:fixture"],
            }
            for check_id in sorted(reader._expected_review_checks(self.root, profile, kind))
        ]

    def _build_publication_candidate(self, revision: int) -> dict[str, Path]:
        publication_dir = self.source_root / "publication/v2"
        publication_dir.mkdir(parents=True, exist_ok=True)
        self.survey_root.mkdir(parents=True, exist_ok=True)
        source = self.survey_root / "main.tex"
        bibliography = self.survey_root / "references.bib"
        pdf = self.survey_root / "main.pdf"
        source.write_text(f"reader-facing source revision {revision} with final synthesis\n", encoding="utf-8")
        bibliography.write_text("@misc{fixture,title={Fixture}}\n", encoding="utf-8")
        pdf.write_bytes(f"%PDF-1.7\nfixture-r{revision}\n".encode("utf-8"))

        paths = {
            "manifest": publication_dir / "reader-manuscript-v2.json",
            "bundle": publication_dir / "quality-regression-bundle-v2.json",
            "semantic": publication_dir / "semantic-editorial-review-v2.json",
            "visual": publication_dir / "visual-review-v2.json",
            "candidate": publication_dir / "publication-candidate-v2.json",
        }
        for path in paths.values():
            if path.exists():
                path.unlink()
        quality_results = publication_dir / "quality-results"
        if quality_results.exists():
            for path in quality_results.glob("*.json"):
                path.unlink()

        approval = self.source_root / self.cfg["state_authority"]["architecture_approval_path"]
        architecture = self.source_root / "architecture-v2.json"
        reader.build_manuscript_manifest(
            self.root,
            self.issue_id,
            self.profile_path,
            architecture,
            approval,
            source,
            [{"role": "BIBLIOGRAPHY", "path": bibliography}],
            [
                {
                    "package_id": "PKG-1",
                    "requirement": "Explain the round-trip result",
                    "status": "FULFILLED",
                    "reader_locations": ["main.tex:fixture"],
                    "detail": "Fixture covers the Architecture requirement.",
                }
            ],
            [
                {
                    "requirement_id": "FINAL_SYNTHESIS",
                    "status": "FULFILLED",
                    "reader_locations": ["main.tex:fixture"],
                    "detail": "Fixture final synthesis present.",
                }
            ],
            "ChatGPT",
            datetime(2026, 8, 24, 0, 20 + revision, tzinfo=timezone.utc),
            paths["manifest"],
        )
        quality.build_bundle(
            self.root,
            self.issue_id,
            source,
            pdf,
            self._deterministic_checks(publication_dir),
            paths["bundle"],
            production_profile_path=self.profile_path,
        )
        reader.build_review_record(
            self.root,
            paths["manifest"],
            pdf,
            8,
            "SEMANTIC_EDITORIAL",
            self._review_checks("SEMANTIC_EDITORIAL"),
            "ChatGPT",
            datetime(2026, 8, 24, 0, 22 + revision, tzinfo=timezone.utc),
            paths["semantic"],
        )
        reader.build_review_record(
            self.root,
            paths["manifest"],
            pdf,
            8,
            "VISUAL",
            self._review_checks("VISUAL"),
            "ChatGPT",
            datetime(2026, 8, 24, 0, 24 + revision, tzinfo=timezone.utc),
            paths["visual"],
        )
        publication.build_candidate(
            self.root,
            self.issue_id,
            "LONGFORM_SPECIAL",
            paths["manifest"],
            source,
            pdf,
            8,
            paths["bundle"],
            paths["semantic"],
            paths["visual"],
            paths["candidate"],
        )
        return {**paths, "source": source, "pdf": pdf}

    def _reach_publication_gate(self, revision: int, minute_base: int) -> dict[str, Path]:
        synthesis_input = self._write_json(f"draft/r{revision}/synthesis-input.json", {"revision": revision})
        synthesis_result = self._write_json(f"draft/r{revision}/synthesis-result.json", {"revision": revision})
        draft_package = self._write_json(f"draft/r{revision}/package.json", {"revision": revision})
        draft_result = self._write_json(f"draft/r{revision}/result.json", {"revision": revision})
        self._advance(
            {
                "synthesis-input": synthesis_input,
                "synthesis-result": synthesis_result,
                "draft-package:PKG-1": draft_package,
                "draft-result:PKG-1": draft_result,
            },
            f"DRAFT_FIXTURE_R{revision}",
            f"2026-08-24T00:{minute_base:02d}:00Z",
        )
        candidate_paths = self._build_publication_candidate(revision)
        self._advance(
            {
                "reader-manuscript": candidate_paths["manifest"],
                "validated-source": candidate_paths["source"],
                "publication-pdf": candidate_paths["pdf"],
                "quality-regression-bundle": candidate_paths["bundle"],
                "semantic-review": candidate_paths["semantic"],
                "visual-review": candidate_paths["visual"],
            },
            f"VALIDATION_FIXTURE_R{revision}",
            f"2026-08-24T00:{minute_base + 1:02d}:00Z",
        )
        state = self._advance(
            {"publication-candidate": candidate_paths["candidate"]},
            f"CANDIDATE_FIXTURE_R{revision}",
            f"2026-08-24T00:{minute_base + 2:02d}:00Z",
        )
        self.assertEqual(state["lifecycle_state"], "RELEASE_CANDIDATE")
        self.assertEqual(state["terminal_reason"], "HUMAN_GATE_REACHED")
        return candidate_paths

    def test_architecture_request_changes_regenerates_r2_then_approves(self) -> None:
        self._advance_to_selection()
        self._reach_architecture_gate("Architecture r1", "2026-08-24T00:05:00Z")
        checkpoint = self.source_root / self.cfg["state_authority"]["agent_checkpoint_dir"] / "SELECTION_COMPLETE.json"
        self.assertTrue(checkpoint.is_file())

        state, record_r1, index, removed = human_gate.request_architecture_revision(
            self.root,
            self.cfg,
            self.state_path,
            "SELECTION_COMPLETE",
            "Clarify the Architecture thesis before drafting.",
            "human-reviewer",
            core.parse_instant("2026-08-24T00:06:00Z"),
            "review:architecture:r1",
            expected_revision=1,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        self.assertEqual(state["lifecycle_state"], "SELECTION_COMPLETE")
        self.assertEqual(state["machine_checkpoints"]["architecture"], "pending")
        self.assertIsNone(state["checkpoint_provenance"]["architecture"])
        self.assertFalse(checkpoint.exists())
        self.assertIn(checkpoint.relative_to(self.root).as_posix(), removed)
        self.assertEqual(core.load_json(record_r1)["decision"], "REQUEST_CHANGES")
        self.assertEqual(core.load_json(index)["reviews"][0]["revision"], 1)

        self._reach_architecture_gate("Architecture r2", "2026-08-24T00:07:00Z")
        with self.assertRaisesRegex(ValueError, "stale Human Gate request"):
            human_gate.record_architecture_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:08:00Z"),
                "review:architecture:stale-r1",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )

        state, record_r2, index = human_gate.record_architecture_approval(
            self.root,
            self.cfg,
            self.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:09:00Z"),
            "review:architecture:r2",
            expected_revision=2,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["next_action"], "stage:drafting-synthesis")
        self.assertIsNone(state["terminal_reason"])
        reviews = core.load_json(index)["reviews"]
        self.assertEqual([(r["revision"], r["decision"]) for r in reviews], [(1, "REQUEST_CHANGES"), (2, "APPROVED")])
        self.assertEqual(core.load_json(record_r2)["decision"], "APPROVED")

    def test_review_commit_must_exist_and_bind_current_gate_bytes(self) -> None:
        self._advance_to_selection()
        self._reach_architecture_gate("Architecture provenance", "2026-08-24T00:05:00Z")

        with self.assertRaisesRegex(ValueError, "reviewed repository commit does not exist"):
            human_gate.record_architecture_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:06:00Z"),
                "review:architecture:missing-commit",
                expected_revision=1,
                reviewed_commit_sha="0" * 40,
            )

        with self.assertRaisesRegex(ValueError, "missing reviewed path"):
            human_gate.record_architecture_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:06:30Z"),
                "review:architecture:missing-bytes",
                expected_revision=1,
                reviewed_commit_sha=self.impl,
            )

        architecture = self.source_root / "architecture-v2.json"
        original = architecture.read_bytes()
        payload = core.load_json(architecture)
        payload["editorial_thesis"] = "Different bytes in the claimed reviewed commit"
        core.write_json(architecture, payload)
        mismatched_commit = self._snapshot_review_commit()
        architecture.write_bytes(original)

        with self.assertRaisesRegex(ValueError, "reviewed repository commit bytes differ"):
            human_gate.record_architecture_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:07:00Z"),
                "review:architecture:mismatched-commit",
                expected_revision=1,
                reviewed_commit_sha=mismatched_commit,
            )

        reviewed_commit = self._snapshot_review_commit()
        state, record_path, _ = human_gate.record_architecture_approval(
            self.root,
            self.cfg,
            self.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:08:00Z"),
            "review:architecture:committed-bytes",
            expected_revision=1,
            reviewed_commit_sha=reviewed_commit,
        )
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(
            core.load_json(record_path)["reviewed_repository_commit_sha"],
            reviewed_commit,
        )

    def test_architecture_revision_rejects_invalid_boundary_and_changed_review_bytes(self) -> None:
        self._advance_to_selection()
        self._reach_architecture_gate("Architecture stable", "2026-08-24T00:05:00Z")
        before = core.load_json(self.state_path)
        with self.assertRaisesRegex(ValueError, "not allowed for ARCHITECTURE_REVIEW"):
            human_gate.request_architecture_revision(
                self.root,
                self.cfg,
                self.state_path,
                "DRAFT_COMPLETE",
                "Invalid rollback.",
                "human-reviewer",
                core.parse_instant("2026-08-24T00:06:00Z"),
                "review:architecture:bad-boundary",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )
        self.assertEqual(core.load_json(self.state_path), before)

        architecture = self.source_root / "architecture-v2.json"
        payload = core.load_json(architecture)
        payload["editorial_thesis"] = "Changed after checkpoint review"
        core.write_json(architecture, payload)
        with self.assertRaisesRegex(ValueError, "Stage Checkpoint artifact drift"):
            human_gate.record_architecture_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:07:00Z"),
                "review:architecture:changed-bytes",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )

    def test_publication_preview_request_changes_regenerates_r2_then_approves(self) -> None:
        self._advance_to_selection()
        self._reach_architecture_gate("Approved Architecture", "2026-08-24T00:05:00Z")
        human_gate.record_architecture_approval(
            self.root,
            self.cfg,
            self.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:06:00Z"),
            "review:architecture:r1",
            expected_revision=1,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        candidate_r1 = self._reach_publication_gate(1, 10)
        validation_checkpoint = self.source_root / self.cfg["state_authority"]["agent_checkpoint_dir"] / "DRAFT_COMPLETE.json"
        candidate_checkpoint = self.source_root / self.cfg["state_authority"]["agent_checkpoint_dir"] / "VALIDATED_DRAFT.json"
        self.assertTrue(validation_checkpoint.is_file())
        self.assertTrue(candidate_checkpoint.is_file())

        original_pdf = candidate_r1["pdf"].read_bytes()
        candidate_r1["pdf"].write_bytes(b"%PDF-1.7\nchanged-after-review\n")
        with self.assertRaises(ValueError):
            human_gate.record_publication_preview_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:14:00Z"),
                "review:publication:changed-bytes",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )
        candidate_r1["pdf"].write_bytes(original_pdf)

        state, record_r1, index, removed = human_gate.request_publication_preview_revision(
            self.root,
            self.cfg,
            self.state_path,
            "DRAFT_COMPLETE",
            "Improve page balance and regenerate the reviewed publication bytes.",
            "human-reviewer",
            core.parse_instant("2026-08-24T00:15:00Z"),
            "review:publication:r1",
            expected_revision=1,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        self.assertEqual(state["lifecycle_state"], "DRAFT_COMPLETE")
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["human_gates"]["publication_preview"], "pending")
        self.assertEqual(state["machine_checkpoints"]["validation"], "pending")
        self.assertFalse(validation_checkpoint.exists())
        self.assertFalse(candidate_checkpoint.exists())
        self.assertIn(validation_checkpoint.relative_to(self.root).as_posix(), removed)
        self.assertIn(candidate_checkpoint.relative_to(self.root).as_posix(), removed)
        self.assertEqual(core.load_json(record_r1)["decision"], "REQUEST_CHANGES")

        candidate_r2 = self._build_publication_candidate(2)
        self._advance(
            {
                "reader-manuscript": candidate_r2["manifest"],
                "validated-source": candidate_r2["source"],
                "publication-pdf": candidate_r2["pdf"],
                "quality-regression-bundle": candidate_r2["bundle"],
                "semantic-review": candidate_r2["semantic"],
                "visual-review": candidate_r2["visual"],
            },
            "VALIDATION_FIXTURE_R2",
            "2026-08-24T00:16:00Z",
        )
        state = self._advance(
            {"publication-candidate": candidate_r2["candidate"]},
            "CANDIDATE_FIXTURE_R2",
            "2026-08-24T00:17:00Z",
        )
        self.assertEqual(state["lifecycle_state"], "RELEASE_CANDIDATE")

        with self.assertRaisesRegex(ValueError, "stale Human Gate request"):
            human_gate.record_publication_preview_approval(
                self.root,
                self.cfg,
                self.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:18:00Z"),
                "review:publication:stale-r1",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )

        state, record_r2, index = human_gate.record_publication_preview_approval(
            self.root,
            self.cfg,
            self.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:19:00Z"),
            "review:publication:r2",
            expected_revision=2,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        self.assertEqual(state["human_gates"]["publication_preview"], "approved")
        self.assertEqual(state["machine_checkpoints"]["publication_preview"], "passed")
        self.assertEqual(state["next_action"], "stage:freeze")
        self.assertIsNone(state["terminal_reason"])
        publication_reviews = [row for row in core.load_json(index)["reviews"] if row["gate"] == "PUBLICATION_PREVIEW"]
        self.assertEqual([(r["revision"], r["decision"]) for r in publication_reviews], [(1, "REQUEST_CHANGES"), (2, "APPROVED")])
        record = core.load_json(record_r2)
        self.assertEqual(record["decision"], "APPROVED")
        candidate_authority = next(row for row in record["reviewed_artifacts"] if row["name"] == "publication-candidate")
        self.assertEqual(candidate_authority["sha256"], core.sha256_file(candidate_r2["candidate"]))

    def test_publication_revision_cannot_cross_architecture_boundary(self) -> None:
        self._advance_to_selection()
        self._reach_architecture_gate("Approved Architecture", "2026-08-24T00:05:00Z")
        human_gate.record_architecture_approval(
            self.root,
            self.cfg,
            self.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:06:00Z"),
            "review:architecture:r1",
            expected_revision=1,
            reviewed_commit_sha=self._snapshot_review_commit(),
        )
        self._reach_publication_gate(1, 10)
        with self.assertRaisesRegex(ValueError, "not allowed for PUBLICATION_PREVIEW"):
            human_gate.request_publication_preview_revision(
                self.root,
                self.cfg,
                self.state_path,
                "SELECTION_COMPLETE",
                "This boundary would improperly reopen Architecture.",
                "human-reviewer",
                core.parse_instant("2026-08-24T00:15:00Z"),
                "review:publication:bad-boundary",
                expected_revision=1,
                reviewed_commit_sha=self._snapshot_review_commit(),
            )


if __name__ == "__main__":
    unittest.main()