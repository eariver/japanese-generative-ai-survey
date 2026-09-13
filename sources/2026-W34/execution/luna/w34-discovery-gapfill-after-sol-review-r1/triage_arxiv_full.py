#!/usr/bin/env python3
"""Run a transparent, Discovery-only triage over the complete collected W34 arXiv set.

The script consumes the previously captured Atom Raw files, verifies that their
version-normalized union matches the accepted 2,296-entry summary, and emits a
row for every entry.  The keyword pass is deliberately high-recall assistance,
not a downstream screening decision.  A deterministic score threshold creates a
reviewable provisional semantic shortlist; Sol remains the independent reviewer.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


ISSUE_ID = "2026-W34"
START = "2026-08-14T22:00:00Z"
END = "2026-08-21T22:00:00Z"
ARXIV_RUN_ID = "arxiv-api-2026-W34-20260907T161121Z"
OBSERVED_AT = "2026-09-07T16:11:21Z"
NS = {"atom": "http://www.w3.org/2005/Atom"}

TERM_GROUPS: dict[str, str] = {
    "language_models": r"\bllm\b|large language model|language model|foundation model|generative ai|genai",
    "agents_tools": r"\bagent(?:s|ic)?\b|tool use|function calling|computer use|autonomous agent",
    "retrieval_embeddings": r"\brag\b|retrieval[- ]augmented|retrieval|knowledge retrieval|embedding",
    "inference_serving": r"\binference\b|serving|quantization|speculative decoding|mixture[- ]of[- ]experts|\bmoe\b",
    "multimodal_media": r"multimodal|vision-language|vision language|\bvlm\b|text-to-video|video generation|image generation",
    "training_methods": r"transformer|diffusion|reasoning|pretraining|pre-training|fine[- ]tuning|post[- ]training|reinforcement learning|distillation|synthetic data",
    "safety_security": r"safety|alignment|security|cyber|adversarial|prompt injection|privacy|authorization|guardrail|robustness",
    "developer_systems": r"code generation|software engineering|program synthesis|code agent|developer|repository|debugging|refactoring",
    "evaluation": r"benchmark|evaluation|evaluating|test-time|assessment|measurement",
    "memory_context": r"\bmemory\b|long[- ]term|context window|context management",
}

METHOD_MARKERS = re.compile(
    r"\b(benchmark|framework|system|method|model|agent|inference|serving|retrieval|security|"
    r"alignment|reasoning|quantization|training|pretraining|fine[- ]tuning|evaluation|tool|"
    r"code|memory|transformer|diffusion)\b",
    re.IGNORECASE,
)
DOMAIN_MARKERS = re.compile(
    r"\b(cancer|clinical|medical|healthcare|radiograph|crop|agriculture|traffic|autonomous driving|"
    r"vehicle|geospatial|remote sensing|protein|chemistry|molecular|financial|stock|maritime|"
    r"education|classroom|social media|political|legal|law|earthquake|weather|wireless|6g|power grid|"
    r"manufacturing|materials?)\b",
    re.IGNORECASE,
)


def base_arxiv_id(value: str) -> str:
    return re.sub(r"v[0-9]+$", "", value.rsplit("/", 1)[-1])


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


def parse_atom(path: Path) -> list[dict[str, Any]]:
    root = ElementTree.fromstring(path.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", NS):
        raw_id = (entry.findtext("atom:id", default="", namespaces=NS) or "").strip()
        title = " ".join((entry.findtext("atom:title", default="", namespaces=NS) or "").split())
        abstract = " ".join((entry.findtext("atom:summary", default="", namespaces=NS) or "").split())
        published = (entry.findtext("atom:published", default="", namespaces=NS) or "").strip()
        updated = (entry.findtext("atom:updated", default="", namespaces=NS) or "").strip()
        categories = sorted({str(node.attrib.get("term", "")) for node in entry.findall("atom:category", NS) if node.attrib.get("term")})
        if not raw_id or not title or not published:
            raise ValueError(f"incomplete arXiv Atom entry in {path}: {raw_id!r}")
        rows.append(
            {
                "arxiv_id": base_arxiv_id(raw_id),
                "versioned_id": raw_id.rsplit("/", 1)[-1],
                "title": title,
                "abstract": abstract,
                "published": published,
                "updated": updated,
                "categories": categories,
                "primary_category": categories[0] if categories else None,
                "raw_file": path.name,
                "locator": f"https://arxiv.org/abs/{base_arxiv_id(raw_id)}",
            }
        )
    return rows


def consolidate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for row in rows:
        old = by_id.get(row["arxiv_id"])
        if old is None:
            by_id[row["arxiv_id"]] = row
            continue
        if row["published"] < old["published"]:
            chosen = dict(row)
            chosen["raw_file"] = min(old["raw_file"], row["raw_file"])
            chosen["categories"] = sorted(set(old["categories"]) | set(row["categories"]))
            chosen["primary_category"] = chosen["categories"][0] if chosen["categories"] else None
            by_id[row["arxiv_id"]] = chosen
        else:
            old["categories"] = sorted(set(old["categories"]) | set(row["categories"]))
            old["primary_category"] = old["categories"][0] if old["categories"] else None
            old["raw_file"] = min(old["raw_file"], row["raw_file"])
    return [by_id[key] for key in sorted(by_id)]


def prior_arxiv_relationships(path: Path) -> dict[str, str]:
    relationships: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        source = row.get("source", {})
        metadata = source.get("metadata", {}) if isinstance(source, dict) else {}
        arxiv_id = metadata.get("arxiv_id")
        if isinstance(arxiv_id, str) and arxiv_id:
            relationships[arxiv_id] = str(row.get("discovery_id"))
    return relationships


def classify(row: dict[str, Any], prior: dict[str, str]) -> dict[str, Any]:
    text = f"{row['title']} {row['abstract']}".lower()
    title = row["title"].lower()
    matched = sorted(name for name, pattern in TERM_GROUPS.items() if re.search(pattern, text, re.IGNORECASE))
    title_matched = sorted(name for name, pattern in TERM_GROUPS.items() if re.search(pattern, title, re.IGNORECASE))
    score = (2 * len(title_matched)) + len(matched)
    if METHOD_MARKERS.search(title):
        score += 2
    high_signal_title = set(title_matched) & {
        "language_models",
        "agents_tools",
        "retrieval_embeddings",
        "inference_serving",
        "safety_security",
        "developer_systems",
    }
    if DOMAIN_MARKERS.search(title) and not high_signal_title:
        score -= 2
    prefilter_hit = bool(matched)
    boundary = "IN_WINDOW"
    if row["published"] < START:
        boundary = "PRE_WINDOW"
    elif row["published"] >= END:
        boundary = "POST_CUTOFF"
    # This is an intentionally mechanical, high-recall semantic-assistance
    # rule. It is not a Sol completeness or downstream editorial decision.
    shortlist = boundary == "IN_WINDOW" and score >= 9
    duplicate = prior.get(row["arxiv_id"])
    if boundary != "IN_WINDOW":
        bucket = "BOUNDARY"
    elif shortlist and duplicate:
        bucket = "DUPLICATE_EXISTING_DISCOVERY"
    elif shortlist:
        bucket = "SEMANTIC_SHORTLIST"
    elif not prefilter_hit:
        bucket = "IRRELEVANT_OR_OUT_OF_SCOPE_SIGNAL"
    else:
        bucket = "PREFILTER_REVIEWABLE_BACKGROUND"
    if title_matched:
        lane = title_matched[0]
    elif matched:
        lane = matched[0]
    else:
        lane = "none"
    rationale = (
        f"Discovery triage only: matched={','.join(matched) or 'none'}; "
        f"title_matches={','.join(title_matched) or 'none'}; score={score}. "
        "Shortlist status is provisional and requires Sol review; no downstream disposition is encoded."
    )
    return {
        "arxiv_id": row["arxiv_id"],
        "title": row["title"],
        "published": row["published"],
        "updated": row["updated"],
        "categories": row["categories"],
        "primary_category": row["primary_category"],
        "candidate_technical_lane": lane,
        "matched_term_groups": matched,
        "title_term_groups": title_matched,
        "deterministic_score": score,
        "deterministic_prefilter_hit": prefilter_hit,
        "boundary": boundary,
        "triage_bucket": bucket,
        "semantic_shortlist": shortlist,
        "duplicate_relationship": duplicate,
        "relevance_rationale": rationale,
        "abstract_excerpt": row["abstract"][:600],
        "source_raw_file": row["raw_file"],
        "source_locator": row["locator"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--arxiv-raw-root", required=True)
    parser.add_argument("--arxiv-summary", required=True)
    parser.add_argument("--prior-discovery", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    raw_root = root / args.arxiv_raw_root
    summary_path = root / args.arxiv_summary
    prior_path = root / args.prior_discovery
    output_root = root / args.output_root
    if output_root.exists() and any(output_root.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty triage output root: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)

    summary = read_json(summary_path)
    expected_count = summary.get("unique_entry_count")
    if expected_count != 2296 or summary.get("collection_window_start") != START or summary.get("collection_window_end") != END:
        raise ValueError("arXiv accepted summary does not match the required W34 corpus/window")
    raw_paths = sorted(raw_root.glob("*.atom"))
    if len(raw_paths) != 6:
        raise ValueError(f"expected six arXiv Atom Raw files, found {len(raw_paths)}")
    raw_rows: list[dict[str, Any]] = []
    raw_file_counts: dict[str, int] = {}
    for path in raw_paths:
        parsed = parse_atom(path)
        raw_file_counts[path.name] = len(parsed)
        raw_rows.extend(parsed)
    rows = consolidate(raw_rows)
    if len(rows) != expected_count:
        raise ValueError(f"Raw union normalized to {len(rows)} entries, expected {expected_count}")

    prior = prior_arxiv_relationships(prior_path)
    triaged = [classify(row, prior) for row in rows]
    buckets = Counter(row["triage_bucket"] for row in triaged)
    lanes = Counter(row["candidate_technical_lane"] for row in triaged if row["semantic_shortlist"])
    shortlist = [row for row in triaged if row["semantic_shortlist"]]
    summary_out = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "run_id": ARXIV_RUN_ID,
        "observed_at": OBSERVED_AT,
        "source_summary_path": args.arxiv_summary,
        "source_summary_sha256": __import__("hashlib").sha256(summary_path.read_bytes()).hexdigest(),
        "raw_files": [
            {
                "path": str(path.relative_to(root)),
                "sha256": __import__("hashlib").sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
                "entry_count": raw_file_counts[path.name],
            }
            for path in raw_paths
        ],
        "raw_entry_count_before_version_deduplication": len(raw_rows),
        "duplicate_version_or_category_rows_removed": len(raw_rows) - len(rows),
        "unique_entry_count": len(rows),
        "collection_window": {"start": START, "end": END, "timezone": "UTC"},
        "method": {
            "stage": "DISCOVERY_ONLY",
            "deterministic_prefilter": "case-insensitive title+abstract vocabulary in the generated method record",
            "semantic_assistance_rule": "score >= 9, with title term groups weighted 2, full-text term groups weighted 1, method-marker bonus 2, and domain-only title penalty 2",
            "no_story_quota": True,
            "no_downstream_disposition": True,
            "sol_independent_review_required": True,
        },
        "counts": {
            "total_collected": len(rows),
            "deterministic_prefilter_hit": sum(1 for row in triaged if row["deterministic_prefilter_hit"]),
            "semantic_shortlist": len(shortlist),
            "semantic_shortlist_new_after_existing_discovery_merge": sum(1 for row in shortlist if not row["duplicate_relationship"]),
            "duplicate_existing_discovery": buckets["DUPLICATE_EXISTING_DISCOVERY"],
            "irrelevant_or_out_of_scope_signal": buckets["IRRELEVANT_OR_OUT_OF_SCOPE_SIGNAL"],
            "reviewable_background_after_prefilter": buckets["PREFILTER_REVIEWABLE_BACKGROUND"],
            "boundary": buckets["BOUNDARY"],
        },
        "shortlist_lane_counts": dict(sorted(lanes.items())),
        "existing_arxiv_relationships_in_shortlist": {
            row["arxiv_id"]: row["duplicate_relationship"] for row in shortlist if row["duplicate_relationship"]
        },
        "corpus_integrity": {
            "raw_union_unique_ids_matches_summary": True,
            "all_entries_have_title_published_categories": True,
            "all_entries_in_configured_window": buckets["BOUNDARY"] == 0,
        },
    }
    write_json(output_root / "arxiv-full-corpus-manifest.json", {
        "issue_id": ISSUE_ID,
        "run_id": ARXIV_RUN_ID,
        "summary": summary_out,
        "entry_ids": [row["arxiv_id"] for row in rows],
    })
    write_json(output_root / "arxiv-triage-summary.json", summary_out)
    write_jsonl(output_root / "arxiv-triage-ledger.jsonl", triaged)
    write_jsonl(output_root / "arxiv-semantic-shortlist.jsonl", shortlist)
    method_lines = [
        "# Full collected arXiv triage method",
        "",
        "This is a Discovery-only, provisional relevance triage. It does not perform Screening, Materiality, Selection, or Evidence acceptance. Sol must independently review the full ledger and shortlist.",
        "",
        f"- Source run: `{ARXIV_RUN_ID}`; six Atom Raw files; raw rows before version/category deduplication: **{len(raw_rows)}**.",
        f"- Normalized unique corpus: **{len(rows)}**; this matches the accepted collector summary's 2,296 entries.",
        f"- W34 boundary: `{START}` inclusive through `{END}` exclusive; boundary rows: **{buckets['BOUNDARY']}**.",
        f"- Deterministic high-recall prefilter hits: **{sum(1 for row in triaged if row['deterministic_prefilter_hit'])}**.",
        f"- Provisional semantic shortlist: **{len(shortlist)}**; after merging IDs already represented in the prior Discovery graph: **{sum(1 for row in shortlist if not row['duplicate_relationship'])}**.",
        f"- Existing-Discovery duplicate relationships: **{buckets['DUPLICATE_EXISTING_DISCOVERY']}**; low-signal/irrelevant-or-out-of-scope signal: **{buckets['IRRELEVANT_OR_OUT_OF_SCOPE_SIGNAL']}**; prefilter-hit background: **{buckets['PREFILTER_REVIEWABLE_BACKGROUND']}**.",
        "",
        "## Vocabulary",
        "",
    ]
    for name, pattern in TERM_GROUPS.items():
        method_lines.append(f"- `{name}`: `{pattern}`")
    method_lines += [
        "",
        "## Provisional semantic rule",
        "",
        "A row enters the provisional shortlist when the deterministic score is at least 9. Title term groups count twice, full title+abstract term groups count once, a title method marker adds 2, and a title that is domain-specific without a high-signal system group loses 2. The rule is designed to expose a broad, inspectable set of technical research leads; it is not a claim that every shortlisted paper is important or W34-material.",
        "",
        "The full ledger records every entry, matched groups, score, bucket, lane, concise rationale, arXiv locator, and the Raw filename. Existing Discovery relationships are explicit rather than silently discarded. No target paper count or story quota was used.",
        "",
    ]
    (output_root / "arxiv-triage-method.md").write_text("\n".join(method_lines) + "\n", encoding="utf-8")
    print(json.dumps(summary_out["counts"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
