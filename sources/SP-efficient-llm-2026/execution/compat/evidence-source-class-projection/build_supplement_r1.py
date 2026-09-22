#!/usr/bin/env python3
"""Build the SP-efficient-llm-2026 Evidence Authority Supplement r1 (edition-local).

Imports frozen Core modules only; modifies nothing outside the edition tree.
Supplement sources use frozen-supported source_type vocabulary so the
unchanged Core validators accept them.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-efficient-llm-2026"
SOURCE_ROOT_REL = "sources/SP-efficient-llm-2026"
SUPP_DIR_REL = SOURCE_ROOT_REL + "/external/evidence-supplement"
RAW_DIR_REL = SUPP_DIR_REL + "/raw"
MANIFEST_REL = SUPP_DIR_REL + "/evidence-authority-supplement-r1.json"
SUPPLEMENT_ID = "evidence-supplement-sp-efficient-llm-2026-r1"
ACCESSED_AT = "2026-09-22T14:00:00Z"

# (raw_filename, discovery_id, locator, source_type, source_class, title, published_at, relation)
SOURCES = [
 ("supp-d005-fp8-abs.html", "EFF-D005", "https://arxiv.org/abs/2209.05433",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "FP8 Formats for Deep Learning (Micikevicius et al.)",
  "2022-09-12T17:39:55Z",
  "Corrected authority for the FP8 format/algorithm origin: bound Discovery locator 2206.06277 is an unrelated paper; this arXiv identity record is the true paper."),
 ("supp-d061-mooncake-abs.html", "EFF-D061", "https://arxiv.org/abs/2407.00079",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving (Qin et al.)",
  "2024-06-24T02:05:32Z",
  "Corrected authority for pooled-KV disaggregation: bound locator 2411.01181 is unrelated; this arXiv identity record is the true paper."),
 ("supp-d062-sarathi2023-abs.html", "EFF-D062", "https://arxiv.org/abs/2308.16369",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills (Agrawal et al.)",
  "2023-08-31T00:03:02Z",
  "Corrected authority for chunked-prefill scheduling: bound locator 2308.16315 is unrelated (digit transposition); this arXiv identity record is the true paper."),
 ("supp-d062-sarathiserve2024-abs.html", "EFF-D062", "https://arxiv.org/abs/2403.02310",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve (Agrawal et al.)",
  "2024-03-04T18:47:08Z",
  "Same-line serving follow-up to SARATHI 2023 (throughput-latency tradeoff); additive authority for the disaggregation-adjacent scheduler thread."),
 ("supp-d093-swepro-abs.html", "EFF-D093", "https://arxiv.org/abs/2509.16941",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Deng et al.)",
  "2025-09-21T06:28:17Z",
  "Corrected identity authority for SWE-bench-Pro: bound locator 2503.01324 is an unrelated federated-learning paper; this arXiv identity record is the true benchmark paper."),
 ("supp-d093-swepro-html.html", "EFF-D093", "https://arxiv.org/html/2509.16941v2",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "SWE-Bench Pro full text v2 (results: public/commercial splits, frontier <45% Pass@1)",
  "2025-09-21T06:28:17Z",
  "Full-text authority for SWE-bench-Pro scale/split/results figures (1,865 problems, 41 repos, public/commercial/held-out, contamination-resistant collection)."),
 ("supp-d094-tbench2-abs.html", "EFF-D094", "https://arxiv.org/abs/2601.11868",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces (Merrill et al.)",
  "2026-01-17T01:29:30Z",
  "Corrected family authority for Terminal-Bench: bound locator 2406.06750 is an unrelated optics paper; Terminal-Bench 2.0 (ICLR 2026, 89 tasks, frontier <65%) verifies the containerized-terminal methodology and version-suffix rule."),
 ("supp-d098-ruler-abs.html", "EFF-D098", "https://arxiv.org/abs/2404.06654",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "RULER: What is the Real Context Size of Your Long-Context Language Models? (Hsieh et al.)",
  "2024-04-09T23:41:27Z",
  "Corrected authority for effective-context grading: bound locator 2404.18532 is MileBench; this arXiv identity record is the true RULER paper."),
 ("supp-d112-pyramidkv-abs.html", "EFF-D112", "https://arxiv.org/abs/2406.02069",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling (Cai et al.)",
  "2024-06-04T07:51:30Z",
  "Corrected authority for pyramidal KV budgets: bound locator 2406.02032 is an unrelated audio paper; this arXiv identity record is the true paper."),
 ("supp-d117-deebert-abs.html", "EFF-D117", "https://arxiv.org/abs/2004.12993",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference (Xin et al.)",
  "2020-04-27T17:58:05Z",
  "Corrected authority for the early-exit precedent: bound locator 2004.12918 is an unrelated game-theory paper (digit transposition); this arXiv identity record is the true paper."),
 ("supp-d139-doremi-abs.html", "EFF-D139", "https://arxiv.org/abs/2305.10429",
  "PRIMARY_PAPER", "PRIMARY_PAPER", "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (Xie et al.)",
  "2023-05-17T17:58:13Z",
  "Corrected authority for DRO data-mixture optimization: bound locator 2308.01833 is an unrelated robotics paper; this arXiv identity record is the true paper."),
 ("supp-d032-v32exp-launch.html", "EFF-D032", "https://www.deepseek.com/en/news/v3-2-exp/",
  "first_party_announcement", "PRIMARY_OFFICIAL", "Introducing DeepSeek-V3.2-Exp (DeepSeek official launch; DSA debut, 50%+ price cut)",
  None,
  "Dedicated first-party DSA authority replacing homepage-only reliance: V3.2-Exp debuts DeepSeek Sparse Attention with API price cuts and open release (HF weights, GitHub tech report, TileLang/CUDA kernels)."),
 ("supp-d119-genai-perf-docs.html", "EFF-D119", "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html",
  "first_party_product_docs", "PRIMARY_OFFICIAL", "GenAI-Perf — NVIDIA Triton Inference Server (tooling docs: metrics, load model, logging)",
  None,
  "Actual NVIDIA/Triton GenAI-Perf tooling authority: output-token throughput, TTFT, ITL, request throughput under specified load; notes GenAI-Perf phase-out in favor of AIPerf (product surface still open)."),
]


def supplement_source_id(discovery_id: str, locator: str) -> str:
    digest = hashlib.sha256(f"supplement:{discovery_id}:{locator}".encode()).hexdigest()[:16]
    return f"supplement-src-{digest}"


def main() -> int:
    root = Path(".").resolve()
    raw_dir = root / RAW_DIR_REL
    entries = []
    for (fname, did, locator, stype, sclass, title, pub, relation) in SOURCES:
        raw_rel = f"{RAW_DIR_REL}/{fname}"
        raw_path = root / raw_rel
        if not raw_path.is_file() or raw_path.stat().st_size < 1:
            raise ValueError(f"supplement Raw missing: {raw_rel}")
        entries.append({
            "supplement_source_id": supplement_source_id(did, locator),
            "discovery_id": did,
            "evidence_task_id": evidence.stable_task_id(ISSUE_ID, did),
            "locator": locator,
            "source_type": stype,
            "source_class": sclass,
            "title": title,
            "published_at": pub,
            "accessed_at": ACCESSED_AT,
            "raw_path": raw_rel,
            "raw_sha256": core.sha256_file(raw_path),
            "byte_count": raw_path.stat().st_size,
            "relation": relation,
        })
    ids = [e["supplement_source_id"] for e in entries]
    assert len(ids) == len(set(ids)), "supplement source IDs must be unique"
    out = root / MANIFEST_REL
    # Same frozen override context the frozen Evidence runner uses for package
    # builds over pre-advance Screening packages (historical state-SHA
    # tolerance only; all other basis checks rerun; see
    # scripts/survey_agent_tool_v2.py module docstring).
    with agent_tool.current_stage_basis_override():
        evidence.build_evidence_authority_supplement(
            root, ISSUE_ID, root / SOURCE_ROOT_REL,
            root / (SOURCE_ROOT_REL + "/discovery/discovery-v2.jsonl"),
            root / (SOURCE_ROOT_REL + "/screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json"),
            entries, out,
            supplement_id=SUPPLEMENT_ID,
            implementation_sha=core.repository_commit_sha(root),
        )
    manifest = core.load_json(out)
    print(json.dumps({
        "manifest": MANIFEST_REL,
        "sha256": core.sha256_file(out),
        "supplement_id": manifest["supplement_id"],
        "source_count": len(manifest["sources"]),
        "total_raw_bytes": sum(e["byte_count"] for e in entries),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
