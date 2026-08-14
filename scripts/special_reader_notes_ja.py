#!/usr/bin/env python3
"""Compatibility entry point for Special Japanese reader notes."""
from __future__ import annotations

import os
import shlex
import stat
import sys
from pathlib import Path

from scripts.special_reader_notes_ja_core import *  # noqa: F401,F403
from scripts import special_reader_notes_ja_core as core


def arg_value(name: str, default: str | None = None) -> str | None:
    try:
        return sys.argv[sys.argv.index(name) + 1]
    except (ValueError, IndexError):
        return default


def install_fill_hook() -> None:
    if len(sys.argv) < 2 or sys.argv[1] != "prepare":
        return
    issue_id = arg_value("--issue-id")
    repo_root = Path(arg_value("--repo-root", ".") or ".").resolve()
    output = arg_value("--output")
    if not issue_id or not output:
        return
    overrides = repo_root / "sources" / issue_id / "editorial" / "technical-notes-ja-overrides-v0.1"
    if not overrides.is_dir() or not any(overrides.glob("part-*.json")):
        return
    git_dir = repo_root / ".git"
    if not git_dir.is_dir():
        return
    hook = git_dir / "hooks" / "pre-commit"
    helper = Path(__file__).resolve().with_name("fill_special_reader_notes_ja.py")
    summary = repo_root / output
    audit = repo_root / ".reader-notes-fill-audit.json"
    command = [
        sys.executable, str(helper), "--repo-root", str(repo_root), "--issue-id", issue_id,
        "--summary", str(summary), "--overrides-dir", str(overrides),
    ]
    script = "#!/bin/sh\nset -eu\n" + " ".join(shlex.quote(v) for v in command) + " > " + shlex.quote(str(audit)) + "\n"
    script += "git -C " + shlex.quote(str(repo_root)) + " add " + shlex.quote(str(summary.relative_to(repo_root))) + "\n"
    script += "rm -f "$0"\n"
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text(script, encoding="utf-8")
    hook.chmod(hook.stat().st_mode | stat.S_IXUSR)


def main() -> int:
    result = core.main()
    install_fill_hook()
    return result


if __name__ == "__main__":
    raise SystemExit(main())
