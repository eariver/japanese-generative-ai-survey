#!/usr/bin/env python3
"""Retrieve official/product primary bodies for non-arxiv tasks + regression alternates.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
"""
from __future__ import annotations
import json, time, hashlib, re
from pathlib import Path
import urllib.request

REPO = Path(".").resolve()
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
OUT_DIR = REPO / EXEC_REL / "evidence-bodies" / "official"
PROV_PATH = REPO / EXEC_REL / "evidence-bodies" / "official-provenance.jsonl"

# discovery_id -> list of urls to try in order (first = configured locator, rest = alternates)
TARGETS: dict[str, list[str]] = {
    "w34-event-c001": ["https://docs.z.ai/release-notes/new-released"],
    "w34-event-c017": ["https://developers.openai.com/api/docs/changelog", "https://openai.com/api/pricing/"],
    "w34-event-c019": ["https://mistral.ai/news/agentic-search/"],
    "w34-event-c021": ["https://stability.ai/news-updates/sharing-a-new-way-to-work-with-stable-audio"],
    "w34-event-c022": ["https://api-docs.deepseek.com/updates/"],
    "w34-event-c025": ["https://x.ai/api/changelog"],
    "w34-event-c039": ["https://github.com/QwenLM/Qwen3.8"],
    "w34-event-c041": ["https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/"],
    "w34-event-c045": ["https://developers.openai.com/api/docs/changelog"],
    "w34-event-c046": ["https://aws.amazon.com/blogs/machine-learning/aws-vector-solutions-build-agentic-ai-where-your-data-lives/"],
    "w34-event-c047": ["https://runway.com/changelog"],
    "w34-event-c048": ["https://api.github.com/repos/huggingface/transformers/releases?per_page=100"],
    "w34-event-c052": ["https://help.openai.com/en/articles/6825453-chatgpt-release-notes"],
    "w34-event-gap-alibaba-kimi-k3-model-studio": ["https://www.alibabacloud.com/help/en/model-studio/newly-released-models"],
    "w34-event-gap-alibaba-wan30-model-studio": ["https://www.alibabacloud.com/help/en/model-studio/newly-released-models"],
    "w34-event-gap-aws-agentcore-memory-json": ["https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-json-payloads/"],
    "w34-event-refresh-apple-grpo-beyond-english": ["https://machinelearning.apple.com/research/grpo-beyond-english"],
    "w34-event-refresh-apple-human-like-behaviors-llms": ["https://machinelearning.apple.com/research/human-like-behaviors-llms"],
    "w34-event-refresh-apple-scaling-laws-mixture-pretraining": ["https://machinelearning.apple.com/research/scaling-laws-mixture-pretraining"],
    "w34-event-refresh-cohere-culture-funnel": ["https://cohere.com/blog/the-culture-funnel-you-cant-align-what-isnt-in-the-data"],
    "w34-event-refresh-kimi-code-cli-v038-v037": ["https://www.kimi.com/code/docs/en/kimi-code/whats-new.html"],
    "w34-event-refresh-openai-defenders-window": ["https://openai.com/index/the-defenders-window"],
    "w34-event-refresh-openai-replit-gpt56-luna": ["https://openai.com/index/replit"],
    # regression / high-signal gap fills (alternate first-party surfaces)
    "w34-event-c004": ["https://openai.com/index/introducing-chatgpt-for-teens", "https://openai.com/index/chatgpt-for-teens"],
    "w34-event-c010": ["https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments/", "https://aws.amazon.com/bedrock/agentcore/"],
    "w34-event-c011": ["https://www.anthropic.com/news/claude-computer-use", "https://docs.anthropic.com/en/docs/agents-and-tools/computer-use", "https://docs.anthropic.com/en/docs/build-with-claude/skills", "https://www.anthropic.com/news/skills", "https://www.anthropic.com/news/files-api"],
    "w34-event-c008": ["https://openai.com/index/zero-data-retention", "https://openai.com/index/introducing-private-safety-processing"],
    "w34-event-c002": ["https://www.anthropic.com/news/watermarking", "https://www.anthropic.com/news/eu-ai-act-transparency"],
    "w34-event-c066": ["https://x.ai/news/grok-bot", "https://x.ai/news/grok-bot-included-with-more-plans"],
    "w34-event-c023": ["https://aws.amazon.com/about-aws/whats-new/2026/08/grok-4-6-bedrock/", "https://x.ai/news/grok-4-6"],
    "w34-event-c024": ["https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/grok", "https://x.ai/news/grok-4-6"],
    "w34-event-c030": ["https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-gpt-5-6-cross-region/"],
    "w34-event-c006": ["https://www.cisa.gov/known-exploited-vulnerabilities-catalog"],
}

def slug(url: str) -> str:
    s = re.sub(r"^https?://", "", url).rstrip("/")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:100]

def fetch(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (W34-Evidence Muse-Spark-1.3)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    done = set()
    if PROV_PATH.exists():
        for line in PROV_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                done.add((d["discovery_id"], d["url"]))
    n_new = 0
    for did, urls in TARGETS.items():
        for url in urls:
            if (did, url) in done:
                continue
            try:
                status, data = fetch(url)
                ok = status == 200 and len(data) > 500
            except Exception as e:
                with PROV_PATH.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"discovery_id": did, "url": url, "outcome": "RETRIEVAL_FAILED",
                                         "error": str(e)[:300],
                                         "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, sort_keys=True) + "\n")
                print(f"FAIL {did} {url} {str(e)[:100]}")
                time.sleep(1)
                continue
            if ok:
                fname = f"{did}__{slug(url)}.html"
                # json/github api may be json; keep extension by content sniff
                if data[:1] == b"{" or data[:1] == b"[":
                    fname += ".json"
                fpath = OUT_DIR / fname
                fpath.write_bytes(data)
                with PROV_PATH.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"discovery_id": did, "url": url, "outcome": "CAPTURED",
                                         "http_status": status, "byte_count": len(data),
                                         "sha256": hashlib.sha256(data).hexdigest(),
                                         "raw_path": str(fpath.relative_to(REPO)),
                                         "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, sort_keys=True) + "\n")
                print(f"OK {did} {url} {len(data)}")
                n_new += 1
            else:
                with PROV_PATH.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"discovery_id": did, "url": url, "outcome": "RETRIEVAL_FAILED",
                                         "error": f"http {status} len {len(data)}",
                                         "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, sort_keys=True) + "\n")
                print(f"FAIL {did} {url} http {status} len {len(data)}")
            time.sleep(1)
    print(f"new captures logged: {n_new}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
