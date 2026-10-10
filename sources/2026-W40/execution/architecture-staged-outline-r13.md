# W40 staged Architecture outline r13 — 28 SELECTED + conditional P6a modules (NOT Architecture)

Status: STAGED_R13 / OUTLINE_ONLY / NO_ARCHITECTURE_ACCEPTANCE
Supersedes (as working outline; r12 preserved immutable):
`execution/architecture-staged-outline-r12.md`
Basis: `selection-preview-r13.json` (SHA `dc024778…`; 28 SELECTED = 20 PRIMARY /
8 SUPPORTING; 4 HOLD; 3 REJECT incl. DGX per Sol r13) on unchanged canonical staging.
Validator: Core `validate_selection` PASS (0 errors) — see
`selection-validation-r13.md`. This outline stages editorial structure for Sol review;
it creates NO `architecture-v2.json`, NO review-summary/attention files, NO checkpoint,
NO State change. Addresses finding W40-R12-F08 (deep staged P1–P8, P6a/P6b depth).
Supplement notes (`editorial-supplement/r13/`) are EXCLUDED from all main-issue
packages below (manifest-r13 restrictions); their conditional P6a modules are staged
in §P6a-COND ONLY.

## Reader-today vs staged-only separation

- REACHES A READER TODAY (ordinary path, after Selection acceptance + Architecture +
  Gates + Freeze/Release): the 28 SELECTED packages P1–P8 below. Nothing else.
- STAGED ONLY (not reader-bound without Issue-#562 supersession or separate Human
  authorization): P6a-COND-A (AstaBrief) + P6a-COND-B (AutoSynthData) modules;
  DGX background facts (evidence retained, NO narrative item); W39 HOLD carry-overs.
- See §9 decision table for the full cross-issue disposition map.

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

## P5 safety-provenance — MEDIUM (five independent subsections + SUPPORTING ×3)

Runtime controls (OpenShell/Sentry reference arch) / training governance (safety-cases
guidance) / biological watermark (SynthID Bio, 3 lab targets) / source attribution
(ProvenanceGuard v2-pinned paper + Sep 29 blog split) / MCP authorization (OAuth v1 +
README mechanics). Never merged under one "safety performance" claim.

## P6a training-methods-and-systems — MEDIUM-LARGE (PRIMARY ×2, depth kept)

ContextLM (file-as-context, Eq.1–6, BCP/EdgeBench/swarm, RL Table 2, SCR, App.D–G +
repo README/CC BY-NC 4.0) / Olmo-core 3 (DDP+EP/PP/dist-opt + grouped-GEMM + MXFP8 +21%,
NVL8-B300 12.9B→1.2T/512GPU, 858 TFLOP/s/GPU, DeepEP-v2, Gerrymandering + slowdown
lessons; §14 cells/§§16–20 ablations/code internals at Architecture depth).
Depth for both is RESERVED at full technical level — no headline collapse (F08).

## P6a-COND — CONDITIONAL post-training + synthetic-curriculum modules (STAGED ONLY)

NOT reader-bound today. admission condition: Issue-#562 Core supersession (HOLD→MATERIAL)
+ Sol re-review + ordinary Selection/Architecture chain, OR separately Human-authorized
supplement path (see `supplement-publication-feasibility-r13.md`; neither preapproved).
Technical staging (from r13-corrected notes):

- COND-A AstaBrief (prospective P6a third PRIMARY subsection): Qwen3-8B + SFT/DPO only
  (RL considered, set aside); 90K query pool → 47K usable (post-DPO-carve-out) →
  density≥0.25 filter → public 39.5K SFT Mix; DPO ~6K article vs 6,622 public rows,
  dual-judge (GPT-4.1 + DeepSeek-R1) agreement, 95% claim hedged (sample size
  undisclosed); 51.1s vs 178.5s end-to-end (≈3.5×) vs generation-time "nearly an order
  of magnitude" (kept distinct); 2025-vintage baselines, no rerun, no SOTA;
  weights Apache-2.0 vs mixes CC-BY-NC-4.0 + third-party-terms boundary sentence;
  four-metric eval (rubric/answer-precision/citation-precision/citation-recall) +
  scope-preservation as future work. Comparison table vs ContextLM (method) /
  Olmo-core (systems) to be drafted at Architecture depth upon admission.
- COND-B AutoSynthData (prospective P6a fourth PRIMARY subsection): task=(spec, prompt,
  verifier); consistency/soundness/completeness triad (F03-corrected) with
  positive/negative gate examples; TARGET→MULTIPLY (no re-seeding); solver band
  target≤1/3 + solver≥2/3; critic + bounded repair + batch meta-review; symmetric
  Hybrid (Gemma-4-26B-A4B-it + Qwen3.8-27B; 2,000/~18h/epoch-5; +7.2pp = 35% rel;
  verifier 63.01→68.55%; 59% gap) vs ITSM (same target + DeepSeek-V4.1-Flash;
  1,994/66h, ran FIRST; 18.77→27.18%); SFT-only, RL future; method-only (F04 bounded
  release wording); Gym background separated. Table-separated from AstaBrief mixes
  and Olmo-core infra upon admission.

## P6b evaluation-and-execution-infra — MEDIUM-LARGE (PRIMARY ×2 + SUPPORTING ×1, depth kept)

AgentPerf (serving-only, 14 configs, living-pin caveat) + OpenTTS (objective metrics +
human-preference disclaimer + scripts repo) + RL-Env Hub interop (SUPPORTING: tag
semantics, seeded tasksets, per-config future). Mechanisms/metrics/limits per system;
full-width treatment reserved (F08).

## P7 multimodal-serving-observability — MEDIUM

FLUX 3 Image (SKU/pricing/windows; weights/license pending) / VSS 3.3 (reference arch +
demo configs + variance) / Nemotron ASR (WER tables + non-generalization caveats) +
Relay observability (ATOF/ATIF/OTel-Phoenix) + Ross embedded note (UNMEASURED).

## P8 enterprise-industry-digest — SMALL

World Labs agreement (not close; valuation caveat) + AI Search GA (terms; billing Nov 1).
DGX Spark: Sol r13 REJECT as standalone narrative item (in-window 13:00:39Z ordinary-
eligible, but hardware-news technical substance/priority insufficient vs P1–P7);
facts retained as evidence/background ONLY (64GB SKU, Sync Cluster Assistant, Oct 23
third-party $4,999 future availability — preorder ≠ shipment). NO P8 subsection.

## §9 Material coverage / cross-issue decision table

| # | Subject | Disposition (preview-r13) | Reader fate |
|---|---|---|---|
| 28 | P1–P8 main-issue items (§P1–P8 matrices) | SELECTED (20 PRIMARY / 8 SUPPORTING) | Reader-bound via ordinary chain (post-acceptance) |
| 2 | AstaBrief 8B / AutoSynthData | HOLD (canonical, retained) + MATERIAL direction (Sol r11) + r13 noncanonical staging | STAGED ONLY → P6a-COND-A/B upon #562 supersession or authorized supplement |
| 1 | DGX Spark 64GB | REJECT (Sol r13 editorial; was INSPECT) | Evidence/background only; no narrative item |
| 2 | W39 carry-over HOLD (Pixel Canary, TBC video) | HOLD | Not reader-bound; unproven primary identity/performance |
| 2 | Other REJECT (Grok/X ledger, LIFT) | REJECT | Out of reader surface (observation-CONTEXT / pre-window) |

## §10 Bounded technical coverage matrices (28 + 2 conditional)

Columns: Role | Source→claim anchor | Mechanism | Metric + denominator/sample | Baseline +
version/timestamp | License | External validity + reproducibility. Matrices are STAGED
editorial working tables, not canonical Architecture packages.

### P1 (3 PRIMARY)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| Sonnet 5.5 | PRIMARY | price card + Terminal-Bench/GDPval-AA attributions | 70.6% TB / 1844 GDPval-AA (attributed) | vendor card vintage | vendor terms | attributed benchmarks, not independent repro |
| GPT-6.1 Sol | PRIMARY | $2/$10/$0.10 + changelog cross-check | price units | changelog-pinned | vendor terms | pricing snapshot, not capability proof |
| Gemini 4 Argon | PRIMARY | 1M OUTPUT exact + intro pricing + tester posture | 1M output tokens | intro pricing window | vendor terms | tester-posture caveats |

### P2 (2 PRIMARY)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| Holo4 | PRIMARY | OSWorld/OSWorld2 + overlap footnote; trajectories open | OSWorld suites | 27B RC-noncommercial vs 35B-A3B Apache-2.0 | split licenses | overlap footnote preserved |
| ELYZA jp-4 | PRIMARY | JA-localized 3-stage; full JA tables | JA suites + JMMLU counterfactual | 33B + 32B-A3B | open weights | JMMLU regressions disclosed |

### P3 (3 PRIMARY)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| Ollama v0.35 | PRIMARY | INTERFACE axis; 91ms illustrative | latency illustration | v0.35 | interface note | illustrative, not benchmark |
| Clef+flash | PRIMARY | open weights; Oct 1 15:34:02Z; vendor-hosted index caveat | weights + index | Oct 1 clock | open weights | index-hosting caveat |
| Strands Decider 2B | PRIMARY | pointer-head; v19 bb282d7 | version pin | v19 | open weights | mechanism-level only |

### P4 (2 PRIMARY + 1 SUPPORTING)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| Agents API computer use | PRIMARY | tiers/Pro500/Enterprise gates; app-handled sign-in | product tiers | DevDay vintage | vendor terms | product-surface, not eval |
| dots | PRIMARY | DevDay body | product surface | DevDay vintage | vendor terms | same |
| DevDay Hub | SUPPORTING | index spine, zero headlines | — (spine) | — | — | no standalone claims |

### P5 (2 PRIMARY + 3 SUPPORTING)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| ProvenanceGuard | PRIMARY | v2-pinned paper + Sep 29 blog split | paper + blog | v2 pin | paper license | split-paper/blog attribution |
| Open Agent Safety | PRIMARY | OpenShell/Sentry reference arch | reference arch | vendor vintage | vendor terms | reference, not deployment proof |
| Safety cases | SUPPORTING | training-governance guidance | guidance doc | — | — | guidance, not eval |
| SynthID Bio | SUPPORTING | 3 lab targets | lab count | — | — | lab-scoped |
| OAuth v1 (MCP) | SUPPORTING | README mechanics | mechanism | v1 | — | mechanism-level |

### P6a main (2 PRIMARY, full depth reserved)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| ContextLM | PRIMARY | file-as-context Eq.1–6; BCP/EdgeBench/swarm; RL Table 2; SCR; App.D–G | suite + table cells | repo README | CC BY-NC 4.0 (README) | ablations at Architecture depth |
| Olmo-core 3 | PRIMARY | DDP+EP/PP/dist-opt; grouped-GEMM; MXFP8 +21%; NVL8-B300 12.9B→1.2T/512GPU; 858 TFLOP/s/GPU; DeepEP-v2; Gerrymandering/slowdown lessons; §14 cells; §§16–20 ablations | hardware + ablation cells | infra vintage | open infra | code-internals at Architecture depth |

### P6a-COND (staged only; admission-gated)

| Item | Role (prospective) | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| COND-A AstaBrief | prospective PRIMARY | HF org article 2026-10-02T15:19:50.340Z + SFT/DPO cards | 51.1s vs 178.5s end-to-end; SQABench-CS2 (200 Qs, 4 metrics); DeepScholarBench (63, non-comparable); 14-Q human study (3 researchers) | 2025-vintage; no rerun; Qwen3-8B base | weights Apache-2.0 / mixes CC-BY-NC-4.0 + 3rd-party-terms boundary | canonical HOLD until #562; 95% hedged; no SOTA |
| COND-B AutoSynthData | prospective PRIMARY | HF org article 2026-10-02T04:01:31.290Z | Hybrid +7.2pp (=35% rel), verifier 63.01→68.55%, 59% gap, 2000/~18h/epoch5; ITSM 18.77→27.18%, 1994/66h (first) | SFT-only; Gym-scoped; RL future | method-only (F04 bounded); Gym Apache-2.0 separate | canonical HOLD until #562; teachers verbatim |

### P6b (2 PRIMARY + 1 SUPPORTING, full depth reserved)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| AgentPerf | PRIMARY | serving-only; 14 configs | 14-config matrix | living pin (caveat) | vendor terms | serving-only scope |
| OpenTTS | PRIMARY | objective metrics + human-preference disclaimer + scripts repo | objective suite | scripts repo | open scripts | preference disclaimer |
| RL-Env Hub | SUPPORTING | tag semantics; seeded tasksets; per-config future | interop tags | hub vintage | hub terms | interop only |

### P7 (PRIMARY ×1 + SUPPORTING ×3 + embedded note)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| FLUX 3 Image | PRIMARY | SKU/pricing/windows | price windows | SKU vintage | weights/license pending | license pending |
| VSS 3.3 | SUPPORTING | reference arch + demo configs + variance | demo configs | 3.3 | vendor terms | variance disclosed |
| Nemotron ASR | SUPPORTING | WER tables | WER suite | adaptation vintage | vendor terms | non-generalization caveats |
| NeMo Relay | SUPPORTING | ATOF/ATIF/OTel-Phoenix | observability signals | — | — | observability only |
| AMD Ross | (embedded, UNMEASURED) | — | — | — | — | no measured claims |

### P8 (2 SUPPORTING)

| Item | Role | Anchor → claim | Metric / denom. | Baseline / version | License | Validity limits |
|---|---|---|---|---|---|---|
| World Labs agreement | SUPPORTING | not-close; valuation caveat | deal terms | agreement vintage | — | not a close |
| AI Search GA | SUPPORTING | terms; billing Nov 1 | GA terms | Nov 1 billing | vendor terms | terms snapshot |

## Depth/budget + guards

P1 largest; P2 large; P6a/P6b medium-large with FULL reserved depth for ContextLM,
Olmo-core 3, AgentPerf, OpenTTS, RL-Env Hub (+ COND-A/B staged at equal technical
density for admission day); P3/P5/P7 medium; P4 medium; P8 small. Every package at
authorship time: mechanisms + metrics WITH conditions + comparisons WITH limits +
sources. Compression guard: 28-item spine vs ≤1-collapse tripwire (re-baselined to 30
only after lawful supersession, by Sol — not here). DGX adds no package. No page-count
cap imposed at staging (F08: do not collapse to headlines).
