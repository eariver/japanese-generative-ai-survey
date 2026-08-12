#!/usr/bin/env python3
"""Run Special source expansion with safe reader-facing joins/rendering.

Draft Packages intentionally do not duplicate Architecture package titles. This
runner joins title by package_id, normalizes machine artifact-type labels only for
display, uses smaller/sloppy URL rendering inside source notes, and applies a few
Special-local cover/header typography adjustments after deterministic expansion.
Immutable upstream Evidence, Draft Packages, Article Drafts, and previous source
revisions are never mutated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import expand_special_validated_source as expansion


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
        lines.extend([
            r"{\bfseries Primary source}",
            r"\begingroup\sloppy",
            r"\Urlmuskip=0mu plus 2mu\relax",
            r"\begin{itemize}[leftmargin=1.5em,itemsep=0.25em]",
        ])
        for url in urls:
            lines.append(r"\item {\scriptsize\url{" + url + "}}")
        lines.extend([r"\end{itemize}", r"\endgroup"])

    lines.extend([
        r"{\scriptsize\color{SurveyMuted}Source-bound record: \texttt{" + esc(task_id) + "}.}",
        r"\end{technicalnote}",
        r"\medskip",
        "",
    ])
    return "\n".join(lines)


def normalize_duplicate_url_titles(path: Path) -> int:
    """Shorten derived BibLaTeX titles that merely repeat the exact URL field.

    Evidence and the URL field remain byte-for-byte unchanged. Only entries whose
    generated title has the exact form ``Primary source N: <url>`` and whose
    ``url`` field contains the same URL are normalized to ``Primary source N``.
    """
    text = path.read_text(encoding="utf-8")
    entry_re = re.compile(r"(?ms)^@online\{[^\n]+\n.*?^\}\s*$")
    title_re = re.compile(r"(?m)^  title = \{Primary source (\d+): ([^}]+)\},$")
    url_re = re.compile(r"(?m)^  url = \{([^}]+)\},$")
    replacements = 0

    def rewrite(match: re.Match[str]) -> str:
        nonlocal replacements
        entry = match.group(0)
        title = title_re.search(entry)
        url = url_re.search(entry)
        if not title or not url or title.group(2) != url.group(1):
            return entry
        replacements += 1
        start, end = title.span()
        shortened = f"  title = {{Primary source {title.group(1)}}},"
        return entry[:start] + shortened + entry[end:]

    revised = entry_re.sub(rewrite, text)
    path.write_text(revised, encoding="utf-8")
    return replacements


def postprocess_special_source(
    root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    titles: dict[str, str],
) -> dict[str, Any]:
    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source_dir = root / "surveys" / "special" / special_slug / "revisions" / source_version
    manifest_path = source_dir / "source-manifest.json"
    main_path = source_dir / "main.tex"
    references_path = source_dir / "references.bib"
    manifest = load_json(manifest_path)
    text = main_path.read_text(encoding="utf-8")

    text = text.replace(
        r"\surveyeditiondescriptor{Retrospective Technical Survey}",
        r"\surveyeditiondescriptor{Retrospective Survey}",
    )
    geometry_line = r"\geometry{margin=22mm,headsep=5mm,footskip=10mm}"
    if geometry_line in text and r"\setlength{\headheight}{14.5pt}" not in text:
        text = text.replace(
            geometry_line,
            geometry_line + "\n" + r"\setlength{\headheight}{14.5pt}",
        )

    synthesis_path = root / state["provenance"]["issue_synthesis"]["result_path"]
    synthesis = load_json(synthesis_path)
    article_run = root / state["provenance"]["article_draft"]["result_set_path"]
    acceptance = load_json(article_run / "acceptance.json")
    result_by_id = {row["package_id"]: row for row in acceptance.get("results") or []}
    for package_id in synthesis["cover"]["anchor_package_ids"]:
        row = result_by_id[package_id]
        draft = load_json(article_run / row["draft_path"])
        old = expansion.tex_escape(str(draft["headline"]))
        new = expansion.tex_escape(titles[package_id])
        text = text.replace(old, new)

    main_path.write_text(text, encoding="utf-8")
    reference_title_replacements = normalize_duplicate_url_titles(references_path)
    manifest["main_tex"]["sha256"] = sha256_file(main_path)
    manifest["references"]["sha256"] = sha256_file(references_path)
    manifest["typography_adjustments"] = {
        "artifact_type_display": "underscores replaced by spaces in reader-facing technical-note labels",
        "source_urls": "scriptsize + sloppy URL paragraphs + Urlmuskip stretch inside technical notes",
        "bibliography_titles": "generated Primary source N titles no longer duplicate an identical URL field",
        "bibliography_title_replacement_count": reference_title_replacements,
        "cover_descriptor": "Retrospective Survey",
        "cover_anchors": "approved Architecture package titles instead of full article headlines",
        "headheight": "14.5pt Special-local override",
        "content_semantics_changed": False,
    }
    write_json(manifest_path, manifest)

    current = state["provenance"]["validated_issue_source"]
    expected_path = manifest_path.relative_to(root).as_posix()
    if current.get("path") != expected_path or current.get("source_version") != source_version:
        raise ValueError("state-pinned source does not match generated source revision")
    current["sha256"] = sha256_file(manifest_path)
    current["typography_revision"] = "v0.4-reference-title-cleanup"
    write_json(state_path, state)
    return manifest


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
    original_artifact_type = expansion.artifact_type

    def display_artifact_type(record: dict[str, Any]) -> str:
        return original_artifact_type(record).replace("_", " ")

    def render_with_architecture_title(package: dict[str, Any]) -> str:
        package_id = str(package.get("package_id") or "")
        if package_id not in titles:
            raise ValueError(f"approved Architecture title missing for package: {package_id}")
        joined = dict(package)
        joined["title"] = titles[package_id]
        return original_renderer(joined)

    expansion.artifact_type = display_artifact_type
    expansion.render_note = safe_note
    expansion.render_technical_notes = render_with_architecture_title
    expansion.build(root, args.special_slug, args.issue_id, args.source_version)
    result = postprocess_special_source(root, args.special_slug, args.issue_id, args.source_version, titles)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
