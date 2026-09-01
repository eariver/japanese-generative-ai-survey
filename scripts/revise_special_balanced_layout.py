#!/usr/bin/env python3
"""Create an immutable balanced mixed-layout revision for a retrospective Special.

The revision preserves accepted article and Technical Note source files byte-for-byte,
derives layout-only article bodies with their top-level section heading removed, renders
those headings full-width, and uses the multicol package for a balanced two-column
narrative that can return to full-width synthesis without a forced page break.

An optional final-synthesis artifact may add a reader-facing retrospective chapter, but
it may cite only Evidence already selected by the approved Issue Architecture.
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
    "Issue #", "Candidate Selection", "Issue Architecture", "Evidence Task",
    "Reaction Pass", "Candidate Inventory", "primary verification",
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
    table = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(table.get(ch, ch) for ch in value)

def input_path(path: str) -> str:
    return Path(path).with_suffix("").as_posix()

def validate_reader_text(text: str, context: str) -> None:
    for phrase in FORBIDDEN_READER_PHRASES:
        if phrase.lower() in text.lower():
            raise ValueError(f"{context}: reader-facing text contains internal phrase: {phrase}")

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

def evidence_index(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for key in ("primary_evidence", "supporting_evidence"):
        for record in package.get(key) or []:
            if not isinstance(record, dict) or not record.get("evidence_task_id"):
                raise ValueError(f"{package.get('package_id')}: malformed {key} record")
            result[str(record["evidence_task_id"])] = record
    return result

def citation_keys(task_ids: list[str], records: dict[str, dict[str, Any]], bib_map: dict[str, str]) -> list[str]:
    keys: list[str] = []
    for task_id in task_ids:
        if task_id not in records:
            raise ValueError(f"final synthesis references non-selected Evidence: {task_id}")
        card = records[task_id].get("card") or {}
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

def cite_tex(task_ids: list[str], records: dict[str, dict[str, Any]], bib_map: dict[str, str]) -> str:
    keys = citation_keys(task_ids, records, bib_map)
    return " \\cite{" + ",".join(keys) + "}" if keys else ""

def split_article_section(source: Path, body_target: Path) -> dict[str, str]:
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    section_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith(r"\section{")), None)
    if section_index is None:
        raise ValueError(f"{source}: top-level section heading not found")
    section_line = lines[section_index].strip()
    label_line = ""
    remove = {section_index}
    for index in range(section_index + 1, min(section_index + 4, len(lines))):
        stripped = lines[index].strip()
        if not stripped:
            continue
        if stripped.startswith(r"\label{"):
            label_line = stripped
            remove.add(index)
        break
    body_target.write_text("".join(line for i, line in enumerate(lines) if i not in remove), encoding="utf-8")
    return {"section_line": section_line, "label_line": label_line, "body_sha256": sha256_file(body_target)}

def render_final_synthesis(final: dict[str, Any], records: dict[str, dict[str, Any]], bib_map: dict[str, str]) -> tuple[str, list[str]]:
    title = str(final.get("title") or "").strip(); lead = str(final.get("lead") or "").strip(); boundary = str(final.get("boundary") or "").strip(); closing = str(final.get("closing") or "").strip()
    if not all((title, lead, boundary, closing)):
        raise ValueError("final synthesis requires title, lead, closing, and boundary")
    validate_reader_text("\n".join((title, lead, boundary, closing)), "final synthesis")
    used: list[str] = []
    lines = ["\\section{" + tex_escape(title) + "}", r"\label{sec:retrospective-synthesis}", r"\noindent\textbf{" + tex_escape(lead) + "}", r"\medskip", r"\begin{multicols}{2}"]
    sections = final.get("sections") or []
    if not isinstance(sections, list) or not sections:
        raise ValueError("final synthesis sections must be a non-empty list")
    for section in sections:
        heading = str(section.get("heading") or "").strip(); validate_reader_text(heading, "final synthesis heading")
        lines.append("\\subsection{" + tex_escape(heading) + "}")
        paragraphs = section.get("paragraphs") or []
        if not paragraphs:
            raise ValueError(f"final synthesis section has no paragraphs: {heading}")
        for paragraph in paragraphs:
            text = str(paragraph.get("text") or "").strip(); task_ids = [str(x) for x in (paragraph.get("evidence_task_ids") or [])]
            if not text or not task_ids:
                raise ValueError(f"final synthesis paragraph requires text and Evidence: {heading}")
            validate_reader_text(text, f"final synthesis paragraph: {heading}")
            lines.extend([tex_escape(text) + cite_tex(task_ids, records, bib_map), ""])
            used.extend(x for x in task_ids if x not in used)
    lines.extend([r"\end{multicols}", r"\Needspace{0.34\textheight}", r"\sectionkicker{Cross-chapter synthesis}", r"\subsection*{各章はどうつながるか}", r"\addcontentsline{toc}{subsection}{各章はどうつながるか}", r"\begin{center}", r"\small", r"\renewcommand{\arraystretch}{1.16}", r"\begin{tabularx}{\linewidth}{@{}p{0.26\linewidth}X@{}}", r"\toprule", r"接続する章 & 本号で見える構造的な関係 \\", r"\midrule"])
    relationships = final.get("relationships") or []
    if not isinstance(relationships, list) or not relationships:
        raise ValueError("final synthesis relationships must be a non-empty list")
    for row in relationships:
        from_name = str(row.get("from") or "").strip(); to_name = str(row.get("to") or "").strip(); relation = str(row.get("relation") or "").strip(); task_ids = [str(x) for x in (row.get("evidence_task_ids") or [])]
        if not from_name or not to_name or not relation or not task_ids:
            raise ValueError("final synthesis relationship requires from/to/relation/Evidence")
        validate_reader_text(from_name + "\n" + to_name + "\n" + relation, "final synthesis relationship")
        left = tex_escape(from_name) + r" $\rightarrow$ " + tex_escape(to_name)
        lines.append(left + " & " + tex_escape(relation) + cite_tex(task_ids, records, bib_map) + r" \\")
        used.extend(x for x in task_ids if x not in used)
    closing_heading = str(final.get("closing_heading") or "この月をどう位置づけるか").strip()
    if not closing_heading:
        raise ValueError("final synthesis closing heading must not be empty")
    validate_reader_text(closing_heading, "final synthesis closing heading")
    lines.extend([r"\bottomrule", r"\end{tabularx}", r"\renewcommand{\arraystretch}{1.0}", r"\end{center}", r"\normalsize", r"\begin{claimboundary}[この総括の境界]", tex_escape(boundary), r"\end{claimboundary}", "\\subsection*{" + tex_escape(closing_heading) + "}", "\\addcontentsline{toc}{subsection}{" + tex_escape(closing_heading) + "}"])
    closing_task_ids = [str(x) for x in (final.get("closing_evidence_task_ids") or [])]
    if not closing_task_ids:
        raise ValueError("final synthesis closing Evidence is required")
    lines.append(tex_escape(closing) + cite_tex(closing_task_ids, records, bib_map)); used.extend(x for x in closing_task_ids if x not in used); lines.append("")
    return "\n".join(lines), used

def build_main_tex(current_main: Path, manifest: dict[str, Any], layout_records: dict[str, dict[str, str]], synthesis_paths: dict[str, str], final_path: str) -> str:
    text = current_main.read_text(encoding="utf-8"); preamble = text.split(r"\begin{document}", 1)[0]
    preamble = preamble.replace("% Special-local mixed presentation: narrative two-column, synthesis/technical notes full-width. Shared weekly source remains unchanged.", "% Special-local balanced mixed presentation: full-width chapter headings, balanced two-column narrative, full-width synthesis/technical notes. Shared weekly source remains unchanged.")
    if r"\usepackage{multicol}" not in preamble:
        preamble = preamble.replace(r"\usepackage{jgaisurvey}", r"\usepackage{jgaisurvey}" + "\n" + r"\usepackage{multicol}" + "\n" + r"\usepackage{needspace}")
    if r"\setlength{\columnsep}" not in preamble:
        preamble += "\\setlength{\\columnsep}{6mm}\n"
    if r"\setlength{\multicolsep}" not in preamble:
        preamble += "\\setlength{\\multicolsep}{0.8em plus 0.2em minus 0.1em}\n"
    lines = [preamble.rstrip(), "", r"\begin{document}", r"\surveycover", r"\clearpage", r"\input{sections/00-frontmatter}", ""]
    for article in manifest.get("articles") or []:
        package_id = str(article["package_id"]); layout = layout_records[package_id]
        lines.extend([r"\clearpage", layout["section_line"]])
        if layout.get("label_line"): lines.append(layout["label_line"])
        lines.extend([r"\vspace{0.15em}", r"\begin{multicols}{2}", "\\input{" + input_path(layout["body_path"]) + "}", r"\end{multicols}"])
        synth = synthesis_paths.get(package_id)
        if synth: lines.extend([r"\Needspace{0.34\textheight}", "\\input{" + input_path(synth) + "}", r"\medskip"])
        lines.extend(["\\input{" + input_path(str(article["technical_notes_path"])) + "}", ""])
    lines.extend([r"\clearpage", "\\input{" + input_path(final_path) + "}", r"\clearpage", r"\printbibliography[title={References / Source Notes}]", r"\end{document}", ""])
    return "\n".join(lines)

def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"; state = load_json(state_path); gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE": raise ValueError(f"balanced layout revision requires RELEASE_CANDIDATE, got {state.get('lifecycle_state')}")
    if gates.get("latex_build") != "passed" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending": raise ValueError("balanced layout revision requires built PDF with Visual Review and Freeze still pending")
    current = dict(state.get("provenance", {}).get("validated_issue_source") or {}); current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha256_file(current_manifest_path) != current.get("sha256"): raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path); current_dir = current_manifest_path.parent
    final_artifact_path = repo_root / "sources" / issue_id / "editorial" / f"final-synthesis-{source_version}.json"; final_artifact = load_json(final_artifact_path)
    if final_artifact.get("issue_id") != issue_id or final_artifact.get("revision") != source_version: raise ValueError("final synthesis issue/revision mismatch")
    constraints = final_artifact.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False or constraints.get("selected_evidence_only") is not True: raise ValueError("final synthesis must be selected-Evidence-only and forbid new external Evidence")
    plan_path = repo_root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json"; plan = load_json(plan_path)
    if plan.get("status") != "APPROVED": raise ValueError("Issue Architecture must remain APPROVED")
    package_plan = {str(p["package_id"]): p for p in plan.get("packages") or [] if isinstance(p, dict) and p.get("package_id")}
    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists(): raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_dir, output_dir); layout_dir = output_dir / "layout-bodies"; layout_dir.mkdir(parents=True, exist_ok=True); final_dir = output_dir / "final-synthesis"; final_dir.mkdir(parents=True, exist_ok=True)
    bib_map = parse_bib_url_map(output_dir / "references.bib"); global_records: dict[str, dict[str, Any]] = {}; layout_records: dict[str, dict[str, str]] = {}
    for article in current_manifest.get("articles") or []:
        package_id = str(article["package_id"])
        if package_id not in package_plan or package_plan[package_id].get("package_type") not in ARTICLE_TYPES: raise ValueError(f"approved Architecture package missing/mismatched: {package_id}")
        package_path = repo_root / str(article["draft_package_path"])
        if sha256_file(package_path) != article["draft_package_sha256"]: raise ValueError(f"Draft Package digest mismatch: {package_id}")
        for task_id, record in evidence_index(load_json(package_path)).items():
            if task_id in global_records and global_records[task_id] != record: raise ValueError(f"conflicting Evidence record for {task_id}")
            global_records[task_id] = record
        original_section = output_dir / str(article["article_section_path"]); body_rel = f"layout-bodies/{package_id}.tex"; split = split_article_section(original_section, output_dir / body_rel)
        layout_records[package_id] = {"section_line": split["section_line"], "label_line": split["label_line"], "body_path": body_rel, "body_sha256": split["body_sha256"], "original_section_sha256": sha256_file(original_section)}
        if sha256_file(original_section) != article["article_section_sha256"]: raise ValueError(f"accepted article section changed unexpectedly: {package_id}")
        notes_path = output_dir / str(article["technical_notes_path"])
        if sha256_file(notes_path) != article["technical_notes_sha256"]: raise ValueError(f"Technical Notes changed unexpectedly: {package_id}")
    synthesis_paths = {str(item["package_id"]): str(item["path"]) for item in (current_manifest.get("theme_synthesis") or []) if isinstance(item, dict) and item.get("package_id") and item.get("path")}
    for path in synthesis_paths.values():
        if not (output_dir / path).is_file(): raise ValueError(f"preserved Theme Synthesis file missing: {path}")
    final_tex, final_used = render_final_synthesis(final_artifact, global_records, bib_map); final_rel = "final-synthesis/70-retrospective-synthesis.tex"; final_path = output_dir / final_rel; final_path.write_text(final_tex, encoding="utf-8")
    main_path = output_dir / "main.tex"; main_path.write_text(build_main_tex(current_dir / "main.tex", current_manifest, layout_records, synthesis_paths, final_rel), encoding="utf-8")
    new_manifest = dict(current_manifest); new_manifest["source_version"] = source_version; new_manifest["status"] = "VALIDATED_BALANCED_MIXED_LAYOUT_REVISION"; new_manifest["derivation"] = "Visual-review revision of the previous validated source. Accepted Article Draft sections, Theme Synthesis panels, and Technical Notes are preserved; layout-only article-body derivatives balance two narrative columns before returning to full-width Evidence material. A new final chapter synthesizes only already-selected Evidence."
    new_manifest["basis"] = dict(current_manifest.get("basis") or {}); new_manifest["basis"]["previous_source_manifest_path"] = current["path"]; new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["layout"] = {"document_font_size": "11pt", "body_mode": "balanced mixed: full-width chapter headings; multicol two-column narrative; full-width synthesis and Technical Notes", "margin": "22mm", "column_gap": "6mm", "transition_policy": "balance narrative columns in place; no hard twocolumn/onecolumn switch between narrative and synthesis", "technical_note_policy": "full-width; exact normalized claims/limitations/source URLs from the prior validated revision"}
    new_manifest["main_tex"] = {"path": "main.tex", "sha256": sha256_file(main_path)}
    new_manifest["article_layout_bodies"] = [{"package_id": package_id, "path": record["body_path"], "sha256": record["body_sha256"], "original_article_section_sha256": record["original_section_sha256"], "transform": "remove only top-level section/label from the layout derivative; render those lines full-width in main.tex"} for package_id, record in layout_records.items()]
    new_manifest["final_synthesis"] = {"artifact_path": final_artifact_path.relative_to(repo_root).as_posix(), "artifact_sha256": sha256_file(final_artifact_path), "tex_path": final_rel, "tex_sha256": sha256_file(final_path), "new_external_evidence": False, "selected_evidence_only": True, "referenced_evidence_task_ids": final_used}
    new_manifest["layout_revision"] = {"from_source_version": current_manifest.get("source_version"), "full_width_chapter_headings": True, "balanced_multicols": True, "hard_column_mode_switches": False, "article_sections_changed": False, "theme_synthesis_changed": False, "technical_notes_changed": False, "final_chapter_added": True, "new_external_evidence": False}
    manifest_path = output_dir / "source-manifest.json"; write_json(manifest_path, new_manifest); manifest_sha = sha256_file(manifest_path)
    history = state.setdefault("provenance_history", {}); history.setdefault("validated_issue_source", []).append(current); previous_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if previous_build: history.setdefault("latex_build", []).append(previous_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"; state["gates"]["latex_build"] = "pending"; state["gates"]["visual_review"] = "pending"; state["gates"]["freeze"] = "pending"
    state["provenance"]["validated_issue_source"] = {"path": manifest_path.relative_to(repo_root).as_posix(), "sha256": manifest_sha, "source_version": source_version, "layout_mode": "balanced-multicol-narrative-full-width-evidence", "final_synthesis_sha256": sha256_file(final_artifact_path)}
    state["provenance"].pop("latex_build", None); state["provenance"]["reader_layout_revision"] = {"source_version": source_version, "final_synthesis_path": final_artifact_path.relative_to(repo_root).as_posix(), "final_synthesis_sha256": sha256_file(final_artifact_path), "reason": "Human Visual Review feedback: eliminate chapter-heading collision, remove wasteful hard column-mode page breaks, balance two-column narrative before full-width Evidence material, and add a final cross-chapter retrospective synthesis."}; write_json(state_path, state)
    return {"schema_version": "1.0", "issue_id": issue_id, "special_slug": special_slug, "source_version": source_version, "previous_source_version": current_manifest.get("source_version"), "source_manifest": manifest_path.relative_to(repo_root).as_posix(), "source_manifest_sha256": manifest_sha, "article_layout_body_count": len(layout_records), "preserved_theme_synthesis_count": len(synthesis_paths), "final_synthesis_evidence_task_count": len(final_used), "article_sections_changed": False, "theme_synthesis_changed": False, "technical_notes_changed": False, "new_external_evidence": False, "lifecycle_state": state["lifecycle_state"], "latex_build_gate": state["gates"]["latex_build"]}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--repo-root", default="."); parser.add_argument("--special-slug", required=True); parser.add_argument("--issue-id", required=True); parser.add_argument("--source-version", required=True); args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version); print(json.dumps(result, ensure_ascii=False, indent=2)); return 0

if __name__ == "__main__": raise SystemExit(main())
