# W42 Muse r7 — Evidence precision correction, conditional Core acceptance, Materiality/Selection proposals

Status: `EXECUTION_AUTHORITY / FROZEN_CORE / BOUNDED_AT_SOL_MATERIALITY_SELECTION_REVIEW`
Date: 2026-10-17 JST
Repo: `eariver/japanese-generative-ai-survey`
Existing branch: `weekly/2026-W42-v2-work`.
Exact start SHA/Tree supplied by Sol at invocation; mandatory read-only preflight. Reviewed `main` SHA `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`. Frozen `production/survey-core-v2` SHA `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch → **ZERO WRITES** and report expected/actual. Never create branches, modify shared Core, reset/rebase/force, or change Human Gates.

Read first:
- `sources/2026-W42/execution/reviews/sol-w42-evidence-authority-review-r6-CONDITIONAL-PASS-20261017.md` (mandatory E42-R6-A to E, plus explicit scope).
- `sources/2026-W42/execution/reviews/sol-w42-evidence-authority-review-r5-REQUEST_CHANGES-20261017.md`.
- `sources/2026-W42/execution/evidence-r6/` (49 local proposed cards, views, authority matrix, depth audit).
- Source bundles `sources/2026-W42/collectors/evidence/runs/` r1/r2/r4/r5/r6, canonical 50 Discovery+Screening, source intake manifest, authoritative production-state/checkpoints, frozen Core v2 Evidence/Materiality/Completeness/Selection schemas and executable contracts; W41 good stage implementation precedent.
- `docs/survey-production-core-v2-sol-luna-review-governance.md` §4.2–4.4; project publication profile and Core QA rules.

## Unit A — mandatory Evidence semantic/provenance precision cleanup

Work from r6 deeper research; do NOT reset to r4/r5 shallow 68-claim results.

1. Verify all 151 candidate-local claims against their actual source/bundle notes. Correct each of the 20 shorthand/non-HTTP sources to exact public URL, or exact repository provenance path + hash and defensible source type, or remove ungrounded claim. No fabricated original-X read. `analyst-note` is editorial analysis, NOT VENDOR/primary authority. External reference `https://3druck.com SMLIB article...` is not a valid exact article URL; verify and replace/qualify.
2. Correct self-contradictory limitations (Wonder research blog read, Nemotron report extracted, FLUX license full text, wet-lab three PDFs extracted, MiniCPM license tag vs unverified file, plus comprehensive sweep across all 49 cards).
3. Revisit all 13 `AUTHORITY_CAPTURED_BUT_UNCONSUMED` at **source granularity**. A body whose bounded claims were actually incorporated is CONSUMED-scoped-to-those-claims even if another document is missing. Log source locator, artifact completeness, actual retrieval outcome, verification target status. For not-found paper use bounded negative evidence. Do not misclassify unread links as present-but-unconsumed.
4. Ensure vendor reports, independent critical reviews, first-party license terms, X observations and editorial synthesis have distinct kinds and appropriately grounded methodology/denominators. OpenMDW-1.1 OSI approval status must be independently demonstrated before asserting approved. Keep read-vs-unread licence and PDF boundaries.
5. Regenerate **substantive edition views** from Evidence, not `AUTHORITY_CONSUMED + N claims` placeholder text. Give each material candidate grounded importance, method novelty, tradeoff, limitations, chronology and what reader would learn. Separate HOLD/CONTEXT rationale. Avoid over-generalized homogeneous Japanese text.

## Unit B — Core Evidence stage conditional acceptance

Build genuinely **Core-conformant** Evidence artifacts from corrected 49 technical candidate records, plus an explicit accepted/non-editorial provenance rule for the 50th X-binding ledger. Check how Core handles screening KEEP binder; never silently drop a canonical record or promote ledger as release. Use actual Core schemas, basis file hashes, input/output cardinalities and deterministic validators; do not merely rename local PROPOSED files or copy only task-count metadata.

If all required Core acceptance and stage guards PASS with traceable claim authorities, complete appropriate Evidence acceptance/advance to the next lifecycle state; record exact checkpoints and acceptance hashes. If any mandatory guard fails, **stop without waiver**, preserve existing accepted Discovery+Screening, return concrete error and proposed remediation. No hardcoded acceptance/waived human editorial decisions.

## Unit C — Materiality, Completeness, Selection *proposals* for Sol review

Only after lawful Evidence acceptance:
- Produce materiality and completeness source-backed per-candidate assessments, including dates/cutoffs, multi-source density, reliability, technical novelty, and missing substantial threads (scientific papers, open-weight/license/hardware, security/coding, JP/audio/video lanes).
- Inspect *selected and unselected* high-signal primary-body depth, especially 28 genuine Screening KEEP plus 16 INSPECT. Distinguish articles vs sidebars vs background vs HOLD; do not treat one X ledger as editorial candidate. Deduplicate families when appropriate while preserving different technical contributions. Explicit treatment of Grok 18→7 X-ledger.
- Prepare Selection alternatives and proposed editorial thesis with enough scope for a non-sparse weekly issue. For each selected item provide technical rationale and expected discussion length; for each high-signal unselected item explain why NOT selected after examining substantive sources. Produce an alternative architecture package sketch only as a **non-binding suggestion**, without materializing/accepting Architecture.
- Run deterministic tests/validation permitted at this stage; if Core allows Materiality/Completeness acceptance mechanically, record exactly what was accepted, but Sol editorial materiality and selection decisions remain mandatory before Architecture.

## Stop / deliverables

Normal commit, non-force push, same existing branch; no shared Core edits, no fabricated tokens, no date-inexact news promotions.

Stop at **`SOL_MATERIALITY_SELECTION_REVIEW_READY`** (or earlier real Core blocker) with exact start/final HEAD/Tree; accepted lifecycle and checkpoint states; 49 evidence cards and 50th binder disposition; correction ledger addressing five r6 findings; Core Evidence acceptance result; selected/unselected candidate matrix, evaluation of high-signal omissions, research/completeness and page-allocation proposals. Never advance Architecture, Draft, TeX/PDF, Human Architecture Gate, Preview, Freeze/Release.

The next Sol review owns final materiality/Selection semantics; do not turn proposed executor selections into authoritative editorial decisions by machine validation alone.
