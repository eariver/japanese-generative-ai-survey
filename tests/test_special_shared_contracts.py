from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


class SpecialSharedContractTests(unittest.TestCase):
    def pattern(self, path: str, *keys: str) -> str:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
        for key in keys:
            value = value[key]
        return value

    def test_core_discovery_and_evidence_contracts_accept_weekly_and_special_ids(self) -> None:
        paths = [
            "schemas/collector-run.schema.json",
            "schemas/screening-record.schema.json",
            "schemas/screening-batch-result.schema.json",
            "schemas/evidence-task.schema.json",
            "schemas/evidence-run.schema.json",
            "schemas/evidence-card.schema.json",
        ]
        for path in paths:
            with self.subTest(path=path):
                pattern = self.pattern(path, "properties", "issue_id", "pattern")
                self.assertIsNotNone(re.fullmatch(pattern, "2026-W33"))
                self.assertIsNotNone(re.fullmatch(pattern, "SP-2026-M07"))
                self.assertIsNone(re.fullmatch(pattern, "2026-M07"))

    def test_evidence_task_identity_binds_special_issue_id(self) -> None:
        pattern = self.pattern("schemas/evidence-task.schema.json", "properties", "evidence_task_id", "pattern")
        self.assertIsNotNone(re.fullmatch(pattern, "evidence:SP-2026-M07:test-item-0123456789"))
        self.assertIsNotNone(re.fullmatch(pattern, "evidence:2026-W33:test-item-0123456789"))


if __name__ == "__main__":
    unittest.main()
