from __future__ import annotations

import unittest

from scripts import survey_evidence_v2 as evidence
from scripts import survey_screening_v2 as screening
from tests import test_survey_screening_v2 as screening_tests


IMPLEMENTATION_SHA = "3" * 40


class SurveyScreeningV2ArchiveTests(unittest.TestCase):
    def fixture(self):
        helper = screening_tests.SurveyScreeningV2Tests(methodName="test_discovery_set_rejects_duplicate_ids")
        helper.setUp()
        temp, root, cfg = helper.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = helper.init_thematic(root, cfg)
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        screening.write_jsonl(
            discovery_path,
            [helper.discovery("SP001", "seed", "BASE")],
        )
        package_path = screening.prepare_package(
            root,
            state_path,
            discovery_path,
            root / "sources/SP001/screening/v2/package",
            IMPLEMENTATION_SHA,
        )
        results_dir = helper._write_valid_results(root, package_path)
        accepted = screening.accept_results(
            root,
            package_path,
            results_dir,
            root / "sources/SP001/screening/v2/runs",
            IMPLEMENTATION_SHA,
        )
        return root, state_path, discovery_path, accepted

    def test_acceptance_preserves_exact_input_and_result_batches(self) -> None:
        root, _, _, accepted = self.fixture()
        payload = screening.validate_acceptance(root, accepted, IMPLEMENTATION_SHA)
        self.assertEqual(payload["result_set_sha256"], accepted.parent.name)
        self.assertTrue((accepted.parent / "input/batches/batch-001.jsonl").is_file())
        self.assertTrue((accepted.parent / "results/batch-001.json").is_file())

    def test_archived_result_tampering_fails_screening_and_downstream_evidence(self) -> None:
        root, state_path, discovery_path, accepted = self.fixture()
        archived_result = accepted.parent / "results/batch-001.json"
        archived_result.write_text(archived_result.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "accepted Screening result batch changed"):
            screening.validate_acceptance(root, accepted, IMPLEMENTATION_SHA)
        with self.assertRaisesRegex(ValueError, "accepted Screening result batch changed"):
            evidence.prepare_evidence_package(
                root,
                state_path,
                discovery_path,
                accepted,
                root / "sources/SP001/evidence/v2/package",
                IMPLEMENTATION_SHA,
            )

    def test_acceptance_is_idempotent_only_when_existing_archive_revalidates(self) -> None:
        root, _, _, accepted = self.fixture()
        package_path = root / "sources/SP001/screening/v2/package/package.json"
        results_dir = package_path.parent / "results"
        second = screening.accept_results(
            root,
            package_path,
            results_dir,
            root / "sources/SP001/screening/v2/runs",
            IMPLEMENTATION_SHA,
        )
        self.assertEqual(second, accepted)


if __name__ == "__main__":
    unittest.main()
