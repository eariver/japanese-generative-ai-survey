# W43 primary bundle 02 — open weights and version successors (claim-level, 2026-10-24)

Collector run: `20261024T120000Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-24T12:00:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Moonshot Kimi K3.1 Pro (Oct 23, 2026, 17:15 ET X / 21:15Z) — IN-WINDOW EDGE, BODY SEARCH-CONFIRMED
- URLs: https://www.kimi.ai/blog/kimi-k3-1-pro (tech blog), https://x.com/Kimi_Moonshot/status/2113680701770068068067 (Oct 23 17:15 ET, 2.3M views), https://platform.moonshot.ai/docs/pricing/chat.
- Claims (vendor + secondary, unvalidated):
  - 2.8T total / 104B active MoE, 1M ctx, multimodal; Highspeed 2-3x faster at 2x price (cache hits same price).
  - Live on kimi.ai/apps/Work/Code/API; weights BY Nov 4 (NOT yet open — must not call current release open-weights availability).
  - Pricing $2/$10 per 1M (same as GPT-6.1 Sol, half Opus 5.5 per Simon Willison).
  - Benchmarks vendor-stated: Terminal-Bench 4.0 65.7% (vs Opus 5.5 66.4, Astra 58.2); OfficeQA Pro v2 64.4 SOTA; hallu 23.4→8.3% on Kimi Hallu Bench Hard; AA Intelligence Index 55, 4th, +11 over K3; Terminal-Bench 67% in AA (vs Sonnet 5.5 64%).
  - Cyber: hacking-related training data removed; TNW Oct 23.
- Timestamp: IN-WINDOW (Oct 23 21:15Z, 45 min before exclusive cutoff Oct 23 22:00Z). Status: CAPTURED_BUT_UNCONSUMED (tech blog not fully read; HF weights absent by design until Nov 4).
- Chronology: API/announce Oct 23 is W43 event; future weights release is NOT W43 availability.

## 2. DeepSeek V4.1-Flash-1017 (Oct 17, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://api-docs.deepseek.com/news/news261017 (release 2026/10/17), https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017, X @deepseek_ai 2026-10-17, Vercel AI Gateway changelog.
- Claims:
  - Minor update to V4.1-Flash (Sep 10): stronger bench, faster task completion, shorter outputs (Pareto).
  - Live web/app/API; MIT weights on HF/ModelScope; GreenBitAI 4bit-paged, Baekpica VQ GGUF same-day community converts.
  - DeepSWE v1.1 77% vs 74.2% (vendor); HLE 36.8-42.6 vs 36.8-39.1; Terminal-Bench tables in card.
  - Free via Harness/Claude Code/Codex integrations until Oct 31 16:00 UTC; billing from Oct 31.
- Status: CAPTURED_BUT_UNCONSUMED (API docs/card not fully read). Evidence must fetch card + harness version + license file.

## 3. StepFun Step 5 Preview weights — OUT-OF-WINDOW BACKGROUND (Oct 15), Oct 22 meetup is community signal only
- URLs: https://www.stepfun.com/step-5-preview, https://huggingface.co/stepfun-ai/Step-5-Preview, MarkTechPost 2026-10-16, Featherless 2026-10-15, FAV0 2026-10-19, foundercal Oct 22 SF launch night.
- Facts:
  - 600B/27B MoE, 1M ctx, vision; FP8/BF16 on HF/ModelScope since Oct 15 (before W43 window).
  - Oct 22 SF launch night + Together Compute is community/distribution, NOT new model event.
- Disposition: BACKGROUND only. Must NOT be presented as W43 launch. thehype calendar Oct 18 date reflects secondary listing, not primary release; primary Oct 15 controls.

## 4. NVIDIA Nemotron 3.5 Bolt E4B 4GB (Oct 23, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-E4B-4GB/ (Published Oct 23 + tech report PDF), https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB, X @NVIDIAAI 2026-10-23 15:41 ET, https://ollama.com/library/nemotron-3.5-bolt:e4b.
- Claims:
  - 8B total / 4B effective (Gemma 4 E4B + Nemotron post-train); conversational + multi-turn agentic; Jetson Orin Nano 8GB local (Reachy Mini demo with Cosmos vision).
  - Weights/data/recipes open; OpenMDW-1.1 per card (OSI approval NOT established — do not call OSI-open); NIM also image/audio.
  - Bench vendor: Tau2 55.1 vs 38.5 Gemma, RULER 87.0, SPEED splits; Unsloth 0.1.910-beta same-day support (Flint/MOSS-Image/Bolt 4B).
- Status: CAPTURED_BUT_UNCONSUMED (tech report PDF unopened; license file unopened). Evidence must fetch PDF + HF license + Ollama blobs.

## Gaps
- Kimi tech blog full body, DeepSeek card full tables, Nemotron report PDF, StepFun card: UNCONSUMED.
- No independent repro for Kimi/DeepSeek/Nemotron in this pass.
