#!/usr/bin/env python3
"""Materialize the bounded W34 Discovery gap-fill and its event crosswalk."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ISSUE_ID = "2026-W34"
EXECUTION_REL = "sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1"
ARXIV_TRIAGE_REL = f"{EXECUTION_REL}/arxiv-triage"
OFFICIAL_RAW_REL = (
    f"{EXECUTION_REL}/source-intake/official-fallback/sources/2026-W34/"
    "collectors/official-pages/runs/20260908T005152Z/raw"
)
ALIBABA_OBSERVATION = f"{EXECUTION_REL}/source-observations/alibaba-model-lifecycle-official-web.md"
OFFICIAL_OBSERVATION = f"{EXECUTION_REL}/source-observations/official-fallback-web-observations.md"
ARXIV_RAW_REL = (
    "sources/2026-W34/execution/luna/"
    "w34-architecture-r2-research-sufficiency-revision-r1/source-intake/"
    "sources/2026-W34/collectors/arxiv/runs/20260907T161121Z/raw"
)
ARXIV_RUN_ID = "arxiv-api-2026-W34-20260907T161121Z"
OFFICIAL_RUN_ID = "official-fallback-web-2026-W34-20260908T005152Z"
OBSERVED_AT = "2026-09-08T00:51:52Z"
OBLIGATIONS = ["weekly:current-relevance", "weekly:technical-significance"]


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}: expected object row")
            rows.append(value)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


def compact(text: str, limit: int = 900) -> str:
    value = " ".join(text.split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


def gap_record(
    *,
    discovery_id: str,
    title: str,
    source_type: str,
    collector_id: str,
    collector_run_id: str,
    locator: str,
    raw_paths: list[str],
    published_at: str | None,
    summary_text: str,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "discovery_id": discovery_id,
        "provenance": {
            "origin": "GAP_FILL",
            "research_pass": 3,
            "parent_refs": [],
            "obligation_ids": list(OBLIGATIONS),
            "reason": (
                "Fresh W34 source-first Discovery gap-fill lead. This record is retained "
                "for independent Sol completeness review; no Screening, Evidence, "
                "Materiality, Selection, or Architecture disposition is made."
            ),
        },
        "source": {
            "source_type": source_type,
            "collector_id": collector_id,
            "collector_run_id": collector_run_id,
            "observed_at": OBSERVED_AT,
            "title": title,
            "locator": locator,
            "raw_paths": raw_paths,
            "published_at": published_at,
            "summary_text": summary_text,
            "metadata": metadata,
        },
    }


def official_record(
    *,
    discovery_id: str,
    title: str,
    locator: str,
    published_at: str,
    summary_text: str,
    lane: str,
    provider: str,
    chronology_role: str,
    identity_action: str,
    reconciles_prior: list[str],
    raw_paths: list[str],
) -> dict[str, Any]:
    return gap_record(
        discovery_id=discovery_id,
        title=title,
        source_type="official_web_fallback_observation",
        collector_id="official-web-fallback",
        collector_run_id=OFFICIAL_RUN_ID,
        locator=locator,
        raw_paths=raw_paths,
        published_at=published_at,
        summary_text=summary_text,
        metadata={
            "authority_class": "DISCOVERY_SOURCE_ONLY",
            "discovery_only": True,
            "fresh_refresh": EXECUTION_REL.rsplit("/", 1)[-1],
            "provider": provider,
            "lane": lane,
            "chronology_role": chronology_role,
            "chronology_precision": "DATE_ONLY_FIRST_PARTY_FALLBACK_OBSERVATION",
            "identity_action": identity_action,
            "reconciles_prior_event_ids": reconciles_prior,
            "selection_not_performed": True,
            "technical_claims_accepted": False,
            "exact_http_body_captured_by_repo_collector": False,
            "window_utc": "[2026-08-14T22:00:00Z, 2026-08-21T22:00:00Z)",
            "window_relation_observation": "IN_WINDOW_DATE_CANDIDATE",
        },
    )


def arxiv_record(row: dict[str, Any], raw_path: str) -> dict[str, Any]:
    arxiv_id = row["arxiv_id"]
    discovery_id = "w34-gapfill-arxiv-triage-" + re.sub(r"[^a-zA-Z0-9]+", "-", arxiv_id).strip("-")
    return gap_record(
        discovery_id=discovery_id,
        title=row["title"],
        source_type="arxiv_atom_snapshot",
        collector_id="arxiv-api",
        collector_run_id=ARXIV_RUN_ID,
        locator=row["source_locator"],
        raw_paths=[raw_path],
        published_at=row["published"],
        summary_text=(
            f"Abstract-level arXiv Discovery lead ({arxiv_id}) in lane "
            f"{row['candidate_technical_lane']}. {row['relevance_rationale']} "
            f"Abstract excerpt: {compact(row['abstract_excerpt'], 650)}"
        ),
        metadata={
            "authority_class": "DISCOVERY_SOURCE_ONLY",
            "discovery_only": True,
            "fresh_refresh": EXECUTION_REL.rsplit("/", 1)[-1],
            "provider": "arXiv",
            "lane": row["candidate_technical_lane"],
            "chronology_precision": "EXACT_PUBLISHED_IN_ATOM_SNAPSHOT",
            "arxiv_id": arxiv_id,
            "categories": row["categories"],
            "primary_category": row["primary_category"],
            "updated_at": row["updated"],
            "deterministic_prefilter_hit": row["deterministic_prefilter_hit"],
            "deterministic_score": row["deterministic_score"],
            "matched_term_groups": row["matched_term_groups"],
            "triage_bucket": row["triage_bucket"],
            "duplicate_relationship": row["duplicate_relationship"],
            "iterative_evidence_priority": True,
            "selection_not_performed": True,
            "technical_claims_accepted": False,
            "window_utc": "[2026-08-14T22:00:00Z, 2026-08-21T22:00:00Z)",
            "window_relation_observation": "IN_WINDOW_DATE_CANDIDATE",
        },
    )


def parse_prior_inventory(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not re.match(r"^\| W34-C\d{3} \|", line):
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        if len(cells) < 6:
            raise ValueError(f"prior inventory row has too few cells: {line}")
        event_id, event, lane, status, sources, notes = cells[:6]
        classification = "UNCHANGED_BASELINE"
        target: list[str] = []
        if event_id in {"W34-C001", "W34-C039"}:
            classification = "CHRONOLOGY_CORRECTED_OR_REFINED"
        if event_id == "W34-C072":
            classification = "SPLIT_PARENT_LATER_INTEGRATION_RETAINED"
        if event_id in {"W34-C010", "W34-C034", "W34-C099", "W34-C100", "W34-C101"}:
            classification = "UNCHANGED_WITH_OFFICIAL_FALLBACK_DUPLICATE"
        if event_id in {"W34-C023", "W34-C024", "W34-C025", "W34-C042"}:
            classification = "UNCHANGED_WITH_XAI_FALLBACK_RECHECK"
        if "BOUNDARY_PRE_WINDOW" in status:
            boundary = "PRE_WINDOW"
        elif "BOUNDARY_POST_CUTOFF" in status:
            boundary = "POST_CUTOFF"
        else:
            boundary = "IN_WINDOW_OR_UNRESOLVED"
        rows.append(
            {
                "row_id": event_id,
                "event_identity": event_id,
                "record_kind": "PRIOR_105_EVENT",
                "classification": classification,
                "boundary": boundary,
                "event": event,
                "lane": lane,
                "prior_discovery_status": status,
                "source_layers": sources,
                "notes": notes,
                "source_trace": "sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md",
                "merged_into": target,
            }
        )
    if len(rows) != 105:
        raise ValueError(f"prior event inventory parsed {len(rows)} rows, expected 105")
    return rows


def prior_refresh_rows(prior_graph: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in prior_graph:
        if record.get("provenance", {}).get("research_pass") != 2:
            continue
        source = record["source"]
        rows.append(
            {
                "row_id": "PRIOR-REFRESH-" + record["discovery_id"],
                "event_identity": record["discovery_id"],
                "record_kind": "PRIOR_REFRESH_LEAD",
                "classification": "UNCHANGED_PRIOR_REFRESH",
                "boundary": "IN_WINDOW_OR_UNRESOLVED",
                "event": source.get("title"),
                "lane": source.get("metadata", {}).get("lane"),
                "prior_discovery_status": "PRIOR_REFRESH_LEAD",
                "source_layers": source.get("source_type"),
                "notes": source.get("summary_text"),
                "source_trace": record["discovery_id"],
                "merged_into": [],
            }
        )
    if len(rows) != 15:
        raise ValueError(f"prior refresh leads parsed {len(rows)} rows, expected 15")
    return rows


def official_inventory_rows() -> list[dict[str, Any]]:
    return [
        {
            "row_id": "W34-GAP-ALIBABA-WAN30-MODEL-STUDIO",
            "event_identity": "W34-GAP-ALIBABA-WAN30-MODEL-STUDIO",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "NEW_SPLIT_CHILD",
            "boundary": "IN_WINDOW",
            "event": "Alibaba Model Studio wan3.0-video-prime lifecycle/availability",
            "lane": "model provider / video service availability",
            "prior_discovery_status": None,
            "source_layers": ALIBABA_OBSERVATION,
            "notes": "Separate in-window Model Studio service row from later Runway Wan integration.",
            "source_trace": "w34-gapfill-alibaba-wan30-model-studio",
            "merged_into": [],
            "split_from": ["W34-C072"],
        },
        {
            "row_id": "W34-GAP-ALIBABA-KIMI-K3-MODEL-STUDIO",
            "event_identity": "W34-GAP-ALIBABA-KIMI-K3-MODEL-STUDIO",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "NEW",
            "boundary": "IN_WINDOW",
            "event": "Alibaba Model Studio kimi-k3 lifecycle/availability",
            "lane": "model provider / service distribution",
            "prior_discovery_status": None,
            "source_layers": ALIBABA_OBSERVATION,
            "notes": "Provider lifecycle row not represented by a prior event-equivalent record.",
            "source_trace": "w34-gapfill-alibaba-kimi-k3-model-studio",
            "merged_into": [],
        },
        {
            "row_id": "W34-GAP-ALIBABA-QWEN38-MODEL-STUDIO",
            "event_identity": "W34-C039",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE_CHRONOLOGY_REFINEMENT",
            "boundary": "IN_WINDOW",
            "event": "Alibaba Model Studio qwen3.8-27b lifecycle/availability",
            "lane": "model provider / service distribution",
            "prior_discovery_status": None,
            "source_layers": ALIBABA_OBSERVATION,
            "notes": "Merge into W34-C039 as a provider/service chronology refinement; do not create a second story.",
            "source_trace": "w34-gapfill-alibaba-qwen38-model-studio",
            "merged_into": ["W34-C039"],
        },
        {
            "row_id": "W34-GAP-ALIBABA-GLM53-MODEL-STUDIO",
            "event_identity": "W34-C001",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE_CHRONOLOGY_REFINEMENT",
            "boundary": "IN_WINDOW",
            "event": "Alibaba Model Studio ZHIPU/GLM-5.3 lifecycle/availability",
            "lane": "model provider / service distribution",
            "prior_discovery_status": None,
            "source_layers": ALIBABA_OBSERVATION,
            "notes": "Merge into W34-C001 as provider/service chronology; keep base release and distribution distinct.",
            "source_trace": "w34-gapfill-alibaba-glm53-model-studio",
            "merged_into": ["W34-C001"],
        },
        {
            "row_id": "W34-GAP-AWS-AGENTCORE-MEMORY-JSON",
            "event_identity": "W34-GAP-AWS-AGENTCORE-MEMORY-JSON",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "NEW",
            "boundary": "IN_WINDOW",
            "event": "Amazon Bedrock AgentCore Memory accepts non-conversational JSON payloads",
            "lane": "agent infrastructure / memory",
            "prior_discovery_status": None,
            "source_layers": OFFICIAL_OBSERVATION,
            "notes": "Distinct Aug 20 AgentCore capability event; no downstream significance judgment.",
            "source_trace": "w34-gapfill-aws-agentcore-memory-json",
            "merged_into": [],
        },
        {
            "row_id": "W34-GAP-AWS-AGENTCORE-PAYMENTS",
            "event_identity": "W34-C010",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE",
            "boundary": "IN_WINDOW",
            "event": "AgentCore payments GA",
            "lane": "agent infrastructure / payments",
            "prior_discovery_status": None,
            "source_layers": OFFICIAL_OBSERVATION,
            "notes": "Direct fallback confirms the existing W34-C010 identity; no new event row.",
            "source_trace": "w34-gapfill-aws-agentcore-payments",
            "merged_into": ["W34-C010"],
        },
        {
            "row_id": "W34-GAP-AWS-AGENTCORE-WEB-SEARCH-FILTERS",
            "event_identity": "W34-C034",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE",
            "boundary": "IN_WINDOW",
            "event": "AgentCore Web Search domain/date filters",
            "lane": "agent infrastructure / retrieval control",
            "prior_discovery_status": None,
            "source_layers": OFFICIAL_OBSERVATION,
            "notes": "Direct fallback confirms the existing W34-C034 identity; no new event row.",
            "source_trace": "w34-gapfill-aws-agentcore-web-search-filters",
            "merged_into": ["W34-C034"],
        },
        {
            "row_id": "W34-GAP-GITHUB-COPILOT-JETBRAINS",
            "event_identity": "W34-C099",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE",
            "boundary": "IN_WINDOW",
            "event": "GitHub Copilot enterprise-managed settings for JetBrains",
            "lane": "developer tooling / agent governance",
            "prior_discovery_status": None,
            "source_layers": f"{OFFICIAL_RAW_REL}/github-copilot-jetbrains-fallback.html",
            "notes": "Exact official fallback page matches existing W34-C099.",
            "source_trace": "w34-gapfill-github-copilot-jetbrains",
            "merged_into": ["W34-C099"],
        },
        {
            "row_id": "W34-GAP-GITHUB-COPILOT-SLACK",
            "event_identity": "W34-C100",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE",
            "boundary": "IN_WINDOW",
            "event": "GitHub Copilot experience in Slack",
            "lane": "developer tooling / collaboration",
            "prior_discovery_status": None,
            "source_layers": f"{OFFICIAL_RAW_REL}/github-copilot-slack-fallback.html",
            "notes": "Exact official fallback page matches existing W34-C100.",
            "source_trace": "w34-gapfill-github-copilot-slack",
            "merged_into": ["W34-C100"],
        },
        {
            "row_id": "W34-GAP-GITHUB-COPILOT-TEAMS",
            "event_identity": "W34-C101",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE",
            "boundary": "IN_WINDOW",
            "event": "GitHub Copilot shared agentic work in Microsoft Teams",
            "lane": "developer tooling / collaboration",
            "prior_discovery_status": None,
            "source_layers": f"{OFFICIAL_RAW_REL}/github-copilot-teams-fallback.html",
            "notes": "Exact official fallback page matches existing W34-C101.",
            "source_trace": "w34-gapfill-github-copilot-teams",
            "merged_into": ["W34-C101"],
        },
        {
            "row_id": "W34-OBS-XAI-GROK46-PREWINDOW",
            "event_identity": "W34-C042",
            "record_kind": "CURRENT_OFFICIAL_FALLBACK",
            "classification": "MERGED_DUPLICATE_BOUNDARY_REFINEMENT",
            "boundary": "PRE_WINDOW",
            "event": "xAI Grok 4.6 base launch chronology",
            "lane": "model provider / base release",
            "prior_discovery_status": None,
            "source_layers": f"{OFFICIAL_RAW_REL}/xai-grok-46-fallback.html",
            "notes": "Official page dated Aug 12 is pre-window; keep W34 integrations/distribution deltas separate.",
            "source_trace": "xai-grok-46-fallback",
            "merged_into": ["W34-C042"],
        },
    ]


def arxiv_inventory_rows(shortlist: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in shortlist:
        duplicate = row.get("duplicate_relationship")
        discovery_id = "w34-gapfill-arxiv-triage-" + re.sub(r"[^a-zA-Z0-9]+", "-", row["arxiv_id"]).strip("-")
        rows.append(
            {
                "row_id": "ARXIV-" + row["arxiv_id"],
                "event_identity": duplicate or discovery_id,
                "record_kind": "CURRENT_ARXIV_SEMANTIC_SHORTLIST",
                "classification": "MERGED_DUPLICATE" if duplicate else "NEW",
                "boundary": row["boundary"],
                "event": row["title"],
                "lane": row["candidate_technical_lane"],
                "prior_discovery_status": None,
                "source_layers": row["source_locator"],
                "notes": row["relevance_rationale"],
                "source_trace": f"{ARXIV_TRIAGE_REL}/arxiv-semantic-shortlist.jsonl#{row['arxiv_id']}",
                "merged_into": [duplicate] if duplicate else [],
                "arxiv_id": row["arxiv_id"],
                "published": row["published"],
                "categories": row["categories"],
                "deterministic_score": row["deterministic_score"],
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--prior-discovery", required=True)
    parser.add_argument("--prior-inventory", required=True)
    parser.add_argument("--triage-shortlist", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    prior_path = root / args.prior_discovery
    prior_inventory_path = root / args.prior_inventory
    shortlist_path = root / args.triage_shortlist
    output_root = root / args.output_root
    if output_root.exists():
        existing = [path for path in output_root.iterdir() if path.name != "fresh-discovery-v3.jsonl"]
        if existing:
            raise ValueError(f"refusing to overwrite non-empty materialization output root: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)

    prior_graph = read_jsonl(prior_path)
    shortlist = read_jsonl(shortlist_path)
    prior_ids = {str(row.get("discovery_id")) for row in prior_graph}
    new_shortlist = [row for row in shortlist if not row.get("duplicate_relationship")]
    records: list[dict[str, Any]] = []

    alibaba_raw = root / ALIBABA_OBSERVATION
    official_observation_raw = root / OFFICIAL_OBSERVATION
    for path in (alibaba_raw, official_observation_raw):
        if not path.is_file():
            raise ValueError(f"required fallback observation is missing: {path}")
    records.extend(
        [
            official_record(
                discovery_id="w34-gapfill-alibaba-wan30-model-studio",
                title="Alibaba Model Studio wan3.0-video-prime lifecycle/availability",
                locator="https://www.alibabacloud.com/help/en/model-studio/newly-released-models",
                published_at="2026-08-20",
                summary_text=(
                    "Alibaba's official Model Studio lifecycle table shows wan3.0-video-prime "
                    "on 2026-08-20. This is a provider/service availability lead and is "
                    "kept separate from the later Runway Wan integration."
                ),
                lane="model provider / video service availability",
                provider="Alibaba Cloud / Model Studio",
                chronology_role="PROVIDER_SERVICE_AVAILABILITY",
                identity_action="NEW_SPLIT_CHILD_FROM_LATER_RUNWAY_EVENT",
                reconciles_prior=["W34-C072"],
                raw_paths=[ALIBABA_OBSERVATION],
            ),
            official_record(
                discovery_id="w34-gapfill-alibaba-kimi-k3-model-studio",
                title="Alibaba Model Studio kimi-k3 lifecycle/availability",
                locator="https://www.alibabacloud.com/help/en/model-studio/newly-released-models",
                published_at="2026-08-19",
                summary_text=(
                    "Alibaba's official Model Studio lifecycle table shows kimi-k3 on "
                    "2026-08-19. The row is retained as a distinct provider/service "
                    "availability Discovery lead for Sol review."
                ),
                lane="model provider / service distribution",
                provider="Alibaba Cloud / Model Studio",
                chronology_role="PROVIDER_SERVICE_AVAILABILITY",
                identity_action="NEW_EVENT_IDENTITY",
                reconciles_prior=[],
                raw_paths=[ALIBABA_OBSERVATION],
            ),
            official_record(
                discovery_id="w34-gapfill-aws-agentcore-memory-json",
                title="Amazon Bedrock AgentCore Memory accepts non-conversational JSON payloads",
                locator="https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-json-payloads/",
                published_at="2026-08-20",
                summary_text=(
                    "AWS's official What\'s New page dated Aug 20 describes AgentCore "
                    "Memory accepting structured non-conversational JSON payloads for "
                    "memory extraction. It is a distinct service capability lead."
                ),
                lane="agent infrastructure / memory",
                provider="AWS / Amazon Bedrock AgentCore",
                chronology_role="SERVICE_CAPABILITY_ANNOUNCEMENT",
                identity_action="NEW_EVENT_IDENTITY",
                reconciles_prior=[],
                raw_paths=[OFFICIAL_OBSERVATION],
            ),
        ]
    )
    records.extend(
        arxiv_record(
            row,
            f"{ARXIV_RAW_REL}/{row['source_raw_file']}",
        )
        for row in new_shortlist
    )
    new_ids = [row["discovery_id"] for row in records]
    if len(new_ids) != len(set(new_ids)) or set(new_ids) & prior_ids:
        raise ValueError("fresh Discovery IDs collide with prior graph")

    fresh_path = output_root / "fresh-discovery-v3.jsonl"
    prior_bytes = prior_path.read_bytes()
    if not prior_bytes.endswith(b"\n"):
        prior_bytes += b"\n"
    with fresh_path.open("wb") as handle:
        handle.write(prior_bytes)
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
            handle.write(b"\n")

    prior_event_rows = parse_prior_inventory(prior_inventory_path)
    prior_refresh = prior_refresh_rows(prior_graph)
    official_rows = official_inventory_rows()
    arxiv_rows = arxiv_inventory_rows(shortlist)
    inventory_rows = prior_event_rows + prior_refresh + official_rows + arxiv_rows
    inventory_path = output_root / "event-level-discovery-inventory-r1.jsonl"
    write_jsonl(inventory_path, inventory_rows)

    new_current = [row for row in inventory_rows if row["classification"] == "NEW"]
    new_split = [row for row in inventory_rows if row["classification"] == "NEW_SPLIT_CHILD"]
    merged = [row for row in inventory_rows if row["classification"].startswith("MERGED_DUPLICATE")]
    corrected = [row for row in inventory_rows if row["classification"] == "CHRONOLOGY_CORRECTED_OR_REFINED"]
    unique_count = 105 + 15 + len(new_current) + len(new_split)
    reconciliation = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "refresh": EXECUTION_REL.rsplit("/", 1)[-1],
        "prior_event_count": 105,
        "prior_canonical_graph_record_count": len(prior_graph),
        "prior_refresh_lead_count": len(prior_refresh),
        "current_arxiv_semantic_shortlist_count": len(shortlist),
        "current_arxiv_new_after_duplicate_merge_count": sum(1 for row in arxiv_rows if row["classification"] == "NEW"),
        "current_official_observation_row_count": len(official_rows),
        "inventory_row_count_including_merge_trace": len(inventory_rows),
        "revised_unique_event_count_after_merge": unique_count,
        "counts": {
            "added_new_event_rows": len(new_current) + len(new_split),
            "added_new_official_event_rows": sum(1 for row in official_rows if row["classification"] in {"NEW", "NEW_SPLIT_CHILD"}),
            "added_new_arxiv_event_rows": sum(1 for row in arxiv_rows if row["classification"] == "NEW"),
            "merged_duplicate_or_refinement_rows": len(merged),
            "split_event_identity_count": len(new_split),
            "chronology_corrected_or_refined_existing_count": len(corrected),
            "unchanged_prior_105_count": sum(1 for row in prior_event_rows if row["classification"] == "UNCHANGED_BASELINE"),
            "unchanged_prior_refresh_count": len(prior_refresh),
            "boundary_pre_window_observations": sum(1 for row in inventory_rows if row["boundary"] == "PRE_WINDOW"),
            "boundary_in_window_observations": sum(1 for row in inventory_rows if row["boundary"] == "IN_WINDOW"),
            "boundary_post_cutoff_observations": sum(1 for row in inventory_rows if row["boundary"] == "POST_CUTOFF"),
            "unresolved_chronology_observations": sum(1 for row in inventory_rows if row["boundary"] == "IN_WINDOW_OR_UNRESOLVED"),
        },
        "alibaba_reconciliation": {
            "wan3.0-video-prime": {"date": "2026-08-20", "action": "NEW_SPLIT_CHILD", "split_from": ["W34-C072"], "role": "MODEL_STUDIO_PROVIDER_SERVICE_AVAILABILITY"},
            "kimi-k3": {"date": "2026-08-19", "action": "NEW", "role": "MODEL_STUDIO_PROVIDER_SERVICE_AVAILABILITY"},
            "qwen3.8-27b": {"date": "2026-08-17", "action": "MERGED_DUPLICATE_CHRONOLOGY_REFINEMENT", "merged_into": ["W34-C039"], "role": "MODEL_STUDIO_PROVIDER_SERVICE_AVAILABILITY"},
            "ZHIPU/GLM-5.3": {"date": "2026-08-17", "action": "MERGED_DUPLICATE_CHRONOLOGY_REFINEMENT", "merged_into": ["W34-C001"], "role": "MODEL_STUDIO_PROVIDER_SERVICE_AVAILABILITY"},
        },
        "boundary_policy": "Discovery records preserve pre-window/in-window/post-cutoff and unresolved chronology; no out-of-window development is reinterpreted as in-window.",
        "downstream_disposition": "NOT_PERFORMED_SOL_DISCOVERY_REVIEW_R2_REQUIRED",
        "source_trace": {
            "prior_inventory": "sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md",
            "prior_refresh_graph": args.prior_discovery,
            "official_observations": [ALIBABA_OBSERVATION, OFFICIAL_OBSERVATION],
            "arxiv_triage": f"{ARXIV_TRIAGE_REL}/arxiv-semantic-shortlist.jsonl",
        },
    }
    write_json(output_root / "event-level-discovery-reconciliation.json", reconciliation)

    high_signal = [row for row in shortlist if row["deterministic_score"] >= 14]
    write_jsonl(output_root / "arxiv-high-signal-later-evidence.jsonl", high_signal)

    ledger = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "prior_graph_records": len(prior_graph),
        "fresh_graph_records": len(prior_graph) + len(records),
        "new_graph_records": len(records),
        "new_graph_official_records": 3,
        "new_graph_arxiv_records": len(new_shortlist),
        "arxiv_shortlist_records_reused_as_existing": len(shortlist) - len(new_shortlist),
        "fresh_discovery_path": str(fresh_path.relative_to(root)),
        "event_inventory_path": str(inventory_path.relative_to(root)),
        "reconciliation_path": str((output_root / "event-level-discovery-reconciliation.json").relative_to(root)),
        "high_signal_later_evidence_path": str((output_root / "arxiv-high-signal-later-evidence.jsonl").relative_to(root)),
        "screening_executed": False,
        "evidence_executed": False,
        "sol_discovery_review_required": True,
    }
    write_json(output_root / "fresh-discovery-ledger.json", ledger)
    write_json(output_root / "materialization-plan.json", {
        "issue_id": ISSUE_ID,
        "stage": "DISCOVERY_ONLY",
        "prior_discovery_preserved_as_exact_input": True,
        "new_records_are_gap_fill_or_research_shortlist": True,
        "downstream_stages": "NOT_EXECUTED",
        "canonical_acceptance_to_be_built_from": str(fresh_path.relative_to(root)),
    })
    print(json.dumps({"fresh_graph_records": len(prior_graph) + len(records), **reconciliation["counts"], "revised_unique_event_count": unique_count, "high_signal_arxiv_count": len(high_signal)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
