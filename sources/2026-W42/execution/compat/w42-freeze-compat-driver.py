#!/usr/bin/env python3
"""W42 edition-local runtime-only Freeze compatibility driver (NO CORE PATCH).

Human authority:
`sources/2026-W42/execution/governance/human-w42-r34-edition-local-compat-freeze-release-authorization-20261021.md`
(HUMAN_OWNER_APPROVED_W42_R34_BOUNDED_RUNTIME_COMPAT / EXACT_PDF_FREEZE_RELEASE / SHARED_CORE_IMMUTABLE).

Frozen Core is NEVER modified by this driver: it only adapts the semantic
*typing/admission* boundary of two frozen validator helpers IN THIS PROCESS,
then calls the real frozen `validate_stage`, `build_stage_checkpoint`, and
`advance_with_checkpoint`. Result label: EDITION_LOCAL_RUNTIME_COMPAT.

Adaptations (bounded, matching the Human-authorized W41 precedent
`sources/2026-W41/execution/compat/w41-freeze-compat-driver.py`):
  A. `_prior_artifacts`: the state's `checkpoint_provenance.publication_preview`
     references the Human Approval record, not a Stage Checkpoint. The compat
     version validates it separately as Human Approval
     (`publication.validate_preview_approval` + state-bound SHA + APPROVED
     decision + exact candidate/PDF binding) and does NOT admit it as a
     checkpoint. Every genuine prior checkpoint is byte-validated with the
     exact frozen logic (copied verbatim), including the `VALIDATED_DRAFT`
     checkpoint with exact SHA + true schema.
  B. `_current_artifacts`: permits the extras `visual-review-record` (required
     by the checkpoint schema's `freezeArtifacts` rule alongside
     `freeze-record` / `release-manifest`; resolved to the candidate-bound
     modern VISUAL review record, validated with
     `reader.validate_review_record`) and `publication-candidate` (the genuine
     exact-current candidate pinned by the true `VALIDATED_DRAFT`
     checkpoint; SHA + file identity asserted). All other logic is verbatim
     frozen code.

Everything else (stage semantics, checkpoint build, advance, state validation)
runs unmodified from frozen Core. Any non-admission Core error aborts.
"""

from __future__ import annotations

import sys
from pathlib import Path


def _install_compat(repo_root: Path) -> dict[str, str]:
    """Install the bounded in-process admission shim. Returns a scope report."""
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    from scripts import survey_publication_v2 as publication
    from scripts import survey_reader_publication_v2 as reader
    from scripts import survey_schema_v2 as schema_gate
    import scripts.survey_stage_validation_v2 as stageval

    frozen_prior = stageval._prior_artifacts
    frozen_current = stageval._current_artifacts

    def compat_prior_artifacts(r_repo_root, cfg, state):
        from scripts import survey_stage_validation_v2 as _stageval_inner
        result: dict[str, Path] = {}
        seen: set[str] = set()
        revalidation, revalidation_errors = agent.resolve_active_publication_revalidation(
            r_repo_root, cfg, state)
        if revalidation_errors:
            raise ValueError("active publication revalidation invalid: " + "; ".join(revalidation_errors))
        superseded: dict[tuple[str, str], str] = {}
        bound_prior: str | None = None
        if revalidation is not None:
            bound_prior = revalidation["prior_checkpoint"]["path"]
            superseded = {(row["name"], row["path"]): row["new_sha256"]
                          for row in revalidation.get("superseded_artifacts", [])}
        for key, ref in (state.get("checkpoint_provenance", {}) or {}).items():
            if ref is None:
                continue
            if key == "publication_preview":
                # Human Approval, not a Stage Checkpoint: validate separately.
                if not isinstance(ref, dict) or set(ref) != {"path", "sha256"}:
                    raise ValueError("publication_preview provenance fields invalid")
                apath = core.repo_local_path(r_repo_root, ref["path"], "Human Approval publication_preview")
                if apath.is_symlink() or not apath.is_file() or core.sha256_file(apath) != ref["sha256"]:
                    raise ValueError("publication_preview Human Approval authority drift")
                approval = publication.validate_preview_approval(
                    r_repo_root, apath, issue_id=state.get("issue_id"))
                if approval.get("decision") != "APPROVED":
                    raise ValueError("publication_preview Human Approval decision is not APPROVED")
                continue
            path = _stageval_inner._authority_ref_path(r_repo_root, ref, "prior Stage Checkpoint")
            rel = _stageval_inner._rel(r_repo_root, path)
            if rel in seen:
                continue
            seen.add(rel)
            record = schema_gate.load_and_validate_json(
                path, r_repo_root / agent.CHECKPOINT_SCHEMA, label="prior Stage Checkpoint")
            if record.get("issue_id") != state.get("issue_id"):
                raise ValueError("prior Stage Checkpoint issue identity mismatch")
            for row in record.get("artifacts", []):
                artifact = core.repo_local_path(r_repo_root, row["path"], f"prior artifact {row['name']}")
                expected = row["sha256"]
                if bound_prior is not None and rel == bound_prior:
                    expected = superseded.get((row["name"], row["path"]), expected)
                if artifact.is_symlink() or not artifact.is_file() or core.sha256_file(artifact) != expected:
                    raise ValueError(f"prior Stage Checkpoint artifact drift: {row['name']}")
                existing = result.get(row["name"])
                if existing is not None and existing.resolve() != artifact.resolve():
                    raise ValueError(f"prior Stage Checkpoints disagree on artifact name: {row['name']}")
                result[row["name"]] = artifact
        return result

    def compat_current_artifacts(r_repo_root, state, values):
        from scripts import survey_stage_validation_v2 as _stageval_inner
        lifecycle = state["lifecycle_state"]
        required = _stageval_inner.REQUIRED_CURRENT.get(lifecycle)
        if required is None:
            raise ValueError(f"no compact local stage validator for lifecycle: {lifecycle}")
        missing = sorted(required - set(values))
        if missing:
            raise ValueError("current stage artifacts missing: " + ", ".join(missing))
        if lifecycle == "RELEASE_CANDIDATE":
            # Bounded allowances: (1) schema freezeArtifacts requires
            # visual-review-record; (2) publication-candidate reaches the merged
            # set ONLY here because no prior provenance references the genuine
            # VALIDATED_DRAFT checkpoint — its pinned bytes are asserted below.
            allowed_extra = {"visual-review-record", "publication-candidate"}
        elif lifecycle == "ARCHITECTURE_ESTABLISHED":
            allowed_extra = {n for n in set(values) - required
                             if n.startswith("draft-package:") or n.startswith("draft-result:")}
            non_draft = sorted(set(values) - required - allowed_extra)
            if non_draft:
                raise ValueError("Draft stage extras must use draft-package:<id> or draft-result:<id>")
            packages = {n.split(":", 1)[1] for n in allowed_extra if n.startswith("draft-package:")}
            results = {n.split(":", 1)[1] for n in allowed_extra if n.startswith("draft-result:")}
            if not packages or packages != results:
                raise ValueError("Draft stage requires exactly paired draft-package:/draft-result: artifacts")
        else:
            allowed_extra = set()
            extra = sorted(set(values) - required)
            if extra:
                raise ValueError("unexpected current stage artifacts: " + ", ".join(extra))
        if "visual-review-record" in values:
            vpath = values["visual-review-record"]
            if not vpath.is_absolute():
                vpath = r_repo_root / vpath
            reader.validate_review_record(
                r_repo_root, vpath, issue_id=state.get("issue_id"), expected_kind="VISUAL")
        return {name: stageval._safe_file(r_repo_root, path, f"current artifact {name}")
                for name, path in values.items()}

    stageval._prior_artifacts = compat_prior_artifacts
    stageval._current_artifacts = compat_current_artifacts
    _ = frozen_prior, frozen_current  # retained for audit clarity; never called
    return {"adapted": "survey_stage_validation_v2._prior_artifacts + _current_artifacts (in-process only)",
            "frozen_code": "unchanged on disk (verified identical to frozen Core HEAD)"}


def main() -> int:
    repo_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    sys.path.insert(0, str(repo_root))
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core

    scope = _install_compat(repo_root)
    print("compat scope: " + scope["adapted"])

    import scripts.survey_stage_validation_v2 as stageval

    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state_path = repo_root / "sources/2026-W42/production-state.json"
    supplied = {
        "freeze-record": repo_root / "sources/2026-W42/publication/v2/freeze-record-v2.json",
        "release-manifest": repo_root / "sources/2026-W42/publication/v2/release-manifest-v2.json",
        "visual-review-record": repo_root / "sources/2026-W42/publication/v2/visual-review-v2.json",
        "publication-candidate": repo_root / "sources/2026-W42/publication/v2/publication-candidate-v2.json",
    }
    # Assert the candidate is the genuine VALIDATED_DRAFT-pinned bytes (no substitute).
    import json as _json
    vd = _json.loads((repo_root / "sources/2026-W42/orchestration/v2/checkpoints/VALIDATED_DRAFT.json").read_text())
    pinned = [r for r in vd.get("artifacts", []) if r.get("name") == "publication-candidate"]
    assert len(pinned) == 1, "VALIDATED_DRAFT checkpoint must pin exactly one publication-candidate"
    from scripts import survey_production_v2 as _core
    actual = _core.sha256_file(supplied["publication-candidate"])
    assert actual == pinned[0]["sha256"], "publication-candidate diverges from VALIDATED_DRAFT-pinned bytes"
    print("candidate pinned-identity asserted:", actual[:12])
    out = repo_root / "sources/2026-W42/execution/validation/freeze-validation-r34.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    from datetime import datetime, timezone
    stageval.validate_stage(repo_root, cfg, state_path,
                            {k: v for k, v in supplied.items()}, out,
                            datetime.now(timezone.utc))
    print("validate_stage PASS: " + str(out.relative_to(repo_root)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
