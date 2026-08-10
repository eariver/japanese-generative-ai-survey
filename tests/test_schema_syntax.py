from __future__ import annotations

import json
import unittest
from pathlib import Path


class SchemaSyntaxTests(unittest.TestCase):
    def test_every_json_schema_parses_and_has_schema_version_marker(self) -> None:
        root = Path(__file__).resolve().parents[1]
        schemas = sorted((root / "schemas").glob("*.json"))
        self.assertTrue(schemas, "no JSON schemas found")
        for path in schemas:
            with self.subTest(schema=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(data, dict)
                self.assertIn("$schema", data)
                self.assertEqual(data.get("type"), "object")


if __name__ == "__main__":
    unittest.main()
