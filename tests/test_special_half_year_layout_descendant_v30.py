from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import revise_special_half_year_review_repairs_v30 as repair


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class HalfYearLayoutDescendantV30Tests(unittest.TestCase):
    def _fixture(self, root: Path, *, parent_status: str = "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION") -> str:
        issue_id = "SP-TEST-H2"
        revisions = root / "surveys" / "special" / "test" / "revisions"
        parent_dir = revisions / "v0.10"
        parent_dir.mkdir(parents=True)
        parent_manifest = parent_dir / "source-manifest.json"
        parent_manifest.write_text(json.dumps({"status": parent_status}), encoding="utf-8")

        current_dir = revisions / "v0.11"
        current_dir.mkdir(parents=True)
        current_manifest = current_dir / "source-manifest.json"
        current_manifest.write_text(
            json.dumps(
                {
                    "status": "VALIDATED_DENSE_THEME_TABLE_LAYOUT_REVISION",
                    "basis": {
                        "previous_source_manifest_path": parent_manifest.relative_to(root).as_posix(),
                        "previous_source_manifest_sha256": sha(parent_manifest),
                    },
                    "reader_facing_technical_notes": {
                        "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED"
                    },
                    "half_year_analysis": {
                        "path": "half-year-analysis/80-half-year-analysis.tex",
                        "selected_evidence_only": True,
                    },
                    "layout_revision": {
                        "reader_content_changed": False,
                        "technical_notes_content_changed": False,
                        "new_external_evidence": False,
                    },
                }
            ),
            encoding="utf-8",
        )
        state_path = root / "sources" / issue_id / "pipeline-state.json"
        state_path.parent.mkdir(parents=True)
        state_path.write_text(
            json.dumps(
                {
                    "provenance": {
                        "validated_issue_source": {
                            "path": current_manifest.relative_to(root).as_posix(),
                            "sha256": sha(current_manifest),
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        return issue_id

    def test_hash_pinned_layout_only_descendant_is_proven_incremental(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id = self._fixture(root)
            proof = repair._prove_incremental_layout_descendant(root, issue_id)
            self.assertIsNotNone(proof)
            assert proof is not None
            self.assertEqual(proof["current_status"], "VALIDATED_DENSE_THEME_TABLE_LAYOUT_REVISION")
            self.assertEqual(proof["parent_status"], "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION")
            self.assertEqual(proof["contract"], "HASH_PINNED_LAYOUT_ONLY_DESCENDANT_TO_INCREMENTAL_V1")

    def test_layout_descendant_with_unrepaired_parent_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id = self._fixture(root, parent_status="VALIDATED_DRAFT")
            with self.assertRaisesRegex(ValueError, "parent is not a recognized structurally repaired"):
                repair._prove_incremental_layout_descendant(root, issue_id)

    def test_layout_descendant_that_changed_reader_content_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id = self._fixture(root)
            state = json.loads((root / "sources" / issue_id / "pipeline-state.json").read_text(encoding="utf-8"))
            current = root / state["provenance"]["validated_issue_source"]["path"]
            manifest = json.loads(current.read_text(encoding="utf-8"))
            manifest["layout_revision"]["reader_content_changed"] = True
            current.write_text(json.dumps(manifest), encoding="utf-8")
            state["provenance"]["validated_issue_source"]["sha256"] = sha(current)
            (root / "sources" / issue_id / "pipeline-state.json").write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "changed reader content"):
                repair._prove_incremental_layout_descendant(root, issue_id)

    def test_build_temporarily_admits_proven_status_to_v8_incremental_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id = self._fixture(root)
            status = "VALIDATED_DENSE_THEME_TABLE_LAYOUT_REVISION"
            self.assertNotIn(status, repair.incremental._ALREADY_STRUCTURALLY_REPAIRED)

            def fake_build(_root: Path, _slug: str, _issue: str, _version: str):
                self.assertIn(status, repair.incremental._ALREADY_STRUCTURALLY_REPAIRED)
                return {"source_manifest": "dummy.json"}

            with patch.object(repair.base.base, "build", side_effect=fake_build):
                result = repair.build(root, "test", issue_id, "v0.12")
            self.assertNotIn(status, repair.incremental._ALREADY_STRUCTURALLY_REPAIRED)
            self.assertEqual(
                result["incremental_parent_recognition_contract"],
                "HASH_PINNED_LAYOUT_ONLY_DESCENDANT_TO_INCREMENTAL_V1",
            )


if __name__ == "__main__":
    unittest.main()
