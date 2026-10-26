# PROPOSED independent Sol r7 layout-and-meta re-audit request (read-only)

Status: `PROPOSED / NOT YET ACCEPTED / HUMAN_PDF_GATE_PENDING`.
Executor: separate independent Sol session (not Muse worker, not editorial
Sol). Read-only toward GitHub/Stage/Gates/Main/Frozen Core. External report
to Google Drive `GPT-Sol_Review` as `yyyyMMddHHmmss_SolReview.md` (never write
PASS into the repo).

## Audit subject (immutable once committed; verify before reading)

- Branch `weekly/2026-W43-v2-work`, worker commit AFTER `794824f68…`
  (one FF commit, paths restricted to `sources/2026-W43/execution/`
  — r7 namespace + handoff + session + index append; exact HEAD/Tree in
  `SOL_W43_CORE_FREE_PREVIEW_R7_HANDOFF.md`).
- New PDF `sources/2026-W43/execution/core-free-preview-r7/main.pdf`
  SHA256 `5d01f49677c25e156da350c023ca5374cb72759b93eba21f049ea86d8dd9f93e`,
  487514 B, 22 A4 pages. New TeX SHA256
  `9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0`.
- Fixed r6 subject for delta: HEAD `d8e21b8fe…`, TeX `7c052f05…`, PDF
  `113b179a…`. Correct historical r3 HEAD
  `3cdf2a01b810a972ecddfaa41c7dccded55c75f9` / Tree
  `17b0525fec79d5624a227f82bf7c5493dd1e5b73` (r6 manifest typos superseded by
  `historical-pin-correction-r7.md`; do NOT use the corrupted strings).

## What worker claims (challenge, don't trust)

1. **P1 layout**: segmented two-column restored (32 multicols segments, W42
   geometry); 20 full-width tables / 5 code / 3 figure boxes outside columns;
   bib two-column. Worker visual QA bounded (11/22 full-res + 22/22
   150dpi sheets + text layer). **Independently inspect EVERY r7 page** at
   full res; confirm two-column prose on story pages, full-width safety on
   dense panels, no blank body pages, flow order, p20 note absent, 5 recap
   paras, 36 bib entries, both proof marks separate.
2. **P1 meta**: 23-pair whitelist (`meta-change-ledger-r7.json`); 0 visible
   leaks claimed; core scientific qualifiers kept; proof layer separate +
   PDF metadata. Re-scan independently (TeX parse + PDF readback, all
   pages); verify no over-stripping of epistemic/cutoff disclosures.
3. **Semantic bridge**: r6 36/36 clean replayed here (witness
   `r6-baseline-replay-clean-r7witness.json`); r7 validator 18/18 clean +
   9/9 negatives (replayable via `portable-independent-replay-r7.md`).
   Re-run all replayable commands; add ≥1 NOVEL adversarial mutation (not
   one of the 9); confirm distinct fail codes. r6 38-negatives are NOT
   re-runnable (harness asserts r3 note) — treat as historical, state
   `CHECKER_REPLAY_NOT_RERUN` scope explicitly.
4. **Links/fonts**: 28 unique http / 0 malformed / 14 embedded subsets
   claimed from real bytes. Re-extract independently; click-sample bib URLs.
5. **Governance**: Architecture 31 versioned (r3.2 20/11 vs r2 18/13, no
   promotion — verify no approved-file change); 15 refs stay
   `CURATED_REVIEW_REQUIRED` (verify no upgrade language in print).

## Terminals (choose one on evidence)

`INDEPENDENT_W43_R7_PDF_PASS` (P0=P1=0, P2/limits explicit) /
`INDEPENDENT_W43_R7_SEMANTIC_PASS_VISUAL_BLOCKED` /
`INDEPENDENT_W43_R7_REQUEST_CHANGES` / `INDEPENDENT_W43_R7_INCONCLUSIVE`.

No Human approval, no native Draft/Validation/Publication completion,
no Freeze/Release/main merge. State stays `ARCHITECTURE_ESTABLISHED`,
Human PDF Gate PENDING, Core native Draft BLOCKED.
