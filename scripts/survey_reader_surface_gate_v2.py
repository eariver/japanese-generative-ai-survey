#!/usr/bin/env python3
"""Pre-Publication Reader-Surface Gate for Survey Production Core v2.

This module enforces a strict, fail-fast boundary between internal Core v2
production/architecture/screening/review metadata and reader-facing publication
prose. It executes before expensive TeX/layout materialization, LuaLaTeX PDF
compilation, and candidate assembly.

The gate operates across two complementary layers on reader-facing fields only:
1. Deterministic Lexical Lint: scans reader-facing text (TeX body blocks,
   headings, bibliography fields, publication payloads, reader manuscript
   details) for prohibited internal vocabulary, stage names, pipeline
   operations, and repository-internal identifiers.
2. Bounded Semantic Review: validates machine-checkable review contracts
   ensuring no reader-facing sentence requires internal production pipeline
   knowledge to make sense to an ordinary technical reader.

A narrow, audited suppression mechanism allows legitimate technical discussion
of similarly named external concepts without globally disabling protection.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from scripts import survey_production_v2 as core
from scripts import survey_reader_fidelity_v2 as fidelity
from scripts import survey_schema_v2 as schema_gate

SURFACE_GATE_SCHEMA = Path("schemas/reader-surface-gate-v2.schema.json")
MANUSCRIPT_SCHEMA = Path("schemas/reader-manuscript-v2.schema.json")


@dataclass(frozen=True)
class RuleDefinition:
    rule_id: str
    layer: str  # "LEXICAL_LINT" | "SEMANTIC_REVIEW"
    description: str
    severity: str  # "BLOCKING" | "WARNING"


@dataclass(frozen=True)
class SurfaceFinding:
    finding_id: str
    rule_id: str
    artifact: str
    path: str
    field_or_block: str
    locator: str
    text_span: str
    severity: str  # "BLOCKING" | "WARNING" | "INFO" | "SUPPRESSED"
    reason: str
    proposed_normalization: str
    disposition: str  # "UNRESOLVED" | "SUPPRESSED" | "NORMALIZED"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


RULES: list[RuleDefinition] = [
    RuleDefinition(
        rule_id="RSG-LEX-CORE-VOCAB",
        layer="LEXICAL_LINT",
        description="Core v2 pipeline and architecture internal terminology in reader-facing prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-SELECTION-SCREENING",
        layer="LEXICAL_LINT",
        description="Candidate screening, selection rounds, and negative selection decisions in reader prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-DISCOVERY-INTAKE",
        layer="LEXICAL_LINT",
        description="Discovery intake, observation metadata, and candidate reviews in reader prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-VERIFICATION-MATERIALITY",
        layer="LEXICAL_LINT",
        description="Internal verification obligations and materiality markers in reader prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-INTERNAL-IDENTIFIERS",
        layer="LEXICAL_LINT",
        description="Internal package identifiers and raw evidence IDs in reader prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-STAGE-LIFECYCLE",
        layer="LEXICAL_LINT",
        description="Internal stage and checkpoint lifecycle names used as publication prose",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-INTERNAL-PATHS",
        layer="LEXICAL_LINT",
        description="Internal repository, transport, or Grok paths in reader prose or URLs",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-BIBLIOGRAPHY-LEAKAGE",
        layer="LEXICAL_LINT",
        description="Internal evidence tags and materiality leaked into bibliography records",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-EDITORIAL-PROCESS",
        layer="LEXICAL_LINT",
        description="Internal editorial operations explained as prose rather than underlying facts",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-LEX-REVIEW-RATIONALE-COP-OUT",
        layer="LEXICAL_LINT",
        description="Architecture review meta-rebuttals and cop-out coverage assertions",
        severity="BLOCKING",
    ),
    RuleDefinition(
        rule_id="RSG-SEM-PROCESS-LEAKAGE",
        layer="SEMANTIC_REVIEW",
        description="Reader-facing sentence requiring internal pipeline knowledge to make sense",
        severity="BLOCKING",
    ),
]

RULE_BY_ID = {rule.rule_id: rule for rule in RULES}

# Patterns for lexical lint
# Each entry is (rule_id, regex_pattern, default_reason, normalization_hint)
LEXICAL_PATTERNS: list[tuple[str, re.Pattern[str], str, str]] = [
    # RSG-LEX-CORE-VOCAB
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"承認済み\s*Architecture", re.IGNORECASE),
        "Leaks internal approved Architecture status into reader prose",
        "Explain the survey structure or topic directly without citing approval state",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bapproved\s+architecture\b", re.IGNORECASE),
        "Leaks internal Architecture approval phrasing into reader prose",
        "State the editorial focus or topic structure directly",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"Core\s*v2\s*contract", re.IGNORECASE),
        "Leaks Core v2 contract into reader prose",
        "Remove pipeline contract reference",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"Core\s*v2\s*Evidence", re.IGNORECASE),
        "Leaks Core v2 Evidence terminology into reader prose",
        "Refer to the underlying sources or factual claims directly",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bCore\s+v2\b", re.IGNORECASE),
        "Leaks Core v2 repository engine name into reader prose",
        "Remove Core v2 reference from publication text",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"Evidence\s+Card", re.IGNORECASE),
        "Leaks internal Evidence Card artifact name into reader prose",
        "Refer to primary documentation or vendor specifications",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"本\s*Evidence"),
        "Leaks internal Evidence artifact reference into reader prose",
        "Refer to the source, benchmark, or announcement directly",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"Evidence\s+pass", re.IGNORECASE),
        "Leaks internal Evidence pass evaluation into reader prose",
        "State the verified technical findings directly",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"Selection\s*済み\s*Evidence"),
        "Leaks Selection-bound Evidence metadata into reader prose",
        "Discuss the selected systems or models on their factual merits",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bnormalized\s+claim\b", re.IGNORECASE),
        "Leaks internal claim normalization vocabulary into reader prose",
        "State the claim in natural reader-facing prose",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bSource-bound\s+record\b", re.IGNORECASE),
        "Leaks internal record binding phrase into reader prose",
        "Describe the source materials directly",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bThis\s+retained\s+evidence\s+note\b", re.IGNORECASE),
        "Leaks internal retained evidence phrasing into reader prose",
        "Frame as an observation or limitation on available data",
    ),
    (
        "RSG-LEX-CORE-VOCAB",
        re.compile(r"\bThe\s+bound\s+[A-Za-z0-9_-]+", re.IGNORECASE),
        "Leaks internal binding phrasing into reader prose",
        "Describe the referenced entity naturally",
    ),

    # RSG-LEX-SELECTION-SCREENING
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?<![A-Za-z0-9])Selection\s+r\d+(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks internal Selection revision round (e.g. Selection r2) into reader prose",
        "Remove selection round reference and discuss the topic directly",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"Candidate\s+Selection", re.IGNORECASE),
        "Leaks internal Candidate Selection stage name into reader prose",
        "Discuss selected developments directly",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"Selection\s*済み"),
        "Leaks internal Selection state into reader prose",
        "Refer to surveyed or featured developments",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?:一次|二次)?Screening\s*(?:で|段階|passed|判定|において|結果|を通過|済み|落ち)"),
        "Leaks internal screening pipeline stage into reader prose",
        "Discuss inclusion scope or criteria substantively",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?<![A-Za-z0-9])(?:candidate|evidence|source)\s+screening(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks candidate screening pipeline concept into reader prose",
        "Discuss editorial scope or research methodology in reader-facing terms",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?<![A-Za-z0-9])DROP\s*(?:判定|とした|と判定|された|扱い|理由)"),
        "Leaks internal DROP candidate disposition into reader prose",
        "Explain non-inclusion through scope boundaries or lack of public data",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?<![A-Za-z0-9_])HOLD_OUT(?:_ONLY)?(?![A-Za-z0-9_])"),
        "Leaks internal HOLD_OUT candidate disposition enum into reader prose",
        "Describe ongoing monitoring or future observation focus",
    ),
    (
        "RSG-LEX-SELECTION-SCREENING",
        re.compile(r"(?<![A-Za-z0-9_])SOCIAL_OBSERVATION(?:_ONLY)?(?![A-Za-z0-9_])"),
        "Leaks internal SOCIAL_OBSERVATION enum into reader prose",
        "Describe community discussion or social reception naturally",
    ),

    # RSG-LEX-DISCOVERY-INTAKE
    (
        "RSG-LEX-DISCOVERY-INTAKE",
        re.compile(r"(?<![A-Za-z0-9])Discovery\s+observation(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks internal Discovery observation terminology into reader prose",
        "Attribute observations to public posts, repository activity, or changelogs",
    ),
    (
        "RSG-LEX-DISCOVERY-INTAKE",
        re.compile(r"(?<![A-Za-z0-9])Discovery\s+sources?(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks internal Discovery sources terminology into reader prose",
        "Cite the specific public sources directly",
    ),
    (
        "RSG-LEX-DISCOVERY-INTAKE",
        re.compile(r"(?<![A-Za-z0-9])Discovery\s+ID(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks Discovery identifier label into reader prose",
        "Cite the public source by author and title",
    ),
    (
        "RSG-LEX-DISCOVERY-INTAKE",
        re.compile(r"(?<![A-Za-z0-9])candidate-specific\s+review(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks candidate-specific review terminology into reader prose",
        "Discuss the system properties directly without referencing review tasks",
    ),

    # RSG-LEX-VERIFICATION-MATERIALITY
    (
        "RSG-LEX-VERIFICATION-MATERIALITY",
        re.compile(r"(?<![A-Za-z0-9])materiality:\s*", re.IGNORECASE),
        "Leaks internal materiality ledger tag into reader prose",
        "Explain the practical significance of the development directly",
    ),
    (
        "RSG-LEX-VERIFICATION-MATERIALITY",
        re.compile(r"Core\s*v2\s*Evidence:\s*", re.IGNORECASE),
        "Leaks internal Core v2 Evidence status prefix into reader prose",
        "Remove internal verification prefix",
    ),
    (
        "RSG-LEX-VERIFICATION-MATERIALITY",
        re.compile(r"(?<![A-Za-z0-9])Verify\s+[A-Za-z0-9_-]+", re.IGNORECASE),
        "Leaks internal verification obligation prose into reader prose",
        "State verified findings or noted limits without raw 'Verify ...' imperative",
    ),

    # RSG-LEX-INTERNAL-IDENTIFIERS
    (
        "RSG-LEX-INTERNAL-IDENTIFIERS",
        re.compile(r"(?<![A-Za-z0-9])Package\s+\d+(?![A-Za-z0-9])"),
        "Leaks internal Package number (e.g. Package 4) into reader prose",
        "Refer to the section or thematic topic by title rather than package number",
    ),
    (
        "RSG-LEX-INTERNAL-IDENTIFIERS",
        re.compile(r"本\s*package(?![A-Za-z0-9])", re.IGNORECASE),
        "Leaks internal package reference ('本 package') into reader prose",
        "Refer to '本節' (this section) or the specific topic name",
    ),
    (
        "RSG-LEX-INTERNAL-IDENTIFIERS",
        re.compile(r"本パッケージ(?![A-Za-z0-9])"),
        "Leaks internal package reference ('本パッケージ') into reader prose",
        "Refer to '本節' (this section) or the specific topic name",
    ),
    (
        "RSG-LEX-INTERNAL-IDENTIFIERS",
        re.compile(r"(?<![A-Za-z0-9._-])[A-Za-z0-9._-]+-D\d{3,}(?![A-Za-z0-9._-])"),
        "Leaks repository-internal Discovery identifier into reader prose",
        "Use public citations (\\cite) or name the source publication directly",
    ),
    (
        "RSG-LEX-INTERNAL-IDENTIFIERS",
        re.compile(r"(?<![A-Za-z0-9])D\d{3,}(?![A-Za-z0-9])"),
        "Leaks short internal Evidence/Discovery identifier (e.g. D017, D021) into reader prose",
        "Distinguish claims by source type (e.g. technical spec vs license) instead of internal IDs",
    ),

    # RSG-LEX-STAGE-LIFECYCLE
    (
        "RSG-LEX-STAGE-LIFECYCLE",
        re.compile(
            r"(?<![A-Za-z0-9_])(?:ISSUE_INITIALIZED|DISCOVERY_COLLECTED|CANDIDATES_NORMALIZED|"
            r"EVIDENCE_REVIEWED|SELECTION_COMPLETE|ARCHITECTURE_ESTABLISHED|"
            r"DRAFT_COMPLETE|VALIDATED_DRAFT|RELEASE_CANDIDATE)(?![A-Za-z0-9_])"
        ),
        "Leaks internal lifecycle stage enum into reader prose",
        "Remove internal stage name from publication text",
    ),

    # RSG-LEX-INTERNAL-PATHS
    (
        "RSG-LEX-INTERNAL-PATHS",
        re.compile(r"/tmp/[A-Za-z0-9._/-]+"),
        "Leaks temporary executor path into reader prose or URLs",
        "Use repository-stable or public canonical URLs",
    ),
    (
        "RSG-LEX-INTERNAL-PATHS",
        re.compile(r"sources/(?:2026-W\d+|SP\d+)/[A-Za-z0-9._/-]*"),
        "Leaks repository internal sources/ path into reader prose or URLs",
        "Use public web URLs or omit internal paths from reader prose",
    ),
    (
        "RSG-LEX-INTERNAL-PATHS",
        re.compile(r"surveys/(?:weekly|special)/[A-Za-z0-9._/-]*"),
        "Leaks repository internal surveys/ path into reader prose or URLs",
        "Use public web URLs or omit internal paths from reader prose",
    ),
    (
        "RSG-LEX-INTERNAL-PATHS",
        re.compile(r"grok/sources/[A-Za-z0-9._/-]*", re.IGNORECASE),
        "Leaks internal Grok intake path into reader prose or URLs",
        "Use public post URLs",
    ),

    # RSG-LEX-BIBLIOGRAPHY-LEAKAGE
    (
        "RSG-LEX-BIBLIOGRAPHY-LEAKAGE",
        re.compile(r"Evidence\s+tags?:", re.IGNORECASE),
        "Leaks internal Evidence tags label into bibliography",
        "Bibliography entries must contain public bibliographic metadata only",
    ),
    (
        "RSG-LEX-BIBLIOGRAPHY-LEAKAGE",
        re.compile(r"\[[VPMCHE]/[VPMCHE]\]"),
        "Leaks internal evidence/materiality matrix tag (e.g. [V/M]) into bibliography",
        "Retain classification in internal ledgers; do not serialize into BibTeX",
    ),

    # RSG-LEX-EDITORIAL-PROCESS
    (
        "RSG-LEX-EDITORIAL-PROCESS",
        re.compile(r"一次資料(?:として|へ)?昇格させない"),
        "Explains internal evidence promotion operation rather than facts",
        "State that findings are based on community testing rather than vendor documentation",
    ),
    (
        "RSG-LEX-EDITORIAL-PROCESS",
        re.compile(r"一次資料(?:として|へ)?昇格"),
        "Discusses evidence promotion process rather than the factual development",
        "Describe the source's authority and scope directly",
    ),
    (
        "RSG-LEX-EDITORIAL-PROCESS",
        re.compile(r"coverage\s*を(?:広げる|拡大|狭める|制限)"),
        "Discusses internal coverage expansion/contraction rather than domain facts",
        "State the scope of analyzed systems directly",
    ),
    (
        "RSG-LEX-EDITORIAL-PROCESS",
        re.compile(r"カバレッジを(?:広げる|拡大|狭める|制限)"),
        "Discusses internal coverage operations rather than domain facts",
        "State the scope of analyzed systems directly",
    ),
    (
        "RSG-LEX-EDITORIAL-PROCESS",
        re.compile(r"本\s*package\s*では"),
        "Uses internal package packaging phrasing to frame content",
        "Use '本節では' or frame by subject matter directly",
    ),

    # RSG-LEX-REVIEW-RATIONALE-COP-OUT
    (
        "RSG-LEX-REVIEW-RATIONALE-COP-OUT",
        re.compile(r"W\d+は三つの(?:Feature|トピック|話題)だけではない"),
        "Meta-rebuttal to prior Architecture Review comment serialized into reader prose",
        "Directly present the multifaceted developments without referencing earlier drafts",
    ),
    (
        "RSG-LEX-REVIEW-RATIONALE-COP-OUT",
        re.compile(r"\bnot\s+a\s+three-story\s+week\b", re.IGNORECASE),
        "Meta-rebuttal to prior Architecture Review comment serialized into reader prose",
        "Present the breadth of developments directly without arguing against prior scope",
    ),
    (
        "RSG-LEX-REVIEW-RATIONALE-COP-OUT",
        re.compile(r"(?:前回の|Reviewでの|レビューでの|Architecture\s*Reviewでの)指摘(?:を|に|により|を受けて|に基づき)"),
        "Serializes internal review feedback history into publication prose",
        "State the established analysis directly without referencing review feedback",
    ),
    (
        "RSG-LEX-REVIEW-RATIONALE-COP-OUT",
        re.compile(r"Architecture\s*(?:requires|要求|は.*を観察軸としている|の要求)"),
        "Asserts Architecture requirement as a cop-out rather than explaining content",
        "Explain the technical mechanisms, tradeoffs, and findings substantively",
    ),
]


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root)).replace("\\", "/")
    except ValueError as exc:
        raise ValueError(f"path must be repository-local: {path}") from exc


def _safe_file(repo_root: Path, path: Path, label: str) -> Path:
    rel = _rel(repo_root, path)
    resolved = core.repo_local_path(repo_root, rel, label)
    if resolved.is_symlink() or not resolved.is_file():
        raise ValueError(f"{label} missing or unsafe: {rel}")
    return resolved


def mask_tex_comments_and_structural_macros(source_text: str) -> tuple[str, list[str]]:
    """Mask TeX comments and purely structural non-reader commands.

    Preserves exact offsets, line breaks, section/subsection titles, kickers,
    and visible paragraph/body text. Masks out LaTeX macro declarations that
    contain internal technical keys (e.g. \\label{pkg:...}, \\cite{...},
    \\Needspace{...}, \\usepackage{...}, \\input{...}) so citation keys and
    cross-reference labels do not trigger false positive lexical matches,
    while scanning all visible reader prose.
    """
    # 1. Mask % comments
    masked = list(fidelity._mask_tex_comments(source_text))

    text = "".join(masked)
    # 2. Mask purely structural non-reader commands
    structural_patterns = [
        re.compile(r"\\label\{[^{}]*\}"),
        re.compile(r"\\(?:auto|text|paren)?cite\w*\{[^{}]*\}"),
        re.compile(r"\\Needspace\{[^{}]*\}"),
        re.compile(r"\\documentclass(?:\[[^\]]*\])?\{[^{}]*\}"),
        re.compile(r"\\usepackage(?:\[[^\]]*\])?\{[^{}]*\}"),
        re.compile(r"\\bibliography\{[^{}]*\}"),
        re.compile(r"\\addbibresource\{[^{}]*\}"),
        re.compile(r"\\input\{[^{}]*\}"),
        re.compile(r"\\include\{[^{}]*\}"),
        re.compile(r"\\pagestyle\{[^{}]*\}"),
        re.compile(r"\\thispagestyle\{[^{}]*\}"),
        re.compile(r"\\bibliographystyle\{[^{}]*\}"),
        re.compile(r"\\ref\{[^{}]*\}"),
        re.compile(r"\\pageref\{[^{}]*\}"),
    ]

    for pat in structural_patterns:
        for match in pat.finditer(text):
            start, end = match.span()
            for i in range(start, end):
                if masked[i] not in "\r\n":
                    masked[i] = " "

    result = "".join(masked)
    lines = result.splitlines(keepends=True)
    return result, lines


def _is_suppressed(
    suppressions: list[dict[str, Any]],
    rule_id: str,
    path: str,
    matched_text: str,
) -> tuple[bool, str]:
    for sup in suppressions:
        if not isinstance(sup, dict):
            continue
        if sup.get("rule_id") == rule_id and sup.get("path") == path:
            target = sup.get("matched_text", "")
            if target and (target in matched_text or matched_text in target):
                reason = sup.get("reason", "").strip()
                if reason:
                    return True, reason
    return False, ""


def scan_reader_text_lines(
    lines: list[str],
    artifact_label: str,
    path_str: str,
    suppressions: list[dict[str, Any]] | None = None,
    block_context: str | None = None,
) -> list[SurfaceFinding]:
    """Scan line-split reader text for lexical lint violations."""
    active_suppressions = suppressions or []
    findings: list[SurfaceFinding] = []
    finding_counter = 0

    current_block = block_context or "body"

    for line_idx, line in enumerate(lines, start=1):
        # Update current block context if heading is detected
        heading_match = re.search(r"\\(?:section|subsection|subsubsection)\*?\{([^}]+)\}", line)
        if heading_match:
            current_block = heading_match.group(1).strip()

        for rule_id, pattern, default_reason, norm_hint in LEXICAL_PATTERNS:
            for match in pattern.finditer(line):
                matched_span = match.group(0)
                finding_counter += 1
                fid = f"{rule_id}-{path_str}-{line_idx}-{finding_counter}"

                suppressed, sup_reason = _is_suppressed(
                    active_suppressions, rule_id, path_str, matched_span
                )

                if suppressed:
                    findings.append(
                        SurfaceFinding(
                            finding_id=fid,
                            rule_id=rule_id,
                            artifact=artifact_label,
                            path=path_str,
                            field_or_block=current_block,
                            locator=f"Line {line_idx}",
                            text_span=matched_span,
                            severity="SUPPRESSED",
                            reason=f"Suppressed: {sup_reason}",
                            proposed_normalization=norm_hint,
                            disposition="SUPPRESSED",
                        )
                    )
                else:
                    findings.append(
                        SurfaceFinding(
                            finding_id=fid,
                            rule_id=rule_id,
                            artifact=artifact_label,
                            path=path_str,
                            field_or_block=current_block,
                            locator=f"Line {line_idx}",
                            text_span=matched_span,
                            severity="BLOCKING",
                            reason=default_reason,
                            proposed_normalization=norm_hint,
                            disposition="UNRESOLVED",
                        )
                    )
    return findings


def scan_tex_file(
    repo_root: Path,
    file_path: Path,
    suppressions: list[dict[str, Any]] | None = None,
    artifact_label: str = "TeX Source",
) -> list[SurfaceFinding]:
    """Scan one TeX source file for reader-surface leakage."""
    resolved = _safe_file(repo_root, file_path, artifact_label)
    rel_path = _rel(repo_root, resolved)
    text = resolved.read_text(encoding="utf-8")
    _, lines = mask_tex_comments_and_structural_macros(text)
    return scan_reader_text_lines(
        lines, artifact_label, rel_path, suppressions=suppressions
    )


def scan_bib_file(
    repo_root: Path,
    file_path: Path,
    suppressions: list[dict[str, Any]] | None = None,
    artifact_label: str = "Bibliography",
) -> list[SurfaceFinding]:
    """Scan a BibTeX bibliography file for leaked evidence metadata."""
    resolved = _safe_file(repo_root, file_path, artifact_label)
    rel_path = _rel(repo_root, resolved)
    text = resolved.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    active_suppressions = suppressions or []
    findings: list[SurfaceFinding] = []
    finding_counter = 0

    entry_key = "preamble"
    for line_idx, line in enumerate(lines, start=1):
        # Detect @entry{key,
        entry_match = re.search(r"@\w+\s*\{\s*([^,]+),", line)
        if entry_match:
            entry_key = entry_match.group(1).strip()

        # Check all lexical patterns against bibliography lines
        for rule_id, pattern, default_reason, norm_hint in LEXICAL_PATTERNS:
            for match in pattern.finditer(line):
                matched_span = match.group(0)
                finding_counter += 1
                fid = f"{rule_id}-{rel_path}-{line_idx}-{finding_counter}"

                suppressed, sup_reason = _is_suppressed(
                    active_suppressions, rule_id, rel_path, matched_span
                )

                if suppressed:
                    findings.append(
                        SurfaceFinding(
                            finding_id=fid,
                            rule_id=rule_id,
                            artifact=artifact_label,
                            path=rel_path,
                            field_or_block=f"entry:{entry_key}",
                            locator=f"Line {line_idx}",
                            text_span=matched_span,
                            severity="SUPPRESSED",
                            reason=f"Suppressed: {sup_reason}",
                            proposed_normalization=norm_hint,
                            disposition="SUPPRESSED",
                        )
                    )
                else:
                    findings.append(
                        SurfaceFinding(
                            finding_id=fid,
                            rule_id=rule_id,
                            artifact=artifact_label,
                            path=rel_path,
                            field_or_block=f"entry:{entry_key}",
                            locator=f"Line {line_idx}",
                            text_span=matched_span,
                            severity="BLOCKING",
                            reason=default_reason,
                            proposed_normalization=norm_hint,
                            disposition="UNRESOLVED",
                        )
                    )
    return findings


def scan_publication_payload(
    payload: dict[str, Any],
    source_path_str: str,
    suppressions: list[dict[str, Any]] | None = None,
) -> list[SurfaceFinding]:
    """Scan publication_payload text fields in Profile Synthesis."""
    findings: list[SurfaceFinding] = []
    finding_counter = 0
    active_suppressions = suppressions or []

    def _walk(obj: Any, prefix: str) -> None:
        nonlocal finding_counter
        if isinstance(obj, str):
            for rule_id, pattern, default_reason, norm_hint in LEXICAL_PATTERNS:
                for match in pattern.finditer(obj):
                    matched_span = match.group(0)
                    finding_counter += 1
                    fid = f"{rule_id}-synthesis-{prefix}-{finding_counter}"
                    suppressed, sup_reason = _is_suppressed(
                        active_suppressions, rule_id, source_path_str, matched_span
                    )
                    findings.append(
                        SurfaceFinding(
                            finding_id=fid,
                            rule_id=rule_id,
                            artifact="Profile Synthesis Result",
                            path=source_path_str,
                            field_or_block=prefix,
                            locator=prefix,
                            text_span=matched_span,
                            severity="SUPPRESSED" if suppressed else "BLOCKING",
                            reason=f"Suppressed: {sup_reason}" if suppressed else default_reason,
                            proposed_normalization=norm_hint,
                            disposition="SUPPRESSED" if suppressed else "UNRESOLVED",
                        )
                    )
        elif isinstance(obj, dict):
            for k, v in obj.items():
                _walk(v, f"{prefix}.{k}" if prefix else k)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                _walk(item, f"{prefix}[{idx}]")

    _walk(payload, "publication_payload")
    return findings


def evaluate_reader_surface_gate(
    repo_root: Path,
    manuscript_path: Path,
    *,
    suppressions: list[dict[str, Any]] | None = None,
    semantic_review_findings: list[dict[str, Any]] | None = None,
    synthesis_result_path: Path | None = None,
    evaluated_by: str = "Core v2 Pre-Publication Reader-Surface Gate",
    recorded_at: datetime | None = None,
    output_path: Path | None = None,
) -> dict[str, Any]:
    """Evaluate Pre-Publication Reader-Surface Gate for a reader manuscript.

    Scans all declared reader-facing source files, bibliography, synthesis
    publication payload, and manifest details. Evaluates lexical lint and
    semantic review findings, applies suppressions, and returns a structured
    gate report conforming to schemas/reader-surface-gate-v2.schema.json.
    """
    ts = recorded_at or datetime.now(timezone.utc)
    m_file = _safe_file(repo_root, manuscript_path, "Reader Manuscript Manifest")
    manuscript = schema_gate.load_and_validate_json(
        m_file, repo_root / MANUSCRIPT_SCHEMA, label="Reader Manuscript Manifest"
    )

    active_suppressions = list(suppressions or [])
    all_findings: list[SurfaceFinding] = []
    scanned_surfaces: list[dict[str, Any]] = []

    # 1. Primary Source
    primary_ref = manuscript["primary_source"]
    primary_path = core.repo_local_path(repo_root, primary_ref["path"], "primary source")
    scanned_surfaces.append(
        {
            "path": primary_ref["path"],
            "sha256": primary_ref["sha256"],
            "kind": "PRIMARY_SOURCE",
            "byte_count": primary_path.stat().st_size,
        }
    )
    primary_findings = scan_tex_file(
        repo_root, primary_path, suppressions=active_suppressions, artifact_label="Primary Source"
    )
    all_findings.extend(primary_findings)

    # 2. Supporting Files
    for support_ref in manuscript.get("supporting_files", []):
        support_path = core.repo_local_path(repo_root, support_ref["path"], "supporting file")
        role = support_ref.get("role")
        kind_label = (
            "BIBLIOGRAPHY"
            if role == "BIBLIOGRAPHY"
            else "SUPPORTING_SOURCE"
        )
        scanned_surfaces.append(
            {
                "path": support_ref["path"],
                "sha256": support_ref["sha256"],
                "kind": kind_label,
                "byte_count": support_path.stat().st_size,
            }
        )
        if role == "BIBLIOGRAPHY":
            bib_findings = scan_bib_file(
                repo_root,
                support_path,
                suppressions=active_suppressions,
                artifact_label=f"Supporting {role}",
            )
            all_findings.extend(bib_findings)
        elif role == "SUPPORTING_SOURCE" and support_path.suffix == ".tex":
            supp_findings = scan_tex_file(
                repo_root,
                support_path,
                suppressions=active_suppressions,
                artifact_label=f"Supporting Source ({support_ref['path']})",
            )
            all_findings.extend(supp_findings)

    # 3. Manuscript Manifest Details (coverage detail fields)
    m_rel = _rel(repo_root, m_file)
    scanned_surfaces.append(
        {
            "path": m_rel,
            "sha256": core.sha256_file(m_file),
            "kind": "MANUSCRIPT_MANIFEST",
            "byte_count": m_file.stat().st_size,
        }
    )
    for idx, cov in enumerate(manuscript.get("architecture_coverage", [])):
        detail_text = cov.get("detail", "")
        pkg = cov.get("package_id", "")
        req = cov.get("requirement", "")
        lines = [detail_text]
        cov_findings = scan_reader_text_lines(
            lines,
            "Architecture Coverage Detail",
            m_rel,
            suppressions=active_suppressions,
            block_context=f"coverage:{pkg}/{req}",
        )
        all_findings.extend(cov_findings)

    # 4. Optional Synthesis Result publication_payload
    if synthesis_result_path is not None and synthesis_result_path.is_file():
        syn_data = core.load_json(synthesis_result_path)
        pub_payload = syn_data.get("publication_payload")
        syn_rel = _rel(repo_root, synthesis_result_path)
        if isinstance(pub_payload, dict) and pub_payload:
            scanned_surfaces.append(
                {
                    "path": syn_rel,
                    "sha256": core.sha256_file(synthesis_result_path),
                    "kind": "SYNTHESIS_PAYLOAD",
                    "byte_count": synthesis_result_path.stat().st_size,
                }
            )
            syn_findings = scan_publication_payload(
                pub_payload, syn_rel, suppressions=active_suppressions
            )
            all_findings.extend(syn_findings)

    # 5. Semantic Review Findings (Layer 2)
    if semantic_review_findings:
        for idx, sem in enumerate(semantic_review_findings):
            if not isinstance(sem, dict):
                continue
            fid = sem.get("finding_id") or f"RSG-SEM-PROCESS-LEAKAGE-{idx+1}"
            rule_id = sem.get("rule_id", "RSG-SEM-PROCESS-LEAKAGE")
            path_str = sem.get("path", m_rel)
            span = sem.get("text_span", "")
            suppressed, sup_reason = _is_suppressed(
                active_suppressions, rule_id, path_str, span
            )
            sev = sem.get("severity", "BLOCKING")
            disp = sem.get("disposition", "UNRESOLVED")
            if suppressed:
                sev = "SUPPRESSED"
                disp = "SUPPRESSED"

            all_findings.append(
                SurfaceFinding(
                    finding_id=fid,
                    rule_id=rule_id,
                    artifact=sem.get("artifact", "Semantic Review"),
                    path=path_str,
                    field_or_block=sem.get("field_or_block", "semantic-review"),
                    locator=sem.get("locator", f"Finding {idx+1}"),
                    text_span=span,
                    severity=sev,
                    reason=f"Suppressed: {sup_reason}" if suppressed else sem.get("reason", "Requires internal pipeline knowledge"),
                    proposed_normalization=sem.get("proposed_normalization", "Rewrite into reader-facing domain prose"),
                    disposition=disp,
                )
            )

    # Summary calculation
    blocking_count = sum(
        1 for f in all_findings if f.severity == "BLOCKING" and f.disposition == "UNRESOLVED"
    )
    warning_count = sum(
        1 for f in all_findings if f.severity == "WARNING" and f.disposition == "UNRESOLVED"
    )
    suppressed_count = sum(
        1 for f in all_findings if f.disposition == "SUPPRESSED"
    )
    normalized_count = sum(
        1 for f in all_findings if f.disposition == "NORMALIZED"
    )

    verdict = "PASSED" if blocking_count == 0 else "FAILED"

    rules_checked_dicts = [asdict(r) for r in RULES]

    base: dict[str, Any] = {
        "schema_version": "2.0-rc1",
        "issue_id": manuscript["issue_id"],
        "publication_profile": manuscript["publication_profile"],
        "status": verdict,
        "scanned_surfaces": scanned_surfaces,
        "rules_checked": rules_checked_dicts,
        "suppressions": active_suppressions,
        "findings": [f.to_dict() for f in all_findings],
        "summary": {
            "total_findings": len(all_findings),
            "blocking_findings": blocking_count,
            "warning_findings": warning_count,
            "suppressed_findings": suppressed_count,
            "normalized_findings": normalized_count,
            "verdict": verdict,
        },
        "evaluated_by": evaluated_by,
        "recorded_at": core.iso_utc(ts),
    }

    report = dict(base)
    report["gate_sha256"] = core.sha256_object(base)

    schema_gate.validate_instance(
        report, repo_root / SURFACE_GATE_SCHEMA, label="Reader-Surface Gate Record"
    )

    if output_path is not None:
        core.write_json(output_path, report)

    return report


def validate_manuscript_surface(
    repo_root: Path,
    manuscript: dict[str, Any],
    suppressions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Fail-fast reader surface validation for a validated manuscript manifest.

    Scans the primary source and all supporting files. Raises ValueError with
    complete finding details if any unresolved blocking findings exist.
    """
    active_suppressions = list(suppressions or [])
    all_findings: list[SurfaceFinding] = []

    # Primary source
    primary_ref = manuscript["primary_source"]
    primary_path = core.repo_local_path(repo_root, primary_ref["path"], "primary source")
    primary_findings = scan_tex_file(
        repo_root, primary_path, suppressions=active_suppressions, artifact_label="Primary Source"
    )
    all_findings.extend(primary_findings)

    # Supporting files
    for support_ref in manuscript.get("supporting_files", []):
        support_path = core.repo_local_path(repo_root, support_ref["path"], "supporting file")
        role = support_ref.get("role")
        if role == "BIBLIOGRAPHY":
            bib_findings = scan_bib_file(
                repo_root,
                support_path,
                suppressions=active_suppressions,
                artifact_label=f"Supporting {role}",
            )
            all_findings.extend(bib_findings)
        elif role == "SUPPORTING_SOURCE" and support_path.suffix == ".tex":
            supp_findings = scan_tex_file(
                repo_root,
                support_path,
                suppressions=active_suppressions,
                artifact_label=f"Supporting Source ({support_ref['path']})",
            )
            all_findings.extend(supp_findings)

    # Coverage detail
    for cov in manuscript.get("architecture_coverage", []):
        detail = cov.get("detail", "")
        pkg = cov.get("package_id", "")
        req = cov.get("requirement", "")
        findings = scan_reader_text_lines(
            [detail],
            "Architecture Coverage Detail",
            manuscript.get("production_profile", {}).get("path", "manifest"),
            suppressions=active_suppressions,
            block_context=f"coverage:{pkg}/{req}",
        )
        all_findings.extend(findings)

    blocking = [
        f for f in all_findings
        if f.severity == "BLOCKING" and f.disposition == "UNRESOLVED"
    ]

    if blocking:
        lines = [
            f"Pre-Publication Reader-Surface Gate FAILED: {len(blocking)} blocking finding(s) detected:"
        ]
        for idx, f in enumerate(blocking, start=1):
            lines.append(
                f"  [{idx}] {f.rule_id} at {f.path} ({f.locator}, {f.field_or_block}): "
                f"leaked {f.text_span!r} - {f.reason}. Normalization: {f.proposed_normalization}"
            )
        raise ValueError("\n".join(lines))

    return {
        "status": "PASSED",
        "total_findings": len(all_findings),
        "blocking_findings": 0,
        "suppressed_findings": sum(1 for f in all_findings if f.disposition == "SUPPRESSED"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pre-Publication Reader-Surface Gate for Survey Production Core v2"
    )
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_m = sub.add_parser("scan-manuscript", help="Scan a reader manuscript manifest and its files")
    scan_m.add_argument("--manuscript", required=True, help="Path to reader-manuscript-v2.json")
    scan_m.add_argument("--suppressions", help="Path to suppressions JSON array")
    scan_m.add_argument("--semantic-review", help="Path to semantic review findings JSON array")
    scan_m.add_argument("--synthesis-result", help="Path to profile-synthesis-result.json")
    scan_m.add_argument("--output", help="Path to write reader-surface-gate-v2.json report")

    scan_f = sub.add_parser("scan-file", help="Scan an individual TeX or BibTeX file")
    scan_f.add_argument("--file", required=True, help="Path to TeX or BibTeX file")
    scan_f.add_argument("--suppressions", help="Path to suppressions JSON array")

    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()

    if args.command == "scan-file":
        target = Path(args.file)
        if not target.is_absolute():
            target = repo_root / target
        suppressions = []
        if args.suppressions:
            suppressions = core.load_json(Path(args.suppressions))

        if target.suffix == ".bib":
            findings = scan_bib_file(repo_root, target, suppressions=suppressions)
        else:
            findings = scan_tex_file(repo_root, target, suppressions=suppressions)

        blocking = [f for f in findings if f.severity == "BLOCKING" and f.disposition == "UNRESOLVED"]
        for f in findings:
            print(f"[{f.severity}] {f.rule_id} at {f.path}:{f.locator} ({f.field_or_block}) - {f.text_span!r}: {f.reason}")
        if blocking:
            print(f"FAILED: {len(blocking)} blocking findings")
            return 1
        print("PASSED: Zero blocking findings")
        return 0

    if args.command == "scan-manuscript":
        m_path = Path(args.manuscript)
        if not m_path.is_absolute():
            m_path = repo_root / m_path
        suppressions = []
        if args.suppressions:
            suppressions = core.load_json(Path(args.suppressions))
        sem_findings = []
        if args.semantic_review:
            sem_findings = core.load_json(Path(args.semantic_review))
        syn_path = None
        if args.synthesis_result:
            syn_path = Path(args.synthesis_result)
            if not syn_path.is_absolute():
                syn_path = repo_root / syn_path
        out_path = None
        if args.output:
            out_path = Path(args.output)
            if not out_path.is_absolute():
                out_path = repo_root / out_path

        report = evaluate_reader_surface_gate(
            repo_root,
            m_path,
            suppressions=suppressions,
            semantic_review_findings=sem_findings,
            synthesis_result_path=syn_path,
            output_path=out_path,
        )

        status = report["status"]
        summary = report["summary"]
        print(f"Reader-Surface Gate: {status}")
        print(f"  Total findings: {summary['total_findings']}")
        print(f"  Blocking: {summary['blocking_findings']}")
        print(f"  Suppressed: {summary['suppressed_findings']}")
        if status != "PASSED":
            for f in report["findings"]:
                if f["severity"] == "BLOCKING" and f["disposition"] == "UNRESOLVED":
                    print(f"  - [{f['rule_id']}] {f['path']}:{f['locator']} ({f['field_or_block']}): {f['text_span']!r} -> {f['reason']}")
            return 1
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
