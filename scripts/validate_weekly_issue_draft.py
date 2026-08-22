#!/usr/bin/env python3
"""Validate a structured W33+ Weekly draft before CI/PDF review.

The validator is deterministic. It checks that Human-approved Selection and
Architecture are in force, that the reader-facing TeX surface matches the
approved structure, that Issue #9 prose rules pass, and that all citation keys
used by the draft exist in the bibliography. On success it may advance the
issue only to DRAFT_COMPLETE; downstream validated states remain idempotently
re-checkable while claim/chronology, LaTeX, visual and freeze gates stay separate.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from editorial_prose_guard import reader_facing_prose_errors

CITE_RE = re.compile(r"\\cite\{([^}]+)\}")
BIB_KEY_RE = re.compile(r"^@[A-Za-z]+\{([^,]+),", re.MULTILINE)
HARD_PAGE_RE = re.compile(r"(?:今号|本号)\s*p\.\s*\d+(?:\s*--\s*\d+)?")
DRAFT_RECHECKABLE_STATES = {"ARCHITECTURE_ESTABLISHED", "DRAFT_COMPLETE", "VALIDATED_DRAFT"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate(repo_root: Path, issue_id: str) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    src = repo_root / "sources" / issue_id
    survey = repo_root / "surveys" / "weekly" / issue_id
    state_path = src / "pipeline-state.json"
    selection_path = src / "selection" / "candidate-selection-v0.1.json"
    arch_approval_path = src / "architecture" / "human-architecture-approval-v0.2.json"
    main_path = survey / "main.tex"
    bib_path = survey / "references.bib"
    sections = survey / "sections"

    required = [state_path, selection_path, arch_approval_path, main_path, bib_path, sections]
    for path in required:
        if not path.exists():
            errors.append(f"required draft input missing: {path.relative_to(repo_root)}")
    if errors:
        return {"schema_version": "1.0", "issue_id": issue_id, "passed": False, "errors": errors, "warnings": warnings}

    state = load_json(state_path)
    selection = load_json(selection_path)
    arch = load_json(arch_approval_path)
    if state.get("lifecycle_state") not in DRAFT_RECHECKABLE_STATES:
        errors.append(f"expected one of {sorted(DRAFT_RECHECKABLE_STATES)}, got {state.get('lifecycle_state')}")
    if state.get("gates", {}).get("candidate_selection") != "passed" or state.get("gates", {}).get("issue_architecture") != "passed":
        errors.append("Candidate Selection and Architecture gates must be passed")
    if state.get("lifecycle_state") in {"DRAFT_COMPLETE", "VALIDATED_DRAFT"} and state.get("gates", {}).get("article_draft") != "passed":
        errors.append("downstream draft state requires article_draft gate passed")
    if state.get("lifecycle_state") == "VALIDATED_DRAFT" and state.get("gates", {}).get("claim_and_chronology_validation") != "passed":
        errors.append("VALIDATED_DRAFT requires claim_and_chronology_validation gate passed")
    if selection.get("status") != "APPROVED":
        errors.append("structured Candidate Selection must be APPROVED")
    if any(a.get("role") == "UNASSIGNED" for a in selection.get("assignments", []) if isinstance(a, dict)):
        errors.append("approved Candidate Selection still contains UNASSIGNED role")
    if arch.get("status") != "APPROVED":
        errors.append("Human Architecture approval must be APPROVED")

    expected_sections = [
        "00-frontmatter.tex",
        "10-daybreak.tex",
        "20-muse-glimmer.tex",
        "30-inference-stack.tex",
        "40-comfyui.tex",
        "50-x-trend-watch.tex",
        "60-chronology.tex",
        "70-weekly-synthesis.tex",
        "99-source-notes.tex",
    ]
    section_paths: list[Path] = []
    for name in expected_sections:
        path = sections / name
        if not path.is_file():
            errors.append(f"approved Architecture section missing: {path.relative_to(repo_root)}")
        else:
            section_paths.append(path)

    main = main_path.read_text(encoding="utf-8")
    order_markers = [
        "sections/10-daybreak",
        "sections/20-muse-glimmer",
        "sections/30-inference-stack",
        "sections/40-comfyui",
        "sections/50-x-trend-watch",
        "sections/60-chronology",
        "sections/70-weekly-synthesis",
        "sections/99-source-notes",
    ]
    positions = [main.find(marker) for marker in order_markers]
    if any(pos < 0 for pos in positions):
        errors.append("main.tex does not include every approved substantive section")
    elif positions != sorted(positions):
        errors.append("main.tex section order differs from approved Architecture")
    if "90-late-breaking" in main or (sections / "90-late-breaking.tex").exists():
        late_roles = [a for a in selection.get("assignments", []) if isinstance(a, dict) and a.get("role") == "LATE_BREAKING"]
        if not late_roles:
            errors.append("empty/unapproved Late Breaking surface exists despite no LATE_BREAKING role")

    for path in section_paths:
        errors.extend(reader_facing_prose_errors(path, repo_root))
        text = path.read_text(encoding="utf-8")
        for match in HARD_PAGE_RE.finditer(text):
            errors.append(f"hard-coded internal page reference at {path.relative_to(repo_root)}: {match.group(0)!r}")

    trend = sections / "50-x-trend-watch.tex"
    if trend.is_file():
        text = trend.read_text(encoding="utf-8")
        for label in ("\\textbf{現状:}", "\\textbf{未確認:}", "\\textbf{注視点:}"):
            count = text.count(label)
            if count != 5:
                errors.append(f"Trend Watch must contain exactly five {label} labels, found {count}")
        for item in ("Grok 4.6", "Qwen3.8-27B", "Nemotron 3.5 Lightning", "DeepSeek-V4-Pro-0813", "Anthropic Risk Report"):
            if item not in text:
                errors.append(f"approved Trend Watch signal missing: {item}")

    synthesis = sections / "70-weekly-synthesis.tex"
    if synthesis.is_file() and "今週の総括" not in synthesis.read_text(encoding="utf-8"):
        errors.append("final Weekly Synthesis section is not reader-facing as '今週の総括'")

    bib_text = bib_path.read_text(encoding="utf-8")
    bib_keys = set(BIB_KEY_RE.findall(bib_text))
    used_keys: set[str] = set()
    for path in [main_path, *section_paths]:
        text = path.read_text(encoding="utf-8")
        for group in CITE_RE.findall(text):
            used_keys.update(key.strip() for key in group.split(",") if key.strip())
    missing_keys = sorted(used_keys - bib_keys)
    if missing_keys:
        errors.append(f"citation keys missing from references.bib: {missing_keys}")
    unused = sorted(bib_keys - used_keys - {"repo2026w33"})
    if unused:
        warnings.append(f"bibliography keys currently unused by explicit cite: {unused}")

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": not errors,
        "reader_facing_section_count": len(section_paths),
        "used_citation_key_count": len(used_keys),
        "bibliography_key_count": len(bib_keys),
        "errors": errors,
        "warnings": warnings,
    }


def advance(repo_root: Path, issue_id: str, report: dict[str, Any]) -> None:
    if not report.get("passed"):
        raise ValueError("cannot advance failed draft validation")
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    lifecycle = state.get("lifecycle_state")
    if lifecycle in {"DRAFT_COMPLETE", "VALIDATED_DRAFT"}:
        if state.get("gates", {}).get("article_draft") != "passed":
            raise ValueError("downstream draft state must have article_draft gate passed")
        return
    if lifecycle != "ARCHITECTURE_ESTABLISHED":
        raise ValueError("state changed after validation; refusing draft transition")
    state["lifecycle_state"] = "DRAFT_COMPLETE"
    state["gates"]["article_draft"] = "passed"
    write_json(state_path, state)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--report")
    parser.add_argument("--advance-state", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    report = validate(root, args.issue_id)
    if args.report:
        write_json(Path(args.report), report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["passed"]:
        return 1
    if args.advance_state:
        advance(root, args.issue_id, report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
