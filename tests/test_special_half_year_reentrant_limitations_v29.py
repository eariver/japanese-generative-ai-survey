from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import revise_special_half_year_review_repairs_v3 as legacy
from scripts import revise_special_half_year_review_repairs_v29 as repair


class HalfYearReentrantLimitationsV29Tests(unittest.TestCase):
    def _fixture(self, root: Path, *, note_text: str) -> tuple[str, Path]:
        issue_id = "SP-TEST-H2"
        source_dir = root / "surveys" / "special" / "test" / "revisions" / "v0.1"
        note_path = source_dir / "technical-notes" / "10-notes.tex"
        note_path.parent.mkdir(parents=True)
        note_path.write_text(note_text, encoding="utf-8")
        main_path = source_dir / "main.tex"
        main_path.write_text(
            "\\documentclass{article}\n"
            "\\begin{document}\n"
            "\\input{technical-notes/10-notes}\n"
            "\\end{document}\n",
            encoding="utf-8",
        )
        manifest = {
            "issue_id": issue_id,
            "source_version": "v0.1",
            "main_tex": {"path": "main.tex"},
            "articles": [
                {
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/10-notes.tex",
                }
            ],
        }
        manifest_path = source_dir / "source-manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        state_path = root / "sources" / issue_id / "pipeline-state.json"
        state_path.parent.mkdir(parents=True)
        state_path.write_text(
            json.dumps(
                {
                    "provenance": {
                        "validated_issue_source": {
                            "path": manifest_path.relative_to(root).as_posix(),
                            "sha256": repair._sha(manifest_path),
                            "source_version": "v0.1",
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        return issue_id, manifest_path

    def _marker(self, root: Path, issue_id: str, version: str = "v0.2") -> None:
        path = root / "sources" / issue_id / "editorial" / f"layout-revision-{version}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "layout_changes": {
                        "allow_reentrant_half_year_repairs": True,
                    }
                }
            ),
            encoding="utf-8",
        )

    def test_parent_clean_proof_requires_boundary_and_no_legacy_limitation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id, manifest_path = self._fixture(
                root,
                note_text=legacy.COMMON_BOUNDARY + "\n\\begin{technicalnote}{A}{主要資料}\n\\end{technicalnote}\n",
            )
            proof = repair._validate_parent_common_limitation_already_absent(root, issue_id)
            self.assertEqual(proof["parent_source_manifest_path"], manifest_path.relative_to(root).as_posix())
            self.assertEqual(proof["rendered_note_file_count"], 1)
            self.assertEqual(proof["generic_limitation_present_count"], 0)
            self.assertEqual(proof["common_boundary_present_count"], 1)

    def test_parent_with_legacy_limitation_cannot_use_reentrant_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id, _ = self._fixture(
                root,
                note_text=(
                    legacy.COMMON_BOUNDARY
                    + "\n"
                    + legacy.GENERIC_LIMITATION
                    + "\n\\begin{technicalnote}{A}{主要資料}\n\\end{technicalnote}\n"
                ),
            )
            with self.assertRaisesRegex(ValueError, "legacy repeated limitation still present"):
                repair._validate_parent_common_limitation_already_absent(root, issue_id)

    def test_parent_without_consolidated_boundary_cannot_use_reentrant_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id, _ = self._fixture(
                root,
                note_text="\\begin{technicalnote}{A}{主要資料}\n\\end{technicalnote}\n",
            )
            with self.assertRaisesRegex(ValueError, "COMMON_BOUNDARY missing"):
                repair._validate_parent_common_limitation_already_absent(root, issue_id)

    def test_final_delegate_bridges_exactly_once_and_rejects_proof_contradiction(self) -> None:
        calls: list[str] = []

        def clean(path: Path, evidence: dict[str, dict[str, object]]) -> tuple[int, int, int]:
            calls.append(path.name)
            return 2, 0, 3

        state = {"used": False}
        bridged = repair._reentrant_delegate(clean, state)
        self.assertEqual(bridged(Path("10-notes.tex"), {}), (2, 1, 3))
        self.assertEqual(bridged(Path("20-notes.tex"), {}), (2, 0, 3))
        self.assertEqual(calls, ["10-notes.tex", "20-notes.tex"])
        self.assertTrue(state["used"])

        def dirty(path: Path, evidence: dict[str, dict[str, object]]) -> tuple[int, int, int]:
            return 1, 1, 1

        with self.assertRaisesRegex(ValueError, "proof contradicted"):
            repair._reentrant_delegate(dirty, {"used": False})(Path("dirty.tex"), {})

    def test_persisted_audit_is_corrected_to_truthful_zero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id, _ = self._fixture(
                root,
                note_text=legacy.COMMON_BOUNDARY + "\n\\begin{technicalnote}{A}{主要資料}\n\\end{technicalnote}\n",
            )
            out = root / "surveys" / "special" / "test" / "revisions" / "v0.2"
            out.mkdir(parents=True)
            manifest_path = out / "source-manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "reader_facing_technical_notes": {"common_limitation_removed_count": 1},
                        "layout_revision": {"technical_notes_common_limitation_removed_count": 1},
                    }
                ),
                encoding="utf-8",
            )
            state_path = root / "sources" / issue_id / "pipeline-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["provenance"]["validated_issue_source"] = {
                "path": manifest_path.relative_to(root).as_posix(),
                "sha256": repair._sha(manifest_path),
                "source_version": "v0.2",
            }
            state_path.write_text(json.dumps(state), encoding="utf-8")
            proof = {
                "parent_source_version": "v0.1",
                "parent_source_manifest_path": "parent.json",
                "parent_source_manifest_sha256": "abc",
                "rendered_note_file_count": 1,
                "generic_limitation_present_count": 0,
                "common_boundary_present_count": 1,
            }
            result = repair._correct_persisted_reentrant_audit(
                root,
                issue_id,
                {
                    "source_manifest": manifest_path.relative_to(root).as_posix(),
                    "source_manifest_sha256": "old",
                    "technical_notes_common_limitation_removed_count": 1,
                },
                proof,
            )
            saved = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["reader_facing_technical_notes"]["common_limitation_removed_count"], 0)
            self.assertTrue(saved["reader_facing_technical_notes"]["common_limitation_already_absent_before_revision"])
            self.assertEqual(saved["layout_revision"]["technical_notes_common_limitation_removed_count"], 0)
            self.assertTrue(saved["layout_revision"]["technical_notes_common_limitation_already_absent_before_revision"])
            self.assertEqual(result["technical_notes_common_limitation_removed_count"], 0)
            updated_state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(
                updated_state["provenance"]["validated_issue_source"]["sha256"],
                repair._sha(manifest_path),
            )

    def test_build_wraps_final_rendered_delegate_and_restores_it(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            issue_id, _ = self._fixture(
                root,
                note_text=legacy.COMMON_BOUNDARY + "\n\\begin{technicalnote}{A}{主要資料}\n\\end{technicalnote}\n",
            )
            self._marker(root, issue_id)
            observed_removed: list[int] = []

            def underlying_repair(_path: Path, _evidence: dict[str, dict[str, object]]) -> tuple[int, int, int]:
                return 2, 0, 3

            def fake_base_build(_root: Path, _slug: str, _issue: str, version: str) -> dict[str, object]:
                _facts, removed, _checked = repair.base._ORIGINAL_REENRICH_NOTE_FILE(Path("dummy.tex"), {})
                observed_removed.append(removed)
                out = root / "surveys" / "special" / "test" / "revisions" / version
                out.mkdir(parents=True)
                manifest_path = out / "source-manifest.json"
                manifest_path.write_text(
                    json.dumps(
                        {
                            "reader_facing_technical_notes": {"common_limitation_removed_count": removed},
                            "layout_revision": {"technical_notes_common_limitation_removed_count": removed},
                        }
                    ),
                    encoding="utf-8",
                )
                state_path = root / "sources" / issue_id / "pipeline-state.json"
                state = json.loads(state_path.read_text(encoding="utf-8"))
                state["provenance"]["validated_issue_source"] = {
                    "path": manifest_path.relative_to(root).as_posix(),
                    "sha256": repair._sha(manifest_path),
                    "source_version": version,
                }
                state_path.write_text(json.dumps(state), encoding="utf-8")
                return {
                    "source_manifest": manifest_path.relative_to(root).as_posix(),
                    "source_manifest_sha256": repair._sha(manifest_path),
                    "technical_notes_common_limitation_removed_count": removed,
                }

            previous = repair.base._ORIGINAL_REENRICH_NOTE_FILE
            repair.base._ORIGINAL_REENRICH_NOTE_FILE = underlying_repair
            try:
                with patch.object(repair.base, "build", side_effect=fake_base_build):
                    result = repair.build(root, "test", issue_id, "v0.2")
                self.assertEqual(observed_removed, [1])
                self.assertEqual(result["technical_notes_common_limitation_removed_count"], 0)
                self.assertEqual(
                    result["half_year_reentrant_repair_contract"],
                    "EXPLICIT_PARENT_CLEAN_PROOF_V3_FINAL_RENDERED_DELEGATE",
                )
                self.assertIs(repair.base._ORIGINAL_REENRICH_NOTE_FILE, underlying_repair)
            finally:
                repair.base._ORIGINAL_REENRICH_NOTE_FILE = previous


if __name__ == "__main__":
    unittest.main()
