#!/usr/bin/env python3
"""Expand an already validated Special source using only accepted Draft Packages.

This is a deterministic reader-facing expansion stage for retrospective Specials
whose compact article prose does not fill the approved page budget. It does not
browse, reopen Screening, or invent new claims. For every selected article it
renders, directly from the immutable Draft Package Evidence cards:

- a theme-at-a-glance matrix;
- one Source-backed Technical Note per primary/supporting Evidence record;
- objective event chronology;
- all normalized claims with their claim class;
- all recorded limitations;
- primary-source URLs.

The previous validated source remains immutable. The expanded source is written
under `surveys/special/<slug>/revisions/<version>/`, and pipeline provenance keeps
both the previous and current source manifests. Lifecycle stays VALIDATED_DRAFT;
PDF build / Visual Review remain later gates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from scripts.render_article_draft_tex import tex_escape

ARTICLE_TYPES = {
    "LEAD", "FEATURE", "COMPARISON", "SECTION", "DEEP_DIVE", "PAPER_WATCH",
    "X_COMMUNITY", "LATE_BREAKING", "WATCHLIST_CHRONOLOGY",
}
CLASS_LABELS = {
    "PRIMARY_FACT": "一次情報で確認できる事実",
    "VENDOR_CLAIM": "Vendor claim",
    "PROJECT_CLAIM": "Project claim",
    "AUTHOR_CLAIM": "Author claim",
    "SOCIAL_OBSERVATION": "Community observation",
    "INFERENCE": "分析上の留意点",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evidence_records(package: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    result: list[tuple[str, dict[str, Any]]] = []
    for role, key in (("PRIMARY", "primary_evidence"), ("SUPPORTING", "supporting_evidence")):
        values = package.get(key) or []
        if not isinstance(values, list):
            raise ValueError(f"{package.get('package_id')}: {key} must be an array")
        for item in values:
            if not isinstance(item, dict):
                raise ValueError(f"{package.get('package_id')}: invalid Evidence record in {key}")
            result.append((role, item))
    return result


def card_name(record: dict[str, Any]) -> str:
    card = record.get("card") or {}
    artifact = card.get("artifact") or {}
    return str(artifact.get("canonical_name") or record.get("evidence_task_id") or "Unnamed Evidence")


def organization(record: dict[str, Any]) -> str:
    artifact = (record.get("card") or {}).get("artifact") or {}
    value = artifact.get("organization")
    return str(value) if value else "-"


def artifact_type(record: dict[str, Any]) -> str:
    artifact = (record.get("card") or {}).get("artifact") or {}
    return str(artifact.get("artifact_type") or "-")


def event_dates(record: dict[str, Any]) -> str:
    events = ((record.get("card") or {}).get("temporal") or {}).get("events") or []
    values: list[str] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        date = event.get("event_date")
        kind = event.get("event_type")
        if date:
            values.append(f"{date} ({kind})" if kind else str(date))
    return "; ".join(values) if values else "-"


def source_urls(record: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for source in (record.get("card") or {}).get("sources") or []:
        if isinstance(source, dict) and isinstance(source.get("url"), str) and source["url"].strip():
            url = source["url"].strip()
            if url not in values:
                values.append(url)
    return values


def render_at_glance(package: dict[str, Any]) -> str:
    rows = evidence_records(package)
    lines = [
        "\\subsection*{Theme at a glance}",
        "\\addcontentsline{toc}{subsection}{Theme at a glance}",
        "\\begin{center}",
        "\\footnotesize",
        "\\begin{tabularx}{\\linewidth}{@{}p{0.19\\linewidth}p{0.11\\linewidth}p{0.13\\linewidth}p{0.43\\linewidth}@{}}",
        "\\toprule",
        "Artifact & Role & Type & Objective chronology \\\\",
        "\\midrule",
    ]
    for role, record in rows:
        lines.append(
            f"{tex_escape(card_name(record))} & {tex_escape(role)} & {tex_escape(artifact_type(record))} & "
            f"{tex_escape(event_dates(record))} \\\\" 
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{center}", "\\normalsize", ""])
    return "\n".join(lines)


def render_note(role: str, record: dict[str, Any], index: int) -> str:
    card = record.get("card") or {}
    artifact = card.get("artifact") or {}
    claims = card.get("claims") or []
    limitations = card.get("limitations") or []
    sources = source_urls(record)
    task_id = str(record.get("evidence_task_id") or "")

    lines = [
        f"\\begin{{technicalnote}}{{{tex_escape(card_name(record))}}}{{{tex_escape(role)}}}",
        "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.22\\linewidth}X@{}}",
        f"Organization & {tex_escape(organization(record))} \\\\" ,
        f"Artifact type & {tex_escape(str(artifact.get('artifact_type') or '-'))} \\\\" ,
        f"Chronology & {tex_escape(event_dates(record))} \\\\" ,
        "\\end{tabularx}",
        "\\smallskip",
        "{\\bfseries 一次資料から整理したtechnical points}",
        "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]",
    ]
    if claims:
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            cls = str(claim.get("evidence_class") or "")
            label = CLASS_LABELS.get(cls, cls or "Claim")
            text = str(claim.get("text") or "")
            if text:
                lines.append(f"\\item \\textbf{{{tex_escape(label)}}}: {tex_escape(text)}")
    else:
        lines.append("\\item このEvidence recordには独立したnormalized claimは記録されていない。")
    lines.extend(["\\end{itemize}"])

    if limitations:
        lines.extend([
            "{\\bfseries 読む際の境界}",
            "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]",
        ])
        for limitation in limitations:
            if isinstance(limitation, dict) and limitation.get("text"):
                cls = str(limitation.get("evidence_class") or "INFERENCE")
                label = CLASS_LABELS.get(cls, cls)
                lines.append(f"\\item \\textbf{{{tex_escape(label)}}}: {tex_escape(str(limitation['text']))}")
        lines.append("\\end{itemize}")

    if sources:
        lines.extend(["{\\bfseries Primary source}", "\\begin{itemize}[leftmargin=1.5em,itemsep=0.25em]"])
        for url in sources:
            lines.append(f"\\item \\url{{{url}}}")
        lines.append("\\end{itemize}")

    lines.extend([
        f"{{\\scriptsize\\color{{SurveyMuted}}Source-bound record: \\texttt{{{tex_escape(task_id)}}}.}}
",
        "\\end{technicalnote}",
        "\\medskip",
        "",
    ])
    return "\n".join(lines)


def render_technical_notes(package: dict[str, Any]) -> str:
    lines = [
        "\\clearpage",
        "\\sectionkicker{Source-backed technical notes}",
        f"\\subsection*{{{tex_escape(package['title'])}: Technical Notes}}",
        "この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。"
        " 新しい外部情報は追加せず、Selection済みEvidence Cardのchronology、normalized claim、limitations、source URLのみを再配置する。",
        "\\medskip",
        render_at_glance(package),
    ]
    for index, (role, record) in enumerate(evidence_records(package), start=1):
        lines.append(render_note(role, record, index))
    return "\n".join(lines)


def copy_article_tex(article_run_dir: Path, acceptance: dict[str, Any], package_id: str, target: Path) -> dict[str, str]:
    row_by_id = {row["package_id"]: row for row in acceptance.get("results") or []}
    row = row_by_id[package_id]
    source = article_run_dir / row["tex_path"]
    if sha256_file(source) != row["tex_sha256"]:
        raise ValueError(f"accepted rendered TeX digest mismatch: {package_id}")
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    inserted = False
    for i, line in enumerate(lines):
        if line.startswith("\\section{"):
            lines.insert(i + 1, f"\\label{{pkg:{package_id}}}")
            inserted = True
            break
    if not inserted:
        raise ValueError(f"rendered TeX lacks section: {package_id}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"source_sha256": row["tex_sha256"], "expanded_sha256": sha256_file(target)}


def build(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError(f"source expansion requires VALIDATED_DRAFT, got {state.get('lifecycle_state')}")
    if state.get("gates", {}).get("claim_and_chronology_validation") != "passed":
        raise ValueError("claim_and_chronology_validation must already be passed")
    if state.get("gates", {}).get("latex_build") != "pending":
        raise ValueError("source expansion is only allowed before a successful PDF build")

    article_run_rel = state["provenance"]["article_draft"]["result_set_path"]
    article_run_dir = repo_root / article_run_rel
    acceptance = load_json(article_run_dir / "acceptance.json")
    plan_path = repo_root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json"
    plan = load_json(plan_path)
    if plan.get("status") != "APPROVED":
        raise ValueError("Issue Architecture must be APPROVED")
    package_dir = repo_root / "sources" / issue_id / "drafting" / "packages" / "v0.1"
    synthesis_path = repo_root / state["provenance"]["issue_synthesis"]["result_path"]
    synthesis = load_json(synthesis_path)

    previous_source = dict(state["provenance"]["validated_issue_source"])
    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"expanded source version already exists: {output_dir}")
    sections = output_dir / "sections"
    notes = output_dir / "technical-notes"
    sections.mkdir(parents=True)
    notes.mkdir(parents=True)

    package_plans = [p for p in plan["packages"] if p["package_type"] in ARTICLE_TYPES]
    package_plans.sort(key=lambda p: p["drafting_order"])
    article_records: list[dict[str, Any]] = []
    inputs: list[str] = []

    # Frontmatter: keep the validated synthesis, but give the Special a compact reader-facing overview.
    front_lines = [
        "% Generated from validated post-draft synthesis. Do not hand-edit.",
        "\\section*{Monthly Signals}",
        "\\addcontentsline{toc}{section}{Monthly Signals}",
    ]
    for signal in synthesis["this_week_signals"]:
        refs = " / ".join(f"p.~\\pageref{{pkg:{pid}}}" for pid in signal["package_ids"])
        front_lines.extend([
            "\\smallskip",
            f"\\noindent\\textbf{{{tex_escape(signal['title'])}}} {tex_escape(signal['summary'])} "
            f"\\hfill{{\\footnotesize {refs}}}\\par",
        ])
    front_lines.extend([
        "\\medskip",
        "\\begin{claimboundary}[Retrospective scope]",
        "本号は2026年7月を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。Coverage Periodと制作時点を同一視せず、vendor / project / author claimの境界は各記事とTechnical Notesで明示する。",
        "\\end{claimboundary}",
        "\\medskip",
        "\\tableofcontents",
        "",
    ])
    front_path = sections / "00-frontmatter.tex"
    front_path.write_text("\n".join(front_lines), encoding="utf-8")

    for index, package_plan in enumerate(package_plans, start=1):
        package_id = package_plan["package_id"]
        article_target = sections / f"{index * 10:02d}-{package_id}.tex"
        hashes = copy_article_tex(article_run_dir, acceptance, package_id, article_target)
        package_path = package_dir / f"{package_id}.json"
        package = load_json(package_path)
        note_target = notes / f"{index * 10:02d}-{package_id}-notes.tex"
        note_target.write_text(render_technical_notes(package), encoding="utf-8")
        inputs.extend([
            f"\\clearpage\n\\input{{sections/{article_target.stem}}}",
            f"\\input{{technical-notes/{note_target.stem}}}",
        ])
        article_records.append({
            "package_id": package_id,
            "page_target": package_plan["page_target"],
            "accepted_article_tex_sha256": hashes["source_sha256"],
            "article_section_path": article_target.relative_to(output_dir).as_posix(),
            "article_section_sha256": hashes["expanded_sha256"],
            "draft_package_path": package_path.relative_to(repo_root).as_posix(),
            "draft_package_sha256": sha256_file(package_path),
            "technical_notes_path": note_target.relative_to(output_dir).as_posix(),
            "technical_notes_sha256": sha256_file(note_target),
            "evidence_record_count": len(evidence_records(package)),
        })

    # Reuse validated, already-deduplicated bibliography bytes from v0.1 source.
    previous_manifest_path = repo_root / previous_source["path"]
    previous_manifest = load_json(previous_manifest_path)
    previous_refs = previous_manifest_path.parent / previous_manifest["references"]["path"]
    refs_target = output_dir / "references.bib"
    shutil.copyfile(previous_refs, refs_target)

    anchor_headlines = []
    accepted_by_id = {row["package_id"]: load_json(article_run_dir / row["draft_path"])["headline"] for row in acceptance["results"]}
    for pid in synthesis["cover"]["anchor_package_ids"]:
        anchor_headlines.append(accepted_by_id[pid])
    anchor_text = " \\quad / \\quad ".join(tex_escape(x) for x in anchor_headlines)
    coverage_start = state["calendar"]["collection_window_start"][:10]
    coverage_end = state["calendar"]["collection_window_end"][:10]
    retrospective = state["calendar"]["retrospective_as_of"][:10]

    main = f"""\\documentclass[lualatex,a4paper,11pt]{{jlreq}}
\\usepackage{{jgaisurvey}}
\\addbibresource{{references.bib}}

% Special-local long-form presentation. The shared weekly style stays unchanged.
\\geometry{{margin=22mm,headsep=5mm,footskip=10mm}}
\\setlength{{\\parskip}}{{0.35em}}
\\setlength{{\\parindent}}{{1em}}
\\newtcolorbox{{technicalnote}}[2]{{
  enhanced,breakable,colback=SurveySoft,colframe=SurveyAccent,
  boxrule=0.65pt,arc=1mm,title={{#1 \\hfill \\footnotesize #2}},fonttitle=\\bfseries,
  left=3mm,right=3mm,top=2mm,bottom=2mm,before skip=4mm,after skip=3mm
}}

\\surveysetup
  {{{tex_escape(issue_id)}}}
  {{Japanese Generative AI Technical Survey}}
  {{Special / Coverage {coverage_start} -- {coverage_end} / Retrospective as of {retrospective}}}
  {{Coverage window: {coverage_start} -- {coverage_end} UTC}}
\\surveyeditiondescriptor{{Retrospective Technical Survey}}
\\surveycoverstory
  {{{tex_escape(synthesis['cover']['headline'])}}}
  {{{tex_escape(synthesis['cover']['deck'])}}}
  {{{anchor_text}}}

\\begin{{document}}
\\surveycover
\\clearpage
\\input{{sections/00-frontmatter}}

{chr(10).join(inputs)}

\\clearpage
\\printbibliography[title={{References / Source Notes}}]
\\end{{document}}
"""
    main_path = output_dir / "main.tex"
    main_path.write_text(main, encoding="utf-8")

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "status": "VALIDATED_SOURCE_EXPANSION",
        "derivation": "Deterministic expansion from accepted Article Draft TeX and immutable Draft Package Evidence cards; no new external facts.",
        "basis": {
            "previous_source_manifest_path": previous_source["path"],
            "previous_source_manifest_sha256": previous_source["sha256"],
            "article_draft_result_set_path": article_run_rel,
            "article_draft_result_set_sha256": state["provenance"]["article_draft"]["result_set_sha256"],
            "architecture_plan_path": plan_path.relative_to(repo_root).as_posix(),
            "architecture_plan_sha256": sha256_file(plan_path),
            "synthesis_result_path": synthesis_path.relative_to(repo_root).as_posix(),
            "synthesis_result_sha256": sha256_file(synthesis_path),
        },
        "layout": {
            "document_font_size": "11pt",
            "body_mode": "single-column long-form",
            "margin": "22mm",
            "technical_note_policy": "one note per selected Evidence record; exact normalized claims/limitations/source URLs",
        },
        "article_count": len(article_records),
        "evidence_record_count": sum(row["evidence_record_count"] for row in article_records),
        "main_tex": {"path": "main.tex", "sha256": sha256_file(main_path)},
        "frontmatter": {"path": front_path.relative_to(output_dir).as_posix(), "sha256": sha256_file(front_path)},
        "references": {"path": "references.bib", "sha256": sha256_file(refs_target)},
        "articles": article_records,
    }
    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, manifest)

    history = state.setdefault("provenance_history", {}).setdefault("validated_issue_source", [])
    if previous_source not in history:
        history.append(previous_source)
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(manifest_path),
        "source_version": source_version,
        "expansion_basis": "selected Evidence cards only",
    }
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
    result = build(root, args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
