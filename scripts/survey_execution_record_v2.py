#!/usr/bin/env python3
"""Initialize and validate edition-local Survey Production Core v2 execution records.

This helper owns structure only. ChatGPT remains responsible for writing the
material production actions, judgments, Human review summaries and defect
observations described by the execution-record policy.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from scripts import survey_agent_control_v2 as agent_control
from scripts import survey_production_v2 as core

SESSION_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
EXECUTION_DIR = "execution"
INDEX_FILE = "index.md"
REQUIRED_DIRS = ("sessions", "reviews", "defects")
INDEX_HEADINGS = (
    "## Current authority",
    "## Human Gates",
    "## Publication Candidate",
    "## Grok/X",
    "## Deviations",
    "## Shared Core defects",
    "## Sessions",
    "## Final disposition",
)
SESSION_HEADINGS = (
    "## Starting authority",
    "## Actions actually performed",
    "## External handoff",
    "## Deviations / failures",
    "## End state",
)
REVIEW_HEADINGS = (
    "## Reviewed authority",
    "## Human decision",
    "## Requested changes",
    "## Regeneration boundary",
    "## Shared-Core implication",
)
DEFECT_HEADINGS = (
    "## Observation",
    "## Reproduction boundary",
    "## Impact",
    "## Safe edition-local workaround",
    "## Core-maintenance pointer",
    "## Production disposition",
)


class ExecutionRecordError(ValueError):
    pass


def _repo_path(repo_root: Path, value: str, label: str) -> Path:
    return core.repo_local_path(repo_root, value, label)


def _load_profile(repo_root: Path, cfg: dict[str, Any], profile_path: Path) -> tuple[Path, dict[str, Any]]:
    path = profile_path if profile_path.is_absolute() else repo_root / profile_path
    path = path.resolve()
    try:
        path.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ExecutionRecordError("Production Profile escapes repository") from exc
    if path.is_symlink() or not path.is_file():
        raise ExecutionRecordError(f"Production Profile missing or unsafe: {path}")
    profile = core.load_json(path)
    errors = core.validate_profile(profile, cfg)
    if errors:
        raise ExecutionRecordError("Production Profile invalid: " + "; ".join(errors))
    return path, profile


def _load_state(repo_root: Path, cfg: dict[str, Any], state_path: Path, profile: dict[str, Any]) -> tuple[Path, dict[str, Any]]:
    path = state_path if state_path.is_absolute() else repo_root / state_path
    path = path.resolve()
    try:
        path.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ExecutionRecordError("Production State escapes repository") from exc
    if path.is_symlink() or not path.is_file():
        raise ExecutionRecordError(f"Production State missing or unsafe: {path}")
    state = core.load_json(path)
    errors = agent_control.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ExecutionRecordError("Production State invalid: " + "; ".join(errors))
    if state.get("issue_id") != profile.get("issue_id"):
        raise ExecutionRecordError("Production State/Profile issue identity mismatch")
    return path, state


def _validate_sha40(value: str, label: str) -> None:
    if not isinstance(value, str) or not SHA40_RE.fullmatch(value):
        raise ExecutionRecordError(f"{label} must be exact lowercase 40-hex commit SHA")


def _validate_session_id(value: str) -> None:
    if not isinstance(value, str) or not SESSION_ID_RE.fullmatch(value):
        raise ExecutionRecordError("session_id must be one safe filename stem")


def _execution_root(repo_root: Path, profile: dict[str, Any]) -> Path:
    source_root = _repo_path(repo_root, profile["paths"]["source_root"], "execution source_root")
    return source_root / EXECUTION_DIR


def _rel(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def _gate_status(state: dict[str, Any], key: str) -> str:
    value = (state.get("human_gates") or {}).get(key)
    return str(value) if value is not None else "not-recorded"


def initialize(
    repo_root: Path,
    cfg: dict[str, Any],
    profile_path: Path,
    state_path: Path,
    *,
    session_id: str,
    started_at: str,
    main_sha: str,
    branch_head: str,
    objective: str,
    requested_stop: str,
    disposition: str = "IN_PROGRESS",
) -> tuple[Path, Path]:
    profile_path, profile = _load_profile(repo_root, cfg, profile_path)
    state_path, state = _load_state(repo_root, cfg, state_path, profile)
    _validate_session_id(session_id)
    core.parse_instant(started_at)
    _validate_sha40(main_sha, "main_sha")
    _validate_sha40(branch_head, "branch_head")
    if not isinstance(objective, str) or not objective.strip():
        raise ExecutionRecordError("objective must be non-empty")
    if requested_stop not in {"ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW", "COMPLETE"}:
        raise ExecutionRecordError("requested_stop must be ARCHITECTURE_REVIEW, PUBLICATION_PREVIEW, or COMPLETE")
    if disposition not in {"IN_PROGRESS", "HUMAN_GATE", "BLOCKED_CORE_DEFECT", "TERMINATED_VALIDATION", "COMPLETE"}:
        raise ExecutionRecordError("unsupported execution disposition")

    root = _execution_root(repo_root, profile)
    index_path = root / INDEX_FILE
    session_path = root / "sessions" / f"{session_id}.md"
    if index_path.exists():
        raise ExecutionRecordError(f"execution index already exists: {_rel(repo_root, index_path)}")
    if session_path.exists():
        raise ExecutionRecordError(f"execution session already exists: {_rel(repo_root, session_path)}")
    for name in REQUIRED_DIRS:
        (root / name).mkdir(parents=True, exist_ok=True)

    state_rel = _rel(repo_root, state_path)
    profile_rel = _rel(repo_root, profile_path)
    state_sha = core.sha256_file(state_path)
    started_utc = core.iso_utc(core.parse_instant(started_at))
    lifecycle = state.get("lifecycle_state") or "unknown"
    terminal = state.get("terminal_reason") or "none"
    next_action = state.get("next_action") or "none"
    branch = profile["paths"]["work_branch"]
    x_policy = cfg.get("external_source_intake", {}).get("x_grok", {}).get("profile_policy", {}).get(profile["research_profile"], "not-configured")

    index = f"""# Survey Production execution index — {profile['issue_id']}

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `{state_rel}`.

## Current authority

- Issue / edition: `{profile['issue_id']}`
- Research Profile: `{profile['research_profile']}`
- Publication Profile: `{profile['publication_profile']}`
- Work branch: `{branch}`
- Start-of-run reviewed `main`: `{main_sha}`
- Run started: `{started_utc}`
- Requested stop: `{requested_stop}`
- Production Profile: `{profile_rel}`
- Production State: `{state_rel}`
- Current State SHA-256: `{state_sha}`
- Current lifecycle: `{lifecycle}`
- Current terminal reason: `{terminal}`
- Current next action: `{next_action}`

## Human Gates

- Architecture Review: `{_gate_status(state, 'architecture_review')}`
- Publication Preview: `{_gate_status(state, 'publication_preview')}`
- Detailed review records: none recorded yet

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `{x_policy}`
- Latest Drive task-file path/reference: none recorded yet
- Latest result disposition: none recorded yet

## Deviations

- None recorded at initialization.

## Shared Core defects

- None recorded at initialization.

## Sessions

- `sessions/{session_id}.md`

## Final disposition

`{disposition}`
"""

    session = f"""# Survey Production session — {session_id}

Issue: `{profile['issue_id']}`  
Started: `{started_utc}`

## Starting authority

- Branch head: `{branch_head}`
- Work branch: `{branch}`
- Reviewed `main`: `{main_sha}`
- Production Profile: `{profile_rel}`
- Production State: `{state_rel}`
- State SHA-256: `{state_sha}`
- Lifecycle: `{lifecycle}`
- Session objective: {objective}
- Requested stop: `{requested_stop}`
- Prior execution index: newly initialized by this session

## Actions actually performed

- Initialized the canonical edition-local execution record tree.
- Replace/add concise stage-grouped bullets here as material production actions occur.

## External handoff

- None recorded yet. When Grok/X is used, record only the exact Drive task-file path/reference, returned result reference, imported Raw authority and disposition.

## Deviations / failures

- None recorded yet. Classify material failures as `EDITION_LOCAL`, `TRANSIENT_EXECUTION`, or `SHARED_CORE_DEFECT`.

## End state

- Lifecycle: `{lifecycle}`
- Terminal reason: `{terminal}`
- Next action: `{next_action}`
- Review target: none recorded yet
- Session status: `IN_PROGRESS`
"""

    index_path.write_text(index, encoding="utf-8")
    session_path.write_text(session, encoding="utf-8")
    return index_path, session_path


def _require_headings(path: Path, headings: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for heading in headings:
        if heading not in text:
            errors.append(f"{path.as_posix()} missing required heading: {heading}")
    return errors


def validate(repo_root: Path, cfg: dict[str, Any], profile_path: Path, state_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        _, profile = _load_profile(repo_root, cfg, profile_path)
        _, state = _load_state(repo_root, cfg, state_path, profile)
    except (OSError, ValueError) as exc:
        return [str(exc)]
    root = _execution_root(repo_root, profile)
    index_path = root / INDEX_FILE
    if index_path.is_symlink() or not index_path.is_file():
        return [f"execution index missing or unsafe: {_rel(repo_root, index_path)}"]
    for name in REQUIRED_DIRS:
        path = root / name
        if path.is_symlink() or not path.is_dir():
            errors.append(f"execution directory missing or unsafe: {_rel(repo_root, path)}")
    errors.extend(_require_headings(index_path, INDEX_HEADINGS))
    index_text = index_path.read_text(encoding="utf-8")
    for required in (
        f"`{profile['issue_id']}`",
        f"`{profile['research_profile']}`",
        f"`{profile['publication_profile']}`",
        f"`{profile['paths']['work_branch']}`",
    ):
        if required not in index_text:
            errors.append(f"execution index missing current Profile identity: {required}")
    session_dir = root / "sessions"
    sessions = sorted(session_dir.glob("*.md")) if session_dir.is_dir() else []
    if not sessions:
        errors.append("execution record requires at least one session log")
    for path in sessions:
        if path.is_symlink():
            errors.append(f"unsafe execution session symlink: {_rel(repo_root, path)}")
            continue
        errors.extend(_require_headings(path, SESSION_HEADINGS))
        if f"sessions/{path.name}" not in index_text:
            errors.append(f"execution index does not list session: {path.name}")
    for subdir, headings in (("reviews", REVIEW_HEADINGS), ("defects", DEFECT_HEADINGS)):
        folder = root / subdir
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.is_symlink():
                errors.append(f"unsafe execution {subdir[:-1]} symlink: {_rel(repo_root, path)}")
                continue
            errors.extend(_require_headings(path, headings))
    state_rel = _rel(repo_root, state_path if state_path.is_absolute() else repo_root / state_path)
    if state_rel not in index_text:
        errors.append("execution index does not point to canonical Production State")
    if state.get("issue_id") != profile.get("issue_id"):
        errors.append("execution index validation State/Profile issue mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--profile", required=True)
    init.add_argument("--state", required=True)
    init.add_argument("--session-id", required=True)
    init.add_argument("--started-at", required=True)
    init.add_argument("--main-sha", required=True)
    init.add_argument("--branch-head", required=True)
    init.add_argument("--objective", required=True)
    init.add_argument("--requested-stop", required=True)
    init.add_argument("--disposition", default="IN_PROGRESS")

    check = sub.add_parser("validate")
    check.add_argument("--profile", required=True)
    check.add_argument("--state", required=True)

    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)

    try:
        if args.command == "init":
            index, session = initialize(
                root,
                cfg,
                Path(args.profile),
                Path(args.state),
                session_id=args.session_id,
                started_at=args.started_at,
                main_sha=args.main_sha,
                branch_head=args.branch_head,
                objective=args.objective,
                requested_stop=args.requested_stop,
                disposition=args.disposition,
            )
            print(_rel(root, index))
            print(_rel(root, session))
        else:
            errors = validate(root, cfg, Path(args.profile), Path(args.state))
            if errors:
                raise ExecutionRecordError("; ".join(errors))
            print("execution record validation PASS")
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
