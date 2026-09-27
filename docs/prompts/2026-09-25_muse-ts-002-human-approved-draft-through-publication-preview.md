# TS-002 — Human-approved Architecture → Draft → Validation → Publication Preview

Status:

`EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_APPROVED / DRAFT_THROUGH_PUBLICATION_PREVIEW`

Date: `2026-09-25 JST`

Repository: `eariver/japanese-generative-ai-survey`

Existing work branch only:

`special/beyond-text-2026-work`

---

# 1. Mission

The Human Owner has explicitly APPROVED the fresh TS-002 Architecture Review r2.

Materialize that Human decision using the current Survey Production Core v2 gate machinery, then continue the approved TS-002 edition through:

`ARCHITECTURE_REVIEW APPROVED`
→ `Draft`
→ `Validation`
→ `Publication Preview`

and stop at the next Human gate with a reviewable manuscript/PDF.

The normal terminal state for this execution is:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

or the exact current-Core equivalent.

Do **not** enter Freeze, Release, publication merge, release-record generation, or any post-Publication-Preview stage.

---

# 2. Human approval authority

The Human decision is recorded here and is authoritative for this execution:

`sources/SP-beyond-text-2026/execution/human-architecture-approval-20260925.md`

Sol pre-Human review authority:

`sources/SP-beyond-text-2026/execution/sol-architecture-review-r2-20260925.md`

Human review surface:

- `sources/SP-beyond-text-2026/execution/architecture-review-dossier-r2.md`
- `sources/SP-beyond-text-2026/architecture-v2.json`
- `sources/SP-beyond-text-2026/architecture-review-summary-v2.json`
- `sources/SP-beyond-text-2026/architecture-review-attention-v2.json`

The Human decision is:

`APPROVED`

Reviewed by:

`Human Owner`

Do not reinterpret this as approval of any manuscript, PDF, Publication Preview, Freeze, or Release. It approves only the Architecture Review r2 and authorizes progression to the next Human gate.

---

# 3. Mandatory start guards

Before any write, verify read-only:

- remote work branch HEAD equals the launch SHA supplied by the caller;
- remote work branch tree equals the launch tree supplied by the caller;
- remote `main` HEAD equals the caller-supplied reviewed main SHA;
- remote `main` tree equals the caller-supplied reviewed main tree.

If any guard mismatches:

- perform zero repository/GitHub writes;
- report expected vs actual;
- stop.

No new branch, fallback branch, repair branch, review branch, or iteration branch is permitted.

No force push, reset, rebase, or history rewrite.

---

# 4. First operation — materialize the Human Architecture approval gate

Use the current Core's canonical Human gate mechanism and the TS-001 precedent where applicable.

Create the canonical TS-002 Architecture approval surface, expected conceptually at:

`sources/SP-beyond-text-2026/gates/architecture-approval.json`

and any current-Core review-index / checkpoint / state surfaces required by the pipeline.

The approval must bind the **current approved r2** artifacts, not r1 and not a stale pre-sanitation architecture:

- current `architecture-v2.json` SHA256;
- current `architecture-review-summary-v2.json` SHA256;
- current `architecture-review-attention-v2.json` SHA256;
- `decision = APPROVED`;
- `reviewed_by = Human Owner`;
- review reference must identify the ChatGPT Human Architecture Review for TS-002 and the reviewed r2 commit/tree recorded in the Human authority file.

Use the actual canonical Core schema; do not hand-invent a parallel gate format if Core already provides one.

After materialization, validate that production state recognizes Architecture Review as approved before entering Draft.

---

# 5. Frozen approved Architecture

Draft against the approved 14-package Architecture. Do not silently redesign it.

Approved chapter/package order:

1. `arch-representation` — 表現と圧縮：生成可能にする短縮の歴史
2. `arch-paradigms` — 生成パラダイムと目的関数：AR・GAN・拡散・フローの分岐
3. `arch-conditioning` — 条件づけとアライメント
4. `arch-control` — 制御と参照：空間・参照・主体性の保存
5. `arch-editing` — 生成から編集へ
6. `arch-speech` — 音声・声の系譜
7. `arch-music` — 音楽・一般音響の系譜
8. `arch-video` — 映像の系譜
9. `arch-temporal` — 長時間・同期・編集の一貫性
10. `arch-runtime` — 実行と配備の経済
11. `arch-evaluation` — 評価の方法論：指標は交換可能ではない
12. `arch-convergence` — 収束問題：統合モデルか連携する専門家群か
13. `arch-capstones` — 2025–2026 capstone群：能力・workflow・lifecycleの証拠
14. `arch-reception` — 受容と counter-signal：現場の証拠

Approved planning envelope:

- target about 80 pages;
- 64–96 pages is guidance, not a hard cap;
- justified depth takes priority over compression;
- do not pad merely to hit a page count.

The Architecture r2 and dossier r2 are authoritative if any shorthand in this prompt omits detail.

---

# 6. Core editorial thesis

The manuscript must explain the technical history of media generation through the coordinate:

`representation/compression/tokenization`
→ `generative process / objective`
→ `conditioning / alignment`
→ `control / reference / identity preservation`
→ `editing / preservation`
→ `temporal / long-horizon structure`
→ `runtime / sampling / deployment`
→ `evaluation validity`
→ `multimodal convergence`

It is not a product catalogue.

For every major historical transition where evidence permits, preserve the causal structure:

1. what bottleneck existed;
2. what mechanism/representation/objective changed;
3. why that improved capability, stability, fidelity, controllability, or efficiency;
4. what trade-off/new failure mode appeared;
5. what successors inherited or replaced the mechanism.

The approved 43-entry semantic transition ledger is a primary drafting input, not optional background.

Do not collapse it into a chronology of famous model names.

---

# 7. Evidence authority and drafting discipline

Use the **active sanitized Evidence result-set**, active Edition Views, current candidate/selection artifacts, and current transition ledger.

Do not fall back to Discovery summaries when a verified Evidence card exists.

Do not treat raw Discovery prose as equivalent to Evidence semantic consumption.

Preserve source-local boundaries.

Current evidence state is expected to remain:

- VERIFIED: 126
- PARTIAL: 8
- NEEDS_MORE/HOLD: 5

Exact PARTIAL set:

- BT-D022
- BT-D059
- BT-D076
- BT-D083
- BT-D089
- BT-D098
- BT-D106
- BT-D134

Exact NEEDS_MORE/HOLD set:

- BT-D024
- BT-D072
- BT-D091
- BT-D120
- BT-D125

BT-D062 is VERIFIED and must not regress to PARTIAL.

PARTIAL/NEEDS_MORE status is an editorial boundary:

- use only facts actually established at the available source level;
- state material limitations where relevant;
- do not upgrade missing detail through narrative confidence;
- do not fabricate mechanism from product behavior.

Completeness is intentionally `LIMITED`; drafting must preserve that honesty rather than make the edition look artificially complete.

---

# 8. Mandatory anti-thinness rules

The Human Owner's core quality concern is a broad but shallow survey. Avoid that failure explicitly.

## 8.1 Representation is first-class

The representation chapter must materially explain why media modeling changed when pixels/waveforms/frames were mapped to:

- continuous latent spaces;
- discrete VQ codebooks;
- RVQ neural codecs;
- semantic/acoustic hierarchies;
- spatiotemporal/video latent representations.

Discuss compression/fidelity/token-rate/editability trade-offs where supported.

Representation must not be reduced to a short introductory glossary.

## 8.2 Architecture, objective, and sampling are distinct

Do not conflate:

- U-Net vs Transformer/DiT/other backbone architecture;
- autoregressive/adversarial/diffusion/score/flow objective/process;
- DDIM/ODE solver/distillation/consistency/few-step inference procedure.

Explain interactions without erasing categories.

## 8.3 Image must not dominate

Speech, music/general audio, and video must each have a coherent internal historical story with representation, mechanism, control/temporal, runtime, and evaluation implications.

Do not make chapters 6–9 appendices to image diffusion history.

## 8.4 Editing is not de-novo generation

Treat preservation, locality, reference identity, instruction following, inpainting/outpainting, multi-turn editing, audio continuation/infilling, and video editing as distinct technical problems.

## 8.5 Long-horizon is not sample fidelity

Separate:

- local perceptual fidelity;
- short-range coherence;
- identity/object permanence;
- AV/lip synchronization;
- continuation consistency;
- minute-scale/structural/narrative coherence;
- edit preservation over time.

Do not infer long-horizon competence from a polished short sample.

## 8.6 Runtime/deployment is technical content

Where supported, preserve:

- steps / NFE;
- latency / first-package latency / RTF;
- VRAM / memory;
- quantization / offload;
- hardware/config binding;
- local/open vs closed deployment constraints.

Do not compare numbers across unmatched hardware/configuration as if directly commensurate.

## 8.7 Evaluation metrics are not interchangeable

Keep FID/IS, FAD/CLAP, WER/speaker metrics/listening tests, music preference studies, VBench/VBench-2.0, physics/commonsense and AV/lip-sync metrics in their actual protocol/modality context.

Do not manufacture a universal leaderboard.

## 8.8 Closed-system boundary

Closed current products may establish:

- disclosed capability;
- workflow;
- availability/lifecycle;
- vendor-reported evaluation only with attribution;
- practical reception where independently observed.

They do **not** establish undisclosed architecture, tokenizer, training recipe, or mechanism.

## 8.9 X/community boundary

The X reception aggregate is useful only for:

- practical adoption;
- deployment/reproduction;
- creator workflows;
- runtime pain;
- observed failures/counter-signals.

It is not technical architecture authority.

---

# 9. LOW_SIGNAL lanes

Do not hide or inflate these unresolved lanes:

- full-duplex interruption/overlap measurement;
- cross-lingual voice-cloning degradation;
- long-range music structure metrics;
- automatic metric vs human-preference contradictions;
- Nano Banana editing corpus limitations;
- few-step ablation strength;
- pure-generation flow-vs-diffusion comparisons;
- consumer-GPU FLUX.2-klein replication;
- independent ElevenLabs Music evaluation;
- Wan 2.5+ authority after open 2.2 line;
- Sora mechanism.

If later-stage drafting discovers no new authorized source, label the uncertainty/open question rather than filling it speculatively.

Do not run a new broad research campaign in this execution unless current Core explicitly requires a bounded late validation lookup for a citation or publication claim. Any such lookup must not silently alter the approved Architecture.

---

# 10. Draft requirements

Produce the canonical Draft artifacts required by current Core.

Publication manuscript output should follow the repository's established longform Special format, including at minimum the equivalent of:

- `surveys/special/beyond-text-2026/main.tex`
- `surveys/special/beyond-text-2026/references.bib`
- `surveys/special/beyond-text-2026/main.pdf`

if those are the current profile's canonical output paths.

Do not invent a different publication layout if the profile/Core specifies one.

The manuscript must be primarily Japanese prose, with technical terms retained in English where clearer/standard.

Quality expectations:

- explanatory paragraphs, not bullet-list dumping;
- explicit transitions between eras/techniques;
- tables only when they improve structured comparison and conditions are commensurate;
- no giant product matrix substituting for narrative;
- citations near factual claims;
- bibliography entries resolve and are actually cited where appropriate;
- vendor claims clearly attributed;
- uncertainty and evidence boundaries visible but not repeated mechanically in every sentence;
- no unsupported superlatives such as “best”, “SOTA”, “most realistic” without condition-bound source support.

---

# 11. Page-depth guard

The approved page plan is a planning guide. After typesetting, audit actual page allocation against the approved emphasis.

Do not accept a manuscript merely because total page count lies in 64–96 pages.

Check specifically that:

- representation and paradigms receive substantial explanatory space;
- speech, music, and video each remain substantive;
- runtime and evaluation are not collapsed to token sections;
- capstone/current-product discussion does not consume a disproportionate share;
- reception/X remains compact and bounded;
- front/back matter does not artificially create the appearance of depth.

If actual pagination materially diverges from the approved architecture because prose density differs, prefer editorial substance over mechanically restoring exact page numbers. Record the delta and rationale in the session report.

---

# 12. Validation requirements

Run all current-Core Draft/Validation/Publication Preview validators required by the profile.

Additionally perform edition-specific checks for at least:

- all 14 approved packages represented in the manuscript;
- all 43 transition-ledger entries accounted for in prose planning/coverage (directly or by justified merged synthesis);
- no active stale provenance future-repair language reintroduced;
- canonical repaired locators used in bibliography/citations;
- PARTIAL/NEEDS_MORE limitations not silently promoted;
- closed-system non-inference boundary preserved;
- X/community material not used as architecture authority;
- TS-002/TS-003 boundary preserved;
- architecture/objective/sampling distinctions not collapsed;
- generation/editing distinction maintained;
- no unsupported cross-condition metric ranking;
- references compile and resolve internally;
- no broken citations or missing bibliography keys;
- no obvious duplicated paragraphs/sections;
- no placeholder/TODO/TBD text unless an explicit Publication Preview blocker is intentionally surfaced;
- no accidental raw execution metadata exposed in reader-facing prose.

## PDF / typesetting QA

Build the PDF and inspect the rendered output, not only LaTeX exit status.

At minimum check:

- page count;
- title/TOC/section hierarchy;
- table overflow/clipping;
- figures if any;
- overfull/underfull problems that visibly affect readability;
- broken Japanese line wrapping;
- citation/bibliography layout;
- orphan headings / near-empty pages;
- footer/header collisions;
- malformed URLs;
- table cells or long technical identifiers crossing margins;
- PDF opens and renders all pages.

If visual/layout issues are found, repair them before presenting Publication Preview, provided the repair does not alter approved research semantics.

---

# 13. Publication Preview stop

After a validated, reviewable PDF is built, create the canonical Publication Preview review surface required by current Core and stop.

Do **not** generate a Human Publication Preview decision.

Do **not** create `publication-preview-approval.json` yourself.

Expected terminal semantics:

- Architecture Review: APPROVED;
- Draft: complete;
- Validation: complete/passed subject to any explicitly reported non-blocking warnings;
- Publication Preview: pending Human decision;
- Freeze: not entered;
- Release: not entered.

The Human Owner must be able to inspect the actual PDF before approving Publication Preview.

---

# 14. Required session report

Create an execution session report under:

`sources/SP-beyond-text-2026/execution/sessions/`

with at least:

- start guard expected/actual values;
- Architecture approval materialization details and hashes;
- resulting gate/review-index/state references;
- active Evidence/View/transition/Architecture hashes used for drafting;
- Draft artifact paths/hashes;
- manuscript section/chapter inventory;
- actual PDF page count;
- approximate page allocation by approved package/chapter;
- bibliography/citation counts;
- transition coverage result (43 entries);
- PARTIAL/NEEDS_MORE handling confirmation;
- LOW_SIGNAL handling confirmation;
- closed-system and X boundary audit;
- validation commands/receipts/results;
- PDF/typesetting QA findings and fixes;
- remaining warnings/open issues suitable for Human Publication Preview review;
- final production lifecycle state;
- final remote HEAD/tree after non-force push;
- explicit confirmation Freeze/Release were not entered.

---

# 15. Prohibitions

Do not:

- create another branch;
- alter shared Survey Production Core v2;
- change the approved Architecture merely to simplify drafting;
- rerun broad Discovery/Screening/Evidence research;
- discard existing semantic Evidence and redraft from summaries;
- infer hidden architecture of closed systems;
- use X as technical authority;
- silently resolve PARTIAL/NEEDS_MORE/LOW_SIGNAL uncertainties;
- force push/rebase/reset/rewrite history;
- enter Freeze or Release;
- fabricate Human Publication Preview approval.

Normal commit(s) and non-force fast-forward push to the existing branch only.

---

# 16. Success condition

Success means a Human-approved Architecture has been formally materialized, a substantive longform TS-002 manuscript has been drafted from semantic Evidence, validated and rendered, and a reviewable Publication Preview PDF is available while the pipeline is stopped at the next Human gate.

Expected stop:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`
