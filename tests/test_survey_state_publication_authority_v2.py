from __future__ import annotations

import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts import survey_production_v2 as core


class SurveyStatePublicationAuthorityV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.impl = "1" * 40

    def sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source_cfg = core.load_json(self.source_root / core.DEFAULT_CONFIG)
        required = [
            "config/survey-production-v2.json",
            "config/weekly-pipeline.json",
            "schemas/survey-production-profile.schema.json",
            "schemas/survey-production-state.schema.json",
            *source_cfg["contract_files"]["pipeline"],
            *source_cfg["contract_files"]["quality"],
        ]
        for rel in dict.fromkeys(required):
            src = self.source_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        cfg = core.load_json(root / core.DEFAULT_CONFIG)
        profile = core.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "How did the synthetic lineage evolve?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T07:00:00Z",
                "scope_dimensions": ["lineage"],
            },
        )
        _, state_path = core.initialize(
            root,
            cfg,
            profile,
            self.impl,
            "ARCHITECTURE_REVIEW",
            datetime(2026, 8, 22, 7, 0, tzinfo=timezone.utc),
        )
        return temp, root, cfg, state_path

    def write_checkpoint_attestation(self, root: Path, cfg: dict, state: dict, checkpoint: str) -> dict[str, str]:
        profile_path = root / state["profile"]["path"]
        profile = core.load_json(profile_path)
        source_root = root / profile["paths"]["source_root"]
        artifact = source_root / "generated" / f"{checkpoint}.json"
        core.write_json(artifact, {"checkpoint": checkpoint, "issue_id": state["issue_id"]})
        attestation = source_root / cfg["state_authority"]["checkpoint_attestation_dir"] / f"{checkpoint}.json"
        core.write_json(
            attestation,
            {
                "schema_version": "2.0-rc1",
                "issue_id": state["issue_id"],
                "checkpoint": checkpoint,
                "action_id": f"action:test:{checkpoint}",
                "action_spec_sha256": "a" * 64,
                "validator": f"validate:{checkpoint}",
                "validator_version": "2.0-rc1",
                "validated_at": "2026-08-22T07:05:00Z",
                "required_inputs": [
                    {
                        "name": "production-profile",
                        "path": str(profile_path.relative_to(root)),
                        "sha256": core.sha256_file(profile_path),
                        "required": True,
                    }
                ],
                "outputs": [
                    {
                        "name": checkpoint,
                        "path": str(artifact.relative_to(root)),
                        "sha256": core.sha256_file(artifact),
                        "required": True,
                    }
                ],
                "status": "PASSED",
            },
        )
        return {"path": str(attestation.relative_to(root)), "sha256": core.sha256_file(attestation)}

    def approved_artifact_backed_state(self, root: Path, cfg: dict, state_path: Path) -> dict:
        state = core.load_json(state_path)
        source = root / "sources/SP001"
        completed = core._completed_stage_checkpoints(cfg, "RELEASE_CANDIDATE")
        for checkpoint in completed:
            state["machine_checkpoints"][checkpoint] = "passed"
            state["checkpoint_provenance"][checkpoint] = self.write_checkpoint_attestation(
                root, cfg, state, checkpoint
            )

        architecture = source / "architecture-v2.json"
        review = source / "architecture-review-summary-v2.json"
        attention = source / "architecture-review-attention-v2.json"
        core.write_json(architecture, {"fixture": "architecture"})
        core.write_json(review, {"fixture": "review"})
        core.write_json(attention, {"fixture": "attention"})
        architecture_approval = source / cfg["state_authority"]["architecture_approval_path"]
        core.write_json(
            architecture_approval,
            {
                "decision": "APPROVED",
                "issue_id": "SP001",
                "architecture_sha256": core.sha256_file(architecture),
                "architecture_review_summary_sha256": core.sha256_file(review),
                "architecture_review_attention_sha256": core.sha256_file(attention),
            },
        )
        state["human_gates"]["architecture_review"] = "approved"
        state["human_gate_provenance"]["architecture_review"] = {
            "path": str(architecture_approval.relative_to(root)),
            "sha256": core.sha256_file(architecture_approval),
        }

        candidate = source / "publication/v2/publication-candidate-v2.json"
        pdf_ref = {
            "storage": "GITHUB_ACTIONS_ARTIFACT",
            "path": "main.pdf",
            "sha256": "b" * 64,
            "byte_count": 12345,
            "page_count": 12,
            "actions_artifact": {
                "repository": "eariver/japanese-generative-ai-survey",
                "workflow_run_id": 123,
                "artifact_id": 456,
                "artifact_name": "survey-SP001-v0.1",
                "artifact_digest": "sha256:" + "c" * 64,
            },
        }
        core.write_json(
            candidate,
            {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "status": "READY_FOR_PUBLICATION_PREVIEW",
                "pdf": pdf_ref,
            },
        )
        preview = source / cfg["state_authority"]["publication_preview_approval_path"]
        core.write_json(
            preview,
            {
                "decision": "APPROVED",
                "gate": "PUBLICATION_PREVIEW",
                "issue_id": "SP001",
                "publication_candidate_path": str(candidate.relative_to(root)),
                "publication_candidate_sha256": core.sha256_file(candidate),
                "pdf_path": pdf_ref["path"],
                "pdf_sha256": pdf_ref["sha256"],
                "page_count": pdf_ref["page_count"],
            },
        )
        preview_authority = {"path": str(preview.relative_to(root)), "sha256": core.sha256_file(preview)}
        state["human_gates"]["publication_preview"] = "approved"
        state["human_gate_provenance"]["publication_preview"] = dict(preview_authority)
        state["machine_checkpoints"]["publication_preview"] = "passed"
        state["checkpoint_provenance"]["publication_preview"] = dict(preview_authority)
        state["lifecycle_state"] = "RELEASE_CANDIDATE"
        base = datetime(2026, 8, 22, 7, 0, tzinfo=timezone.utc)
        current_index = core.LIFECYCLE.index("RELEASE_CANDIDATE")
        state["history"] = [
            {
                "from": None if index == 0 else core.LIFECYCLE[index - 1],
                "to": core.LIFECYCLE[index],
                "recorded_at": core.iso_utc(base + timedelta(minutes=index)),
                "repository_commit_sha": self.impl,
            }
            for index in range(current_index + 1)
        ]
        state["target_gate"] = "PUBLICATION_PREVIEW"
        return core.refresh_state_control(state, cfg)

    def test_actions_artifact_preview_state_remains_valid_without_local_pdf(self) -> None:
        temp, root, cfg, state_path = self.sandbox()
        self.addCleanup(temp.cleanup)
        state = self.approved_artifact_backed_state(root, cfg, state_path)

        self.assertFalse((root / "main.pdf").exists())
        self.assertEqual(core.validate_state_semantics(root, cfg, state), [])
        core.verify_state_basis(root, cfg, state, self.impl)

    def test_actions_artifact_authority_tamper_fails_state_validation(self) -> None:
        temp, root, cfg, state_path = self.sandbox()
        self.addCleanup(temp.cleanup)
        state = self.approved_artifact_backed_state(root, cfg, state_path)
        candidate = root / "sources/SP001/publication/v2/publication-candidate-v2.json"
        payload = core.load_json(candidate)
        payload["pdf"]["actions_artifact"]["artifact_digest"] = "not-a-digest"
        core.write_json(candidate, payload)

        errors = core.validate_state_semantics(root, cfg, state)
        self.assertTrue(any("Candidate/PDF bytes" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
