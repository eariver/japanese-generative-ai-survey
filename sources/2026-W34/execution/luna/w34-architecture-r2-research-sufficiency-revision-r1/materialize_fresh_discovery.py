#!/usr/bin/env python3
"""Materialize the W34 research-sufficiency Discovery refresh.

This is a bounded Discovery-only materializer.  It preserves the previous
canonical graph as input, derives new leads from the fresh Source Intake Raw
snapshots, and emits ordinary Core Discovery JSONL.  It deliberately does not
perform Screening, Evidence, Materiality, Selection, or Architecture work.
"""

from __future__ import annotations

import argparse
import json
import re
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


ISSUE_ID = "2026-W34"
EXECUTION_REL = (
    "sources/2026-W34/execution/luna/"
    "w34-architecture-r2-research-sufficiency-revision-r1"
)
SOURCE_INTAKE_REL = f"{EXECUTION_REL}/source-intake/sources/2026-W34/collectors"
OFFICIAL_RUN_ID = "official-pages-2026-W34-20260907T161655Z"
ARXIV_RUN_ID = "arxiv-api-2026-W34-20260907T161121Z"
OBSERVED_OFFICIAL = "2026-09-07T16:16:55Z"
OBSERVED_ARXIV = "2026-09-07T16:11:21Z"
OBLIGATIONS = ["weekly:current-relevance", "weekly:technical-significance"]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected JSON object")
        rows.append(value)
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            fh.write("\n")


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def official_path(filename: str) -> str:
    return f"{SOURCE_INTAKE_REL}/official-pages/runs/20260907T161655Z/raw/{filename}"


def arxiv_path(filename: str) -> str:
    return f"{SOURCE_INTAKE_REL}/arxiv/runs/20260907T161121Z/raw/{filename}"


def base_metadata(*, lane: str, provider: str, chronology_precision: str, refresh_note: str) -> dict[str, Any]:
    return {
        "authority_class": "DISCOVERY_SOURCE_ONLY",
        "chronology_precision": chronology_precision,
        "discovery_only": True,
        "exact_http_bytes_preserved": True,
        "fresh_refresh": "w34-architecture-r2-research-sufficiency-revision-r1",
        "lane": lane,
        "provider": provider,
        "refresh_note": refresh_note,
        "selection_not_performed": True,
        "technical_claims_accepted": False,
        "window_utc": "[2026-08-14T22:00:00Z, 2026-08-21T22:00:00Z)",
        "window_relation_observation": "IN_WINDOW_DATE_CANDIDATE",
    }


def gap_record(
    *,
    discovery_id: str,
    title: str,
    source_type: str,
    collector_id: str,
    collector_run_id: str,
    observed_at: str,
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
            "research_pass": 2,
            "parent_refs": [],
            "obligation_ids": list(OBLIGATIONS),
            "reason": (
                "Fresh W34 source-first Discovery refresh lead. The source is "
                "captured for independent Sol completeness review; no Screening, "
                "Evidence, Materiality, Selection, or Architecture disposition is made."
            ),
        },
        "source": {
            "source_type": source_type,
            "collector_id": collector_id,
            "collector_run_id": collector_run_id,
            "observed_at": observed_at,
            "title": title,
            "locator": locator,
            "raw_paths": raw_paths,
            "published_at": published_at,
            "summary_text": summary_text,
            "metadata": metadata,
        },
    }


def openai_items(path: Path) -> dict[str, dict[str, str]]:
    root = ElementTree.fromstring(path.read_text(encoding="utf-8"))
    wanted = {
        "Replit expands access to software creation with GPT-5.6 Luna": "w34-refresh-openai-replit-gpt56-luna",
        "The Defender’s Window": "w34-refresh-openai-defenders-window",
    }
    found: dict[str, dict[str, str]] = {}
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        if title not in wanted:
            continue
        date = parsedate_to_datetime((item.findtext("pubDate") or "").strip()).astimezone()
        found[title] = {
            "discovery_id": wanted[title],
            "title": title,
            "locator": (item.findtext("link") or "").strip(),
            "published_at": date.astimezone().isoformat(timespec="seconds").replace("+00:00", "Z"),
        }
    missing = sorted(set(wanted) - set(found))
    if missing:
        raise ValueError(f"fresh OpenAI RSS snapshot missing expected W34 items: {missing}")
    return found


def arxiv_entries(path: Path, wanted_ids: list[str]) -> dict[str, dict[str, Any]]:
    payload = read_json(path)
    entries = payload.get("entries")
    if not isinstance(entries, list):
        raise ValueError("arXiv summary does not contain entries")
    wanted = set(wanted_ids)
    result: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        raw_id = str(entry.get("id", ""))
        base_id = raw_id.rsplit("/", 1)[-1]
        base_id = re.sub(r"v[0-9]+$", "", base_id)
        if base_id in wanted:
            result[base_id] = entry
    missing = sorted(wanted - set(result))
    if missing:
        raise ValueError(f"fresh arXiv summary missing expected IDs: {missing}")
    return result


def arxiv_record(
    *,
    entry: dict[str, Any],
    discovery_id: str,
    raw_filename: str,
    lane: str,
) -> dict[str, Any]:
    raw_id = str(entry["id"])
    base_id = re.sub(r"v[0-9]+$", "", raw_id.rsplit("/", 1)[-1])
    summary = " ".join(str(entry.get("summary", "")).split())
    categories = entry.get("categories") or []
    metadata = base_metadata(
        lane=lane,
        provider="arXiv",
        chronology_precision="EXACT_PUBLISHED_IN_ATOM_SUMMARY",
        refresh_note=(
            "The Atom response is a broad category sweep. The abstract is a "
            "Discovery lead only; paper-level Evidence and significance remain for Sol/Luna review."
        ),
    )
    metadata.update(
        {
            "arxiv_id": base_id,
            "categories": categories,
            "primary_category": entry.get("primary_category"),
            "updated_at": entry.get("updated"),
            "iterative_evidence_priority": True,
        }
    )
    return gap_record(
        discovery_id=discovery_id,
        title=str(entry["title"]),
        source_type="arxiv_atom_snapshot",
        collector_id="arxiv-api",
        collector_run_id=ARXIV_RUN_ID,
        observed_at=OBSERVED_ARXIV,
        locator=f"https://arxiv.org/abs/{base_id}",
        raw_paths=[arxiv_path(raw_filename)],
        published_at=str(entry["published"]),
        summary_text=summary,
        metadata=metadata,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--prior", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--ledger", required=True)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    prior_path = repo_root / args.prior
    output_path = repo_root / args.output
    ledger_path = repo_root / args.ledger
    if output_path.exists() or ledger_path.exists():
        raise ValueError("fresh Discovery output or ledger already exists; refusing overwrite")

    prior = read_jsonl(prior_path)
    prior_ids = {row.get("discovery_id") for row in prior}

    official_file = repo_root / official_path("openai-news-rss.html")
    official_items_found = openai_items(official_file)
    official_raw = {
        "kimi": repo_root / official_path("kimi-code-whats-new.html"),
        "cohere": repo_root / official_path("cohere-blog.html"),
        "apple": repo_root / official_path("apple-ml-research.html"),
    }
    if not all(path.is_file() for path in official_raw.values()):
        raise ValueError("required official-page Raw snapshot is missing")
    kimi_text = official_raw["kimi"].read_text(encoding="utf-8", errors="replace")
    if "v0.38.0" not in kimi_text or "v0.37.0" not in kimi_text:
        raise ValueError("Kimi Code W34 release-note markers missing")
    cohere_text = official_raw["cohere"].read_text(encoding="utf-8", errors="replace")
    if "The Culture Funnel: You can’t align what isn’t in the data" not in cohere_text:
        raise ValueError("Cohere W34 research marker missing")
    apple_text = official_raw["apple"].read_text(encoding="utf-8", errors="replace")

    new_records: list[dict[str, Any]] = []
    new_records.append(
        gap_record(
            discovery_id="w34-refresh-kimi-code-cli-v038-v037",
            title="Kimi Code CLI v0.38.0 and v0.37.0 release notes",
            source_type="official_release_notes_snapshot",
            collector_id="official-pages",
            collector_run_id=OFFICIAL_RUN_ID,
            observed_at=OBSERVED_OFFICIAL,
            locator="https://www.kimi.com/code/docs/en/kimi-code/whats-new.html",
            raw_paths=[official_path("kimi-code-whats-new.html")],
            published_at="2026-08-20",
            summary_text=(
                "The official Kimi Code release-note page lists v0.38.0 on Aug 20 and "
                "v0.37.0 on Aug 18, including a WaitFor tool, additional data sources, "
                "multi-skill activation, and Windows CLI auto-update. Candidate-level "
                "scope and chronology still require Evidence review."
            ),
            metadata=base_metadata(
                lane="developer tooling / agent infrastructure",
                provider="Kimi",
                chronology_precision="DATE_ONLY_OFFICIAL_RELEASE_NOTES",
                refresh_note="Current official release-notes snapshot; no final technical claim is accepted here.",
            )
            | {"iterative_evidence_priority": True, "release_dates": ["2026-08-18", "2026-08-20"]},
        )
    )

    for title, row in official_items_found.items():
        new_records.append(
            gap_record(
                discovery_id=row["discovery_id"],
                title=title,
                source_type="official_rss_index_snapshot",
                collector_id="official-pages",
                collector_run_id=OFFICIAL_RUN_ID,
                observed_at=OBSERVED_OFFICIAL,
                locator=row["locator"],
                raw_paths=[official_path("openai-news-rss.html")],
                published_at=row["published_at"],
                summary_text=(
                    f"OpenAI's official RSS snapshot lists the W34 item {title!r}. "
                    "The RSS item is a Discovery lead; the linked article body and technical "
                    "relevance require candidate-specific Evidence review."
                ),
                metadata=base_metadata(
                    lane="major model provider / developer and security signals",
                    provider="OpenAI",
                    chronology_precision="EXACT_RSS_PUBDATE_CURRENT_FEED_SNAPSHOT",
                    refresh_note="RSS index item captured; linked article body was not promoted as Evidence in Discovery.",
                )
                | {"iterative_evidence_priority": True},
            )
        )

    new_records.append(
        gap_record(
            discovery_id="w34-refresh-cohere-culture-funnel",
            title="The Culture Funnel: You can’t align what isn’t in the data",
            source_type="official_research_index_snapshot",
            collector_id="official-pages",
            collector_run_id=OFFICIAL_RUN_ID,
            observed_at=OBSERVED_OFFICIAL,
            locator="https://cohere.com/blog/the-culture-funnel-you-cant-align-what-isnt-in-the-data",
            raw_paths=[official_path("cohere-blog.html")],
            published_at="2026-08-19T20:28:00Z",
            summary_text=(
                "Cohere's official blog index lists this Aug 19 Research item and describes "
                "a finding that cultural diversity can be lost in post-training data mixes. "
                "The current index snapshot is a research lead, not an accepted technical claim."
            ),
            metadata=base_metadata(
                lane="research / training data / alignment",
                provider="Cohere Labs",
                chronology_precision="EXACT_EMBEDDED_DATE_CURRENT_INDEX_SNAPSHOT",
                refresh_note="Research item requires article-body and methods review before any downstream use.",
            )
            | {"iterative_evidence_priority": True},
        )
    )

    apple_specs = [
        (
            "w34-refresh-apple-grpo-beyond-english",
            "grpo-beyond-english",
            "GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings",
            "2026-08-18",
            "training / reasoning / multilingual",
        ),
        (
            "w34-refresh-apple-human-like-behaviors-llms",
            "human-like-behaviors-llms",
            "Examining Human-Like Behaviors in LLMs: A Multi-Dimensional Analysis of Model Behaviors, User Factors, and System Prompts",
            "2026-08-19",
            "model behavior / evaluation",
        ),
        (
            "w34-refresh-apple-scaling-laws-mixture-pretraining",
            "scaling-laws-mixture-pretraining",
            "Scaling Laws for Mixture Pretraining Under Data Constraints",
            "2026-08-20",
            "training / data mixture / scaling",
        ),
    ]
    for discovery_id, slug, title, published_at, lane in apple_specs:
        if f'"slug":"{slug}"' not in apple_text or f'"title":"{title}"' not in apple_text:
            raise ValueError(f"Apple W34 research marker missing: {slug}")
        new_records.append(
            gap_record(
                discovery_id=discovery_id,
                title=title,
                source_type="official_research_index_snapshot",
                collector_id="official-pages",
                collector_run_id=OFFICIAL_RUN_ID,
                observed_at=OBSERVED_OFFICIAL,
                locator=f"https://machinelearning.apple.com/research/{slug}",
                raw_paths=[official_path("apple-ml-research.html")],
                published_at=published_at,
                summary_text=(
                    f"Apple ML Research's current index lists {title!r} with a {published_at} "
                    "publication date. The index entry is a Discovery lead; paper body, "
                    "methods, and technical significance require independent review."
                ),
                metadata=base_metadata(
                    lane=lane,
                    provider="Apple Machine Learning Research",
                    chronology_precision="DATE_ONLY_OFFICIAL_RESEARCH_INDEX",
                    refresh_note="Index snapshot is broad and current; paper-level Evidence remains open.",
                )
                | {"iterative_evidence_priority": True, "slug": slug},
            )
        )

    wanted_arxiv = [
        "2608.21601",
        "2608.21614",
        "2608.23611",
        "2608.21500",
        "2608.21159",
        "2608.21134",
        "2608.21265",
        "2608.21584",
    ]
    arxiv = arxiv_entries(
        repo_root / f"{SOURCE_INTAKE_REL}/arxiv/runs/20260907T161121Z/summary.json",
        wanted_arxiv,
    )
    arxiv_specs = [
        ("2608.21601", "w34-refresh-arxiv-k-bench", "cs-ai.atom", "evaluation / scientific agents"),
        ("2608.21614", "w34-refresh-arxiv-saem", "cs-ai.atom", "MoE inference / serving"),
        ("2608.23611", "w34-refresh-arxiv-refine", "cs-ai.atom", "developer tooling / agentic code"),
        ("2608.21500", "w34-refresh-arxiv-sec-opd", "cs-cr.atom", "agent security / prompt injection"),
        ("2608.21159", "w34-refresh-arxiv-aid-guard", "cs-cr.atom", "agent security / authorization"),
        ("2608.21134", "w34-refresh-arxiv-llama-mobile", "cs-cv.atom", "VLM inference / edge deployment"),
        ("2608.21265", "w34-refresh-arxiv-memory-augmentation", "cs-cl.atom", "reasoning efficiency / retrieval"),
        ("2608.21584", "w34-refresh-arxiv-algorithm-dispatch", "cs-ai.atom", "LLM systems / algorithm discovery"),
    ]
    for arxiv_id, discovery_id, raw_filename, lane in arxiv_specs:
        new_records.append(
            arxiv_record(
                entry=arxiv[arxiv_id],
                discovery_id=discovery_id,
                raw_filename=raw_filename,
                lane=lane,
            )
        )

    duplicate_ids = sorted(prior_ids.intersection(row["discovery_id"] for row in new_records))
    if duplicate_ids:
        raise ValueError(f"fresh Discovery IDs already exist in prior graph: {duplicate_ids}")

    all_records = prior + new_records
    write_jsonl(output_path, all_records)
    ledger = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "refresh": "w34-architecture-r2-research-sufficiency-revision-r1",
        "prior_canonical_graph_records": len(prior),
        "fresh_graph_records": len(all_records),
        "new_discovery_leads": len(new_records),
        "new_discovery_ids": [row["discovery_id"] for row in new_records],
        "unchanged_prior_records": len(prior),
        "consolidated_duplicates": [],
        "chronology_reclassified_candidates": [],
        "downstream_disposition": "NOT_PERFORMED_SOL_DISCOVERY_REVIEW_REQUIRED",
        "source_intake_runs": [ARXIV_RUN_ID, "github-releases-2026-W34-20260907T161442Z", OFFICIAL_RUN_ID],
        "source_intake_overall_status": "partial",
    }
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(ledger, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
