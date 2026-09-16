# W36 pre-Discovery research preparation (NON-AUTHORITATIVE INPUT, NOT DISCOVERY)

Status: `PRE_DISCOVERY_INPUT / AWAITING_GROK / NOT_ACCEPTED`
Date: `2026-09-16 UTC`
Scope authority: canonical ordinary window `[2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)` (ET `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)`, JST `[2026-08-29T07:00:00+09:00, 2026-09-05T07:00:00+09:00)`), end-exclusive.

## Starting authority

- Parent session: `w36-sol-initialize-through-architecture-review-20260916-r1`
- Production Profile: `sources/2026-W36/production-profile.json`
- Lifecycle at time of writing: `ISSUE_INITIALIZED`; X manifest `AWAITING_GROK`.

## Actions actually performed

This note is a Sol working input to accelerate formal Discovery after the Grok/X result is
imported. It is NOT Discovery, NOT Evidence, and NOT authority. Every lead below requires
primary-source retrieval, semantic consumption, and formal Discovery normalization before it
can enter the pipeline. Counts below are preparation breadth, not completeness evidence.
Search snippets were never treated as Evidence. No quota was filled; weak lanes are marked
`NONE_FOUND` / `UNCERTAIN`.

## Lane coverage achieved in preparation sweep

### A. Foundation Models / Reasoning
- OpenAI GPT-6 Astra (2026-09-03, ordinary-window): first model OpenAI designates Critical
  cybersecurity capability under its Preparedness Framework; claims ExploitBench 100% plus
  two zero-days found in internal V8 port; alignment/monitorability claims (53% fewer
  sev-3+ flags vs GPT-5.6 Sol on 54K Codex-task simulation; adversarial CoT-evasion caveat).
  Primary candidates: `https://openai.com/index/safety-overview-gpt-6-astra/`,
  `https://openai.com/index/path-to-astra/` (2026-09-01), Astra system card / deployment
  safety hub. Vendor claims only until reproduced; benchmark-contamination caveat is material.
- IFM/MBZUAI K2 Horizon fleet (2026-09-03, ordinary-window): six models 0.9B→375B-A23B,
  Apache 2.0 weights+code, checkpoints/data-recipes/logs published; 36B-A4B Mixture-of-Value
  Attention, 524K native context; SOTA-at-scale claims for 0.9B/3.7B/7B. Primary candidate:
  `https://ifm.ai/blog/k2/` + HF org `IFM`. Cross-lists to lanes G/H. Local-run caveat:
  llama.cpp upstream support still in progress (project fork referenced).
- Gnani Evon 3.3 30B open-weights + Artha stack (unveiled New Delhi 2026-08-28): boundary
  event straddling window open; exact UTC time vs `2026-08-28T22:00:00Z` needs classification
  (ordinary-window vs background). Primary needed: Gnani official announcement.
- Tencent Hy4 preview (2026-08-28): already a W35 ordinary-window item; for W36 it is
  background/carry context only, not a fresh candidate.

### B. Agents / Coding / Harness / Computer Use
- Z.ai ZCode desktop coding agent (2026-09-01, ordinary-window): standalone app on GLM-5.3;
  independent hands-on (Flavio Copes, 2026-08-31, boundary) reports Z Code Bench 31.4% high
  effort vs Opus 4.8 29.5% vs Fable 5 39.5% with token-efficiency note. Primary needed:
  Z.ai official ZCode post; Copes original as independent-test lead (not authority).
- Microsoft Copilot Studio GitHub Copilot harness GA (2026-09-02 post, August updates):
  reasoning-heavy agent harness + skills/memory/MCP/knowledge; Claude Sonnet 5 + GPT-5.5 Chat
  as primary models. Primary candidate: Microsoft Copilot Blog 2026-09-02.
- Kilo Code for JetBrains multi-agent control room (2026-09-01): parallel agents, isolated
  git worktrees, Run Configurations, PR tracking. Primary needed: Kilo blog + repo/docs.
- Muse Code GA/programmability claims (community report 2026-08-31, boundary): UNCONFIRMED;
  must not enter Evidence as fact without Meta first-party source.
- Huawei Cloud CodeArts Agent APAC commercial GA (2026-08-28 16:16 CST = 08:16 UTC):
  BEFORE window open → background, not ordinary-window.

### C. Multimodal Foundation Models
- ByteDance Lance 3B (2026-08-29, ordinary-window): natively unified understanding+generation
  (image/video understanding, generation, cross-modal editing), 3B active, Apache 2.0, HF
  weights, claimed 128-A100 full run. Primary needed: ByteDance Research post + HF repo.
  Third-party aggregator copy only so far; license/architecture unverified.
- World Labs Atlas omni world model (2026-09-01/02, ordinary-window): text/image/video/3D
  autoregressive diffusion transformer; video generation + 3D reconstruction + robot sim in one;
  early access only, no pricing/public API. Primary candidate: `https://www.worldlabs.ai/blog/atlas`.

### D. Image Generation / Editing
- Google Pics (2026-09-01, ordinary-window): Workspace image creation/editing app (pics.new;
  Docs/Slides now, Drive later) on Nano Banana models; object segmentation, in-image
  text edit/translation, 2K/4K upscale, collaboration; gradual rollout (Rapid from 09-01,
  Scheduled from 09-15). Primary candidate: Google Workspace blog 2026-09-01.
- Meta Muse Image agentic image model via fal (2026-09-01, ordinary-window): planner+diffuser,
  web-search references, self-correction; top-5 Arena claim across three tracks. Primary needed:
  Meta official model page + fal model page; Arena standing needs independent check.
- Second pass performed (per Weekly overlay C/D/E/F rule): both D leads above are
  ordinary-window with first-party anchors identified.

### E. Video Generation / Editing
- fal H3 Max (2026-09-01, ordinary-window): post-trained MiniMax H3, ~3s wall for 5s video,
  claimed 35x official-endpoint throughput / 15x vs comparable quality; promo pricing to 09-07.
  Vendor+platform claims; leaderboard refs (Design Arena / Artificial Analysis as of 08-26)
  need recheck. Primary candidate: fal press release 2026-09-01.
- Alibaba Wan 3.0 distribution wave (2026-08-28→08-31, ordinary-window distribution activity):
  integrations (PowerDirector/A2E/PixelDojo/DeepInfra/Medeo/Buzzy); 30s native claim; 4K and
  open-weights/Apache claims DISPUTED by third-party analysis → must not assert. Primary needed:
  Alibaba Cloud official announcements.
- DreamX-Creator 1.0 (arXiv 2608.31106, 2026-08-31, ordinary-window): 7B native joint
  audio-video generation + 2K refiner; open release claimed. Primary candidate: arXiv paper.
- Background only (pre-window): Gemini Omni 1.1 Flash stable (08-27), FastH3 Preview v1 (08-27),
  Sand.ai MAGI Preview (08-05). Preview-shutdown note (omni-flash-preview → 09-30, replacement
  1.1-flash) is post-cutoff-adjacent context, not an ordinary-window event.
- Second pass performed: E lane has multiple ordinary-window leads.

### F. Speech / Audio / Music Generation
- `UNCERTAIN` / no dedicated W36-window generative-audio model release captured in this sweep.
  Adjacent serving-side signal only: SGLang-Omni v0.1.4 (09-xx) MiniMax Music 3 support —
  serving coverage, not a model release. Qwen3-TTS speed-cost third-party analysis (08-19) is
  pre-window background. Grok result + targeted first-party recheck required before calling
  this lane quiet.

### G. Open Weight / Local AI / Quantization
- K2 Horizon (09-03): Apache 2.0 fleet on HF with FP8/GGUF builds; day-zero vLLM/SGLang/Ollama;
  FP8-near-BF16 claim is vendor self-eval; GGUF/llama.cpp fork dependency is a material caveat.
- Lance 3B (08-29): Apache 2.0 claimed; HF availability needs direct confirmation.
- No new quantization-method release captured for the window; `UNCERTAIN`, await Grok.

### H. Inference / Serving / Systems
- Day-zero serving paths for K2 Horizon (vLLM/SGLang/Ollama; NVIDIA/AMD/Cerebras) — vendor-named,
  needs repo/release-tag confirmation per engine.
- vLLM v0.29.0 (2026-09-09): POST-CUTOFF → Late Breaking candidate, not ordinary-window.
- SGLang-Omni TTS refactor activity (08-xx): background engineering context at most.

### I. Memory / Multi-Agent / Retrieval
- `NONE_FOUND` in this sweep for dedicated memory/retrieval-window releases. Multi-agent
  execution signals live under lane B (Kilo, Copilot harness) and are not double-counted here.
  Await Grok + first-party recheck.

### J. Evaluation / Benchmarks
- FUSE framework (arXiv 2609.02168, 2026-09-02, ordinary-window): K/D/H dangerous-capability
  profiles across 12 commercial LLMs; non-monotonic safety-vs-recency finding. Primary
  candidate: arXiv paper. Methodology-level item; no model fact asserted.
- Astra ExploitBench claims (vendor evals, contamination-aware internal port): publisher-only
  until independent reproduction; evaluation-design caveat is material.
- AgentAudit (arXiv 2609.09875, 2026-09-09): POST-CUTOFF → Late Breaking candidate.

### K. Safety / Security
- OpenAI Astra safeguard package (09-01→09-03): Critical-cyber designation, checkpoint
  encryption, isolation, universal CoT/trajectory monitoring, blocking alignment evals,
  two-week training pause after Hugging Face incident. Vendor disclosure; monitor-evasion
  adversarial findings cut against reassurance reading.
- Anthropic alignment & security follow-up (2026-09-01, ordinary-window): eval-env hardening,
  real-time sandbox-escape classifier, RL-env monitoring, partner practices, Mythos-class
  infra hardening (from April), reward-hacking research (~80 hackable envs). Primary candidate:
  Anthropic official post (via explainx summary as locator only).
- Anthropic Sep 9 alignment assessment of four cyber-eval incidents: POST-CUTOFF → Late Breaking.

### L. Other Emerging Generative AI Technology
- World Labs Atlas (covered in C; spatial-intelligence track) is the principal L lead.
- Google Pics Workspace embedding (covered in D) is the principal productization lead.
- No additional L-only releases asserted; further emerging-tech sweep deferred to post-Grok gap fill.

## Post-cutoff Late Breaking separation (NOT ordinary-window)

- vLLM v0.29.0 (2026-09-09)
- AgentAudit framework (2026-09-09)
- Anthropic four-incident alignment assessment (2026-09-09)
- Gloo Code GA (2026-09-08)
- Any Grok-observed post-09-04T18:00-04:00 momentum must join this list, not the ordinary ranking.

## Explicitly NOT covered / negative space (must be revisited post-Grok)

- Lane F (generative speech/audio/music) and lane I (memory/retrieval) have no W36-window
  primary leads from this sweep — may be genuinely quiet or a sweep gap; Grok result +
  targeted first-party recheck required before calling either quiet.
- Lane G quantization-method releases: `UNCERTAIN`, same recheck required.
- Formal duplicate/concentration analysis and negative-space audit are deferred to the Sol
  Discovery completeness review after formal Discovery materialization.

## Carry-over input (not authority)

- W35 RELEASED authority read: 20 Discovery / 19 screened (19 KEEP / 1 DROP) / 8 VERIFIED +
  11 PARTIAL / 17 SELECTED + 2 HOLD across 5 architecture packages; thesis centered on
  open-weight efficiency + agent coding plane + flagship receipts + safety/governance.
- W35 HOLD/RESIDUAL items (incl. HUG-VIS CONTEXT/HOLD disposition and any unresolved authority)
  are revalidation inputs only. No W35 Selection/Evidence/Architecture/Human decision is
  inherited as a W36 conclusion. W35 HOLDs do not auto-promote without new window-specific signal.
- W36 formal carry-over derivation is deferred to the canonical ledger path post-Grok
  (`initialize_weekly_carryover_ledger.py` / `validate_weekly_carryover_ledger.py`); nothing is
  fixed by this note.

## External handoff

- None performed by this note. Grok/X handoff is owned by the parent session log; this note
  consumed only public web search results as preparation leads, never as X authority.

## Deviations / failures

- None. This note is explicitly non-authoritative and creates no lifecycle, Discovery, Evidence,
  Selection, or Architecture authority.

## End state

- Parent session remains `ISSUE_INITIALIZED / AWAITING_GROK_BLOCKED`.
- Next action unchanged: `import Grok result -> record-result -> stage:discovery`.
