# J-GAS 2026-W43 — Independent Sol audit REQUEST: r6 print delta + full-visible re-audit (PROPOSED, not a result)

Date: 2026-10-27 JST.
Status: `INDEPENDENT_SOL_READ_ONLY_AUDIT_REQUEST / R6_PRINT_READY_FOR_REAUDIT / HUMAN_PDF_GATE_PENDING`.
Repository: `eariver/japanese-generative-ai-survey`.
Audience: **separate independent Sol audit session** (NOT editorial Sol, NOT Muse Worker).

## 0. Immutable subjects (exact pins)

Audit the immutable request-parent commit recorded at commit time (this
request is committed AFTER its subject; verify exact HEAD/Tree before
analysis and never substitute current tip):

- Existing work branch: `weekly/2026-W43-v2-work`.
- **New r6 print subject**: `sources/2026-W43/execution/core-free-preview-r6/main.pdf`
  raw SHA-256 `113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320`,
  482659 bytes, 22 A4 pages, Git blob SHA
  `0342d2b5b5b38d9bd5cbb9488cbe98519a6c2af1`.
- **New r6 TeX**: `…/core-free-preview-r6/main.tex`, raw SHA-256
  `7c052f05227228332fecec469b3b90e1b8952d4c3ab44ea65f180cecd4dd662b`
  (90920 bytes), Git blob `38bbe745d21eb3558344bfe49b9a7c85dc060d24`.
  Projection (`63ad2617…`) and `preview.sty` (`46326113…`) are
  byte-identical to r3.
- Historical subjects (do NOT re-assert as current): r5 QA HEAD
  `fa1caaedb6f2b09a6d8e1f77a505d363ca6d0c31` / Tree
  `4576f190346da02c1937778e459eb0391fbf6430`; r3 print HEAD
  `3cdf2a01b810a972ecddfaa41c3dccded55c75f9` / Tree
  `17b0525fec79d5624a227f82bf7dccded55c75f9`, r3 PDF
  `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`,
  r3 TeX `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`.
- Protected: reviewed main HEAD
  `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree
  `a134dc36a407d08ab1de416324229b3955e0325a`; Frozen
  `production/survey-core-v2` HEAD
  `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree
  `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

**Read-only**: no GitHub commit/issue/PR, no file updates, no branch, no
Core execution, no State/Gate mutation. Write the external report to
Google Drive folder `GPT-Sol_Review` as `yyyyMMddHHmmss_SolReview.md`;
never write an audit PASS into the repo.

## 1. What r6 claims (challenge, do not trust)

- Phase A: 36-check full-visible join PASS + 38-case negatives PASS,
  portable (`--repo-root` / `--staged-dir`); segment map, runbook,
  13+2 curation, 18/13 architecture recount are committed beside the
  validator. Re-run both modes yourself; probe at least ONE novel
  adversarial mutant of your own (recap-adjacent or note-adjacent).
- Phase B: exactly ONE TeX-line deletion (production note after
  `\label{sec:recap}`); 5 recap paras byte-identical; lualatex x2
  (LuaHBTeX 1.24.0, TL2026), 22 pages, 0 errors, 0 overfull/underfull;
  22 PNGs + 3 contact sheets; worker all-page QA PASS; links/fonts
  extraction from real PDF bytes (44 annots, 36 http, 0 malformed).
- References stay curated (13+2); architecture 18/13 recount changes
  nothing (grounds for Sol, not a promotion).

## 2. Audit A — r6 print delta (must review the NEW binary)

- Recompute r6 PDF/TeX SHA-256 from actual bytes; confirm the diff is
  exactly the one-line deletion (`print-only-diff-r6.md`).
- Re-verify the five recap paras in the NEW PDF bytes and the ABSENCE
  of the production note; confirm no repagination damage (recap still
  p20, bibliography still p21–22, TOC numbers still correct).
- Do NOT reuse the prior r3 22-page visual result as if the r6 binary
  were identical: the bytes differ (`d0fa8b56…` vs `113b179a…`).

## 3. Audit B — full-visible re-audit (Phase A replay + novelty)

- Re-run the r6 clean + negatives from a read-only checkout or the
  staged-dir procedure; verify counts (36 / 38) and exit codes.
- Confirm each mandated negative fails for its asserted cause with
  hash-bound mutants, especially the exact
  `N-AUD-RECAP-SEMANTIC-REVERSAL` TeX-side replay and
  `N-PRINT-NOTE-LEAK`.
- State limits honestly: `PDF_VISUAL_AUDIT_BLOCKED` if binary access
  fails; never PASS a page you did not render.

## 4. Report

Deliver `yyyyMMddHHmmss_SolReview.md` with: exact r6 subject pins,
recomputed hashes, rerun evidence, novel mutant, P0/P1/P2 findings
(`W43-R6-AUD-xx`), and one explicit terminal:
`INDEPENDENT_W43_R6_PDF_PASS` (semantic + full visual, P0=P1=0),
`INDEPENDENT_W43_R6_SEMANTIC_PASS_VISUAL_BLOCKED`,
`INDEPENDENT_W43_R6_REQUEST_CHANGES`, or
`INDEPENDENT_W43_R6_INCONCLUSIVE`.
Stage stays `ARCHITECTURE_ESTABLISHED`; Human PDF Gate stays PENDING;
no Freeze/Release/merge. Report to editorial Sol for adjudication.
