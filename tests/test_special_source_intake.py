import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "special_source_intake.py"
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location("special_source_intake", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


PLAN = {
    "issue_id": "SP-2024-H2",
    "edition_kind": "RETROSPECTIVE_PERIOD",
    "collection_window_start": "2024-07-01T00:00:00Z",
    "collection_window_end": "2024-12-31T23:59:59Z",
}

CFG = {
    "coverage_policy": {
        "base_intake_role": "BROAD_SEED_NOT_EXHAUSTIVE",
        "retrospective_period_requires_coverage_audit": True,
        "long_window_partition_threshold_days": 45,
    },
    "arxiv": {"enabled": True, "max_results_per_query": 200},
    "github_releases": {"enabled": True},
    "official_pages": {"enabled": True},
}


def fake_run(plan, collector):
    return {
        "run_id": f"{collector}-{plan['collection_window_start']}",
        "collector": {"id": collector},
        "status": "success",
        "outputs": [],
    }


class SpecialSourceIntakeTests(unittest.TestCase):
    def test_calendar_month_slices_cover_half_year(self):
        start = module.base.parse_instant(PLAN["collection_window_start"])
        end = module.base.parse_instant(PLAN["collection_window_end"])
        slices = module.calendar_month_slices(start, end)
        self.assertEqual(len(slices), 6)
        self.assertEqual(module.base.iso_utc(slices[0][0]), "2024-07-01T00:00:00Z")
        self.assertEqual(module.base.iso_utc(slices[0][1]), "2024-07-31T23:59:59Z")
        self.assertEqual(module.base.iso_utc(slices[-1][0]), "2024-12-01T00:00:00Z")
        self.assertEqual(module.base.iso_utc(slices[-1][1]), "2024-12-31T23:59:59Z")

    def test_long_retrospective_partitions_arxiv_but_not_other_collectors(self):
        arxiv_plans = []
        github_plans = []
        official_plans = []

        def arxiv(plan, cfg, output_root):
            arxiv_plans.append(dict(plan))
            return fake_run(plan, "arxiv-api")

        def github(plan, cfg, output_root):
            github_plans.append(dict(plan))
            return fake_run(plan, "github-releases")

        def official(plan, cfg, output_root):
            official_plans.append(dict(plan))
            return fake_run(plan, "official-pages")

        with tempfile.TemporaryDirectory() as td, \
             patch.object(module.base, "run_arxiv", side_effect=arxiv), \
             patch.object(module.base, "run_github_releases", side_effect=github), \
             patch.object(module.base, "run_official_pages", side_effect=official), \
             patch.object(module, "arxiv_cap_observations", return_value=[]):
            report = module.run(PLAN, CFG, Path(td), "all")

        self.assertEqual(len(arxiv_plans), 6)
        self.assertEqual(len(github_plans), 1)
        self.assertEqual(len(official_plans), 1)
        self.assertEqual(github_plans[0]["collection_window_start"], PLAN["collection_window_start"])
        self.assertEqual(github_plans[0]["collection_window_end"], PLAN["collection_window_end"])
        self.assertEqual(report["overall_status"], "success")
        self.assertEqual(report["coverage"]["arxiv_temporal_partition"], "CALENDAR_MONTH")
        self.assertEqual(len(report["coverage"]["arxiv_slices"]), 6)
        self.assertTrue(report["coverage"]["coverage_audit_required"])

    def test_short_retrospective_window_is_not_partitioned(self):
        plan = dict(PLAN)
        plan["collection_window_start"] = "2024-12-01T00:00:00Z"
        plan["collection_window_end"] = "2024-12-31T23:59:59Z"
        arxiv_plans = []

        def arxiv(p, cfg, output_root):
            arxiv_plans.append(dict(p))
            return fake_run(p, "arxiv-api")

        with tempfile.TemporaryDirectory() as td, \
             patch.object(module.base, "run_arxiv", side_effect=arxiv), \
             patch.object(module, "arxiv_cap_observations", return_value=[]):
            report = module.run(plan, CFG, Path(td), "arxiv")

        self.assertEqual(len(arxiv_plans), 1)
        self.assertEqual(report["coverage"]["arxiv_temporal_partition"], "NONE")


if __name__ == "__main__":
    unittest.main()
