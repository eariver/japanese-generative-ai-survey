#!/usr/bin/env python3
"""Temporary one-shot 2026-W33 rebuild to Architecture Review under Core v2 0.15.

This is transport-only production glue. It reuses previously researched W33 Raw
and editorial preparation, but regenerates every current Core acceptance,
checkpoint, Selection, and Architecture authority from the canonical 0.15 State.
It never records a Human decision and stops at Architecture Review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def git(root: Path, *args: str, capture: bool = False) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        text=True,
        capture_output=capture,
    )
    return result.stdout if capture else ""


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_jsonl_bytes(data: bytes) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lineno, raw in enumerate(data.decode("utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError(f"old Discovery line {lineno} is not an object")
        rows.append(value)
    return rows


def canonical_jsonl_line(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as fh:
        for row in rows:
            fh.write(canonical_jsonl_line(row))


def restore_semantic_inputs(root: Path) -> None:
    # Old machine acceptances/checkpoints are deliberately not restored.
    git(root, "checkout", "origin/temp/w33-architecture-stage", "--", "sources/2026-W33/collectors")
    git(
        root,
        "checkout",
        "origin/archive/pre-core015-2026-W33-v2-work-20260829",
        "--",
        "sources/2026-W33/postmerge-research-intake.md",
        "sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md",
    )


def old_discoveries(root: Path) -> list[dict[str, Any]]:
    data = subprocess.run(
        [
            "git", "-C", str(root), "show",
            "origin/temp/w33-architecture-stage:sources/2026-W33/discovery/discovery-v2.jsonl",
        ],
        check=True,
        capture_output=True,
    ).stdout
    rows = read_jsonl_bytes(data)
    # Drop stale pre-postmerge X intake records; postmerge Raw receives a fresh exact binding.
    kept: list[dict[str, Any]] = []
    for row in rows:
        source = row.get("source", {})
        raw_paths = source.get("raw_paths", []) if isinstance(source, dict) else []
        if source.get("source_type") == "x-community-signal":
            continue
        if any("sources/2026-W33/external/x/" in str(path) for path in raw_paths):
            continue
        kept.append(row)
    return kept


def make_gap(
    did: str,
    *,
    title: str,
    locator: str,
    published_at: str | None,
    summary: str,
    source_type: str = "primary-official-followup",
) -> dict[str, Any]:
    return {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "discovery_id": did,
        "provenance": {
            "origin": "GAP_FILL",
            "research_pass": 1,
            "parent_refs": [],
            "obligation_ids": ["weekly:current-relevance", "weekly:technical-significance"],
            "reason": "Post-merge primary-source verification closed a material gap in the original W33 candidate pool.",
        },
        "source": {
            "source_type": source_type,
            "collector_id": "chatgpt-postmerge-primary-verification",
            "collector_run_id": "w33-postmerge-research-intake-r1",
            "observed_at": "2026-08-23T13:20:00Z",
            "title": title,
            "locator": locator,
            "raw_paths": ["sources/2026-W33/postmerge-research-intake.md"],
            "published_at": published_at,
            "summary_text": summary,
            "metadata": {"authority_role": "POSTMERGE_PRIMARY_VERIFICATION"},
        },
    }


def build_new_discoveries() -> list[dict[str, Any]]:
    return [
        make_gap(
            "gap-postmerge-grok-4-6",
            title="Grok 4.6",
            locator="https://x.ai/news/grok-4-6",
            published_at="2026-08-12T00:00:00Z",
            summary="xAI released Grok 4.6 in-window, positioning it for long-running agents, coding and knowledge work, and ambitious interactive/visual tasks; benchmark claims remain vendor-attributed.",
        ),
        make_gap(
            "gap-postmerge-qwen3-8-openweight",
            title="Qwen3.8 open-weight release wave",
            locator="https://github.com/QwenLM/Qwen3.8",
            published_at="2026-08-12T00:00:00Z",
            summary="Official Qwen repository chronology records Qwen3.8-2.4T-A95B on Aug 12 and Qwen3.8-27B on Aug 14; W33 relevance is open-weight/local distribution rather than the earlier hosted announcement.",
            source_type="primary-repository-followup",
        ),
        make_gap(
            "gap-postmerge-gemini-3-7-flash",
            title="Gemini 3.7 Flash",
            locator="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
            published_at="2026-08-13T00:00:00Z",
            summary="Google announced Gemini 3.7 Flash GA on Aug 13 as a workhorse model for coding and agents, with multimodal/tool-oriented product capabilities; price and benchmark comparisons remain Google-attributed.",
        ),
        make_gap(
            "gap-postmerge-glm-5-3",
            title="GLM-5.3",
            locator="https://z.ai/blog/glm-5.3",
            published_at="2026-08-14T00:00:00Z",
            summary="Z.ai announced GLM-5.3 with scaled post-training over the GLM-5.2 base, emphasizing coding, long-horizon tasks and cybersecurity; the source stated local weights would become public later, so W33 must not imply in-window downloadable weights.",
        ),
        make_gap(
            "gap-postmerge-astra-cyber",
            title="Astra critical-cyber capability signal",
            locator="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/",
            published_at="2026-08-07T00:00:00Z",
            summary="OpenAI reported that internal evaluation of unreleased Astra could not rule out the Critical cybersecurity threshold and described strengthened controls; this is capability/governance context, not an Astra product release.",
        ),
        make_gap(
            "gap-postmerge-grok-bot",
            title="Grok Bot",
            locator="https://x.ai/news/introducing-grok-bot",
            published_at="2026-08-11T00:00:00Z",
            summary="xAI introduced Grok Bot as a persistent agent with its own computer and cross-application work, supporting the shift from one-shot chat toward delegated execution.",
        ),
        make_gap(
            "gap-postmerge-qwen-code-runtime",
            title="Qwen Code weekly update 2026-08-13",
            locator="https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-13/",
            published_at="2026-08-13T00:00:00Z",
            summary="Qwen Code shipped v0.21.7-v0.21.11, continued long tasks beyond 50 turns, expanded plugins, and added /coordinate runtime-enforced role separation with read-only research roles and a write role in a Git worktree.",
        ),
    ]


def x_discovery() -> dict[str, Any]:
    return {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "discovery_id": "x-weekly-postmerge-signal-wave",
        "provenance": {
            "origin": "BASE",
            "research_pass": 0,
            "parent_refs": [],
            "obligation_ids": ["weekly:current-relevance", "weekly:technical-significance"],
            "reason": "Exact post-merge Grok/X scan is retained as community-signal Discovery only; primary facts are verified separately.",
        },
        "source": {
            "source_type": "x-community-signal",
            "collector_id": "grok-x-source-intake",
            "collector_run_id": "weekly-x-2026-W33-postmerge-r1",
            "observed_at": "2026-08-23T12:48:54Z",
            "title": "W33 post-merge X community signal wave",
            "locator": "Grok_X_SourseIntake/Weekly/2026-W33/weekly-x-2026-W33-postmerge-r1/grok-x-result.md",
            "raw_paths": ["sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md"],
            "published_at": None,
            "summary_text": "X momentum concentrated around GLM-5.3, Grok 4.6, Qwen3.8 local/open adoption, agentic coding, price pressure, and practical local-inference friction; all technical claims remain non-authoritative until primary-source verification.",
            "metadata": {"role": "DISCOVERY_AND_COMMUNITY_SIGNAL_ONLY", "coverage_lanes": "A-L"},
        },
    }


def build_x_manifest(root: Path, profile_path: Path, raw_path: Path) -> Path:
    from scripts import survey_production_v2 as core
    from scripts import survey_x_intake_v2 as x_intake

    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    spec = {
        "decision": "REQUIRED",
        "rationale": "Weekly profile requires X/Grok intake; reuse the exact completed post-merge W33 task and Raw bytes.",
        "series_context": None,
        "runs": [
            {
                "run_id": "weekly-x-2026-W33-postmerge-r1",
                "purpose": "Perform a clean post-merge Weekly X Source Intake validation for 2026-W33 and identify technically material generative-AI community momentum for downstream ChatGPT verification and editorial selection.",
                "research_questions": [
                    "What technically material generative-AI developments had meaningful X momentum during the canonical 2026-W33 window?",
                    "Which developments show independent testing, reproduction, integration, operational adoption, disagreement, or newly discovered constraints rather than only announcement amplification?",
                    "Which primary-source artifacts should downstream ChatGPT verify before any technical claim is accepted?",
                    "What community movement is material enough to support the mandatory reader-facing Weekly community section, including explicit quiet/negative findings where appropriate?",
                ],
                "coverage_focus": [
                    "Foundation Models / Reasoning",
                    "Agents / Coding / Harness / Computer Use",
                    "Multimodal Foundation Models",
                    "Image Generation / Editing",
                    "Video Generation / Editing",
                    "Speech / Audio / Music Generation",
                    "Open Weight / Local AI / Quantization",
                    "Inference / Serving / Systems",
                    "Memory / Multi-Agent / Retrieval",
                    "Evaluation / Benchmarks",
                    "Safety / Security",
                    "Other Emerging Generative AI Technology",
                ],
                "time_scope": "Canonical Weekly editorial window [2026-08-07T18:00:00-04:00, 2026-08-14T18:00:00-04:00), America/New_York. Treat material after the 2026-08-14T18:00:00-04:00 cutoff as Late Breaking rather than ordinary-window material.",
                "expected_result_filename": "grok-x-result.md",
            }
        ],
    }
    manifest = x_intake.build_manifest(root, cfg, profile_path, spec)
    task_path = manifest.parent / "weekly-x-2026-W33-postmerge-r1/grok-task.md"
    expected_task_sha = "c86a6124bb0ff32832995883d37b7f44e08da7142af4ac39032fb7436035b356"
    if task_path.stat().st_size != 9612 or core.sha256_file(task_path) != expected_task_sha:
        raise ValueError(
            f"current Core did not reproduce exact historical Grok task bytes: size={task_path.stat().st_size} sha={core.sha256_file(task_path)}"
        )
    expected_raw_sha = "93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06"
    if raw_path.stat().st_size != 12171 or core.sha256_file(raw_path) != expected_raw_sha:
        raise ValueError("post-merge Grok Raw bytes differ from verified historical authority")
    x_intake.record_result(
        root,
        cfg,
        manifest,
        "weekly-x-2026-W33-postmerge-r1",
        raw_path,
        "grok-x-result.md",
        "2026-08-23T12:48:54Z",
        datetime.now(timezone.utc).isoformat(),
        "SUCCESS",
        "DISCOVERY_RECORDED",
        ["x-weekly-postmerge-signal-wave"],
        "Raw X observation is retained only as community-signal Discovery; primary technical facts are represented by separately verified sources.",
    )
    x_intake.validate_manifest(root, cfg, manifest, require_complete=True)
    return manifest


def record_text(row: dict[str, Any]) -> str:
    source = row["source"]
    return " ".join(
        str(value).lower()
        for value in (
            row["discovery_id"], source.get("title"), source.get("locator"), source.get("summary_text")
        )
        if value is not None
    )


PAPER_IDS = {
    "2608.08654": "Scaffolding",
    "2608.09072": "SWE-RPG",
    "2608.08700": "PluginEval",
    "2608.11888": "Agent Skills Can Be Harmful",
    "2608.10669": "REDAgentBench",
    "2608.08097": "OasisKV",
}


def group_for(row: dict[str, Any]) -> str | None:
    did = row["discovery_id"]
    text = record_text(row)
    locator = str(row["source"].get("locator", "")).lower()
    if did in {
        "gap-postmerge-grok-4-6",
        "gap-postmerge-qwen3-8-openweight",
        "gap-postmerge-gemini-3-7-flash",
        "gap-postmerge-glm-5-3",
    }:
        return "release"
    if did == "gap-postmerge-astra-cyber" or "daybreak" in text or "trusted hands" in text or "frontier cyber models" in text:
        return "cyber"
    if did == "gap-postmerge-grok-bot" or did == "gap-postmerge-qwen-code-runtime":
        return "runtime"
    if did == "x-weekly-postmerge-signal-wave":
        return "community"
    if any(pid in locator or pid.replace(".", "_") in did for pid in PAPER_IDS):
        return "papers"
    if "ultrafast" in text:
        return "serving"
    if "sglang" in locator and ("0.5.17" in text or "v0_5_17" in did):
        return "serving"
    if "vllm" in locator and ("0.27.0" in text or "v0_27_0" in did):
        return "serving"
    if "flashinfer" in locator and ("0.6.17" in text or "v0_6_17" in did):
        return "serving"
    return None


def screening_decision(row: dict[str, Any]) -> dict[str, Any]:
    group = group_for(row)
    if group is not None:
        targets = {
            "release": ["Verify exact in-window chronology, distribution model, and vendor-claim boundaries."],
            "cyber": ["Verify capability/access/governance facts and distinguish unreleased capability signals from product events."],
            "serving": ["Verify exact release/preview facts without constructing unmatched cross-project performance rankings."],
            "community": ["Preserve X only as community observation and counter-signal evidence."],
            "papers": ["Verify paper identity/chronology; keep method/performance claims bounded unless full-paper review supports them."],
            "runtime": ["Verify agent/runtime control behavior and product chronology from the first-party source."],
        }[group]
        return {
            "discovery_id": row["discovery_id"],
            "decision": "KEEP",
            "reason": f"Retained for W33 {group} architecture after post-merge research and primary-source follow-up.",
            "scope_tags": [group, "2026-W33"],
            "duplicate_group": None,
            "verification_targets": targets,
            "confidence": "high" if group != "community" else "medium",
        }
    reason = (
        "Carry-over was explicitly rechecked and no fresh W33 authority justified promotion."
        if "weekly:carry-over" in row["provenance"].get("obligation_ids", [])
        else "Retained in broad W33 Discovery coverage but not selected after post-merge materiality comparison."
    )
    return {
        "discovery_id": row["discovery_id"],
        "decision": "DROP",
        "reason": reason,
        "scope_tags": ["explicit-disposition", "2026-W33"],
        "duplicate_group": None,
        "verification_targets": [],
        "confidence": "high",
    }


def evidence_profile(row: dict[str, Any]) -> dict[str, Any]:
    group = group_for(row)
    if group is None:
        raise ValueError(f"Evidence requested for non-kept Discovery: {row['discovery_id']}")
    did = row["discovery_id"]
    source = row["source"]
    text = record_text(row)
    if group == "papers":
        return {
            "status": "PARTIAL",
            "artifact_type": "PAPER",
            "entity_type": "PAPER",
            "source_class": "PRIMARY_PAPER",
            "claim_class": "PRIMARY_FACT",
            "claim": f"The primary paper record establishes '{source['title']}' as a W33 research item; method and performance conclusions remain bounded pending full-paper review.",
            "limitation": "Paper identity and chronology are accepted here; headline method/performance claims are not generalized beyond the authors' reported setup.",
        }
    if group == "community":
        return {
            "status": "PARTIAL",
            "artifact_type": "OTHER",
            "entity_type": "OTHER",
            "source_class": "SOCIAL",
            "claim_class": "SOCIAL_OBSERVATION",
            "claim": "The exact post-merge X scan observed strong practitioner attention around rapid model releases, local/open-weight adoption, agentic coding, price pressure, and practical local-inference friction.",
            "limitation": "X engagement, qualitative parity claims, local speed reports, and rumors are observation-time community signals, not technical fact authority.",
        }
    if did == "gap-postmerge-grok-4-6":
        claim = "xAI's in-window Grok 4.6 announcement positions the model around long-running agents, coding/knowledge work, and ambitious interactive/visual tasks."
        limitation = "Model-level benchmark claims remain vendor-attributed and are not normalized into a cross-vendor ranking."
        artifact_type, entity_type = "MODEL_UPDATE", "MODEL"
    elif did == "gap-postmerge-qwen3-8-openweight":
        claim = "The official Qwen repository records Qwen3.8-2.4T-A95B on Aug 12 and Qwen3.8-27B on Aug 14, making open-weight/local distribution the material W33 event."
        limitation = "Community consumer-hardware speed, quality, and frontier-parity claims are not accepted as independently reproduced facts."
        artifact_type, entity_type = "OPEN_WEIGHT", "MODEL_FAMILY"
    elif did == "gap-postmerge-gemini-3-7-flash":
        claim = "Google announced Gemini 3.7 Flash GA on Aug 13 and positioned it as a workhorse model for coding and agents."
        limitation = "Comparative pricing and benchmark statements remain Google-attributed rather than independent cross-vendor measurements."
        artifact_type, entity_type = "MODEL_UPDATE", "MODEL"
    elif did == "gap-postmerge-glm-5-3":
        claim = "Z.ai announced GLM-5.3 on Aug 14, emphasizing scaled post-training over the GLM-5.2 base, complex coding/long-horizon tasks, and cybersecurity capability."
        limitation = "The announcement stated local weights would become public later; W33 must not imply that GLM-5.3 weights were downloadable during the issue window."
        artifact_type, entity_type = "MODEL_UPDATE", "MODEL"
    elif did == "gap-postmerge-astra-cyber":
        claim = "OpenAI reported that internal evaluation of unreleased Astra could not rule out the Critical cybersecurity capability threshold and described strengthened controls."
        limitation = "Astra is unreleased in this authority and must be treated as capability/governance context, not a product launch."
        artifact_type, entity_type = "SECURITY_EVENT", "MODEL"
    elif did == "gap-postmerge-grok-bot":
        claim = "xAI introduced Grok Bot as a persistent agent with its own computer and cross-application work, providing an in-window delegated-execution product signal."
        limitation = "This item is used as a supporting runtime/product example rather than evidence of general autonomous reliability."
        artifact_type, entity_type = "AGENT", "AGENT"
    elif did == "gap-postmerge-qwen-code-runtime":
        claim = "The Aug 13 Qwen Code update records v0.21.7-v0.21.11, longer-running task continuation, plugin expansion, and /coordinate runtime-enforced role separation."
        limitation = "The control semantics are reported from the project update and are not generalized to all agent runtimes."
        artifact_type, entity_type = "FRAMEWORK", "FRAMEWORK"
    elif "ultrafast" in text:
        claim = "OpenAI's Ultrafast item is an in-window preview that productizes frontier-model inference latency as a service tier."
        limitation = "Advertised speed multipliers and output-token rates are vendor preview claims, not independently reproduced throughput measurements."
        artifact_type, entity_type = "PRODUCT", "PRODUCT"
    elif group == "cyber":
        claim = f"The first-party W33 source '{source['title']}' establishes a concrete Daybreak/frontier-cyber access or distribution event used in the governed-capability package."
        limitation = "Capability statements remain first-party claims; editorial use must preserve authorization, safeguards, and access-control context."
        artifact_type, entity_type = "PRODUCT", "PRODUCT"
    elif group == "serving":
        claim = f"The upstream W33 release source '{source['title']}' establishes a concrete serving/runtime update inside the issue window."
        limitation = "Project-reported performance/resource numbers are not treated as a controlled cross-framework benchmark."
        artifact_type, entity_type = "FRAMEWORK", "FRAMEWORK"
    else:
        raise ValueError(f"unhandled Evidence profile: {did}")
    source_type = str(source.get("source_type", ""))
    source_class = "PRIMARY_REPOSITORY" if ("github" in source_type or "repository" in source_type or "github.com" in str(source.get("locator"))) else "PRIMARY_OFFICIAL"
    return {
        "status": "VERIFIED",
        "artifact_type": artifact_type,
        "entity_type": entity_type,
        "source_class": source_class,
        "claim_class": "PRIMARY_FACT",
        "claim": claim,
        "limitation": limitation,
    }


def build_evidence_card(root: Path, package: dict[str, Any], meta: dict[str, Any], task: dict[str, Any], discovery: dict[str, Any]) -> dict[str, Any]:
    from scripts import survey_production_v2 as core

    prof = evidence_profile(discovery)
    source = discovery["source"]
    locator = source["locator"]
    accessed_at = source["observed_at"]
    published_at = source.get("published_at")
    source_id = "src"
    entities = [{
        "entity_id": "subject",
        "canonical_name": source["title"],
        "entity_type": prof["entity_type"],
        "organization": None,
        "canonical_url": locator,
    }]
    events = []
    if published_at is not None:
        events.append({
            "event_id": "event-1",
            "event_type": "SOURCE_PUBLISHED_OR_RELEASED",
            "event_date": published_at,
            "subject_id": "subject",
            "subject_role": "PRIMARY_SUBJECT",
            "source_ids": [source_id],
        })
    claim = {
        "statement_id": "claim-1",
        "text": prof["claim"],
        "subject_id": "subject",
        "subject_role": "PRIMARY_SUBJECT",
        "evidence_class": prof["claim_class"],
        "source_ids": [source_id],
        "context": discovery["discovery_id"],
    }
    limitation = {
        "statement_id": "lim-1",
        "text": prof["limitation"],
        "subject_id": "subject",
        "subject_role": "PRIMARY_SUBJECT",
        "evidence_class": "PRIMARY_FACT" if prof["source_class"] != "SOCIAL" else "SOCIAL_OBSERVATION",
        "source_ids": [source_id],
        "context": "Evidence boundary",
    }
    target_status = "VERIFIED" if prof["status"] == "VERIFIED" else "UNRESOLVED"
    targets = [
        {
            "target": target,
            "status": target_status,
            "finding": (
                "Post-merge primary-source review supports bounded W33 use."
                if target_status == "VERIFIED"
                else "The source is retained with explicit partial/community or paper-review limitations."
            ),
            "subject_ids": ["subject"],
            "source_ids": [source_id],
        }
        for target in task.get("verification_targets", [])
    ]
    unresolved = [] if prof["status"] == "VERIFIED" else [prof["limitation"]]
    return {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "evidence_task_id": meta["evidence_task_id"],
        "basis": {
            "task_sha256": meta["sha256"],
            "screening_acceptance_sha256": task["screening_basis"]["screening_acceptance_sha256"],
            "prompt_sha256": package["prompt"]["sha256"],
            "result_contract_sha256": package["contracts"]["card"]["sha256"],
        },
        "status": prof["status"],
        "entities": entities,
        "artifact": {
            "primary_subject_id": "subject",
            "artifact_type": prof["artifact_type"],
            "canonical_name": source["title"],
            "canonical_url": locator,
        },
        "temporal": {"observed_at": accessed_at, "events": events},
        "sources": [{
            "source_id": source_id,
            "url": locator,
            "source_class": prof["source_class"],
            "title": source["title"],
            "published_at": published_at,
            "accessed_at": accessed_at,
            "role": "Exact accepted Discovery locator used for bounded factual/community verification.",
        }],
        "claims": [claim],
        "metrics": [],
        "limitations": [limitation],
        "verification": {"targets": targets, "unresolved_questions": unresolved, "contradictions": []},
    }


def why_this_issue(group: str) -> str:
    return {
        "release": "Four Aug 12-14 releases expose agentic/coding work as a common frontier axis while distribution remains split between closed services and open weights.",
        "cyber": "W33 links frontier cyber capability growth to access tiers, authorization, safeguards, monitoring, and enterprise distribution.",
        "serving": "W33 combines frontier latency productization with open serving/runtime engineering, making deployment systems part of the competitive frontier.",
        "community": "The exact post-merge X scan records practitioner attention, local/open adoption, price pressure, and counter-signals without elevating social claims into technical facts.",
        "papers": "The paper watch supplies diagnostic research on scaffolding, requirements, tool use, agent safety, skills, and KV-cache systems that counterbalances release headlines.",
        "runtime": "Qwen Code and Grok Bot show persistent/long-lived agents turning orchestration and permissions into explicit runtime concerns.",
    }[group]


def package_plan() -> dict[str, dict[str, Any]]:
    return {
        "release": {
            "package_id": "pkg-01-release-wave",
            "title": "Release wave: agentic work becomes the common frontier",
            "purpose": "Compare Grok 4.6, Qwen3.8, Gemini 3.7 Flash, and GLM-5.3 through agentic/coding orientation, distribution model, deployment locality, and long-horizon work without flattening vendor benchmark methodologies.",
            "must": [
                "Preserve exact in-window chronology.",
                "Separate closed-service delivery from open-weight/local deployment.",
                "Treat coding/agentic work as a common comparison axis rather than inventing a cross-vendor leaderboard.",
                "State that GLM-5.3 weights were not yet downloadable in the W33 window.",
            ],
            "extra_boundaries": ["Vendor benchmark methodologies are not normalized into a synthetic cross-vendor ranking."],
        },
        "cyber": {
            "package_id": "pkg-02-cyber-governance",
            "title": "Cyber capability becomes governed infrastructure",
            "purpose": "Connect capability-threshold detection, model specialization, access tiers, authorization, monitoring, safeguards, and enterprise-cloud delivery.",
            "must": [
                "Treat Astra as an unreleased capability/governance signal, not a product release.",
                "Use Daybreak expansion as the concrete product/access event.",
                "Preserve authorized defensive-use and access-control framing.",
            ],
            "extra_boundaries": ["Capability claims and access-governance facts must remain explicitly separated."],
        },
        "serving": {
            "package_id": "pkg-03-serving-frontier",
            "title": "Serving becomes part of the frontier product",
            "purpose": "Show frontier-model latency productization and open serving/runtime engineering moving together across Ultrafast, SGLang, vLLM, and FlashInfer.",
            "must": [
                "Keep Ultrafast speed figures as vendor preview claims.",
                "Compare OSS releases by engineering direction/support rather than unmatched speed numbers.",
                "Explain time-to-support, MoE, memory/KV pressure, and deployment latency as systems-level competitive dimensions.",
            ],
            "extra_boundaries": ["No cross-framework performance ranking is permitted without matched workloads and hardware."],
        },
        "community": {
            "package_id": "pkg-04-community-pulse",
            "title": "Community Pulse: open/local viability meets practical friction",
            "purpose": "Capture what practitioners tested and debated around Qwen/GLM open-local momentum, Grok 4.6 reactions, price pressure, and local-inference constraints.",
            "must": [
                "Separate underlying event dates from the later X observation time.",
                "Keep X reaction distinct from primary technical facts.",
                "Include counter-signals such as slow long tasks or optimization gaps.",
                "Preserve X visibility and sampling limitations.",
            ],
            "extra_boundaries": ["Community observations are not substitutes for primary-source technical verification."],
        },
        "papers": {
            "package_id": "pkg-05-paper-watch",
            "title": "Research Paper Watch: diagnose the agent and serving stack",
            "purpose": "Use six W33 papers as a diagnostic counterpoint on scaffolding, requirement recovery, function-call errors, harmful skills, executable agent safety, and KV-cache systems.",
            "must": [
                "Keep paper claims distinct from production release facts.",
                "Use papers as bounded research watch items rather than treating abstracts as independently reproduced performance evidence.",
            ],
            "extra_boundaries": ["Paper method/performance conclusions remain author-reported unless the full setup is reviewed."],
        },
        "runtime": {
            "package_id": "pkg-06-agent-runtime",
            "title": "OSS / Agent Runtime Watch: orchestration becomes execution control",
            "purpose": "Use Qwen Code runtime role separation and Grok Bot persistent-agent behavior to show agent orchestration becoming an execution-control problem.",
            "must": [
                "Explain /coordinate as runtime-enforced permission separation rather than prompt etiquette.",
                "Use Grok Bot as a supporting persistent-agent product example.",
                "Avoid duplicating serving-stack mini-articles already owned by the serving package.",
            ],
            "extra_boundaries": ["Product/project behavior is not generalized into a universal agent-runtime guarantee."],
        },
    }


def selection_role(group: str) -> str:
    return {
        "release": "WEEKLY:FEATURE",
        "cyber": "WEEKLY:FEATURE",
        "serving": "WEEKLY:FEATURE",
        "community": "WEEKLY:COMMUNITY",
        "papers": "WEEKLY:PAPER_WATCH",
        "runtime": "WEEKLY:OSS_WATCH",
    }[group]


def usage_for(row: dict[str, Any], group: str) -> str:
    text = record_text(row)
    did = row["discovery_id"]
    locator = str(row["source"].get("locator", "")).lower()
    if group in {"release", "community"}:
        return "PRIMARY"
    if group == "cyber":
        if did == "gap-postmerge-astra-cyber" or "aws" in text or "trusted hands" in text:
            return "SUPPORTING"
        return "PRIMARY"
    if group == "serving":
        if "vllm" in locator or "flashinfer" in locator:
            return "SUPPORTING"
        return "PRIMARY"
    if group == "papers":
        return "PRIMARY" if "2608.08654" in locator else "SUPPORTING"
    if group == "runtime":
        return "PRIMARY" if did == "gap-postmerge-qwen-code-runtime" else "SUPPORTING"
    raise ValueError(group)


def stage_advance(
    root: Path,
    state_path: Path,
    artifacts: dict[str, Path],
    *,
    label: str,
    review_kind: str,
    summary: str,
    recorded_at: datetime,
) -> dict[str, Any]:
    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_production_v2 as core
    from scripts import survey_stage_validation_v2 as stage_validation

    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(state_path)
    review_root = state_path.parent / "orchestration/v2/reviews"
    review_root.mkdir(parents=True, exist_ok=True)
    report_path = review_root / f"{state['lifecycle_state']}-core-stage-contract.json"
    reviews_path = review_root / f"{state['lifecycle_state']}-reviews.json"
    stage_validation.validate_stage(root, cfg, state_path, artifacts, report_path, recorded_at)
    reviews = {
        "reviews": [
            {
                "check_id": "CORE_STAGE_CONTRACT",
                "kind": "DETERMINISTIC",
                "executor": "survey_stage_validation_v2",
                "evidence": f"Current Core 0.15 deterministic stage contract passed for {label}.",
                "result_path": str(report_path.relative_to(root)),
            },
            {
                "check_id": f"W33_{label.upper()}_CHATGPT_REVIEW",
                "kind": review_kind,
                "executor": "ChatGPT/GPT-5.6-Sol",
                "evidence": summary,
            },
        ]
    }
    write_json(reviews_path, reviews)
    checkpoint = agent.build_stage_checkpoint(
        root,
        cfg,
        state_path,
        artifacts,
        reviews_path,
        summary,
        recorded_at,
        core.repository_commit_sha(root),
    )
    return agent.advance_with_checkpoint(root, cfg, state_path, checkpoint)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True)
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    sys.path.insert(0, str(root))

    from scripts import survey_agent_control_v2 as agent
    from scripts import survey_agent_tool_v2 as agent_tool
    from scripts import survey_architecture_v2 as architecture
    from scripts import survey_completeness_v2 as completeness
    from scripts import survey_discovery_v2 as discovery
    from scripts import survey_evidence_v2 as evidence
    from scripts import survey_production_v2 as core
    from scripts import survey_review_attention_v2 as review_attention
    from scripts import survey_schema_v2 as schema_gate
    from scripts import survey_screening_v2 as screening

    source_root = root / "sources/2026-W33"
    profile_path = source_root / "production-profile.json"
    state_path = source_root / "production-state.json"
    profile = load_json(profile_path)
    if profile["paths"]["work_branch"] != "weekly/2026-W33-v2-work":
        raise ValueError("runner invoked against wrong W33 work branch profile")
    state = load_json(state_path)
    if state["lifecycle_state"] != "ISSUE_INITIALIZED":
        raise ValueError(f"W33 rebuild requires ISSUE_INITIALIZED, got {state['lifecycle_state']}")
    if agent.validate_agent_state(root, core.load_json(root / core.DEFAULT_CONFIG), state):
        raise ValueError("initial W33 Production State is not safely resumable")

    restore_semantic_inputs(root)
    raw_path = source_root / "external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md"
    x_manifest = build_x_manifest(root, profile_path, raw_path)

    rows = old_discoveries(root)
    rows.extend(build_new_discoveries())
    rows.append(x_discovery())
    ids = [row["discovery_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("final Discovery set contains duplicate discovery_id")
    discovery_path = source_root / "discovery/discovery-v2.jsonl"
    write_jsonl(discovery_path, rows)
    screening.validate_discovery_set(rows, "2026-W33")
    discovery_acceptance = source_root / "discovery/discovery-accepted-v2.json"
    discovery.build_acceptance(root, discovery_path, x_manifest, "2026-W33", discovery_acceptance)

    t0 = datetime.now(timezone.utc).replace(microsecond=0)
    stage_advance(
        root, state_path, {"discovery-acceptance": discovery_acceptance},
        label="discovery", review_kind="AGENT_RESEARCH",
        summary="Rebuilt W33 Discovery from preserved broad collector coverage, exact post-merge Grok Raw, and bounded primary-source gap-fill; stale pre-postmerge X Discovery was removed.",
        recorded_at=t0,
    )

    # Screening under the current DISCOVERY_COLLECTED State.
    screening_work = source_root / "screening/v2/work/core015-rebuild"
    with agent_tool.current_stage_basis_override():
        package_path = screening.prepare_package(
            root, state_path, discovery_path, screening_work, core.repository_commit_sha(root)
        )
    package = load_json(package_path)
    results_dir = screening_work / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    by_id = {row["discovery_id"]: row for row in rows}
    all_decisions: list[dict[str, Any]] = []
    for batch in package["input"]["batches"]:
        batch_path = package_path.parent / batch["path"]
        batch_rows = screening.read_jsonl(batch_path)
        decisions = [screening_decision(row) for row in batch_rows]
        all_decisions.extend(decisions)
        result = {
            "schema_version": "2.0-rc1",
            "issue_id": "2026-W33",
            "batch_id": batch["batch_id"],
            "basis": screening.expected_result_basis(root, package_path, package, batch),
            "decisions": decisions,
        }
        write_json(results_dir / f"{batch['batch_id']}.json", result)
    with agent_tool.current_stage_basis_override():
        screening_acceptance = screening.accept_results(
            root,
            package_path,
            results_dir,
            source_root / "screening/v2/accepted",
            core.repository_commit_sha(root),
        )
    shutil.rmtree(screening_work)
    stage_advance(
        root, state_path, {"screening-acceptance": screening_acceptance},
        label="screening", review_kind="AGENT_RESEARCH",
        summary="Screened the complete rebuilt W33 Discovery set. Post-merge feature/cyber/serving/community/runtime and six-paper authorities are retained; all other broad candidates and carry-over items receive explicit DROP dispositions.",
        recorded_at=t0 + timedelta(seconds=10),
    )

    # Evidence, Edition Views, Materiality, Completeness under CANDIDATES_NORMALIZED.
    evidence_work = source_root / "evidence/v2/work/core015-rebuild"
    with agent_tool.current_stage_basis_override():
        evidence_package_path = evidence.prepare_evidence_package(
            root,
            state_path,
            discovery_path,
            screening_acceptance,
            evidence_work,
            core.repository_commit_sha(root),
        )
    evidence_package = load_json(evidence_package_path)
    evidence_results = evidence_work / "results"
    evidence_results.mkdir(parents=True, exist_ok=True)
    discovery_by_id = {row["discovery_id"]: row for row in rows}
    task_by_id: dict[str, dict[str, Any]] = {}
    for meta in evidence_package["tasks"]:
        task_path = evidence_package_path.parent / meta["path"]
        task = load_json(task_path)
        did = task["discovery_ids"][0]
        task_by_id[meta["evidence_task_id"]] = task
        card = build_evidence_card(root, evidence_package, meta, task, discovery_by_id[did])
        errors = evidence.validate_evidence_card(card, task, meta["sha256"], evidence_package)
        if errors:
            raise ValueError(f"generated Evidence Card invalid for {did}: {'; '.join(errors)}")
        write_json(evidence_results / Path(meta["path"]).name, card)
    with agent_tool.current_stage_basis_override():
        evidence_acceptance = evidence.accept_evidence_results(
            root,
            evidence_package_path,
            evidence_results,
            source_root / "evidence/v2/accepted",
            core.repository_commit_sha(root),
        )
    shutil.rmtree(evidence_work)

    evidence_accepted = load_json(evidence_acceptance)
    views_work = source_root / "evidence/v2/views/work/core015-rebuild"
    views_work.mkdir(parents=True, exist_ok=True)
    evidence_by_task = {row["evidence_task_id"]: row for row in evidence_accepted["results"]}
    for task_id, evrow in evidence_by_task.items():
        task = task_by_id[task_id]
        did = task["discovery_ids"][0]
        group = group_for(discovery_by_id[did])
        if group is None:
            raise ValueError(f"kept Evidence has no architecture group: {did}")
        materiality = "CONTEXT" if group == "papers" else "MATERIAL"
        window_relation = "OTHER" if group == "community" else (
            "PRE_WINDOW_RELEVANCE" if did == "gap-postmerge-astra-cyber" else "MAIN_EVENT"
        )
        view = {
            "schema_version": "2.0-rc1",
            "issue_id": "2026-W33",
            "research_profile": "WEEKLY",
            "evidence_task_id": task_id,
            "evidence_sha256": evrow["sha256"],
            "materiality": {"status": materiality, "rationale": why_this_issue(group)},
            "scope_dimensions": ["current relevance", "technical significance"],
            "profile_annotations": {
                "why_this_issue": why_this_issue(group),
                "window_relation": window_relation,
                "carry_over": False,
            },
        }
        card = load_json(evidence_acceptance.parent / "results" / evrow["filename"])
        errors = evidence.validate_edition_view(view, profile, evrow["sha256"], card["status"])
        if errors:
            raise ValueError(f"generated Edition View invalid for {did}: {'; '.join(errors)}")
        write_json(views_work / evidence.view_filename(task_id), view)
    with agent_tool.current_stage_basis_override():
        views_acceptance = evidence.accept_edition_views(
            root,
            profile_path,
            evidence_acceptance,
            views_work,
            source_root / "evidence/v2/views/accepted",
            core.repository_commit_sha(root),
        )
    shutil.rmtree(views_work)

    with agent_tool.current_stage_basis_override():
        ledger = evidence.build_materiality_ledger(
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            core.repository_commit_sha(root),
        )
    ledger_path = source_root / "materiality-ledger-v2.json"
    evidence.write_materiality_ledger(ledger_path, ledger)

    initial = {
        row["obligation_id"]: row
        for row in profile["research_scope"]["initial_obligations"]
    }
    named: dict[str, list[str]] = {}
    for row in rows:
        for oid in row["provenance"]["obligation_ids"]:
            named.setdefault(oid, []).append(row["discovery_id"])
    ledger_by_discovery = {row["discovery_id"]: row for row in ledger["rows"]}
    obligations = []
    for oid in sorted(set(initial) | set(named)):
        if oid in initial:
            dimension = initial[oid]["dimension"]
            description = initial[oid]["description"]
        else:
            dimension = "carry-over obligations" if "carry" in oid else (
                "technical significance" if "technical" in oid else "current relevance"
            )
            description = f"Resolve named Discovery obligation {oid} under the W33 research profile."
        d_ids = sorted(set(named.get(oid, [])))
        task_ids = sorted({
            task_id
            for did in d_ids
            for task_id in ledger_by_discovery[did]["evidence_task_ids"]
        })
        obligations.append({
            "obligation_id": oid,
            "dimension": dimension,
            "description": description,
            "status": "SATISFIED",
            "discovery_ids": d_ids,
            "evidence_task_ids": task_ids,
            "rationale": "The rebuilt W33 materiality ledger contains an explicit downstream disposition for every declaring Discovery; retained material is evidence/view bound and excluded/carry-over material is explicitly disposed.",
        })
    completeness_payload = {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "research_profile": "WEEKLY",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        },
        "overall_status": "READY",
        "obligations": obligations,
        "residual_limitations": [],
        "closure": None,
    }
    completeness_path = source_root / "profile-completeness-v2.json"
    schema_gate.validate_instance(
        completeness_payload,
        root / Path("schemas/profile-completeness-result.schema.json"),
        label="W33 Profile Completeness",
    )
    with agent_tool.current_stage_basis_override():
        errors = completeness.validate_profile_completeness(
            completeness_payload,
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            ledger_path,
            core.repository_commit_sha(root),
        )
    if errors:
        raise ValueError("generated W33 Completeness invalid: " + "; ".join(errors))
    write_json(completeness_path, completeness_payload)
    stage_advance(
        root,
        state_path,
        {
            "evidence-acceptance": evidence_acceptance,
            "edition-views-acceptance": views_acceptance,
            "materiality-ledger": ledger_path,
            "profile-completeness": completeness_path,
        },
        label="evidence", review_kind="AGENT_RESEARCH",
        summary="Primary-source follow-up was converted into factual Evidence cards with explicit vendor/project/community boundaries; every non-DROP Discovery has one Evidence task and Edition View, and Weekly completeness closes all named obligations.",
        recorded_at=t0 + timedelta(seconds=20),
    )

    # Candidate Matrix + complete Selection under EVIDENCE_REVIEWED.
    with agent_tool.current_stage_basis_override():
        matrix = architecture.derive_candidate_matrix(
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            ledger_path,
            completeness_path,
            core.repository_commit_sha(root),
        )
    matrix_path = source_root / "candidate-matrix-v2.json"
    architecture.write_candidate_matrix(matrix_path, matrix)
    matrix_by_did = {row["discovery_ids"][0]: row for row in matrix["rows"]}
    assignments = []
    for did in sorted(matrix_by_did):
        source_row = discovery_by_id[did]
        group = group_for(source_row)
        if group is None:
            raise ValueError(f"Matrix candidate lacks intended W33 group: {did}")
        assignments.append({
            "candidate_id": matrix_by_did[did]["candidate_id"],
            "disposition": "SELECTED",
            "rationale": why_this_issue(group),
            "architecture_usage": usage_for(source_row, group),
            "publication_role": None,
            "architecture_role": selection_role(group),
            "profile_extensions": {},
        })
    selection = {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "research_profile": "WEEKLY",
        "publication_profile": "WEEKLY_MAGAZINE",
        "selection_version": "core015-postmerge-rebuild-r1",
        "status": "ESTABLISHED",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        },
        "assignments": assignments,
        "summary": {
            "candidate_count": len(assignments),
            "disposition_counts": {"SELECTED": len(assignments)},
            "selected_count": len(assignments),
        },
    }
    selection_path = source_root / "candidate-selection-v2.json"
    schema_gate.validate_instance(selection, root / Path("schemas/candidate-selection-v2.schema.json"), label="W33 Selection")
    errors = architecture.validate_selection(root, selection, profile_path, matrix_path, completeness_path, ledger_path)
    if errors:
        raise ValueError("generated W33 Selection invalid: " + "; ".join(errors))
    write_json(selection_path, selection)
    stage_advance(
        root,
        state_path,
        {"candidate-matrix": matrix_path, "candidate-selection": selection_path},
        label="selection", review_kind="AGENT_EDITORIAL",
        summary="Candidate Selection retains only the post-merge architecture set: release wave, cyber governance, serving, community pulse, six-paper watch, and agent-runtime watch; every Matrix candidate is explicitly assigned.",
        recorded_at=t0 + timedelta(seconds=30),
    )

    # Proposed Architecture under SELECTION_COMPLETE.
    selection_by_cid = {row["candidate_id"]: row for row in assignments}
    package_meta = package_plan()
    package_rows: list[dict[str, Any]] = []
    for group_name in ("release", "cyber", "serving", "community", "papers", "runtime"):
        primary: list[str] = []
        supporting: list[str] = []
        boundaries = list(package_meta[group_name]["extra_boundaries"])
        for did, mrow in matrix_by_did.items():
            if group_for(discovery_by_id[did]) != group_name:
                continue
            cid = mrow["candidate_id"]
            usage = selection_by_cid[cid]["architecture_usage"]
            (primary if usage == "PRIMARY" else supporting).append(cid)
            boundaries.extend(mrow["remaining_boundaries"])
        package_rows.append({
            "package_id": package_meta[group_name]["package_id"],
            "title": package_meta[group_name]["title"],
            "purpose": package_meta[group_name]["purpose"],
            "primary_candidate_ids": sorted(primary),
            "supporting_candidate_ids": sorted(supporting),
            "must_cover_requirements": package_meta[group_name]["must"],
            "boundaries": list(dict.fromkeys(boundaries)),
            "drafting_order": len(package_rows) + 1,
            "profile_extensions": {},
            "publication_extensions": {},
        })
    package_rows.append({
        "package_id": "pkg-07-weekly-synthesis",
        "title": "今週の総括 — usable frontier becomes an end-to-end system property",
        "purpose": "Synthesize what changed at the system level across agent-oriented models, governed high-risk access, inference/serving, and runtime controls for long-lived agents.",
        "primary_candidate_ids": [],
        "supporting_candidate_ids": [],
        "must_cover_requirements": [
            "Answer what changed at the system level rather than naming a model winner.",
            "Connect open/local distribution to serving quality, harness design, permissions, memory architecture, and verification.",
            "Preserve the distinction between verified primary facts and community observations.",
        ],
        "boundaries": ["Cross-package synthesis may reuse only facts already owned by prior factual packages."],
        "drafting_order": 7,
        "profile_extensions": {},
        "publication_extensions": {},
    })
    proposed = {
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W33",
        "research_profile": "WEEKLY",
        "publication_profile": "WEEKLY_MAGAZINE",
        "status": "PROPOSED",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
        },
        "editorial_thesis": "W33 shows the usable AI frontier becoming an end-to-end system property: a rapid agent-oriented model release wave coincides with governed cyber-capability access, serving/latency engineering, and explicit runtime controls for long-lived agents.",
        "architecture_goals": [
            "Lead with the Aug 12-14 model release wave without inventing a cross-vendor benchmark leaderboard.",
            "Treat cyber capability as a capability-plus-governance infrastructure story.",
            "Make serving, locality, memory pressure, and time-to-support first-class technical dimensions.",
            "Give community signal a bounded reader-facing role with counter-signals and visibility limitations.",
            "Use research papers and OSS runtime changes as diagnostic/supporting layers rather than release-equivalent headlines.",
            "Close with a system-level synthesis instead of a model-winner verdict.",
        ],
        "page_plan": {
            "target_pages": 14,
            "max_pages": 16,
            "notes": "Six factual/watch packages plus a final cross-package synthesis. Avoid duplicate mini-articles for serving items already owned by Package 3.",
        },
        "packages": package_rows,
        "selected_exceptions": [],
        "profile_extensions": {},
        "publication_extensions": {},
        "human_review": {"reviewed_by": None, "reviewed_at": None, "review_reference": None},
    }
    architecture_path = source_root / "architecture-v2.json"
    schema_gate.validate_instance(proposed, root / Path("schemas/issue-architecture-v2.schema.json"), label="W33 Architecture")
    errors = architecture.validate_architecture(
        root, proposed, profile_path, completeness_path, ledger_path, matrix_path, selection_path, require_approved=False
    )
    if errors:
        raise ValueError("generated W33 Architecture invalid: " + "; ".join(errors))
    write_json(architecture_path, proposed)
    with agent_tool.current_stage_basis_override():
        review_summary = architecture.build_architecture_review_summary(
            root,
            profile_path,
            discovery_path,
            screening_acceptance,
            evidence_acceptance,
            views_acceptance,
            ledger_path,
            completeness_path,
            matrix_path,
            selection_path,
            architecture_path,
            core.repository_commit_sha(root),
        )
    if review_summary["readiness"]["status"] != "READY_FOR_ARCHITECTURE_REVIEW":
        raise ValueError("W33 Architecture Review Summary is blocked: " + repr(review_summary["readiness"]["errors"]))
    review_summary_path = source_root / "architecture-review-summary-v2.json"
    write_json(review_summary_path, review_summary)
    attention_path = source_root / "architecture-review-attention-v2.json"
    review_attention.build_attention(root, screening_acceptance, ledger_path, selection_path, attention_path, limit=50)
    stage_advance(
        root,
        state_path,
        {
            "issue-architecture": architecture_path,
            "architecture-review-summary": review_summary_path,
            "architecture-review-attention": attention_path,
        },
        label="architecture", review_kind="AGENT_EDITORIAL",
        summary="Proposed W33 Architecture integrates the post-merge model release wave with cyber governance, serving, community pulse, research watch, agent runtime, and a final end-to-end system synthesis. No Human Architecture decision has been recorded.",
        recorded_at=t0 + timedelta(seconds=40),
    )

    final_state = load_json(state_path)
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_errors = agent.validate_agent_state(root, cfg, final_state)
    if state_errors:
        raise ValueError("final W33 State invalid: " + "; ".join(state_errors))
    if (
        final_state["lifecycle_state"] != "ARCHITECTURE_ESTABLISHED"
        or final_state.get("terminal_reason") != "HUMAN_GATE_REACHED"
        or final_state.get("human_gates", {}).get("architecture_review") != "pending"
    ):
        raise ValueError(f"runner did not stop at pending Architecture Human Gate: {final_state}")

    counts = Counter(row["decision"] for row in all_decisions)
    audit = {
        "schema_version": "1.0",
        "issue_id": "2026-W33",
        "status": "PASS",
        "core_version": cfg["orchestrator_version"],
        "implementation_commit_sha": core.repository_commit_sha(root),
        "reuse_policy": "Reuse prior Raw/semantic research only; regenerate current-Core acceptances/checkpoints and never import old Production State or Human decisions.",
        "discovery_record_count": len(rows),
        "screening_counts": dict(sorted(counts.items())),
        "evidence_task_count": len(evidence_accepted["results"]),
        "selected_candidate_count": len(assignments),
        "architecture_package_count": len(package_rows),
        "authorities": {
            "x_manifest_sha256": core.sha256_file(x_manifest),
            "discovery_sha256": core.sha256_file(discovery_path),
            "discovery_acceptance_sha256": core.sha256_file(discovery_acceptance),
            "screening_acceptance_sha256": core.sha256_file(screening_acceptance),
            "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance),
            "edition_views_acceptance_sha256": core.sha256_file(views_acceptance),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
            "architecture_sha256": core.sha256_file(architecture_path),
            "architecture_review_summary_sha256": core.sha256_file(review_summary_path),
            "architecture_review_attention_sha256": core.sha256_file(attention_path),
        },
        "final_state": {
            "lifecycle_state": final_state["lifecycle_state"],
            "next_action": final_state["next_action"],
            "terminal_reason": final_state["terminal_reason"],
            "architecture_review": final_state["human_gates"]["architecture_review"],
        },
    }
    write_json(source_root / "core015-rebuild-audit.json", audit)
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
