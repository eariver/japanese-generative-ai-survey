# W40 staged Architecture outline r12 — frozen 28 SELECTED ONLY (NOT Architecture)

Status: STAGED_R12 / OUTLINE_ONLY / NO_ARCHITECTURE_ACCEPTANCE
Basis: `selection-preview-r12.json` (28 SELECTED = 20 PRIMARY / 8 SUPPORTING) on unchanged
canonical staging. This outline stages editorial structure for Sol review; it creates NO
`architecture-v2.json`, NO review-summary/attention files, NO checkpoint, NO State change.
Supplemental notes are EXCLUDED from all packages below (see manifest restrictions).

## P1 frontier-models — LARGEST (PRIMARY ×3)

Sonnet 5.5 (price card + Terminal-Bench 70.6%/GDPval-AA 1844 attributed + safeguard posture)
+ GPT-6.1 Sol ($2/$10/$0.10 + changelog cross-check) + Gemini 4 Argon (1M OUTPUT exact +
intro pricing + tester posture). Separate per-vendor tables; cost-per-task economics frame.
Ultrafast-soon (Oct 8) excluded.

## P2 open-reasoning — LARGE (PRIMARY ×2, two halves + comparison table)

P2a Holo4 generalist GUI/agent weights (27B research-noncommercial vs 35B-A3B Apache-2.0;
OSWorld/OSWorld2 + overlap footnote; trajectories open). P2b ELYZA Japanese-specialist
(33B + 32B-A3B; JA-localized 3-stage; full JA tables + global-trail counterfactual with
JMMLU regressions). Shared mechanics intro, independent subsections.

## P3 decision-inference — MEDIUM (PRIMARY ×3, separated axes)

Ollama System One (INTERFACE, 91ms illustrative) / Clef+flash (open weights, Oct 1
15:34:02Z, vendor-hosted index caveat) / Strands Decider 2B (v19 bb282d7, pointer-head).
Interface / weights / latency axes never merged. Oct 9 Clef-omni guarded out.

## P4 devday-product-surface — MEDIUM (PRIMARY ×2 + SUPPORTING spine)

Hub (SUPPORTING, index spine, zero headlines) + dots + Agents API (PRIMARY bodies;
tiers/Pro500/Enterprise gates, app-handled sign-in). Decisions API (Oct 6) excluded.

## P5 safety-provenance — MEDIUM (five independent subsections)

Runtime controls (OpenShell/Sentry reference arch) / training governance (safety-cases
guidance) / biological watermark (SynthID Bio, 3 lab targets) / source attribution
(ProvenanceGuard v2-pinned paper + Sep 29 blog split) / MCP authorization (OAuth v1 +
README mechanics). Never merged under one "safety performance" claim.

## P6a training-methods-and-systems — MEDIUM-LARGE (PRIMARY ×2, depth kept)

ContextLM (file-as-context, Eq.1–6, BCP/EdgeBench/swarm, RL Table 2, SCR, App.D–G +
repo README/CC BY-NC 4.0) / Olmo-core 3 (DDP+EP/PP/dist-opt + grouped-GEMM + MXFP8 +21%,
NVL8-B300 12.9B→1.2T/512GPU, 858 TFLOP/s/GPU, DeepEP-v2, Gerrymandering + slowdown
lessons; §14 cells/§§16–20 ablations/code internals at Architecture depth).
FUTURE (not here): AstaBrief + AutoSynthData subsections after Core supersession.

## P6b evaluation-and-execution-infra — MEDIUM-LARGE (PRIMARY ×2 + SUPPORTING ×1)

AgentPerf (serving-only, 14 configs, living-pin caveat) + OpenTTS (objective metrics +
human-preference disclaimer + scripts repo) + RL-Env Hub interop (SUPPORTING: tag
semantics, seeded tasksets, per-config future). Mechanisms/metrics/limits per system.

## P7 multimodal-serving-observability — MEDIUM

FLUX 3 Image (SKU/pricing/windows; weights/license pending) / VSS 3.3 (reference arch +
demo configs + variance) / Nemotron ASR (WER tables + non-generalization caveats) +
Relay observability (ATOF/ATIF/OTel-Phoenix) + Ross embedded note (UNMEASURED).

## P8 enterprise-industry-digest — SMALL

World Labs agreement (not close; valuation caveat) + AI Search GA (terms; billing Nov 1).
DGX INSPECT: propose EXCLUDE unless Sol judges hardware-news merit (13:00:39Z resolved;
Oct 23 future-shipping + price framing weak vs P1–P7 density).

## Depth/budget + guards

P1 largest; P2 large; P6a/P6b medium-large; P3/P5/P7 medium; P4 medium; P8 small.
Every package: mechanisms + metrics WITH conditions + comparisons WITH limits + sources.
Compression guard: 28-item spine vs ≤1-collapse tripwire (to be re-baselined to 30 only
after lawful supersession, by Sol — not here).
