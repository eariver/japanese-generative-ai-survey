import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_grok_trend_run.py"
spec = importlib.util.spec_from_file_location("generate_grok_trend_run", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class GrokTrendRunGenerationTests(unittest.TestCase):
    def test_generate_binds_window_prompt_hash_and_output_path(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            prompt = root / "config/prompts/grok/x-trend-sensor-v0.4.md"
            prompt.parent.mkdir(parents=True)
            prompt.write_text("prompt body\n", encoding="utf-8")

            plan = {
                "issue_id": "2026-W33",
                "generated_at": "2026-08-15T00:30:00+00:00",
                "editorial_cutoff": "2026-08-14T18:00:00-04:00",
                "collection_window_start": "2026-08-09T23:00:00+09:00",
            }

            md, metadata = module.generate(plan, root)

            self.assertEqual(metadata["issue_id"], "2026-W33")
            self.assertEqual(metadata["stage"], "trend-discovery")
            self.assertEqual(metadata["status"], "ready")
            self.assertEqual(metadata["time"]["collection_window_start"], "2026-08-09T23:00:00+09:00")
            self.assertEqual(metadata["time"]["editorial_cutoff"], "2026-08-14T18:00:00-04:00")
            self.assertEqual(metadata["expected_output"]["filename"], "x-trend-sensor-2026-08-15-v0.4.md")
            self.assertEqual(
                metadata["expected_output"]["repository_path"],
                "sources/2026-W33/grok/raw/x-trend-sensor-2026-08-15-v0.4.md",
            )
            self.assertRegex(metadata["collector"]["prompt_hash"], r"^sha256:[0-9a-f]{64}$")
            self.assertEqual(metadata["execution"]["repository_write_authority"], "none")
            self.assertIn("2026-08-14T18:00:00-04:00", md)
            self.assertIn("2026-08-09T23:00:00+09:00", md)
            self.assertIn("observed_at", md)
            self.assertIn("collector-run.schema.json", md)
            self.assertIn("GitHubへのPushは試みないでください", md)

    def test_generate_requires_collection_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            prompt = root / "config/prompts/grok/x-trend-sensor-v0.4.md"
            prompt.parent.mkdir(parents=True)
            prompt.write_text("prompt body\n", encoding="utf-8")
            plan = {
                "issue_id": "2026-W33",
                "generated_at": "2026-08-15T00:30:00+00:00",
                "editorial_cutoff": "2026-08-14T18:00:00-04:00",
                "collection_window_start": None,
            }
            with self.assertRaises(ValueError):
                module.generate(plan, root)


if __name__ == "__main__":
    unittest.main()
