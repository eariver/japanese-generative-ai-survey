#!/usr/bin/env python3
"""Run existing Core v2 stage helpers under the current reviewed agent-first toolchain.

Initialization implementation identity is historical provenance. Canonical
agent-first work may integrate a reviewed generic main change into the edition
work branch and then execute the stage helper from that new branch head. Some
WU-006/WU-007 helper functions still call the legacy ``core.verify_state_basis``
function, whose semantics intentionally pin the old orchestration model.

This wrapper replaces that verifier only for the lifetime of one helper process
with the agent-first State validator. It also permits an *accepted, immutable*
Screening package to retain the State SHA it was created from after Production
State has legitimately advanced to a later lifecycle state. That historical
exception is fail-closed: it is available only when the package is already
content-addressed by a sibling ``screening-accepted.json`` whose package hash
matches the exact archived package bytes; every other Screening basis check is
rerun against the current repository and current agent-first State.

It does not mutate Production State and it does not weaken legacy Action/Handoff
compatibility when those tools are run directly.
"""
from __future__ import annotations

import argparse
import runpy
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening

ALLOWED_HELPERS = {
    "scripts/survey_screening_v2.py",
    "scripts/survey_evidence_v2.py",
}


def verify_current_stage_basis(repo_root: Path, cfg: dict, state: dict, implementation_sha: str) -> None:
    current = core.repository_commit_sha(repo_root)
    if implementation_sha != current:
        raise ValueError(
            "agent-first stage helper must record the actual current work-branch implementation commit"
        )
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("agent-first Production State invalid: " + "; ".join(errors))


def _historical_screening_basis_wrapper(original):
    """Return a strict wrapper that tolerates only archived historical State SHA drift.

    Screening is prepared/accepted while Production State is at the Screening
    boundary. Downstream Evidence runs after State advances, so the canonical
    State path legitimately contains new bytes. The accepted Screening package
    already cryptographically binds its historical ``state_sha256`` through its
    own package hash and content-addressed acceptance. For that one case, rerun
    the original validator with only the in-memory expected State SHA replaced by
    the current State SHA; the archived package bytes themselves are never
    changed. This preserves all Profile, Discovery, prompt, schema, archive and
    current-State validation performed by the original function.
    """

    def validate(repo_root: Path, package_path: Path, package: dict, implementation_sha: str) -> None:
        try:
            original(repo_root, package_path, package, implementation_sha)
            return
        except ValueError as exc:
            if str(exc) != "Screening package basis drift: state_sha256":
                raise
            state_error = exc

        acceptance_path = package_path.parent / "screening-accepted.json"
        if acceptance_path.is_symlink() or not acceptance_path.is_file():
            raise state_error
        acceptance = core.load_json(acceptance_path)
        if core.sha256_file(package_path) != acceptance.get("package_sha256"):
            raise ValueError("accepted Screening package copy changed")

        basis = package.get("basis")
        if not isinstance(basis, dict):
            raise state_error
        state_rel = basis.get("state_path")
        if not isinstance(state_rel, str) or not state_rel:
            raise state_error
        state_path = (repo_root / state_rel).resolve()
        try:
            state_path.relative_to(repo_root.resolve())
        except ValueError as exc:
            raise ValueError("Screening package State path escapes repository") from exc
        if state_path.is_symlink() or not state_path.is_file():
            raise ValueError("Screening package basis drift: state_sha256")

        adjusted = dict(package)
        adjusted_basis = dict(basis)
        adjusted_basis["state_sha256"] = core.sha256_file(state_path)
        adjusted["basis"] = adjusted_basis
        original(repo_root, package_path, adjusted, implementation_sha)

    return validate


@contextmanager
def current_stage_basis_override() -> Iterator[None]:
    original_state_verifier = core.verify_state_basis
    original_screening_verifier = screening.validate_package_basis
    core.verify_state_basis = verify_current_stage_basis
    screening.validate_package_basis = _historical_screening_basis_wrapper(
        original_screening_verifier
    )
    try:
        yield
    finally:
        screening.validate_package_basis = original_screening_verifier
        core.verify_state_basis = original_state_verifier


def run_helper(repo_root: Path, state_path: Path, helper: str, helper_args: list[str]) -> int:
    normalized = Path(helper).as_posix()
    if normalized not in ALLOWED_HELPERS:
        raise ValueError(f"helper is not allowlisted for agent-first runtime: {helper}")
    target = (repo_root / normalized).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError("helper escapes repository root") from exc
    if not target.is_file():
        raise ValueError(f"helper missing: {normalized}")

    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("agent-first Production State invalid before helper execution: " + "; ".join(errors))

    old_argv = sys.argv[:]
    try:
        sys.argv = [str(target), "--repo-root", str(repo_root), *helper_args]
        with current_stage_basis_override():
            try:
                runpy.run_path(str(target), run_name="__main__")
            except SystemExit as exc:
                code = exc.code
                if code is None:
                    return 0
                if isinstance(code, int):
                    return code
                raise ValueError(str(code)) from exc
        return 0
    finally:
        sys.argv = old_argv


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--state", required=True)
    parser.add_argument("--helper", required=True, choices=sorted(ALLOWED_HELPERS))
    parser.add_argument("helper_args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = root / state_path
    forwarded = list(args.helper_args)
    if forwarded and forwarded[0] == "--":
        forwarded = forwarded[1:]
    try:
        return run_helper(root, state_path, args.helper, forwarded)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
