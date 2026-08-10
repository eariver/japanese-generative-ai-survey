from __future__ import annotations

import json
import py_compile
import unittest
from pathlib import Path


class RepositoryContractSyntaxTests(unittest.TestCase):
    def test_every_pipeline_script_compiles(self) -> None:
        root = Path(__file__).resolve().parents[1]
        scripts = sorted((root / "scripts").glob("*.py"))
        self.assertTrue(scripts)
        for path in scripts:
            with self.subTest(path=path.relative_to(root).as_posix()):
                py_compile.compile(str(path), doraise=True)

    def test_all_json_schemas_and_configuration_parse(self) -> None:
        root = Path(__file__).resolve().parents[1]
        paths = [
            *sorted((root / "schemas").glob("*.json")),
            *sorted((root / "config").rglob("*.json")),
        ]
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.relative_to(root).as_posix()):
                value = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(value, (dict, list))


if __name__ == "__main__":
    unittest.main()
