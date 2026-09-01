from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import raw_provenance as rp


class RawProvenanceTests(unittest.TestCase):
    def _raw(self, root: Path, issue: str, name: str, content: str) -> Path:
        path = root / "sources" / issue / "grok" / "raw" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_update_then_check_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            self._raw(root, issue, "trend.md", "raw observation")
            index = root / "sources" / issue / "raw-index.json"

            update_report, updated = rp.update(root, issue, index)
            self.assertTrue(updated, update_report)
            self.assertEqual(update_report["indexed_count"], 1)

            check_report, checked = rp.check(root, issue, index)
            self.assertTrue(checked, check_report)

    def test_modified_indexed_raw_file_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            raw = self._raw(root, issue, "trend.md", "original")
            index = root / "sources" / issue / "raw-index.json"
            rp.update(root, issue, index)

            raw.write_text("edited downstream", encoding="utf-8")
            check_report, checked = rp.check(root, issue, index)
            self.assertFalse(checked)
            self.assertEqual(len(check_report["modified_raw_files"]), 1)

            update_report, updated = rp.update(root, issue, index)
            self.assertFalse(updated)
            self.assertTrue(update_report["refused_update"])

    def test_new_raw_file_requires_index_update(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            self._raw(root, issue, "trend.md", "one")
            index = root / "sources" / issue / "raw-index.json"
            rp.update(root, issue, index)

            self._raw(root, issue, "trend-2.md", "two")
            check_report, checked = rp.check(root, issue, index)
            self.assertFalse(checked)
            self.assertEqual(len(check_report["unindexed_raw_files"]), 1)

            update_report, updated = rp.update(root, issue, index)
            self.assertTrue(updated, update_report)
            self.assertEqual(update_report["indexed_count"], 2)

    def test_removed_indexed_raw_file_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue = "2026-W99"
            raw = self._raw(root, issue, "trend.md", "one")
            index = root / "sources" / issue / "raw-index.json"
            rp.update(root, issue, index)
            raw.unlink()

            check_report, checked = rp.check(root, issue, index)
            self.assertFalse(checked)
            self.assertEqual(len(check_report["missing_indexed_files"]), 1)


if __name__ == "__main__":
    unittest.main()
