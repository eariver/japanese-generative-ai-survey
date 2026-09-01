#!/usr/bin/env python3
"""Expand a validated retrospective Special using only selected Evidence cards.

The previous validated source remains immutable. A new source revision is written
under surveys/special/<slug>/revisions/<version> and becomes the state-pinned
current source. No browsing or new factual claims occur here: the expansion is a
reader-facing rendering of immutable Draft Package chronology, normalized claims,
limitations, and primary-source URLs.
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
                raise ValueError(f"{package.get('package_id')}: invalid Evidence record")
            result.append((role, item))
    return result


def card(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("card") or {}
    if not isinstance(value, dict):
        raise ValueError("Evidence card must be an object")
    return value


def card_name(record: dict[str, Any]) -> str:
    artifact = card(record).get("artifact") or {}
    return str(artifact.get("canonical_name") or record.get("evidence_task_id") or "Unnamed Evidence")


def organization(record: dict[str, Any]) -> str:
    artifact = card(record).get("artifact") or {}
    value = artifact.get("organization")
    return str(value) if value else "-"


def artifact_type(record: dict[str, Any]) -> str:
    artifact = card(record).get("artifact") or {}
    return str(artifact.get("artifact_type") or "-")


def event_dates(record: dict[str, Any]) -> str:
    events = (card(record).get("temporal") or {}).get("events") or []
    values: list[str] = []
    for event in events:
        if not isinstance(event, dict) or not event.get("event_date"):
            continue
        text = str(event["event_date"])
        if event.get("event_type"):
            text += f" ({event['event_type']})"
        values.append(text)
    return "; ".join(values) if values else "-"


def source_urls(record: dict[str, Any]) -> list[str]:
    result: list[str] = []
    for source in card(record).get("sources") or []:
        if isinstance(source, dict) and isinstance(source.get("url"), str):
            url = source["url"].strip()
            if url and url not in result:
                result.append(url)
    return result


def render_at_glance(package: dict[str, Any]) -> str:
    lines = [
        r"\subsection*{Theme at a glance}",
        r"\addcontentsline{toc}{subsection}{Theme at a glance}",
        r"\begin{center}",
        r"\footnotesize",
        r"\begin{tabularx}{\linewidth}{@{}p{0.20\linewidth}p{0.10\linewidth}p{0.14\linewidth}X@{}}",
        r"\toprule",
        r"Artifact & Role & Type & Objective chronology \\",
        r"\midrule",
    ]
    for role, record in evidence_records(package):
        row = "{} & {} & {} & {} \\\\".format(
            tex_escape(card_name(record)),
            tex_escape(role),
            tex_escape(artifact_type(record)),
            tex_escape(event_dates(record)),
        )
        lines.append(row)
    lines.extend([r"\bottomrule", r"\end{tabularx}", r"\end{center}", r"\normalsize", ""])
    return "\n".join(lines)


def render_note(role: str, record: dict[str, Any]) -> str:
    c = card(record)
    claims = c.get("claims") or []
    limitations = c.get("limitations") or []
    task_id = str(record.get("evidence_task_id") or "")
    lines = [
        "\\begin{{technicalnote}}{{{}}}{{{}}}".format(tex_escape(card_name(record)), tex_escape(role)),
        r"\begin{tabularx}{\linewidth}{@{}>{\bfseries}p{0.22\linewidth}X@{}}",
        "Organization & {} \\\\".format(tex_escape(organization(record))),
        "Artifact type & {} \\\\".format(tex_escape(artifact_type(record))),
        "Chronology & {} \\\\".format(tex_escape(event_dates(record))),
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
            label = CLASS_LABELS.get(cls, cls or "Claim")
            lines.append("\\item \\textbf{{{}}}: {}".format(tex_escape(label), tex_escape(str(claim["text"]))))
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
            label = CLASS_LABELS.get(cls, cls)
            lines.append("\\item \\textbf{{{}}}: {}".format(tex_escape(label), tex_escape(str(limitation["text"]))))
        lines.append(r"\end{itemize}")

    urls = source_urls(record)
    if urls:
        lines.extend([r"{\bfseries Primary source}", r"\begin{itemize}[leftmargin=1.5em,itemsep=0.25em]"])
        for url in urls:
            # URLs have already been accepted in Evidence; \url performs its own escaping.
            lines.append("\\item \\url{{{}}}".format(url))
        lines.append(r"\end{itemize}")

    lines.extend([
        "{\\scriptsize\\color{{SurveyMuted}}Source-bound record: \\texttt{{{}}}.}".format(tex_escape(task_id)),
        r"\end{technicalnote}",
        r"\medskip",
        "",
    ])
    return "\n".join(lines)


def render_technical_notes(package: dict[str, Any]) -> str:
    lines = [
        r"\clearpage",
        r"\sectionkicker{Source-backed technical notes}",
        "\\subsection*{{{}: Technical Notes}}".format(tex_escape(str(package["title"]))),
        "この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。"
        "新しい外部情報は追加せず、Selection済みEvidenceのchronology、normalized claim、limitations、source URLのみを再配置する。",
        r"\medskip",
        render_at_glance(package),
    ]
    for role, record in evidence_records(package):
        lines.append(render_note(role, record))
    return "\n".join(lines)


def copy_article_tex(article_run_dir: Path, acceptance: dict[str, Any], package_id: str, target: Path) -> dict[str, str]:
    row_by_id = {row["package_id"]: row for row in acceptance.get("results") or []}
    if package_id not in row_by_id:
        raise ValueError(f"accepted Article Draft missing package: {package_id}")
    row = row_by_id[package_id]
    source = article_run_dir / row["tex_path"]
    if sha256_file(source) != row["tex_sha256"]:
        raise ValueError(f"accepted rendered TeX digest mismatch: {package_id}")
    lines = source.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith(r"\section{"):
            lines.insert(i + 1, f"\\label{{pkg:{package_id}}}")
            break
    else:
        raise ValueError(f"rendered article lacks section heading: {package_id}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"source_sha256": row["tex_sha256"], "expanded_sha256": sha256_file(target)}


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError(f"source expansion requires VALIDATED_DRAFT, got {state.get('lifecycle_state')}")
    if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "pending":
        raise ValueError("source expansion requires claim validation passed and latex_build pending")

    previous_source = dict(state["provenance"]["validated_issue_source"])
    previous_manifest_path = repo_root / previous_source["path"]
    if sha256_file(previous_manifest_path) != previous_source["sha256"]:
        raise ValueError("previous validated source manifest digest mismatch")
    previous_manifest = load_json(previous_manifest_path)

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

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"expanded source version already exists: {output_dir}")
    sections_dir = output_dir / "sections"
    notes_dir = output_dir / "technical-notes"
    sections_dir.mkdir(parents=True)
    notes_dir.mkdir(parents=True)

    front_lines = [
        "% Generated from validated synthesis. Do not hand-edit.",
        r"\section*{Monthly Signals}",
        r"\addcontentsline{toc}{section}{Monthly Signals}",
    ]
    for signal in synthesis["this_week_signals"]:
        refs = " / ".join(f"p.~\\pageref{{pkg:{pid}}}" for pid in signal["package_ids"])
        front_lines.extend([
            r"\smallskip",
            "\\noindent\\textbf{{{}}} {} \\hfill{{\\footnotesize {}}}\\par".format(
                tex_escape(signal["title"]), tex_escape(signal["summary"]), refs
            ),
        ])
    front_lines.extend([
        r"\medskip",
        r"\begin{claimboundary}[Retrospective scope]",
        "本号は2026年7月を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。Coverage Periodと制作時点を同一視せず、vendor / project / author claimの境界は各記事とTechnical Notesで明示する。",
        r"\end{claimboundary}",
        r"\medskip",
        r"\tableofcontents",
        "",
    ])
    front_path = sections_dir / "00-frontmatter.tex"
    front_path.write_text("\n".join(front_lines), encoding="utf-8")

    package_plans = [p for p in plan["packages"] if p["package_type"] in ARTICLE_TYPES]
    package_plans.sort(key=lambda p: p["drafting_order"])
    inputs: list[str] = []
    article_records: list[dict[str, Any]] = []
    for index, package_plan in enumerate(package_plans, start=1):
        package_id = package_plan["package_id"]
        article_target = sections_dir / f"{index * 10:02d}-{package_id}.tex"
        hashes = copy_article_tex(article_run_dir, acceptance, package_id, article_target)
        package_path = package_dir / f"{package_id}.json"
        package = load_json(package_path)
        note_target = notes_dir / f"{index * 10:02d}-{package_id}-notes.tex"
        note_target.write_text(render_technical_notes(package), encoding="utf-8")
        inputs.append(f"\\clearpage\n\\input{{sections/{article_target.stem}}}")
        inputs.append(f"\\input{{technical-notes/{note_target.stem}}}")
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

    previous_refs = previous_manifest_path.parent / previous_manifest["references"]["path"]
    refs_target = output_dir / "references.bib"
    shutil.copyfile(previous_refs, refs_target)

    accepted_by_id = {
        row["package_id"]: load_json(article_run_dir / row["draft_path"])["headline"]
        for row in acceptance["results"]
    }
    anchor_text = " \\quad / \\quad ".join(
        tex_escape(accepted_by_id[pid]) for pid in synthesis["cover"]["anchor_package_ids"]
    )
    coverage_start = state["calendar"]["collection_window_start"][:10]
    coverage_end = state["calendar"]["collection_window_end"][:10]
    retrospective = state["calendar"]["retrospective_as_of"][:10]

    main = f"""\\documentclass[lualatex,a4paper,11pt]{{jlreq}}
\\usepackage{{jgaisurvey}}
\\addbibresource{{references.bib}}

% Special-local long-form presentation. Shared weekly source remains unchanged.
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
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
