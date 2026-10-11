# W40 staged Architecture outline r14 — derived from architecture-coverage-r14.json (NOT Architecture)

Status: STAGED_R14 / OUTLINE_ONLY / NO_ARCHITECTURE_ACCEPTANCE
Supersedes as working outline (r13 preserved immutable):
`execution/architecture-staged-outline-r13.md`
Single authoritative map: `execution/architecture-coverage-r14.json` (28 entries,
file SHA-256 `3de8bd56…`; derived from `selection-preview-r13.json` SHA `dc024778…`
+ r10 matrix SHA `f07b1166…`); reconciliation:
`execution/architecture-coverage-validation-r14.json` (10 checks, status PASS).
This outline creates NO `architecture-v2.json`, NO review-summary/attention files,
NO checkpoint, NO State change, and claims NO Reader Manifest `architecture_coverage`.
It is 28 SELECTED = 20 PRIMARY + 8 SUPPORTING; 4 HOLD + 3 REJECT are NOT placed.
r13 outline Role errors (SynthID Bio, VSS 3.3, Nemotron ASR) are corrected here;
r13's Ross-without-destination gap is closed (explicit P7 supporting destination).

## Reader-today vs staged-only separation

- READER-BOUND ONLY via the ordinary chain (post-acceptance Selection → Architecture →
  manuscript → Candidate → Human Gates → Freeze → Release): P1–P8 below.
- STAGED ONLY: COND-A AstaBrief + COND-B AutoSynthData (NON_CANONICAL HOLD, NOT in the
  28 mapping or any package placement); DGX background facts (evidence only);
  W39 HOLD carry-overs.

## P1 frontier-models — LARGEST (PRIMARY ×3)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:b22893750847d0a9 | Claude Sonnet 5.5 | PRIMARY | WEEKLY:frontier-models |
| candidate:2026-W40:8cec00c34e0532a2 | GPT-6.1 Sol | PRIMARY | WEEKLY:frontier-models |
| candidate:2026-W40:fc912402fc5e5025 | Gemini 4 Argon | PRIMARY | WEEKLY:frontier-models |

Sonnet 5.5 (price card + Terminal-Bench 70.6%/GDPval-AA 1844 attributed + safeguard
posture) + GPT-6.1 Sol ($2/$10/$0.10 + changelog cross-check) + Gemini 4 Argon
(1M OUTPUT exact + intro pricing + tester posture). Separate per-vendor tables;
cost-per-task economics frame. Ultrafast-soon (Oct 8) excluded.

## P2 open-reasoning — LARGE (PRIMARY ×2)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:4f523016fa837285 | Holo4 agent models | PRIMARY | WEEKLY:japanese-open-reasoning |
| candidate:2026-W40:d8b07b761859ff02 | ELYZA Thinking LLM-jp-4 models | PRIMARY | WEEKLY:japanese-open-reasoning |

P2a Holo4 generalist GUI/agent weights (27B research-noncommercial vs 35B-A3B
Apache-2.0; OSWorld/OSWorld2 + overlap footnote; trajectories open). P2b ELYZA
Japanese-specialist (33B + 32B-A3B; JA-localized 3-stage; full JA tables +
global-trail counterfactual with JMMLU regressions). Shared mechanics intro,
independent subsections.

## P3 decision-inference — MEDIUM (PRIMARY ×3)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:e7c620cc779a6e34 | Ollama v0.35 decision-model support | PRIMARY | WEEKLY:decision-inference |
| candidate:2026-W40:4cc1306230500269 | Cloudflare Clef decision models | PRIMARY | WEEKLY:decision-inference |
| candidate:2026-W40:4dd078cf92f1c9c9 | Strands Decider 2B | PRIMARY | WEEKLY:decision-inference |

Ollama System One (INTERFACE, 91ms illustrative) / Clef+flash (open weights, Oct 1
15:34:02Z, vendor-hosted index caveat) / Strands Decider 2B (v19 bb282d7,
pointer-head). Interface / weights / latency axes never merged. Oct 9 Clef-omni
guarded out.

## P4 devday-product-surface — MEDIUM (PRIMARY ×2 + SUPPORTING ×1)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:2a2e5255e276e2fc | OpenAI Agents API computer use | PRIMARY | WEEKLY:devday-product-surface |
| candidate:2026-W40:5400e29ebe4568ec | OpenAI dots | PRIMARY | WEEKLY:devday-product-surface |
| candidate:2026-W40:c4c210a74c6428e8 | OpenAI DevDay 2026 announcements | SUPPORTING | WEEKLY:devday-product-surface |

Hub (SUPPORTING, index spine, zero headlines) + dots + Agents API (PRIMARY bodies;
tiers/Pro500/Enterprise gates, app-handled sign-in). Decisions API (Oct 6) excluded.

## P5 safety-provenance — MEDIUM (PRIMARY ×3 + SUPPORTING ×2; CORRECTED)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:00ad8b21e165c26e | ProvenanceGuard | PRIMARY | WEEKLY:safety-provenance |
| candidate:2026-W40:ad91dec415837190 | NVIDIA Open Agent Safety Platform | PRIMARY | WEEKLY:safety-provenance |
| candidate:2026-W40:f375b6c488969327 | SynthID Bio | PRIMARY | WEEKLY:safety-provenance |
| candidate:2026-W40:a08a45630e4d9ba0 | OpenAI frontier training safety cases | SUPPORTING | WEEKLY:safety-provenance |
| candidate:2026-W40:fba60168479c9784 | Cloudflare Workers OAuth Provider v1 | SUPPORTING | WEEKLY:safety-provenance |

CORRECTION vs r13 outline: SynthID Bio is PRIMARY (selection bytes), not SUPPORTING;
map is 3 PRIMARY / 2 SUPPORTING. Runtime controls (OpenShell/Sentry reference arch) /
training governance (safety-cases guidance) / biological watermark (SynthID Bio, 3 lab
targets) / source attribution (ProvenanceGuard v2-pinned paper + Sep 29 blog split) /
MCP authorization (OAuth v1 + README mechanics). Never merged under one "safety
performance" claim.

## P6a training-methods-and-systems — MEDIUM-LARGE (PRIMARY ×2)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:92241424368e1305 | Context Language Models | PRIMARY | WEEKLY:training-eval-infra |
| candidate:2026-W40:a5143ea24719b616 | Olmo-core 3 | PRIMARY | WEEKLY:training-eval-infra |

ContextLM (file-as-context, Eq.1–6, BCP/EdgeBench/swarm, RL Table 2, SCR, App.D–G +
repo README/CC BY-NC 4.0) / Olmo-core 3 (DDP+EP/PP/dist-opt + grouped-GEMM + MXFP8
+21%, NVL8-B300 12.9B→1.2T/512GPU, 858 TFLOP/s/GPU, DeepEP-v2, Gerrymandering +
slowdown lessons; §14 cells/§§16–20 ablations/code internals at Architecture depth).
Full technical depth reserved; substantive drafts in `technical-prep-r14/p6a-deep-draft.md`.

## P6b evaluation-and-execution-infra — MEDIUM-LARGE (PRIMARY ×2 + SUPPORTING ×1)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:9de6ffd245268468 | AA-AgentPerf-Local | PRIMARY | WEEKLY:training-eval-infra |
| candidate:2026-W40:113e97bcb642e557 | Open TTS Leaderboard | PRIMARY | WEEKLY:training-eval-infra |
| candidate:2026-W40:bed589208da5f196 | Hugging Face RL Environments Hub | SUPPORTING | WEEKLY:training-eval-infra |

AgentPerf (serving-only, 14 configs, living-pin caveat) + OpenTTS (objective metrics +
human-preference disclaimer + scripts repo) + RL-Env Hub interop (SUPPORTING: tag
semantics, seeded tasksets, per-config future). Mechanisms/metrics/limits per system.
P6a and P6b share the `WEEKLY:training-eval-infra` role namespace (selection bytes)
but remain TWO justified editorial destination packages; no fictitious Core "split" role
is claimed. Substantive drafts in `technical-prep-r14/p6b-deep-draft.md`.

## P7 multimodal-serving-observability — MEDIUM (PRIMARY ×3 + SUPPORTING ×2; CORRECTED)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:f3395a322bb2c7fa | FLUX 3 Image | PRIMARY | WEEKLY:image-video-audio-serving |
| candidate:2026-W40:055bb2f3f5be21c2 | NVIDIA VSS Blueprint 3.3 | PRIMARY | WEEKLY:image-video-audio-serving |
| candidate:2026-W40:11b49826dd7c91d3 | Nemotron Saudi Arabic ASR adaptation | PRIMARY | WEEKLY:image-video-audio-serving |
| candidate:2026-W40:297161b79687e931 | NVIDIA NeMo Relay | SUPPORTING | WEEKLY:image-video-audio-serving |
| candidate:2026-W40:0180c8edb63bd8b3 | AMD Ross | SUPPORTING | WEEKLY:image-video-audio-serving |

CORRECTIONS vs r13 outline: VSS 3.3 and Nemotron ASR are PRIMARY (selection bytes),
not SUPPORTING; AMD Ross is SUPPORTING with an EXPLICIT P7 supporting destination
(reader prose stays a small embedded UNMEASURED note — placement, not promotion).
FLUX 3 Image (SKU/pricing/windows; weights/license pending) / VSS 3.3 (reference arch +
demo configs + variance) / Nemotron ASR (WER tables + non-generalization caveats) +
Relay observability (ATOF/ATIF/OTel-Phoenix) + Ross embedded note.

## P8 enterprise-industry-digest — SMALL (SUPPORTING ×2)

| Candidate ID | Item | Usage | architecture_role |
|---|---|---|---|
| candidate:2026-W40:83a557645d769ec1 | AMD acquisition agreement for World Labs | SUPPORTING | WEEKLY:corporate-enterprise-infra |
| candidate:2026-W40:baa2a35dcad0b509 | Cloudflare AI Search | SUPPORTING | WEEKLY:corporate-enterprise-infra |

World Labs agreement (not close; valuation caveat) + AI Search GA (terms; billing
Nov 1). DGX Spark NOT placed (Sol r13 REJECT; evidence/background only).

## P6a-COND — conditional future topics (NOT placed, NOT counted)

- COND-A AstaBrief (`candidate:2026-W40:00ac1151955c20ff`, HOLD) and COND-B AutoSynthData
  (`candidate:2026-W40:ba7d989d5b799f66`, HOLD) remain NON_CANONICAL HOLD. They appear in
  NO package above and in NO entry of `architecture-coverage-r14.json`. Admission only
  via Issue-#562 supersession or separately authorized supplement path.

## Package totals (one-to-one audit)

P1 3 / P2 2 / P3 3 / P4 3 / P5 5 / P6a 2 / P6b 3 / P7 5 / P8 2 = 28 placed, 28 SELECTED.
PRIMARY 20 (P1 3, P2 2, P3 3, P4 2, P5 3, P6a 2, P6b 2, P7 3, P8 0); SUPPORTING 8
(P4 1, P5 2, P6b 1, P7 2, P8 2). Zero HOLD/REJECT placed; zero invented IDs; Ross placed.
Prior r13 "27-item" appearance is explained: Ross had prose but no destination; now resolved.
Every r13 SELECTED candidate is lawfully placed; none dropped. If Sol finds otherwise,
this outline — not the Selection — is the defective artifact.

## Depth/budget + guards

P1 largest; P2 large; P6a/P6b medium-large with FULL reserved depth (see
`technical-prep-r14/` drafts); P3/P5/P7 medium; P4 medium; P8 small. Every package at
authorship time: mechanisms + metrics WITH conditions + comparisons WITH limits +
sources. Compression guard: 28-item spine vs ≤1-collapse tripwire (re-baselined to 30
only after lawful supersession, by Sol — not here). No page-count cap at staging.
