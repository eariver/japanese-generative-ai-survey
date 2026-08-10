#!/usr/bin/env python3
"""Run Special source expansion with safe reader-facing joins/rendering.

Draft Packages intentionally do not duplicate Architecture package titles. This
runner joins title by package_id and replaces only the Technical Note string
renderer with an equivalent implementation that avoids Python-format/TeX brace
collisions. Immutable upstream artifacts are never mutated.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import expand_special_validated_source as expansion


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def safe_note(role: str, record: dict[str, Any]) -> str:
    c = expansion.card(record)
    claims = c.get("claims") or []
    limitations = c.get("limitations") or []
    esc = expansion.tex_escape
    task_id = str(record.get("evidence_task_id") or "")
    lines = [
        "\\begin{technicalnote}{" + esc(expansion.card_name(record)) + "}{" + esc(role) + "}",
        r"\begin{tabularx}{\linewidth}{@{}>{\bfseries}p{0.22\linewidth}X@{}}",
        "Organization & " + esc(expansion.organization(record)) + r" \\",
        "Artifact type & " + esc(expansion.artifact_type(record)) + r" \\",
        "Chronology & " + esc(expansion.event_dates(record)) + r" \\",
        r"\end{tabularx}",
        r"\smallskip",
        r"{\bfseries 一次資料から整理したtechnical points}",
        r"\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]",
    ]
    if claims:
        for claim in claims:
            if not isinstance(claim, dict) or not claim.get("text"):
                continue
            cls = str(claim.get("evidence_class") or "")
            label = expansion.CLASS_LABELS.get(cls, cls or "Claim")
            lines.append(r"\item \textbf{" + esc(label) + "}: " + esc(str(claim["text"])))
    else:
        lines.append(r"\item このrecordには独立したnormalized claimは記録されていない。")
    lines.append(r"\end{itemize}")

    if limitations:
        lines.extend([
            r"{\bfseries 読む際の境界}",
            r"\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]",
        ])
        for limitation in limitations:
            if not isinstance(limitation, dict) or not limitation.get("text"):
                continue
            cls = str(limitation.get("evidence_class") or "INFERENCE")
            label = expansion.CLASS_LABELS.get(cls, cls)
            lines.append(r"\item \textbf{" + esc(label) + "}: " + esc(str(limitation["text"])))
        lines.append(r"\end{itemize}")

    urls = expansion.source_urls(record)
    if urls:
        lines.extend([r"{\bfseries Primary source}", r"\begin{itemize}[leftmargin=1.5em,itemsep=0.25em]"])
        for url in urls:
            lines.append(r"\item \url{" + url + "}")
        lines.append(r"\end{itemize}")

    lines.extend([
        r"{\scriptsize\color{SurveyMuted}Source-bound record: \texttt{" + esc(task_id) + "}.}",
        r"\end{technicalnote}",
        r"\medskip",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", default="v0.2")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    plan_path = root / "sources" / args.issue_id / "architecture" / "issue-architecture-v0.1.json"
    plan = load_json(plan_path)
    if plan.get("status") != "APPROVED":
        raise ValueError("Issue Architecture must be APPROVED")
    titles = {
        str(package["package_id"]): str(package["title"])
        for package in plan.get("packages") or []
        if isinstance(package, dict) and package.get("package_id") and package.get("title")
    }

    original_renderer = expansion.render_technical_notes

    def render_with_architecture_title(package: dict[str, Any]) -> str:
        package_id = str(package.get("package_id") or "")
        if package_id not in titles:
            raise ValueError(f"approved Architecture title missing for package: {package_id}")
        joined = dict(package)
        joined["title"] = titles[package_id]
        return original_renderer(joined)

    expansion.render_note = safe_note
    expansion.render_technical_notes = render_with_architecture_title
    result = expansion.build(root, args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
