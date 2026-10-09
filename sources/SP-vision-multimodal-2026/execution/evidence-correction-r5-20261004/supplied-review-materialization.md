# Supplied fresh independent Draft content review — materialization (EVIDENCE CORRECTION REQUIRED)

Provenance: materialized from supplied fresh independent Draft content review received 2026-10-04
against Exact Starting SHA `382833c30d294f54e847c0333fc4a03a58748a32`
(tree `08d50dfa7bf3150051564c1b6cc08bf4c9ad7c4b`).
Reviewed main `d6381568cc897a47d6de992189e20339350342b7`
(tree `83ce3a216d852a1c32d0138f9c56fadefa800666`).
Frozen Production Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
(tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`).
Remote work-branch HEAD/tree, remote main HEAD/tree, and Frozen Core commit/tree were all
read-only verified as exact matches before any write. No mismatch; no stop was required.

This file is a worker transcription of the supplied review's decision and directives.
It is NOT a worker-performed review, NOT a Human review, NOT a Human decision, and NOT an
Architecture Review. No Human/Sol approval is generated or self-declared by this file.

Working-tree note: the working tree carries uncommitted bytes from the prior
`content-revision-r4-20261004` run (16 draft-results + synthesis + checkpoint + state
provenance). Those bytes are NOT part of the reviewed starting authority and are NOT
touched by this run (old Draft is never patched here; Draft is never regenerated here).

## Decision

- Accepted Evidence authority itself contains at least one factual defect → this is NOT a
  `DRAFT_COMPLETE`-internal prose repair.
- Ordered trajectory: `targeted Evidence correction` → downstream deterministic replay →
  fresh Architecture authority → fresh pending Human Architecture Review r5.
- Human Architecture r4 APPROVED is preserved as history. It is NOT reused for any new
  Architecture (Evidence change breaks the exact hash chain r4 bound).
- Normal end state: fresh `ARCHITECTURE_REVIEW r5 PENDING` → STOP. No Draft regeneration,
  no TeX, no PDF, no Publication Validation.

## Reviewer-side authority corrections (mandatory correction note, §2)

1. Current approved Architecture artifact is `sources/SP-vision-multimodal-2026/architecture-v2.json`
   SHA-256 `71cb47989f328ed002f5db561345c7031d3360e6e4d7e0b0ee8d5f53d5975f72`.
   `architecture-v4.json` is NOT current r4 authority. Do NOT confuse Human review revision
   `r4` with artifact filename/version `v2`. (Repo note: `architecture-v3.json` /
   `architecture-v4.json` exist as non-canonical replay/proposal artifacts; only
   `architecture-v2.json` is bound by r4 approval + state provenance.)
2. Video IDs: `VM-D089 = Flash-VStream` (online streaming contract);
   `VM-D112 = Agentic Video Understanding` (stored-timeline / query-driven selective
   acquisition contract). Any supplied-review wording of the form
   `VM-D089 = agentic/on-demand video authority` MUST NOT be used as authority.
   Current Architecture `p15_cross_package_synthesis_map` contains VM-D089 but NOT VM-D112.

## Directives (faithful transcription, §§3–16)

- §3 Re-entry boundary: current state `DRAFT_COMPLETE`; Evidence checkpoint provenance bound
  in `CANDIDATES_NORMALIZED.json`. No Discovery/Screening redo. Re-enter via canonical Core
  mechanism to the boundary where Evidence is regenerable. Expected semantic boundary:
  `CANDIDATES_NORMALIZED`. No hand-mimicked state/checkpoint edits. Use Core-required formal
  operator invalidation / re-entry mechanism. Discovery 112 + Screening authority unchanged.
- §4 Mandatory correction VM-D062 LLaVA: current `end-to-end vision-encoder+LLM tuning` is
  wrong as stated. Re-confirm primary; materialize at least training topology: Stage 1 =
  visual encoder frozen + LLM frozen + projection matrix trainable; Stage 2 = visual encoder
  remains frozen + projection trainable + LLM trainable. Do NOT confuse the paper's
  `end-to-end trained large multimodal model` system phrasing with updating the vision
  encoder end-to-end. Split claims追跡可能に: instruction-data generation /
  architecture-interface / Stage 1 / Stage 2 / evaluation conditions / limitations.
  Remove the old wrong claim.
- §5 Targeted depth (NOT all 112): VM-D061 MiniGPT-4 (BLIP-2 stack/ViT/Q-Former/freeze/
  single linear projection/Vicuna; Q-Former removal is ablation variant; prevent
  `Q-Formerのようなquery選択を持たない` vs `BLIP-2由来のViTとQ-Formerを凍結して借りる`
  self-contradiction recurrence); VM-D034 DINO (centering/sharpening/momentum teacher/
  teacher-student/temperature IF Draft uses them — formally Evidence-ize from primary;
  never keep reversed `student-sharpen/teacher-smooth`; unverifiable detail gets no Draft
  authority); VM-D033 MAE (asymmetric enc-dec/visible-only/mask ratio/decoder-depth/
  pixel target/normalized-vs-unnormalized/linear-vs-finetune IF kept; default vs final
  recipe distinguished; low-value granularity ledgered for Draft deletion); VM-D103 I-JEPA
  (card already holds `single context block → multiple target-block representations`;
  no change in principle; read back canonical wording); VM-D102 DreamerV3 (RSSM +
  imagination-based policy improvement held; expand only if current Evidence insufficient
  for mechanism-depth restoration).
- §6 P05/P06/P08 granularity ledger: Draft statement → Evidence claim/metric/limitation →
  supported/unsupported/over-specific (LayoutLM/Donut/Nougat/GOT/DocVQA/MAE/DINO/MiniGPT-4/
  LLaVA). Strengthen Evidence only for FULL/TRANSITION load-bearing mechanism needed by
  survey depth; ledger the rest for Draft deletion. No mechanical "prose-exists-so-expand".
- §7 Molmo 2 currentness (VM-D071/VM-D077, limited): paper-side open release already in
  Evidence (Open weights/data/code + 9 datasets); repo-bound VM-D077 holds older unresolved
  license/data-availability state. Only if first-party current source can update currentness
  of EXISTING candidates with NO Discovery mutation, sort Molmo-2-owned open release / code
  license / newly released datasets / third-party restrictions into separate buckets. Never
  confuse Molmo-2 Apache-2.0/open release with third-party mixture licenses. If Discovery
  addition needed, report instead of widening.
- §8 Preserve unaffected Evidence: no semantic rewrite by regeneration; keep 112 identity;
  non-targets byte-identical/deterministically unchanged; never promote PARTIAL×5 to
  VERIFIED by prose.
- §9 Downstream replay via current formal pipeline: Evidence acceptance, Edition Views,
  Materiality, Completeness, Candidate Matrix, Selection, Architecture, both review
  summaries, required checkpoints/state. No arbitrary Selection change. Expected semantic
  result: 112 Discovery / 112 selected chain / 16-package skeleton / P04 four-node cap /
  P07A-B split / P11 three contracts / P14 four-pole / VM-D112 P09-P11 SUPPORTING /
  Something-Something V1 lineage / P15 39-authority map. Genuine semantic diffs only if
  truly required, explicitly diffed.
- §10 P15 contract: keep root `p15_cross_package_synthesis_map` (39 distinct authorities).
  Record P15-Draft-14-only consumption as known Draft-stage blocker; do NOT implement the
  overlay this run (no Draft yet); hand off 39-map → edition-local binding for post-r5 Draft.
  Never weaken Architecture to fit current P15 Draft.
- §11 VM-D112/VM-D089 discipline: streaming vs stored-timeline/query-driven; never confuse;
  never add D112 to P15 map on replay; preserve r4 semantic design.
- §12 Deferred post-r5 Draft handoff (NOT this run): MiniGPT-4/LLaVA/DINO/MAE prose,
  MMMU/MMBench decontamination, I-JEPA wording, P15 39-authority materialization +
  repetition removal, POPE terminology, terminology normalization, DreamerV3 depth,
  Molmo 2 wording/currentness, synthesis regeneration.
- §13 Core Freeze: no shared Core change (drafting scripts/schemas/config/workflows
  untouched); record mixed-placement defect as deferred, do NOT solve.
- §14 Gates: r4 APPROVED → history; fresh Architecture NEVER treated as r4-approved;
  new surface `ARCHITECTURE_REVIEW r5 = PENDING`; no worker-generated Human decision;
  no self-declared Sol/Human approval.
- §15 Final readback items; §16 terminal: DRAFT_COMPLETE → re-entry → correction → replay →
  ARCHITECTURE_ESTABLISHED → r5 PENDING → STOP (no Draft/TeX/PDF/Validation).
