# J-GAS W43 — Editorial Sol decision: one comprehensive independent audit, consolidated repair, PDF Preview

Date: 2026-10-26 JST.
Status: `HUMAN_EDITORIAL_WORKFLOW_DIRECTIVE / FULL_INDEPENDENT_AUDIT_FIRST / CONSOLIDATED_REPAIR / CORE_FREE_PDF_PREVIEW_TARGET / NO_RELEASE`.
Repository `eariver/japanese-generative-ai-survey`, existing branch `weekly/2026-W43-v2-work`.
Source: Human Owner explicitly asked: **「それであれば、再度網羅的な独立監査を実施して、問題点を洗い出してから修正して、まとめてPreviewまでもっていった方がいいと思います」**.

## Operational pivot

Prior r3.2.1 microfix instruction `sources/2026-W43/execution/instructions/sol-w43-r321-small-reader-provenance-cleanup-20261026.md` was committed at `7d8fb22900fb1b6c3e2b10f5ee6f77fb2c8302df` but **NOT DISPATCHED / NOT EXECUTED**. It is henceforth **SUPERSEDED_AS_SOLE_EXECUTION_AUTHORITY**; keep untouched as historical context. Its 3 identified concerns (npm unscoped wrong source, reader operational metadata, keyframes false contradiction certainty) become audit inputs only, not a new Muse correction assignment now. Do NOT spend another revision cycle applying these three before the comprehensive independent review.

**Audit's immutable subject** is Muse's last completed r3.2 edition-local manuscript commit `efac8324ff7a9f35ad34be391ba2ea328cfc1722`, Git root Tree `61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43` (direct parent of unused r3.2.1 instruction). Latest work branch HEAD is only a locator/contract transport and **not** the audit target.

Current facts confirmed by six-way read-only guard:
- Work HEAD `7d8fb22900fb1b6c3e2b10f5ee6f77fb2c8302df` / Tree `d089b75618ccbbf743199c5b835036b1d82a0e6c`.
- main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Frozen Core branch `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Canonical `production-state.json` remains `ARCHITECTURE_ESTABLISHED`, human Architecture Review `approved`, Human Publication Preview `pending`, machine Draft checkpoint `pending`; frozen native Draft runner blocked at pre-existing `Screening package basis drift: state_sha256`.
- Human Architecture r6 is explicitly approved; final **「今週の総括」** is mandatory; no architecture reopen, no Core repair.

## Binding ordered workflow, no premature "PASS"

1. A **different independent Sol session** performs a read-only **complete** manuscript/technical/primary-source/figure/table/reader-quality audit at the frozen r3.2 Git commit. Audit contract `sources/2026-W43/execution/audits/independent-sol-w43-r32-full-manuscript-evidence-publication-audit-request-20261026.md`. Existing Muse QA / Sol spotchecks are advisory, NOT presumptive audit passes. Report all P0/P1/P2, conditions and risks; independent output `PASS | PASS_WITH_LIMITATIONS | REQUEST_CHANGES` for editorial content; separately `NATIVE_DRAFT_VALIDATION=BLOCKED`. No GitHub writes.
2. Editorial Sol retrieves the complete independent report and performs one **comprehensive issue adjudication**, merging prior r3.1 independent 4 findings, r3.2 known regressions and any new source/content issues, de-duplicating by root cause. Establish issue-to-block-to-source matrix, actionable severity and remediation, publication-blocking/allowable unresolved. Only then create **ONE consolidated Muse repair contract** with an exact 6-way guarded starting SHA/Tree. Muse works on existing branch only, new edition-local r3.3 (version number can adapt to actual next state) and preserves all r1–r3.2. No single-item repair cycles.
3. Editorial Sol performs integrated result review. If no uncorrected P0/P1 and source/claim/page requirements satisfied (P2 and inherent PARTIAL properly qualified), obtain a **one-shot independent regression/closure check** of repaired differences and highest-risk unchanged claims, rather than automatically commissioning another full audit. If still P0/P1 factual or source fabrication, STOP; do not roll blindly into Preview.
4. **Noncanonical Core-free production**: from accepted revised reader Markdown and complete row-level citation ledger, use a separate, edition-local rendering/LaTeX/PDF procedure that DOES NOT patch, wrap, bypass-in-place, or claim success for Frozen Core native Draft validator. Separate auditable source and render build log with exact SHA of manuscript, fonts/licences as installed, correct citations, 20+ tables/figures as typeset, Japanese typography, mathematical notations, meaningful technical depth and prepublication boundary validation. Generate a clearly designated **W43 PREPUBLICATION PDF preview** in edition-local staging (not released `surveys/**/main.pdf`) and checksums plus page-wise visual QA. No page padding; 35 pp package body/38 pp target/44 pp editorial maximum are estimates and must be checked against real content, not treated as success proxies.
5. Editorial Sol presents the actual PDF preview to Human Owner for visual/content decision; status **`CORE_FREE_PREPUBLICATION_PREVIEW / NONCANONICAL / HUMAN_REVIEW_PENDING`**. The user's request to reach Preview is **NOT authorization to approve the Preview, mark Human Publication Preview Gate `approved`, Freeze/Release or merge main**. Formal native Stage and Human gate remain truthful `pending` until a separately reviewed governance decision; document any irreconcilable publication limitations honestly.

## Hard boundaries

Frozen Core v2 unchanged: no `scripts/`, `schemas/`, `config/`, canonical State/Checkpoints/architecture/selection/evidence, accepted Human approvals or frozen production branch mutation. No fresh fallback/review/repair branch, no force/rebase/reset/rewrite. Each GitHub write: before writing read-only exact six-way work/main/core HEAD+tree; mismatch stop. New files on existing work branch with normal commits + nonforce FF and remote readback. Do not manufacture native QA receipts, selection changes or machine `DRAFT_COMPLETE`. No unapproved publication. The **separate independent audit is not performed by editorial Sol itself**; preparing this contract does not constitute independent audit completion.

Preview technical contract/exit checks are in `sources/2026-W43/execution/plans/sol-w43-post-full-audit-batched-repair-to-noncanonical-pdf-preview-20261026.md`. 
