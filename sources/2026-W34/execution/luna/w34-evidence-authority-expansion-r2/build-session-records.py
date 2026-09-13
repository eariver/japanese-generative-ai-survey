#!/usr/bin/env python3
"""Build the immutable, edition-local evidence expansion records.

The script reads only the already-accepted W34 Evidence task records and the
new session's capture manifest.  It does not modify any canonical Evidence,
Selection, Architecture, or production-State artifact.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


SESSION = Path(__file__).resolve().parent
REPO = SESSION.parents[4]
RAW = SESSION / "raw"
OLD_EVIDENCE = REPO / "sources/2026-W34/evidence/v2/accepted/917f6b5d958d0782e9994a699899145c7fc5f11e0cc9525625385427ce721452/tasks"
WINDOW = {
    "start": "2026-08-14T18:00:00-04:00",
    "end": "2026-08-21T18:00:00-04:00",
    "timezone": "America/New_York",
}


# One row per non-DROP task.  The reasons are deliberately candidate-local:
# an unresolved result records what was searched and what boundary remains.
RESULT_ROWS = """
C001|PARTIALLY_VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|The official Z.ai release-notes body was captured and contains a GLM-5.3-Flash entry, but the W34 start-boundary time and the flagship-release and adoption delta are not isolated.|keep with explicit chronology and flagship-scope qualifier
C002|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|First-party Anthropic news and research paths were attempted; no authoritative page or technical record for the token-choice watermark claim was found or captured.|hold pending first-party technical evidence; do not promote the claim
C003|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|OpenRouter and Stripe first-party announcements were captured and identify the Aug19 joining or acquisition event.|retain with date-only boundary qualifier
C004|VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|OpenAI first-party post and Help article were captured and state that global rollout begins Aug18.|retain with date-only boundary qualifier
C005|VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|OpenAI first-party safety publication was captured and dated Aug18; the pacing-model claim is directly addressed.|retain with date-only boundary qualifier
C006|VERIFIED|2026-08-17|IN_WINDOW_DATE_ONLY|The official CISA KEV repository mirror was captured; the CVE-2025-62593 record names Ray-Project, gives dateAdded 2026-08-17, and records the code-injection vulnerability.|retain as CISA-backed security event
C007|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|Alipay first-party launch, product, and API paths were attempted; no authoritative launch page or API record for the full-stack agentic-commerce claim was captured.|hold pending first-party product or API evidence
C008|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|OpenAI first-party post was captured and directly documents Zero Data Retention and Private Safety Processing for frontier models.|retain with date-only boundary qualifier
C009|VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|Anthropic first-party research page was captured and directly describes protein-design and analytical-chemistry results.|retain with date-only boundary qualifier
C010|PARTIALLY_VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|AWS release and technical-blog primary pages were located and reviewed through web access, but local shell retrieval timed out and no local body bytes were captured.|retain only the AWS-located claim with blocked-capture limitation
C011|PARTIALLY_VERIFIED|2026-08|IN_WINDOW_DATE_ONLY|The Anthropic API release-notes body was captured and contains out-of-beta Skills and Files API and Computer Use entries, but the combined GA chronology and exact date for the full task claim are not isolated.|retain with scope and chronology qualifier
C012|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Slack first-party article and changelog body were captured and directly describe Code channels for agents.|retain with date-only boundary qualifier
C013|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Liquid AI first-party post was captured and directly describes LFM2.5-DSpark speculative-decoding checkpoints.|retain with date-only boundary qualifier
C014|PARTIALLY_VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The OpenAI cookbook body was captured and confirms a gpt-image-2 transparent-background example, but broader preview availability and edge-quality caveats are not established.|retain only the directly evidenced transparent-background capability
C015|PARTIALLY_VERIFIED|UNRESOLVED|W34_RELEVANCE_UNRESOLVED|Tencent's official UI-Mate README was captured and confirms the project, but release or tag chronology and a W34 availability delta are not explicit.|retain with chronology qualifier
C016|OUT_OF_WINDOW|2026-08-24|OUT_OF_WINDOW_POST|The official X Business article was captured and dated Aug24, after the W34 end boundary.|exclude from W34 package; retain only as post-window chronology
C017|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The OpenAI API changelog body was captured and contains the GPT-5.6 Sol pricing reduction entry.|retain with date-only boundary qualifier
C018|VERIFIED|2026-08-17|IN_WINDOW_DATE_ONLY|The official Google Firebase migration guide was captured and states that Imagen models are deprecated or shutting down as early as Aug17 with migration to Gemini image models.|retain with date-only boundary qualifier
C019|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Mistral's first-party Agentic Search announcement was captured and directly describes the release.|retain with date-only boundary qualifier
C020|PARTIALLY_VERIFIED|2026-08-14|IN_WINDOW_DATE_ONLY|Pika's first-party post was captured and dated Aug14, but exact release time relative to the 22:00Z start and complete model-level detail are not resolved.|retain with start-boundary qualifier
C021|VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|Stability's first-party post was captured and directly documents the Stable Audio workflow expansion.|retain with date-only boundary qualifier
C022|VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|DeepSeek's official changelog body is dated 2026-08-21 and directly identifies the DeepSeek-V4-Flash-Vision-Exp release.|retain with end-boundary qualifier
C023|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|xAI's first-party Amazon Bedrock announcement was captured and directly describes Grok 4.6 availability there.|retain with date-only boundary qualifier
C024|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|xAI's first-party Gemini Enterprise announcement was captured and dated Aug21, but the exact publication time relative to the W34 cutoff is not available.|retain with end-boundary qualifier
C025|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|xAI's first-party Grok Build announcement was captured and states web and mobile availability across plans.|retain with date-only boundary qualifier
C026|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|OpenAI and NVIDIA first-party infrastructure and newsroom paths were attempted; no authoritative record matching the PORTS-Pike and NVIDIA-SB energy-infrastructure claim was captured.|hold pending a specific first-party announcement
C027|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|Google and Gemma first-party announcement and documentation paths were attempted; no authoritative download-count record for the claimed 1B threshold was captured.|hold pending a first-party metric source
C028|PARTIALLY_VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Micron's first-party investor-release URL was located and reviewed, but the local response was a Cloudflare access page rather than the release body.|retain only with blocked-capture limitation
C029|PARTIALLY_VERIFIED|2026-08-11|OUT_OF_WINDOW_PRE|NVIDIA's official technical blog was captured and confirms Nemotron 3.5 Lightning, but the AWS SageMaker JumpStart release is dated Aug11 and the task's W34 delta is not established.|exclude the pre-window release from W34; retain as context only
C030|PARTIALLY_VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The AWS primary blog and What's New pages were located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C031|PARTIALLY_VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The AWS Dogwood primary blog and documentation were located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C032|VERIFIED|2026-08-17|IN_WINDOW_DATE_ONLY|OpenRouter's first-party Activity Dashboard announcement was captured and dated Aug17.|retain with date-only boundary qualifier
C033|VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|OpenRouter's first-party Visual Image Benchmarks article was captured and dated Aug21 and directly describes the benchmark launch.|retain with end-boundary qualifier
C034|OUT_OF_WINDOW|2026-07-20|OUT_OF_WINDOW_PRE|The official AWS connector documentation was located; the relevant connector version and domain/date filter material is dated before W34, with no distinct W34 delta found.|exclude the pre-window feature from W34; retain only as context
C035|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|OpenAI and NVIDIA first-party infrastructure and newsroom paths were attempted; no authoritative Vera Rubin racks or training-stack record matching the task was captured.|hold pending a specific first-party technical source
C036|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|DeepMind's first-party games-research article was captured and dated Aug21, but the partnership and long-horizon research boundary is date-only and not independently separated within the page.|retain with scope qualifier
C037|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|MiniMax first-party newsroom and product paths were attempted; no authoritative Design-agent platform release body was captured.|hold pending first-party product evidence
C038|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|SenseTime first-party newsroom and product paths were attempted; no authoritative SenseNova-U1.5 release or technical record was captured.|hold pending first-party model evidence
C039|PARTIALLY_VERIFIED|UNRESOLVED|W34_RELEVANCE_UNRESOLVED|Qwen's official README was captured and identifies Qwen3.8, but release or tag chronology and the W34 local-inference delta are not explicit.|retain with chronology qualifier
C040|PARTIALLY_VERIFIED|UNRESOLVED|W34_RELEVANCE_UNRESOLVED|DeepSeek's official pricing page was captured and lists deepseek-v4-pro, but an effective publication date and before/after W34 price delta are not explicit.|retain only the current pricing/model fact with change-date qualifier
C041|OUT_OF_WINDOW|2026-08-13|OUT_OF_WINDOW_PRE|The official Google post was captured and dated Aug13, before the W34 start; no separate W34 adoption or usage delta was found.|exclude the pre-window release from W34; retain only as context
C043|PARTIALLY_VERIFIED|UNRESOLVED|W34_RELEVANCE_UNRESOLVED|Unsloth's official repository README was captured and lists Qwen3.8 and GGUF support, but no dated W34 optimization release or exact Qwen3.8 artifact delta is established.|retain with chronology and artifact qualifier
C044|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|The official MLX repository README was captured, but it does not document the claimed W34 speedup or abliteration wave and no dated primary artifact was found.|hold pending a dated first-party artifact
C045|VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|OpenAI's data-controls guide and API changelog body were captured; the changelog records the regional-processing update and the guide documents the control surface.|retain with end-boundary qualifier
C046|PARTIALLY_VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The AWS primary technical blog was located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C047|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Runway's captured changelog body contains the Aug20 Workflow Support in Runway MCP entry and its workflow list, edit, and run capabilities.|retain with date-only boundary qualifier
C048|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|The existing official GitHub Releases raw record for Transformers v5.15.1 was retained unchanged; it is dated 2026-08-19 and lists the patch fixes.|regression-only primary record; do not replace the existing raw
C050|OUT_OF_WINDOW|2026-08-13|OUT_OF_WINDOW_PRE|The AutoDesign arXiv record and PDF were captured and submitted Aug13, before the W34 start.|exclude from W34 package; retain only as pre-window research context
C051|PARTIALLY_VERIFIED|2026-04-18|SOURCE_PRE_WINDOW_W34_EVENT_UNRESOLVED|The arXiv record and USENIX paper PDF were captured, but the paper's publication or discussion event is outside or not resolved to the W34 window; the W34 scam-experiment delta is not independently dated.|retain only with publication and chronology qualifier
C052|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|OpenAI Computer History documentation and release notes were captured and directly document the rollout and privacy behavior.|retain with date-only boundary qualifier
C053|OUT_OF_WINDOW|2026-07-31|OUT_OF_WINDOW_PRE|The primary Seedance 2.5 chronology available to the search is July31, before W34, with no distinct W34 availability record captured.|exclude from W34 package; retain only as context
C054|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|MediaTek first-party press and technical-blog paths were attempted; no authoritative automotive-edge Qwen3.8 deployment record was captured.|hold pending a first-party deployment source
C055|PARTIALLY_VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|The official MITRE CVE API body was captured and dates CVE-2026-24301 publication and public disclosure to Aug18, but it does not substantiate the full CoSnitch exploit-chain detail.|retain the CVE-backed security fact with secondary-detail exclusion
C056|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|Meta first-party newsroom and AI product paths were attempted; no authoritative Mac-app, Muse Spark, or system-wide-dictation release body was captured.|hold pending first-party product evidence
C057|PARTIALLY_VERIFIED|2026-08-17|IN_WINDOW_DATE_ONLY|The Motion Picture Association's first-party policy page was captured and explicitly records the Aug17 MPA-ByteDance MOU and shared guardrail framework, but a ByteDance first-party copy was not captured.|retain with one-sided-authority qualifier
C058|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|U.S. government first-party White House, State, and Commerce paths were attempted; no authoritative record for the claimed pressure on allies over a China-led AI framework was captured.|hold pending a government statement or filing
C065|PARTIALLY_VERIFIED|2026-08-26|OUT_OF_WINDOW_POST|The official Z.ai GLM-5.3-Flash page was retrieved as an app shell and its article is post-window; it confirms the later identity context but cannot backdate the W34 anonymous Ox Alpha observation.|keep the W34 observation separate; do not backdate the post-window identity
C066|OUT_OF_WINDOW|2026-08-26|OUT_OF_WINDOW_POST|The official xAI Grok Bot plans page was captured and dated Aug26, after W34.|exclude from W34 package; retain only as post-window chronology
C073|OUT_OF_WINDOW|2026-08-24|OUT_OF_WINDOW_POST|The available official or product chronology places InferenceX AgentX v3 on Aug24, after W34; no in-window primary release was captured.|exclude from W34 package; retain only as post-window chronology
C080|VERIFIED|2026-08-15|IN_WINDOW_DATE_ONLY|The arXiv record and PDF for LAPF were captured and submitted Aug15 within W34.|retain as primary research record
C081|VERIFIED|2026-08-15|IN_WINDOW_DATE_ONLY|The arXiv record and PDF for agent inheritance and creative-agent governance were captured and submitted Aug15 within W34.|retain as primary research record
C082|VERIFIED|2026-08-16|IN_WINDOW_DATE_ONLY|The arXiv record and PDF for EgoGazeLite were captured and submitted Aug16 within W34.|retain as primary research record
C083|VERIFIED|2026-08-17|IN_WINDOW_DATE_ONLY|The arXiv record and PDF for embodied-agent security were captured and submitted Aug17 within W34.|retain as primary research record
C085|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|arXiv and GitHub first-party search paths for the agent-harness or DarwinX evolution claim were attempted; no authoritative dated record matching the task was captured.|hold pending a dated primary research or repository record
C087|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|The AWS AgentCore Gateway primary blog was located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C088|PARTIALLY_VERIFIED|2026-08-14|IN_WINDOW_DATE_ONLY|The AWS Nova Forge primary blog was located and reviewed for the Aug14 reward-function claim, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C091|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|Adobe's first-party release body was captured and directly documents Firefly Audio GA expansion.|retain with date-only boundary qualifier
C092|VERIFIED|2026-08-15/2026-08-21|IN_WINDOW_DATE_ONLY|The OpenMOSS README was captured with the Aug15 technical-report entry and the ms-swift README was captured with the Aug21 integration delta.|retain with separate report and integration dates
C093|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|arXiv and project-site search paths for 4DAnyone were attempted; no authoritative dated paper or project record matching the task was captured.|hold pending primary paper or project evidence
C095|VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|OpenAI release notes body was captured with the Aug21 plugin-discovery, time-aware-answer, and long-conversation UX update block.|retain with end-boundary qualifier
C096|VERIFIED|2026-08-20|IN_WINDOW_DATE_ONLY|The official Codex changelog body was captured with the Apple Messages plugin entry in the Aug20 update block.|retain with date-only boundary qualifier
C097|UNRESOLVED|UNRESOLVED|W34_RELATION_UNRESOLVED|Kling official documentation and product paths were attempted; no primary launch body for the combined Kling 3.0 Turbo, MCP, and CLI claim was captured.|hold pending an official Kuaishou or Kling announcement
C098|VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|Liquid AI's first-party QAD post was captured and dated Aug19 and directly documents the LFM2.5 Q4_0 quantization-aware-distillation checkpoints.|retain with date-only boundary qualifier
C099|VERIFIED|2026-08-18|IN_WINDOW_DATE_ONLY|GitHub's first-party changelog body was captured and directly documents managed settings for Copilot in JetBrains.|retain with date-only boundary qualifier
C100|VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|GitHub's first-party Slack changelog body was captured and directly documents the new Copilot experience in Slack.|retain with end-boundary qualifier
C101|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|GitHub's first-party Teams changelog body was captured and directly documents shared agentic work, but the exact publication time relative to the cutoff is not available.|retain with end-boundary qualifier
C102|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|Google Cloud's first-party Antigravity enterprise page was located and reviewed, but local shell retrieval timed out and no local body bytes were captured.|retain only with blocked-capture limitation
C103|PARTIALLY_VERIFIED|2026-08-21|IN_WINDOW_DATE_ONLY|Google Cloud's first-party intelligent-delegation article was located and reviewed, but local shell retrieval timed out and no local body bytes were captured.|retain only with blocked-capture limitation
C104|PARTIALLY_VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|AWS Security's first-party authorization-propagation blog was located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
C105|PARTIALLY_VERIFIED|2026-08-19|IN_WINDOW_DATE_ONLY|AWS's first-party asynchronous AgentCore blog and documentation were located and reviewed, but local shell retrieval timed out and no local AWS body bytes were captured.|retain only with blocked-capture limitation
"""


LOCATOR_OVERRIDES = {
    "C002": ["https://www.anthropic.com/news", "https://www.anthropic.com/research"],
    "C007": ["https://www.alibabagroup.com/en/news", "https://open.alipay.com/", "https://open.alipay.com/mcp"],
    "C026": ["https://openai.com/news/", "https://www.nvidia.com/en-us/news/"],
    "C027": ["https://blog.google/technology/ai/", "https://ai.google.dev/gemma"],
    "C035": ["https://openai.com/index/", "https://www.nvidia.com/en-us/"],
    "C037": ["https://www.minimax.io/news", "https://www.minimaxi.com/"],
    "C038": ["https://www.sensetime.com/en/news", "https://www.sensetime.com/"],
    "C054": ["https://www.mediatek.com/press", "https://www.mediatek.com/tek-talk-blogs"],
    "C056": ["https://about.fb.com/news/", "https://ai.meta.com/"],
    "C058": ["https://www.whitehouse.gov/", "https://www.state.gov/", "https://www.commerce.gov/"],
    "C073": ["https://www.inferencex.com/", "https://agentx.inferencex.com/"],
    "C085": ["https://arxiv.org/search/?query=DarwinX+agent", "https://github.com/search?q=DarwinX+agent&type=repositories"],
    "C093": ["https://arxiv.org/search/?query=4DAnyone&type=all", "https://www.4danyone.com/"],
    "C097": ["https://app.klingai.com/global/", "https://app.klingai.com/global/dev/document-api/"],
    "C048": ["https://github.com/huggingface/transformers/releases/tag/v5.15.1", "https://api.github.com/repos/huggingface/transformers/releases/tags/v5.15.1"],
    "C095": ["https://help.openai.com/en/articles/6825453-chatgpt-release-notes"],
}

EXISTING_C048_PATH = REPO / "sources/2026-W34/collectors/github-releases/runs/20260902T121634Z/raw/huggingface__transformers.json"
EXISTING_C048_REPO_PATH = "sources/2026-W34/collectors/github-releases/runs/20260902T121634Z/raw/huggingface__transformers.json"
CROSS_TASK_SOURCES = {
    "C095": [
        {
            "path": "sources/2026-W34/execution/luna/w34-evidence-authority-expansion-r2/raw/c052-openai-release-notes.html",
            "url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
            "source_class": "first_party_product_release_notes",
            "relationship": "same captured first-party page; Aug21 UX block is task-specific",
        }
    ],
}
NON_SUBSTANTIVE = {
    "c001-zai-glm53-blog.html": "application shell without article body",
    "c028-micron-research-labs.html": "Cloudflare challenge body, not the release",
    "c055-cve-record.html": "application shell without CVE record data",
    "c055-msrc-record.html": "application shell without advisory data",
    "c065-zai-glm53-flash.html": "application shell without article body",
}


def parse_result_rows():
    out = {}
    for line in RESULT_ROWS.strip().splitlines():
        task, result, date, relation, reason, disposition = line.split("|", 5)
        out[task] = {
            "result": result,
            "publication_release_date": date,
            "w34_window_relation": relation,
            "unresolved_reason": reason,
            "next_disposition": disposition,
        }
    return out


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def header_metadata(path: Path):
    if not path.exists():
        return {"http_status": "NOT_CAPTURED", "content_type": None}
    text = path.read_text(errors="replace")
    statuses = re.findall(r"^HTTP/[^ ]+\s+(\d{3})", text, re.MULTILINE)
    status = statuses[-1] if statuses else "UNKNOWN"
    types = re.findall(r"^content-type:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)
    return {"http_status": status, "content_type": types[-1].strip() if types else None}


def load_targets():
    records = []
    with (SESSION / "capture-targets.tsv").open(newline="") as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if not row or not row[0]:
                continue
            task, url, source_class, filename = row
            body = RAW / filename
            headers = RAW / f"{filename}.headers"
            stderr = RAW / f"{filename}.curl-stderr"
            size = body.stat().st_size if body.exists() else 0
            meta = header_metadata(headers)
            # A truncated/empty body is recorded as an attempted fetch but not
            # mistaken for an HTTP success merely because a proxy sent 200.
            status = meta["http_status"]
            if size == 0:
                status = "000"
            substantive = size > 0 and status == "200" and filename not in NON_SUBSTANTIVE
            records.append(
                {
                    "task": task,
                    "url": url,
                    "source_class": source_class,
                    "filename": filename,
                    "raw_path": f"sources/2026-W34/execution/luna/w34-evidence-authority-expansion-r2/raw/{filename}",
                    "body_bytes": size,
                    "sha256": sha256(body) if body.exists() and size else None,
                    "retrieved_at_utc": iso_mtime(body) if body.exists() and size else (iso_mtime(headers) if headers.exists() else None),
                    "http_status": status,
                    "content_type": meta["content_type"],
                    "actual_authority_bytes": substantive,
                    "capture_outcome": (
                        "EXACT_BODY_CAPTURED" if substantive else
                        ("NON_SUBSTANTIVE_SUCCESS_BODY" if size and status == "200" else
                         ("HTTP_ERROR_RESPONSE_CAPTURED" if size else "HTTP_000_OR_TIMEOUT_NO_BODY"))
                    ),
                    "non_substantive_reason": NON_SUBSTANTIVE.get(filename),
                    "curl_stderr_path": f"sources/2026-W34/execution/luna/w34-evidence-authority-expansion-r2/raw/{filename}.curl-stderr" if stderr.exists() else None,
                }
            )
    return records


def load_tasks():
    tasks = {}
    for path in OLD_EVIDENCE.glob("*.json"):
        task = json.loads(path.read_text())
        if not task.get("discovery_ids"):
            continue
        discovery_id = task["discovery_ids"][0]
        match = re.search(r"c(\d+)$", discovery_id)
        if not match:
            continue
        task_code = f"C{int(match.group(1)):03d}"
        task["_task_code"] = task_code
        tasks[task_code] = task
    return dict(sorted(tasks.items(), key=lambda item: int(item[0][1:])))


def legacy_discovery_locators(task):
    locators = []
    for source in task.get("source_records", []):
        locator = source.get("locator")
        if locator and locator not in locators:
            locators.append(locator)
    return locators


def task_primary_locators(task_code, target_rows):
    rows = target_rows.get(task_code, [])
    if rows:
        return list(dict.fromkeys(row["url"] for row in rows))
    return LOCATOR_OVERRIDES.get(task_code, [f"search://first-party-authority/{task_code.lower()}"])


def source_record_for_row(row):
    return {
        "url": row["url"],
        "raw_path": row["raw_path"] if row["body_bytes"] else None,
        "source_class": row["source_class"],
        "retrieved_at_utc": row["retrieved_at_utc"],
        "http_status": row["http_status"],
        "body_bytes": row["body_bytes"],
        "sha256": row["sha256"],
        "capture_outcome": row["capture_outcome"],
        "actual_authority_bytes": row["actual_authority_bytes"],
        "non_substantive_reason": row["non_substantive_reason"],
        "curl_stderr_path": row["curl_stderr_path"],
    }


def build_provenance(target_rows):
    counts = Counter(row["capture_outcome"] for row in target_rows)
    return {
        "schema_version": "0.1",
        "issue_id": "2026-W34",
        "session_id": "w34-evidence-authority-expansion-r2",
        "purpose": "Exact primary-source retrieval provenance for pre-Human Evidence authority expansion",
        "capture_method": "curl -L --silent --show-error --max-time 20/30 with response headers, raw body, and stderr preserved per target",
        "retrieval_clock": "filesystem mtime recorded in UTC for the captured body or response headers",
        "source_policy": "First-party, official, primary technical, government/security, then strong secondary only if primary authority is unavailable; X/DailyX/Grok remain discovery signals.",
        "targets_total": len(target_rows),
        "capture_outcome_counts": dict(sorted(counts.items())),
        "actual_authority_bytes_count": sum(row["actual_authority_bytes"] for row in target_rows),
        "unique_actual_authority_sha256_count": len({row["sha256"] for row in target_rows if row["actual_authority_bytes"]}),
        "records": target_rows,
    }


def build_ledger(tasks, target_rows, decisions):
    by_task = defaultdict(list)
    for row in target_rows:
        by_task[row["task"]].append(row)
    records = []
    for code, task in tasks.items():
        decision = decisions[code]
        captured = [source_record_for_row(row) for row in by_task.get(code, [])]
        actual_paths = [row["raw_path"] for row in by_task.get(code, []) if row["actual_authority_bytes"]]
        cross_sources = []
        for item in CROSS_TASK_SOURCES.get(code, []):
            path = REPO / item["path"]
            if path.exists():
                cross = dict(item)
                cross.update(
                    {
                        "retrieved_at_utc": iso_mtime(path),
                        "body_bytes": path.stat().st_size,
                        "sha256": sha256(path),
                        "actual_authority_bytes": True,
                        "capture_outcome": "EXACT_BODY_CAPTURED",
                    }
                )
                cross_sources.append(cross)
                actual_paths.append(item["path"])
        if code == "C048" and EXISTING_C048_PATH.exists():
            cross_sources.append(
                {
                    "url": "https://github.com/huggingface/transformers/releases/tag/v5.15.1",
                    "raw_path": EXISTING_C048_REPO_PATH,
                    "source_class": "official_github_release_api_snapshot",
                    "relationship": "pre-existing accepted primary raw retained for regression",
                    "retrieved_at_utc": iso_mtime(EXISTING_C048_PATH),
                    "body_bytes": EXISTING_C048_PATH.stat().st_size,
                    "sha256": sha256(EXISTING_C048_PATH),
                    "actual_authority_bytes": True,
                    "capture_outcome": "RETAINED_EXISTING_EXACT_BODY",
                }
            )
            actual_paths.append(EXISTING_C048_REPO_PATH)
        captured.extend(cross_sources)
        source_classes = sorted({item["source_class"] for item in captured})
        accessibility = (
            "LOCAL_EXACT_BODY_CAPTURED" if any(item.get("actual_authority_bytes") for item in captured) else
            ("PRIMARY_LOCATOR_CAPTURE_ATTEMPTED_NO_LOCAL_AUTHORITY_BODY" if captured else "NO_LOCAL_PRIMARY_BODY_CAPTURED")
        )
        verification_target = task.get("verification_targets") or [task.get("source_records", [{}])[0].get("summary_text", task.get("source_records", [{}])[0].get("title", code))]
        title = task.get("source_records", [{}])[0].get("title", code)
        discovery_id = task.get("discovery_ids", [f"w34-event-{code.lower()}"])[0]
        search_query = f"first-party authority search for {title}"
        records.append(
            {
                "discovery_id": discovery_id,
                "evidence_task_id": task["evidence_task_id"],
                "screening_decision": task.get("screening_basis", {}).get("decisions", [{}])[0].get("decision"),
                "claim_identity": {
                    "candidate_code": code,
                    "title": title,
                    "target_claim": verification_target[0],
                    "legacy_discovery_locators": legacy_discovery_locators(task),
                },
                "target_claim": verification_target[0],
                "verification_attempted": True,
                "verification_attempted_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                "primary_source_search_queries": [search_query],
                "attempted_primary_source_locators": task_primary_locators(code, by_task),
                "actual_retrieved_authority_paths": list(dict.fromkeys(actual_paths)),
                "source_accessibility": accessibility,
                "source_class": source_classes,
                "source_records": captured,
                "publication_release_date": decision["publication_release_date"],
                "w34_window_relation": decision["w34_window_relation"],
                "result": decision["result"],
                "unresolved_reason": decision["unresolved_reason"],
                "next_disposition": decision["next_disposition"],
            }
        )
    counts = Counter(record["result"] for record in records)
    return {
        "schema_version": "0.1",
        "issue_id": "2026-W34",
        "session_id": "w34-evidence-authority-expansion-r2",
        "verification_scope": "All 80 non-DROP Evidence tasks from the accepted W34 Screening authority",
        "window": WINDOW,
        "source_policy": "X/DailyX/Grok are discovery or locator signals only; captured technical authority must be first-party, official, primary research, or government/security authority where available.",
        "coverage": {
            "non_drop_tasks_expected": 80,
            "records_written": len(records),
            "verification_attempted_records": sum(record["verification_attempted"] for record in records),
            "all_records_have_task_specific_attempt": all(record["verification_attempted"] and record["attempted_primary_source_locators"] for record in records),
        },
        "result_counts": dict(sorted(counts.items())),
        "records": records,
    }


def main():
    decisions = parse_result_rows()
    tasks = load_tasks()
    if len(tasks) != 80:
        raise SystemExit(f"expected 80 Evidence tasks, found {len(tasks)}")
    if set(tasks) != set(decisions):
        raise SystemExit(f"decision/task mismatch: tasks={sorted(set(tasks)-set(decisions))}, decisions={sorted(set(decisions)-set(tasks))}")
    target_rows = load_targets()
    target_by_task = defaultdict(list)
    for row in target_rows:
        target_by_task[row["task"]].append(row)
    provenance = build_provenance(target_rows)
    ledger = build_ledger(tasks, target_rows, decisions)
    (SESSION / "source-retrieval-provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    (SESSION / "verification-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"records": len(ledger["records"]), "result_counts": ledger["result_counts"], "capture_outcomes": provenance["capture_outcome_counts"], "actual_authority_bytes": provenance["actual_authority_bytes_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
