# W40 Selection dossier r10 (PROPOSED reviewer input for Sol semantic review — REVISED)

Status: `PROPOSED_NOT_ACCEPTED` — NOT canonical `SELECTION_COMPLETE`. Companion to
`selection-proposal-r10.json` (35 assignments: 28 SELECTED = 20 PRIMARY / 8 SUPPORTING + 1 INSPECT + 4 HOLD +
2 REJECT; counts machine-recomputed in `count-report-r10.json`) and Core review-only preview
`selection-preview-r10.json` (Core `validate_selection` PASS; NOT canonical acceptance).
Basis SHAs: profile `c921bd14…`, matrix staging (frozen-derived), evidence-accepted `ca5e21a7…` (set `0a62346f…`),
views-accepted (file `51887616…`, set `1effd744…`), ledger `ce63f3a9…`, completeness `f83b2d94…`.
r9 dossier preserved as history; this file revises package axes/depth ONLY (no merit/HOLD changes).

## Reviewer assumptions (unchanged from r9 + r10 evidence)

Sol MC r1 conditional PASS (SC-M01/M02 repaired); vendor/publisher figures attributed, never independently
reproduced; day-only dates stay day-only; AstaBrief/AutoSynthData TIME_UNRESOLVED HOLD; DGX ordinary-eligible
(13:00:39Z) with Oct 23 future-shipping caveat; LIFT pre-window; W39 rumors HOLD; licenses/version pins stand;
post-window items (Clef-omni Oct 9, 6.1-Ultrafast Oct 8, Decisions beta Oct 6) and Oct 2 day-only Cloudflare items
(Web Search API, Pi harness — hour UNPROVEN, unadmitted) excluded from publishable claims.

## Revised packages (r10 — information-density redesign)

### P1 frontier-models (PRIMARY ×3) — largely READY, tables required

Sonnet 5.5 / GPT-6.1 Sol / Gemini 4 Argon. Price cards, input/output limits, availability tiers and
evaluation-benchmark CONDITIONS in separate tables (never cross-vendor ranking: different harnesses/efforts).
Argon 1M OUTPUT wording exact. Relative depth: LARGEST (cost-per-task economics + safeguard/rollout posture).

### P2 open-reasoning (PRIMARY ×2) — RENAMED/REVISED (was: Open/JA Reasoning)

- **P2a generalist GUI/agent open weights — Holo4**: 27B dense (research-noncommercial) vs 35B-A3B MoE
  (Apache-2.0) split explicit; OSWorld/OSWorld2/AutomationBench conditions + training-overlap footnote;
  trajectories open. Holo4 is NOT a Japanese-specialist model — the old name misled.
- **P2b Japanese-specialist reasoning release — ELYZA**: 33B Dense + 32B-A3B MoE, JA-localized 3-stage method,
  full JA benchmark tables with global-trail counterfactual (trails Qwen3.5/Gemma4; JMMLU regressions preserved).
  JA-survey significance stated. The two halves share open-weights mechanics but address different readers;
  independent subsections with a shared comparison table (license/price/scale/JA-eval).

### P3 decision-inference (PRIMARY ×3) — largely READY with separation discipline

Ollama System One (INTERFACE, not weights; 91ms illustrative) / Clef+flash (open weights, exact Oct 1 timestamp;
vendor-hosted index caveat) / Strands Decider 2B (v19 pin bb282d7; pointer-head architecture). Same theme, three
release types; interface / model-weights / pointer-head / latency axes separated; NO cross-vendor apples-to-apples.

### P4 devday-product-surface (PRIMARY dots + Agents API; SUPPORTING DevDay hub) — largely READY

Hub as introduction/index spine (anti-double-counting); dots and Agents API bodies never duplicated from hub;
availability + permission-boundary table (tiers, Pro500/Enterprise gates, app-handled sign-in; no safety inference).

### P5 safety-provenance — REVISED into five independent subsections (was: one safety bucket)

1. **Runtime controls** — OpenShell/Sentry (reference architecture, enforcement mechanics, Vera/BlueField scope;
   NOT empirical assurance). 2. **Training governance** — safety-cases guidance (aspirational, not deployed).
3. **Biological watermark** — SynthID Bio (lab-bounded function on 3 targets; tamper-robustness future).
4. **Source attribution** — ProvenanceGuard (v2-pinned paper + Sep 29 blog event split; metrics with adjudication
   transparency). 5. **MCP authorization** — OAuth Provider v1 + repo README mechanics (spec adherence ≠ resistance).
   Never merged under one "safety performance" claim.

### P6 — SPLIT (was: single medium training-eval-infra; MAJOR REVISE)

- **P6a training-methods-and-systems** (PRIMARY ×2): ContextLM (file-as-context method, Eq.1–6, BCP/EdgeBench/swarm
  conditions, RL Table 2, SCR, App.D–G now consumed incl. repo README/CC BY-NC 4.0) / Olmo-core 3 (DDP+EP/PP/dist-opt
  + grouped-GEMM + MXFP8 +21%, NVL8-B300 12.9B→1.2T/512GPU, 858 TFLOP/s/GPU, DeepEP-v2 2.38T capacity test, Token
  Gerrymandering + overlap-slowdown lessons; §14 cells/§§16–20 ablations/code internals still Selection-depth).
  AutoSynthData joins P6a ONLY if its hour is ever proven + canonicalized (currently HOLD, not included).
- **P6b evaluation-and-execution-infra** (PRIMARY AgentPerf + OpenTTS; SUPPORTING RL-Env): serving benchmark scope
  (serving-only, 14 configs, living-pin caveat) / objective TTS metrics + human-preference disclaimer + scripts repo /
  Hub interop feature (tag semantics, seeded tasksets, per-config future). Distinct mechanisms/metrics/method
  conditions/repro limits per system; comparison tables per sub-package, never blended.

### P7 multimodal-serving-observability — REVISED (was: mixed product/research/tutorial)

- **Image/video/audio products** — FLUX 3 Image (SKU/pricing/availability windows; weights/license pending) /
  VSS 3.3 (reference arch, exact demo configs + variance) / Nemotron ASR (WER tables + non-generalization caveats).
- **Agent observability (cross-cutting)** — NeMo Relay (ATOF/ATIF/OTel-Phoenix; instrumentation, not proof).
- **Embedded product note** — AMD Ross (components/availability; promotion UNMEASURED).
  Product / reference / tutorial / instrumentation never blended.

### P8 enterprise-industry-digest — REVISED (PRIMARY = 0 → short digest, was: independent package)

World Labs agreement (not close; valuation caveat) + AI Search GA (service terms; billing Nov 1) as SHORT industry
items; DGX INSPECT decided here: **propose EXCLUDE from narrative unless Sol judges hardware-news merit** —
timestamp resolved but Oct 23 future-shipping + price framing make it a weak ordinary story vs P1–P7 density
(Sol decides; INSPECT preserved either way, never silent). P8 frees space for P2/P5/P6 depth without growing total.

## Relation map / overlap / DevDay exclusions (35 candidates)

DevDay hub counted ZERO times as a headline (spine only); dots + Agents API carry the publishable claims;
Decisions API (Oct 6) excluded post-window. Ollama/Clef/Decider never merged. Sonnet/GPT-6.1/Argon never ranked
across vendors. Holo4/ELYZA licenses never conflated. FLUX Jul-23 vs Oct-1 split. SynthID Sep-30 vs Oct-1 X split.
Argon 1M OUTPUT exact. Guard paper v1/v2-only (NO v3 asserted). LIFT + X ledger REJECT-from-narrative (citable
outside narrative). Sweeps EXCLUDED. Candidate↔Discovery map: see `candidate-id-crosswalk-r10.json`
(r9-slug → Core candidate_id + evidence_task_id + evidence/view SHAs + materiality).

## Strong-omission counterfactual + unselected review

Included priorities (Holo4, ELYZA, Olmo-core 3, ContextLM, Open TTS, RL-Env, ProvenanceGuard) all retained with
caveats; DGX conditional above. HOLDs (Pixel Canary, TBC, AstaBrief, AutoSynthData) sampled with substance —
HOLD reasons are time/authority gaps, NOT thin-evidence excuses; AstaBrief/AutoSynthData hour-proofs attempted
(r10 time log) and still unresolved. No 30th material event surfaced (Oct 2 day-only items + Oct 8/9 post-window
guarded, not qualifying). Full consumption would deepen the SAME ~28 MATERIAL items (system cards, repo docs,
weight files, eval scripts, replays, Nature body, Olmo cells/ablations) — no hidden-candidate risk beyond the
guarded items. Compression guard holds: 28-item spine vs ≤1-collapse tripwire; no page-count forcing.

## Depth/budget (relative; substantive coverage per theme)

P1 largest; P2 large (two halves + comparison table); P6a + P6b medium-large each (methods/conditions/ablations
vs metrics/scopes/limits); P3/P5/P7 medium (separated axes/subsections); P4 medium (spine + bodies);
P8 small digest. Every package: core mechanisms, evaluated metrics WITH conditions, comparisons WITH limits,
sources, and relative space — no 29-headline skim.
