#!/usr/bin/env python3
"""Reader-facing LONGFORM_SPECIAL revision contract for Survey Production Core v2.

This module implements the post-draft Evidence-backed supplemental-synthesis path
allowed by docs/special-layout-policy.md. It never edits accepted Draft Package
bytes. Instead it validates a reviewed publication-only revision against the
already assigned package Evidence and renders mixed-layout reader-facing TeX.
"""
from __future__ import annotations

import re
from typing import Any, Callable

from scripts.render_article_draft_tex import tex_escape

FORBIDDEN_READER_PATTERNS = (
    "Core v2 Evidence:",
    "materiality:",
    "Selection済みEvidence",
    "normalized claim",
    "Source-bound record",
    "This retained evidence note",
    "The bound ",
)

_DISCOVERY_ID = re.compile(r"^[A-Za-z0-9._-]+-D\d{3,}$")


def _nonempty(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _reader_text(value: Any, label: str) -> str:
    text = _nonempty(value, label)
    for pattern in FORBIDDEN_READER_PATTERNS:
        if pattern.lower() in text.lower():
            raise ValueError(f"{label} leaks production metadata: {pattern}")
    if re.search(r"\bVerify\b", text):
        raise ValueError(f"{label} leaks an internal verification obligation")
    if re.search(r"\b[A-Za-z0-9._-]+-D\d{3,}\b", text):
        raise ValueError(f"{label} exposes a repository Discovery/Evidence identifier")
    return text


def _ids(value: Any, label: str, allowed: set[str]) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must contain one or more Discovery IDs")
    out: list[str] = []
    for raw in value:
        if not isinstance(raw, str) or not _DISCOVERY_ID.fullmatch(raw):
            raise ValueError(f"{label} contains an invalid Discovery ID: {raw!r}")
        if raw not in allowed:
            raise ValueError(f"{label} cites Evidence outside the approved package: {raw}")
        if raw not in out:
            out.append(raw)
    return out


def _validate_paragraph_rows(rows: Any, label: str, allowed: set[str]) -> list[dict[str, Any]]:
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{label} must be a non-empty list")
    out=[]
    for idx,row in enumerate(rows):
        if not isinstance(row,dict) or set(row)!={"text","discovery_ids"}:
            raise ValueError(f"{label}[{idx}] has an invalid envelope")
        out.append({
            "text":_reader_text(row["text"],f"{label}[{idx}].text"),
            "discovery_ids":_ids(row["discovery_ids"],f"{label}[{idx}].discovery_ids",allowed),
        })
    return out


def validate_revision(
    revision: Any,
    packages: list[dict[str, Any]],
    records: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if not isinstance(revision,dict):
        raise ValueError("LONGFORM_SPECIAL requires longform_revision for post-draft publication revision")
    expected={"review_reference","new_external_evidence","packages","cross_family_synthesis"}
    if set(revision)!=expected:
        raise ValueError("longform_revision envelope invalid")
    review_reference=_nonempty(revision["review_reference"],"longform_revision.review_reference")
    if revision["new_external_evidence"] is not False:
        raise ValueError("post-draft longform revision must not introduce new external Evidence")
    plan_by_id={p["package_id"]:p for p in packages}
    rows=revision["packages"]
    if not isinstance(rows,list) or len(rows)!=len(plan_by_id):
        raise ValueError("longform_revision must provide exactly one row per approved Architecture package")
    normalized=[]
    seen=set()
    selected_union:set[str]=set()
    for p in packages:
        selected_union.update(p["evidence_discovery_ids"])
    for idx,row in enumerate(rows):
        required={"package_id","theme_at_a_glance","narrative_sections","timeline","synthesis","reader_claim_boundary","technical_notes"}
        if not isinstance(row,dict) or set(row)!=required:
            raise ValueError(f"longform_revision.packages[{idx}] envelope invalid")
        pid=_nonempty(row["package_id"],f"packages[{idx}].package_id")
        if pid not in plan_by_id or pid in seen:
            raise ValueError(f"unknown or duplicate longform package: {pid}")
        seen.add(pid)
        allowed=set(plan_by_id[pid]["evidence_discovery_ids"])
        for did in allowed:
            evidence=records.get(did)
            if evidence is None:
                raise ValueError(f"approved package Evidence is missing from accepted Evidence: {pid}/{did}")
            if evidence.get("materiality")=="HOLD" or evidence.get("status")=="NEEDS_MORE":
                raise ValueError(f"longform package cannot promote HOLD/NEEDS_MORE Evidence: {pid}/{did}")
        glance=row["theme_at_a_glance"]
        if not isinstance(glance,list) or len(glance)<2:
            raise ValueError(f"{pid} Theme at a glance requires at least two rows")
        glance_out=[]
        for j,item in enumerate(glance):
            if not isinstance(item,dict) or set(item)!={"label","text","discovery_ids"}:
                raise ValueError(f"{pid} theme_at_a_glance[{j}] invalid")
            glance_out.append({
                "label":_reader_text(item["label"],f"{pid}.glance[{j}].label"),
                "text":_reader_text(item["text"],f"{pid}.glance[{j}].text"),
                "discovery_ids":_ids(item["discovery_ids"],f"{pid}.glance[{j}].discovery_ids",allowed),
            })
        sections=row["narrative_sections"]
        if not isinstance(sections,list) or len(sections)<2:
            raise ValueError(f"{pid} requires at least two supplemental narrative sections")
        sections_out=[]
        for j,section in enumerate(sections):
            if not isinstance(section,dict) or set(section)!={"heading","paragraphs"}:
                raise ValueError(f"{pid}.narrative_sections[{j}] invalid")
            sections_out.append({
                "heading":_reader_text(section["heading"],f"{pid}.narrative_sections[{j}].heading"),
                "paragraphs":_validate_paragraph_rows(section["paragraphs"],f"{pid}.narrative_sections[{j}].paragraphs",allowed),
            })
        timeline=row["timeline"]
        if not isinstance(timeline,list) or len(timeline)<2:
            raise ValueError(f"{pid} timeline requires at least two transition anchors")
        timeline_out=[]
        for j,item in enumerate(timeline):
            if not isinstance(item,dict) or set(item)!={"label","text","discovery_ids"}:
                raise ValueError(f"{pid}.timeline[{j}] invalid")
            timeline_out.append({
                "label":_reader_text(item["label"],f"{pid}.timeline[{j}].label"),
                "text":_reader_text(item["text"],f"{pid}.timeline[{j}].text"),
                "discovery_ids":_ids(item["discovery_ids"],f"{pid}.timeline[{j}].discovery_ids",allowed),
            })
        synthesis=row["synthesis"]
        if not isinstance(synthesis,dict) or set(synthesis)!={"heading","paragraphs"}:
            raise ValueError(f"{pid}.synthesis invalid")
        synthesis_out={
            "heading":_reader_text(synthesis["heading"],f"{pid}.synthesis.heading"),
            "paragraphs":_validate_paragraph_rows(synthesis["paragraphs"],f"{pid}.synthesis.paragraphs",allowed),
        }
        boundary=_validate_paragraph_rows(row["reader_claim_boundary"],f"{pid}.reader_claim_boundary",allowed)
        notes=row["technical_notes"]
        if not isinstance(notes,list) or not notes:
            raise ValueError(f"{pid} requires source-backed Technical Notes")
        note_out=[]; note_ids=[]
        for j,note in enumerate(notes):
            required_note={"title","discovery_id","chronology","technical_points","limitation","primary_url"}
            if not isinstance(note,dict) or set(note)!=required_note:
                raise ValueError(f"{pid}.technical_notes[{j}] invalid")
            did=note["discovery_id"]
            _ids([did],f"{pid}.technical_notes[{j}].discovery_id",allowed)
            evidence=records[did]; canonical_url=(evidence.get("entity") or {}).get("canonical_url")
            if note["primary_url"]!=canonical_url:
                raise ValueError(f"{pid}.technical_notes[{j}] primary_url differs from accepted Evidence: {did}")
            points=note["technical_points"]
            if not isinstance(points,list) or len(points)<2:
                raise ValueError(f"{pid}.technical_notes[{j}] requires at least two technical points")
            point_out=[_reader_text(v,f"{pid}.technical_notes[{j}].technical_points") for v in points]
            note_out.append({
                "title":_reader_text(note["title"],f"{pid}.technical_notes[{j}].title"),
                "discovery_id":did,
                "chronology":_reader_text(note["chronology"],f"{pid}.technical_notes[{j}].chronology"),
                "technical_points":point_out,
                "limitation":_reader_text(note["limitation"],f"{pid}.technical_notes[{j}].limitation"),
                "primary_url":canonical_url,
            })
            note_ids.append(did)
        if set(note_ids)!=allowed:
            missing=sorted(allowed-set(note_ids)); extra=sorted(set(note_ids)-allowed)
            raise ValueError(f"{pid} Technical Notes must cover every assigned Evidence source exactly once; missing={missing}, extra={extra}")
        normalized.append({
            "package_id":pid,"theme_at_a_glance":glance_out,"narrative_sections":sections_out,
            "timeline":timeline_out,"synthesis":synthesis_out,"reader_claim_boundary":boundary,"technical_notes":note_out,
        })
    if seen!=set(plan_by_id):
        raise ValueError("longform_revision package coverage differs from Architecture")
    cross=revision["cross_family_synthesis"]
    if not isinstance(cross,dict) or set(cross)!={"heading","paragraphs","comparison_rows"}:
        raise ValueError("cross_family_synthesis envelope invalid")
    comparison=cross["comparison_rows"]
    if not isinstance(comparison,list) or len(comparison)<3:
        raise ValueError("cross_family_synthesis requires at least three comparison rows")
    comp_out=[]
    for idx,row in enumerate(comparison):
        required_row={"dimension","glm","qwen","deepseek","kimi","discovery_ids"}
        if not isinstance(row,dict) or set(row)!=required_row:
            raise ValueError(f"cross_family_synthesis.comparison_rows[{idx}] invalid")
        comp_out.append({
            "dimension":_reader_text(row["dimension"],f"cross comparison[{idx}].dimension"),
            "glm":_reader_text(row["glm"],f"cross comparison[{idx}].glm"),
            "qwen":_reader_text(row["qwen"],f"cross comparison[{idx}].qwen"),
            "deepseek":_reader_text(row["deepseek"],f"cross comparison[{idx}].deepseek"),
            "kimi":_reader_text(row["kimi"],f"cross comparison[{idx}].kimi"),
            "discovery_ids":_ids(row["discovery_ids"],f"cross comparison[{idx}].discovery_ids",selected_union),
        })
    return {
        "review_reference":review_reference,
        "new_external_evidence":False,
        "packages":normalized,
        "cross_family_synthesis":{
            "heading":_reader_text(cross["heading"],"cross_family_synthesis.heading"),
            "paragraphs":_validate_paragraph_rows(cross["paragraphs"],"cross_family_synthesis.paragraphs",selected_union),
            "comparison_rows":comp_out,
        },
    }


def _cite(ids: list[str], bib_key_by_did: dict[str,str]) -> str:
    return "" if not ids else " \\cite{"+",".join(bib_key_by_did[d] for d in ids)+"}"


def render_package(
    spec: dict[str,Any],
    result: dict[str,Any],
    supplement: dict[str,Any],
    bib_key_by_did: dict[str,str],
    kicker: str,
) -> list[str]:
    pid=result["package_id"]
    lines=[
        "\\Needspace{0.24\\textheight}",
        f"\\section{{{tex_escape(result['headline'])}}}",
        f"\\label{{pkg:{tex_escape(pid)}}}",
        f"\\sectionkicker{{{tex_escape(kicker)}}}",
        "\\noindent\\textbf{"+tex_escape(result["deck"])+"}"+_cite(spec["deck_discovery_ids"],bib_key_by_did)+"\\par\\medskip",
        "\\begin{themeoverview}[Theme at a glance]",
        "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.22\\linewidth}X@{}}",
    ]
    for item in supplement["theme_at_a_glance"]:
        lines.append(tex_escape(item["label"])+" & "+tex_escape(item["text"])+_cite(item["discovery_ids"],bib_key_by_did)+" \\\\")
    lines.extend(["\\end{tabularx}","\\end{themeoverview}","\\medskip","\\begin{multicols}{2}"])
    spec_blocks={row["block_id"]:row for row in spec["blocks"]}
    for block in result["blocks"]:
        if block["block_type"]=="CLAIM_BOUNDARY":
            continue
        source_spec=spec_blocks.get(block["block_id"])
        if source_spec is None:
            raise ValueError(f"non-boundary Draft block missing semantic source: {pid}/{block['block_id']}")
        lines.extend([
            f"% block:{block['block_id']} attribution:{block['attribution_mode']}",
            "\\noindent "+tex_escape(block["text"])+_cite(source_spec.get("discovery_ids",[]),bib_key_by_did)+"\\par\\medskip",
        ])
    for section in supplement["narrative_sections"]:
        lines.append("\\subsection*{"+tex_escape(section["heading"])+"}")
        for para in section["paragraphs"]:
            lines.append("\\noindent "+tex_escape(para["text"])+_cite(para["discovery_ids"],bib_key_by_did)+"\\par\\medskip")
    lines.extend(["\\end{multicols}","\\medskip","\\subsection*{Transition timeline}","\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.20\\linewidth}X@{}}"])
    for item in supplement["timeline"]:
        lines.append(tex_escape(item["label"])+" & "+tex_escape(item["text"])+_cite(item["discovery_ids"],bib_key_by_did)+" \\\\")
    lines.extend(["\\end{tabularx}","\\medskip","\\subsection*{"+tex_escape(supplement["synthesis"]["heading"])+"}"])
    for para in supplement["synthesis"]["paragraphs"]:
        lines.append("\\noindent "+tex_escape(para["text"])+_cite(para["discovery_ids"],bib_key_by_did)+"\\par\\medskip")
    lines.append("\\begin{claimboundary}[Claim boundary]")
    for para in supplement["reader_claim_boundary"]:
        lines.append("\\noindent "+tex_escape(para["text"])+_cite(para["discovery_ids"],bib_key_by_did)+"\\par")
    lines.extend(["\\end{claimboundary}","\\medskip","\\subsection*{Source-backed Technical Notes}"])
    for note in supplement["technical_notes"]:
        did=note["discovery_id"]
        lines.extend([
            "\\begin{technicalnote}["+tex_escape(note["title"])+"]",
            "\\noindent\\textbf{Chronology:} "+tex_escape(note["chronology"])+_cite([did],bib_key_by_did)+"\\par",
            "\\smallskip\\noindent\\textbf{Technical points:}\\par",
            "\\begin{itemize}",
        ])
        for point in note["technical_points"]:
            lines.append("\\item "+tex_escape(point)+_cite([did],bib_key_by_did))
        lines.extend([
            "\\end{itemize}",
            "\\noindent\\textbf{Limitation / attribution:} "+tex_escape(note["limitation"])+"\\par",
            "\\smallskip\\noindent\\textbf{Primary URL:} \\url{"+note["primary_url"]+"}\\par",
            "\\end{technicalnote}","\\smallskip",
        ])
    return lines


def render_cross_family(cross: dict[str,Any], bib_key_by_did: dict[str,str]) -> list[str]:
    lines=["\\Needspace{0.30\\textheight}","\\section{"+tex_escape(cross["heading"])+"}","\\sectionkicker{CROSS-FAMILY SYNTHESIS}"]
    for para in cross["paragraphs"]:
        lines.append("\\noindent "+tex_escape(para["text"])+_cite(para["discovery_ids"],bib_key_by_did)+"\\par\\medskip")
    lines.extend([
        "\\begin{sidewaysfigure}",
        "\\centering",
        "\\small",
        "\\begin{tabularx}{0.96\\textheight}{@{}>{\\bfseries}p{0.12\\textheight}XXXX@{}}",
        "\\toprule",
        "観点 & GLM & Qwen & DeepSeek & Kimi \\\\",
        "\\midrule",
    ])
    for row in cross["comparison_rows"]:
        citation=_cite(row["discovery_ids"],bib_key_by_did)
        lines.append(tex_escape(row["dimension"])+" & "+tex_escape(row["glm"])+" & "+tex_escape(row["qwen"])+" & "+tex_escape(row["deepseek"])+" & "+tex_escape(row["kimi"])+citation+" \\\\")
    lines.extend(["\\bottomrule","\\end{tabularx}","\\caption{同一benchmark順位ではなく、各系譜がどの問題設定をどの層で解いたかを比較する。}","\\end{sidewaysfigure}"])
    return lines


def preflight_tex(tex: str, bibliography: str, package_count: int) -> dict[str,Any]:
    findings=[]
    multicol_count=tex.count("\\begin{multicols}{2}")
    if multicol_count < package_count+1:
        findings.append(f"balanced two-column narrative flows missing: {multicol_count} < {package_count+1}")
    if "\\end{claimboundary}\n\\clearpage" in tex:
        findings.append("package-level unconditional clearpage after Claim Boundary detected")
    if tex.count("\\clearpage") > 2:
        findings.append(f"too many unconditional clearpage commands for LONGFORM_SPECIAL: {tex.count('\\\\clearpage')}")
    if tex.count("\\begin{technicalnote}") < package_count:
        findings.append("reader-facing Source-backed Technical Notes are missing")
    if "Theme at a glance" not in tex or "CROSS-FAMILY SYNTHESIS" not in tex:
        findings.append("structured reader-facing synthesis layer is incomplete")
    joined=tex+"\n"+bibliography
    for pattern in FORBIDDEN_READER_PATTERNS:
        if pattern.lower() in joined.lower():
            findings.append(f"production metadata leaked into reader-facing source: {pattern}")
    if re.search(r"\bVerify\b",joined):
        findings.append("internal Verify obligation leaked into reader-facing source")
    return {
        "status":"PASS" if not findings else "FAIL",
        "package_count":package_count,
        "multicol_flow_count":multicol_count,
        "clearpage_count":tex.count("\\clearpage"),
        "technical_note_count":tex.count("\\begin{technicalnote}"),
        "findings":findings,
    }
