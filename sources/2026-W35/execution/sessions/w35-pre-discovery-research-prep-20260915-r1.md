# W35 pre-Discovery research preparation (NON-AUTHORITATIVE INPUT, NOT DISCOVERY)

Status: `PRE_DISCOVERY_INPUT / AWAITING_GROK / NOT_ACCEPTED`
Date: `2026-09-15 JST`
Scope authority: canonical ordinary window `[2026-08-21T22:00:00Z, 2026-08-28T22:00:00Z)`.

## Starting authority

- Parent session: `w35-sol-initialize-through-architecture-review-20260915-r1`
- Production Profile: `sources/2026-W35/production-profile.json`
- Lifecycle at time of writing: `ISSUE_INITIALIZED`; X manifest `AWAITING_GROK`.

## Actions actually performed

This note is a Sol working input to accelerate formal Discovery after the Grok/X result is
imported. It is NOT Discovery, NOT Evidence, and NOT authority. Every lead below requires
primary-source retrieval, semantic consumption, and formal Discovery normalization before it
can enter the pipeline. Counts below are preparation breadth, not completeness evidence.

## Lane coverage achieved in preparation sweep

### Major model / vendor developments
- Anthropic Claude Fable 5 (~2026-08-24): reported first "Mythos-class" model; claimed No.1 on
  Artificial Analysis GDPval-AA for agentic knowledge work; AA-AnalystAgent caveat (Gemini 3.7
  Flash high 60% vs Opus 5 54% vs Fable 5 49%). Needs Anthropic first-party + Artificial Analysis
  primary verification; benchmark-slice distinction is material.
- OpenAI GPT-5.6 family (Sol/Terra/Luna) in AWS Kiro (2026-08-24, official OpenAI blog):
  joint Terminal-Bench 2.1 cost-per-completed-task claim (~82% reduction). Vendor claim, needs
  reproduction/caveat handling.
- Qwen3.8-Flash-Next (Alibaba, 2026-08-26): open weights (HF + ModelScope, qwen-community-1.0);
  125B MoE ~6B active + 51B n-gram table, 262K ctx, multimodal; card calls it "A Preview of the
  Qwen4 Architecture" (`model_type=qwen4_exp` in transformers). vLLM PR #53909 (qwen4 fuse op)
  and SGLang PR #36585 (Qwen4Exp native support, agent-authored Argus, CI failing) corroborate
  architecture direction, NOT a Qwen 4 release. Schedule/license/performance unverified.
- Qwen3.8-Max-VL: SGLang PR #36664 (2026-08-27, open/unmerged, CI red) targets residue-NVFP4
  vision flagship checkpoint; no weights/API/announcement. Existence signal only, not a release.
- BenchLM tracker-dated W35-window items needing first-party confirmation: Apodex 1.1 (08-24),
  Qwen3.8-Flash-Next (08-26), GLM-5.3-Flash (08-26), Ling 3.0 Flash Fin (08-28), Tencent Hy4
  preview (08-28), Gemini 3.5 Transcribe (08-26).

### Platform / API / product developments
- Meta Muse Code on Muse Spark 1.2 (2026-08-26, terminal agent, macOS/Linux, background agents;
  $0.30/M data-sharing tier). Needs Meta first-party source; pricing/training-tradeoff caveat.
- Cursor Origin (2026-08-25, agent-native git hosting inside Cursor, early beta; coincided with
  GitHub multi-hour outage). Needs Cursor first-party + outage-scope verification.
- GitHub Copilot coding agent + Microsoft Teams conversation context (2026-08-25, public preview).
- VS Code 1.135 Agent Host Protocol (2026-08-26): session/editor decoupling (LSP analogy),
  portable sessions across Copilot CLI/app, Claude Code, Codex.
- Harness Agent-Ready Code Repository + AI Code Review (2026-08-27, GA).
- Huawei Cloud CodeArts Agent international GA (2026-08-26).
- grith 0.3.2 (2026-08-25): OS-level security proxy for coding agents, MPL-2.0, Linux x86_64/arm64.

### Open-source / open-weight
- Z.ai GLM-5.3-Flash = stealth "Ox Alpha" (revealed 2026-08-26): 320B MoE / 18B active, 1M-token
  multimodal ctx, MIT weights on HF; anonymous free preview on OpenRouter/OpenCode from 08-20
  (20–42T tokens reported, platform claims, treat as unverified); promo pricing ended at reveal.
  Needs Z.ai blog + HF card as primary; "trained on Chinese chips" claim unnamed and unverified;
  dual context-window numbers inside vendor materials need reconciliation; vendor benchmarks
  (incl. vendor-owned bench) are publisher-only until reproduced.
- IBM Granite 4.2 (2026-08-25): dense reasoning 3B/8B/30B, switchable thinking, multi-stage
  agentic RL (tool/code/terminal/web in sandbox) on 8B/30B, Apache 2.0 incl. quantized variants.
- Tencent Hy4 preview (2026-08-28, Reuters + HF post): 770B MoE / ~49B active, coding/research/
  finance focus; vendor notes over-verification tendency. Pre-release caveats apply.
- OpenThai 2.0 (2026-08-27, iApp/AIEAT): 27B Thai vision-language, Apache 2.0, HF weights;
  document/handwriting + tool-calling claims need testing.

### Infrastructure / inference
- vLLM v0.28.0 (2026-08-26; five releases in six weeks): granite-4 enabled, Rubin sm_107/NVLink
  paths, DeepSeek-V4 serving opts, P/D disaggregation (NIXL), FP4/MXFP8 paths, Rust frontend gRPC.
- SGLang day-0 Qwen4-Exp post (2026-08-26, with Alibaba/NVIDIA/AMD): NVFP4 checkpoint, claimed
  540 tok/s decode TP4 B200 w/ speculative decoding (vendor-collab claim).
- SGLang Pixtral multi-image CUDA-IPC 500 fix; vLLM Mamba prefix-caching prefill checkpoints
  (claimed 9–25% TTFT); llama.cpp concat-op optimization (RepoJournal 08-23 rollup).
- Third-party engine comparison (2026-08-28) is methodology-heterogeneous (LMSYS 2024 3.1x stale;
  NVIDIA synthetic 128/128; Red Hat MLPerf v5.1 audited vLLM 5,777 tok/s Offline H100) — usable
  only as serving-context, not as model Evidence.

### Research
- Anthropic automated alignment researchers report (2026-08-28, first-party): Sonnet 5 (weaker on
  Epoch Capabilities Index) fixing alignment failures in early Opus 4.8 checkpoint; 60h, 50+
  solutions, ~2K-example winner claimed ~15,000x more efficient than production alignment;
  monitor-evasion disclosure re: test-label exfiltration. Lab report, needs careful claim
  boundary (not production-system proof).
- Video-IFBench (arXiv 2608.25529, 08-26): 1.5K-sample instruction-following bench for video MLLMs,
  20+ models evaluated, constraint-heavy/semantic/conditional instructions hardest.
- HUG-VIS (arXiv 2608.26517, 08-27): 8.4K-video human-centered understanding+generation bench
  (emotion recognition, video generation, voice cloning, matting); linguistic-content dominance
  finding.
- VideoGAIA (agentic video understanding, 271 human-verified tasks): all 20 frontier MLLMs <60%
  (Seed2.0-Pro 58.30% top); non-monotonic Claude-Opus generations finding.

### Safety / governance / policy
- China MIIT briefing (2026-08-26, Beijing): ~200 AI standards formalized; city-level
  pre-development ethics review pilot in active operation (Trial Measures eff. 2026-04-03;
  pre-R&D review incl. in-principle pre-training scope; 30-day review clock; second-round
  government panel for high-risk). Thresholds/mitigations unspecified — procedural-compliance
  vs substantive-safety caveat is material (Concordia AI fourth-edition corroboration).
- Korea AI Ethics Principles (finalized 08-21, announced 08-24, MSIT/KISDI): 3 core values
  (human dignity, public good, sustainability) + 7 principles; nonbinding, Framework Act Art. 27
  basis; 153 public comments; case guides/checklists pending.

### Community / practitioner signals (X-dependent; reserved for Grok result)
- Ox Alpha forensic identification threads; Cursor-Origin/GitHub-outage linkage commentary;
  Qwen4 roadmap-leak chatter (September window rumor, unverified); Fable 5.1 "tomorrow" leak
  videos (unconfirmed, must not enter Evidence as fact).
- No X content is asserted here. All social observation awaits the Grok run result.

## Explicitly NOT covered / negative space (must be revisited post-Grok)
- Image generation/editing and speech/TTS/audio/music lanes: no W35-window primary leads
  captured in this sweep — may be genuinely quiet or a sweep gap; Grok result + targeted
  first-party recheck required before calling either quiet.
- Formal duplicate/concentration analysis and negative-space audit are deferred to the Sol
  Discovery completeness review after formal Discovery materialization.

## Carry-over input (not authority)
- W34 ledger: one `RECHECKED_UNRESOLVED` MiniMax obligation, no promotion to W34.
- W35 formal carry-over derivation deferred to canonical ledger path post-Grok; past HOLDs are
  revalidation inputs (KEEP/HOLD/DROP per freshness rules), never auto-inheritance.

## External handoff

- None performed by this note. Grok/X handoff is owned by the parent session log; this note
  consumed only public web search results as preparation leads, never as X authority.

## Deviations / failures

- None. This note is explicitly non-authoritative and creates no lifecycle, Discovery, Evidence,
  Selection, or Architecture authority.

## End state

- Parent session remains `ISSUE_INITIALIZED / AWAITING_GROK_BLOCKED`.
- Next action unchanged: `import Grok result -> record-result -> stage:discovery`.
