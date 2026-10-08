# TS-003 Human Architecture Review Dossier — r9 candidate with P12 Evidence-safe cost framing (fresh)

Status: `ARCHITECTURE_REVIEW_R9_PENDING / DOSSIER_FRESH / NO_APPROVAL_RECORDED`

- Edition: `SP-vision-multimodal-2026` (THEMATIC / LONGFORM_SPECIAL)
- Revision: Architecture r9 candidate (`architecture-v2.json`, status PROPOSED)
- Architecture SHA-256: `cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af`
  (previous r9 candidate `549ae186…`; delta is P12-only, see below)
- Lifecycle: `ARCHITECTURE_ESTABLISHED`; gates: architecture_review `pending`,
  publication_preview `pending`; no active approval.
- Reviewed bytes: the exact pushed head of branch
  `special/vision-multimodal-2026-work` for run
  `execution/r9-p12-cost-framing-20261008` (HEAD/Tree in the run's final report).
- Prior surfaces: r8 APPROVED records preserved as history; the two previous r9
  dossiers (P02 bridge; attribution closure) remain untouched history — this fresh
  dossier is the active Human review surface.

## 1. What this execution changed (P12 only)

- P12 must-cover BEFORE:
  `Screenshot-loop token costs via TS-001 vocabulary; safety audits as eval metadata only`
- P12 must-cover AFTER: `Long-horizon interaction and state-management burden:
  measured tool-call counts may be used as an interaction-horizon/state-management
  proxy; token, context, memory, latency, or compute costs may be asserted only
  where directly measured by bound Evidence. Safety audits remain evaluation
  metadata only.`
- P12 boundary ADDED: `Tool-call count is not itself a direct measurement of token
  count, context-window utilization, KV-cache/memory footprint, latency, or compute
  cost. It may be used only as a proxy for interaction horizon and state-management
  burden unless a corresponding efficiency field is directly measured by bound Evidence.`
- Semantics: tool-call count = directly measured; interaction horizon /
  state-management burden = legitimate proxy interpretation; token / context-memory /
  KV-cache / latency / compute costs NOT inferred from tool calls; direct efficiency
  claims require direct Evidence. Bound Evidence (VM-D091: 108 long-horizon workflows,
  318.4 tool calls with exact conditions, state-management bottleneck) supports
  exactly this framing and measures no token/KV/context/compute field directly.
- P12 long-horizon thesis, OSWorld 1.0/2.0 distinction, and exact condition binding
  (model/thinking/tool/steps/release) preserved.

## 2. What did NOT change

- P02: bridges, convergence wording, depth, budget, disambiguation — byte-identical.
- P15: purpose, must-cover, synthesis map (40 entries), budget, depth — byte-identical.
  The 4-role evaluator taxonomy stays a fresh-Draft requirement, not Architecture.
- P04: X02 wording untouched (DUSt3R downstream links recorded as a deferred Draft
  guard: editorial synthesis, not causal inheritance).
- P01/P03/P05/P06/P07A/P07B/P08/P09/P10/P11/P13/P14: byte-identical.
- Evidence 124 (119/5), Selection 124, Completeness judgments, matrix content,
  Discovery 125: all unchanged (machine-proven identical SHAs in the run audit).

## 3. Research coverage / Evidence quality / candidate map

Unchanged from the previous r9 dossier (attribution closure): Discovery 125,
Evidence 124 (119/5, source-local), Selection 124, VM-O02 SATISFIED, P15 40/40.
No intake, no new Evidence, no status changes in this run.

## 4. Omission review

No new omission; no expansion (Conditional/Anchor DETR still out by design).

## 5. Editorial thesis / packages / pages

Unchanged except the P12 cost-framing contract. P02 budget 6, P12 budget 5 held.

## 6. Counterfactuals

Keeping the old `Screenshot-loop token costs` wording was rejected: it licenses
downstream Draft to convert tool-call counts into measured token/context/memory
costs the Evidence does not support. No other alternative was in scope.

## 7. Limitations / risks

- The correction constrains Draft wording; it adds no new claims to defend.
- rev5 Draft not regenerated; queued Draft corrections (see deferred list) still
  pending. Coverage Freeze unchanged (P02-bridge exception still the only one).

## 8. Sol findings and recommendation

- P12 correction verified against bound Evidence (Sol-level check in-run:
  VM-D091 supports tool counts + state bottleneck; no direct cost measurement).
- Sol blocking findings: none.
- Recommendation: Human APPROVED (continue to fresh Draft) or REQUEST_CHANGES
  with a pre-Architecture boundary. No worker approval; no Draft; no publication.

## 9. Human decision options (only now that the above is presented)

- `APPROVED` — record against the durable reviewed commit via the Human Gate
  mechanism; then continue to drafting.
- `REQUEST_CHANGES` — supply requested changes + one allowed pre-Architecture
  regeneration boundary; Core invalidates only affected downstream authority.
