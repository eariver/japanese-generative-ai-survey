# W40 Selection-input dossier r9 (PROPOSED reviewer input for Sol semantic review)

Status: `PROPOSED_NOT_ACCEPTED` — NOT canonical `SELECTION_COMPLETE`. Companion to
`execution/selection/selection-proposal-r9.json` (35 assignments: 28 SELECTED + 1 INSPECT + 4 HOLD + 2 REJECT-from-narrative).
Basis SHAs (recomputed, exact): profile `c921bd14…`, evidence-accepted `ca5e21a7…` (set `0a62346f…`),
views-accepted (file `51887616…`, set `1effd744…`), ledger `ce63f3a9…`, completeness `f83b2d94…`.

## Reviewer assumptions

1. Sol r1 Materiality (conditional PASS, SC-M01/M02 repaired) is the editorial authority; this proposal
   changes no merit/HOLD verdict.
2. Vendor/publisher benchmark figures are attributed, never independently reproduced here.
3. Day-only dates stay day-only; AstaBrief/AutoSynthData remain TIME_UNRESOLVED; DGX ordinary-eligible by
   publisher metadata (13:00:39Z) with Oct 23 future-shipping caveat; LIFT pre-window; W39 rumors HOLD.
4. Licenses/version pins from Evidence stand (Holo4 split, Strands v19, ELYZA/others Apache-2.0).
5. Post-window items (Clef-omni Oct 9, 6.1-Ultrafast Oct 8, Decisions beta Oct 6) and Oct 2 day-only Cloudflare
   items are excluded from publishable claims.

## Grouping / overlap map (8 packages; no generic catch-all)

- **P1 frontier-models** (PRIMARY ×3): Sonnet 5.5 / GPT-6.1 Sol / Gemini 4 Argon. Overlap managed: price cards
  compared side-by-side; benchmarks never cross-compared (vendor-run, different harnesses); Argon 1M OUTPUT wording exact.
- **P2 japanese-open-reasoning** (PRIMARY ×2): Holo4 (27B noncommercial vs 35B-A3B Apache-2.0 split explicit) /
  ELYZA 33B + MoE (JA tables + method; global-trail counterfactual noted). Generalist vs JA-domestic kept distinct.
- **P3 decision-inference** (PRIMARY ×3): Ollama System One (interface, NOT weights) / Clef+flash (open weights,
  exact Oct 1 timestamp) / Strands Decider 2B (v19 pin). Same theme, three release types; benchmark families judged
  separately, never apples-to-apples.
- **P4 devday-product-surface** (PRIMARY dots + Agents API; SUPPORTING DevDay hub): dots (tiers/availability) /
  Agents computer use (changelog verbatim, no safety inference) / hub as anti-double-counting spine.
- **P5 safety-provenance** (PRIMARY agent-safety + SynthID + ProvenanceGuard; SUPPORTING safety-cases + MCPAuth):
  enforcement (OpenShell/Sentry reference, not proof) vs training-governance (guidance, not deployment) vs watermark
  (lab-bounded) vs attribution verification (paper v1/v2 ONLY) vs spec surface (adherence ≠ resistance).
- **P6 training-eval-infra** (PRIMARY ContextLM + AgentPerf + Olmo-core + OpenTTS; SUPPORTING RL-Env):
  method (full-text consumed) vs benchmark tool (serving-only scope) vs training stack (reporter-level, report
  unread) vs eval platform (not a model) vs Hub feature (not OpenEnv invention).
- **P7 image-video-audio-serving** (PRIMARY FLUX + VSS + ASR; SUPPORTING Relay + Ross): SKU/pricing vs reference
  arch (exact demo configs) vs tutorial-with-caveats vs instrumentation (not proof) vs product coverage (unmeasured).
- **P8 corporate-enterprise-infra** (SUPPORTING World Labs + AISearch; INSPECT DGX): agreement-not-close +
  service-terms + timestamp-resolved hardware with merit question open.

## Explicit negative decisions (REJECT/HOLD/EXCLUDED — reviewable)

- REJECT-from-narrative (publishable set exclusion, NOT negative judgment): LIFT (pre-window context) and X ledger
  (methodology; methods-section citation only). Both remain citable outside narrative.
- HOLD (4): Pixel Canary (needs dated card + incident history), TBC video (needs measured bench/paper),
  AstaBrief (needs exact clock proof), AutoSynthData (needs clock proof; standalone release absent).
- EXCLUDED (2): r1/r2 sweep methodology logs (provenance preserved; no candidacy).
- INSPECT (1): DGX Spark — include iff Selection accepts hardware-news merit with $4,999/Oct-23-future caveats.

## Counterfactual missed-story audit

- If captured-but-unconsumed bodies were fully consumed (system cards, repo docs, weight files, eval scripts,
  trajectory replays, Nature paper body, Olmo report, rate pages), the Architecture would gain DEPTH on the same
  ~28 MATERIAL items, not new candidates: no 30th material event surfaced in r9 scans (Oct 2 day-only Cloudflare
  items lack times; Oct 8/9 items post-window).
- Strong-omission risks checked: ELYZA (included, provisional MATERIAL), Holo4 (included, license-split),
  Olmo-core (included, reporter-level flagged), ContextLM (included, full-text), OpenTTS (included, platform
  scope), RL-Env (included, interop scope), ProvenanceGuard (included, v2-pinned), DGX (INSPECT, not dropped).
- Vendor-benchmark dependence: every quantitative claim carries publisher attribution + no-independent-reproduction
  caveat for manuscript transfer.

## Anti-compression guard

- 28 SELECTED + 1 INSPECT + networked SUPPORTING roles constitute a FULL issue spine. Compressing to ≤1 SELECTED
  while non-DROP ≥ 20 would trigger the mandatory Sol compression audit per governance; this proposal explicitly
  guards against thin-headline skim (each P1–P8 package carries its own mechanism/metric/comparison/limitation
  depth below) and against page-count forcing before Architecture.

## Depth/budget proposal per package (relative space, substantive coverage)

- **P1 (largest)**: per-model mechanism (reasoning/effort, context budgets), price cards with intro/standard splits,
  evaluated metrics WITH harness/effort conditions, competitor figures as vendor-reported context only, safeguard/
  rollout posture, availability tiers. Heaviest on Sonnet/GPT-6.1/Argon deltas and cost-per-task economics.
- **P2 (large)**: Holo4 license split + benchmark footnotes (training-overlap caveat) + trajectory openness; ELYZA
  JA tables + 3-stage method + conditions + global-trail counterfactual. JA-survey significance stated.
- **P3 (medium-large)**: interface-vs-weights distinction; per-system latency/accuracy with vendor caveats; v19 pin
  discipline; no cross-vendor ranking table.
- **P4 (medium)**: per-product availability/permission boundaries; changelog-verbatim capabilities; no reliability
  claims; hub as navigation spine.
- **P5 (medium-large)**: enforcement/reference vs guidance vs lab-bounded watermark vs v2-pinned verification vs spec
  surface; each with method conditions and explicit non-claims (no attack-proof, no deployment guarantee, no
  biological generality, no threat-resistance-from-spec).
- **P6 (medium)**: method equations/conditions (CLM), serving scope + configs (AgentPerf), reporter-level infra
  figures + retry avenue (Olmo-core), platform metrics + human-preference disclaimer (OpenTTS), interop scope
  + future items (RL-Env).
- **P7 (medium)**: SKU/pricing/availability windows (FLUX), exact demo configs + variance (VSS), WER tables +
  non-generalization caveats (ASR), trace formats + tutorial scope (Relay), product components + unmeasured
  promotion flag (Ross).
- **P8 (small)**: agreement terms + valuation caveat (World Labs), service terms + billing dates (AISearch),
  timestamp proof + future-shipping caveat (DGX, conditional on inclusion).

## Candidate ↔ Discovery map (35)

sonnet55→w40-primary-sonnet55-20260928; gpt61sol→w40-primary-gpt61-sol-20260929;
geminiargon→w40-primary-gemini-argon-20260930; holo4→w40-primary-holo4-20260928;
elyza→w40-weak-elyza-20261002; ollama→w40-primary-ollama-jev-20260929; clef→w40-primary-cloudflare-clef-20261001;
decider→w40-primary-strands-decider-20261001; devday→w40-primary-openai-devday-20260929;
dots→w40-primary-openai-dots-20260929; agentsapi→w40-primary-agentsapi-computeruse-20260929;
agentsafety→w40-primary-nvidia-agentsafety-20260928; safetycases→w40-primary-openai-safetycases-20260928;
synthidbio→w40-primary-synthid-bio-20260930; provenanceguard→w40-primary-provenanceguard-20260929;
mcpauth→w40-primary-cloudflare-mcpauth-20261001; contextlm→w40-primary-contextlms-20260929;
agentperf→w40-primary-aa-agentperf-20260929; olmocore3→w40-primary-olmocore3-20261001;
opentts→w40-primary-opentts-20260930; rlenv→w40-primary-hf-rl-environments-20260928;
fluximage→w40-primary-flux3-image-20261001; vss→w40-primary-vss33-20260929;
nemotronasr→w40-primary-nemotron-asr-20260930; nemorelay→w40-primary-nemorelay-20260930;
amdross→w40-primary-amd-ross-20260930; worldlabs→w40-primary-amd-worldlabs-20260928;
aisearch→w40-primary-cloudflare-aisearch-20261001; dgx→w40-hold-dgxspark64-20261002;
pixelcanary→w40-carryover-pixelcanary-20261009; tbcvideo→w40-carryover-tbc-video-20261009;
astabrief→w40-hold-astabrief-20261002; autosynthdata→w40-hold-autosynthdata-20261002;
lift→w40-prewindow-lift-20260925; xledger→w40-grok-x-ledger-20261009.
(Sweeps r1/r2 EXCLUDED: w40-sweep-negativespace-20261009, w40-sweep-negativespace-r2-20261010.)
