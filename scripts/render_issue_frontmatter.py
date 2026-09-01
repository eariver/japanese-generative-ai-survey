#!/usr/bin/env python3
"""Render validated post-draft issue synthesis into frontmatter LaTeX."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import validate_issue_synthesis as synthesis_validator
from scripts.render_article_draft_tex import tex_escape

BS = chr(92)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_refs(package_ids: list[str]) -> str:
    refs = [f"p.~{BS}pageref{{pkg:{package_id}}}" for package_id in package_ids]
    return " / ".join(refs)


def render(input_path: Path, result_path: Path, prompt_path: Path, output_path: Path, manifest_path: Path) -> tuple[dict[str, Any], bool]:
    validation, passed = synthesis_validator.validate(input_path, result_path, prompt_path)
    if not passed:
        raise ValueError(f"Issue synthesis did not validate: {validation['errors']}")
    synthesis_input = load_json(input_path)
    result = load_json(result_path)
    article_by_id = {article["package_id"]: article for article in synthesis_input["articles"]}

    anchors = [article_by_id[package_id]["headline"] for package_id in result["cover"]["anchor_package_ids"]]
    anchor_text = f" {BS}textbullet{{}} ".join(tex_escape(value) for value in anchors)
    lines = [
        "% Generated from validated post-draft Issue Synthesis. Do not hand-edit.",
        f"{BS}surveycoverstory",
        f"  {{{tex_escape(result['cover']['headline'])}}}",
        f"  {{{tex_escape(result['cover']['deck'])}}}",
        f"  {{{anchor_text}}}",
        "",
        f"{BS}clearpage",
        f"{BS}section*{{This Week in AI}}",
    ]

    for signal in result["this_week_signals"]:
        text = (
            f"{BS}textbf{{{tex_escape(signal['title'])}}} "
            f"{tex_escape(signal['summary'])} "
            f"{BS}hfill{{{BS}footnotesize {page_refs(signal['package_ids'])}}}"
        )
        if signal["late_breaking"]:
            lines.extend([f"{BS}begin{{latebreaking}}", text, f"{BS}end{{latebreaking}}"])
        else:
            lines.extend([f"{BS}smallskip", f"{BS}noindent {text}", f"{BS}par"])

    lines.extend(["", f"{BS}medskip", f"{BS}tableofcontents", ""])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    manifest = {
        "schema_version": "1.0",
        "issue_id": synthesis_input["issue_id"],
        "passed": True,
        "basis": {
            "synthesis_input_sha256": sha256_file(input_path),
            "synthesis_result_sha256": sha256_file(result_path),
            "prompt_sha256": sha256_file(prompt_path),
        },
        "output": {"path": output_path.as_posix(), "sha256": sha256_file(output_path), "bytes": output_path.stat().st_size},
        "anchor_package_ids": result["cover"]["anchor_package_ids"],
        "signal_count": len(result["this_week_signals"]),
        "note": "Article page references are generated via \\pageref{pkg:<package-id>}; no literal page numbers are emitted.",
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/issue-synthesis-v0.1.md")
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest-output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, _ = render(Path(args.input), Path(args.result), Path(args.prompt), Path(args.output), Path(args.manifest_output))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
