# W42 primary bundle — Reflection Beam + Elorian Glimpse (bodies consumed/confirmed, 2026-10-17)

Collector run: `20261017T063300Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-17T06:52:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Reflection Beam availability (Oct 16, 2026) — BODY CONSUMED (reflection.ai/blog/beam-is-available)
- URL: https://reflection.ai/blog/beam-is-available (page shows Oct 16, 2026, 6 min read).
- X: @reflection_ai 2026-10-16 13:01 UTC in-window.
- Core facts (source-backed):
  - First open-weight model; weights on HF under Apache 2.0 (501B total / 23B active MoE per HF blog + search).
  - Precisions: BF16, FP8, NVFP4 + speculative drafter (DFlash2); fused kernels; day-0 Transformers/vLLM/SGLang/Unsloth/Axolotl/TokenSpeed/Dynamo.
  - Model card = final benchmarks; Safety Technical Report = full methodology (both referenced, bodies NOT read here — gap).
  - Mirror CLI harness (open-source-friendly, Rust core + Python frontend, resumable/parallel/MCP/Python ext); tested with Pi/OpenCode/Hermes.
  - Customization: RL recipes (1.3B sandboxes peak run; 883k vCPUs across 23 clusters GCP/AWS); OpenEnv upstream; self-distillation recipes forthcoming.
  - Platforms: 40+ (AWS/Nscale/Baseten/Cloudflare/CoreWeave/Databricks/Fireworks/GCP/Hermes/LM Studio/Foundry/Modal/Nebius/NIM/Ollama/OpenCode/OpenRouter/Oracle/Together/Vercel/W&B); on-prem Dell/HPE.
  - Context: Oct 5 intro post (501B/23B, coding/reasoning/agentic) is background; Oct 16 availability is the W42 event.
- HF blog (search-confirmed Oct 16): 501B/23B, 1M ctx, text-in, 5 effort levels (low→max), Rust harness, Apache 2.0.
- Timestamp: IN-WINDOW (Oct 16). AUTHORITY_CONSUMED for availability/license-formats/platforms; benchmarks/card/safety: UNCONSUMED gap.

## 2. Elorian Glimpse (Oct 16, 2026) — BODY SEARCH-CONFIRMED (elorian.ai/blog/introducing-glimpse)
- URL: https://elorian.ai/blog/introducing-glimpse (Elorian, Oct 16, 2026 per search).
- X: @AndrewDai 2026-10-16 17:08 UTC in-window (developer本人); @ElorianAI same window.
- Claims (search-confirmed, vendor):
  - Visual-thinking model: reasons IN visual space; visual scratch space (zoom/re-scan/track; 8→14 fps re-scan example; 0.9s window; window-edge 2.2s→5.13s traces).
  - Agent: end-to-end multimodal tools (code/image-transform/video), subagents exchanging text/visual/representations.
  - Benchmarks (vendor): frontier-level; beats GPT-6 Astra on scientific chart + short-video (vendor); HSS (Scale AI, 522 tasks, human 93.1%, Astra 53.6, Glimpse 46.36, Opus 5.5 44.6, Sol 46.6) — vendor-built benchmark, Glimpse does NOT top it (credibility note per OrcaRouter).
  - Efficiency: small team, few-hundred GPUs, post-trained on open-weights base (base undisclosed); $0.60/$3 per 1M (94% cheaper than Astra per press); 262k ctx (OpenRouter) — context figure from secondary, verify.
  - Access: API + chat UI today; research preview.
- Timestamp: IN-WINDOW (Oct 16). Status: CAPTURED_BUT_UNCONSUMED (official blog not fully read here). Evidence must fetch blog + HSS paper + pricing page + independent harness.

## Gaps
- Beam model card benchmarks, safety report, HF file list: not consumed.
- Glimpse base model, context window, independent reproduction: not consumed.
- Arena/Agent Arena ranks for Beam: secondary only.
