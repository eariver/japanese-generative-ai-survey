from __future__ import annotations

import shutil
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality


class SurveyPublicationV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in [
            quality.QUALITY_SCHEMA,
            publication.CANDIDATE_SCHEMA,
            publication.PREVIEW_APPROVAL_SCHEMA,
            publication.VISUAL_REVIEW_SCHEMA,
            publication.FREEZE_SCHEMA,
            publication.RELEASE_MANIFEST_SCHEMA,
            publication.MERGE_VERIFICATION_SCHEMA,
            publication.RELEASE_RECORD_SCHEMA,
        ]:
            dst = self.root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.source_root / rel, dst)
        self.dir = self.root / "sources/SP001/publication"
        self.dir.mkdir(parents=True)
        self.source = self.dir / "SP001.tex"
        self.pdf = self.dir / "SP001.pdf"
        self.source.write_text("validated source\n", encoding="utf-8")
        self.pdf.write_bytes(b"%PDF-1.7\nfixture\n")

    def _checks(self) -> list[dict[str, str]]:
        return [
            {"check_id": check_id, "status": "PASS", "evidence": f"fixture:{check_id}"}
            for check_id in sorted(quality.REQUIRED_CHECKS)
        ]

    def _candidate(self) -> tuple[Path, Path]:
        bundle = self.dir / "quality-regression-bundle-v2.json"
        quality.build_bundle(self.root, "SP001", self.source, self.pdf, self._checks(), bundle)
        candidate = self.dir / "publication-candidate-v2.json"
        publication.build_candidate(
            self.root, "SP001", "LONGFORM_SPECIAL", self.source, self.pdf, 12, bundle, candidate
        )
        return bundle, candidate

    def test_exact_pdf_chain_reaches_release_without_new_human_gate(self) -> None:
        _, candidate = self._candidate()
        now = datetime(2026, 8, 22, 5, 0, tzinfo=timezone.utc)
        approval = self.dir / "publication-preview-approval-v2.json"
        publication.build_preview_approval(self.root, candidate, approval, "human-reviewer", now, "review:SP001:preview")
        visual = self.dir / "visual-review-v2.json"
        publication.build_visual_review(
            self.root,
            approval,
            [{"check_id": "ALL_PAGES_RENDERED", "status": "PASS", "detail": "all 12 pages inspected"}],
            "render-first-qa-v2",
            now,
            visual,
        )
        freeze = self.dir / "freeze-record-v2.json"
        manifest = self.dir / "release-manifest-v2.json"
        publication.build_freeze(self.root, candidate, approval, visual, now, freeze, manifest)
        verification = self.dir / "merge-verification-v2.json"
        publication.build_merge_verification(self.root, manifest, "a" * 40, now, verification)
        release = self.dir / "release-record-v2.json"
        publication.build_release_record(self.root, manifest, verification, now, "release:SP001", release)
        record = publication.validate_release_record(self.root, release)
        self.assertEqual(record["status"], "RELEASED")
        self.assertEqual(record["release_identity"], "special/SP001")

    def test_pdf_change_after_human_preview_invalidates_every_downstream_step(self) -> None:
        _, candidate = self._candidate()
        now = datetime(2026, 8, 22, 5, 0, tzinfo=timezone.utc)
        approval = self.dir / "publication-preview-approval-v2.json"
        publication.build_preview_approval(self.root, candidate, approval, "human-reviewer", now, "review:SP001:preview")
        self.pdf.write_bytes(b"%PDF-1.7\nchanged-after-review\n")
        with self.assertRaisesRegex(ValueError, "bytes drifted"):
            publication.validate_preview_approval(self.root, approval)

    def test_missing_coupled_regression_blocks_publication_candidate(self) -> None:
        checks = self._checks()[:-1]
        with self.assertRaisesRegex(ValueError, "regression family incomplete"):
            quality.build_bundle(
                self.root,
                "SP001",
                self.source,
                self.pdf,
                checks,
                self.dir / "quality-regression-bundle-v2.json",
            )

    def test_release_manifest_fails_if_frozen_source_changes(self) -> None:
        _, candidate = self._candidate()
        now = datetime(2026, 8, 22, 5, 0, tzinfo=timezone.utc)
        approval = self.dir / "publication-preview-approval-v2.json"
        publication.build_preview_approval(self.root, candidate, approval, "human-reviewer", now, "review:SP001:preview")
        visual = self.dir / "visual-review-v2.json"
        publication.build_visual_review(
            self.root,
            approval,
            [{"check_id": "ALL_PAGES_RENDERED", "status": "PASS", "detail": "all pages inspected"}],
            "render-first-qa-v2",
            now,
            visual,
        )
        freeze = self.dir / "freeze-record-v2.json"
        manifest = self.dir / "release-manifest-v2.json"
        publication.build_freeze(self.root, candidate, approval, visual, now, freeze, manifest)
        self.source.write_text("changed after freeze\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "frozen artifact bytes drift"):
            publication.validate_release_manifest(self.root, manifest)


if __name__ == "__main__":
    unittest.main()
