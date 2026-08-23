#!/usr/bin/env python3
"""Assemble a Core v2 WEEKLY_MAGAZINE DRAFT_COMPLETE issue into exact publication source.

This renderer consumes only accepted Core v2 authorities: approved Architecture,
accepted Draft Package/Result bytes, Profile Synthesis, Evidence acceptance,
Candidate Matrix, Materiality Ledger, accepted Discovery, and a compact reviewed
semantic publication input. It does not advance Production State or approve the
Publication Preview Human Gate.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
from scripts.render_article_draft_tex import tex_escape


STYLE_PATH = Path("templates/survey/jgaisurvey.sty")


def _load(path: Path) -> dict[str, Any]:
    return core.load_json(path)


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


def _safe(root: Path, raw: str, label: str) -> Path:
    path = (root / raw).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"{label} escapes repository: {raw}") from exc
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"{label} missing or unsafe: {raw}")
    return path


def _find_sha(root: Path, expected_sha: str, name: str) -> Path:
    matches: list[Path] = []
    for path in root.rglob(name):
        if path.is_file() and not path.is_symlink() and core.sha256_file(path) == expected_sha:
            matches.append(path)
    if len(matches) != 1:
        raise ValueError(f"{name} SHA must resolve exactly once: {expected_sha} -> {matches}")
    return matches[0]


def _write_json(path: Path, value: Any) -> None:
    if path.exists():
        raise ValueError(f"refusing to overwrite publication artifact: {path}")
    core.write_json(path, value)


def _bib_text(key: str, record: dict[str, Any], urldate: str) -> str:
    entity = record["entity"]
    title = str(entity["canonical_name"]).replace("{", "\\{").replace("}", "\\}")
    org = str(entity.get("organization") or "Unknown").replace("{", "\\{").replace("}", "\\}")
    url = str(entity["canonical_url"])
    status = str(record.get("status") or "UNKNOWN")
    materiality = str(record.get("materiality") or "UNKNOWN")
    return (
        f"@online{{{key},\n"
        f"  title = {{{{{title}}}}},\n"
        f"  author = {{{{{org}}}}},\n"
        f"  url = {{{url}}},\n"
        f"  urldate = {{{urldate}}},\n"
        f"  note = {{Core v2 Evidence: {status}; materiality: {materiality}}}\n"
        "}"
    )


def _cite(keys: list[str]) -> str:
    if not keys:
        return ""
    return " \\cite{" + ",".join(keys) + "}"


def _window(profile: dict[str, Any]) -> tuple[str, str, str]:
    temporal = profile.get("research_scope", {}).get("temporal_policy", {})
    if temporal.get("mode") != "ROLLING_WINDOW":
        raise ValueError("WEEKLY_MAGAZINE semantic publication requires ROLLING_WINDOW temporal policy")
    start = temporal.get("window_start")
    end = temporal.get("window_end")
    cutoff = temporal.get("cutoff")
    timezone = temporal.get("timezone")
    if not all(isinstance(x, str) and x.strip() for x in (start, end, cutoff, timezone)):
        raise ValueError("Weekly temporal policy requires window_start/window_end/cutoff/timezone")
    if end != cutoff:
        raise ValueError("Weekly semantic publication requires window_end == cutoff")
    display_date = end[:10]
    start_display = start[:16].replace("T", " ")
    end_display = end[:16].replace("T", " ")
    boundary = f"Window: {start_display} - {end_display} {timezone}"
    return display_date, boundary, display_date


def _closing_summary(architecture: dict[str, Any]) -> tuple[str, str]:
    closing = architecture.get("publication_extensions", {}).get("closing_summary")
    if not isinstance(closing, dict) or closing.get("required") is not True:
        raise ValueError("Weekly Architecture requires publication_extensions.closing_summary")
    heading = closing.get("heading")
    placement = closing.get("placement")
    if not isinstance(heading, str) or not heading.strip():
        raise ValueError("Weekly Architecture closing summary heading is required")
    if placement != "after_body_before_references":
        raise ValueError("Weekly Architecture closing summary placement must be after_body_before_references")
    weekly = architecture.get("profile_extensions", {}).get("weekly_closing_summary")
    if not isinstance(weekly, dict) or weekly.get("required") is not True:
        raise ValueError("Weekly Architecture requires profile_extensions.weekly_closing_summary")
    if weekly.get("source") != "profile_synthesis.current_interpretation":
        raise ValueError("Weekly closing summary must be sourced from profile_synthesis.current_interpretation")
    return heading, placement


def _validate_input(data: dict[str, Any], issue_id: str, expected_heading: str) -> None:
    expected = {"schema_version", "issue_id", "runner", "cover", "frontmatter", "final_summary"}
    if set(data) != expected or data.get("schema_version") != "2.0-rc1" or data.get("issue_id") != issue_id:
        raise ValueError("semantic publication input envelope invalid")
    if data.get("runner") != "WEEKLY_MAGAZINE":
        raise ValueError("Weekly semantic publication input runner must be WEEKLY_MAGAZINE")
    cover = data["cover"]
    if set(cover) != {"headline", "deck", "anchors"}:
        raise ValueError("publication cover fields invalid")
    if not all(isinstance(cover.get(k), str) and cover[k].strip() for k in ("headline", "deck")):
        raise ValueError("publication cover invalid")
    if not isinstance(cover["anchors"], list) or not cover["anchors"] or not all(
        isinstance(x, str) and x.strip() for x in cover["anchors"]
    ):
        raise ValueError("publication cover anchors invalid")
    front = data["frontmatter"]
    if set(front) != {"heading", "lede", "scope_notes"}:
        raise ValueError("publication frontmatter fields invalid")
    if not all(isinstance(front.get(k), str) and front[k].strip() for k in ("heading", "lede")):
        raise ValueError("publication frontmatter invalid")
    if not isinstance(front["scope_notes"], list) or not front["scope_notes"] or not all(
        isinstance(x, str) and x.strip() for x in front["scope_notes"]
    ):
        raise ValueError("publication scope notes invalid")
    summary = data["final_summary"]
    if set(summary) != {"heading", "paragraphs"} or summary.get("heading") != expected_heading:
        raise ValueError("Weekly final issue summary heading differs from approved Architecture")
    if not isinstance(summary["paragraphs"], list) or len(summary["paragraphs"]) < 3 or not all(
        isinstance(x, str) and x.strip() for x in summary["paragraphs"]
    ):
        raise ValueError("Weekly final issue summary must contain at least three substantive paragraphs")


def _section_label(plan: dict[str, Any]) -> str:
    label = plan.get("publication_extensions", {}).get("section_label")
    if not isinstance(label, str) or not label.strip():
        raise ValueError(f"Weekly package missing publication section_label: {plan.get('package_id')}")
    return label.strip()


def _records_from_authorities(
    source_root: Path,
    evidence_acceptance_sha: str,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, str]]]:
    acceptance_path = _find_sha(source_root / "evidence", evidence_acceptance_sha, "evidence-accepted.json")
    acceptance = _load(acceptance_path)
    accepted_status: dict[str, str] = {}
    for result in acceptance.get("results", []):
        status = result.get("status")
        if not isinstance(status, str) or not status:
            raise ValueError("Evidence acceptance result status missing")
        for did in result.get("discovery_ids", []):
            if did in accepted_status:
                raise ValueError(f"Discovery ID appears more than once in Evidence acceptance: {did}")
            accepted_status[did] = status

    matrix_path = source_root / "candidate-matrix-v2.json"
    matrix = _load(matrix_path)
    if matrix.get("basis", {}).get("evidence_acceptance_sha256") != evidence_acceptance_sha:
        raise ValueError("Candidate Matrix does not bind Draft Evidence acceptance authority")

    ledger_path = source_root / "materiality-ledger-v2.json"
    ledger = _load(ledger_path)
    expected_ledger_sha = matrix.get("basis", {}).get("materiality_ledger_sha256")
    if expected_ledger_sha != core.sha256_file(ledger_path):
        raise ValueError("Candidate Matrix materiality authority drifted")
    materiality: dict[str, str] = {}
    for row in ledger.get("rows", []):
        did = row.get("discovery_id")
        disposition = row.get("downstream_disposition")
        if not isinstance(did, str) or not isinstance(disposition, str):
            raise ValueError("Materiality Ledger row invalid")
        if did in materiality:
            raise ValueError(f"Materiality Ledger duplicates Discovery ID: {did}")
        materiality[did] = disposition

    discovery_path = source_root / "discovery" / "discovery-accepted-v2.json"
    discovery = _load(discovery_path)
    discovery_rows: dict[str, dict[str, Any]] = {}
    for row in discovery.get("records", []):
        did = row.get("discovery_id")
        if not isinstance(did, str) or not did:
            raise ValueError("accepted Discovery row lacks discovery_id")
        if did in discovery_rows:
            raise ValueError(f"accepted Discovery duplicates Discovery ID: {did}")
        discovery_rows[did] = row

    records: dict[str, dict[str, Any]] = {}
    for row in matrix.get("rows", []):
        title = row.get("title")
        matrix_status = row.get("evidence_status")
        matrix_materiality = row.get("materiality")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Candidate Matrix row lacks title: {row.get('candidate_id')}")
        if not isinstance(matrix_status, str) or not isinstance(matrix_materiality, str):
            raise ValueError(f"Candidate Matrix authority fields invalid: {row.get('candidate_id')}")
        for did in row.get("discovery_ids", []):
            if did in records:
                raise ValueError(f"Candidate Matrix duplicates Discovery ID: {did}")
            if accepted_status.get(did) != matrix_status:
                raise ValueError(f"Evidence status authority mismatch for {did}")
            if materiality.get(did) != matrix_materiality:
                raise ValueError(f"Materiality authority mismatch for {did}")
            discovery_row = discovery_rows.get(did)
            if discovery_row is None:
                raise ValueError(f"Candidate Matrix Discovery ID missing from accepted Discovery: {did}")
            locator = discovery_row.get("source_locator")
            if not isinstance(locator, str) or not locator.strip():
                raise ValueError(f"accepted Discovery lacks source locator: {did}")
            records[did] = {
                "entity": {
                    "canonical_name": title.strip(),
                    "canonical_url": locator.strip(),
                    "organization": None,
                },
                "status": matrix_status,
                "materiality": matrix_materiality,
            }

    authority = {
        "evidence_acceptance": {"path": str(acceptance_path), "sha256": core.sha256_file(acceptance_path)},
        "candidate_matrix": {"path": str(matrix_path), "sha256": core.sha256_file(matrix_path)},
        "materiality_ledger": {"path": str(ledger_path), "sha256": core.sha256_file(ledger_path)},
        "discovery_acceptance": {"path": str(discovery_path), "sha256": core.sha256_file(discovery_path)},
    }
    return records, authority


def _render_tex(
    issue_id: str,
    display_date: str,
    boundary: str,
    publication: dict[str, Any],
    ordered: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]],
    bib_key_by_did: dict[str, str],
) -> str:
    cover = publication["cover"]
    front = publication["frontmatter"]
    summary = publication["final_summary"]
    lines = [
        "% Generated from Core v2 validated Draft bytes. Do not hand-edit.",
        "\\documentclass[lualatex,a4paper,10pt]{jlreq}",
        "\\usepackage{jgaisurvey}",
        "\\addbibresource{references.bib}",
        "",
        f"\\surveysetup{{{tex_escape(issue_id)}}}{{Japanese Generative AI Technical Survey}}{{{tex_escape(display_date)}}}{{{tex_escape(boundary)}}}",
        f"\\surveycoverstory{{{tex_escape(cover['headline'])}}}{{{tex_escape(cover['deck'])}}}{{{tex_escape(' / '.join(cover['anchors']))}}}",
        "",
        "\\begin{document}",
        "\\surveycover",
        "\\clearpage",
        f"\\section*{{{tex_escape(front['heading'])}}}",
        tex_escape(front["lede"]),
        "",
        "\\begin{claimboundary}[Evidence / scope boundary]",
    ]
    for note in front["scope_notes"]:
        lines.append("\\noindent " + tex_escape(note) + "\\par")
    lines.extend(["\\end{claimboundary}", "\\clearpage", "\\twocolumn"])

    for plan, spec, package, result in ordered:
        del package
        pid = result["package_id"]
        lines.extend([
            f"% package:{pid} draft-result-sha256:{core.sha256_object(result)}",
            f"\\section{{{tex_escape(result['headline'])}}}",
            f"\\label{{pkg:{tex_escape(pid)}}}",
            f"\\sectionkicker{{{tex_escape(_section_label(plan))}}}",
        ])
        deck_keys = [bib_key_by_did[did] for did in spec["deck_discovery_ids"]]
        lines.append("\\noindent\\textbf{" + tex_escape(result["deck"]) + "}" + _cite(deck_keys) + "\\par\\medskip")
        spec_blocks = {row["block_id"]: row for row in spec["blocks"]}
        for block in result["blocks"]:
            bid = block["block_id"]
            text = tex_escape(block["text"])
            if block["block_type"] == "CLAIM_BOUNDARY":
                lines.extend(["\\begin{claimboundary}[Claim boundary]", text, "\\end{claimboundary}"])
                continue
            source_spec = spec_blocks.get(bid)
            if source_spec is None:
                raise ValueError(f"non-boundary Draft block missing semantic source: {pid}/{bid}")
            keys = [bib_key_by_did[did] for did in source_spec.get("discovery_ids", [])]
            lines.extend([
                f"% block:{bid} attribution:{block['attribution_mode']}",
                "\\noindent " + text + _cite(keys) + "\\par\\medskip",
            ])

    lines.extend([
        "\\clearpage",
        "\\onecolumn",
        f"\\section{{{tex_escape(summary['heading'])}}}",
        "\\label{sec:issue-summary}",
        "\\sectionkicker{WEEKLY SYNTHESIS}",
    ])
    for paragraph in summary["paragraphs"]:
        lines.extend(["\\noindent " + tex_escape(paragraph) + "\\par\\medskip"])
    lines.extend([
        "\\clearpage",
        "\\onecolumn",
        "\\printbibliography[title={References / Source Notes}]",
        "\\end{document}",
        "",
    ])
    return "\n".join(lines)


def _identifier_tokens(issue_id: str, records: dict[str, dict[str, Any]], cited: list[str]) -> list[str]:
    tokens = [issue_id]
    for did in cited:
        row = records[did]
        if row.get("materiality") != "MATERIAL":
            continue
        name = str((row.get("entity") or {}).get("canonical_name") or "").strip()
        if name and name not in tokens:
            tokens.append(name)
        if len(tokens) >= 8:
            break
    return tokens


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--state", required=True)
    ap.add_argument("--input", required=True)
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    state_path = _safe(root, args.state, "Production State")
    input_path = _safe(root, args.input, "semantic publication input")
    state = _load(state_path)
    if state.get("lifecycle_state") != "DRAFT_COMPLETE" or state.get("next_action") != "stage:semantic-publication-validation":
        raise SystemExit("semantic publication requires DRAFT_COMPLETE State")

    issue_id = state["issue_id"]
    profile_path = _safe(root, state["profile"]["path"], "Production Profile")
    profile = _load(profile_path)
    if profile.get("research_profile") != "WEEKLY" or profile.get("publication_profile") != "WEEKLY_MAGAZINE":
        raise SystemExit("this renderer requires WEEKLY / WEEKLY_MAGAZINE")

    source_root = (root / profile["paths"]["source_root"]).resolve()
    survey_root = (root / profile["paths"]["survey_root"]).resolve()
    source_root.relative_to(root)
    survey_root.relative_to(root)

    architecture_path = source_root / "architecture-v2.json"
    architecture = _load(architecture_path)
    if architecture.get("issue_id") != issue_id or architecture.get("publication_profile") != "WEEKLY_MAGAZINE":
        raise SystemExit("Weekly Architecture identity mismatch")
    expected_heading, summary_placement = _closing_summary(architecture)

    data = _load(input_path)
    _validate_input(data, issue_id, expected_heading)

    synthesis_input_path = source_root / "draft/v2/profile-synthesis-input.json"
    synthesis_result_path = source_root / "draft/v2/profile-synthesis-result.json"
    synthesis_result = _load(synthesis_result_path)
    syn_errors = drafting.validate_synthesis_result(synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT)
    if syn_errors:
        raise SystemExit("upstream Profile Synthesis invalid: " + "; ".join(syn_errors))

    profile_payload = synthesis_result.get("profile_payload")
    current_interpretation = profile_payload.get("current_interpretation") if isinstance(profile_payload, dict) else None
    if not isinstance(current_interpretation, str) or not current_interpretation.strip():
        raise SystemExit("Weekly Profile Synthesis lacks profile_payload.current_interpretation required by Architecture")
    if current_interpretation not in data["final_summary"]["paragraphs"]:
        raise SystemExit("Weekly final summary must preserve exact profile_synthesis.current_interpretation as an approved source paragraph")

    semantic_archive = _load(source_root / "draft/v2/interactive-drafting-synthesis-input.json")
    spec_by_id = {row["package_id"]: row for row in semantic_archive["packages"]}

    ordered: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]] = []
    evidence_acceptance_sha: str | None = None
    for plan in sorted(architecture["packages"], key=lambda r: (r["drafting_order"], r["package_id"])):
        pid = plan["package_id"]
        _section_label(plan)
        package_path = source_root / "draft/v2/packages" / pid / "draft-package.json"
        result_path = source_root / "draft/v2/packages" / pid / "draft-result.json"
        package = _load(package_path)
        result = _load(result_path)
        errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
        if errors:
            raise SystemExit(f"upstream Draft Result invalid for {pid}: " + "; ".join(errors))
        spec = spec_by_id.get(pid)
        if spec is None or result["headline"] != spec["headline"] or result["deck"] != spec["deck"]:
            raise SystemExit(f"Draft semantic archive drift for {pid}")
        result_blocks = {b["block_id"]: b for b in result["blocks"] if b["block_type"] != "CLAIM_BOUNDARY"}
        for block_spec in spec["blocks"]:
            block = result_blocks.get(block_spec["block_id"])
            if block is None or block["text"] != block_spec["text"]:
                raise SystemExit(f"Draft block semantic archive drift for {pid}/{block_spec['block_id']}")
        current_ea = package["basis"]["evidence_acceptance_sha256"]
        if evidence_acceptance_sha is None:
            evidence_acceptance_sha = current_ea
        elif evidence_acceptance_sha != current_ea:
            raise SystemExit("Draft packages disagree on Evidence acceptance authority")
        ordered.append((plan, spec, package, result))

    if evidence_acceptance_sha is None:
        raise SystemExit("Weekly Architecture contains no draftable packages")
    records, authority = _records_from_authorities(source_root, evidence_acceptance_sha)

    cited: list[str] = []
    for _, spec, _, _ in ordered:
        cited.extend(spec["deck_discovery_ids"])
        for block in spec["blocks"]:
            cited.extend(block.get("discovery_ids", []))
    cited = list(dict.fromkeys(cited))
    for did in cited:
        row = records.get(did)
        if row is None:
            raise SystemExit(f"cited Discovery ID missing from accepted Core authorities: {did}")
        if row.get("materiality") == "HOLD" or row.get("status") == "NEEDS_MORE":
            raise SystemExit(f"publication cannot cite HOLD/NEEDS_MORE Evidence as factual support: {did}")
        entity = row.get("entity") or {}
        if not entity.get("canonical_name") or not entity.get("canonical_url"):
            raise SystemExit(f"cited authority lacks canonical bibliography metadata: {did}")

    survey_root.mkdir(parents=True, exist_ok=True)
    publication_root = source_root / "publication/v2"
    publication_root.mkdir(parents=True, exist_ok=True)
    quality_root = publication_root / "quality"
    quality_root.mkdir(parents=True, exist_ok=True)
    for path in (
        survey_root / "main.tex",
        survey_root / "references.bib",
        survey_root / "jgaisurvey.sty",
        publication_root / "validated-source-manifest.json",
    ):
        if path.exists():
            raise SystemExit(f"refusing existing semantic publication artifact: {path}")

    style_source = root / STYLE_PATH
    shutil.copyfile(style_source, survey_root / "jgaisurvey.sty")

    display_date, boundary, urldate = _window(profile)
    bib_key_by_did = {
        did: "w" + issue_id.lower().replace("-", "").replace(".", "") + did.lower().replace("-", "")
        for did in cited
    }
    bib = "\n\n".join(_bib_text(bib_key_by_did[did], records[did], urldate) for did in cited) + "\n"
    (survey_root / "references.bib").write_text(bib, encoding="utf-8")
    tex = _render_tex(issue_id, display_date, boundary, data, ordered, bib_key_by_did)
    (survey_root / "main.tex").write_text(tex, encoding="utf-8")

    archived_input = publication_root / "interactive-semantic-publication-input.json"
    _write_json(archived_input, data)

    draft_refs = []
    for _, _, _, result in ordered:
        path = source_root / "draft/v2/packages" / result["package_id"] / "draft-result.json"
        draft_refs.append({"package_id": result["package_id"], "path": _rel(root, path), "sha256": core.sha256_file(path)})

    evidence_binding = {
        key: {"path": _rel(root, Path(value["path"])), "sha256": value["sha256"]}
        for key, value in authority.items()
    }
    manifest = {
        "schema_version": "2.0-rc1",
        "issue_id": issue_id,
        "status": "ESTABLISHED",
        "production_profile": {"path": _rel(root, profile_path), "sha256": core.sha256_file(profile_path)},
        "production_state_basis": {
            "path": _rel(root, state_path),
            "sha256": core.sha256_file(state_path),
            "lifecycle_state": "DRAFT_COMPLETE",
        },
        "publication_semantic_input": {"path": _rel(root, archived_input), "sha256": core.sha256_file(archived_input)},
        "architecture_closing_summary": {
            "path": _rel(root, architecture_path),
            "sha256": core.sha256_file(architecture_path),
            "heading": expected_heading,
            "placement": summary_placement,
            "source": "profile_synthesis.current_interpretation",
        },
        "profile_synthesis": {
            "input": {"path": _rel(root, synthesis_input_path), "sha256": core.sha256_file(synthesis_input_path)},
            "result": {"path": _rel(root, synthesis_result_path), "sha256": core.sha256_file(synthesis_result_path)},
        },
        "evidence_binding": evidence_binding,
        "draft_results": draft_refs,
        "rendered_source": {"path": _rel(root, survey_root / "main.tex"), "sha256": core.sha256_file(survey_root / "main.tex")},
        "bibliography": {
            "path": _rel(root, survey_root / "references.bib"),
            "sha256": core.sha256_file(survey_root / "references.bib"),
            "cited_discovery_ids": cited,
        },
        "style": {
            "source_path": str(STYLE_PATH),
            "source_sha256": core.sha256_file(style_source),
            "copied_path": _rel(root, survey_root / "jgaisurvey.sty"),
            "copied_sha256": core.sha256_file(survey_root / "jgaisurvey.sty"),
        },
        "final_summary": {
            "heading": data["final_summary"]["heading"],
            "placement": "after_body_before_references",
            "paragraph_count": len(data["final_summary"]["paragraphs"]),
        },
    }
    _write_json(publication_root / "validated-source-manifest.json", manifest)

    subject_result = {
        "schema_version": "2.0-rc1",
        "check_id": "SUBJECT_ENTITY_PROPERTY_BINDING",
        "status": "PASS",
        "issue_id": issue_id,
        "cited_discovery_count": len(cited),
        "bindings": [
            {
                "discovery_id": did,
                "canonical_name": records[did]["entity"]["canonical_name"],
                "canonical_url": records[did]["entity"]["canonical_url"],
                "materiality": records[did]["materiality"],
                "status": records[did]["status"],
            }
            for did in cited
        ],
    }
    _write_json(quality_root / "subject-entity-property-binding.json", subject_result)

    print(json.dumps({
        "issue_id": issue_id,
        "source_root": _rel(root, source_root),
        "survey_root": _rel(root, survey_root),
        "source_manifest": _rel(root, publication_root / "validated-source-manifest.json"),
        "main_tex": _rel(root, survey_root / "main.tex"),
        "bibliography": _rel(root, survey_root / "references.bib"),
        "style": _rel(root, survey_root / "jgaisurvey.sty"),
        "subject_result": _rel(root, quality_root / "subject-entity-property-binding.json"),
        "identifier_tokens": _identifier_tokens(issue_id, records, cited),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
