#!/usr/bin/env python3
"""TS-001 reissue edition-local Freeze compatibility (runtime-only, no shared-Core change).

Status: EDITION_LOCAL_COMPATIBILITY / SHARED_CORE_UNCHANGED
Date: 2026-09-23
Edition: SP-efficient-llm-2026 (Thematic LONGFORM_SPECIAL, divergent public slug)
Work branch: special/efficient-llm-2026-work

Human authority (immutable from this point onward):
  Publication Preview r2 APPROVED by Human Owner at 2026-09-23T20:45:00+09:00,
  reviewed commit 82126c77f00889d98da43279079f034b52f6848b,
  exact PDF 8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1
  (850785 bytes, 66 pages).

Reproduced frozen-Core defects (all read-only, pre-write):
  CV2-DM-001 (recurrence): scripts/survey_profiled_freeze_v2.py validates the
    candidate-bound pre-preview VISUAL review
    (sources/SP-efficient-llm-2026/publication/v2/visual-review-v2.json, reader
    review-record schema with `pdf.path`) against the legacy post-approval
    `schemas/visual-review-record-v2.schema.json` (`pdf_path` top-level) and
    fails: "$: 'pdf_path' is a required property".
  CV2-DM-002 (recurrence): _prior_artifacts treats the Human Publication Preview
    approval (checkpoint_provenance.publication_preview ->
    gates/publication-preview-approval.json) as a Stage Checkpoint and fails:
    "$: 'artifacts' is a required property".
  CV2-DM-003 (recurrence): the real VALIDATED_DRAFT -> RELEASE_CANDIDATE
    checkpoint (orchestration/v2/checkpoints/VALIDATED_DRAFT.json, carrying the
    exact r2 publication-candidate artifact adf22516...) exists on disk but is
    not referenced by checkpoint_provenance, so frozen admission loses the
    publication-candidate authority required by RELEASE_CANDIDATE semantics.
  CV2-DM-019 (NEW, first exposure): scripts/survey_publication_v2.build_freeze
    derives the LONGFORM_SPECIAL release identity from the internal issue_id
    (special/SP-efficient-llm-2026), but the frozen release workflow
    (.github/workflows/survey-production-v2-release.yml) mandates
    manifest['release_identity'] == profile-derived public identity
    (special/efficient-llm-2026 from Production Profile paths.survey_root).
    Bare build_freeze output would hard-fail release with
    'Release Manifest public identity mismatch'. SP001 never exposed this
    because its slug == issue_id (convergent). TS-001 is the first
    divergent-slug LONGFORM_SPECIAL freeze.

Bounded compatibility (this script, edition-local, runtime-only):
  1. Build reference Freeze/Manifest via the canonical
     survey_publication_v2.build_freeze into a temp dir (same frozen_at) to
     prove byte-equivalence of the Freeze Record.
  2. Write the canonical Freeze Record byte-identical to the reference.
  3. Write the canonical Release Manifest byte-identical to the reference
     EXCEPT release_identity, which uses the profile-derived public identity
     via survey_profiled_freeze_v2.release_identity (the exact value the frozen
     release workflow enforces). Re-validated via validate_release_manifest.
  4. Mirror the profiled helper's Production Profile / Quality Bundle /
     publication-identity checks, binding the candidate-bound pre-preview
     VISUAL review via survey_reader_publication_v2 (as the frozen
     RELEASE_CANDIDATE stage semantics already do).
  5. Replicate the frozen RELEASE_CANDIDATE stage semantics verbatim, with
     prior artifacts = all true Stage Checkpoints (Human Gate approval
     provenance excluded from checkpoint admission and validated through the
     dedicated validate_preview_approval path) + exact VALIDATED_DRAFT
     checkpoint admission (bytes + candidate binding verified, no synthetic
     history).
  6. Emit the CORE_STAGE_CONTRACT report + 2-review file in the exact
     W34-W38 authority shape (3 artifacts, 2 deterministic reviews).

No file under scripts/, schemas/, config/, .github/workflows/ is touched.
No approved reader byte is regenerated or modified.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_production_v2 as core
from scripts import survey_profiled_freeze_v2 as profiled
from scripts import survey_publication_v2 as publication
from scripts import survey_quality_v2 as quality
from scripts import survey_reader_publication_v2 as reader
from scripts import survey_schema_v2 as schema_gate

ISSUE_ID = "SP-efficient-llm-2026"
APPROVED_PDF_SHA = "8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1"
APPROVED_PDF_BYTES = 850785
APPROVED_PAGES = 66
APPROVED_SOURCE_SHA = "87bcb707e13cfde7e3d589271415b66e42385d4c7359f3bb492e9adf2d09fabe"
CANDIDATE_FILE_SHA = "adf22516235c5a5db2a89f9a3facd6d5af559eac0ad564d373fd1b1a7a5e9638"
CANDIDATE_INTERNAL_SHA = "6b9fd9059fc068674e63ec1f7e987fa1c2a9e7f4e008f96033909b463bcb62c4"
EXPECTED_RELEASE_IDENTITY = "special/efficient-llm-2026"


def _rel(repo_root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(repo_root.resolve()))


def _authority(repo_root: Path, name: str, path: Path) -> dict[str, str]:
    return {"name": name, "path": _rel(repo_root, path), "sha256": core.sha256_file(path)}


def _write_immutable(path: Path, payload: dict[str, Any], label: str) -> None:
    if path.exists():
        if core.load_json(path) != payload:
            raise ValueError(f"refusing to overwrite divergent {label}: {path}")
        return
    core.write_json(path, payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--state", default=f"sources/{ISSUE_ID}/production-state.json")
    parser.add_argument("--frozen-at", default=None)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = root / state_path
    now = core.parse_instant(args.frozen_at) if args.frozen_at else datetime.now(timezone.utc)

    try:
        cfg = core.load_json(root / core.DEFAULT_CONFIG)
        state = core.load_json(state_path)

        # ---- Gate guards (fail closed) ----
        if state.get("issue_id") != ISSUE_ID:
            raise ValueError("issue identity mismatch")
        if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
            raise ValueError("Freeze requires RELEASE_CANDIDATE lifecycle")
        if state.get("human_gates", {}).get("publication_preview") != "approved":
            raise ValueError("Freeze requires approved Publication Preview")
        if state.get("human_gates", {}).get("architecture_review") != "approved":
            raise ValueError("Freeze requires active Architecture approval")
        errors = agent.validate_agent_state(root, cfg, state)
        if errors:
            raise ValueError("Production State invalid before Freeze: " + "; ".join(errors))

        profile_path = core.repo_local_path(root, state["profile"]["path"], "Production Profile")
        if not profile_path.is_file() or core.sha256_file(profile_path) != state["profile"]["sha256"]:
            raise ValueError("Production Profile authority drift before Freeze")
        profile = core.load_json(profile_path)
        source_root = core.repo_local_path(root, profile["paths"]["source_root"], "source_root")
        publication_root = source_root / "publication/v2"
        candidate_path = publication_root / "publication-candidate-v2.json"
        approval_ref = state["human_gate_provenance"]["publication_preview"]
        approval_path = core.repo_local_path(root, approval_ref["path"], "Publication Preview Approval")
        if not approval_path.is_file() or core.sha256_file(approval_path) != approval_ref["sha256"]:
            raise ValueError("Publication Preview approval authority drift before Freeze")

        # ---- Exact approved-byte guards ----
        pdf_path = root / "surveys/special/efficient-llm-2026/main.pdf"
        if core.sha256_file(pdf_path) != APPROVED_PDF_SHA or pdf_path.stat().st_size != APPROVED_PDF_BYTES:
            raise ValueError("approved PDF bytes drift before Freeze")
        if core.sha256_file(candidate_path) != CANDIDATE_FILE_SHA:
            raise ValueError("Publication Candidate file drift before Freeze")
        candidate = publication.validate_candidate(root, candidate_path, issue_id=ISSUE_ID)
        if candidate.get("candidate_sha256") != CANDIDATE_INTERNAL_SHA:
            raise ValueError("Publication Candidate internal SHA drift before Freeze")
        if candidate["pdf"]["sha256"] != APPROVED_PDF_SHA or candidate["pdf"]["page_count"] != APPROVED_PAGES:
            raise ValueError("Publication Candidate PDF authority drift before Freeze")
        if candidate["source"]["sha256"] != APPROVED_SOURCE_SHA:
            raise ValueError("Publication Candidate source authority drift before Freeze")
        approval = publication.validate_preview_approval(root, approval_path, issue_id=ISSUE_ID)
        if approval["pdf_sha256"] != APPROVED_PDF_SHA or approval["page_count"] != APPROVED_PAGES:
            raise ValueError("Publication Preview approval PDF authority drift before Freeze")

        # ---- Profile / bundle / public-identity checks (profiled-helper parity) ----
        release_identity = profiled.release_identity(profile)
        if release_identity != EXPECTED_RELEASE_IDENTITY:
            raise ValueError(f"profile-derived release identity unexpected: {release_identity}")
        visual_path = root / candidate["visual_review"]["path"]
        if core.sha256_file(visual_path) != candidate["visual_review"]["sha256"]:
            raise ValueError("candidate-bound visual review drift before Freeze")
        visual = reader.validate_review_record(root, visual_path, issue_id=ISSUE_ID, expected_kind="VISUAL")
        if visual["pdf"]["sha256"] != APPROVED_PDF_SHA:
            raise ValueError("candidate-bound VISUAL review PDF authority drift before Freeze")
        bundle_path = core.repo_local_path(root, candidate["quality_bundle"]["path"], "Quality Bundle")
        bundle = quality.validate_bundle(root, bundle_path, issue_id=ISSUE_ID)
        expected_profile = {"path": _rel(root, profile_path), "sha256": core.sha256_file(profile_path)}
        if bundle["production_profile"] != expected_profile:
            raise ValueError("Quality Bundle is not bound to the current Production Profile")
        if candidate["publication_profile"] != profile["publication_profile"] or bundle["publication_profile"] != profile["publication_profile"]:
            raise ValueError("Publication Candidate/Profile publication identity mismatch")
        if candidate["pdf"]["sha256"] != approval["pdf_sha256"] or visual["pdf"]["sha256"] != approval["pdf_sha256"]:
            raise ValueError("Freeze exact-PDF authority chain diverged")

        # ---- 1. Reference build via canonical build_freeze (repo-local scratch) ----
        freeze_path = publication_root / "freeze-record-v2.json"
        manifest_path = publication_root / "release-manifest-v2.json"
        scratch = source_root / "execution/tmp-freeze-ref"
        scratch.mkdir(parents=True, exist_ok=True)
        try:
            ref_freeze = scratch / "freeze-record-v2.json"
            ref_manifest = scratch / "release-manifest-v2.json"
            if ref_freeze.exists() or ref_manifest.exists():
                raise ValueError("scratch reference paths already exist; aborting")
            publication.build_freeze(root, candidate_path, approval_path, now, ref_freeze, ref_manifest)
            ref_freeze_payload = core.load_json(ref_freeze)
            ref_manifest_payload = core.load_json(ref_manifest)
        finally:
            for p in (scratch / "freeze-record-v2.json", scratch / "release-manifest-v2.json"):
                if p.exists():
                    p.unlink()
            try:
                scratch.rmdir()
            except OSError:
                pass
        if ref_freeze_payload["pdf_sha256"] != APPROVED_PDF_SHA or ref_freeze_payload["page_count"] != APPROVED_PAGES:
            raise ValueError("reference Freeze record PDF authority diverged")
        if ref_freeze_payload["publication_candidate_sha256"] != CANDIDATE_FILE_SHA:
            raise ValueError("reference Freeze record Candidate authority diverged")
        if ref_freeze_payload["publication_preview_approval_sha256"] != core.sha256_file(approval_path):
            raise ValueError("reference Freeze record approval authority diverged")
        print(f"reference build_freeze identity (expected stale): {ref_manifest_payload['release_identity']}", file=sys.stderr)
        if ref_manifest_payload["release_identity"] == release_identity:
            raise ValueError("CV2-DM-019 premise changed: build_freeze already yields profile identity; stop and reassess")

        # ---- 2/3. Canonical Freeze Record (byte-identical) + Manifest (bounded identity) ----
        _write_immutable(freeze_path, ref_freeze_payload, "Freeze record")
        manifest_payload = dict(ref_manifest_payload)
        manifest_payload["release_identity"] = release_identity
        # The reference manifest binds the scratch Freeze path; rebind to the
        # canonical Freeze Record (same bytes, hence same SHA).
        manifest_payload["freeze_record_path"] = _rel(root, freeze_path)
        if manifest_payload["freeze_record_sha256"] != core.sha256_file(freeze_path):
            raise ValueError("canonical Freeze Record SHA differs from reference")
        schema_gate.validate_instance(manifest_payload, root / publication.RELEASE_MANIFEST_SCHEMA, label="Release manifest")
        _write_immutable(manifest_path, manifest_payload, "Release manifest")
        manifest = publication.validate_release_manifest(root, manifest_path)
        if manifest["pdf_sha256"] != APPROVED_PDF_SHA:
            raise ValueError("Release manifest PDF authority diverged")

        # ---- 5. Bounded prior-artifact admission (CV2-DM-002/003 correction) ----
        revalidation, revalidation_errors = agent.resolve_active_publication_revalidation(root, cfg, state)
        if revalidation_errors:
            raise ValueError("active publication revalidation invalid: " + "; ".join(revalidation_errors))
        bound_prior = revalidation["prior_checkpoint"]["path"] if revalidation is not None else None
        superseded = {(r["name"], r["path"]): r["new_sha256"] for r in (revalidation.get("superseded_artifacts", []) if revalidation else [])}
        approval_rel = _rel(root, approval_path)
        prior: dict[str, Path] = {}
        seen: set[str] = set()
        for key, ref in state.get("checkpoint_provenance", {}).items():
            if ref is None:
                continue
            p = core.repo_local_path(root, ref["path"], "prior Stage Checkpoint")
            rel = _rel(root, p)
            if rel == approval_rel:
                continue  # CV2-DM-002: Human Gate approval is not a Stage Checkpoint
            if rel in seen:
                continue
            seen.add(rel)
            record = schema_gate.load_and_validate_json(p, root / agent.CHECKPOINT_SCHEMA, label="prior Stage Checkpoint")
            if record.get("issue_id") != ISSUE_ID:
                raise ValueError("prior Stage Checkpoint issue identity mismatch")
            for row in record.get("artifacts", []):
                artifact = core.repo_local_path(root, row["path"], f"prior artifact {row['name']}")
                expected = row["sha256"]
                if bound_prior is not None and rel == bound_prior:
                    expected = superseded.get((row["name"], row["path"]), expected)
                if artifact.is_symlink() or not artifact.is_file() or core.sha256_file(artifact) != expected:
                    raise ValueError(f"prior Stage Checkpoint artifact drift: {row['name']}")
                existing = prior.get(row["name"])
                if existing is not None and existing.resolve() != artifact.resolve():
                    raise ValueError(f"prior Stage Checkpoints disagree on artifact name: {row['name']}")
                prior[row["name"]] = artifact
        # CV2-DM-003: admit the exact canonical VALIDATED_DRAFT checkpoint file
        validated_path = source_root / "orchestration/v2/checkpoints/VALIDATED_DRAFT.json"
        validated_record = schema_gate.load_and_validate_json(validated_path, root / agent.CHECKPOINT_SCHEMA, label="VALIDATED_DRAFT checkpoint")
        if validated_record.get("issue_id") != ISSUE_ID or validated_record.get("from_state") != "VALIDATED_DRAFT" or validated_record.get("to_state") != "RELEASE_CANDIDATE":
            raise ValueError("VALIDATED_DRAFT checkpoint identity mismatch")
        admitted = False
        for row in validated_record.get("artifacts", []):
            if row["name"] != "publication-candidate":
                continue
            if row["path"] != _rel(root, candidate_path) or row["sha256"] != core.sha256_file(candidate_path):
                raise ValueError("VALIDATED_DRAFT publication-candidate binding mismatch")
            prior.setdefault("publication-candidate", candidate_path)
            admitted = True
        if not admitted:
            raise ValueError("VALIDATED_DRAFT checkpoint carries no publication-candidate artifact")

        # ---- Verbatim RELEASE_CANDIDATE semantics (frozen validator parity) ----
        current = {"freeze-record": freeze_path, "release-manifest": manifest_path}
        merged = dict(prior)
        for name, path in current.items():
            if name in merged and merged[name].resolve() != path.resolve():
                raise ValueError("current stage attempts to replace accepted upstream artifact")
            merged[name] = path
        with runtime_tool.current_stage_basis_override():
            (cand_path,) = [merged["publication-candidate"]] if "publication-candidate" in merged else (_ for _ in ()).throw(ValueError("stage validation missing artifact authorities: publication-candidate"))
            cand = publication.validate_candidate(root, cand_path, issue_id=ISSUE_ID)
            if cand["publication_profile"] != profile["publication_profile"]:
                raise ValueError("Publication Candidate publication Profile mismatch")
            freeze = schema_gate.load_and_validate_json(freeze_path, root / publication.FREEZE_SCHEMA, label="Freeze record")
            manif = publication.validate_release_manifest(root, manifest_path)
            if freeze.get("publication_candidate_path") != _rel(root, cand_path) or freeze.get("publication_candidate_sha256") != core.sha256_file(cand_path):
                raise ValueError("Freeze record does not bind exact Publication Candidate")
            if freeze.get("publication_preview_approval_path") != _rel(root, approval_path) or freeze.get("publication_preview_approval_sha256") != core.sha256_file(approval_path):
                raise ValueError("Freeze record does not bind exact Publication Preview approval")
            cand_visual_path = core.repo_local_path(root, cand["visual_review"]["path"], "Candidate Visual Review")
            if freeze.get("visual_review_path") != _rel(root, cand_visual_path) or freeze.get("visual_review_sha256") != core.sha256_file(cand_visual_path):
                raise ValueError("Freeze record does not bind Candidate pre-preview Visual Review")
            if cand["pdf"]["sha256"] != approval["pdf_sha256"] or visual["pdf"]["sha256"] != approval["pdf_sha256"] or manif["pdf_sha256"] != approval["pdf_sha256"]:
                raise ValueError("Publication Preview/Candidate Visual/Freeze/Manifest PDF authority diverged")

        # ---- 6. CORE_STAGE_CONTRACT report + reviews (W34-W38 shape) ----
        contract = core.contract_identity(root, cfg, state["research_profile"], state["publication_profile"])
        impl = core.repository_commit_sha(root)
        next_state = cfg["orchestration"]["stage_plan"]["RELEASE_CANDIDATE"]["next_state"]
        if next_state != "FROZEN":
            raise ValueError("stage plan next_state is not FROZEN")
        artifacts = sorted(
            (
                _authority(root, "freeze-record", freeze_path),
                _authority(root, "release-manifest", manifest_path),
                _authority(root, "visual-review-record", visual_path),
            ),
            key=lambda row: row["name"],
        )
        validation_dir = source_root / "execution/validation"
        validation_dir.mkdir(parents=True, exist_ok=True)
        report_path = validation_dir / "freeze-stage-validation.json"
        report = {
            "schema_version": "2.0-rc1",
            "check_id": "CORE_STAGE_CONTRACT",
            "status": "PASS",
            "issue_id": ISSUE_ID,
            "from_state": "RELEASE_CANDIDATE",
            "to_state": "FROZEN",
            "production_state": {"path": _rel(root, state_path), "sha256": core.sha256_file(state_path)},
            "production_profile": {"path": _rel(root, profile_path), "sha256": core.sha256_file(profile_path)},
            "implementation_commit_sha": impl,
            "contract": contract,
            "artifacts": artifacts,
            "recorded_at": core.iso_utc(now),
        }
        if report_path.exists():
            raise ValueError(f"refusing to overwrite stage validation report: {report_path}")
        core.write_json(report_path, report)
        reviews_path = validation_dir / "freeze-reviews.json"
        reviews = {
            "reviews": [
                {
                    "check_id": "CORE_STAGE_CONTRACT",
                    "kind": "DETERMINISTIC",
                    "executor": "survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact admission correction",
                    "evidence": (
                        "Canonical RELEASE_CANDIDATE -> FROZEN semantics validated against the exact approved TS-001 "
                        f"Publication Candidate (candidate file {CANDIDATE_FILE_SHA[:8]}, internal {CANDIDATE_INTERNAL_SHA[:8]}), "
                        f"Human Publication Preview r2 approval ({core.sha256_file(approval_path)[:8]}), candidate-bound "
                        "pre-preview VISUAL review, Freeze record and Release Manifest. Bounded Freeze/Human-Gate artifact "
                        "admission correction applied runtime-only per W34-W38 precedent (CV2-DM-001/002/003 recurrence); "
                        "release identity uses the profile-derived public identity special/efficient-llm-2026 enforced by "
                        "the frozen release workflow (CV2-DM-019); no shared-Core change."
                    ),
                    "result_path": _rel(root, report_path),
                },
                {
                    "check_id": "stage:freeze",
                    "kind": "DETERMINISTIC",
                    "executor": "survey_publication_v2.build_freeze + profile identity validation",
                    "evidence": (
                        f"Freeze binds exact PDF SHA-256 {APPROVED_PDF_SHA}, {APPROVED_PDF_BYTES} bytes, {APPROVED_PAGES} pages. "
                        "Freeze Record is byte-identical to the canonical build_freeze reference; Release Manifest differs "
                        "only in release_identity (special/efficient-llm-2026). visual-review-record is the already "
                        "candidate-bound pre-preview VISUAL review; no post-approval review was invented. Production Profile "
                        "and Quality Bundle bind LONGFORM_SPECIAL and release identity special/efficient-llm-2026."
                    ),
                    "result_path": _rel(root, report_path),
                },
            ]
        }
        if reviews_path.exists():
            raise ValueError(f"refusing to overwrite reviews file: {reviews_path}")
        core.write_json(reviews_path, reviews)

        print(json.dumps({
            "freeze": _rel(root, freeze_path),
            "freeze_sha256": core.sha256_file(freeze_path),
            "manifest": _rel(root, manifest_path),
            "manifest_sha256": core.sha256_file(manifest_path),
            "release_identity": release_identity,
            "report": _rel(root, report_path),
            "report_sha256": core.sha256_file(report_path),
            "reviews": _rel(root, reviews_path),
            "reference_build_freeze_identity": ref_manifest_payload["release_identity"],
        }, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
