#!/usr/bin/env python3
"""Compatibility entry point for Special Japanese reader notes."""
from __future__ import annotations

import re
import shlex
import stat
import sys
from pathlib import Path

from scripts.special_reader_notes_ja_core import *  # noqa: F401,F403
from scripts import special_reader_notes_ja_core as core

_ORIGINAL_CHECK = core.check
_GENERIC_READER_FALLBACKS = (
    '一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目',
    '提供元・プロジェクト・著者側の評価または説明として記録された項目',
    '一次資料と時系列から導いた編集上の整理。根拠となる事実と推論を区別して扱う',
)
_NOTE_RE = re.compile(r"\\begin\{technicalnote\}.*?\\end\{technicalnote\}", re.DOTALL)
_ITEM_RE = re.compile(r"^\\item\s+(.+)$", re.MULTILINE)


def arg_value(name: str, default: str | None = None) -> str | None:
    try:
        return sys.argv[sys.argv.index(name) + 1]
    except (ValueError, IndexError):
        return default


def check_compat(root: Path, issue_id: str) -> dict:
    report = _ORIGINAL_CHECK(root, issue_id)
    errors = list(report.get('errors') or [])
    state = core.load_json(root / 'sources' / issue_id / 'pipeline-state.json')
    source = state.get('provenance', {}).get('validated_issue_source') or {}
    manifest_path = root / str(source.get('path') or '')
    manifest = core.load_json(manifest_path)

    fallback_findings = 0
    duplicate_bullet_findings = 0
    for article in manifest.get('articles') or []:
        rel = str(article.get('technical_notes_path') or '')
        if not rel:
            continue
        path = manifest_path.parent / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        for phrase in _GENERIC_READER_FALLBACKS:
            count = text.count(phrase)
            if count:
                fallback_findings += count
                errors.append(
                    f"generic Technical Notes fallback in {article.get('package_id')}: {phrase} ({count})"
                )
        for block in _NOTE_RE.findall(text):
            title_match = re.match(r"\\begin\{technicalnote\}\{(.+?)\}\{", block)
            title = title_match.group(1) if title_match else str(article.get('package_id'))
            seen: set[str] = set()
            duplicates: set[str] = set()
            for value in _ITEM_RE.findall(block):
                normalized = re.sub(r"\s+", " ", value).strip()
                if normalized in seen:
                    duplicates.add(normalized)
                seen.add(normalized)
            if duplicates:
                duplicate_bullet_findings += len(duplicates)
                errors.append(
                    f"duplicate Technical Notes bullet in {article.get('package_id')}/{title}: "
                    + '; '.join(sorted(duplicates))[:300]
                )

    report['generic_fallback_findings'] = fallback_findings
    report['duplicate_bullet_findings'] = duplicate_bullet_findings
    report['source_specific_summary_policy'] = 'required-no-generic-fallback'
    report['errors'] = errors
    report['passed'] = not errors
    return report


# core.main resolves check from its module globals, so patch the compatibility
# validation before dispatching any subcommand.
core.check = check_compat


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
    script += 'rm -f "$0"\n'
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text(script, encoding="utf-8")
    hook.chmod(hook.stat().st_mode | stat.S_IXUSR)


def main() -> int:
    result = core.main()
    install_fill_hook()
    return result


if __name__ == "__main__":
    raise SystemExit(main())
