# J-GAS W41 — Muse r7 canonical Selection → developed Architecture → fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / SOL_SELECTION_R6_PASS / CORE_V2_IMMUTABLE / STOP_AT_ARCHITECTURE_REVIEW_PENDING`
Date: 2026-10-12 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch ONLY: `weekly/2026-W41-v2-work`
Sol independent Selection audit: `sources/2026-W41/execution/reviews/sol-w41-selection-semantic-r6-PASS-20261012.md`
Source Muse reviewer surface: `execution/SOL_SELECTION_MATERIALITY_PREVIEW_HANDOFF-r6.md` and `execution/selection-preview-r6.md`.

## 0. Exact starting gate — read-only before ANY mutation

Invoke with exact remote W41 Starting HEAD and Tree supplied by Sol separately (the exact commit containing THIS instruction).
- Remote W41 HEAD/Tree == invoking exact identities.
- THIS instruction commit parent == `12c192d4b592ea9979d6ac9050605d65c6b8e5d3` (Sol Selection audit terminology-corrected).
- Muse r6 HEAD/Tree `0e80f00e822af27c5a95c73041c895c8b3eaf687` / `66604739735ff2a1b1dfe79f23028587746b772b` in exact ancestor chain.
- Remote main HEAD/Tree `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8` / `31c0adc5b57761e5073d100554279a8adc5a18f4`.
- Remote shared Core `production/survey-core-v2` HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- W41 State `EVIDENCE_REVIEWED / stage:selection`, Discovery/Screening/Evidence/Materiality/Completeness machine checkpoints PASSED, selection and all later checkpoints PENDING; both Human Gates `pending` and no Human approval provenance.
- Accepted 37 Discovery/37 Screening/36 Evidence and 36 View graph unchanged; exact Evidence set `717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db`, Views set `cd661097ccfb2c4e3960a334d2aab39b629fc656436593186011fe416f0a04b2`, canonical Materiality37 20/13/3/1 and Completeness `LIMITED`.
- No conflicting remote execution or unowned dirty local edits.

Any mismatch => STOP / **ZERO WRITES** and expected/actual report. No new/fallback/repair/review branch, reset/rebase/cherry-pick/force push, history rewrite, shared Core/schema/config/scripts/workflow edits, main/W40/other-edition mutation, Issue change or Human Gate decision.

## 1. Read order and scope authority

1. This contract + full Sol r6 Selection PASS audit (S41-A..D).
2. W41 r6 `execution/candidate-matrix-r6.PROPOSED.json` (SHA-256 `0d56de2b8b1b0417ce7f0cac34283a4549e6e91ca5279016aa826416e9f98d25`) and `execution/candidate-selection-r6.PROPOSED.json` (SHA-256 `3bedcb4acbb80647539ef3a318fd6ce654e31a540d9a6e76e55d2361ab729033`); `execution/selection-preview-r6.md` and `execution/materiality-editorial-dossier-r6.md`.
3. `execution/nanobanana-legacy-negative-exclusion-r6.md`; canonical `materiality-ledger-v2.json` (20/13/3/1), `profile-completeness-v2.json` (LIMITED).
4. Core frozen `scripts/survey_architecture_v2_base.py` (derive/validate Matrix, validate Selection, validate Architecture, build Architecture Review Summary), `scripts/survey_architecture_v2.py`, `scripts/survey_stage_validation_v2.py`, stage/checkpoint/State contracts and quality contract; see W40 r18-r20 as **format/quality precedents only**.
5. Accepted Evidence 36 + exact 36 View source bindings; W41 Daily X 7 source originals / 92-topic crosswalk and Grok 14 links / 12 in-window and 2 out-of-window, only if needed to resolve source roles (no broad new discovery).

## 2. Canonical Selection and exact stage

- First independently recompute Preview candidate IDs and basis hashes. Matrix exactly **36**; Selection exactly **36** unique assignments = `20 SELECTED (5 PRIMARY, 15 SUPPORTING) + 13 HOLD + 2 INSPECT + 1 REJECT`. Exact Crosswalk through 36 accepted Evidence/View references.
- Canonicalize `sources/2026-W41/candidate-matrix-v2.json` and `sources/2026-W41/candidate-selection-v2.json` ONLY from the Sol-reviewed r6 preview via frozen Core builders/validators; preserve exact preview bytes if Core accepts them. Never treat `PROPOSED` path as already canonical; never alter `status=ESTABLISHED` preview to fabricate an earlier State.
- Run frozen Core `validate_candidate_matrix` and `validate_selection` on canonical files with the **actual current basis**. No new additions, no changed Materiality or HOLD promotion, no change in selected roles/architectural usage. 2 INSPECT and Grok ledger are nonselected and cannot enter Architecture packages.
- Run canonical Stage Validation/checkpoint + normal State transition `EVIDENCE_REVIEWED -> SELECTION_COMPLETE` via current Core/authorized trusted bridge. Exact SHA readback, no manual State/checkpoint editing. If any contract basis/implementation mismatch, STOP and report; no monkeypatch/fallback/shadow authority.

## 3. Substantive Architecture — not a thin news outline

Once `SELECTION_COMPLETE` exists:
- Draft a **genuinely developed**, validated W41 Architecture. Use roughly **six coherent editorial packages** rather than forcing 20 standalone articles; adapt package boundaries to actual Core schema. Five PRIMARY candidates (GPT-6+Intelligent UI, Claude Haiku 5.5, Decisions API beta, Kolibri, textGrain) each placed **exactly once** as PRIMARY. All 15 SUPPORTING placed at least once, appropriately as briefs, analytical subtopics or comparators; do not repurpose as PRIMARY without fresh Sol Selection review. Every selected candidate's source Matrix `remaining_boundaries[]` membership must appear *exactly and fully* in destination Architecture package boundaries arrays as Core requires. Preserve explicit counts, IDs and SHA crosswalk. No nonselected assignments in packages and no invented/invalid role namespaces.
- Editorial groups and potential core story:
  A. GPT-6 + Haiku rollout, tier/price/safety/system-card evidence distinctions and 44% **time-to-start** vendor claim (not wall-time).
  B. Agent and Decisions infrastructure: Decisions API beta, Perplexity decider/embed, Ultrafast and Gemini Work agent stub (distinguish technical API spec from marketing and forum observations).
  C. Shipped-vs-promised local/open weights: Kolibri, Liquid d1, EmbeddingGemma 2, Reflection Beam, Mistral Large 4, compare MoE active/total, licensing, actually downloadable vs promised; serve audio Clef-omni/Nova Sonic in same or separate scoped group according to evidence depth.
  D. Image model card: Nano Banana 2.1 brief with real card specs and vendor Elo, carefully limited negative-search language.
  E. Provenance/safety: textGrain + SynthID with publisher-reported FPR/token/edit, verification scope, *unconsumed tech PDF* limits, no unproven efficacy and cross-modality false equivalence.
  F. Safety/science briefs: Anthropic Cyber Mission, OpenAI maths, Ironclad simulated computer-use evaluation; no invented field deployment or benchmarks.
  These are **editorial grouping suggestions**, not permission to assign an unsupported PRIMARY to a package or to invent source claims. Attach technical depth to supported source material, not news count.
- Produce an actual technical-preparation/readiness file for every substantial package, with: thesis and significance, 2–4 **concrete** technical mechanisms/architecture details from consumed sources where available, parameterized claim/source IDs, vendor vs independently reproduced benchmark column, evaluation methodology/denominator if known, uncertainty/negative boundaries, cross-article duplication control and Japanese reader relevance. If a package lacks evidence for genuine technical treatment, explicitly downgrade to a brief instead of repeating marketing.
- Proposed article-length/space plan must give justified relative word/paragraph and page-resource ranges, at least one meaningful comparative table in major technical groups (frontier, weights/availability, provenance), and **no arbitrarily small maximum page cap**. Do not invent PDF pagination or pad by importing HOLDs. Discuss headline-level prose density and figure/table sourcing. Final PDF has not been created.
- Distinguish Japanese technical terminology, natural Japanese over literal/over-kanji translated expressions, and reserve machine-readable editorial JSON for later translator/claim validation before TeX, per Special/Weekly prior quality lessons.

## 4. Critical inherited boundary and source guards

- `execution/nanobanana-legacy-negative-exclusion-r6.md` applies. Core `validate_architecture` **requires** Matrix `remaining_boundaries` to flow byte-exact into machine Architecture package `boundaries`. One historic boundary contains unsupported categorical `rollout post nonexistent`. Preserve its literal membership in the **machine trace array only**, labeled `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE` in a separate architecture trace exception. Never copy it into `title`, `purpose`, `must_cover_requirements`, reader outline, human-facing claim summary, Draft JSON, TeX or final PDF as a factual claim. The only admissible narrative is `not located among issuer pages checked on 2026-10-12`. If frozen Core auto-emits that inherited string as an endorsed claim in a mandatory human-reader surface, STOP and report the exact path instead of forging acceptance.
- Retain textGrain PDF-not-consumed caveat; blog-published results are vendor-measured and **not independently reproduced**. Keep Mistral 49B X versus 52B current docs source versions separate, Mistral/Reflection promised weights unshipped (unless separately pinned as distinct in-window event), unknown OpenRouter/StepFun pricing and model preview conditions out of articles, no automated promotion of 13 HOLD, no invented 09:00 Daily X.
- Anthropic Usage Policy and ELYZA pre-window are the two `INSPECT` nonselected: cannot be placed as PRIMARY/SUPPORTING in Core Architecture. May inform methods/context without becoming article placements. Grok ledger remains methods-only, not an article.
- All 10 recorded Completeness residual limitations are carried to Human-facing reviewer attention without exaggerating their impact. No substantial unsupported metric in reader-facing architecture.

## 5. Canonical Architecture Review and exact terminal stop

- Build Core-compatible canonical `sources/2026-W41/architecture-v2.json`, Core `architecture-review-summary-v2.json` and actual review attention/architecture coverage. Validate against exact accepted Selection/Matrix/Materiality/Completeness sources and real source-role boundaries with **unmodified** Core validators; no placeholder names, empty thesis, fake source consumption, or page-plan contradictions.
- Demonstrate: **20 selected candidates all placed; 5 PRIMARY exactly once; 15 SUPPORTING at least once; 13 HOLD/2 INSPECT/1 REJECT unplaced**; boundaries exact membership and proper role mapping; genuine proposed article titles and technical must-covers; `READY_FOR_ARCHITECTURE_REVIEW` if true. Human Architecture Gate must remain PENDING.
- Execute ordinary Core stage/checkpoint and transition `SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED` only on canonical validation PASS. Validate remote readback and checkpoint hashes; if stage fails, STOP with exact defect. Prepare full Sol/reader Architecture review dossier with per-package source↔claim links, details/limits, role/coverage, resource plan, ignored/held material counterfactuals and history.
- **STOP** at `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW_PENDING`. Do NOT approve/reject Human Gate, start Draft, generate PDF, change publication, Freeze or Release. Do not enter Work mode to circumvent this contract. No Human gate origin, SHA or decision may be fabricated. Sol will do an independent read-only Architecture audit before presenting to Human for approval.

## 6. Final report / fail-closed

Include exact starting and ending remote W41 HEAD + Trees, main/Core exact identities; commit parent chain, all changed paths, normal non-force push and readback; Core Matrix/Selection SHA and actual Selection checkpoint, accepted canonical Architecture/summary/attention SHA and real Architecture checkpoint, State/gate exact values, all 20 source↔candidate and exact boundary mapping counts, qualitative/quantitative technical depth plan, acknowledged first-party source gaps, Nano legacy exclusion evidence, which drafts remain unstarted, no Core/shared roots modified.

On legitimate failure, report precise error and last lawful state, leave safe changes only on the existing W41 branch and await Sol. No new branch, Core patch, replacement release or manual Human approval.
