#!/usr/bin/env python3
"""Reader-facing Architecture fidelity support for Core v2.

The Reader Manuscript manifest is an accountability map, not machine proof of
editorial quality. This module therefore keeps deterministic responsibility
narrow: LONGFORM_SPECIAL coverage locations must resolve to real, non-empty TeX
content blocks. Substantive adequacy remains ChatGPT-owned semantic/editorial
review, but that review must explicitly bind every approved package and every
exact reader block it claims to have assessed.

A soft Architecture page target is never a quota. When a LONGFORM_SPECIAL is
rendered below that target, however, LONGFORM_TECHNICAL_DEPTH must explicitly
record the actual/target observation and a semantic disposition showing that
the below-target density was consciously reviewed rather than auto-passed.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Any

_HEADING = re.compile(r"\\(?P<kind>section|subsection)(?P<star>\*)?\{(?P<title>[^{}]+)\}")
_CITATION = re.compile(r"\\(?:auto|text|paren)?cite\w*\{([^{}]+)\}")
_LOCATION = re.compile(
    r"^(?P<kind>Section|Subsection)\s+(?P<number>\d+(?:\.\d+)?)\s*(?:—|–|-|:)\s*(?P<title>.+)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ReaderBlock:
    canonical_location: str
    kind: str
    section_number: int
    subsection_number: int | None
    title: str
    body: str
    visible_chars: int
    citation_keys: frozenset[str]


def _normal_title(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def _visible_chars(text: str) -> int:
    value = re.sub(r"(?m)%.*$", " ", text)
    # Heading labels are navigation, not substantive reader prose. Remove the
    # entire matched heading before generic command stripping so title text
    # alone cannot make an otherwise empty block appear non-empty.
    value = _HEADING.sub(" ", value)
    value = _CITATION.sub(" ", value)
    value = re.sub(r"\\(?:begin|end)\{[^{}]+\}", " ", value)
    value = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", value)
    value = value.replace("{", " ").replace("}", " ")
    value = re.sub(r"\s+", "", value)
    return len(value)


def _citation_keys(text: str) -> frozenset[str]:
    keys: set[str] = set()
    for match in _CITATION.finditer(text):
        for key in match.group(1).split(","):
            key = key.strip()
            if key:
                keys.add(key)
    return frozenset(keys)


def parse_longform_blocks(source_text: str) -> tuple[list[ReaderBlock], dict[str, ReaderBlock]]:
    """Parse numbered sections and their subsections into stable reader blocks.

    Starred headings are not reader-location authorities because LaTeX does not
    assign them section numbers. They still terminate the preceding numbered
    block, however, so unnumbered appendices/notes/references cannot be silently
    attributed to the preceding numbered reader location.
    """
    matches = list(_HEADING.finditer(source_text))
    section_matches = [match for match in matches if match.group("kind") == "section"]
    numbered_sections = [match for match in section_matches if not match.group("star")]
    section_end_by_start = {
        match.start(): (
            section_matches[index + 1].start()
            if index + 1 < len(section_matches)
            else len(source_text)
        )
        for index, match in enumerate(section_matches)
    }
    blocks: list[ReaderBlock] = []
    by_location: dict[str, ReaderBlock] = {}

    for section_index, section_match in enumerate(numbered_sections, start=1):
        section_end = section_end_by_start[section_match.start()]
        section_body_start = section_match.end()
        section_body = source_text[section_body_start:section_end]
        section_title = section_match.group("title").strip()
        section_location = f"Section {section_index} — {section_title}"
        section_block = ReaderBlock(
            canonical_location=section_location,
            kind="SECTION",
            section_number=section_index,
            subsection_number=None,
            title=section_title,
            body=section_body,
            visible_chars=_visible_chars(section_body),
            citation_keys=_citation_keys(section_body),
        )
        blocks.append(section_block)
        by_location[section_location] = section_block

        all_subsection_matches = [
            match
            for match in matches
            if match.group("kind") == "subsection"
            and section_body_start <= match.start() < section_end
        ]
        subsection_end_by_start = {
            match.start(): (
                all_subsection_matches[index + 1].start()
                if index + 1 < len(all_subsection_matches)
                else section_end
            )
            for index, match in enumerate(all_subsection_matches)
        }
        numbered_subsection_matches = [
            match for match in all_subsection_matches if not match.group("star")
        ]
        for subsection_index, subsection_match in enumerate(numbered_subsection_matches, start=1):
            subsection_end = subsection_end_by_start[subsection_match.start()]
            body = source_text[subsection_match.end():subsection_end]
            title = subsection_match.group("title").strip()
            location = f"Subsection {section_index}.{subsection_index} — {title}"
            block = ReaderBlock(
                canonical_location=location,
                kind="SUBSECTION",
                section_number=section_index,
                subsection_number=subsection_index,
                title=title,
                body=body,
                visible_chars=_visible_chars(body),
                citation_keys=_citation_keys(body),
            )
            blocks.append(block)
            by_location[location] = block

    return blocks, by_location


def _resolve_location(raw: Any, blocks: list[ReaderBlock]) -> ReaderBlock:
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError("reader location must be a non-empty string")
    match = _LOCATION.fullmatch(raw.strip())
    if not match:
        raise ValueError(
            "LONGFORM_SPECIAL reader location must identify an exact TeX content block as "
            "'Section N — title' or 'Subsection N.M — title'"
        )
    kind = match.group("kind").casefold()
    number = match.group("number")
    title = _normal_title(match.group("title"))
    candidates: list[ReaderBlock] = []
    if kind == "section" and "." not in number:
        section_number = int(number)
        candidates = [
            block
            for block in blocks
            if block.kind == "SECTION" and block.section_number == section_number
        ]
    elif kind == "subsection" and "." in number:
        first, second = number.split(".", 1)
        candidates = [
            block
            for block in blocks
            if block.kind == "SUBSECTION"
            and block.section_number == int(first)
            and block.subsection_number == int(second)
        ]
    if len(candidates) != 1:
        raise ValueError(f"reader location does not resolve to exactly one TeX block: {raw}")
    block = candidates[0]
    if _normal_title(block.title) != title:
        raise ValueError(
            f"reader location title does not match exact TeX heading: {raw!r} != {block.canonical_location!r}"
        )
    if block.visible_chars < 1:
        raise ValueError(f"reader location resolves to an empty TeX content block: {block.canonical_location}")
    return block


def _package_requirements(architecture: dict[str, Any]) -> list[tuple[str, list[str]]]:
    out: list[tuple[str, list[str]]] = []
    for package in architecture.get("packages", []):
        package_id = package.get("package_id")
        requirements = package.get("must_cover_requirements", [])
        if not isinstance(package_id, str) or not package_id:
            raise ValueError("Architecture package_id invalid")
        if not isinstance(requirements, list) or not all(
            isinstance(value, str) and value.strip() for value in requirements
        ):
            raise ValueError(f"Architecture must-cover requirements invalid: {package_id}")
        out.append((package_id, requirements))
    if not out:
        raise ValueError("LONGFORM_SPECIAL Architecture must contain packages")
    return out


def validate_reader_fidelity(
    source_text: str,
    architecture: dict[str, Any],
    architecture_coverage: list[dict[str, Any]],
    reader_requirements: list[dict[str, Any]],
    publication_profile: str,
) -> dict[str, Any]:
    """Validate deterministic traceability for LONGFORM_SPECIAL reader claims.

    This intentionally does not infer editorial quality from character counts,
    page counts, section counts, source counts, or one-package/one-section
    layout. Those are semantic/editorial questions. The deterministic invariant
    is that every claimed coverage location is an exact, extant, non-empty
    reader-facing content block whose bytes are already bound by the manifest.
    """
    if publication_profile != "LONGFORM_SPECIAL":
        return {"status": "NOT_APPLICABLE", "publication_profile": publication_profile}

    package_requirements = _package_requirements(architecture)
    blocks, _ = parse_longform_blocks(source_text)
    if not blocks:
        raise ValueError("LONGFORM_SPECIAL reader source exposes no numbered TeX content blocks")

    coverage_keys = {
        (row.get("package_id"), row.get("requirement"))
        for row in architecture_coverage
        if isinstance(row, dict)
    }
    expected_keys = {
        (package_id, requirement)
        for package_id, requirements in package_requirements
        for requirement in requirements
    }
    if coverage_keys != expected_keys:
        raise ValueError(
            "Architecture coverage must exactly match approved must-cover requirements before fidelity review"
        )

    package_locations: dict[str, set[str]] = {
        package_id: set() for package_id, _ in package_requirements
    }
    coverage_locations: set[str] = set()
    for row in architecture_coverage:
        package_id = row["package_id"]
        locations = row.get("reader_locations")
        if not isinstance(locations, list) or not locations:
            raise ValueError(
                f"Architecture coverage requires reader locations: {package_id}/{row['requirement']}"
            )
        for raw_location in locations:
            block = _resolve_location(raw_location, blocks)
            package_locations[package_id].add(block.canonical_location)
            coverage_locations.add(block.canonical_location)

    final_rows = [
        row
        for row in reader_requirements
        if isinstance(row, dict) and row.get("requirement_id") == "FINAL_SYNTHESIS"
    ]
    if len(final_rows) != 1:
        raise ValueError("LONGFORM_SPECIAL Reader Manifest requires exactly one FINAL_SYNTHESIS requirement")
    final_locations = final_rows[0].get("reader_locations")
    if not isinstance(final_locations, list) or not final_locations:
        raise ValueError("FINAL_SYNTHESIS requires exact reader locations")
    resolved_final = [_resolve_location(value, blocks) for value in final_locations]

    return {
        "status": "PASS",
        "publication_profile": publication_profile,
        "package_locations": {
            package_id: sorted(locations)
            for package_id, locations in package_locations.items()
        },
        "coverage_locations": sorted(coverage_locations),
        "final_synthesis_locations": sorted(
            block.canonical_location for block in resolved_final
        ),
    }


def _check_row(checks: list[dict[str, Any]], check_id: str) -> dict[str, Any]:
    rows = [
        row
        for row in checks
        if isinstance(row, dict) and row.get("check_id") == check_id
    ]
    if len(rows) != 1:
        raise ValueError(f"semantic review requires exactly one {check_id} check")
    return rows[0]


def _locations_from_manifest(manuscript: dict[str, Any]) -> tuple[set[str], set[str]]:
    coverage_locations = {
        location
        for row in manuscript.get("architecture_coverage", [])
        if isinstance(row, dict)
        for location in row.get("reader_locations", [])
        if isinstance(location, str) and location
    }
    final_locations = {
        location
        for row in manuscript.get("reader_requirements", [])
        if isinstance(row, dict) and row.get("requirement_id") == "FINAL_SYNTHESIS"
        for location in row.get("reader_locations", [])
        if isinstance(location, str) and location
    }
    return coverage_locations, final_locations


def _require_evidence(
    check: dict[str, Any],
    required: set[str],
    label: str,
) -> None:
    actual = set(check.get("evidence_locations", []))
    if not required.issubset(actual):
        missing = sorted(required - actual)
        raise ValueError(f"{label} must bind exact semantic-review evidence; missing={missing}")


def _final_package_id(architecture: dict[str, Any]) -> str | None:
    ordered: list[tuple[int, str]] = []
    for package in architecture.get("packages", []):
        if not isinstance(package, dict):
            continue
        package_id = package.get("package_id")
        drafting_order = package.get("drafting_order")
        if not isinstance(package_id, str) or not package_id:
            raise ValueError("Architecture package_id invalid for final-synthesis review")
        if isinstance(drafting_order, bool) or not isinstance(drafting_order, int):
            raise ValueError(f"Architecture drafting_order invalid for {package_id}")
        ordered.append((drafting_order, package_id))
    if not ordered:
        return None
    max_order = max(order for order, _ in ordered)
    finalists = [package_id for order, package_id in ordered if order == max_order]
    if len(finalists) != 1:
        raise ValueError("Architecture final package is ambiguous by drafting_order")
    return finalists[0]


def _page_target_marker(target: int | float) -> str:
    numeric = float(target)
    if numeric.is_integer():
        return str(int(numeric))
    return format(numeric, ".15g")


def validate_review_depth(
    profile: dict[str, Any],
    architecture: dict[str, Any],
    manuscript: dict[str, Any],
    page_count: int,
    checks: list[dict[str, Any]],
    review_kind: str,
) -> None:
    """Require explicit package/block-level semantic review for LONGFORM_SPECIAL."""
    if (
        review_kind != "SEMANTIC_EDITORIAL"
        or profile.get("publication_profile") != "LONGFORM_SPECIAL"
    ):
        return

    package_ids = [
        row.get("package_id")
        for row in architecture.get("packages", [])
        if isinstance(row, dict) and isinstance(row.get("package_id"), str)
    ]
    package_markers = {f"package:{package_id}" for package_id in package_ids}
    coverage_locations, final_locations = _locations_from_manifest(manuscript)

    architecture_fidelity = _check_row(checks, "ARCHITECTURE_CONTENT_FIDELITY")
    _require_evidence(
        architecture_fidelity,
        package_markers | coverage_locations,
        "ARCHITECTURE_CONTENT_FIDELITY",
    )

    longform_depth = _check_row(checks, "LONGFORM_TECHNICAL_DEPTH")
    _require_evidence(
        longform_depth,
        package_markers | coverage_locations,
        "LONGFORM_TECHNICAL_DEPTH",
    )

    final = _check_row(checks, "FINAL_SYNTHESIS_QUALITY")
    final_required = set(final_locations) | {"reader-role:final-synthesis"}
    final_package_id = _final_package_id(architecture)
    if final_package_id is not None:
        final_required.add(f"package:{final_package_id}")
    _require_evidence(final, final_required, "FINAL_SYNTHESIS_QUALITY")

    page_plan = architecture.get("page_plan") or {}
    target = page_plan.get("target_pages") if isinstance(page_plan, dict) else None
    if (
        isinstance(target, bool)
        or not isinstance(target, (int, float))
        or not math.isfinite(float(target))
        or target < 1
        or page_count >= target
    ):
        return

    density_required = {
        f"page-plan:{page_count}/{_page_target_marker(target)}",
        "density-review:below-target-substantive",
    }
    _require_evidence(
        longform_depth,
        density_required,
        "below-target LONGFORM_TECHNICAL_DEPTH",
    )
