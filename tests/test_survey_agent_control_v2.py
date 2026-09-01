from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core


INITIAL_IMPLEMENTATION = "1" * 40


class SurveyAgentControlV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        self._last_artifacts: dict[str, Path] = {}

    def initialize(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path, dict]:
        temp = tempfile.TemporaryDirectory(dir=self.root)
        base = Path(temp.name)
        rel = str(base.relative_to(self.root))
        spec = {
            "issue_id": "SP-AGENT-CONTROL",
            "question": "Can an agent-operated edition adopt reviewed tool improvements without losing provenance?",
            "temporal_mode": "OPEN_HISTORY_AS_OF",
            "as_of": "2026-08-22T09:00:00Z",
            "scope_dimensions": ["tool evolution"],
            "source_root": rel,
            "survey_root": f"{rel}/survey",
            "work_branch": "test/agent-control",
        }
        profile = core.thematic_profile(self.root, self.cfg, spec)
        profile_path, state_path = core.initialize(
            self.root,
            self.cfg,
            profile,
            INITIAL_IMPLEMENTATION,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T09:00:00Z"),
        )
        return temp, profile_path, state_path, profile

    def review_file(
        self,
        base: Path,
        check_id: str,
        *,
        kind: str = "AGENT_RESEARCH",
        cfg: dict | None = None,
    ) -> Path:
        active_cfg = cfg or self.cfg
        state_path = base / active_cfg["state_authority"]["authoritative_filename"]
        state = core.load_json(state_path)
        profile_path = self.root / state["profile"]["path"]
        stage = active_cfg["orchestration"]["stage_plan"][state["lifecycle_state"]]
        artifacts = [
            {
                "name": name,
                "path": str(path.relative_to(self.root)),
                "sha256": core.sha256_file(path),
            }
            for name, path in sorted(self._last_artifacts.items())
        ]
        core_result = base / "review-results" / f"CORE_STAGE_CONTRACT-{state['lifecycle_state']}.json"
        core.write_json(
            core_result,
            {
                "schema_version": "2.0-rc1",
                "check_id": "CORE_STAGE_CONTRACT",
                "status": "PASS",
                "issue_id": state["issue_id"],
                "from_state": state["lifecycle_state"],
                "to_state": stage["next_state"],
                "production_state": {
                    "path": str(state_path.relative_to(self.root)),
                    "sha256": core.sha256_file(state_path),
                },
                "production_profile": {
                    "path": str(profile_path.relative_to(self.root)),
                    "sha256": core.sha256_file(profile_path),
                },
                "implementation_commit_sha": core.repository_commit_sha(self.root),
                "contract": core.contract_identity(
                    self.root,
                    active_cfg,
                    state["research_profile"],
                    state["publication_profile"],
                ),
                "artifacts": artifacts,
                "recorded_at": "2026-08-22T09:05:00Z",
            },
        )
        rows = [
            {
                "check_id": "CORE_STAGE_CONTRACT",
                "kind": "DETERMINISTIC",
                "executor": "survey_stage_validation_v2 fixture",
                "evidence": "fixture deterministic stage-contract validation bound to exact State/Profile/artifacts",
                "result_path": str(core_result.relative_to(self.root)),
            }
        ]
        if check_id != "CORE_STAGE_CONTRACT":
            result_path = None
            if kind == "DETERMINISTIC":
                result = base / "review-results" / f"{check_id}.json"
                core.write_json(result, {"check_id": check_id, "status": "PASS"})
                result_path = str(result.relative_to(self.root))
            rows.append(
                {
                    "check_id": check_id,
                    "kind": kind,
                    "executor": "ChatGPT" if kind != "DETERMINISTIC" else "fixture-validator",
                    "evidence": "reviewed the exact stage outputs and found the stage ready to advance",
                    **({"result_path": result_path} if result_path is not None else {}),
                }
            )
        path = base / "reviews" / f"{check_id}.json"
        core.write_json(path, {"reviews": rows})
        return path

    def artifact_map(self, base: Path, rows: dict[str, str]) -> dict[str, Path]:
        result: dict[str, Path] = {}
        for name, rel in rows.items():
            path = base / rel
            core.write_json(path, {"fixture": name})
            result[name] = path
        self._last_artifacts = dict(result)
        return result

    def test_stage_checkpoint_records_current_implementation_not_initialization_pin(self) -> None:
        temp, _, state_path, profile = self.initialize()
        self.addCleanup(temp.cleanup)
        base = self.root / profile["paths"]["source_root"]
        artifacts = self.artifact_map(base, {"discovery-acceptance": "discovery/discovery-accepted-v2.json"})
        reviews = self.review_file(base, "DISCOVERY_STAGE_REVIEW", kind="DETERMINISTIC")

        checkpoint = agent.build_stage_checkpoint(
            self.root,
            self.cfg,
            state_path,
            artifacts,
            reviews,
            "Discovery research and deterministic intake checks are complete.",
            core.parse_instant("2026-08-22T09:10:00Z"),
        )
        record = core.load_json(checkpoint)
        current_head = core.repository_commit_sha(self.root)
        self.assertNotEqual(current_head, INITIAL_IMPLEMENTATION)
        self.assertEqual(record["implementation"]["repository_commit_sha"], current_head)

        state = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)
        self.assertEqual(state["implementation"]["repository_commit_sha"], INITIAL_IMPLEMENTATION)
        self.assertEqual(state["history"][0]["repository_commit_sha"], INITIAL_IMPLEMENTATION)
        self.assertEqual(state["history"][1]["repository_commit_sha"], current_head)
        self.assertEqual(state["lifecycle_state"], "DISCOVERY_COLLECTED")
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, state), [])

    def test_new_contract_version_can_validate_next_stage_without_rewriting_initial_profile(self) -> None:
        temp, profile_path, state_path, profile = self.initialize()
        self.addCleanup(temp.cleanup)
        base = self.root / profile["paths"]["source_root"]
        discovery = self.artifact_map(base, {"discovery-acceptance": "discovery/discovery-accepted-v2.json"})
        reviews = self.review_file(base, "DISCOVERY_STAGE_REVIEW", kind="DETERMINISTIC")
        first = agent.build_stage_checkpoint(
            self.root, self.cfg, state_path,
            discovery, reviews,
            "Discovery stage reviewed.", core.parse_instant("2026-08-22T09:10:00Z"),
        )
        agent.advance_with_checkpoint(self.root, self.cfg, state_path, first)

        upgraded = copy.deepcopy(self.cfg)
        upgraded["pipeline_contract_version"] = "2.0-rc1+reviewed-tool-upgrade"
        self.assertEqual(agent.validate_agent_state(self.root, upgraded, core.load_json(state_path)), [])
        self.assertEqual(core.load_json(profile_path)["contract"], core.load_json(state_path)["contract"])

        screening = self.artifact_map(base, {"screening-acceptance": "screening/v2/accepted-fixture/screening-accepted.json"})
        reviews2 = self.review_file(base, "SCREENING_STAGE_REVIEW", kind="AGENT_RESEARCH", cfg=upgraded)
        second = agent.build_stage_checkpoint(
            self.root, upgraded, state_path, screening, reviews2,
            "Screening outputs were reviewed using the newer repository contract.",
            core.parse_instant("2026-08-22T09:20:00Z"),
        )
        record = core.load_json(second)
        self.assertEqual(record["contract"]["pipeline_contract_version"], "2.0-rc1+reviewed-tool-upgrade")
        state = agent.advance_with_checkpoint(self.root, upgraded, state_path, second)
        self.assertEqual(state["lifecycle_state"], "CANDIDATES_NORMALIZED")
        self.assertEqual(state["contract"], core.load_json(profile_path)["contract"])
        self.assertEqual(agent.validate_agent_state(self.root, upgraded, state), [])

    def test_compact_checkpoint_cannot_advance_on_review_only_without_stage_authority(self) -> None:
        temp, _, state_path, profile = self.initialize()
        self.addCleanup(temp.cleanup)
        base = self.root / profile["paths"]["source_root"]
        first = agent.build_stage_checkpoint(
            self.root,
            self.cfg,
            state_path,
            self.artifact_map(base, {"discovery-acceptance": "discovery/discovery-accepted-v2.json"}),
            self.review_file(base, "DISCOVERY_STAGE_REVIEW", kind="DETERMINISTIC"),
            "Discovery stage reviewed.",
            core.parse_instant("2026-08-22T09:10:00Z"),
        )
        agent.advance_with_checkpoint(self.root, self.cfg, state_path, first)
        self._last_artifacts = {}
        reviews = self.review_file(base, "SCREENING_REVIEW_WITHOUT_ACCEPTANCE")
        with self.assertRaises(ValueError):
            agent.build_stage_checkpoint(
                self.root,
                self.cfg,
                state_path,
                {},
                reviews,
                "A review statement alone must not advance Screening.",
                core.parse_instant("2026-08-22T09:20:00Z"),
            )
        self.assertEqual(core.load_json(state_path)["lifecycle_state"], "DISCOVERY_COLLECTED")

    def test_normal_progress_stops_at_architecture_human_gate_not_internal_stages(self) -> None:
        temp, _, state_path, profile = self.initialize()
        self.addCleanup(temp.cleanup)
        base = self.root / profile["paths"]["source_root"]
        stages = [
            ("discovery", {"discovery-acceptance": "discovery/discovery-accepted-v2.json"}),
            ("screening", {"screening-acceptance": "screening/v2/accepted-fixture/screening-accepted.json"}),
            (
                "evidence",
                {
                    "evidence-acceptance": "evidence/v2/evidence-accepted.json",
                    "edition-views-acceptance": "evidence/v2/edition-views-accepted.json",
                    "materiality-ledger": "materiality-ledger-v2.json",
                    "profile-completeness": "profile-completeness-v2.json",
                },
            ),
            (
                "selection",
                {
                    "candidate-matrix": "candidate-matrix-v2.json",
                    "candidate-selection": "candidate-selection-v2.json",
                },
            ),
            (
                "architecture",
                {
                    "issue-architecture": "architecture-v2.json",
                    "architecture-review-summary": "architecture-review-summary-v2.json",
                    "architecture-review-attention": "architecture-review-attention-v2.json",
                },
            ),
        ]
        for index, (name, rows) in enumerate(stages, start=1):
            artifacts = self.artifact_map(base, rows)
            reviews = self.review_file(base, f"{name.upper()}_AGENT_REVIEW")
            checkpoint = agent.build_stage_checkpoint(
                self.root, self.cfg, state_path, artifacts, reviews,
                f"{name} stage reviewed by ChatGPT.",
                core.parse_instant(f"2026-08-22T09:{index}0:00Z"),
            )
            state = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)

        self.assertEqual(state["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["next_action"], "ARCHITECTURE_REVIEW")
        self.assertEqual(state["terminal_reason"], "HUMAN_GATE_REACHED")
        self._last_artifacts = {}
        reviews = self.review_file(base, "MUST_NOT_DRAFT_BEFORE_OWNER_APPROVAL")
        with self.assertRaisesRegex(agent.AgentControlError, "cannot advance while State is terminal"):
            agent.build_stage_checkpoint(
                self.root, self.cfg, state_path, {}, reviews,
                "Drafting must not begin before Architecture approval.",
                core.parse_instant("2026-08-22T10:00:00Z"),
            )

    def test_agent_review_cannot_fake_deterministic_result(self) -> None:
        temp, _, state_path, profile = self.initialize()
        self.addCleanup(temp.cleanup)
        base = self.root / profile["paths"]["source_root"]
        discovery = base / "discovery/discovery-accepted-v2.json"
        core.write_json(discovery, {"fixture": "accepted discovery"})
        reviews = base / "reviews/bad.json"
        core.write_json(
            reviews,
            {
                "reviews": [
                    {
                        "check_id": "DISCOVERY_VALIDATOR",
                        "kind": "DETERMINISTIC",
                        "executor": "ChatGPT",
                        "evidence": "claimed a deterministic pass without a result artifact",
                    }
                ]
            },
        )
        with self.assertRaisesRegex(agent.AgentControlError, "requires result_path"):
            agent.build_stage_checkpoint(
                self.root, self.cfg, state_path,
                {"discovery-acceptance": discovery}, reviews,
                "Invalid deterministic claim.", core.parse_instant("2026-08-22T09:10:00Z"),
            )


if __name__ == "__main__":
    unittest.main()
