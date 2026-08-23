from __future__ import annotations

import io
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_production_v2 as core
from scripts import survey_retrospective_profile_v2 as retrospective
from scripts import survey_schema_v2 as schema_gate


class SurveyRetrospectiveProfileV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.cfg = core.load_json(cls.root / core.DEFAULT_CONFIG)
        cls.scope_schema = cls.root / retrospective.SCOPE_SCHEMA

    def scope(self, slug: str, recorded_at: str = "2026-08-23T14:00:00Z") -> dict:
        plan, authority = retrospective.planning_authority(self.root, slug)
        dimensions = ["period coverage", "chronology", "technical synthesis"]
        return {
            "schema_version": "2.0-rc1",
            "issue_id": plan["special_id"],
            "special_slug": slug,
            "planning_authority": authority,
            "question": f"What materially changed in generative AI during {plan['label']}?",
            "inclusion": ["material technical developments inside the configured period"],
            "exclusion": ["later outcomes except where explicitly bounded as hindsight"],
            "scope_dimensions": dimensions,
            "initial_obligations": [
                {
                    "obligation_id": f"period:{index:02d}",
                    "dimension": dimension,
                    "description": f"Establish evidence-backed {dimension} for the configured period.",
                }
                for index, dimension in enumerate(dimensions, start=1)
            ],
            "materialized_by": "ChatGPT",
            "materialized_at": recorded_at,
        }

    def test_scope_schema_accepts_period_materialization(self) -> None:
        schema_gate.validate_instance(self.scope("2024-H1"), self.scope_schema, label="Retrospective scope")

    def test_one_builder_resolves_monthly_half_year_and_annual_configured_periods(self) -> None:
        cases = {
            "2026-M07": ("SP-2026-M07", "2026-07-01T00:00:00Z", "2026-07-31T23:59:59Z"),
            "2024-H1": ("SP-2024-H1", "2024-01-01T00:00:00Z", "2024-06-30T23:59:59Z"),
            "2023-Y": ("SP-2023-Y", "2023-01-01T00:00:00Z", "2023-12-31T23:59:59Z"),
        }
        recorded_at = core.parse_instant("2026-08-23T14:00:00Z")
        for slug, (issue_id, start, end) in cases.items():
            with self.subTest(slug=slug):
                profile = retrospective.build_profile(self.root, self.cfg, self.scope(slug), recorded_at)
                self.assertEqual(profile["issue_id"], issue_id)
                self.assertEqual(profile["research_profile"], "RETROSPECTIVE_PERIOD")
                self.assertEqual(profile["publication_profile"], "LONGFORM_SPECIAL")
                self.assertEqual(profile["research_scope"]["temporal_policy"], {
                    "mode": "BOUNDED_PERIOD",
                    "start": start,
                    "end": end,
                    "as_of": "2026-08-23T14:00:00Z",
                    "timezone": "UTC",
                })
                self.assertEqual(profile["paths"], {
                    "source_root": f"sources/{issue_id}",
                    "survey_root": f"surveys/special/{slug}",
                    "work_branch": f"special/{slug}-work",
                })
                self.assertEqual(core.validate_profile(profile, self.cfg), [])

    def test_profile_rejects_stale_or_forged_configured_period_authority(self) -> None:
        scope = self.scope("2024-H1")
        scope["planning_authority"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "configured-period authority bytes"):
            retrospective.build_profile(
                self.root,
                self.cfg,
                scope,
                core.parse_instant("2026-08-23T14:00:00Z"),
            )

        scope = self.scope("2024-H1")
        scope["issue_id"] = "SP-2024-H2"
        with self.assertRaisesRegex(ValueError, "issue_id differs"):
            retrospective.build_profile(
                self.root,
                self.cfg,
                scope,
                core.parse_instant("2026-08-23T14:00:00Z"),
            )

    def test_profile_rejects_initialization_before_period_end_or_before_scope_materialization(self) -> None:
        with self.assertRaisesRegex(ValueError, "before configured period end"):
            retrospective.build_profile(
                self.root,
                self.cfg,
                self.scope("2026-M07", recorded_at="2026-07-15T00:00:00Z"),
                core.parse_instant("2026-07-15T00:00:00Z"),
            )

        scope = self.scope("2024-H1")
        scope["materialized_at"] = "2026-08-24T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "dated after initialization"):
            retrospective.build_profile(
                self.root,
                self.cfg,
                scope,
                core.parse_instant("2026-08-23T14:00:00Z"),
            )

    def test_profile_rejects_uncovered_scope_dimension_through_core_contract(self) -> None:
        scope = self.scope("2024-H1")
        scope["initial_obligations"] = scope["initial_obligations"][:-1]
        with self.assertRaisesRegex(ValueError, "do not cover Profile dimensions"):
            retrospective.build_profile(
                self.root,
                self.cfg,
                scope,
                core.parse_instant("2026-08-23T14:00:00Z"),
            )

    def test_plan_scope_exposes_required_period_guides_without_authored_taxonomy(self) -> None:
        half = retrospective.plan_scope(self.root, "2024-H1", core.parse_instant("2026-08-23T14:00:00Z"))
        annual = retrospective.plan_scope(self.root, "2023-Y", core.parse_instant("2026-08-23T14:00:00Z"))
        monthly = retrospective.plan_scope(self.root, "2026-M07", core.parse_instant("2026-08-23T14:00:00Z"))
        self.assertIn("docs/half-year-retrospective-specials.md", half["required_guides"])
        self.assertIn("docs/annual-retrospective-specials.md", annual["required_guides"])
        self.assertNotIn("docs/half-year-retrospective-specials.md", monthly["required_guides"])
        self.assertNotIn("scope_dimensions", half)
        self.assertIn("ChatGPT reads the configured period and required guides", half["instruction"])

    def test_unconfigured_period_is_not_invented(self) -> None:
        with self.assertRaisesRegex(ValueError, "not configured"):
            retrospective.plan_scope(self.root, "2099-Y", core.parse_instant("2099-12-31T23:59:59Z"))

    def test_cli_invalid_recorded_at_fails_closed_without_traceback(self) -> None:
        stderr = io.StringIO()
        with mock.patch.object(
            retrospective.sys,
            "argv",
            [
                "survey_retrospective_profile_v2.py",
                "plan",
                "--special-slug",
                "2024-H1",
                "--recorded-at",
                "not-a-timestamp",
            ],
        ), mock.patch.object(retrospective.sys, "stderr", stderr):
            self.assertEqual(retrospective.main(), 2)
        self.assertTrue(stderr.getvalue().strip())
        self.assertNotIn("Traceback", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
