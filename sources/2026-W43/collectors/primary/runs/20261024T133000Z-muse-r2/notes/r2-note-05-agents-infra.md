# W43 r2 consumption note 05 — agents/infra priority bodies (DC-07, SUBSTANTIVELY_CONSUMED 2026-10-24)

## Anthropic Claude Duet (Oct 21) — announcement read in full
- Research preview, waitlist, US Pro/Max first; same usage limits (background checks + large tasks consume more). iOS/Android/claude.ai; VM + own browser (laptop/phone off); checks every few hours (limit-aware); type/voice single thread; memory/skills/apps carried over.
- Model/safety: Opus 5.5; trustworthy-agents framework (Code/Chrome lineage); Managed-Agents credential design (never sees passwords/tokens); auto-mode classifier approval; browser-use prompt-injection defenses; red-team + external pen-test + bug bounty; new dedicated classifier + safety prompt (blocks CC/gov-ID tier; health/finance only on explicit instruction).
- Capability: morning brief; 6000+ Marketplace connectors (Gmail/Slack, QuickBooks/Stripe, Gusto, LinkedIn, Docusign, HubSpot, Canva, Shopify); Link (virtual card) + Shop Pay; 1Password coming soon; securities/money-movement off-limits even with approval; disconnect per app; work-first (personal errands weaker, browser not yet visible).
- Distribution signals (not merged): related Oct 22 Google Cloud (Claude Platform managed) + Oct 23 Cowork Enterprise + Duet Safety article. Auto-mode default (X 2113360845409583307) is separate locator, not body-consumed.

## DeepSeek V4.1-Flash-1017 (Oct 17) — API docs read
- Wish-driven programming; RL self-feedback; end-to-end project builds (Forbidden City 3D, racing game, Portal 2 Godot, Valley of Ages); Harness/CodeBuddy/WorkBuddy optimized (Harness ≥v0.2.1-rc.1); web/app/API live.
- Search & Fetch open: $0.75/1k calls; free via server-side Harness/Claude Code/Codex until Oct 31 16:00 UTC. OSS: HF deepseek-ai/DeepSeek-V4.1-Flash-1017 + ModelScope; footnotes pin harnesses (mini-swe-v2, Claude-Code, official leaderboards tbench.ai/terminal-bench-science/swe-marathon/posttrainbench/vals) + temp 1.0/top-p/max effort conventions.

## DeepInfer (Oct 20 announce; repo created Oct 16 07:47:23Z OUT) — README read
- 21.5k stars / 2.4k forks / 4 commits; Apache-2.0. Offline-only OSS cut for V4.1-Flash; kernels FlashMLA/DeepGEMM/DeepEP/TileKernels/DeepSelect/TileLang; Attention DP/balanced CP, MoE EP+EPLB; DSpark + confidence-scheduled verification (ENABLE_MTP_VARLEN=1, NEXTN_DECODE default 5); SWA bounded replay (YOCO compact, KEEP 140); async scheduling default; batch-invariant + deterministic sampling (NVIDIA); structured outputs; SM100 + Ascend 950; MISSING KV cache / VE-prefill-decode disagg / load balancing (explicit non-inclusion); build GCC≥13/Python 3.12/CUDA 13/CANN 9.2; default checkpoint 1017; benches 4 SM100 prefill + 64 decode; vLLM-derived + SGLang/TRT-LLM credit. Repo OUT vs announce IN kept distinct.

## NVIDIA Bolt E4B (Oct 23) — research page read
- Published Oct 23 + tech report; Gemma 4 E4B + Nemotron post-train; 64K ctx (corrected — r1 1M was wrong family figure); 35 langs (+140 base); 40% vs Nano avg, 80% fewer tokens; tables consumed (Tau2 55.1 vs 38.5 Gemma; RULER 87.0; Brevity 82.5; IF 63.8/84.8; GaRAGe 42.6; RelyTool 63.2); RTX/Jetson Q4_K_M llama.cpp AIPerf tables; RLVR/RLHF NeMo-RL/Gym (2:1 non-reasoning); DFlash +21% vs Gemma MTP; checkpoints GGUF/DFlash/BF16/NVFP4; deploy HF/Ollama/LM Studio/Unsloth/Canonical/Jetson/In-Game; Reachy Mini Orin Nano 8GB + Cosmos 3 Edge demo. Weights/data/recipes open; OpenMDW-1.1 (OSI unproven).

## GitHub platform (Oct 19/22/23) — changelogs read
- Teams Oct 23: @github issue/PR + thread context → reproduce/test/fix/PR; legacy app renamed deprecated, retires Nov 16; consolidated app required. Metrics Oct 23: totals_by_client (opencode/claude_code/codex/zed/copilot_cli/github_app/cloud_agent/code_review/vscode/jetbrains/other) + request/session/tokens/totals_by_model + selection mode (user/auto/product/other/unknown); server-side; enterprise/org 1-day/28-day; additive. Oct 19: model policy API + deprecations (list unpinned). Oct 22: VS Sep update + custom skills/agents/MCP in metrics + global default GA + impact dashboard; Oct 21 CLI OAuth. Oct 15 multi-repo = OUT background.

## TanStack AI 1.0 (Oct 23) — blog read
- Stable core, harness experimental 0.x; 23 adapters + openaiCompatible; 8 UI frameworks; 143 contributors; codemod + upgrade together + threadId required + 3 old UI pkgs dropped + saved-data migration; harness (durable sessions/steer/follow-up, typed agents, plugins, background work) + runCli coding agent (permissions NOT sandbox; ACP/MCP only with packages); AG-UI routes. Production ask is stable core.
