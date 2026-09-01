#!/usr/bin/env python3
"""Detect internal editorial workflow language in reader-facing publication prose.

The guard is publication-series agnostic. Weekly and Special source preflights may
reuse it. It intentionally allows an explicit source-comment exemption for files
whose published purpose is Source Notes / provenance rather than narrative prose.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PROSE_LINT_EXEMPT_MARKER = "% reader-facing-prose-lint: allow-internal-metadata"
READER_FACING_FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("Candidate Inventory", re.compile(r"Candidate\s+Inventory", re.IGNORECASE)),
    ("Candidate Selection", re.compile(r"Candidate\s+Selection", re.IGNORECASE)),
    ("Reaction Pass", re.compile(r"(?:Grok\s+)?Reaction\s+Pass", re.IGNORECASE)),
    ("primary verification workflow status", re.compile(r"primary\s+verification", re.IGNORECASE)),
    ("Issue Architecture", re.compile(r"Issue\s+Architecture", re.IGNORECASE)),
    ("Evidence Task", re.compile(r"Evidence\s+Task", re.IGNORECASE)),
    ("Draft Package", re.compile(r"Draft\s+Package", re.IGNORECASE)),
    ("selected-candidate workflow phrasing", re.compile(r"今号で採用した[^。\n]{0,30}候補")),
    ("future production TODO", re.compile(r"次号(?:以降)?[^。\n]{0,40}(?:追跡|昇格)")),
    (
        "candidate queue-management language",
        re.compile(
            r"候補として保存|Candidate\s+Inventoryへ残|昇格させ|選考ステータス|記事にできなかった情報の墓場",
            re.IGNORECASE,
        ),
    ),
)


def strip_tex_comment(line: str) -> str:
    """Remove an unescaped TeX comment from one source line."""
    return re.sub(r"(?<!\\)%.*$", "", line)


def reader_facing_prose_errors(path: Path, root: Path) -> list[str]:
    """Return deterministic errors for internal workflow language in visible prose."""
    text = path.read_text(encoding="utf-8")
    if PROSE_LINT_EXEMPT_MARKER in text:
        return []

    try:
        display_path = path.relative_to(root).as_posix()
    except ValueError:
        display_path = path.as_posix()

    errors: list[str] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        visible = strip_tex_comment(raw_line)
        if not visible.strip():
            continue
        for rule, pattern in READER_FACING_FORBIDDEN_PATTERNS:
            match = pattern.search(visible)
            if match:
                errors.append(
                    f"reader-facing prose violation [{rule}] at {display_path}:{line_number}: {match.group(0)!r}"
                )
    return errors


def scan_paths(paths: list[Path], root: Path) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            errors.append(f"reader-facing prose input missing: {path}")
            continue
        errors.extend(reader_facing_prose_errors(path, root))
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Reader-facing TeX/text files to scan")
    parser.add_argument("--root", default=".", help="Root used to render deterministic relative paths")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root)
    paths = [Path(value) for value in args.paths]
    errors = scan_paths(paths, root)
    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "paths": [path.as_posix() for path in paths],
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
