# J-GAS W43 — Sol candidate-readiness review and General audit hash transcription disposition

Date: 2026-10-28 JST.
Status: `SOL_W43_CANDIDATE_READY_FOR_HUMAN_EXACT_PDF_PREVIEW / MINOR_GENERAL_REPORT_HASH_TRANSCRIPTION_EXCEPTION`.
Authority: editorial Sol's GitHub read-back, **NOT** a new independent PDF binary audit or Human approval.

## Scope and exact immutable PDF

Reviewed W43 branch HEAD at this evaluation:
`f766225caa2d94f794fac79d788c2b9a1a7f6dda`, root Tree `3d6461b9e746a8c2408e7ac4dfaf8c6fd0199dfc`.

Canonical PDF: `surveys/weekly/2026-W43/main.pdf`, expected and Candidate-bound SHA-256:
`b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165`,
486967 bytes, 22 A4 pages.

Candidate: `sources/2026-W43/publication/v2/publication-candidate-v2.json`,
`READY_FOR_PUBLICATION_PREVIEW`, own `candidate_sha256=b006f6dff81e5283147b76fb97fcf96409911b536917329a6bc5e532621d5c81`,
Reader Manuscript whole-file SHA `c24e0fe6be1a82112411035999311c2753228f0fa54366f116d70bc677f08032`,
TeX SHA `3fa6ca3b4c610cd12fecd3e6ce449e0d9cffd9e7edc67efb1b85f5bd0e758784`.

Human-approved earlier noncanonical r8 PDF SHA:
`abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`,
487351 bytes / 22 A4 pages. This correct 64-char value was pinned by the older independent GPT audit, the immutable r8 subject and integrated execution contract.

## Checks personally read by editorial Sol

- Remote existing W43 branch current HEAD/Tree fetched and matched; main protected HEAD/Tree unchanged `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`; Frozen Core v2 HEAD/Tree unchanged `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Current `sources/2026-W43/production-state.json`: `RELEASE_CANDIDATE`, `next_action=PUBLICATION_PREVIEW`, `terminal_reason=HUMAN_GATE_REACHED`, architecture_review approved, publication_preview pending, exception_gate inactive; draft and validation passed, Preview/Freeze/Release pending.
- Three trusted operator receipts inspected at `execution/bridge-runs/muse-w43-{draft-advance,validate,release}-20261028/receipt.json`: all `status=PASS` and State transitions ARCHITECTURE_ESTABLISHED→DRAFT_COMPLETE→VALIDATED_DRAFT→RELEASE_CANDIDATE.
- `publication-candidate-v2.json` references exact Reader Manifest, TeX, PDF, quality bundle, semantic/visual records and `READY_FOR_PUBLICATION_PREVIEW`.
- `execution/audits/general-w43-r8-to-candidate-20261028.md` states `GENERAL_W43_EQUIVALENCE_PASS`, no P0/P1, 6 bounded P2; documents direct r8-vs-candidate TeX four-hunk diff, all-page fresh rendering and fixed A/B/C caveats, 20 tables, 3 diagrams, 5 code items, 5-paragraph recap, 36 bibkeys, 75 URI links/28 targets. This is the **General report's** execution evidence, not a repeated Sol independent binary test.
- Handoff uses `079e07ce...` for Reader Manifest's internal `manifest_sha256`, whereas Candidate refers to Reader Manifest whole-file SHA `c24e0fe6...`: independently read internal `manifest_sha256=079e07ce53f14fe50983ca1e1d97ab391a217431e733321bfda10ca94c2fb882`. These are distinct fields, NOT a mismatch.

## General audit report editorial correction note (nonblocking, preserve original report)

In the **General audit report** §1 hash table, old r8 PDF "SHA256 measured" is printed as:
`abd5b99bd051703dbdc9420c19965ed039585c0436090ae6e65c6d17dc72`
which is only **60 hex characters**, not a valid SHA-256 digest, and does NOT equal the 64-character fixed r8 PDF SHA:
`abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`.

Disposition: classify this as **P2 audit-report transcription/provenance notation defect**; General's literal claim `measured SHA / YES` for that one row is not independently substantiated by that malformed printed string. No change to r8 or canonical PDF is justified from the discrepancy. All other General comparisons (TeX exact diff, page text, canonical candidate SHA bindings and render evidence) are separately described in the report. Do NOT silently amend or rewrite General's verbatim report. If needed for a downstream independent machine proof, the General auditor should reissue a corrected additive observation with real `sha256sum` output. This Sol note does **not** pretend to have run that command. The previous independent GPT audit already established fixed r8's full correct hash.

## Editorial disposition / human gate

Accept the **candidate's technical readiness for a Human exact-PDF review invitation**, conditional on the user actually viewing the canonical PDF. This is NOT a Human publication approval. The final reviewed commit for any formal approval must be a current, durable work-branch commit containing the unchanged exact Candidate, State, Gate inputs and PDF. This document commit changes no Candidate/PDF/State/Gate bytes; it must not be mistaken for a new artifact generation.

Do not run `RECORD_PUBLICATION_PREVIEW_APPROVAL` before explicit Human GO on the **canonical** PDF SHA `b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165`. Do not Freeze, merge, tag or Release before it. If PDF/Candidate/source SHA changes before approval, re-present the exact newly bound PDF to Human and re-audit relevant differences.
