# W43 primary bundle 03 — inference, serving and edge runtime (claim-level, 2026-10-24)

Collector run: `20261024T120000Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-24T12:00:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. DeepSeek DeepInfer (Oct 20, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://github.com/deepseek-ai/DeepInfer, X @deepseek_ai 2026-10-20 09:30 ET, PyPI deepinfer 0.1.0 (Oct 20), TNW 2026-10-20, SCMP 2026-10-21, NeoTeo 2026-10-22.
- Claims (vendor + secondary, unvalidated):
  - Apache 2.0; production inference framework behind DeepSeek large-scale services; offline inference only in OSS cut.
  - Supports ONE model: DeepSeek-V4.1-Flash (V4.1-Flash-1017); vLLM-derived + SGLang/Tensor ideas; attention DP, optimized kernels, DSpark speculative decoding, deepseek-recipe Rust codec companion.
  - Hardware: NVIDIA SM100 (Blackwell datacenter) + Huawei Ascend 950; NO Hopper, NO KV-cache system per secondary; 64x datacenter Blackwell bench (vendor, unreproduced); serves 155T tokens/day cluster claim via X commentator (NOT primary).
- Status: CAPTURED_BUT_UNCONSUMED (repo README not fully read; no local run). Evidence must fetch README + release tag + hardware reqs + license file.

## 2. Local distribution same-week (supporting)
- Vercel AI Gateway: V4.1-Flash-1017 live (changelog, Oct 17 snapshot).
- Ollama: nemotron-3.5-bolt:e4b blobs (DFlash, Qwen3 arch note, tool/vision); Unsloth 0.1.910-beta (Flint/MOSS-Image/Bolt 4B, desktop chat-only option).
- Status: LOCATOR_ONLY. Versions need pinning in Evidence.

## 3. Qwen-Image-2.1 Pro/Turbo — OUT-OF-WINDOW BACKGROUND, do not relabel
- Facts: Turbo weights Oct 9, Pro/Turbo APIs Oct 9, docs Oct 14; Sep 20 blog for 2.1 base; GitHub News entries Oct 9.
- thehype Oct 16 date is secondary listing, NOT primary release. W42 already tracked Turbo as background.
- Disposition: BACKGROUND only. A genuinely new W43 Qwen image event requires fresh primary dated in-window.

## Gaps
- DeepInfer repo files, PyPI sdist, hardware docs: UNFETCHED.
- Throughput/latency independently unreproduced.
