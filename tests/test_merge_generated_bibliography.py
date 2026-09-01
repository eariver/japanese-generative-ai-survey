from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import merge_generated_bibliography as mgb


class GeneratedBibliographyMergeTests(unittest.TestCase):
    def _entry(self, key: str, title: str, url: str) -> str:
        return (
            f"@online{{{key},\n"
            f"  title = {{{title}}},\n"
            f"  url = {{{url}}}\n"
            "}\n"
        )

    def test_identical_keys_are_deduplicated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = root / "a.bib"
            b = root / "b.bib"
            text = self._entry("src-abc", "Title", "https://example.com")
            a.write_text(text, encoding="utf-8")
            b.write_text(text, encoding="utf-8")
            out = root / "merged.bib"
            manifest_path = root / "manifest.json"
            manifest, passed = mgb.merge([a, b], out, manifest_path)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["entry_count"], 1)
            self.assertEqual(manifest["deduplicated_keys"], ["src-abc"])
            self.assertEqual(out.read_text(encoding="utf-8").count("@online{src-abc"), 1)

    def test_conflicting_same_key_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = root / "a.bib"
            b = root / "b.bib"
            a.write_text(self._entry("src-abc", "Title A", "https://example.com"), encoding="utf-8")
            b.write_text(self._entry("src-abc", "Title B", "https://example.com"), encoding="utf-8")
            out = root / "merged.bib"
            manifest, passed = mgb.merge([a, b], out, root / "manifest.json")
            self.assertFalse(passed)
            self.assertFalse(out.exists())
            self.assertEqual(manifest["conflicts"][0]["key"], "src-abc")

    def test_malformed_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "bad.bib"
            bad.write_text("not bibtex\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                mgb.merge([bad], root / "out.bib", root / "manifest.json")


if __name__ == "__main__":
    unittest.main()
