# W43 — Muse/independent Sol bounded edition-local editorial Draft review (Frozen Core bypass)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / CORE_NATIVE_DRAFT_UNVALIDATED / HUMAN_ARCHITECTURE_APPROVED`
Date: 2026-10-25 JST.
Repository: `eariver/japanese-generative-ai-survey`.
Existing branch: `weekly/2026-W43-v2-work`.
**Exact starting HEAD and Tree are supplied by the Sol dispatch based on the new committed instruction.** No stale inferred local SHA. Before any repo writes, read-only remote six-way guard HEAD+Root Tree for work, main, Frozen Core v2; mismatch STOP_ZERO_WRITES. If local checkout is clean and strictly fast-forward-behind expected remote, permit `git fetch` followed only by `git merge --ff-only` after remote guard; never reset/rebase/force/new branch or merge commit.

Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core `production/survey-core-v2`: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## Inputs (read in order)

1. Human-approved r6 Architecture authority `sources/2026-W43/architecture-v2.json`, `architecture-review-summary-v2.json`, `architecture-review-attention-v2.json`, `candidate-matrix-v2.json`, `candidate-selection-v2.json`; State `ARCHITECTURE_ESTABLISHED` and actual `gates/architecture-approval.json` `APPROVED`. Selection 19/1/12 and 8 packages/31 requirements; source limits remain.
2. Original Human Owner requirement in `sources/2026-W43/execution/governance/human-w43-r6-architecture-approved-with-closing-weekly-summary-20261025.md` and subsequent **explicit** Owner instruction "Core v2の修復は禁止なのでBypassしてください".
3. `sources/2026-W43/execution/defects/w43-drafting-screening-basis-drift-20261025.md` and original Muse JSON `sources/2026-W43/execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json` (SHA256 `d1cb5277e9243d0feb04f585be8d316e0f6137b2ebd5c9d4763d68760690c409`; **not canonical**). Critical its `runner.generated_at` is not an independently confirmed execution timestamp.
4. Binding **Sol workaround authorization** `sources/2026-W43/execution/governance/sol-w43-core-free-editorial-bypass-authorization-20261025.md`.
5. Editorial preview `sources/2026-W43/execution/editorial-bypass/w43-r1-readable-reader-preview-UNVALIDATED-20261025.md`, standalone conclusion `w43-closing-weekly-summary-r1-UNVALIDATED-20261025.md`, 113-block `w43-r1-block-index-UNVALIDATED-20261025.json`. This is a literal prose transfer from the preserved input, with standalone added closing conclusion, **NOT a native Core Draft Result**.
6. Edition-local Evidence Cards, Evidence Views, Discovery originals, supplement/source crosswalk, Profile Completeness and Materiality/selected-risk ledger, source fetches where legally available. Do not assume `discovery_ids` are full original source URLs.

## Mission

**Do not rerun, patch, monkey-patch, wrap, forge, or partially satisfy the frozen native Draft runner.** Its `Screening package basis drift: state_sha256` failure is recorded and intentionally out of the editorial path. Human approves continuation in noncanonical preview only, not blanket waiver of later publication gates.

Make the human-readable **P1–P8 + closing「今週の総括」** a defensible, detailed, fact-sourced Japanese editorial draft in a NEW edition-local revision location, e.g. `sources/2026-W43/execution/editorial-bypass/w43-r2-reader-preview-UNVALIDATED-20261025.md` with fresh `execution/editorial-bypass/w43-r2-citation-confidence-ledger.json` and `w43-r2-editorial-qa.md`. Do not overwrite r1 or the original input. Keep full paragraphs rather than losing the useful draft. Improve clarity where unsupported, unnatural kanji vocabulary, inconsistent model names, unit/denominator, first-party attribution, license, availability and event clocks; expand genuinely thin explanations where accepted Evidence supports it, no filler or invented new sources.

### Per-claim audit / requirements

- Trace all **62 existing PARAGRAPH** blocks, **15 TABLE** raw text blocks, **8 NOTE** blocks and the new final recap to exact best-supported original source and relevant `evidence_task_id`/Evidence claim pointers; record original URL, checked publication timestamp/UTC vs day-only, source tier `FIRST_PARTY / THIRD_PARTY_ORIGINAL / DERIVED_ONLY / UNAVAILABLE`, `VERIFIED_DIRECT / SOURCE_REPORTED / LIMITED / UNRESOLVED / OUT_OF_WINDOW`, and citation-ready key. Absent source -> mark `SOURCE_NOT_VERIFIED`; never invent URL or promote artifact.
- Check the 31 Architecture must-cover requirements mapped through 8 packages and 19 selected candidate placements; no unselected candidate turned into a lead article. Preserve all 5 LIMITED, 68 Attention and human Gate. Review P1/P2 mechanistic depth, P5 conflicting Voxtral sources, P6 first-party rendered-only Patch, P7 evaluation sample distinctions, P8 per-request fees; validate FLUX formulas 25.37x/22.31x/95.52%, GH/npm timestamps and cautious CVE language.
- All big claims with math, speed, Elo, benchmark, weights/license, GA release clock and pricing must have explicit conditional source references; no independent benchmark claim without an actually distinct independent original.
- The source input is about **22,185 text characters** across 8 packages; the current draft may be thin for the 35-page body estimate. Perform **substantive depth review** rather than assuming 113 blocks assures 37pp. Deepen genuinely supported mechanism/evaluation/comparison; do not pad to reach a target. 15 original TABLE blocks contain delimiter text, not publisher-ready formatted tables; normalize for readability only after ensuring column meaning, otherwise mark `TABLE_UNRESOLVED`.
- Inspect the closing recap for accuracy with P1–P8 final revised prose; keep title exactly `今週の総括`, after P8 but before bibliography, with 4–6 coherent substantive paragraphs and clear limitations. This section is editorial end matter, **not P9** or a Core Draft Package. If unsupported summary assertion, revise or mark pending.
- Generate concise reviewer navigation and issue list prioritized P0/P1/P2 by factual impact, cite precise block IDs and actual source links; explicitly separate hard errors vs review limitations. No new external factual assertions without verification.
- Do not create fake native Draft Packages/Results, Synthesis, official QA receipts, machine `DRAFT_COMPLETE`, `ADVANCE_STAGE` request, or Human publication approval. Production State stays `ARCHITECTURE_ESTABLISHED`, draft checkpoint pending and Architecture Human Gate remains approved. No TeX/PDF in this phase. Document that any future official publication/Release needs separately authorized, truthfully labeled path because Core Draft Stage remains blocked.

## Stop and report

Normal commits/nonforce pushes on original existing branch only, then remote read-back. Deliver the new edition-local revised reader preview and exact key/hash, citation-confidence ledger, evidence/claim coverage counters, 31/19 coverage matrix, substantive page-depth assessment, full 「今週の総括」 excerpt and placement, recorded residual risks, no native State changes, final remote HEAD/Root Tree.
Stop `SOL_W43_CORE_FREE_EDITORIAL_DRAFT_AUDIT_READY`.

If major P1 factual/authority issue discovered, stop `SOL_W43_CORE_FREE_EDITORIAL_DRAFT_REQUEST_CHANGES` with detailed evidence. If repo Core/source/Architecture edits appear necessary, STOP, report alternatives; **Core repair is explicitly forbidden**.