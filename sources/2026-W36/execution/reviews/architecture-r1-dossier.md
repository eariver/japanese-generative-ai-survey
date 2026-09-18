# Human-facing Architecture Review dossier — 2026-W36 r1

Edition `2026-W36` (WEEKLY + WEEKLY_MAGAZINE). Lifecycle `ARCHITECTURE_ESTABLISHED`, terminal `HUMAN_GATE_REACHED`. No Human decision recorded or inferred.

## 1. Exact review identity

- Edition/revision: `2026-W36` r1; research profile `WEEKLY`, publication profile `WEEKLY_MAGAZINE`.
- Reviewed repository commit SHA: `0295bd08c6b46a5b1be3a10051970d9e749cc73b` (tree `c5111e91509d6b68a28be2b7520ab54acee43bdd`; this dossier is presented against the exact pushed commit recorded in `architecture-r1.md`).
- Start-of-run reviewed `main`: `5acbff8528890ed9fc324c0227e6c4e43067c438`; pinned Production Line `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (untouched; verified at every stage).
- Current lifecycle/Gate state: `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW` pending / Publication Preview pending.
- Gate inputs (r1): `architecture-v2.json` (thesis + 6 packages), `architecture-review-summary-v2.json` (READY_FOR_ARCHITECTURE_REVIEW), `architecture-review-attention-v2.json` (1 HOLD attention item).

## 2. Research coverage

- Source Intake surfaces: required Weekly X intake (`weekly-x-2026-W36`, Grok r4 accepted: 15 URLs — 12 ordinary [3 official + 9 independent from 8 accounts], 0 background, 3 late-breaking; manifest COMPLETE) + 18 edition-local primary Raws (OpenAI x3, Anthropic x3, NVIDIA, Google x3, Meta, IFM, Z.ai/HF, World Labs, fal PR, arXiv, Microsoft, Kilo) + pre-Discovery 12-lane breadth sweep.
- Discovery scale: 19 BASE records (1 X-ledger + 18 primaries), graph `9c55b223`, all research_pass 0; Screening 19 KEEP / 0 DROP; Evidence 13 VERIFIED / 6 PARTIAL.
- Independent completeness findings (Sol review): all 12 lanes examined; F (speech/audio model release) and I (standalone memory/retrieval) quiet after Grok + first-party recheck; C has Atlas only; H covered via K2/fal/GLM paths; GLM boundary date medium-confidence; Lance-3B Aug-29 claim correctly excluded (primaries May 2026); ZCode Sep-01 correctly excluded (no dated primary); post-cutoff items (vLLM 0.29, AgentAudit, Sep-09 assessment, Gloo) correctly separated.
- Residual coverage gaps: speech/audio and memory/retrieval model releases (may be genuinely quiet); FUSE full text; Muse methodology report; Astra system-card subpages; HF acquisition blog; GLM hour precision.

## 3. Evidence quality

- Status counts: VERIFIED 13 / PARTIAL 6; materiality MATERIAL 18 / CONTEXT 1; completeness LIMITED with 3/3 obligations SATISFIED.
- Authority-consumption findings: 18 primary bodies consumed at claim level (full pages read; findings mapped to exact sections); abstract-only FUSE and image-only Muse scorecard explicitly bounded; X never promoted beyond SOCIAL_OBSERVATION + ledger PRIMARY_FACT recount; W35 never copied; 4 issue-local vocabulary defects repaired edition-locally with full regeneration (no Core defect).
- Consumed-not-merely-bound: Astra monitorability decrease, 54K-task figures, Fermat triple-check, $12.93B agreement language, Fable/Gemini/Muse efficiency deltas, K2 audit correction, GLM license field, Atlas/Copilot/Kilo capability enumerations — each converted into bounded claims with limitations reflecting the source.

## 4. Major candidate map

- SELECTED (18): Astra safety/path/launch (flagship safety, PRIMARY x3); Fermat science/github (formal verification, PRIMARY x2); NVIDIA-HF (ecosystem platform, PRIMARY); Fable/Mythos, Gemini blog, Muse Spark (frontier coding, PRIMARY x3); K2, GLM weights (open efficient, PRIMARY x2); Atlas (spatial, PRIMARY); Pics (productization, PRIMARY); fal H3 Max (video, PRIMARY); FUSE (methods, SUPPORTING); Copilot harness, Kilo (agent harness, PRIMARY x2); Grok r4 ledger (community signal, SUPPORTING).
- HOLD (1): Gemini model card (CONTEXT companion; watched, unarchitected to avoid duplicating the release event).
- DROP (0): no background-only item required exclusion.
- Excluded/misdirected (correctly out): Lance-3B, ZCode-Sep01, Hy4-as-fresh, post-cutoff items, late-breaking X posts (context only), W35 HOLD abstracts (no attached event; not inherited).

## 5. Negative-space / omission review

- Important unselected: Gemini card (deliberate grouping hygiene — its eval richness duplicates the SELECTED blog event; inspected, not a consumption defect); W35 video abstracts (superseded by W36's own fal H3 Max window event); late-breaking X security/exploit anecdote (post-cutoff, must not enter ordinary totals).
- Why absent from the issue: card HOLD avoids double-counting one release; W35 abstracts have no W36-window event attachment; late-breaking items are post-cutoff momentum, eligible only as context.
- Quiet lanes F/I are declared gaps with recheck evidence, not oversight.

## 6. Editorial thesis

In 2026-W36 frontier capability turned governable-and-checkable — OpenAI shipped its first Critical-cyber model under broad monitoring while admitting weaker monitorability, Anthropic closed the largest computer-checked proof in Lean with a replayable artifact, and NVIDIA moved to own the open platform it pledges to keep neutral — while open efficient fleets, frontier coding releases, agent harnesses, and spatial/video productization filled out a dense, source-bounded week. The synthesis fits a week where the three heaviest events each pair a capability step with an explicit check (monitoring, proof artifact, openness pledge) and the undercard is unusually broad.

## 7. Architecture packages

1. `w36-astra-critical-cyber` — Astra safety/path/launch PRIMARY + Grok + FUSE SUPPORTING. Role: flagship safety/computer-use. Boundaries: vendor-evals publisher-only; launch date edition-attributed; FUSE abstract-level.
2. `w36-fermat-proof` — Fermat science + repo PRIMARY. Role: formal verification. Boundaries: verification-not-new-proof; no rerun; repo date edition-attributed.
3. `w36-open-efficient` — K2 + GLM PRIMARY. Role: open weights. Boundaries: Apache covers code/models not datasets; GLM MIT is Flash-only; GLM window medium-confidence.
4. `w36-frontier-coding` — Fable + Gemini blog + Muse PRIMARY. Role: proprietary coding. Boundaries: all figures vendor-reported; Muse scorecard excluded; Gemini methodology missing.
5. `w36-agent-harness` — Copilot + Kilo PRIMARY. Role: agent infrastructure. Boundaries: preview labels preserved; no independent testing.
6. `w36-ecosystem-spatial-media` — NVIDIA-HF + Atlas + Pics + fal PRIMARY. Role: platforms/spatial/media. Boundaries: deal announced-not-closed; Atlas preferences vendor-reported; H3 rankings date-bound.
Order follows evidential weight (strongest convergence first). No W35 structure copied; no model-specific number/license/benchmark generalized cluster-wide (W35 r1 failure mode explicitly avoided: per-model licenses, per-model benchmarks, per-record dates preserved).

## 8. Page/section allocation

Deferred to drafting (page_plan notes order above is the editorial order; target/max pages null). No optional-section omission decided. Six packages suggest a full-issue week; Paper Watch inclusion for FUSE is a drafting decision pending approval.

## 9. Counterfactual alternatives

- (a) Flagship-coding-first (P4 first): rejected — proprietary coding claims are least-verified (PARTIAL, methodologies missing); leading with weakest-verified claims misleads.
- (b) Single frontier mega-package (all flagship models together): rejected — forces cluster-wide generalization across distinct licenses/benchmarks/autonomy claims (the W35 r1 failure mode).
- (c) Sparse issue (Astra + Fermat + NVIDIA only, rest HOLD): rejected — compression audit not triggered (18 SELECTED) and the undercard carries independently consumed authority; sparsity would hide verified research.

## 10. Known limitations and risks

Vendor figures publisher-only throughout; edition-attributed dates (Astra launch page, Fermat repo) flagged; GLM boundary medium-confidence; NVIDIA-HF pledges not facts; FUSE abstract-only; Muse scorecard excluded; F/I quiet; C thin (Atlas only); H via paths; late-breaking out of scope; engagement/star counts fetch-time; no independent reproduction of any benchmark; W35 judgments not inherited (verified zero carry roles).

## 11. Sol review finding

0 blocking findings; 1 non-blocking (P3 boundary weight, inherited into must-cover bounds). Coverage, authority-consumption, materiality/selection, and architecture reviews all recorded in `execution/decisions/sol-w36-supervisory-reviews-20260917-r1.md`. Recommendation: present for Human Architecture Review; do not auto-advance. Machine READY status and deterministic PASS do not substitute for Human judgment of research sufficiency — this dossier supplies that judgment basis.

## 12. Human decision options

After reviewing the above, please choose: `APPROVED` (record against the exact reviewed commit; continue to drafting) or `REQUEST_CHANGES` (supply requested changes + one allowed pre-Architecture regeneration boundary from ISSUE_INITIALIZED / DISCOVERY_COLLECTED / CANDIDATES_NORMALIZED / EVIDENCE_REVIEWED / SELECTION_COMPLETE; Core records rN and returns to that boundary). Silence is not a decision.
