from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_profiled_freeze_v2 as profiled


class SurveyProfiledFreezeV2Tests(unittest.TestCase):
    def profile(self, issue_id: str, research_profile: str, publication_profile: str, survey_root: str) -> dict:
        return {
            "issue_id": issue_id,
            "research_profile": research_profile,
            "publication_profile": publication_profile,
            "paths": {"survey_root": survey_root},
        }

    def test_retrospective_internal_id_preserves_existing_public_special_slug(self) -> None:
        profile = self.profile(
            "SP-2025-H2", "RETROSPECTIVE_PERIOD", "LONGFORM_SPECIAL", "surveys/special/2025-H2"
        )
        self.assertEqual(profiled.public_issue_slug(profile), "2025-H2")
        self.assertEqual(profiled.release_identity(profile), "special/2025-H2")

    def test_thematic_and_weekly_public_identity_remain_natural(self) -> None:
        thematic = self.profile("SP001", "THEMATIC", "LONGFORM_SPECIAL", "surveys/special/SP001")
        weekly = self.profile("2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", "surveys/weekly/2026-W35")
        self.assertEqual(profiled.release_identity(thematic), "special/SP001")
        self.assertEqual(profiled.release_identity(weekly), "weekly/2026-W35")

    def test_release_workflow_rederives_tag_title_and_asset_from_profile_slug(self) -> None:
        text = Path(".github/workflows/survey-production-v2-release.yml").read_text(encoding="utf-8")
        self.assertIn("from scripts import survey_profiled_freeze_v2 as profiled", text)
        self.assertIn("public_slug=profiled.public_issue_slug(profile)", text)
        self.assertIn("expected_tag=profiled.release_identity(profile)", text)
        self.assertIn("if tag != expected_tag", text)
        self.assertIn("Technical Survey Special — {public_slug}", text)
        self.assertIn("Technical_Survey_Special_{public_slug}.pdf", text)
        self.assertNotIn("if tag not in {f'weekly/{issue}',f'special/{issue}'}", text)


if __name__ == "__main__":
    unittest.main()
