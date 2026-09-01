#!/usr/bin/env python3
"""Finalize a DRAFT_COMPLETE Special into validated issue source.

This stage is deterministic except for the already-reviewed interactive synthesis
body supplied by the caller. It does not browse or reopen Evidence. It:

- revalidates the approved Architecture and all accepted Article Draft Results;
- builds a post-draft synthesis input from those exact article bytes;
- binds the reviewed synthesis body to exact input/prompt hashes and validates it;
- checks article chronology against the Special coverage window;
- rejects reader-facing internal workflow jargon;
- renders Special frontmatter, article TeX, and a deduplicated bibliography;
- advances only claim_and_chronology_validation to passed / VALIDATED_DRAFT.

PDF build, Visual Review, Freeze, merge, and public Release remain later gates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from scripts import validate_article_draft as article_validator
from scripts import validate_issue_architecture as architecture_validator
from scripts import validate_issue_synthesis as synthesis_validator
from scripts.render_article_draft_tex import tex_escape

ARTICLE_TYPES = {
    "LEAD", "FEATURE", "COMPARISON", "SECTION", "DEEP_DIVE", "PAPER_WATCH",
    "X_COMMUNITY", "LATE_BREAKING", "WATCHLIST_CHRONOLOGY",
}
INTERNAL_READER_TERMS = (
    "Candidate Inventory", "Reaction Pass", "primary verification",
    "PENDING_APPROVAL", "EVIDENCE_REVIEWED", "SELECTION_COMPLETE",
    "ARCHITECTURE_ESTABLISHED", "DRAFT_COMPLETE",
)
ENTRY_START_RE = re.compile(r"(?m)^@")
ENTRY_KEY_RE = re.compile(r"^@[A-Za-z]+\{([^,]+),")


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


def parse_instant(value: str) -> datetime:
    text = value.strip()
    if len(text) == 10:
        return datetime.fromisoformat(text).replace(tzinfo=timezone.utc)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def event_timing_relation(value: str, start: datetime, cutoff: datetime) -> str:
    text = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}", text):
        year, month = (int(part) for part in text.split("-"))
        first = datetime(year, month, 1, tzinfo=timezone.utc).date()
        if month == 12:
            next_month = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
        else:
            next_month = datetime(year, month + 1, 1, tzinfo=timezone.utc)
        last = (next_month - timedelta(days=1)).date()
        if first >= start.date() and last <= cutoff.date():
            return "MAIN_EVENT"
        if last < start.date():
            return "PRE_WINDOW"
        if first > cutoff.date():
            return "POST_CUTOFF"
        return "TIMING_UNRESOLVED"
    instant = parse_instant(text)
    if start <= instant <= cutoff:
        return "MAIN_EVENT"
    return "PRE_WINDOW" if instant < start else "POST_CUTOFF"


def body_text(article: dict[str, Any]) -> str:
    parts = [str(article.get("headline") or ""), str(article.get("deck") or "")]
    for block in article.get("blocks") or []:
        if isinstance(block, dict):
            parts.append(str(block.get("text") or ""))
    return "\n".join(parts)


def evidence_records(package: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for key in ("primary_evidence", "supporting_evidence"):
        values = package.get(key) or []
        if not isinstance(values, list):
            raise ValueError(f"Draft Package {package.get('package_id')}: {key} must be an array")
        for value in values:
            if not isinstance(value, dict):
                raise ValueError(f"Draft Package {package.get('package_id')}: invalid {key} record")
            records.append(value)
    return records


def validate_and_collect_articles(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    package_dir: Path,
    article_run_dir: Path,
    article_prompt_path: Path,
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    report, passed = architecture_validator.validate(
        architecture_input_path, architecture_plan_path, require_approved=True
    )
    if not passed:
        raise ValueError(f"Architecture is not finalization-ready: {report['errors']}")

    plan = load_json(architecture_plan_path)
    acceptance = load_json(article_run_dir / "acceptance.json")
    if acceptance.get("status") != "ACCEPTED" or acceptance.get("issue_id") != plan.get("issue_id"):
        raise ValueError("Article Draft acceptance does not match approved Architecture")

    result_by_id = {row["package_id"]: row for row in acceptance.get("results") or []}
    articles: list[dict[str, Any]] = []
    validations: list[dict[str, Any]] = []
    errors: list[str] = []

    packages = [p for p in plan["packages"] if p["package_type"] in ARTICLE_TYPES]
    packages.sort(key=lambda p: p["drafting_order"])
    expected_ids = [p["package_id"] for p in packages]
    if set(result_by_id) != set(expected_ids):
        raise ValueError(
            f"accepted Article Draft set differs from Architecture: expected={expected_ids}, actual={sorted(result_by_id)}"
        )

    cover_anchor_candidates = set(plan.get("cover", {}).get("anchor_candidates") or [])
    unknown_cover_anchors = sorted(cover_anchor_candidates - set(expected_ids))
    if unknown_cover_anchors:
        raise ValueError(f"Architecture cover anchors reference unknown article packages: {unknown_cover_anchors}")
    cover_package_ids = [package_id for package_id in expected_ids if package_id in cover_anchor_candidates]

    for package_plan in packages:
        package_id = package_plan["package_id"]
        row = result_by_id[package_id]
        package_path = package_dir / f"{package_id}.json"
        draft_path = article_run_dir / row["draft_path"]
        if sha256_file(draft_path) != row["draft_sha256"]:
            raise ValueError(f"accepted draft digest mismatch: {package_id}")
        validation, ok = article_validator.validate(package_path, draft_path, article_prompt_path)
        validations.append({"package_id": package_id, **validation})
        if not ok:
            errors.extend(f"{package_id}: {item}" for item in validation["errors"])
            continue
        draft = load_json(draft_path)
        package = load_json(package_path)
        reader_text = body_text(draft)
        for term in INTERNAL_READER_TERMS:
            if term.casefold() in reader_text.casefold():
                errors.append(f"{package_id}: reader-facing internal workflow term remains: {term}")
        articles.append(
            {
                "package_id": package_id,
                "package_type": package_plan["package_type"],
                "drafting_order": package_plan["drafting_order"],
                "page_target": package_plan["page_target"],
                "late_breaking": package_plan["late_breaking"],
                "editorial_angle": package_plan["editorial_angle"],
                "boundaries": package_plan.get("boundaries") or [],
                "headline": draft["headline"],
                "deck": draft["deck"],
                "blocks": [
                    {
                        "block_id": block["block_id"],
                        "block_type": block["block_type"],
                        "text": block["text"],
                        "attribution_mode": block["attribution_mode"],
                    }
                    for block in draft["blocks"]
                ],
                "draft_sha256": sha256_file(draft_path),
                "draft_path": row["draft_path"],
                "tex_path": row["tex_path"],
                "tex_sha256": row["tex_sha256"],
                "bib_path": row["bib_path"],
                "bib_sha256": row["bib_sha256"],
            }
        )

    if errors:
        raise ValueError(f"Article finalization validation failed: {errors}")
    if not cover_package_ids:
        raise ValueError("Architecture cover anchors do not map to any article package")
    return plan, articles, validations, cover_package_ids


def build_synthesis_input(
    issue_id: str,
    plan: dict[str, Any],
    articles: list[dict[str, Any]],
    cover_package_ids: list[str],
    architecture_input_path: Path,
    architecture_plan_path: Path,
    article_prompt_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    value = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "post-draft-synthesis-input-ready",
        "basis": {
            "architecture_input_sha256": sha256_file(architecture_input_path),
            "architecture_plan_sha256": sha256_file(architecture_plan_path),
            "article_prompt_sha256": sha256_file(article_prompt_path),
            "article_drafts": [
                {"package_id": a["package_id"], "article_draft_sha256": a["draft_sha256"]}
                for a in articles
            ],
        },
        "editorial_thesis": plan["editorial_thesis"],
        "cover_anchor_candidates": cover_package_ids,
        "articles": [
            {key: article[key] for key in (
                "package_id", "package_type", "drafting_order", "page_target", "late_breaking",
                "editorial_angle", "boundaries", "headline", "deck", "blocks",
            )}
            for article in articles
        ],
        "constraints": {
            "language": "ja",
            "max_this_week_signals": 5,
            "no_new_external_facts": True,
            "summarize_only_validated_article_text": True,
            "late_breaking_boundary_required": True,
            "page_references_must_use_package_ids": True,
        },
    }
    write_json(output_path, value)
    return value


def bind_synthesis_body(
    body_path: Path,
    input_path: Path,
    prompt_path: Path,
    generated_at: str,
    run_reference: str,
    output_path: Path,
) -> dict[str, Any]:
    body = load_json(body_path)
    result = {
        "schema_version": body.get("schema_version"),
        "issue_id": body.get("issue_id"),
        "synthesis_version": body.get("synthesis_version"),
        "status": body.get("status"),
        "basis": {
            "synthesis_input_sha256": sha256_file(input_path),
            "prompt_id": "issue-synthesis-v0.1",
            "prompt_sha256": sha256_file(prompt_path),
        },
        "runner": {
            "provider": "OpenAI",
            "model": "GPT-5.6 Sol",
            "invocation": "interactive ChatGPT post-draft synthesis; no paid inference-provider API",
            "generated_at": generated_at,
            "run_reference": run_reference,
        },
        "cover": body.get("cover"),
        "this_week_signals": body.get("this_week_signals"),
    }
    write_json(output_path, result)
    return result


def split_bib_entries(text: str) -> list[str]:
    starts = [match.start() for match in ENTRY_START_RE.finditer(text)]
    if not starts:
        return []
    starts.append(len(text))
    return [text[starts[i]:starts[i + 1]].strip() for i in range(len(starts) - 1)]


def merge_bibliography(article_run_dir: Path, articles: list[dict[str, Any]], output_path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for article in articles:
        bib_path = article_run_dir / article["bib_path"]
        if sha256_file(bib_path) != article["bib_sha256"]:
            raise ValueError(f"rendered bibliography digest mismatch: {article['package_id']}")
        for entry in split_bib_entries(bib_path.read_text(encoding="utf-8")):
            match = ENTRY_KEY_RE.match(entry)
            if not match:
                raise ValueError(f"cannot parse generated BibLaTeX entry in {bib_path}: {entry[:80]!r}")
            key = match.group(1)
            if key in entries and entries[key] != entry:
                raise ValueError(f"conflicting generated bibliography entry for {key}")
            entries[key] = entry
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(entries[key] for key in sorted(entries)) + "\n", encoding="utf-8")
    return entries


def inject_package_label(tex: str, package_id: str) -> str:
    lines = tex.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("\\section{"):
            lines.insert(index + 1, f"\\label{{pkg:{package_id}}}")
            return "\n".join(lines) + "\n"
    raise ValueError(f"rendered article lacks section heading: {package_id}")


def render_frontmatter(result: dict[str, Any], output_path: Path) -> None:
    lines = [
        "% Generated from validated Special post-draft synthesis. Do not hand-edit.",
        "\\section*{Monthly Signals}",
        "\\addcontentsline{toc}{section}{Monthly Signals}",
    ]
    for signal in result["this_week_signals"]:
        refs = " / ".join(f"p.~\\pageref{{pkg:{package_id}}}" for package_id in signal["package_ids"])
        lines.extend([
            "\\smallskip",
            f"\\noindent \\textbf{{{tex_escape(signal['title'])}}} {tex_escape(signal['summary'])} "
            f"\\hfill{{\\footnotesize {refs}}}",
            "\\par",
        ])
    lines.extend([
        "\\medskip",
        "\\begin{claimboundary}[Retrospective scope]",
        "本号は2026年7月を、後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。Coverage Periodと制作時点を同一視せず、vendor / project / author claimの境界は各記事で明示する。",
        "\\end{claimboundary}",
        "\\medskip",
        "\\tableofcontents",
        "",
    ])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def chronology_audit(
    state: dict[str, Any],
    package_dir: Path,
    articles: list[dict[str, Any]],
    validations: list[dict[str, Any]],
    synthesis_validation: dict[str, Any],
) -> dict[str, Any]:
    start = parse_instant(state["calendar"]["collection_window_start"])
    cutoff = parse_instant(state["calendar"]["editorial_cutoff"])
    errors: list[str] = []
    event_rows: list[dict[str, str]] = []
    evidence_task_count = 0
    for article in articles:
        package = load_json(package_dir / f"{article['package_id']}.json")
        seen_tasks: set[str] = set()
        for record in evidence_records(package):
            task_id = record.get("evidence_task_id")
            if isinstance(task_id, str):
                seen_tasks.add(task_id)
            card = record.get("card") or {}
            for event in (card.get("temporal") or {}).get("events") or []:
                raw = event.get("event_date")
                if not isinstance(raw, str) or not raw.strip():
                    continue
                relation = event_timing_relation(raw, start, cutoff)
                event_rows.append({
                    "package_id": article["package_id"],
                    "evidence_task_id": str(task_id),
                    "event_id": str(event.get("event_id") or ""),
                    "event_date": raw,
                    "relation": relation,
                })
                if article["late_breaking"] is not True and relation != "MAIN_EVENT":
                    errors.append(
                        f"{article['package_id']}: non-Late-Breaking Evidence event falls outside coverage: {task_id} {raw} ({relation})"
                    )
        evidence_task_count += len(seen_tasks)
    if any(not item.get("passed") for item in validations):
        errors.append("one or more Article Draft validation reports failed")
    if synthesis_validation.get("passed") is not True:
        errors.append("Issue Synthesis validation failed")
    return {
        "schema_version": "1.0",
        "issue_id": state["issue_id"],
        "passed": not errors,
        "coverage_start": state["calendar"]["collection_window_start"],
        "editorial_cutoff": state["calendar"]["editorial_cutoff"],
        "article_count": len(articles),
        "evidence_task_occurrence_count": evidence_task_count,
        "event_count": len(event_rows),
        "events": sorted(event_rows, key=lambda row: (row["event_date"], row["package_id"], row["evidence_task_id"])),
        "article_validations": validations,
        "synthesis_validation": synthesis_validation,
        "errors": errors,
    }


def build_issue_source(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    state: dict[str, Any],
    result: dict[str, Any],
    article_run_dir: Path,
    articles: list[dict[str, Any]],
    output_dir: Path,
) -> dict[str, Any]:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    sections_dir = output_dir / "sections"
    sections_dir.mkdir(parents=True)
    render_frontmatter(result, sections_dir / "00-frontmatter.tex")

    section_paths: list[str] = []
    source_records: list[dict[str, Any]] = []
    for index, article in enumerate(articles, start=1):
        source_tex = article_run_dir / article["tex_path"]
        if sha256_file(source_tex) != article["tex_sha256"]:
            raise ValueError(f"rendered article digest mismatch: {article['package_id']}")
        target = sections_dir / f"{index * 10:02d}-{article['package_id']}.tex"
        target.write_text(
            inject_package_label(source_tex.read_text(encoding="utf-8"), article["package_id"]),
            encoding="utf-8",
        )
        rel = target.relative_to(output_dir).as_posix()
        section_paths.append(rel)
        source_records.append({
            "package_id": article["package_id"],
            "accepted_tex_path": article["tex_path"],
            "accepted_tex_sha256": article["tex_sha256"],
            "issue_section_path": rel,
            "issue_section_sha256": sha256_file(target),
        })

    references_path = output_dir / "references.bib"
    bib_entries = merge_bibliography(article_run_dir, articles, references_path)

    anchor_headlines = []
    by_id = {article["package_id"]: article for article in articles}
    for package_id in result["cover"]["anchor_package_ids"]:
        anchor_headlines.append(by_id[package_id]["headline"])
    anchors_tex = " \\quad / \\quad ".join(tex_escape(value) for value in anchor_headlines)

    coverage_start = state["calendar"]["collection_window_start"][:10]
    coverage_end = state["calendar"]["collection_window_end"][:10]
    retrospective = state["calendar"]["retrospective_as_of"][:10]
    inputs = "\n".join(f"\\input{{{path[:-4]}}}" for path in section_paths)
    main = f"""\\documentclass[lualatex,a4paper,10pt]{{jlreq}}
\\usepackage{{../../../templates/survey/jgaisurvey}}
\\addbibresource{{references.bib}}

\\surveysetup
  {{{tex_escape(issue_id)}}}
  {{Japanese Generative AI Technical Survey Special}}
  {{Coverage: {coverage_start} -- {coverage_end} / Retrospective as of {retrospective}}}
  {{Coverage window: {coverage_start} -- {coverage_end} UTC}}
\\surveyeditiondescriptor{{Retrospective Technical Survey}}

\\surveycoverstory
  {{{tex_escape(result['cover']['headline'])}}}
  {{{tex_escape(result['cover']['deck'])}}}
  {{{anchors_tex}}}

\\begin{{document}}

\\surveycover
\\clearpage
\\input{{sections/00-frontmatter}}

\\clearpage
\\twocolumn
{inputs}

\\clearpage
\\onecolumn
\\printbibliography[title={{References / Source Notes}}]

\\end{{document}}
"""
    (output_dir / "main.tex").write_text(main, encoding="utf-8")

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "status": "VALIDATED_SOURCE",
        "article_count": len(articles),
        "bibliography_entry_count": len(bib_entries),
        "main_tex": {"path": "main.tex", "sha256": sha256_file(output_dir / "main.tex")},
        "frontmatter": {"path": "sections/00-frontmatter.tex", "sha256": sha256_file(sections_dir / "00-frontmatter.tex")},
        "references": {"path": "references.bib", "sha256": sha256_file(references_path)},
        "articles": source_records,
    }
    write_json(output_dir / "source-manifest.json", manifest)
    return manifest


def finalize(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    article_run_dir: Path,
    synthesis_body_path: Path,
    generated_at: str,
    run_reference: str,
) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "DRAFT_COMPLETE":
        raise ValueError(f"Special finalization requires DRAFT_COMPLETE, got {state.get('lifecycle_state')}")
    if state.get("gates", {}).get("article_draft") != "passed":
        raise ValueError("article_draft gate must be passed")
    if state.get("gates", {}).get("claim_and_chronology_validation") != "pending":
        raise ValueError("claim_and_chronology_validation must be pending")

    architecture_input = repo_root / "sources" / issue_id / "architecture" / "architecture-input-v0.1.json"
    architecture_plan = repo_root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json"
    package_dir = repo_root / "sources" / issue_id / "drafting" / "packages" / "v0.1"
    article_prompt = repo_root / "config" / "prompts" / "editorial" / "article-drafting-v0.1.md"
    synthesis_prompt = repo_root / "config" / "prompts" / "editorial" / "issue-synthesis-v0.1.md"

    plan, articles, article_validations, cover_package_ids = validate_and_collect_articles(
        architecture_input, architecture_plan, package_dir, article_run_dir, article_prompt
    )

    final_dir = repo_root / "sources" / issue_id / "finalization" / "v0.1"
    final_dir.mkdir(parents=True, exist_ok=True)
    synthesis_input_path = final_dir / "synthesis-input.json"
    synthesis_result_path = final_dir / "synthesis-result.json"
    synthesis_validation_path = final_dir / "synthesis-validation.json"
    audit_path = final_dir / "claim-chronology-audit.json"
    build_synthesis_input(
        issue_id, plan, articles, cover_package_ids,
        architecture_input, architecture_plan, article_prompt, synthesis_input_path,
    )
    result = bind_synthesis_body(
        synthesis_body_path, synthesis_input_path, synthesis_prompt,
        generated_at, run_reference, synthesis_result_path,
    )
    synthesis_validation, synthesis_ok = synthesis_validator.validate(
        synthesis_input_path, synthesis_result_path, synthesis_prompt
    )
    write_json(synthesis_validation_path, synthesis_validation)
    if not synthesis_ok:
        raise ValueError(f"Special synthesis validation failed: {synthesis_validation['errors']}")

    audit = chronology_audit(state, package_dir, articles, article_validations, synthesis_validation)
    write_json(audit_path, audit)
    if not audit["passed"]:
        raise ValueError(f"claim/chronology audit failed: {audit['errors']}")

    issue_output = repo_root / "surveys" / "special" / special_slug
    source_manifest = build_issue_source(
        repo_root, special_slug, issue_id, state, result, article_run_dir, articles, issue_output
    )

    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["claim_and_chronology_validation"] = "passed"
    state.setdefault("provenance", {})["issue_synthesis"] = {
        "input_path": synthesis_input_path.relative_to(repo_root).as_posix(),
        "input_sha256": sha256_file(synthesis_input_path),
        "result_path": synthesis_result_path.relative_to(repo_root).as_posix(),
        "result_sha256": sha256_file(synthesis_result_path),
        "validation_sha256": sha256_file(synthesis_validation_path),
        "generated_at": generated_at,
    }
    state["provenance"]["claim_and_chronology_validation"] = {
        "path": audit_path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(audit_path),
    }
    state["provenance"]["validated_issue_source"] = {
        "path": (issue_output / "source-manifest.json").relative_to(repo_root).as_posix(),
        "sha256": sha256_file(issue_output / "source-manifest.json"),
    }
    write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "VALIDATED_DRAFT",
        "article_count": len(articles),
        "synthesis_signal_count": len(result["this_week_signals"]),
        "claim_chronology_audit_sha256": sha256_file(audit_path),
        "source_manifest_sha256": sha256_file(issue_output / "source-manifest.json"),
        "source_manifest": source_manifest,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--article-run-dir", required=True)
    parser.add_argument("--synthesis-body", required=True)
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--run-reference", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    result = finalize(
        root,
        args.special_slug,
        args.issue_id,
        (root / args.article_run_dir).resolve(),
        (root / args.synthesis_body).resolve(),
        args.generated_at,
        args.run_reference,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
