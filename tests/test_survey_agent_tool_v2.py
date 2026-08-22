from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core


class SurveyAgentToolV2Tests(unittest.TestCase):
    def _accepted_run(self, root: Path, kind: str, acceptance_name: str) -> tuple[Path, dict, Path]:
        state_path = root / "sources/SP001/production-state.json"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        core.write_json(state_path, {"current": f"state-after-{kind}"})
        run_dir = root / f"sources/SP001/{kind}/v2/accepted/run"
        run_dir.mkdir(parents=True)
        package_path = run_dir / "package.json"
        package = {
            "basis": {
                "state_path": "sources/SP001/production-state.json",
                "state_sha256": "0" * 64,
            }
        }
        core.write_json(package_path, package)
        core.write_json(
            run_dir / acceptance_name,
            {"package_sha256": core.sha256_file(package_path)},
        )
        return package_path, package, state_path

    def test_archived_screening_may_revalidate_after_canonical_state_bytes_advance(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package_path, package, state_path = self._accepted_run(
                root, "screening", "screening-accepted.json"
            )
            seen: list[str] = []

            def strict(repo_root: Path, path: Path, value: dict, implementation_sha: str) -> None:
                expected = core.sha256_file(repo_root / value["basis"]["state_path"])
                if value["basis"]["state_sha256"] != expected:
                    raise ValueError("Screening package basis drift: state_sha256")
                seen.append(value["basis"]["state_sha256"])

            wrapped = agent_tool._historical_screening_basis_wrapper(strict)
            wrapped(root, package_path, package, "f" * 40)
            self.assertEqual(seen, [core.sha256_file(state_path)])
            self.assertEqual(package["basis"]["state_sha256"], "0" * 64)

    def test_archived_evidence_may_revalidate_after_canonical_state_bytes_advance(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package_path, package, state_path = self._accepted_run(
                root, "evidence", "evidence-accepted.json"
            )
            seen: list[str] = []

            def strict(repo_root: Path, path: Path, value: dict, implementation_sha: str):
                expected = core.sha256_file(repo_root / value["basis"]["state_path"])
                if value["basis"]["state_sha256"] != expected:
                    raise ValueError("Evidence package basis drift: state_sha256")
                seen.append(value["basis"]["state_sha256"])
                return {"accepted": True}, []

            wrapped = agent_tool._historical_evidence_basis_wrapper(strict)
            result = wrapped(root, package_path, package, "f" * 40)
            self.assertEqual(result, ({"accepted": True}, []))
            self.assertEqual(seen, [core.sha256_file(state_path)])
            self.assertEqual(package["basis"]["state_sha256"], "0" * 64)

    def test_historical_state_exception_requires_content_addressed_acceptance(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state_path = root / "state.json"
            core.write_json(state_path, {"current": True})
            package_path = root / "package.json"
            package = {"basis": {"state_path": "state.json", "state_sha256": "0" * 64}}
            core.write_json(package_path, package)

            def strict(repo_root: Path, path: Path, value: dict, implementation_sha: str) -> None:
                raise ValueError("Screening package basis drift: state_sha256")

            wrapped = agent_tool._historical_screening_basis_wrapper(strict)
            with self.assertRaisesRegex(ValueError, "state_sha256"):
                wrapped(root, package_path, package, "f" * 40)

    def test_non_state_screening_drift_is_never_relaxed(self) -> None:
        def strict(repo_root: Path, path: Path, value: dict, implementation_sha: str) -> None:
            raise ValueError("Screening prompt contract drift")

        wrapped = agent_tool._historical_screening_basis_wrapper(strict)
        with self.assertRaisesRegex(ValueError, "prompt contract drift"):
            wrapped(Path("."), Path("package.json"), {}, "f" * 40)

    def test_non_state_evidence_drift_is_never_relaxed(self) -> None:
        def strict(repo_root: Path, path: Path, value: dict, implementation_sha: str):
            raise ValueError("Evidence prompt contract drift")

        wrapped = agent_tool._historical_evidence_basis_wrapper(strict)
        with self.assertRaisesRegex(ValueError, "prompt contract drift"):
            wrapped(Path("."), Path("package.json"), {}, "f" * 40)


if __name__ == "__main__":
    unittest.main()
