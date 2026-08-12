import importlib.util
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "source_intake.py"
spec = importlib.util.spec_from_file_location("source_intake_retry", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


PLAN = {
    "issue_id": "SP-TEST",
    "editorial_cutoff": "2026-03-31T23:59:59Z",
    "collection_window_start": "2026-03-01T00:00:00Z",
    "collection_window_end": "2026-03-31T23:59:59Z",
}

ATOM = b'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2603.12345v1</id>
    <updated>2026-03-12T12:00:00Z</updated>
    <published>2026-03-12T12:00:00Z</published>
    <title>Retry Test Paper</title>
    <summary>Abstract</summary>
    <author><name>A</name></author>
    <category term="cs.AI"/>
  </entry>
</feed>'''


def config(**arxiv_overrides):
    arxiv = {
        "enabled": True,
        "endpoint": "https://export.arxiv.org/api/query",
        "delay_seconds": 20,
        "request_timeout_seconds": 120,
        "max_attempts": 3,
        "retry_backoff_seconds": 20,
        "max_results_per_query": 200,
        "queries": [{"id": "cs-ai", "search_query": "cat:cs.AI"}],
    }
    arxiv.update(arxiv_overrides)
    return {
        "user_agent": "test",
        "http_timeout_seconds": 45,
        "arxiv": arxiv,
    }


class ArxivRetryTests(unittest.TestCase):
    def test_shared_config_uses_conservative_arxiv_settings(self):
        cfg = json.loads((ROOT / "config" / "source-intake.json").read_text(encoding="utf-8"))
        self.assertEqual(cfg["arxiv"]["delay_seconds"], 20)
        self.assertEqual(cfg["arxiv"]["request_timeout_seconds"], 120)
        self.assertEqual(cfg["arxiv"]["max_attempts"], 3)
        self.assertEqual(cfg["arxiv"]["retry_backoff_seconds"], 20)

    def test_arxiv_429_is_retried_and_retry_is_recorded(self):
        error = urllib.error.HTTPError(
            "https://export.arxiv.org/api/query",
            429,
            "Too Many Requests",
            {},
            None,
        )
        with tempfile.TemporaryDirectory() as td, patch.object(
            module,
            "http_get",
            side_effect=[error, (ATOM, {"status": 200, "final_url": "https://export.arxiv.org/api/query"})],
        ) as get_mock, patch.object(module.time, "sleep") as sleep_mock:
            root = Path(td)
            run = module.run_arxiv(PLAN, config(), root)

            self.assertEqual(run["status"], "success")
            self.assertEqual(get_mock.call_count, 2)
            self.assertEqual(get_mock.call_args.kwargs["timeout"], 120)
            sleep_mock.assert_called_once_with(20.0)

            summary_path = next(root.glob("sources/SP-TEST/collectors/arxiv/runs/*/summary.json"))
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            query = summary["queries"][0]
            self.assertEqual(query["attempt_count"], 2)
            self.assertEqual(len(query["retry_history"]), 1)
            self.assertTrue(query["retry_history"][0]["retryable"])
            self.assertEqual(query["retry_history"][0]["retry_delay_seconds"], 20.0)

    def test_arxiv_non_transient_http_error_is_not_retried(self):
        error = urllib.error.HTTPError(
            "https://export.arxiv.org/api/query",
            404,
            "Not Found",
            {},
            None,
        )
        with tempfile.TemporaryDirectory() as td, patch.object(
            module, "http_get", side_effect=error
        ) as get_mock, patch.object(module.time, "sleep") as sleep_mock:
            root = Path(td)
            run = module.run_arxiv(PLAN, config(), root)

            self.assertEqual(run["status"], "failed")
            self.assertEqual(get_mock.call_count, 1)
            sleep_mock.assert_not_called()

            summary_path = next(root.glob("sources/SP-TEST/collectors/arxiv/runs/*/summary.json"))
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            self.assertEqual(summary["errors"][0]["attempt_count"], 1)
            self.assertFalse(summary["errors"][0]["retry_history"][0]["retryable"])


if __name__ == "__main__":
    unittest.main()
