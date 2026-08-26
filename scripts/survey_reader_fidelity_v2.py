#!/usr/bin/env python3
"""Deterministic reader-facing substantive-fidelity checks for Core v2.

The Reader Manuscript manifest is an accountability map, not evidence that an
Architecture requirement was substantively fulfilled.  This module resolves
that map against the exact TeX source and rejects LONGFORM_SPECIAL manuscripts
that only prove structural/topic presence.

The checks deliberately do not turn page targets into quotas.  They measure
reader-facing content blocks derived from the authored section/subsection
structure, require Architecture requirements to map to real blocks, and force
an explicit package-by-package semantic depth review when the rendered result
is severely below the soft Architecture page target.
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
_FINAL_ROLE = re.compile(r"(?:総括|まとめ|結論|synthesis|conclusion|final)", re.IGNORECASE)


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
    """Parse numbered sections and their subsections into stable reader blocks."""
    matches = list(_HEADING.finditer(source_text))
    numbered_sections = [m for m in matches if m.group("kind") == "section" and not m.group("star")]
    blocks: list[ReaderBlock] = []
    by_location: dict[str, ReaderBlock] = {}

    for section_index, section_match in enumerate(numbered_sections, start=1):
        section_end = (
            numbered_sections[section_index].start()
            if section_index < len(numbered_sections)
            else len(source_text)
        )
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

        subsection_matches = [
            m for m in matches
            if m.group("kind") == "subsection"
            and section_body_start <= m.start() < section_end
        ]
        for subsection_index, subsection_match in enumerate(subsection_matches, start=1):
            subsection_end = (
                subsection_matches[subsection_index].start()
                if subsection_index < len(subsection_matches)
                else section_end
            )
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
            "reader location must identify an exact TeX content block as "
            "'Section N — title' or 'Subsection N.M — title'"
        )
    kind = match.group("kind").casefold()
    number = match.group("number")
    title = _normal_title(match.group("title"))
    candidates: list[ReaderBlock] = []
    if kind == "section" and "." not in number:
        section_number = int(number)
        candidates = [
            block for block in blocks
            if block.kind == "SECTION" and block.section_number == section_number
        ]
    elif kind == "subsection" and "." in number:
        first, second = number.split(".", 1)
        candidates = [
            block for block in blocks
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
    return block


def _package_requirements(architecture: dict[str, Any]) -> list[tuple[str, list[str]]]:
    out: list[tuple[str, list[str]]] = []
    for package in architecture.get("packages", []):
        package_id = package.get("package_id")
        requirements = package.get("must_cover_requirements", [])
        if not isinstance(package_id, str) or not package_id:
            raise ValueError("Architecture package_id invalid")
        if not isinstance(requirements, list) or not all(isinstance(v, str) and v.strip() for v in requirements):
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
    """Validate exact reader blocks against approved Architecture requirements.

    WEEKLY_MAGAZINE remains governed by its existing publication-boundary and
    semantic checks.  The stricter quantitative block accounting here targets
    the remaining #434 LONGFORM_SPECIAL failure observed after the redesign.
    """
    if publication_profile != "LONGFORM_SPECIAL":
        return {"status": "NOT_APPLICABLE", "publication_profile": publication_profile}

    package_requirements = _package_requirements(architecture)
    blocks, _ = parse_longform_blocks(source_text)
    sections = [block for block in blocks if block.kind == "SECTION"]
    if len(sections) != len(package_requirements):
        raise ValueError(
            "LONGFORM_SPECIAL reader source must expose exactly one numbered section per approved "
            f"Architecture package: expected={len(package_requirements)} actual={len(sections)}"
        )

    package_index = {package_id: idx + 1 for idx, (package_id, _) in enumerate(package_requirements)}
    requirements_by_package = {package_id: requirements for package_id, requirements in package_requirements}
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
        raise ValueError("Architecture coverage must exactly match approved must-cover requirements before fidelity review")

    location_use: dict[str, int] = {}
    package_locations: dict[str, set[str]] = {package_id: set() for package_id, _ in package_requirements}
    for row in architecture_coverage:
        package_id = row["package_id"]
        locations = row.get("reader_locations")
        if not isinstance(locations, list) or not locations:
            raise ValueError(f"Architecture coverage requires reader locations: {package_id}/{row['requirement']}")
        for raw_location in locations:
            block = _resolve_location(raw_location, blocks)
            if block.section_number != package_index[package_id]:
                raise ValueError(
                    f"Architecture requirement maps outside its package reader section: "
                    f"{package_id}/{row['requirement']} -> {block.canonical_location}"
                )
            minimum = 500 if block.kind == "SECTION" else 220
            if block.visible_chars < minimum:
                raise ValueError(
                    f"reader content block is too thin for substantive Architecture coverage: "
                    f"{block.canonical_location} visible_chars={block.visible_chars} minimum={minimum}"
                )
            location_use[block.canonical_location] = location_use.get(block.canonical_location, 0) + 1
            if location_use[block.canonical_location] > 2:
                raise ValueError(
                    "one reader content block may satisfy at most two Architecture requirements; "
                    f"overloaded={block.canonical_location}"
                )
            package_locations[package_id].add(block.canonical_location)

    metrics: list[dict[str, Any]] = []
    for package_id, requirements in package_requirements:
        section = sections[package_index[package_id] - 1]
        distinct_locations = package_locations[package_id]
        minimum_blocks = max(2, math.ceil(len(requirements) / 2)) if requirements else 1
        if len(distinct_locations) < minimum_blocks:
            raise ValueError(
                f"LONGFORM_SPECIAL package lacks distinct reader blocks for its Architecture obligations: "
                f"{package_id} blocks={len(distinct_locations)} minimum={minimum_blocks}"
            )
        minimum_chars = max(1600, 600 * max(1, len(requirements)))
        if section.visible_chars < minimum_chars:
            raise ValueError(
                "LONGFORM_SPECIAL package is structurally present but lacks substantive reader-facing depth: "
                f"{package_id} visible_chars={section.visible_chars} minimum={minimum_chars} "
                f"must_cover={len(requirements)}"
            )
        minimum_citations = 2 if len(requirements) >= 2 else 1
        if len(section.citation_keys) < minimum_citations:
            raise ValueError(
                f"LONGFORM_SPECIAL package lacks source diversity for substantive treatment: "
                f"{package_id} citation_keys={len(section.citation_keys)} minimum={minimum_citations}"
            )
        metrics.append(
            {
                "package_id": package_id,
                "visible_chars": section.visible_chars,
                "citation_key_count": len(section.citation_keys),
                "mapped_block_count": len(distinct_locations),
                "must_cover_count": len(requirements),
            }
        )

    final_rows = [row for row in reader_requirements if row.get("requirement_id") == "FINAL_SYNTHESIS"]
    if len(final_rows) != 1:
        raise ValueError("LONGFORM_SPECIAL Reader Manifest requires exactly one FINAL_SYNTHESIS requirement")
    final_section = sections[-1]
    final_locations = final_rows[0].get("reader_locations")
    if not isinstance(final_locations, list) or not final_locations:
        raise ValueError("FINAL_SYNTHESIS requires exact reader locations")
    resolved_final = [_resolve_location(value, blocks) for value in final_locations]
    if not any(block.section_number == final_section.section_number for block in resolved_final):
        raise ValueError("FINAL_SYNTHESIS must resolve inside the final Architecture package section")
    if not _FINAL_ROLE.search(final_section.title):
        raise ValueError(
            "final Architecture package must remain reader-visible as a synthesis/conclusion role; "
            f"heading={final_section.title!r}"
        )
    final_package_id, final_requirements = package_requirements[-1]
    final_minimum = max(1800, 600 * max(1, len(final_requirements)))
    if final_section.visible_chars < final_minimum:
        raise ValueError(
            f"final synthesis is too thin for approved Architecture intent: {final_package_id} "
            f"visible_chars={final_section.visible_chars} minimum={final_minimum}"
        )

    return {
        "status": "PASS",
        "publication_profile": publication_profile,
        "package_metrics": metrics,
        "total_visible_chars": sum(section.visible_chars for section in sections),
        "total_must_cover": sum(len(requirements) for _, requirements in package_requirements),
        "final_synthesis_location": final_section.canonical_location,
    }


def _check_row(checks: list[dict[str, Any]], check_id: str) -> dict[str, Any]:
    rows = [row for row in checks if isinstance(row, dict) and row.get("check_id") == check_id]
    if len(rows) != 1:
        raise ValueError(f"semantic review requires exactly one {check_id} check")
    return rows[0]


def validate_review_depth(
    profile: dict[str, Any],
    architecture: dict[str, Any],
    page_count: int,
    checks: list[dict[str, Any]],
    review_kind: str,
) -> None:
    """Harden the existing semantic checks when a longform result is compressed."""
    if review_kind != "SEMANTIC_EDITORIAL" or profile.get("publication_profile") != "LONGFORM_SPECIAL":
        return
    packages = architecture.get("packages", [])
    package_ids = [row.get("package_id") for row in packages if isinstance(row, dict)]
    expected_locations = {f"package:{package_id}" for package_id in package_ids if package_id}

    fidelity = _check_row(checks, "ARCHITECTURE_CONTENT_FIDELITY")
    fidelity_locations = set(fidelity.get("evidence_locations", []))
    if not expected_locations.issubset(fidelity_locations):
        missing = sorted(expected_locations - fidelity_locations)
        raise ValueError(
            "ARCHITECTURE_CONTENT_FIDELITY must record package-by-package substantive review evidence; "
            f"missing={missing}"
        )

    final = _check_row(checks, "FINAL_SYNTHESIS_QUALITY")
    final_locations = set(final.get("evidence_locations", []))
    if package_ids and f"package:{package_ids[-1]}" not in final_locations:
        raise ValueError("FINAL_SYNTHESIS_QUALITY must bind the final Architecture package explicitly")
    if "reader-role:final-synthesis" not in final_locations:
        raise ValueError("FINAL_SYNTHESIS_QUALITY must confirm the reader-visible final-synthesis role")

    page_plan = architecture.get("page_plan") or {}
    target = page_plan.get("target_pages") if isinstance(page_plan, dict) else None
    if not isinstance(target, int) or target < 1:
        return
    if page_count * 3 >= target * 2:
        return

    depth = _check_row(checks, "LONGFORM_TECHNICAL_DEPTH")
    depth_locations = set(depth.get("evidence_locations", []))
    if not expected_locations.issubset(depth_locations):
        missing = sorted(expected_locations - depth_locations)
        raise ValueError(
            "severely below-target LONGFORM_SPECIAL requires package-by-package depth review; "
            f"actual_pages={page_count} target_pages={target} missing={missing}"
        )
    if f"page-plan:{page_count}/{target}" not in depth_locations:
        raise ValueError(
            "severely below-target LONGFORM_SPECIAL must record the exact actual/target page-plan observation "
            f"as page-plan:{page_count}/{target}"
        )
    detail = depth.get("detail")
    if not isinstance(detail, str) or len(re.sub(r"\s+", "", detail)) < 120:
        raise ValueError(
            "severely below-target LONGFORM_SPECIAL requires an explicit substantive density/depth justification"
        )
