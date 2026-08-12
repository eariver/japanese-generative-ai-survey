import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.revise_special_interactive_evidence import validate_current_state, validate_prior_run


class SpecialEvidenceRevisionBoundaryTests(unittest.TestCase):
    def write_json(self, path: Path, value: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_current_state_requires_pre_selection_evidence_reviewed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_path = root / "sources" / "SP-2026-M04" / "pipeline-state.json"
            state = {
                "issue_id": "SP-2026-M04",
                "lifecycle_state": "EVIDENCE_REVIEWED",
                "gates": {
                    "candidate_inventory": "passed",
                    "evidence_normalized": "passed",
                    "candidate_selection": "pending",
                    "issue_architecture": "pending",
                },
            }
            self.write_json(state_path, state)
            path, loaded, raw = validate_current_state(root, "SP-2026-M04")
            self.assertEqual(path, state_path)
            self.assertEqual(loaded, state)
            self.assertEqual(raw, state_path.read_bytes())

            state["gates"]["candidate_selection"] = "passed"
            self.write_json(state_path, state)
            with self.assertRaisesRegex(ValueError, "forbidden after Candidate Selection"):
                validate_current_state(root, "SP-2026-M04")

    def test_prior_run_requires_exact_rebuilt_package_sha(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package_root = root / "package"
            package_root.mkdir()
            package_path = package_root / "evidence-execution-package.json"
            package_path.write_text('{"schema_version":"1.0"}\n', encoding="utf-8")
            package_sha = hashlib.sha256(package_path.read_bytes()).hexdigest()
            prior_sha = "1" * 64
            acceptance_path = root / "sources" / "SP-2026-M04" / "evidence" / "runs" / prior_sha / "acceptance.json"
            self.write_json(
                acceptance_path,
                {
                    "schema_version": "1.0",
                    "issue_id": "SP-2026-M04",
                    "status": "ACCEPTED",
                    "result_set_sha256": prior_sha,
                    "evidence_package": {"package_manifest_sha256": package_sha},
                },
            )
            accepted = validate_prior_run(root, "SP-2026-M04", prior_sha, package_root)
            self.assertEqual(accepted["result_set_sha256"], prior_sha)

            package_path.write_text('{"schema_version":"1.1"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "do not match the prior accepted package"):
                validate_prior_run(root, "SP-2026-M04", prior_sha, package_root)


if __name__ == "__main__":
    unittest.main()
