import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "collect_special_supplemental_sources.py"
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location("collect_special_supplemental_sources", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class SupplementalSourceCollectorTests(unittest.TestCase):
    def test_plan_requires_gap_reason_and_in_window_date(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "plan.json"
            path.write_text(json.dumps({
                "schema_version": "1.0",
                "issue_id": "SP-2024-H2",
                "coverage": {"start": "2024-07-01T00:00:00Z", "end": "2024-12-31T23:59:59Z"},
                "items": [{
                    "id": "supplemental-example",
                    "title": "Example",
                    "url": "https://example.com/item",
                    "published_at": "2024-08-01T00:00:00Z",
                    "coverage_gap_reason": "Not represented by the base watchlist.",
                }],
            }), encoding="utf-8")
            value = module.load_plan(path)
            self.assertEqual(value["issue_id"], "SP-2024-H2")

    def test_collection_uses_official_pages_shape_for_canonical_screening(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            plan = root / "sources" / "SP-2024-H2" / "coverage" / "supplemental-source-plan-v0.1.json"
            plan.parent.mkdir(parents=True)
            plan.write_text(json.dumps({
                "schema_version": "1.0",
                "issue_id": "SP-2024-H2",
                "purpose": "SUPPLEMENTAL_PRIMARY_SOURCE_GAP_FILL",
                "coverage": {"start": "2024-07-01T00:00:00Z", "end": "2024-12-31T23:59:59Z"},
                "items": [{
                    "id": "supplemental-example",
                    "title": "Example release",
                    "url": "https://example.com/item",
                    "published_at": "2024-08-01T00:00:00Z",
                    "coverage_gap_reason": "Missing from base intake.",
                }],
            }), encoding="utf-8")
            with patch.object(module.base, "http_get", return_value=(b"<html>example</html>", {"status": 200, "final_url": "https://example.com/item"})):
                audit = module.run(plan_path=plan, output_root=root, user_agent="test", timeout=5)
            self.assertEqual(audit["status"], "success")
            self.assertEqual(audit["screening_ids"], ["official-index:supplemental-example"])
            summaries = list((root / "sources" / "SP-2024-H2" / "collectors" / "official-pages" / "runs").glob("*/summary.json"))
            self.assertEqual(len(summaries), 1)
            summary = json.loads(summaries[0].read_text(encoding="utf-8"))
            self.assertEqual(summary["collection_mode"], "SUPPLEMENTAL_COVERAGE_GAP_FILL")
            self.assertEqual(summary["pages"][0]["id"], "supplemental-example")
            run = json.loads((summaries[0].parent / "collector-run.json").read_text(encoding="utf-8"))
            self.assertEqual(run["collector"]["id"], "official-pages")
            self.assertEqual(run["stage"], "supplemental-primary-source-discovery")


if __name__ == "__main__":
    unittest.main()
