import importlib.util
import sys
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "weekly_source_intake.py"
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location("weekly_source_intake", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


PLAN = {
    "issue_id": "2026-W33",
    "editorial_cutoff": "2026-08-14T18:00:00-04:00",
    "collection_window_start": "2026-08-07T18:00:00-04:00",
    "collection_window_end": "2026-08-14T18:00:00-04:00",
}

CFG = {
    "coverage_policy": {
        "base_intake_role": "BROAD_SEED_NOT_EXHAUSTIVE",
        "weekly_requires_coverage_audit": True,
        "weekly_arxiv_initial_slices": 2,
        "weekly_arxiv_min_slice_minutes": 360,
    },
    "arxiv": {"enabled": True, "max_results_per_query": 200},
    "github_releases": {"enabled": True},
    "official_pages": {"enabled": True},
}


def fake_run(plan, collector):
    return {
        "run_id": f"{collector}-{plan['collection_window_start']}-{plan['collection_window_end']}",
        "collector": {"id": collector},
        "status": "success",
        "outputs": [],
    }


class WeeklySourceIntakeTests(unittest.TestCase):
    def test_two_initial_slices_cover_exact_cutoff_window(self):
        start = module.base.parse_instant(PLAN["collection_window_start"])
        end = module.base.parse_instant(PLAN["collection_window_end"])
        slices = module.partition_evenly(start, end, 2)
        self.assertEqual(len(slices), 2)
        self.assertEqual(module.base.iso_utc(slices[0][0]), "2026-08-07T22:00:00Z")
        self.assertEqual(module.base.iso_utc(slices[0][1]), "2026-08-11T10:00:00Z")
        self.assertEqual(module.base.iso_utc(slices[1][0]), "2026-08-11T10:00:00Z")
        self.assertEqual(module.base.iso_utc(slices[1][1]), "2026-08-14T22:00:00Z")

    def test_cap_hit_halves_are_recursively_bisected(self):
        arxiv_plans = []

        def arxiv(plan, cfg, output_root):
            arxiv_plans.append(dict(plan))
            return fake_run(plan, "arxiv-api")

        def cap_hits(output_root, run, max_results):
            start_text, end_text = run["run_id"].split("arxiv-api-", 1)[1].rsplit("-", 1)
            start = module.base.parse_instant(start_text)
            end = module.base.parse_instant(end_text)
            if end - start > timedelta(days=2):
                return [{"query_id": "cs-ai", "entry_count": max_results, "configured_cap": max_results}]
            return []

        # Avoid parsing run ids containing ISO '-' by deriving duration from recorded plans instead.
        def cap_hits_by_plan(output_root, run, max_results):
            plan = next(p for p in arxiv_plans if run["run_id"] == fake_run(p, "arxiv-api")["run_id"])
            start = module.base.parse_instant(plan["collection_window_start"])
            end = module.base.parse_instant(plan["collection_window_end"])
            if end - start > timedelta(days=2):
                return [{"query_id": "cs-ai", "entry_count": max_results, "configured_cap": max_results}]
            return []

        with tempfile.TemporaryDirectory() as td, \
             patch.object(module.base, "run_arxiv", side_effect=arxiv), \
             patch.object(module, "cap_hits_for_run", side_effect=cap_hits_by_plan):
            report = module.run(PLAN, CFG, Path(td), "arxiv")

        # Two 3.5-day parents each split into two 1.75-day terminal children.
        self.assertEqual(len(arxiv_plans), 6)
        self.assertEqual(len(report["coverage"]["arxiv_slice_observations"]), 6)
        self.assertEqual(report["coverage"]["arxiv_residual_cap_hits"], [])
        terminals = [
            item for item in report["coverage"]["arxiv_slice_observations"]
            if item["terminal_reason"] == "BELOW_CAP"
        ]
        self.assertEqual(len(terminals), 4)
        self.assertEqual(report["coverage"]["coverage_status"], "BASE_INTAKE_COLLECTED")

    def test_residual_cap_hit_is_explicit_at_minimum_slice(self):
        cfg = dict(CFG)
        cfg["coverage_policy"] = dict(CFG["coverage_policy"])
        cfg["coverage_policy"]["weekly_arxiv_min_slice_minutes"] = 84 * 60

        with tempfile.TemporaryDirectory() as td, \
             patch.object(module.base, "run_arxiv", side_effect=lambda p, c, o: fake_run(p, "arxiv-api")), \
             patch.object(
                 module,
                 "cap_hits_for_run",
                 return_value=[{"query_id": "cs-ai", "entry_count": 200, "configured_cap": 200}],
             ):
            report = module.run(PLAN, cfg, Path(td), "arxiv")

        self.assertEqual(len(report["coverage"]["arxiv_residual_cap_hits"]), 2)
        self.assertEqual(report["coverage"]["coverage_status"], "INCOMPLETE_CAP_HIT")

    def test_non_arxiv_collectors_use_full_canonical_window_once(self):
        github_plans = []
        official_plans = []

        def github(plan, cfg, output_root):
            github_plans.append(dict(plan))
            return fake_run(plan, "github-releases")

        def official(plan, cfg, output_root):
            official_plans.append(dict(plan))
            return fake_run(plan, "official-pages")

        with tempfile.TemporaryDirectory() as td, \
             patch.object(module.base, "run_github_releases", side_effect=github), \
             patch.object(module.base, "run_official_pages", side_effect=official):
            report = module.run(PLAN, CFG, Path(td), "all")

        # arXiv is not mocked here and therefore must be disabled for this assertion.
        self.assertEqual(report["overall_status"], "success")
        self.assertEqual(len(github_plans), 1)
        self.assertEqual(len(official_plans), 1)
        self.assertEqual(github_plans[0]["collection_window_start"], PLAN["collection_window_start"])
        self.assertEqual(github_plans[0]["collection_window_end"], PLAN["collection_window_end"])
        self.assertEqual(official_plans[0]["collection_window_start"], PLAN["collection_window_start"])
        self.assertEqual(official_plans[0]["collection_window_end"], PLAN["collection_window_end"])


if __name__ == "__main__":
    unittest.main()
