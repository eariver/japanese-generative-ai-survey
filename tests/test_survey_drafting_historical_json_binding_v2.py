from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core


class DraftHistoricalJsonBindingV2Tests(unittest.TestCase):
    @staticmethod
    def _write_compact(path: Path, value: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )

    def _fixture(self) -> tuple[Path, dict, dict]:
        temp = tempfile.TemporaryDirectory(prefix="survey-draft-historical-json-")
        self.addCleanup(temp.cleanup)
        source_root = Path(temp.name)
        profile_path = source_root / "production-profile.json"
        profile_path.write_text("{}\n", encoding="utf-8")

        card = {
            "schema_version": "2.0-rc1",
            "issue_id": "HISTORICAL-JSON",
            "evidence_task_id": "evidence:HISTORICAL-JSON:t1",
            "claims": [{"statement_id": "claim-1", "text": "historical raw evidence"}],
        }
        card_path = (
            source_root
            / "evidence/v2/accepted/result-set-1/results/task-1.json"
        )
        self._write_compact(card_path, card)
        card_sha = core.sha256_file(card_path)

        acceptance = {
            "schema_version": "2.0-rc1",
            "result_set_sha256": "result-set-1",
            "results": [
                {
                    "evidence_task_id": "evidence:HISTORICAL-JSON:t1",
                    "sha256": card_sha,
                    "filename": "task-1.json",
                }
            ],
        }
        acceptance_path = card_path.parent.parent / "evidence-accepted.json"
        self._write_compact(acceptance_path, acceptance)

        matrix = {
            "schema_version": "2.0-rc1",
            "rows": [
                {
                    "candidate_id": "candidate:HISTORICAL-JSON:c1",
                    "evidence_task_id": "evidence:HISTORICAL-JSON:t1",
                    "evidence_sha256": card_sha,
                }
            ],
        }
        matrix_path = source_root / "candidate-matrix-v2.json"
        self._write_compact(matrix_path, matrix)

        package = {
            "basis": {
                "candidate_matrix_sha256": core.sha256_file(matrix_path),
                "evidence_acceptance_sha256": core.sha256_file(acceptance_path),
            },
            "candidate_matrix": matrix,
            "evidence_acceptance": acceptance,
            "evidence_inputs": [
                {
                    "candidate_id": "candidate:HISTORICAL-JSON:c1",
                    "architecture_usage": "PRIMARY",
                    "evidence_task_id": "evidence:HISTORICAL-JSON:t1",
                    "evidence_sha256": card_sha,
                    "evidence_card": card,
                }
            ],
        }
        return profile_path, package, card

    def test_compact_historical_bytes_bind_without_current_reserialization(self) -> None:
        profile_path, package, card = self._fixture()
        errors, raw_hashes = drafting._historical_raw_authority_hashes(
            package, profile_path
        )
        self.assertEqual(errors, [])
        accepted_sha = package["evidence_inputs"][0]["evidence_sha256"]
        self.assertEqual(raw_hashes[core.sha256_object(card)], accepted_sha)

        # The regression is meaningful only if the current pretty serializer
        # would produce different bytes from the historical compact artifact.
        self.assertNotEqual(drafting._base._object_sha(card), accepted_sha)

        observed = drafting._run_with_authoritative_raw_hashes(
            lambda: [drafting._base._object_sha(card)], raw_hashes
        )
        self.assertEqual(observed, [accepted_sha])
        self.assertNotEqual(drafting._base._object_sha(card), accepted_sha)

    def test_partial_authority_missing_matrix_fails_closed(self) -> None:
        profile_path, package, _ = self._fixture()
        (profile_path.parent / "candidate-matrix-v2.json").unlink()

        errors, raw_hashes = drafting._historical_raw_authority_hashes(
            package, profile_path
        )

        self.assertEqual(
            errors,
            ["Draft Package canonical Candidate Matrix is missing"],
        )
        self.assertEqual(raw_hashes, {})

    def test_partial_authority_missing_accepted_tree_fails_closed(self) -> None:
        profile_path, package, _ = self._fixture()
        accepted_root = profile_path.parent / "evidence/v2/accepted"
        accepted_root.rename(profile_path.parent / "evidence/v2/accepted-missing")

        errors, raw_hashes = drafting._historical_raw_authority_hashes(
            package, profile_path
        )

        self.assertEqual(
            errors,
            ["Draft Package canonical accepted Evidence authority is missing"],
        )
        self.assertEqual(raw_hashes, {})

    def test_no_canonical_authority_preserves_isolated_fixture_fallback(self) -> None:
        profile_path, package, _ = self._fixture()
        (profile_path.parent / "candidate-matrix-v2.json").unlink()
        accepted_root = profile_path.parent / "evidence/v2/accepted"
        accepted_root.rename(profile_path.parent / "evidence/v2/accepted-missing")

        errors, raw_hashes = drafting._historical_raw_authority_hashes(
            package, profile_path
        )

        self.assertEqual(errors, [])
        self.assertEqual(raw_hashes, {})

    def test_embedded_card_drift_fails_even_when_claimed_raw_sha_is_unchanged(self) -> None:
        profile_path, package, _ = self._fixture()
        altered = copy.deepcopy(package)
        altered["evidence_inputs"][0]["evidence_card"]["claims"][0]["text"] = (
            "tampered embedded evidence"
        )
        errors, _ = drafting._historical_raw_authority_hashes(altered, profile_path)
        self.assertTrue(
            any("embedded Evidence Card differs" in error for error in errors), errors
        )

    def test_exact_raw_card_byte_drift_fails_closed(self) -> None:
        profile_path, package, card = self._fixture()
        card_path = (
            profile_path.parent
            / "evidence/v2/accepted/result-set-1/results/task-1.json"
        )
        core.write_json(card_path, card)
        errors, _ = drafting._historical_raw_authority_hashes(package, profile_path)
        self.assertTrue(
            any("canonical Evidence Card raw bytes drifted" in error for error in errors),
            errors,
        )


if __name__ == "__main__":
    unittest.main()
