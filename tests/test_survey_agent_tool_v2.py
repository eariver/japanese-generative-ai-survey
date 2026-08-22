from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core


class SurveyAgentToolV2Tests(unittest.TestCase):
    def test_archived_screening_may_revalidate_after_canonical_state_bytes_advance(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state_path = root / "sources/SP001/production-state.json"
            state_path.parent.mkdir(parents=True)
            core.write_json(state_path, {"current": "state-after-screening"})

            run_dir = root / "sources/SP001/screening/v2/accepted/run"
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
                run_dir / "screening-accepted.json",
                {"package_sha256": core.sha256_file(package_path)},
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


if __name__ == "__main__":
    unittest.main()
