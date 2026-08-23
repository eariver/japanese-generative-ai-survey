#!/usr/bin/env python3
"""Narrow reader-facing overrides for Core v2 LONGFORM_SPECIAL revisions.

The accepted-Evidence validator remains in survey_longform_publication_v2_base.
This wrapper only changes publication rendering and strengthens leakage/layout
preflight for a Human-review revision; accepted Draft/Evidence bytes stay intact.
"""
from __future__ import annotations

from typing import Any

from scripts import survey_longform_publication_v2_base as _base
from scripts.render_article_draft_tex import tex_escape

# Re-export the base contract and strengthen its reader-text validator in place.
validate_revision = _base.validate_revision
FORBIDDEN_READER_PATTERNS = tuple(_base.FORBIDDEN_READER_PATTERNS) + (
    "Evidence pass",
    "本Evidence",
)
_base.FORBIDDEN_READER_PATTERNS = FORBIDDEN_READER_PATTERNS


def _cite(ids: list[str], bib_key_by_did: dict[str, str]) -> str:
    return _base._cite(ids, bib_key_by_did)


def render_package(
    spec: dict[str, Any],
    result: dict[str, Any],
    supplement: dict[str, Any],
    bib_key_by_did: dict[str, str],
    kicker: str,
) -> list[str]:
    """Render reviewed longform prose without replaying raw production Draft blocks."""
    pid = result["package_id"]
    lines = [
        "\\Needspace{0.24\\textheight}",
        f"\\section{{{tex_escape(result['headline'])}}}",
        f"\\label{{pkg:{tex_escape(pid)}}}",
        f"\\sectionkicker{{{tex_escape(kicker)}}}",
        "\\noindent\\textbf{" + tex_escape(result["deck"]) + "}"
        + _cite(spec["deck_discovery_ids"], bib_key_by_did) + "\\par\\medskip",
        "\\begin{themeoverview}[Theme at a glance]",
        "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.22\\linewidth}X@{}}",
    ]
    for item in supplement["theme_at_a_glance"]:
        lines.append(
            tex_escape(item["label"]) + " & " + tex_escape(item["text"])
            + _cite(item["discovery_ids"], bib_key_by_did) + " \\\\"
        )
    lines.extend([
        "\\end{tabularx}", "\\end{themeoverview}", "\\medskip",
        "\\begin{multicols}{2}",
    ])
    for section in supplement["narrative_sections"]:
        lines.append("\\subsection*{" + tex_escape(section["heading"]) + "}")
        for para in section["paragraphs"]:
            lines.append(
                "\\noindent " + tex_escape(para["text"])
                + _cite(para["discovery_ids"], bib_key_by_did) + "\\par\\medskip"
            )
    lines.extend([
        "\\end{multicols}", "\\medskip", "\\begin{wideflow}",
        "\\subsection*{Transition timeline}",
        "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.20\\linewidth}X@{}}",
    ])
    for item in supplement["timeline"]:
        lines.append(
            tex_escape(item["label"]) + " & " + tex_escape(item["text"])
            + _cite(item["discovery_ids"], bib_key_by_did) + " \\\\"
        )
    lines.extend(["\\end{tabularx}", "\\end{wideflow}", "\\medskip"])
    lines.extend(["\\begin{multicols}{2}", "\\subsection*{" + tex_escape(supplement["synthesis"]["heading"]) + "}"])
    for para in supplement["synthesis"]["paragraphs"]:
        lines.append(
            "\\noindent " + tex_escape(para["text"])
            + _cite(para["discovery_ids"], bib_key_by_did) + "\\par\\medskip"
        )
    lines.extend(["\\end{multicols}", "\\medskip", "\\begin{claimboundary}[Claim boundary]"])
    for para in supplement["reader_claim_boundary"]:
        lines.append(
            "\\noindent " + tex_escape(para["text"])
            + _cite(para["discovery_ids"], bib_key_by_did) + "\\par"
        )
    lines.extend(["\\end{claimboundary}", "\\medskip", "\\subsection*{Source-backed Technical Notes}"])
    for note in supplement["technical_notes"]:
        did = note["discovery_id"]
        lines.extend([
            "\\begin{technicalnote}[" + tex_escape(note["title"]) + "]",
            "\\noindent\\textbf{Chronology:} " + tex_escape(note["chronology"])
            + _cite([did], bib_key_by_did) + "\\par",
            "\\smallskip\\noindent\\textbf{Technical points:}\\par",
            "\\begin{itemize}",
        ])
        for point in note["technical_points"]:
            lines.append("\\item " + tex_escape(point) + _cite([did], bib_key_by_did))
        lines.extend([
            "\\end{itemize}",
            "\\noindent\\textbf{Limitation / attribution:} " + tex_escape(note["limitation"]) + "\\par",
            "\\smallskip\\noindent\\textbf{Primary URL:} \\url{" + note["primary_url"] + "}\\par",
            "\\end{technicalnote}", "\\smallskip",
        ])
    return lines


def render_cross_family(cross: dict[str, Any], bib_key_by_did: dict[str, str]) -> list[str]:
    """Render a normal full-width comparison; never rotate the publication page."""
    lines = [
        "\\Needspace{0.30\\textheight}",
        "\\section{" + tex_escape(cross["heading"]) + "}",
        "\\sectionkicker{CROSS-FAMILY SYNTHESIS}",
    ]
    for para in cross["paragraphs"]:
        lines.append(
            "\\noindent " + tex_escape(para["text"])
            + _cite(para["discovery_ids"], bib_key_by_did) + "\\par\\medskip"
        )
    lines.extend([
        "\\begin{themeoverview}[Cross-family comparison]",
        "\\scriptsize",
        "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.12\\linewidth}XXXX@{}}",
        "\\toprule", "観点 & GLM & Qwen & DeepSeek & Kimi \\\\ ", "\\midrule",
    ])
    for row in cross["comparison_rows"]:
        lines.append(
            tex_escape(row["dimension"]) + " & " + tex_escape(row["glm"]) + " & "
            + tex_escape(row["qwen"]) + " & " + tex_escape(row["deepseek"]) + " & "
            + tex_escape(row["kimi"]) + _cite(row["discovery_ids"], bib_key_by_did) + " \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{themeoverview}"])
    return lines


def preflight_tex(tex: str, bibliography: str, package_count: int) -> dict[str, Any]:
    result = _base.preflight_tex(tex, bibliography, package_count)
    findings = list(result.get("findings", []))
    joined = tex + "\n" + bibliography
    for pattern in ("Evidence pass", "本Evidence"):
        if pattern.lower() in joined.lower():
            findings.append(f"production review wording leaked into reader-facing source: {pattern}")
    if "\\begin{sidewaysfigure}" in tex or "\\begin{sidewaystable}" in tex:
        findings.append("rotated cross-family float detected; LONGFORM_SPECIAL synthesis must remain normal full-width")
    result["findings"] = list(dict.fromkeys(findings))
    result["status"] = "PASS" if not result["findings"] else "FAIL"
    result["wideflow_count"] = tex.count("\\begin{wideflow}") + tex.count("\\begin{themeoverview}")
    return result
