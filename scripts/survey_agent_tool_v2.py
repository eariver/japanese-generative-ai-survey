#!/usr/bin/env python3
"""Run existing Core v2 stage helpers under the current reviewed agent-first toolchain.

Initialization implementation identity is historical provenance.  Canonical
agent-first work may integrate a reviewed generic main change into the edition
work branch and then execute the stage helper from that new branch head.  Some
WU-006/WU-007 helper functions still call the legacy ``core.verify_state_basis``
function, whose semantics intentionally pin the old orchestration model.

This wrapper replaces that verifier only for the lifetime of one helper process
with the agent-first State validator.  It does not mutate Production State and
it does not weaken legacy Action/Handoff compatibility when those tools are run
directly.
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


@contextmanager
def current_stage_basis_override() -> Iterator[None]:
    original = core.verify_state_basis
    core.verify_state_basis = verify_current_stage_basis
    try:
        yield
    finally:
        core.verify_state_basis = original


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
