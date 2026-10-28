# W43 Core-free editorial QA r3.5 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE / R3.5_SINGLE_P1_SEMANTIC_CLAIM`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `execution/instructions/sol-w43-r35-single-p1-semantic-claim-closure-20261026.md`
(parent verified `b6101733…`, diff = contract file only; dispatch HEAD `2ec0202b…`/Tree `1fb36c82…`,
main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…` — 6-way PASS before any write).
r3.5 preview: `execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md`
Ledger: `execution/editorial-bypass/w43-r3-5-citation-confidence-ledger.json` (96 blocks / 20 TABLES / 80 table sub-rows + 3 figure rows / 29 claims)
Manifest: `execution/editorial-bypass/w43-r3-5-physical-row-manifest.json` (20 tables, 80 rows: EXACT 49 / EXACT_AFTER_RSTRIP 18 / SANCTIONED_ALIAS 13)
Strict semantic checker: `execution/editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py` → `w43-r3-5-semantic-join-result.json` **EDITION_LOCAL_ROW_JOIN_PASS, exit 0**
Crosswalk delta: `w43-r3-5-source-crosswalk-delta.md`. Basis: r3.4 subject `1a4cfedb…` inspected by independent Sol (REQUEST_CHANGES, P1 R32-FULL-003 only); r3.4 bytes preserved.

## 1. R32-FULL-003 (P1) — single-finding semantic closure, no vacuous PASS

- T1 (20 headers): all 20 reader 表 headers parsed in order, byte-exact match to pinned expected strings + manifest header identity. Header mutation negative (`Kimi改`) FAILs with `T1-HEADER-MISMATCH` even with 80 rows unchanged.
- T2 (80 bijection): 80 physical ｜-lines + UTF-8 SHA256 + line numbers + ordinals + `row_id` ↔ 80 manifest rows ↔ 80 ledger `table_rows`, exact, no dups/gaps. Manifest↔ledger `row_type` matched for all 80 (78 DATA / 2 NOTE: `p1-t2-04`, `p4-t1-05 NOTE`). 13 sanctioned aliases pinned to expected `(ledger_label, physical-first)` pairs; self-declared alias fails `T2-ALIAS-UNSANCTIONED`. NOTE excluded from claims; 3 figure rows out of scope.
- C (29 semantic): pinned independent baseline of 29 claims (block/row/value/metric/variant/unit/comparator/URL/tier hardcoded, not generated from ledger). EVERY claim validated: own-block DATA, ledger baseline exact, physical row actually prints its own value (narrow lexical map: `40%超≡40%+`, `500ms未満≡sub-500ms`, `対象外≡excluded`, npm seconds normalize `.491Z`), correct variant in physical (e.g., COBOL in `p7-f1-01`, npm+GH separation in `p8-f2-03`), metric/unit/comparator/URL/provenance honesty. Generic token-in-URL/clock does NOT excuse missing physical value (r3.4 loophole closed).
- The 2 repairs:
  - COBOL `40%+` (enterprise share, NOT accuracy): `p7-f1-01` physical now `…・企業現場40%超（オンラインバンキング言及、精度とは別）`. Checker requires `40%` + (`企業現場`|`オンラインバンキング`) + `精度とは別` in same physical row, plus `COBOL`. Value `40%+` stays `enterprise share / percent of online banking / enterprise feedback`, never benchmark performance.
  - npm `2026-10-22T15:21:49Z` (registry clock): `p8-f2-03` physical now `…（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠）`. Checker requires `15:21:49` + `2026-10-22` + `npm` + (`GH`+`別`) in same physical row. GH vs npm kept separate; scoped URL + `RAW_NOT_ARCHIVED` preserved; millis `.491Z` in ledger clock, seconds in reader (documented).
- Provenance honesty: 5 `RAW_PRIMARY` (4× MemT README 208–219 + 1× TanStack GH JSON) validated for file existence AND relevant text (`Attribution-NonCommercial-ShareAlike` / `PolyForm` / `flash-linear-attention` / `not covered` / `15:18:14Z`), not mere `Path.exists()`. 24 `QUALIFIED_UNAVAILABLE` (`ARCHIVE_UNAVAILABLE` / `RAW_NOT_ARCHIVED`) honestly labeled, never promoted. MemT 66x storage scope, Patch stage4/5, Voxtral comparators/units, DeepInfer PSEUDOCODE, DeepSeek MIT caveat, FAQ unknowns all retained.
- Digests (unambiguous, exact file bytes): reader `6f07cb49…1cc5da46d6`, ledger `6fd9d6fe…382e6d4`, manifest `85d94d74…26a3cf111` (see result JSON). Canonical normalized hashes stored separately as `ledger_canonical_json_sha256` (`49c1e650…`) / `manifest_canonical_json_sha256`, never named `*_sha256`.
- Negatives 24/24 PASS, each for its SPECIFIC semantic reason (not incidental): 9 preserved r3.4 regressions + 15 true physical/semantic — incl. phys del/dup/swap/mutate row, header mutate, claim remove (29→28), claim value change w/o row change, variant/metric/URL/provenance/unit changes, row_type DATA↔NOTE flip, NOTE-target, unscoped npm, false price confirm, comparator unqualified, AND both pre-fix counterexamples (`P_cobol_strip` → `p7-f1-01/enterprise-40p C-VALUE-MISSING`, `P_npm_strip` → `p8-f2-03/npm-clock C-VALUE-MISSING`). Pre-fix r3.4 files run through r3.5 checker → `P1_OPEN` with exactly the 2 semantic `C-VALUE-MISSING` families (COBOL 40%+ + npm clock + qualifiers/roles/dates), proving the fix is load-bearing, not vacuous.
- Verdict `EDITION_LOCAL_ROW_JOIN_PASS` = edition-local join only; never source originality, native Stage, guaranteed provenance, or independent Sol sign-off.

## 2. Preserved (contract §4)

R32-FULL-001/002 meanings intact (storage ~1/66, parametric scope, 1.86x SOURCE_UNVERIFIED; stage4 product-update prep, stage5 post-patch guidance, Daybreak/checker outside, CVE≠none); 004 scoped npm; 005 clean header; 007 path split; 008/009 bounded limitations; 010 pseudocode labels. 8 packages, 31-baseline 20/11, 5-para recap (still 5 paras, not P9), r3.4 bytes, 96 IDs, 29 claims. Reader table-row byte diff r3.4→r3.5 is exactly 2 ｜-lines (title version label + 2 physical facets); `grep -c ｜` counts unchanged (80). No new research, no Architecture/Selection revision, no r3.4 PASS self-claim.

## 3. Invariants + stop

Untouched: r1–r3.4 assets, Architecture r6, Selection, accepted Evidence/Views, production-state.json, gates/reviews + approvals, reviewed Human approval, reviewed main, Frozen Core v2, shared roots. No TeX/PDF/Stage/Gate/Freeze/Release. No new branch, no reset/rebase/force.

Terminal: `MUSE_W43_R35_SINGLE_P1_SEMANTIC_CLAIM_REPAIR_READY_FOR_SOL_RECHECK`
