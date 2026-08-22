from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from scripts import survey_period_v2 as period
from scripts import survey_production_v2 as core


class SurveyPeriodV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)

    def test_configured_month_half_year_and_annual_resolve_to_one_generic_profile(self) -> None:
        now = core.parse_instant("2026-08-22T09:00:00Z")
        cases = [
            ("2026-M07", "monthly", "2026-06-30T15:00:00+00:00", "2026-07-31T14:59:59+00:00"),
            ("2025-H2", "half_year", "2025-06-30T15:00:00+00:00", "2025-12-31T14:59:59+00:00"),
            ("2023-Y", "annual", "2022-12-31T15:00:00+00:00", "2023-12-31T14:59:59+00:00"),
        ]
        for slug, granularity, start, end in cases:
            with self.subTest(slug=slug):
                spec = period.resolve_configured_period(self.root, slug, now)
                self.assertEqual(spec["granularity"], granularity)
                profile = period.period_profile(self.root, self.cfg, spec)
                self.assertEqual(profile["research_profile"], "RETROSPECTIVE_PERIOD")
                self.assertEqual(profile["publication_profile"], "LONGFORM_SPECIAL")
                policy = profile["research_scope"]["temporal_policy"]
                self.assertEqual(policy["mode"], "BOUNDED_PERIOD")
                self.assertEqual(policy["start"], start)
                self.assertEqual(policy["end"], end)
                self.assertEqual(policy["timezone"], "Asia/Tokyo")
                self.assertEqual(len(profile["research_scope"]["initial_obligations"]), 4)

    def test_custom_bounded_period_is_first_class_without_edition_specific_code(self) -> None:
        with tempfile.TemporaryDirectory(dir=self.root) as raw:
            base = Path(raw)
            rel = str(base.relative_to(self.root))
            spec = {
                "issue_id": "SP-CUSTOM-BOUND",
                "start": "2024-02-01T00:00:00+09:00",
                "end": "2024-03-15T23:59:59+09:00",
                "as_of": "2026-08-22T09:00:00Z",
                "timezone": "Asia/Tokyo",
                "question": "What changed across this explicitly bounded custom retrospective?",
                "scope_dimensions": ["coverage", "trajectory"],
                "source_root": rel,
                "survey_root": f"{rel}/survey",
                "work_branch": "special/custom-bound-v2-work",
            }
            profile = period.period_profile(self.root, self.cfg, spec)
            self.assertEqual([row["dimension"] for row in profile["research_scope"]["initial_obligations"]], ["coverage", "trajectory"])
            plan = period.build_plan(self.root, self.cfg, spec)
            self.assertEqual(plan["next_operation"], "INITIALIZE")

    def test_retrospective_period_cannot_initialize_before_period_end(self) -> None:
        spec = {
            "issue_id": "SP-FUTURE-PERIOD",
            "start": "2026-08-01T00:00:00+09:00",
            "end": "2026-08-31T23:59:59+09:00",
            "as_of": "2026-08-22T09:00:00Z",
            "timezone": "Asia/Tokyo",
            "question": "What happened during the full month?",
            "scope_dimensions": ["coverage"],
            "source_root": "sources/SP-FUTURE-PERIOD",
            "survey_root": "surveys/special/FUTURE-PERIOD",
            "work_branch": "special/future-period-v2-work",
        }
        with self.assertRaisesRegex(ValueError, "cannot initialize before its bounded period has ended"):
            period.period_profile(self.root, self.cfg, spec)

    def test_initialized_period_resumes_after_contract_tool_update_without_rematerializing_as_of(self) -> None:
        temp = tempfile.TemporaryDirectory(dir=self.root)
        self.addCleanup(temp.cleanup)
        base = Path(temp.name)
        rel = str(base.relative_to(self.root))
        spec = {
            "issue_id": "SP-PERIOD-RESUME",
            "start": "2025-01-01T00:00:00+09:00",
            "end": "2025-06-30T23:59:59+09:00",
            "as_of": "2026-08-22T09:00:00Z",
            "timezone": "Asia/Tokyo",
            "question": "What mattered across the bounded period?",
            "scope_dimensions": ["coverage", "synthesis"],
            "source_root": rel,
            "survey_root": f"{rel}/survey",
            "work_branch": "special/period-resume-v2-work",
        }
        profile = period.period_profile(self.root, self.cfg, spec)
        profile_path, _ = core.initialize(
            self.root,
            self.cfg,
            profile,
            "1" * 40,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T09:00:00Z"),
        )
        initial_profile = core.load_json(profile_path)

        upgraded = copy.deepcopy(self.cfg)
        upgraded["quality_contract_version"] = "2.0-rc1+reviewed-upgrade"
        later = dict(spec)
        later["as_of"] = "2026-08-29T09:00:00Z"
        plan = period.build_plan(self.root, upgraded, later)
        self.assertEqual(plan["next_operation"], "RESUME")
        self.assertEqual(plan["profile"], initial_profile)
        self.assertEqual(
            plan["profile"]["research_scope"]["temporal_policy"]["as_of"],
            "2026-08-22T09:00:00Z",
        )

    def test_configured_period_does_not_invent_unknown_slug(self) -> None:
        with self.assertRaisesRegex(ValueError, "must resolve exactly once"):
            period.resolve_configured_period(
                self.root, "2099-Y", core.parse_instant("2026-08-22T09:00:00Z")
            )


if __name__ == "__main__":
    unittest.main()
