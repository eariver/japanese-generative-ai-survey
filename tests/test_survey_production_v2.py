from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as v2


IMPLEMENTATION_SHA = "1" * 40
OTHER_IMPLEMENTATION_SHA = "2" * 40


class SurveyProductionV2FoundationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(".").resolve()
        self.cfg = v2.load_json(self.repo_root / "config/survey-production-v2.json")

    def make_sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source_cfg = v2.load_json(self.repo_root / "config/survey-production-v2.json")
        required = [
            "config/survey-production-v2.json",
            "config/weekly-pipeline.json",
            "schemas/survey-production-profile.schema.json",
            "schemas/survey-production-state.schema.json",
            *source_cfg["contract_files"]["pipeline"],
            *source_cfg["contract_files"]["quality"],
        ]
        for rel in dict.fromkeys(required):
            src = self.repo_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return temp, root

    def test_contract_manifest_declares_two_human_gates_and_non_authoritative_legacy_state(self) -> None:
        self.assertEqual(self.cfg["human_gates"], ["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"])
        self.assertEqual(self.cfg["state_authority"]["authoritative_filename"], "production-state.json")
        self.assertEqual(self.cfg["state_authority"]["legacy_mode"], "NON_AUTHORITATIVE_READ_ONLY")
        self.assertFalse("CANDIDATE_SELECTION" in self.cfg["human_gates"])

    def test_weekly_profile_uses_existing_cutoff_logic_and_resolves_w33_before_cutoff(self) -> None:
        now = v2.parse_instant("2026-08-22T02:00:00+09:00")
        profile = v2.weekly_profile(self.repo_root, self.cfg, now, "2026-W33")
        policy = profile["research_scope"]["temporal_policy"]
        self.assertEqual(profile["research_profile"], "WEEKLY")
        self.assertEqual(profile["publication_profile"], "WEEKLY_MAGAZINE")
        self.assertEqual(policy["mode"], "ROLLING_WINDOW")
        self.assertEqual(policy["timezone"], "America/New_York")
        self.assertTrue(policy["window_start"].endswith("-04:00"))
        self.assertTrue(policy["window_end"].endswith("-04:00"))
        self.assertEqual(policy["window_end"], policy["cutoff"])

    def test_weekly_profile_refuses_future_issue_before_cutoff(self) -> None:
        now = v2.parse_instant("2026-08-22T02:00:00+09:00")
        with self.assertRaisesRegex(ValueError, "does not match current completed cutoff"):
            v2.weekly_profile(self.repo_root, self.cfg, now, "2026-W34")

    def test_thematic_profile_has_no_fake_bounded_window(self) -> None:
        spec = {
            "issue_id": "SP001",
            "question": "How did Chinese generative AI ecosystems emerge and differentiate?",
            "temporal_mode": "OPEN_HISTORY_AS_OF",
            "as_of": "2026-08-22T02:00:00+09:00",
            "inclusion": ["major model and developer ecosystems"],
            "exclusion": ["policy-only material without technical relevance"],
            "scope_dimensions": ["lineage", "distribution", "reasoning", "coding"],
        }
        profile = v2.thematic_profile(self.repo_root, self.cfg, spec)
        policy = profile["research_scope"]["temporal_policy"]
        self.assertEqual(profile["research_profile"], "THEMATIC")
        self.assertEqual(policy["mode"], "OPEN_HISTORY_AS_OF")
        self.assertEqual(set(policy), {"mode", "as_of"})
        self.assertNotIn("start", policy)
        self.assertNotIn("end", policy)
        self.assertNotIn("window_start", policy)
        self.assertNotIn("window_end", policy)

    def test_thematic_profile_rejects_bounded_period_mode(self) -> None:
        spec = {
            "issue_id": "SP001",
            "question": "test",
            "temporal_mode": "BOUNDED_PERIOD",
            "as_of": "2026-08-22T02:00:00+09:00",
        }
        with self.assertRaisesRegex(ValueError, "OPEN_HISTORY_AS_OF or CURRENT_STATE_AS_OF"):
            v2.thematic_profile(self.repo_root, self.cfg, spec)

    def test_initialize_is_non_destructive_and_records_separate_identities(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        spec = {
            "issue_id": "SP001",
            "question": "test thematic question",
            "temporal_mode": "CURRENT_STATE_AS_OF",
            "as_of": "2026-08-22T02:00:00+09:00",
        }
        profile = v2.thematic_profile(root, cfg, spec)
        profile_path, state_path = v2.initialize(
            root,
            cfg,
            profile,
            IMPLEMENTATION_SHA,
            "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)
        self.assertEqual(state["profile"]["sha256"], v2.sha256_file(profile_path))
        self.assertEqual(state["implementation"]["repository_commit_sha"], IMPLEMENTATION_SHA)
        self.assertEqual(state["contract"], profile["contract"])
        self.assertNotEqual(state["contract"]["pipeline_contract_sha256"], state["profile"]["sha256"])
        with self.assertRaisesRegex(ValueError, "refusing destructive"):
            v2.initialize(
                root,
                cfg,
                profile,
                IMPLEMENTATION_SHA,
                "ARCHITECTURE_REVIEW",
                v2.parse_instant("2026-08-22T02:06:00+09:00"),
            )

    def test_transition_is_exactly_one_step_and_rejects_implementation_drift(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "test",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T02:00:00+09:00",
            },
        )
        _, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW", v2.parse_instant("2026-08-22T02:05:00+09:00")
        )
        state = v2.load_json(state_path)
        advanced = v2.transition_state(
            root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:10:00+09:00")
        )
        self.assertEqual(advanced["lifecycle_state"], "DISCOVERY_COLLECTED")
        with self.assertRaisesRegex(ValueError, "exactly one forward step"):
            v2.transition_state(
                root, cfg, state, "EVIDENCE_REVIEWED", IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:11:00+09:00")
            )
        with self.assertRaisesRegex(ValueError, "implementation commit differs"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", OTHER_IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:12:00+09:00")
            )

    def test_transition_rejects_profile_contract_and_legacy_drift(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        source_root = root / "sources/SP001"
        source_root.mkdir(parents=True, exist_ok=True)
        legacy_path = source_root / "pipeline-state.json"
        legacy_path.write_text('{"legacy": 1}\n', encoding="utf-8")
        profile = v2.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "test",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T02:00:00+09:00",
            },
        )
        profile_path, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW", v2.parse_instant("2026-08-22T02:05:00+09:00")
        )
        state = v2.load_json(state_path)
        self.assertTrue(state["legacy_compatibility"]["legacy_state_present"])

        legacy_path.write_text('{"legacy": 2}\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "legacy compatibility artifact changed"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:10:00+09:00")
            )

        legacy_path.write_text('{"legacy": 1}\n', encoding="utf-8")
        changed_profile = json.loads(profile_path.read_text(encoding="utf-8"))
        changed_profile["research_scope"]["question"] = "changed after initialization"
        profile_path.write_text(json.dumps(changed_profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "profile bytes changed"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:11:00+09:00")
            )

    def test_transition_rejects_contract_file_drift(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "test",
                "temporal_mode": "CURRENT_STATE_AS_OF",
                "as_of": "2026-08-22T02:00:00+09:00",
            },
        )
        _, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW", v2.parse_instant("2026-08-22T02:05:00+09:00")
        )
        state = v2.load_json(state_path)
        contract_path = root / "docs/survey-production-core-v2-authority.md"
        contract_path.write_text(contract_path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "semantic contract files differ"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA, v2.parse_instant("2026-08-22T02:10:00+09:00")
            )


if __name__ == "__main__":
    unittest.main()
