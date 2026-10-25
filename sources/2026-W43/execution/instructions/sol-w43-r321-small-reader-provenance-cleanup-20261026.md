# W43 Muse r3.2.1 — tiny Core-free source locator and reader hygiene repair

Status: `SOLE_MUSE_R321_EXECUTION_CONTRACT / THREE_MICROFIXES / DO_NOT_REOPEN_ARCHITECTURE / CORE_V2_FROZEN / NO_NATIVE_DRAFT_STAGE`
Date: 2026-10-26 JST.
Repository `eariver/japanese-generative-ai-survey`; existing branch ONLY `weekly/2026-W43-v2-work`.
**Exact work-branch start SHA and root tree must be provided separately by editorial Sol AFTER this file is committed.**
Reviewed main HEAD/tree fixed `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen `production/survey-core-v2` HEAD/tree fixed `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## 0. Mandatory guard and local FF sync

Read-only verify exact REMOTE work/main/frozen HEAD+Root Tree (6/6) against Sol dispatch BEFORE any repo writes. Mismatch = STOP_ZERO_WRITES with expected/actual. Clean local older commit that is an ancestor of fixed remote may be fetch+fast-forward-only after guard; dirty/diverged/unknown local STOP. Only the existing branch, no new branch/fallback/review branches, reset, rebase, force or merge commits. Original r1/r2/r3/r3.1/r3.2 must remain unmodified.

## 1. Fixed source and scope

Read binding Sol verdict `sources/2026-W43/execution/reviews/sol-w43-r32-targeted-spotcheck-and-r321-cleanup-20261026.md` R32-SOL-01/02/03, independent report `20261026005634_SolReview.md` if actually available (else disclosed limitation), prior original four-item contract and Muse r3.2 QA/handoff.
r3.2 fixed historic subject `efac8324ff7a9f35ad34be391ba2ea328cfc1722`, root Tree `61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43`.
Read `sources/2026-W43/execution/editorial-bypass/w43-r3-2-reader-preview-UNVALIDATED-20261026.md`, 96-row ledger, crosswalk, QA, full source accepted Evidence, source paths. Human Architecture approved r6; State `ARCHITECTURE_ESTABLISHED`, machine Draft PENDING. No Core rerun/repair or native Stage.
Do ONLY three spotcheck failures (details in Sol verdict), preserve all sound P1–P8 technical prose and exact five paragraphs in `今週の総括`.

### R32-SOL-01 P1: correct scoped npm original metadata URI

- Check actual publisher package `@tanstack/ai` (official npm package `https://www.npmjs.com/package/%40tanstack/ai`), GitHub release tag `@tanstack/ai@1.0.0` and accepted selection rationale `GitHub 2026-10-22T15:18:14Z` versus npm registry `2026-10-22T15:21:49Z`.
- r3.2 ledger `p8-f2.table_rows[row=版固定].url` mistakenly cites **unscoped** `https://registry.npmjs.org/ai`. Correct to properly resolved scoped registry URI (canonical likely `https://registry.npmjs.org/@tanstack%2Fai`, but verify correct package/key by publisher's npm source before making a raw-proof claim) or mark `REGISTRY_RAW_NOT_VERIFIED` and cite the actual official `@tanstack/ai` package page rather than unrelated package. If the raw timestamp cannot be independently read, keep separately attributed older Evidence/Selection publisher timing as such — no "direct fresh registry" claim.
- Check new row's `clock`, `url`, `claims[]`, source crosswalk and reader P8 table time notes for internally consistent attribution. GH release and npm metadata MUST have **independent** references; one URL cannot prove both.

### R32-SOL-02 P2: clean reader-facing opening

- New reader-export body must begin with a neutral reader masthead e.g. `# 日本語版週刊AIサーベイ — 2026年第43週` followed by the first article P1, optionally a real editorial introduction, NOT a `UNVALIDATED` legend, `実行根拠と状態`, Git SHA, draft checkpoint or previous revision lineage inside reader.
- Put governance and "UNVALIDATED" and edition-local provenance in internal QA/handoff and file **filename** only. This is NOT permission to claim native Stage passed or to remove truthful governance from audit files.
- Make `今週の総括` P8 afterword full five substantive paragraphs, no editor meta trailing, not P9, no new claims.

### R32-SOL-03 P2: remove keyframes false official contradiction certainty

- Inspect every P4 wording `keyframes`, `FAQ`, `矛盾`, `資料間` in reader and ledger `p4-p2,p4-p7`.
- Treat actual first-party PR/blog keyframes announcement as **publisher claims**. The contrary `Two at launch` allegedly from FAQ is **NOT a verified publisher document**, its exact URL/version/clock unavailable. Phrase as `発表元のPR/ブログではkeyframes対応が案内されている。一方、二様式のみとするFAQ由来とされる記述については原典・発行者を確認できていないため、公式資料同士の矛盾とは断定できない。live/schema/GAは未確認` (paraphrase freely).
- Preserve `UNRESOLVED_FAQ_ATTRIBUTION`, `UNVERIFIED_CONTRARY_DESCRIPTION` and source provenance in internal ledger. Do not incorrectly eliminate documented vendor PR/blog **speed values 10.95s vs 12.45s**, **Elo +47/+50** conflicts. Distinguish unsupported keyframes contradiction from those supported numeric discrepancies.
- Approved canonical Architecture old conflict label retained as historical source state, no changes.

## 2. Deliverables / acceptance

Create entirely NEW edition-local r3.2.1 files (prior versions immutable):
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-1-reader-preview-UNVALIDATED-20261026.md`;
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-1-citation-confidence-ledger.json`;
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-1-source-crosswalk.md`;
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-1-editorial-qa.md`;
- `sources/2026-W43/execution/SOL_W43_CORE_FREE_EDITORIAL_R3_2_1_SPOTCHECK_HANDOFF.md`; session/index update.

Check 96 unique ledger IDs, 20/20 `table_rows[]`, five newly added tables' 29 claim-level refs, no unmatched rows, and 31 requirements with source-supported `26 SUBSTANTIVE_COMPLETE / 5 PARTIAL` unless new evidence strictly justifies a real change. No new topic or W44 claim. Verify first reader lines free of operator metadata, P4 unsupported certainty absent, P8 npm package reference exact match, and ending five recap paras unchanged. Show exact diff SHA and normal commit chronology. Mark any unverified original publisher registry as unverified, not false success. Note 20 tables still DRAFT_TEXT and source gaps still not a Core native PASS.

Do not alter shared Core or any config/schema/scripts, machine State/checkpoints, Architecture/Selection/Evidence, Gates, receipts, upstream authority, other branches; do not run blocked Core, no `ADVANCE_STAGE`, TeX/PDF, Publication Preview, Freeze/Release. Local repo normal commit/non-force push to ONLY work branch, then remote HEAD/Root Tree readback. Stop `SOL_W43_CORE_FREE_EDITORIAL_R3_2_1_READY_FOR_SOL_SPOTCHECK`.

If scoped registry package cannot be resolved, you may validly record `REGISTRY_RAW_NOT_VERIFIED` with authoritative npm package webpage and accepted Selection rationale; if package/clock actually contradicts accepted Selection, stop `SOL_W43_R321_SOURCE_CONFLICT` and report rather than silently changing source or Architecture.
