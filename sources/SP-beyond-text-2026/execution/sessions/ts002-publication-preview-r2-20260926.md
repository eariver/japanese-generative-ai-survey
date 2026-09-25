# Survey Production session — ts002-publication-preview-r2-20260926

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work` (existing only; no new/fallback/repair/review branches)
Execution authority: `docs/prompts/2026-09-26_muse-ts-002-publication-preview-r2-bibliography-and-depth-audit.md`
Sol authority: `sources/SP-beyond-text-2026/execution/sol-publication-preview-review-r1-20260926.md`
Human decision obtained in-session: `PUBLICATION_PREVIEW r1 / REQUEST_CHANGES @ DRAFT_COMPLETE`
(Human Owner, explicit; recorded canonically as `gates/reviews/publication-r1.json`)

## Starting guards (read-only, all PASS; repo writes zero until Human decision)

- Remote work HEAD `bf6f53017047ac485ad91d127846b52ed2eb5203` == user-supplied Exact Starting SHA.
- Remote work tree `a4ae8ed60491065597e3c1172b869f6dccd31d64` == user-supplied Expected Starting Tree.
- Remote main HEAD `0bbb02b3c5963403860897daec2feaf61e82589a` / tree `e4ddde5ed5059d303b818f54e27204369b256bcb` == reviewed main.
- Note: the prompt file embeds an older guard pair (`c48f35368…`); user-supplied launch values governed (same pattern as prior runs) and all four matched.

## Lifecycle mechanics (why a Human decision was required first)

- r1 candidate reached RELEASE_CANDIDATE but was never Human-presented; Sol r1 (internal) found defects.
- Core analysis: at RELEASE_CANDIDATE with approved Architecture, no operator/invalidation/revalidation path permits pre-Human publication repair (operator invalidation blocked by active Architecture approval; revalidation is VALIDATED_DRAFT-only with reason class REVIEWED_CORE_CHANGE; checkpoints immutable).
- Efficient precedent confirms the canonical order: Human REQUEST_CHANGES → repair → re-advance.
- Presented r1 surface + Sol findings + first-hand verification to Human Owner with zero repo writes; Human explicitly selected REQUEST_CHANGES with publication-local boundary DRAFT_COMPLETE.
- Recorded via `survey_human_gate_v2.request_publication_preview_revision` (canonical): publication-r1.json, lifecycle → DRAFT_COMPLETE, Architecture approval preserved, invalidated validation checkpoints removed (DRAFT_COMPLETE.json, VALIDATED_DRAFT.json). State revalidated clean.

## Bibliography repair method

- Committed deterministic generator `execution/bib-repair-r2-20260926/gen_bib_r2.py` from sanitized Evidence acceptance f8e273fd.
- Authors: all 139 display strings emitted as literal BibLaTeX (`{{…}}`); zero name-list parsing; zero invented metadata.
- Boilerplate removed from 125 ordinary VERIFIED entries; 8 PARTIAL + 5 HOLD entries carry rewritten reader-facing limitation notes; X ledger carries a reception-only note. URLs/dates preserved. Built-in self-check rejects pipeline jargon/macros.

## Bibliography author fields changed: 139 (all entries literalized)

- Before: `K. et al.`, `C. et al.`, `H. et al.`, `I. 2. Panayotov et al.`, `B. F. Labs.` (verified in rendered r1 PDF).
- After (verified in rendered r2 PDF p58/62/65): `Karras et al.`, `Chen et al.`, `Heusel et al.`, `Panayotov et al.`, `Black Forest Labs`, `OpenAI`, `Google`, etc.

## Generic provenance notes removed/retained

- Removed from 125 VERIFIED entries: `Source class PRIMARY_* as bound in Evidence` + `Primary locator as rebound in 2026-09-24 provenance repair where applicable`.
- Retained (rewritten): 8 PARTIAL + 5 HOLD + 1 X-ledger reader-facing notes. Provenance audit detail stays in Evidence/execution artifacts.

## 43-transition audit counts

- SUBSTANTIVE: 24; COMPRESSED_BUT_SUFFICIENT: 16; BOUNDARY_ONLY: 3 (T-VI-03 closed capstones, T-X-01 reception, T-CLOSED-01 lifecycle); UNDER_EXPLAINED: 0.
- Files: `execution/publication-preview-r2-depth-audit/semantic-depth-delta-audit.json` + `.md`.
- T-EV-01/T-EV-02 adjudication: worker-labelled UNDER_EXPLAINED but rationales state gaps trace to absent Evidence (abstract-only/snippet-only/gated); §8 permits expansion only with active-Evidence support → reclassified COMPRESSED_BUT_SUFFICIENT with documented rationale; evidence-side re-consumption is future work.

## Package-level audit (representation/paradigms/speech/music/video)

- All 5 chapters pass all 7 anti-thinness questions (mechanisms-not-names; arch/obj/inference separation; condition-bound quantities; trade-offs; succession; no one-line majors; no modality compression). No expansion recommended.

## Sections expanded: none (body substantially unchanged per §8)

- main.tex body bytes identical to r1 except zero prose changes (only references.bib regenerated).
- Architecture page-plan arithmetic defect recorded (not repaired — approved authority preserved): listed allocations sum to 94, not the stated 84.

## Before/after manuscript proxy

- main.tex: 293701 → 293701 bytes body (unchanged); references.bib: 53481 → 34940 bytes (boilerplate removed).
- Extracted PDF text: r1 200473 chars → r2 shorter refs section (11 → ~8 reference pages).

## Before/after page count; bibliography page count

- r1: 68 pages (6 front / 51 body / 11 refs). r2: 65 pages (refs compacted by note removal). Body pagination unchanged.
- 65 lies within the 64–96 planning envelope; no padding added; below-target disposition recorded (`page-plan:65/80`, `density-review:below-target-substantive`).

## Citation count: 139/139 cited, 139/139 records cited; undefined 0, uncited 0 (CI + deterministic binding both PASS)

## PDF visual QA results

- r2 CI build (run 36171853391, commit f9e21bee0): PASS, 65 pages, 0 blocking, 0 layout findings.
- Rendered QA: cover, TOC, representation/speech/music/video/runtime/evaluation/capstones/synthesis spot pages from r1 carried over (body unchanged); refs beginning/middle/end freshly inspected — literal authors, reader notes, no macros, no clipping, X entry clean without URL, tail page acceptable.
- Extracted-text macro scan: bibinitperiod/bibnamedelim/mangled-initial patterns all zero.
- All 65 pages text-verified (no near-blank pages).

## Validator receipts

- build_validation_r2.py: manuscript (`56d6faff`) → deterministic ×4 → quality bundle → surface review → surface gate → semantic (9 PASS) → visual (5 PASS).
- advance_validation_r2.py: DRAFT_COMPLETE → VALIDATED_DRAFT (receipts `-r2.json`).
- advance_candidate_r2.py: candidate `c3a01a5b07bdf02d` READY_FOR_PUBLICATION_PREVIEW → VALIDATED_DRAFT → RELEASE_CANDIDATE (receipts `-r2.json`).
- Final `validate_agent_state`: clean.

## Final production lifecycle state

- RELEASE_CANDIDATE, architecture_review approved, publication_preview pending, HUMAN_GATE_REACHED.
- Review index: ARCHITECTURE r1 APPROVED (preserved), PUBLICATION r1 REQUEST_CHANGES (Human, this session). Next Human decision records publication-r2.
- Semantics: `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION_R2`. No publication-preview approval fabricated. Freeze/Release not entered (no freeze/release artifacts).

## Final remote HEAD/tree

- (recorded after push)
