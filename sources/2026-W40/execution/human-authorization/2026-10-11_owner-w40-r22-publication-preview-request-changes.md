# W40 r22 — Human Publication Preview REQUEST_CHANGES authorization (revision 2)

Status: `HUMAN_OWNER_EXPLICIT_REQUEST_CHANGES / CORE_V2_FROZEN / BOUNDED_R23_REWRITE_AUTHORIZED`
Human decision: **2026-10-11 JST**, precise in-chat timestamp not asserted.
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W40-v2-work`
Owner-reviewed r22 candidate content commit: `ae22a5837fe453b177a3e72dfe948b1b69328b39`
Existing branch at decision: `ee56893d23c726477212f01c2941c344200d8e86`, Tree `1f55be28b774caf39ee28fb691e945409c60678f`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, Tree `fe3f07c653f255f67087b4b46d006f8943df7115`

## Human decision (faithful transcription of the Owner's written instruction)

The Owner authorized a single bounded revision round against the r22 Publication Preview, with the following verdict and bounding condition (original wording preserved):

> OKですが、毎回大きく手戻りを発生させると、TS-003のようにいつまでも編纂が終わらなくなるので、独立監査の内容を丸ごと鵜呑みにするのではなく限界を規定して作業してください。

This is an **explicit Human Owner PUBLICATION_PREVIEW `REQUEST_CHANGES` (expected revision 2)** for the existing r22 Publication Candidate. The independent audit findings are **candidates for correction, not automatic obligations for every item**. The r22 base shall be completed in principle in **one** bounded rewrite round; no new research/design cycle is started. This markdown is source evidence for the official Human Gate operation, not a forged official Gate record. The exact time of the in-chat message is unknown; use the real execution UTC timestamp when invoking the Core CLI.

## Scope authorized

1. Mandatory P0 corrections (must fix before publication): Gemini 4 Argon discount separation; AgentPerf 14-config mistranslation; ELYZA table/denominator overstatements (complement only from adopted sources, invent nothing); ContextLM Eq.3/Eq.5/Eq.6 within r15/r16 verified scope; reader-facing editorial leakage removal.
2. Bounded P1 improvements only where already adopted Evidence/technical prep supports them. No full rewrite directive; keep existing explanations that already convey technical meaning accurately.
3. Explicit scope ceiling: no Discovery/Evidence/Selection/Architecture rerun, no new candidates/HOLD promotions, no Core v2/shared/config/schema/workflow/main changes, no exhaustive benchmark reinvestigation, no padding, no forced SUPPORTING expansion, no taste-only rewrites, no new branches/force/history rewrite, no automatic r24 cycle.
4. Stopping boundary: fresh `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED` with new Candidate/PDF, Architecture APPROVED, recorded Preview r2 REQUEST_CHANGES, new Preview pending/null. No Preview approval, Freeze, or Release.

## Audit basis

- Sol focused review: `sources/2026-W40/execution/reviews/sol-w40-r22-focused-publication-editorial-audit-20261011.md` (BOUNDED_REVISION_REQUIRED, R22-F01..F07).
- Prior Sol/independent r21 audits remain historical context, not automatic obligations.

Execution: Muse must use unchanged Core `scripts/survey_human_gate_v2.py request-publication-preview-revision` with `regeneration_boundary=ARCHITECTURE_ESTABLISHED` (preserves Architecture approval) and verify output.
