import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "source_intake.py"
spec = importlib.util.spec_from_file_location("source_intake", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


PLAN = {
    "issue_id": "2026-W33",
    "generated_at": "2026-08-15T00:30:00+00:00",
    "editorial_cutoff": "2026-08-14T18:00:00-04:00",
    "collection_window_start": "2026-08-09T23:00:00+09:00",
    "collection_window_end": "2026-08-15T09:30:00+09:00",
}


def only_match(root: Path, pattern: str) -> Path:
    matches = list(root.glob(pattern))
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one match for {pattern}, found {matches}")
    return matches[0]


class SourceIntakeTests(unittest.TestCase):
    def test_parse_arxiv_atom(self):
        atom = b'''<?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <id>http://arxiv.org/abs/2608.12345v1</id>
            <updated>2026-08-12T12:00:00Z</updated>
            <published>2026-08-12T12:00:00Z</published>
            <title> Test   Paper </title>
            <summary> Test abstract. </summary>
            <author><name>Alice Example</name></author>
            <category term="cs.AI"/>
            <arxiv:primary_category term="cs.AI"/>
            <link href="https://arxiv.org/abs/2608.12345v1" rel="alternate" type="text/html"/>
          </entry>
        </feed>'''
        entries = module.parse_arxiv_atom(atom)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["title"], "Test Paper")
        self.assertEqual(entries[0]["authors"], ["Alice Example"])
        self.assertEqual(entries[0]["primary_category"], "cs.AI")

    def test_github_release_window_filter_and_raw_preservation(self):
        releases = [
            {
                "id": 1,
                "tag_name": "v1.2.3",
                "name": "v1.2.3",
                "html_url": "https://github.com/example/repo/releases/tag/v1.2.3",
                "draft": False,
                "prerelease": False,
                "created_at": "2026-08-12T00:00:00Z",
                "published_at": "2026-08-12T00:00:00Z",
            },
            {
                "id": 2,
                "tag_name": "old",
                "name": "old",
                "html_url": "https://github.com/example/repo/releases/tag/old",
                "draft": False,
                "prerelease": False,
                "created_at": "2026-07-01T00:00:00Z",
                "published_at": "2026-07-01T00:00:00Z",
            },
        ]
        raw = json.dumps(releases, separators=(",", ":")).encode("utf-8")
        config = {
            "user_agent": "test",
            "http_timeout_seconds": 5,
            "github_releases": {
                "enabled": True,
                "api_version": "2026-03-10",
                "per_page": 100,
                "repositories": ["example/repo"],
            },
        }
        with tempfile.TemporaryDirectory() as td, patch.object(
            module, "http_get", return_value=(raw, {"status": 200, "final_url": "x"})
        ):
            root = Path(td)
            run = module.run_github_releases(PLAN, config, root)
            self.assertEqual(run["status"], "success")
            raw_path = only_match(
                root,
                "sources/2026-W33/collectors/github-releases/runs/*/raw/example__repo.json",
            )
            self.assertEqual(raw_path.read_bytes(), raw)
            summary_path = only_match(
                root,
                "sources/2026-W33/collectors/github-releases/runs/*/summary.json",
            )
            summary = json.loads(summary_path.read_text())
            self.assertEqual(summary["matching_release_count"], 1)
            self.assertEqual(summary["matching_releases"][0]["tag_name"], "v1.2.3")

    def test_arxiv_run_preserves_atom_and_writes_summary(self):
        atom = b'''<?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <id>http://arxiv.org/abs/2608.12345v1</id>
            <updated>2026-08-12T12:00:00Z</updated>
            <published>2026-08-12T12:00:00Z</published>
            <title>Paper</title><summary>Abstract</summary>
            <author><name>A</name></author><category term="cs.AI"/>
          </entry>
        </feed>'''
        config = {
            "user_agent": "test",
            "http_timeout_seconds": 5,
            "arxiv": {
                "enabled": True,
                "endpoint": "https://export.arxiv.org/api/query",
                "delay_seconds": 0,
                "max_results_per_query": 10,
                "queries": [{"id": "cs-ai", "search_query": "cat:cs.AI"}],
            },
        }
        with tempfile.TemporaryDirectory() as td, patch.object(
            module, "http_get", return_value=(atom, {"status": 200, "final_url": "x"})
        ):
            root = Path(td)
            run = module.run_arxiv(PLAN, config, root)
            self.assertEqual(run["status"], "success")
            raw_path = only_match(root, "sources/2026-W33/collectors/arxiv/runs/*/raw/cs-ai.atom")
            self.assertEqual(raw_path.read_bytes(), atom)
            summary_path = only_match(root, "sources/2026-W33/collectors/arxiv/runs/*/summary.json")
            summary = json.loads(summary_path.read_text())
            self.assertEqual(summary["unique_entry_count"], 1)

    def test_official_snapshot_preserves_html(self):
        html = b"<html><body>news</body></html>"
        config = {
            "user_agent": "test",
            "http_timeout_seconds": 5,
            "official_pages": {
                "enabled": True,
                "pages": [{"id": "vendor-news", "url": "https://example.com/news"}],
            },
        }
        with tempfile.TemporaryDirectory() as td, patch.object(
            module, "http_get", return_value=(html, {"status": 200, "final_url": "https://example.com/news"})
        ):
            root = Path(td)
            run = module.run_official_pages(PLAN, config, root)
            self.assertEqual(run["status"], "success")
            raw_path = only_match(
                root,
                "sources/2026-W33/collectors/official-pages/runs/*/raw/vendor-news.html",
            )
            self.assertEqual(raw_path.read_bytes(), html)

    def test_run_paths_do_not_collide_across_observation_times(self):
        a = module.run_base("2026-W33", "arxiv", module.parse_instant("2026-08-15T00:00:00Z"))
        b = module.run_base("2026-W33", "arxiv", module.parse_instant("2026-08-15T00:00:01Z"))
        self.assertNotEqual(a, b)
        self.assertIn("runs/20260815T000000Z", a)
        self.assertIn("runs/20260815T000001Z", b)


if __name__ == "__main__":
    unittest.main()
