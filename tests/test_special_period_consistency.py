from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import special_period_consistency as period
from scripts import special_period_consistency_retrospective as retrospective_period


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialPeriodConsistencyTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        dump(
            root / "specials/2026-M06/edition.json",
            {
                "special_id": "SP-2026-M06",
                "special_slug": "2026-M06",
                "coverage": {
                    "start": "2026-06-01T00:00:00Z",
                    "end": "2026-06-30T23:59:59Z",
                    "timezone": "UTC",
                },
            },
        )
        source = root / "surveys/special/2026-M06/revisions/v0.1"
        source.mkdir(parents=True)
        (source / "sections").mkdir()
        (source / "sections/00-frontmatter.tex").write_text(
            "\\begin{claimboundary}[Retrospective scope]\n"
            "本号は2026年7月を、後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。"
            "本文では7月の一般提供など正当な翌月chronologyを言及してよい。\n"
            "\\end{claimboundary}\n",
            encoding="utf-8",
        )
        (source / "main.tex").write_text(
            "\\surveysetup\n"
            "  {SP-2026-M06}\n"
            "  {Japanese Generative AI Technical Survey Special}\n"
            "  {Special / Coverage 2026-06-01 -- 2026-06-30 / Retrospective as of 2026-08-11}\n"
            "  {Coverage window: 2026-06-01 -- 2026-06-30 UTC}\n",
            encoding="utf-8",
        )
        manifest_path = source / "source-manifest.json"
        dump(
            manifest_path,
            {
                "issue_id": "SP-2026-M06",
                "special_slug": "2026-M06",
                "source_version": "v0.1",
                "frontmatter": {"path": "sections/00-frontmatter.tex", "sha256": sha(source / "sections/00-frontmatter.tex")},
                "main_tex": {"path": "main.tex", "sha256": sha(source / "main.tex")},
            },
        )
        dump(
            root / "sources/SP-2026-M06/pipeline-state.json",
            {
                "provenance": {
                    "validated_issue_source": {
                        "path": "surveys/special/2026-M06/revisions/v0.1/source-manifest.json",
                        "sha256": sha(manifest_path),
                        "source_version": "v0.1",
                    }
                }
            },
        )
        return td, root

    def test_apply_corrects_only_structured_scope_period(self) -> None:
        td, root = self.make_repo()
        self.addCleanup(td.cleanup)
        report = period.apply_scope_period(root, "SP-2026-M06", "2026-M06")
        self.assertTrue(report["passed"])
        self.assertTrue(report["changed"])
        text = (root / "surveys/special/2026-M06/revisions/v0.1/sections/00-frontmatter.tex").read_text(encoding="utf-8")
        self.assertIn("本号は2026年6月を後日確認可能", text)
        self.assertIn("7月の一般提供", text, "legitimate adjacent-month chronology must not be globally replaced")

    def test_check_rejects_wrong_scope_month(self) -> None:
        td, root = self.make_repo()
        self.addCleanup(td.cleanup)
        report = period.check_structured_periods(root, "SP-2026-M06", "2026-M06")
        self.assertFalse(report["passed"])
        self.assertTrue(any("Retrospective scope period mismatch" in e for e in report["errors"]))

    def test_single_month_coverage_is_derived_from_manifest(self) -> None:
        value = period.derive_period(
            {"coverage": {"start": "2026-11-01T00:00:00+09:00", "end": "2026-11-30T23:59:59+09:00"}}
        )
        self.assertEqual(value["year_month"], "2026-11")
        self.assertEqual(value["ja"], "2026年11月")

    def test_retrospective_wrapper_preserves_monthly_display_label(self) -> None:
        value = retrospective_period.derive_period(
            {
                "display_label": "2026年6月 Retrospective",
                "coverage": {"start": "2026-06-01T00:00:00Z", "end": "2026-06-30T23:59:59Z"},
            }
        )
        self.assertEqual(value["label"], "2026年6月")
        self.assertEqual(value["year_month"], "2026-06")

    def test_retrospective_wrapper_accepts_half_year_display_label(self) -> None:
        value = retrospective_period.derive_period(
            {
                "display_label": "2025年後期 Retrospective",
                "coverage": {"start": "2025-07-01T00:00:00Z", "end": "2025-12-31T23:59:59Z"},
            }
        )
        self.assertEqual(value["label"], "2025年後期")
        self.assertEqual(value["start_date"], "2025-07-01")
        self.assertEqual(value["end_date"], "2025-12-31")
        self.assertNotIn("year_month", value)

    def test_signal_heading_is_monthly_by_default(self) -> None:
        self.assertEqual(retrospective_period.signal_section_title({}), "Monthly Signals")
        self.assertEqual(
            retrospective_period.signal_section_title({"edition_kind": "RETROSPECTIVE_MONTH"}),
            "Monthly Signals",
        )

    def test_signal_heading_is_retrospective_for_period_special(self) -> None:
        self.assertEqual(
            retrospective_period.signal_section_title({"edition_kind": "RETROSPECTIVE_PERIOD"}),
            "Retrospective Signals",
        )


if __name__ == "__main__":
    unittest.main()
