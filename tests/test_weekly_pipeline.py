from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from scripts import weekly_pipeline as wp


CONFIG = {
    "editorial": {
        "cutoff_timezone": "America/New_York",
        "cutoff_weekday": "FRIDAY",
        "cutoff_hour": 18,
        "cutoff_minute": 0,
        "compilation_timezone": "Asia/Tokyo",
    }
}


class WeeklyPipelineCalendarTests(unittest.TestCase):
    def test_edt_cutoff_and_issue_id(self) -> None:
        now = wp.parse_instant("2026-08-08T00:00:00Z")
        cutoff = wp.latest_cutoff(now, CONFIG)
        self.assertEqual(cutoff.isoformat(), "2026-08-07T18:00:00-04:00")
        self.assertEqual(wp.issue_id_from_cutoff(cutoff), "2026-W32")

    def test_est_cutoff_uses_new_york_timezone_not_fixed_offset(self) -> None:
        now = wp.parse_instant("2026-12-05T01:00:00Z")
        cutoff = wp.latest_cutoff(now, CONFIG)
        self.assertEqual(cutoff.isoformat(), "2026-12-04T18:00:00-05:00")

    def test_plan_carries_previous_collection_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state = root / "sources" / "2026-W32" / "pipeline-state.json"
            state.parent.mkdir(parents=True)
            state.write_text(
                json.dumps(
                    {
                        "calendar": {
                            "collection_anchor_at": "2026-08-09T23:40:00+09:00"
                        }
                    }
                ),
                encoding="utf-8",
            )
            plan = wp.build_plan(
                root,
                CONFIG,
                wp.parse_instant("2026-08-15T10:00:00+09:00"),
            )
            self.assertEqual(plan["issue_id"], "2026-W33")
            self.assertEqual(
                plan["editorial_cutoff"], "2026-08-14T18:00:00-04:00"
            )
            self.assertEqual(
                plan["collection_window_start"], "2026-08-09T23:40:00+09:00"
            )

    def test_named_bootstrap_issue_replays_its_committed_window(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state = root / "sources" / "2026-W32" / "pipeline-state.json"
            state.parent.mkdir(parents=True)
            state.write_text(
                json.dumps(
                    {
                        "issue_id": "2026-W32",
                        "calendar": {
                            "editorial_cutoff": "2026-08-07T18:00:00-04:00",
                            "cutoff_timezone": "America/New_York",
                            "collection_window_start": "2026-08-01T00:00:00-04:00",
                            "collection_anchor_at": "2026-08-09T23:40:00+09:00",
                        },
                    }
                ),
                encoding="utf-8",
            )
            plan = wp.build_plan_for_issue(
                root,
                CONFIG,
                wp.parse_instant("2026-08-10T14:23:28+09:00"),
                "2026-W32",
            )
            self.assertEqual(plan["issue_id"], "2026-W32")
            self.assertEqual(plan["plan_source"], "pipeline-state")
            self.assertEqual(plan["automation_mode"], "historical-replay")
            self.assertEqual(
                plan["collection_window_start"], "2026-08-01T00:00:00-04:00"
            )
            self.assertEqual(
                plan["collection_window_end"], "2026-08-09T23:40:00+09:00"
            )

    def test_named_current_issue_prefers_rolling_previous_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state = root / "sources" / "2026-W32" / "pipeline-state.json"
            state.parent.mkdir(parents=True)
            state.write_text(
                json.dumps(
                    {
                        "calendar": {
                            "collection_anchor_at": "2026-08-09T23:40:00+09:00"
                        }
                    }
                ),
                encoding="utf-8",
            )
            plan = wp.build_plan_for_issue(
                root,
                CONFIG,
                wp.parse_instant("2026-08-15T10:00:00+09:00"),
                "2026-W33",
            )
            self.assertEqual(plan["plan_source"], "latest-cutoff")
            self.assertEqual(
                plan["collection_window_start"], "2026-08-09T23:40:00+09:00"
            )

    def test_init_rejects_future_issue_id_instead_of_relabeling_current_cutoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = SimpleNamespace(
                repo_root=str(root),
                now="2026-08-10T19:00:00+09:00",
                issue_id="2026-W33",
                force=False,
            )
            self.assertEqual(wp.cmd_init(args, CONFIG), 2)
            self.assertFalse((root / "sources" / "2026-W33" / "pipeline-state.json").exists())

    def test_init_allows_current_issue_assertion_and_preserves_derived_cutoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = SimpleNamespace(
                repo_root=str(root),
                now="2026-08-10T19:00:00+09:00",
                issue_id="2026-W32",
                force=False,
            )
            self.assertEqual(wp.cmd_init(args, CONFIG), 0)
            state_path = root / "sources" / "2026-W32" / "pipeline-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["issue_id"], "2026-W32")
            self.assertEqual(state["calendar"]["editorial_cutoff"], "2026-08-07T18:00:00-04:00")


class WeeklyPipelineValidationTests(unittest.TestCase):
    def _write(self, root: Path, relative: str, content: str = "x") -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_selection_does_not_require_paper_watch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            self._write(root, f"sources/{issue}/pipeline-state.json", "{}")
            self._write(root, f"sources/{issue}/manifest.yaml")
            self._write(root, f"sources/{issue}/candidates/index.yaml")
            self._write(root, f"sources/{issue}/candidate-selection.yaml")

            report, passed = wp.validate(root, issue, "selection")
            self.assertTrue(passed, report)
            paper_check = next(
                check for check in report["checks"] if check["name"] == "paper_evidence"
            )
            self.assertFalse(paper_check["passed"])

    def test_only_explicit_internal_page_numbers_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            section = root / "surveys" / "weekly" / issue / "sections" / "10-test.tex"
            section.parent.mkdir(parents=True)
            section.write_text(
                "論文のp.3を参照する。\\nただし今号p.3--4のような直書きは避ける。",
                encoding="utf-8",
            )

            findings = wp.internal_page_reference_findings(root, issue)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]["text"], "今号p.3--4")


if __name__ == "__main__":
    unittest.main()
