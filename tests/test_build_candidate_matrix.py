from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_candidate_matrix as bcm


class CandidateMatrixTests(unittest.TestCase):
    def _item(
        self,
        title: str,
        event_date: str | None,
        *,
        recommendation: str = "CANDIDATE",
        status: str = "VERIFIED",
        why_now: bool = True,
        limitations: bool = False,
    ) -> dict:
        events = [] if event_date is None else [{
            "event_type": "MODEL_UPDATE",
            "event_date": event_date,
            "source_published_at": event_date,
            "source_ids": ["s1"],
        }]
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": f"evidence:2026-W32:{title.lower().replace(' ', '-')}-12345678",
            "card": {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "evidence_task_id": f"evidence:2026-W32:{title.lower().replace(' ', '-')}-12345678",
                "status": status,
                "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
                "artifact": {"canonical_name": title, "artifact_type": "MODEL_UPDATE", "organization": "Org", "canonical_url": "https://example.com"},
                "temporal": {"artifact_first_announced": event_date, "observed_at": "2026-08-10T00:00:00Z", "events": events},
                "sources": [{"source_id": "s1", "source_class": "PRIMARY_OFFICIAL"}],
                "claims": [{"claim_id": "c1", "text": "exists", "evidence_class": "PRIMARY_FACT", "source_ids": ["s1"], "context": None}],
                "metrics": [{"metric_id": "m1", "name": "speed", "value": "2", "unit": "x", "context": "project setup", "evidence_class": "PROJECT_CLAIM", "source_ids": ["s1"]}],
                "limitations": ([{"limitation_id": "l1", "text": "No independent reproduction.", "evidence_class": "INFERENCE", "source_ids": ["s1"]}] if limitations else []),
                "verification": {"targets": [], "unresolved_questions": [], "contradictions": []},
                "editorial": {"why_now_confirmed": why_now, "why_now_note": None, "candidate_recommendation": recommendation, "rationale": "test"},
            },
        }

    def _write_inputs(self, root: Path, items: list[dict]) -> tuple[Path, Path]:
        reviewed = root / "evidence-reviewed.jsonl"
        reviewed.write_text("".join(json.dumps(item) + "\n" for item in items), encoding="utf-8")
        state = root / "pipeline-state.json"
        state.write_text(json.dumps({
            "issue_id": "2026-W32",
            "calendar": {
                "collection_window_start": "2026-08-01T00:00:00-04:00",
                "editorial_cutoff": "2026-08-07T18:00:00-04:00",
            },
        }), encoding="utf-8")
        return reviewed, state

    def test_timing_preserves_cutoff_day_date_only_uncertainty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reviewed, state = self._write_inputs(root, [
                self._item("Main exact", "2026-08-07T16:00:00-04:00"),
                self._item("Post exact", "2026-08-07T20:00:00-04:00"),
                self._item("Cutoff date only", "2026-08-07"),
                self._item("Pre relevant", "2026-07-31", why_now=True),
            ])
            matrix = bcm.build(reviewed, state)
            relation = {row["title"]: row["timing_relation"] for row in matrix["rows"]}
            self.assertEqual(relation["Main exact"], "MAIN_EVENT")
            self.assertEqual(relation["Post exact"], "POST_CUTOFF")
            self.assertEqual(relation["Cutoff date only"], "TIMING_UNRESOLVED")
            self.assertEqual(relation["Pre relevant"], "PRE_WINDOW_RELEVANCE")
            self.assertIsNone(matrix["ranking"])

    def test_readiness_is_non_ranking_and_keeps_caveats(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reviewed, state = self._write_inputs(root, [
                self._item("Clean", "2026-08-05T00:00:00Z"),
                self._item("Caveat", "2026-08-05T00:00:00Z", limitations=True),
                self._item("Hold", "2026-08-05T00:00:00Z", recommendation="HOLD", status="PARTIAL"),
            ])
            matrix = bcm.build(reviewed, state)
            readiness = {row["title"]: row["comparison_readiness"] for row in matrix["rows"]}
            self.assertEqual(readiness["Clean"], "READY")
            self.assertEqual(readiness["Caveat"], "READY_WITH_CAVEAT")
            self.assertEqual(readiness["Hold"], "HOLD")
            caveat = next(row for row in matrix["rows"] if row["title"] == "Caveat")
            self.assertIn("No independent reproduction.", caveat["remaining_boundaries"])
            self.assertEqual(caveat["evidence_class_counts"]["PROJECT_CLAIM"], 1)


if __name__ == "__main__":
    unittest.main()
