from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_execution_record_v2 as execution


class SurveyExecutionRecordV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.profile_path = self.root / "sources/2026-W35/production-profile.json"
        self.state_path = self.root / "sources/2026-W35/production-state.json"
        self.profile_path.parent.mkdir(parents=True, exist_ok=True)
        self.profile_path.write_text("{}\n", encoding="utf-8")
        self.state_path.write_text("{\"fixture\":true}\n", encoding="utf-8")
        self.profile = {
            "issue_id": "2026-W35",
            "research_profile": "WEEKLY",
            "publication_profile": "WEEKLY_MAGAZINE",
            "paths": {
                "source_root": "sources/2026-W35",
                "survey_root": "surveys/weekly/2026-W35",
                "work_branch": "weekly/2026-W35-v2-work",
            },
        }
        self.state = {
            "issue_id": "2026-W35",
            "lifecycle_state": "ISSUE_INITIALIZED",
            "terminal_reason": None,
            "next_action": "stage:discovery",
            "human_gates": {
                "architecture_review": "pending",
                "publication_preview": "pending",
            },
        }
        self.cfg = {
            "external_source_intake": {
                "x_grok": {"profile_policy": {"WEEKLY": "REQUIRED_BY_PROFILE"}}
            }
        }

    def patches(self):
        return (
            mock.patch.object(execution, "_load_profile", return_value=(self.profile_path, self.profile)),
            mock.patch.object(execution, "_load_state", return_value=(self.state_path, self.state)),
        )

    def initialize(self):
        profile_patch, state_patch = self.patches()
        with profile_patch, state_patch:
            return execution.initialize(
                self.root,
                self.cfg,
                self.profile_path,
                self.state_path,
                session_id="2026-08-23T1849-JST-source-intake",
                started_at="2026-08-23T18:49:00+09:00",
                main_sha="a" * 40,
                branch_head="b" * 40,
                objective="Compile the Weekly autonomously to Architecture Review.",
                requested_stop="ARCHITECTURE_REVIEW",
            )

    def validate(self):
        profile_patch, state_patch = self.patches()
        with profile_patch, state_patch:
            return execution.validate(self.root, self.cfg, self.profile_path, self.state_path)

    def test_initialize_creates_canonical_tree_and_required_navigation(self) -> None:
        index, session = self.initialize()
        self.assertTrue(index.is_file())
        self.assertTrue(session.is_file())
        root = index.parent
        for name in execution.REQUIRED_DIRS:
            self.assertTrue((root / name).is_dir())
        index_text = index.read_text(encoding="utf-8")
        self.assertIn("`2026-W35`", index_text)
        self.assertIn("`WEEKLY`", index_text)
        self.assertIn("`WEEKLY_MAGAZINE`", index_text)
        self.assertIn("`weekly/2026-W35-v2-work`", index_text)
        self.assertIn("REQUIRED_BY_PROFILE", index_text)
        self.assertIn(f"`{execution._rel(self.root, self.state_path)}`", index_text)
        self.assertEqual(self.validate(), [])

    def test_initialize_is_non_destructive(self) -> None:
        self.initialize()
        profile_patch, state_patch = self.patches()
        with profile_patch, state_patch, self.assertRaisesRegex(ValueError, "execution index already exists"):
            execution.initialize(
                self.root,
                self.cfg,
                self.profile_path,
                self.state_path,
                session_id="2026-08-23T1900-JST-resume",
                started_at="2026-08-23T19:00:00+09:00",
                main_sha="a" * 40,
                branch_head="b" * 40,
                objective="Resume production.",
                requested_stop="ARCHITECTURE_REVIEW",
            )

    def test_unlisted_session_is_detected_instead_of_fragmenting_history(self) -> None:
        index, session = self.initialize()
        second = session.parent / "2026-08-23T2000-JST-resume.md"
        second.write_text(session.read_text(encoding="utf-8"), encoding="utf-8")
        errors = self.validate()
        self.assertTrue(any("does not list session" in error for error in errors), errors)
        index.write_text(
            index.read_text(encoding="utf-8") + "\n- `sessions/2026-08-23T2000-JST-resume.md`\n",
            encoding="utf-8",
        )
        self.assertEqual(self.validate(), [])

    def test_review_and_shared_core_defect_records_require_policy_headings(self) -> None:
        index, _ = self.initialize()
        review = index.parent / "reviews/architecture-r1.md"
        defect = index.parent / "defects/core-001.md"
        review.write_text("# review\n\n## Human decision\n", encoding="utf-8")
        defect.write_text("# defect\n\n## Observation\n", encoding="utf-8")
        errors = self.validate()
        self.assertTrue(any("architecture-r1.md missing required heading" in error for error in errors), errors)
        self.assertTrue(any("core-001.md missing required heading" in error for error in errors), errors)

    def test_unsafe_session_identity_and_commit_identity_fail_closed(self) -> None:
        profile_patch, state_patch = self.patches()
        with profile_patch, state_patch, self.assertRaisesRegex(ValueError, "session_id"):
            execution.initialize(
                self.root,
                self.cfg,
                self.profile_path,
                self.state_path,
                session_id="../escape",
                started_at="2026-08-23T18:49:00+09:00",
                main_sha="a" * 40,
                branch_head="b" * 40,
                objective="fixture",
                requested_stop="ARCHITECTURE_REVIEW",
            )
        profile_patch, state_patch = self.patches()
        with profile_patch, state_patch, self.assertRaisesRegex(ValueError, "main_sha"):
            execution.initialize(
                self.root,
                self.cfg,
                self.profile_path,
                self.state_path,
                session_id="safe-session",
                started_at="2026-08-23T18:49:00+09:00",
                main_sha="not-a-sha",
                branch_head="b" * 40,
                objective="fixture",
                requested_stop="ARCHITECTURE_REVIEW",
            )


if __name__ == "__main__":
    unittest.main()
