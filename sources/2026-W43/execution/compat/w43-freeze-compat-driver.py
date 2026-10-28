#!/usr/bin/env python3
"""W43 edition-local runtime-only Freeze compatibility driver (NO CORE PATCH).

Human authority: contract
`sources/2026-W43/execution/instructions/sol-w43-post-go-freeze-compat-through-public-release-20261028.md`
(HUMAN_FINAL_PDF_GO_ALREADY_RECORDED / W43_ONLY_FREEZE_ADMISSION_COMPAT / RELEASE_AUTHORIZED),
adapting proven W42 `w42-freeze-compat-driver.py` (+ W41 precedent) to W43 ONLY.
Trusted first-party attempt run #40608878000 remains the failed evidence
(CV2-DM-002: approval treated as Stage Checkpoint).

Frozen Core is NEVER modified: this driver adapts ONLY the semantic
typing/admission boundary of two frozen validator helpers IN THIS PROCESS
(by WRAPPING the actual frozen functions, not copying them), then calls the
real frozen `validate_stage`. Result label: EDITION_LOCAL_RUNTIME_COMPAT.

Adaptations (bounded):
  A. `_prior_artifacts`: call the FROZEN helper on a state copy whose
     `checkpoint_provenance` excludes ONLY `publication_preview`; validate the
     excluded Human Approval separately (exact state-bound file SHA,
     `publication.validate_preview_approval`, decision APPROVED). Every genuine
     prior checkpoint is verified by the exact frozen code path.
  B. `_current_artifacts`: call the FROZEN helper on the required subset only;
     permit strictly the W42-proven extras `visual-review-record` (validated
     with frozen `reader.validate_review_record`, VISUAL) and
     `publication-candidate` (asserted byte-identical to the genuine
     VALIDATED_DRAFT-pinned bytes). No other extra admitted.
Any non-admission Core error aborts with no mutation.
"""

from __future__ import annotations

import sys
from pathlib import Path


def _install_compat(repo_root: Path) -> dict[str, str]:
    """Install the bounded in-process admission shim. Returns a scope report."""
    from scripts import survey_agent_control_v2 as agent  # noqa: F401
    from scripts import survey_production_v2 as core
    from scripts import survey_publication_v2 as publication
    from scripts import survey_reader_publication_v2 as reader
    import scripts.survey_stage_validation_v2 as stageval

    frozen_prior = stageval._prior_artifacts
    frozen_current = stageval._current_artifacts

    def compat_prior_artifacts(r_repo_root, cfg, state):
        prov = state.get("checkpoint_provenance", {}) or {}
        trimmed = dict(state)
        trimmed["checkpoint_provenance"] = {
            k: v for k, v in prov.items() if k != "publication_preview"
        }
        # All genuine checkpoints verified by the exact frozen code path.
        result = frozen_prior(r_repo_root, cfg, trimmed)
        # Excluded entry validated separately as Human Approval (W42 parity).
        ref = prov.get("publication_preview")
        if not isinstance(ref, dict) or set(ref) != {"path", "sha256"}:
            raise ValueError("publication_preview provenance fields invalid")
        apath = core.repo_local_path(
            r_repo_root, ref["path"], "Human Approval publication_preview")
        if apath.is_symlink() or not apath.is_file() or core.sha256_file(apath) != ref["sha256"]:
            raise ValueError("publication_preview Human Approval authority drift")
        approval = publication.validate_preview_approval(
            r_repo_root, apath, issue_id=state.get("issue_id"))
        if approval.get("decision") != "APPROVED":
            raise ValueError("publication_preview Human Approval decision is not APPROVED")
        return result

    def compat_current_artifacts(r_repo_root, state, values):
        lifecycle = state["lifecycle_state"]
        required = stageval.REQUIRED_CURRENT.get(lifecycle)
        if required is None:
            raise ValueError(f"no compact local stage validator for lifecycle: {lifecycle}")
        missing = sorted(required - set(values))
        if missing:
            raise ValueError("current stage artifacts missing: " + ", ".join(missing))
        extras = set(values) - required
        if lifecycle == "RELEASE_CANDIDATE":
            allowed = {"visual-review-record", "publication-candidate"}
            bad = sorted(extras - allowed)
            if bad:
                raise ValueError("Freeze stage extras not allowlisted: " + ", ".join(bad))
            if "visual-review-record" in values:
                vpath = values["visual-review-record"]
                if not vpath.is_absolute():
                    vpath = r_repo_root / vpath
                reader.validate_review_record(
                    r_repo_root, vpath, issue_id=state.get("issue_id"), expected_kind="VISUAL")
            if "publication-candidate" in values:
                import json as _json
                vd = _json.loads((r_repo_root / "sources/2026-W43/orchestration/v2/checkpoints/VALIDATED_DRAFT.json").read_text())
                pinned = [r for r in vd.get("artifacts", []) if r.get("name") == "publication-candidate"]
                if len(pinned) != 1:
                    raise ValueError("VALIDATED_DRAFT checkpoint must pin exactly one publication-candidate")
                cpath = values["publication-candidate"]
                if not cpath.is_absolute():
                    cpath = r_repo_root / cpath
                if core.sha256_file(cpath) != pinned[0]["sha256"]:
                    raise ValueError("publication-candidate diverges from VALIDATED_DRAFT-pinned bytes")
        elif extras:
            raise ValueError("unexpected current stage artifacts: " + ", ".join(sorted(extras)))
        base = frozen_current(
            r_repo_root, state, {k: v for k, v in values.items() if k in required})
        for name in extras:
            p = values[name]
            if not p.is_absolute():
                p = r_repo_root / p
            base[name] = stageval._safe_file(r_repo_root, p, f"current artifact {name}")
        return base

    stageval._prior_artifacts = compat_prior_artifacts
    stageval._current_artifacts = compat_current_artifacts
    _ = frozen_prior, frozen_current  # retained for audit clarity; called via wrappers
    return {"adapted": "survey_stage_validation_v2._prior_artifacts + _current_artifacts (in-process WRAPPERS around frozen originals, W43 only)",
            "frozen_code": "unchanged on disk"}


def main() -> int:
    repo_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    sys.path.insert(0, str(repo_root))
    from scripts import survey_agent_control_v2 as agent  # noqa: F401
    from scripts import survey_production_v2 as core

    scope = _install_compat(repo_root)
    print("compat scope: " + scope["adapted"])

    import scripts.survey_stage_validation_v2 as stageval

    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state_path = repo_root / "sources/2026-W43/production-state.json"
    state = core.load_json(state_path)
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise SystemExit("W43 compat driver requires RELEASE_CANDIDATE State")
    if state.get("human_gates", {}).get("publication_preview") != "approved":
        raise SystemExit("W43 compat driver requires APPROVED Publication Preview gate")

    supplied = {
        "freeze-record": repo_root / "sources/2026-W43/publication/v2/freeze-record-v2.json",
        "release-manifest": repo_root / "sources/2026-W43/publication/v2/release-manifest-v2.json",
        "visual-review-record": repo_root / "sources/2026-W43/publication/v2/visual-review-v2.json",
        "publication-candidate": repo_root / "sources/2026-W43/publication/v2/publication-candidate-v2.json",
    }
    print("candidate pinned-identity asserted:",
          core.sha256_file(supplied["publication-candidate"])[:12])
    out = repo_root / "sources/2026-W43/execution/validation/freeze-validation-w43.json"
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
