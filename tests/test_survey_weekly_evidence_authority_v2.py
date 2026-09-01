from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_weekly_semantic_publication_v2 as weekly


class WeeklyEvidenceAuthorityJoinTests(unittest.TestCase):
    def _fixture(self, root: Path) -> tuple[Path, str]:
        source_root = root / "sources/2026-W33"
        accepted = source_root / "evidence/v2/accepted/testset"
        accepted.mkdir(parents=True)
        discovery = source_root / "discovery"
        discovery.mkdir(parents=True)

        core.write_json(
            accepted / "evidence-accepted.json",
            {
                "schema_version": "2.0-rc1",
                "issue_id": "2026-W33",
                "results": [
                    {
                        "discovery_ids": ["d1"],
                        "status": "VERIFIED",
                    }
                ],
            },
        )
        acceptance_sha = core.sha256_file(accepted / "evidence-accepted.json")

        core.write_json(
            source_root / "materiality-ledger-v2.json",
            {
                "schema_version": "2.0-rc1",
                "issue_id": "2026-W33",
                "rows": [
                    {
                        "discovery_id": "d1",
                        "downstream_disposition": "MATERIAL",
                    }
                ],
            },
        )
        ledger_sha = core.sha256_file(source_root / "materiality-ledger-v2.json")

        core.write_json(
            source_root / "candidate-matrix-v2.json",
            {
                "schema_version": "2.0-rc1",
                "issue_id": "2026-W33",
                "basis": {
                    "evidence_acceptance_sha256": acceptance_sha,
                    "materiality_ledger_sha256": ledger_sha,
                },
                "rows": [
                    {
                        "candidate_id": "candidate:2026-W33:test",
                        "discovery_ids": ["d1"],
                        "title": "Canonical title",
                        "evidence_status": "VERIFIED",
                        "materiality": "MATERIAL",
                    }
                ],
            },
        )
        core.write_json(
            discovery / "discovery-accepted-v2.json",
            {
                "schema_version": "2.0-rc1",
                "issue_id": "2026-W33",
                "records": [
                    {
                        "discovery_id": "d1",
                        "source_locator": "https://example.com/source",
                    }
                ],
            },
        )
        return source_root, acceptance_sha

    def test_join_uses_only_accepted_core_authorities(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_root, acceptance_sha = self._fixture(Path(tmp))
            records, authority = weekly._records_from_authorities(source_root, acceptance_sha)
            self.assertEqual(records["d1"]["entity"]["canonical_name"], "Canonical title")
            self.assertEqual(records["d1"]["entity"]["canonical_url"], "https://example.com/source")
            self.assertEqual(records["d1"]["status"], "VERIFIED")
            self.assertEqual(records["d1"]["materiality"], "MATERIAL")
            self.assertEqual(authority["evidence_acceptance"]["sha256"], acceptance_sha)

    def test_join_fails_closed_on_evidence_status_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_root, acceptance_sha = self._fixture(Path(tmp))
            matrix = core.load_json(source_root / "candidate-matrix-v2.json")
            matrix["rows"][0]["evidence_status"] = "PARTIAL"
            core.write_json(source_root / "candidate-matrix-v2.json", matrix)
            with self.assertRaisesRegex(ValueError, "Evidence status authority mismatch"):
                weekly._records_from_authorities(source_root, acceptance_sha)


if __name__ == "__main__":
    unittest.main()
