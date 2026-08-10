from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_candidate_comparison as comparison


class CandidateComparisonTests(unittest.TestCase):
    def _write_json(self, path: Path, value) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def _item(self, task_id: str, name: str, event_date: str | None, recommendation: str = "CANDIDATE") -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": task_id,
            "task_file": task_id.rsplit(":", 1)[-1] + ".json",
            "run_file": task_id.rsplit(":", 1)[-1] + ".json",
            "runner": {"provider": "test", "model": "model", "invocation": "unit"},
            "evidence_task_sha256": "0" * 64,
            "prompt_id": "primary-source-verification-v0.1",
            "prompt_sha256": "1" * 64,
            "card": {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "evidence_task_id": task_id,
                "status": "VERIFIED" if recommendation == "CANDIDATE" else "PARTIAL",
                "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
                "artifact": {
                    "canonical_name": name,
                    "artifact_type": "MODEL_UPDATE",
                    "organization": "Example",
                    "canonical_url": f"https://example.com/{name.lower().replace(' ', '-')}",
                },
                "temporal": {
                    "artifact_first_announced": event_date,
                    "observed_at": "2026-08-10T00:00:00Z",
                    "events": [] if event_date is None else [
                        {
                            "event_type": "MODEL_UPDATE",
                            "event_date": event_date,
                            "source_published_at": event_date,
                            "source_ids": ["s1"],
                        }
                    ],
                },
                "sources": [
                    {
                        "source_id": "s1",
                        "url": "https://example.com/source",
                        "source_class": "PRIMARY_OFFICIAL",
                        "title": "Source",
                        "published_at": event_date,
                        "accessed_at": "2026-08-10T00:00:00Z",
                        "role": "official",
                    }
                ],
                "claims": [
                    {
                        "claim_id": "c1",
                        "text": "Exists.",
                        "evidence_class": "PRIMARY_FACT",
                        "source_ids": ["s1"],
                        "context": None,
                    },
                    {
                        "claim_id": "c2",
                        "text": "Vendor says it is faster.",
                        "evidence_class": "VENDOR_CLAIM",
                        "source_ids": ["s1"],
                        "context": "vendor evaluation",
                    },
                ],
                "metrics": [],
                "limitations": [
                    {
                        "limitation_id": "l1",
                        "text": "No independent reproduction.",
                        "evidence_class": "INFERENCE",
                        "source_ids": ["s1"],
                    }
                ],
                "verification": {
                    "targets": [],
                    "unresolved_questions": [] if recommendation == "CANDIDATE" else ["Chronology needs confirmation."],
                    "contradictions": [],
                },
                "editorial": {
                    "why_now_confirmed": recommendation == "CANDIDATE",
                    "why_now_note": "in-window event" if recommendation == "CANDIDATE" else None,
                    "candidate_recommendation": recommendation,
                    "rationale": "Evidence routing rationale.",
                },
            },
        }

    def test_builds_all_evidence_routes_and_conservative_temporal_hints(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reviewed = root / "evidence-reviewed.jsonl"
            items = [
                self._item("evidence:2026-W32:pre", "Pre Window", "2026-07-31"),
                self._item("evidence:2026-W32:main", "Main Window", "2026-08-04"),
                self._item("evidence:2026-W32:cutoff", "Cutoff Day", "2026-08-07", "HOLD"),
                self._item("evidence:2026-W32:late", "Post Cutoff", "2026-08-08", "REJECT"),
            ]
            reviewed.write_text("\n".join(json.dumps(item) for item in items) + "\n", encoding="utf-8")

            tasks = root / "tasks"
            for item in items:
                task_id = item["evidence_task_id"]
                self._write_json(
                    tasks / (task_id.rsplit(":", 1)[-1] + ".json"),
                    {
                        "schema_version": "1.0",
                        "issue_id": "2026-W32",
                        "evidence_task_id": task_id,
                        "topic_lanes": ["A", "G"],
                    },
                )

            state = root / "pipeline-state.json"
            self._write_json(
                state,
                {
                    "schema_version": "1.0",
                    "issue_id": "2026-W32",
                    "calendar": {
                        "collection_window_start": "2026-08-01T00:00:00-04:00",
                        "editorial_cutoff": "2026-08-07T18:00:00-04:00",
                    },
                },
            )
            out = root / "out"
            manifest, passed = comparison.build(reviewed, tasks, state, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["record_count"], 4)
            records = [json.loads(line) for line in (out / "candidate-comparison-input.jsonl").read_text(encoding="utf-8").splitlines()]
            by_name = {row["artifact"]["canonical_name"]: row for row in records}
            self.assertEqual(by_name["Pre Window"]["temporal"]["position_hints"], ["PRE_WINDOW"])
            self.assertEqual(by_name["Main Window"]["temporal"]["position_hints"], ["MAIN_WINDOW"])
            self.assertEqual(by_name["Cutoff Day"]["temporal"]["position_hints"], ["CUTOFF_DAY_UNRESOLVED"])
            self.assertEqual(by_name["Post Cutoff"]["temporal"]["position_hints"], ["POST_CUTOFF"])
            self.assertIsNotNone(by_name["Main Window"]["candidate_id"])
            self.assertIsNone(by_name["Cutoff Day"]["candidate_id"])
            self.assertEqual(by_name["Main Window"]["claim_counts"], {"PRIMARY_FACT": 1, "VENDOR_CLAIM": 1})
            self.assertEqual(by_name["Main Window"]["topic_lanes"], ["A", "G"])

    def test_missing_task_fails_without_dropping_other_records(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reviewed = root / "evidence-reviewed.jsonl"
            item = self._item("evidence:2026-W32:missing", "Missing Task", "2026-08-04")
            reviewed.write_text(json.dumps(item) + "\n", encoding="utf-8")
            tasks = root / "tasks"
            tasks.mkdir()
            state = root / "pipeline-state.json"
            self._write_json(
                state,
                {
                    "issue_id": "2026-W32",
                    "calendar": {
                        "collection_window_start": "2026-08-01T00:00:00-04:00",
                        "editorial_cutoff": "2026-08-07T18:00:00-04:00",
                    },
                },
            )
            manifest, passed = comparison.build(reviewed, tasks, state, root / "out")
            self.assertFalse(passed)
            self.assertEqual(manifest["record_count"], 0)
            self.assertTrue(any("missing Evidence Task" in error for error in manifest["errors"]))


if __name__ == "__main__":
    unittest.main()
