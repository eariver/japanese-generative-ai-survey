#!/usr/bin/env python3
# Validate the reader-facing Special layout contract before PDF publication.
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts.special_layout_text_normalization import (
    first_substantive_line,
    manual_item_marker_findings,
)
from scripts.special_technical_note_entity_binding_check import inspect_entity_binding


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_derived_reader_layer(article: dict[str, Any]) -> bool:
    return (
        article.get("_sparse_architecture_derived") is True
        and article.get("derived_reader_layer") is True
    )


def declared_non_narrative_multicols(manifest: dict[str, Any], main_text: str) -> tuple[int, list[str]]:
    """Count explicitly declared reader layers that may use multicols outside narrative articles.

    Narrative article cardinality remains strict. A later layout-only descendant may declare a
    two-column References body; that block is allowed only when the manifest explicitly records the
    References multicol contract and the source has the full-width heading plus heading=none body.
    A still later log-cleanup descendant may additionally declare local ``\\raggedright`` inside
    that exact References block; the declaration is accepted only when its manifest flag is true.
    """
    errors: list[str] = []
    lr = manifest.get("layout_revision") or {}
    extra = 0
    if lr.get("half_year_reference_multicol_compaction") is True:
        if lr.get("references_columns") != 2:
            errors.append("References multicol revision must declare references_columns=2")
        required = (
            r"\section*{References / Source Notes}",
            r"\addcontentsline{toc}{section}{References / Source Notes}",
        )
        for token in required:
            if token not in main_text:
                errors.append(f"declared References multicol source marker missing: {token}")

        body_lines = [r"\begin{multicols}{2}"]
        if lr.get("half_year_reference_raggedright_compaction") is True:
            if lr.get("references_raggedright") is not True:
                errors.append("References ragged-right revision must declare references_raggedright=true")
            body_lines.extend(
                [
                    "% half-year References ragged-right compaction",
                    r"\raggedright",
                ]
            )
        body_lines.extend([r"\printbibliography[heading=none]", r"\end{multicols}"])
        body = "\n".join(body_lines)
        if body not in main_text:
            errors.append(f"declared References multicol source marker missing: {body}")
        if not errors:
            extra += 1
    return extra, errors


def inspect_layout(
    manifest: dict[str, Any],
    main_text: str,
    architecture: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    articles = [x for x in (manifest.get("articles") or []) if isinstance(x, dict)]
    if not articles:
        return ["validated Special source has no article entries"]
    narrative_articles = [x for x in articles if not is_derived_reader_layer(x)]
    if not narrative_articles:
        return ["validated Special source has no narrative article entries"]

    override = architecture.get("layout_override") or {}
    single_column_approved = (
        architecture.get("status") == "APPROVED"
        and isinstance(override, dict)
        and override.get("narrative_body_mode") == "single-column"
        and bool(str(override.get("approval_reference") or "").strip())
    )
    if single_column_approved:
        return errors

    body_mode = str((manifest.get("layout") or {}).get("body_mode") or "")
    if "single-column" in body_mode.lower():
        errors.append(
            "Special narrative body_mode regressed to single-column without approved override"
        )
    has_local_multicols = r"\begin{multicols}{2}" in main_text
    if "two-column" not in body_mode.lower() or (
        "multicol" not in body_mode.lower() and not has_local_multicols
    ):
        errors.append(
            "Special layout manifest/source does not declare or implement local two-column multicols narrative"
        )
    if r"\twocolumn" in main_text or r"\onecolumn" in main_text:
        errors.append(
            "global twocolumn/onecolumn switch is forbidden for normal Special layout"
        )

    non_narrative_multicols, non_narrative_errors = declared_non_narrative_multicols(manifest, main_text)
    errors.extend(non_narrative_errors)
    begin_count = main_text.count(r"\begin{multicols}{2}")
    end_count = main_text.count(r"\end{multicols}")
    expected_multicols = len(narrative_articles) + non_narrative_multicols
    if begin_count != expected_multicols or end_count != expected_multicols:
        errors.append(
            "expected one balanced two-column narrative block per narrative article plus declared reader blocks: "
            f"narrative_articles={len(narrative_articles)} total_articles={len(articles)} "
            f"declared_non_narrative={non_narrative_multicols} begin={begin_count} end={end_count}"
        )

    front = str(
        (manifest.get("frontmatter") or {}).get("path")
        or "sections/00-frontmatter.tex"
    )
    front_input = r"\input{" + Path(front).with_suffix("").as_posix() + "}"
    first_multicol = main_text.find(r"\begin{multicols}{2}")
    if front_input not in main_text or (
        first_multicol >= 0 and main_text.find(front_input) > first_multicol
    ):
        errors.append("frontmatter must remain full-width before narrative multicols")

    standfirst_inputs: list[str] = []
    for article in narrative_articles:
        if not article.get("layout_standfirst_present"):
            continue
        standfirst = str(article.get("layout_standfirst_path") or "")
        body = str(article.get("layout_body_path") or "")
        if not standfirst:
            errors.append(f"{article.get('package_id')}: standfirst marked present without path")
            continue
        standfirst_input = r"\input{" + Path(standfirst).with_suffix("").as_posix() + "}"
        standfirst_inputs.append(standfirst_input)
        if standfirst_input not in main_text:
            errors.append(f"{article.get('package_id')}: full-width standfirst input missing")
            continue
        if body:
            body_input = r"\input{" + Path(body).with_suffix("").as_posix() + "}"
            if body_input in main_text and main_text.find(standfirst_input) > main_text.find(body_input):
                errors.append(f"{article.get('package_id')}: standfirst must precede narrative body")

    depth = 0
    for line in main_text.splitlines():
        if r"\begin{multicols}{2}" in line:
            depth += 1
        if (
            "technical-notes/" in line
            and r"\input{" in line
            and depth != 0
        ):
            errors.append("Technical Notes input is nested inside narrative multicols")
        if depth != 0 and any(token in line for token in standfirst_inputs):
            errors.append("standfirst input is nested inside narrative multicols")
        if r"\end{multicols}" in line:
            depth -= 1
        if depth < 0:
            errors.append("unbalanced multicols end marker")
            depth = 0
    if depth != 0:
        errors.append("unbalanced multicols environment")
    return errors


def inspect_derived_layout_files(manifest: dict[str, Any], source_dir: Path) -> list[str]:
    errors: list[str] = []
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        package_id = str(article.get("package_id") or "<unknown>")
        standfirst_rel = str(article.get("layout_standfirst_path") or "")
        if article.get("layout_standfirst_present"):
            standfirst_path = source_dir / standfirst_rel
            if not standfirst_rel or not standfirst_path.is_file():
                errors.append(f"{package_id}: declared standfirst file missing")
            else:
                expected = str(article.get("layout_standfirst_sha256") or "")
                if expected and sha(standfirst_path) != expected:
                    errors.append(f"{package_id}: standfirst digest mismatch")
                first = first_substantive_line(standfirst_path.read_text(encoding="utf-8"))
                if not first.startswith(r"\noindent\textbf{"):
                    errors.append(f"{package_id}: full-width standfirst is not the generated bold lead")

        for key in ("layout_body_path", "layout_wide_path"):
            rel = str(article.get(key) or "")
            if not rel:
                continue
            path = source_dir / rel
            if not path.is_file():
                errors.append(f"{package_id}: derived layout file missing: {rel}")
                continue
            text = path.read_text(encoding="utf-8")
            if key == "layout_body_path" and first_substantive_line(text).startswith(r"\noindent\textbf{"):
                errors.append(f"{package_id}: standfirst leaked into two-column narrative body")
            findings = manual_item_marker_findings(text)
            if findings:
                errors.append(
                    f"{package_id}: manual bullet marker remains inside LaTeX item(s): {findings}"
                )
    return errors


def check(repo_root: Path, issue_id: str) -> dict[str, Any]:
    state = load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = repo_root / str(source.get("path") or "")
    if not manifest_path.is_file() or sha(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    manifest = load_json(manifest_path)

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = manifest_path.parent / main_rel
    if not main_path.is_file():
        raise ValueError("state-pinned main.tex missing")

    architecture_path = (
        repo_root
        / "sources"
        / issue_id
        / "architecture"
        / "issue-architecture-v0.1.json"
    )
    architecture = load_json(architecture_path)
    errors = inspect_layout(
        manifest,
        main_path.read_text(encoding="utf-8"),
        architecture,
    )
    errors.extend(inspect_derived_layout_files(manifest, manifest_path.parent))
    errors.extend(inspect_entity_binding(manifest, manifest_path.parent))
    articles = [x for x in (manifest.get("articles") or []) if isinstance(x, dict)]
    derived_layers = [
        str(x.get("package_id") or "<unknown>")
        for x in articles
        if is_derived_reader_layer(x)
    ]
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "article_count": len(articles),
        "narrative_article_count": len(articles) - len(derived_layers),
        "derived_reader_layers": derived_layers,
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--issue-id", required=True)
    args = ap.parse_args()
    report = check(Path(args.repo_root).resolve(), args.issue_id)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
