#!/usr/bin/env python3
"""Create an immutable mixed-layout revision of a built retrospective Special.

The revision keeps accepted Article Draft TeX and Technical Notes byte-identical,
returns narrative articles to a two-column house style, keeps comparison / Evidence
material full-width, and may add a reviewed synthesis artifact that references only
Evidence already selected by the approved Issue Architecture.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


ARTICLE_TYPES = {"FEATURE", "DEEP_DIVE", "SECTION", "PAPER_WATCH"}
FORBIDDEN_READER_PHRASES = (
    "Issue #",
    "Candidate Selection",
    "Issue Architecture",
    "Evidence Task",
    "Reaction Pass",
    "Candidate Inventory",
    "primary verification",
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tex_escape(value: str) -> str:
    table = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(table.get(ch, ch) for ch in value)


def input_path(path: str) -> str:
    p = Path(path)
    return p.with_suffix("").as_posix()


def evidence_index(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for key in ("primary_evidence", "supporting_evidence"):
        for record in package.get(key) or []:
            if not isinstance(record, dict) or not record.get("evidence_task_id"):
                raise ValueError(f"{package.get('package_id')}: malformed {key} record")
            result[str(record["evidence_task_id"])] = record
    return result


def parse_bib_url_map(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for block in re.split(r"(?=@online\{)", text):
        key_match = re.match(r"@online\{([^,]+),", block)
        url_match = re.search(r"\n\s*url\s*=\s*\{([^}]*)\},", block)
        if key_match and url_match:
            result[url_match.group(1).strip()] = key_match.group(1).strip()
    if not result:
        raise ValueError(f"no URL bibliography entries parsed from {path}")
    return result


def citation_keys(task_ids: list[str], records: dict[str, dict[str, Any]], bib_map: dict[str, str]) -> list[str]:
    keys: list[str] = []
    for task_id in task_ids:
        record = records[task_id]
        card = record.get("card") or {}
        for source in card.get("sources") or []:
            if not isinstance(source, dict) or not source.get("url"):
                continue
            url = str(source["url"]).strip()
            key = bib_map.get(url)
            if key is None:
                raise ValueError(f"bibliography key missing for selected source URL: {url}")
            if key not in keys:
                keys.append(key)
    return keys


def validate_reader_text(text: str, context: str) -> None:
    for phrase in FORBIDDEN_READER_PHRASES:
        if phrase.lower() in text.lower():
            raise ValueError(f"{context}: reader-facing synthesis contains internal phrase: {phrase}")


def render_synthesis(
    theme: dict[str, Any],
    package: dict[str, Any],
    bib_map: dict[str, str],
) -> str:
    records = evidence_index(package)
    title = str(theme.get("title") or "").strip()
    intro = str(theme.get("intro") or "").strip()
    if not title or not intro:
        raise ValueError(f"{package['package_id']}: synthesis title/intro required")
    validate_reader_text(title + "\n" + intro, package["package_id"])

    lines = [
        r"\sectionkicker{Theme synthesis}",
        "\\subsection*{" + tex_escape(title) + "}",
        "\\addcontentsline{toc}{subsection}{" + tex_escape(title) + "}",
        tex_escape(intro),
        r"\medskip",
        r"\begin{center}",
        r"\small",
        r"\renewcommand{\arraystretch}{1.16}",
        r"\begin{tabularx}{\linewidth}{@{}p{0.20\linewidth}X@{}}",
        r"\toprule",
        r"観察軸 & 7月の一次資料・論文から読めること \\",
        r"\midrule",
    ]
    used: list[str] = []
    rows = theme.get("rows") or []
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{package['package_id']}: synthesis rows required")
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{package['package_id']}: invalid synthesis row")
        dimension = str(row.get("dimension") or "").strip()
        observation = str(row.get("observation") or "").strip()
        task_ids = [str(x) for x in (row.get("evidence_task_ids") or [])]
        if not dimension or not observation or not task_ids:
            raise ValueError(f"{package['package_id']}: synthesis row requires dimension, observation, evidence_task_ids")
        validate_reader_text(dimension + "\n" + observation, package["package_id"])
        unknown = sorted(set(task_ids) - set(records))
        if unknown:
            raise ValueError(f"{package['package_id']}: synthesis references non-package Evidence: {unknown}")
        cites = citation_keys(task_ids, records, bib_map)
        cite_tex = " \\cite{" + ",".join(cites) + "}" if cites else ""
        lines.append(tex_escape(dimension) + " & " + tex_escape(observation) + cite_tex + r" \\")
        used.extend(task_id for task_id in task_ids if task_id not in used)
    lines.extend([
        r"\bottomrule",
        r"\end{tabularx}",
        r"\renewcommand{\arraystretch}{1.0}",
        r"\end{center}",
        r"\normalsize",
        r"\begin{claimboundary}[この比較の境界]",
        "この表は本号で既に検証・参照している一次資料と論文を横断比較の形へ再配置したものである。"
        "vendor / project / author が報告した性能値や優位性は独立再現済みの一般則へ変換せず、本文とSource Notesの帰属境界をそのまま維持する。",
        r"\end{claimboundary}",
        "",
    ])
    return "\n".join(lines), used


def build_main_tex(current_main: Path, manifest: dict[str, Any], synthesis_paths: dict[str, str]) -> str:
    text = current_main.read_text(encoding="utf-8")
    preamble = text.split("\\begin{document}", 1)[0]
    preamble = preamble.replace(
        "% Special-local long-form presentation. Shared weekly source remains unchanged.",
        "% Special-local mixed presentation: narrative two-column, synthesis/technical notes full-width. Shared weekly source remains unchanged.",
    )
    preamble = preamble.replace(r"\surveyeditiondescriptor{Retrospective Survey}", r"\surveyeditiondescriptor{Retrospective}")
    if r"\setlength{\columnsep}" not in preamble:
        preamble += "\\setlength{\\columnsep}{6mm}\n"

    lines = [preamble.rstrip(), "", r"\begin{document}", r"\surveycover", r"\clearpage", r"\onecolumn", r"\input{sections/00-frontmatter}", ""]
    for article in manifest.get("articles") or []:
        package_id = str(article["package_id"])
        lines.extend([
            r"\clearpage",
            r"\twocolumn",
            "\\input{" + input_path(str(article["article_section_path"])) + "}",
            r"\clearpage",
            r"\onecolumn",
        ])
        synth = synthesis_paths.get(package_id)
        if synth:
            lines.append("\\input{" + input_path(synth) + "}")
            lines.append(r"\medskip")
        lines.append("\\input{" + input_path(str(article["technical_notes_path"])) + "}")
        lines.append("")
    lines.extend([
        r"\clearpage",
        r"\onecolumn",
        r"\printbibliography[title={References / Source Notes}]",
        r"\end{document}",
        "",
    ])
    return "\n".join(lines)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError(f"mixed-layout revision requires RELEASE_CANDIDATE, got {state.get('lifecycle_state')}")
    if gates.get("latex_build") != "passed" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("mixed-layout revision requires built PDF with Visual Review and Freeze still pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha256_file(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent

    supplement_path = repo_root / "sources" / issue_id / "editorial" / f"theme-synthesis-{source_version}.json"
    supplement = load_json(supplement_path)
    if supplement.get("issue_id") != issue_id or supplement.get("revision") != source_version:
        raise ValueError("theme synthesis issue/revision mismatch")
    if (supplement.get("constraints") or {}).get("new_external_evidence_allowed") is not False:
        raise ValueError("theme synthesis must forbid new external Evidence")

    plan_path = repo_root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json"
    plan = load_json(plan_path)
    if plan.get("status") != "APPROVED":
        raise ValueError("Issue Architecture must remain APPROVED")
    package_plan = {str(p["package_id"]): p for p in plan.get("packages") or [] if isinstance(p, dict) and p.get("package_id")}

    article_by_id = {str(a["package_id"]): a for a in current_manifest.get("articles") or []}
    theme_by_id = {str(t["package_id"]): t for t in supplement.get("themes") or []}
    unknown_themes = sorted(set(theme_by_id) - set(article_by_id))
    if unknown_themes:
        raise ValueError(f"theme synthesis references unknown article packages: {unknown_themes}")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_dir, output_dir)
    synth_dir = output_dir / "theme-synthesis"
    synth_dir.mkdir(parents=True, exist_ok=True)

    bib_path = output_dir / "references.bib"
    bib_map = parse_bib_url_map(bib_path)
    synthesis_paths: dict[str, str] = {}
    synthesis_records: list[dict[str, Any]] = []
    all_used: list[str] = []

    for index, article in enumerate(current_manifest.get("articles") or [], start=1):
        package_id = str(article["package_id"])
        theme = theme_by_id.get(package_id)
        if theme is None:
            continue
        package_path = repo_root / str(article["draft_package_path"])
        if sha256_file(package_path) != article["draft_package_sha256"]:
            raise ValueError(f"Draft Package digest mismatch: {package_id}")
        package = load_json(package_path)
        if package_id not in package_plan or package_plan[package_id].get("package_type") not in ARTICLE_TYPES:
            raise ValueError(f"approved Architecture package missing/mismatched: {package_id}")
        rendered, used = render_synthesis(theme, package, bib_map)
        rel = f"theme-synthesis/{index:02d}-{package_id}-synthesis.tex"
        target = output_dir / rel
        target.write_text(rendered, encoding="utf-8")
        synthesis_paths[package_id] = rel
        synthesis_records.append({
            "package_id": package_id,
            "path": rel,
            "sha256": sha256_file(target),
            "row_count": len(theme.get("rows") or []),
            "evidence_task_ids": used,
        })
        all_used.extend(x for x in used if x not in all_used)

    main_path = output_dir / "main.tex"
    main_path.write_text(build_main_tex(current_dir / "main.tex", current_manifest, synthesis_paths), encoding="utf-8")

    new_manifest = dict(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_MIXED_LAYOUT_REVISION"
    new_manifest["derivation"] = (
        "Mixed-layout revision of the previous validated source: accepted Article Draft sections and Technical Notes are copied byte-for-byte; "
        "reviewed full-width theme synthesis is restricted to Evidence already selected by the approved Architecture."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["layout"] = {
        "document_font_size": "11pt",
        "body_mode": "mixed: narrative articles two-column; theme synthesis and Technical Notes one-column full-width",
        "margin": "22mm",
        "column_gap": "6mm",
        "technical_note_policy": "one full-width note per selected Evidence record; exact normalized claims/limitations/source URLs",
        "house_style_reason": "restore Weekly-series two-column narrative identity without forcing wide Evidence tables/URLs into narrow columns",
    }
    new_manifest["main_tex"] = {"path": "main.tex", "sha256": sha256_file(main_path)}
    new_manifest["editorial_supplement"] = {
        "path": supplement_path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(supplement_path),
        "new_external_evidence": false,
        "selected_evidence_only": true,
        "synthesis_panel_count": len(synthesis_records),
        "referenced_evidence_task_ids": all_used,
    }
    new_manifest["theme_synthesis"] = synthesis_records
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "narrative_columns": 2,
        "full_width_sections": ["frontmatter", "theme synthesis", "Technical Notes", "References / Source Notes"],
        "cover_descriptor": "Retrospective",
        "article_sections_changed": false,
        "technical_notes_changed": false,
        "reader_synthesis_added": true,
        "new_external_evidence": false,
    }
    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha256_file(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    previous_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if previous_build:
        history.setdefault("latex_build", []).append(previous_build)

    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "mixed-two-column-narrative-full-width-evidence",
        "editorial_supplement_sha256": sha256_file(supplement_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "supplement_path": supplement_path.relative_to(repo_root).as_posix(),
        "supplement_sha256": sha256_file(supplement_path),
        "reason": "Human Visual Review feedback: restore two-column narrative body, keep wide Evidence material full-width, and restore comparison depth from already-collected information.",
    }
    write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": current_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "synthesis_panel_count": len(synthesis_records),
        "referenced_evidence_task_count": len(all_used),
        "article_sections_changed": false,
        "technical_notes_changed": false,
        "new_external_evidence": false,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
