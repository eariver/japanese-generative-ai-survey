import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialIssueOnlyReleaseTests(unittest.TestCase):
    def test_publication_preview_authorizes_deterministic_freeze_and_versionless_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            issue = "SP-TEST-M06"
            slug = "2026-M06"
            source_version = "v0.9"
            source = root / "surveys" / "special" / slug / "revisions" / source_version / "source-manifest.json"
            dump(source, {"schema_version": "1.0", "issue_id": issue, "source_version": source_version})
            top_main = root / "surveys" / "special" / slug / "main.tex"
            top_main.parent.mkdir(parents=True, exist_ok=True)
            top_main.write_text("\\documentclass{article}\n", encoding="utf-8")
            pdf = root / "main.pdf"
            pdf.write_bytes(b"%PDF-issue-only-test")
            pdf_sha = sha(pdf)

            state_path = root / "sources" / issue / "pipeline-state.json"
            state = {
                "schema_version": "1.0",
                "issue_id": issue,
                "lifecycle_state": "RELEASE_CANDIDATE",
                "revision": "internal-state-r1",
                "calendar": {"frozen_at": None},
                "gates": {
                    "latex_build": "passed",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
                "automation": {
                    "human_gate_model": "ARCHITECTURE_PUBLICATION_PREVIEW_WITH_EXCEPTION",
                    "unattended_public_release": False,
                    "human_gate_required_for_public_release": False,
                },
                "provenance": {
                    "validated_issue_source": {
                        "path": str(source.relative_to(root)),
                        "sha256": sha(source),
                        "source_version": source_version,
                    },
                    "latex_build": {
                        "pdf_sha256": pdf_sha,
                        "page_count": 34,
                        "workflow_run_id": 12345,
                        "source_version": source_version,
                    },
                },
            }
            dump(state_path, state)

            approved_at = "2026-08-13T09:00:00+09:00"
            approval_reference = "Publication Preview test approval"
            subprocess.run([
                sys.executable,
                "-m", "scripts.accept_special_visual_review_issue_only",
                "--repo-root", str(root),
                "--issue-id", issue,
                "--special-slug", slug,
                "--approved-pdf", str(pdf),
                "--approved-pdf-sha256", pdf_sha,
                "--approval-reference", approval_reference,
                "--approved-at", approved_at,
                "--artifact-name", "special-test-v0.9",
                "--artifact-id", "999",
                "--artifact-digest", "sha256:" + "b" * 64,
            ], check=True, cwd=ROOT, capture_output=True, text=True)

            approval = json.loads((root / "sources" / issue / "visual-review" / source_version / "approval.json").read_text(encoding="utf-8"))
            self.assertEqual(approval["approval_mode"], "PUBLICATION_PREVIEW_APPROVAL")
            self.assertEqual(approval["authorizes"], ["visual_review", "freeze", "work_pr_merge", "public_release"])

            candidate_path = root / "sources" / issue / "freeze" / "freeze-candidate.json"
            candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
            self.assertEqual(candidate["status"], "READY_FOR_DETERMINISTIC_FREEZE")
            self.assertEqual(candidate["publication_authority"]["mode"], "PUBLICATION_PREVIEW_APPROVAL")
            self.assertEqual(candidate["release_identity_mode"], "ISSUE_ONLY")
            self.assertEqual(candidate["release_tag"], "special/2026-M06")
            self.assertNotIn("proposed_release_revision", candidate)
            self.assertNotIn("v0.9", candidate["release_title"])
            self.assertNotIn("v0.9", candidate["asset_name"])

            subprocess.run([
                sys.executable,
                "-m", "scripts.accept_special_freeze_issue_only",
                "--repo-root", str(root),
                "--issue-id", issue,
                "--special-slug", slug,
                "--approved-at", approved_at,
                "--approval-reference", approval_reference,
            ], check=True, cwd=ROOT, capture_output=True, text=True)

            freeze = json.loads((root / "sources" / issue / "freeze" / "freeze.json").read_text(encoding="utf-8"))
            self.assertEqual(freeze["release_authority"], "PUBLICATION_PREVIEW_APPROVAL")
            manifest = json.loads((root / "sources" / issue / "release-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["release_identity_mode"], "ISSUE_ONLY")
            self.assertEqual(manifest["release_tag"], "special/2026-M06")
            self.assertEqual(manifest["asset_name"], "Japanese_Generative_AI_Technical_Survey_Special_2026-M06.pdf")
            self.assertNotIn("revision", manifest)
            self.assertEqual(manifest["source_version"], source_version)
            self.assertTrue(manifest["public_release_authorized"])
            self.assertEqual(manifest["release_authorization"]["mode"], "PUBLICATION_PREVIEW_APPROVAL")
            self.assertEqual(manifest["release_authorization"]["approval_reference"], approval_reference)
            current = (root / "surveys" / "special" / slug / "CURRENT_RELEASE.md").read_text(encoding="utf-8")
            self.assertIn("Canonical source", current)
            self.assertIn("not a public Release version", current)
            self.assertTrue(top_main.read_text(encoding="utf-8").startswith("% WORKSPACE ENTRY POINT"))

    def test_freeze_rejects_mismatched_new_approval_reference(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            issue = "SP-TEST-M06"
            slug = "2026-M06"
            source_version = "v0.9"
            source = root / "surveys" / "special" / slug / "revisions" / source_version / "source-manifest.json"
            dump(source, {"schema_version": "1.0", "issue_id": issue, "source_version": source_version})
            pdf = root / "main.pdf"
            pdf.write_bytes(b"%PDF-authority-test")
            pdf_sha = sha(pdf)
            state = {
                "schema_version": "1.0",
                "issue_id": issue,
                "lifecycle_state": "RELEASE_CANDIDATE",
                "calendar": {"frozen_at": None},
                "gates": {"latex_build": "passed", "visual_review": "pending", "freeze": "pending"},
                "automation": {"human_gate_model": "ARCHITECTURE_PUBLICATION_PREVIEW_WITH_EXCEPTION", "unattended_public_release": False, "human_gate_required_for_public_release": False},
                "provenance": {
                    "validated_issue_source": {"path": str(source.relative_to(root)), "sha256": sha(source), "source_version": source_version},
                    "latex_build": {"pdf_sha256": pdf_sha, "page_count": 1, "workflow_run_id": 7, "source_version": source_version},
                },
            }
            dump(root / "sources" / issue / "pipeline-state.json", state)
            approved_at = "2026-08-13T09:00:00+09:00"
            subprocess.run([
                sys.executable, "-m", "scripts.accept_special_visual_review_issue_only",
                "--repo-root", str(root), "--issue-id", issue, "--special-slug", slug,
                "--approved-pdf", str(pdf), "--approved-pdf-sha256", pdf_sha,
                "--approval-reference", "canonical preview approval", "--approved-at", approved_at,
                "--artifact-name", "artifact", "--artifact-id", "1", "--artifact-digest", "sha256:" + "c" * 64,
            ], check=True, cwd=ROOT, capture_output=True, text=True)
            failed = subprocess.run([
                sys.executable, "-m", "scripts.accept_special_freeze_issue_only",
                "--repo-root", str(root), "--issue-id", issue, "--special-slug", slug,
                "--approved-at", approved_at, "--approval-reference", "invented freeze approval",
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertFalse((root / "sources" / issue / "freeze" / "freeze.json").exists())


if __name__ == "__main__":
    unittest.main()
