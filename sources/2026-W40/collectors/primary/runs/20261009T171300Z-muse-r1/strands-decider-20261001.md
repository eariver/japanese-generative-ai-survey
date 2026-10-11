# Collector raw — Strands: Decider 2B (Oct 1)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://strandsagents.com/blog/introducing-strands-decider/
- source_type: PRIMARY_OFFICIAL
- published: 2026-10-01 (vendor blog header Oct 1, 2026; SiliconANGLE/GateNews same date)

## Consumed claims (claim-level)

1. EVENT: Strands Labs (AWS) released Strands Decider 2B Oct 1, 2026: small open-source decision model for agentic workflows; v19 pinned for W40 (repo notes v21 exists later; W40 must cite v19, not retroactive head). (PRIMARY_FACT: release, date, version pin)
2. ARCHITECTURE: Qwen3.5-2B torso with LM head removed, pointer head (~1M params) scoring options; rank-16 LoRA; single parallel pass, no text generation; typed choice/score + reliability scores; multiple questions per prompt in one pass. (PRIMARY_FACT as vendor architecture description)
3. PERF (vendor-run, attribution required): JevBench public-set accuracy/calibration 3rd-of-33 in 2B class (1st-of-30 excluding just-over-2B); median local latency ~115ms RTX 3090 (~153ms M3 MacBook small tasks), linear in task size; 100% easy JevBench tasks. Training trajectory/Brier charts on page. (VENDOR_CLAIM)
4. DISTRIBUTION: Code github.com/strands-labs/strands-decider; weights Hugging Face StrandsAgents; training data + scripts released; CLI `strands-decider ask`; Strands agent intervention example (before_tool_call -> Proceed/Deny/Confirm/Guide). Apache-2.0 per Sol register (verify SPDX in repo at Evidence stage; page states open source without inline SPDX). (PRIMARY_FACT as distribution statement with license recheck noted)
5. POSITIONING: Hybrid agents (LLM hard decisions + decider rote decisions); model routing/tool selection/evals/guardrails/memory/policy; not for coding/chat/summarization. (VENDOR_CLAIM as vendor guidance)

## Boundaries / unresolved

- Distinct from Cloudflare Clef (27B/9B, Oct 1) and Ollama /v1/systemone (Sep 29 interface); do not merge benchmarks/latencies/licenses.
- "Open weights/training code" needs repo-commit pin at Evidence; current default may show v21.
- marc-brooker origin story (AWS Strands Labs) corroborated by SiliconANGLE; not primary authority alone.
