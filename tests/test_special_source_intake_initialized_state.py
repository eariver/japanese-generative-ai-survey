from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.accept_special_source_intake_artifact import accept, build_initial_state, build_state


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class SpecialSourceIntakeInitializedStateTests(unittest.TestCase):
    def test_accept_transitions_exact_initialized_state_to_discovery(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = root / "repo"
            artifact = root / "artifact"
            slug = "TEST-M06"
            issue = f"SP-{slug}"
            edition = {
                "special_id": issue,
                "special_slug": slug,
                "edition_kind": "RETROSPECTIVE_PERIOD",
                "status": "ACTIVE",
                "coverage": {
                    "start": "2026-06-01T00:00:00Z",
                    "end": "2026-06-30T23:59:59Z",
                    "retrospective_as_of": "2026-08-11T06:22:00Z",
                },
                "community_research": {"mode": "DISABLED", "reason": "test"},
            }
            plan = {
                "series": "SPECIAL",
                "issue_id": issue,
                "special_slug": slug,
                "collection_window_start": edition["coverage"]["start"],
                "collection_window_end": edition["coverage"]["end"],
                "editorial_cutoff": edition["coverage"]["end"],
                "cutoff_timezone": "UTC",
                "retrospective_as_of": edition["coverage"]["retrospective_as_of"],
                "community_research": edition["community_research"],
            }
            dump(repo / "specials" / slug / "edition.json", edition)
            state_path = repo / "sources" / issue / "pipeline-state.json"
            dump(state_path, build_initial_state(edition, plan))
            dump(
                artifact / "special-source-intake" / "source-intake-report.json",
                {"issue_id": issue, "overall_status": "success"},
            )
            dump(artifact / "special-source-intake-control" / "plan.json", plan)
            raw = artifact / "special-source-intake" / "sources" / issue / "collectors" / "test" / "raw" / "response.bin"
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(b"exact raw bytes")

            result = accept(
                artifact_root=artifact,
                repo_root=repo,
                special_slug=slug,
                workflow_run_id=123,
                artifact_id=456,
                artifact_name="special-source-intake-TEST-M06",
                artifact_digest="sha256:" + "a" * 64,
                review_reference="unit test reviewed artifact",
            )

            self.assertEqual(result["state_transition"], "ISSUE_INITIALIZED -> DISCOVERY_COLLECTED")
            self.assertEqual(result["raw_file_count"], 1)
            self.assertEqual(json.loads(state_path.read_text(encoding="utf-8")), build_state(edition, plan))
            self.assertEqual(
                (repo / "sources" / issue / "collectors" / "test" / "raw" / "response.bin").read_bytes(),
                b"exact raw bytes",
            )

    def test_rejects_noncanonical_initialized_state(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = root / "repo"
            artifact = root / "artifact"
            slug = "TEST-M06"
            issue = f"SP-{slug}"
            edition = {
                "special_id": issue,
                "special_slug": slug,
                "edition_kind": "RETROSPECTIVE_PERIOD",
                "status": "ACTIVE",
                "coverage": {
                    "start": "2026-06-01T00:00:00Z",
                    "end": "2026-06-30T23:59:59Z",
                    "retrospective_as_of": "2026-08-11T06:22:00Z",
                },
                "community_research": {"mode": "DISABLED", "reason": "test"},
            }
            plan = {
                "series": "SPECIAL",
                "issue_id": issue,
                "special_slug": slug,
                "collection_window_start": edition["coverage"]["start"],
                "collection_window_end": edition["coverage"]["end"],
                "editorial_cutoff": edition["coverage"]["end"],
                "cutoff_timezone": "UTC",
                "retrospective_as_of": edition["coverage"]["retrospective_as_of"],
                "community_research": edition["community_research"],
            }
            dump(repo / "specials" / slug / "edition.json", edition)
            bad_state = build_initial_state(edition, plan)
            bad_state["calendar"]["collection_window_start"] = "2026-06-02T00:00:00Z"
            dump(repo / "sources" / issue / "pipeline-state.json", bad_state)
            dump(
                artifact / "special-source-intake" / "source-intake-report.json",
                {"issue_id": issue, "overall_status": "success"},
            )
            dump(artifact / "special-source-intake-control" / "plan.json", plan)
            raw = artifact / "special-source-intake" / "sources" / issue / "collectors" / "test" / "raw" / "response.bin"
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(b"exact raw bytes")

            with self.assertRaisesRegex(ValueError, "initialized state differs"):
                accept(
                    artifact_root=artifact,
                    repo_root=repo,
                    special_slug=slug,
                    workflow_run_id=123,
                    artifact_id=456,
                    artifact_name="special-source-intake-TEST-M06",
                    artifact_digest="sha256:" + "a" * 64,
                    review_reference="unit test reviewed artifact",
                )


if __name__ == "__main__":
    unittest.main()
