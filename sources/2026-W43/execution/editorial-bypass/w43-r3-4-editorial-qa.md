# W43 Core-free editorial QA r3.4 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE / R3.4_BOUNDED_ROW_JOIN_FAQ`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `execution/instructions/sol-w43-r34-bounded-editorial-closure-table-join-faq-20261026.md` (parent verified `4f89fba23…`, diff = contract file only; 6-way guard PASS).
r3.4 preview: `execution/editorial-bypass/w43-r3-4-reader-preview-UNVALIDATED-20261026.md`
Ledger: `execution/editorial-bypass/w43-r3-4-citation-confidence-ledger.json` (96 blocks / 20 TABLES / 80 table sub-rows + 3 figure rows / 29 claims)
Manifest: `execution/editorial-bypass/w43-r3-4-physical-row-manifest.json` (20 tables, 80 rows: EXACT 49 / EXACT_AFTER_RSTRIP 18 / SANCTIONED_ALIAS 13)
Strict checker: `execution/editorial-bypass/w43-r3-4-strict-row-join-check.py` → `w43-r3-4-row-join-result.json` **EDITION_LOCAL_ROW_JOIN_PASS, exit 0**
Crosswalk delta: `w43-r3-4-source-crosswalk-delta.md`. Basis: r3.3 subject `4f89fba23…` inspected by editorial Sol; r3.3 bytes preserved.

## 1. R32-FULL-003 (P1) — strict join proof, no count-smoke reliance

- Parsed all 20 reader ```text 表 blocks (figures p1-f1/p3-f1/p6-f1, p8-f1 example, code blocks excluded). Physical row = a line containing ｜ (exactly 80; 典拠 lines use ／ and contain no ｜).
- Bijection T1/T2: 20/20 tables in expected order; 80 physical lines+hashes == 80 manifest rows == 80 ledger `table_rows[].row_id`; no missing/duplicate/extra/swapped. Label rule governed: EXACT 49, EXACT_AFTER_RSTRIP 18 (reader pads " ｜"; exact bytes hash-bound), SANCTIONED_ALIAS 13 (p1-t2×3, p1-t4×3, p2-t2×3, p2-f2×2, p4-t1 22x NOTE×1, p5-t1 TTS×1 — each with recorded note, no literal equality asserted).
- Claims C1–C8: 29/29 on own-block DATA rows; `noted` triggers FAIL (C2 proven by same-block synthetic NOTE test); variant/value bound to row context; required fields non-empty; archive honesty enforced (repo paths existence-checked: 5 RAW_PRIMARY; 24 QUALIFIED_UNAVAILABLE incl. RAW_NOT_ARCHIVED npm; 0 OTHER — no false verified promotion); price-confirmation registry (Mini/Speech only), WER/recall comparator rule, npm scope+clock rule all hold.
- Anchors T5: MemT storage wording, 1.86x SOURCE_UNVERIFIED, parametric scope, p3-t2 classifier, TTS Speech 3, Controlled Voice — all present in manifest physical text.
- Negatives 9/9 detected, each for its specific reason: drop/dup/swap/mutate row, claim→NOTE (x-block + same-block C2), claim→wrong block, unscoped npm, false unit confirmation.
- Explicit ledger micro-fixes (justified, counts unchanged): p8-f3 free-till→02 / bench→03; recall qualifier → COMPARATOR_UNVERIFIED.
- Verdict `EDITION_LOCAL_ROW_JOIN_PASS` = join proof only; never source originality or native Stage PASS. SHAs: reader `9dcd7a79…cf4d89af`, ledger `db3590cc…564001ee` (see result JSON).

## 2. R32-FULL-006 (P2) — FAQ contradiction wording, every P4 mention

- Intro (L230): 数値の不整合 (verified arithmetic; 矛盾 word removed). §4.1 (L234): 未照合の食い違い + FAQ原文未特定 + 確定矛盾として扱わない (explicit). Subsection (L258): 未照合の食い違い + 確定した資料間矛盾ではない (explicit). 注意 (L260): 食い違う分母 (再計算で不整合を確認). Recap para 3: 公表値の再計算不整合 / 版・snapshot相違 / 提供機能の未照合の食い違い (no definite conflict stated).
- Reader-wide `矛盾` grep: only remaining hits are the two explicit denials above. Benchmark arithmetic, live/schema/GA UNKNOWN, all evidence limitations preserved. Architecture untouched.

## 3. Preserved (contract §2)

R32-FULL-001/002 meanings intact (storage ~1/66, parametric scope, 1.86x SOURCE_UNVERIFIED; stage4 product-update prep, stage5 post-patch guidance, Daybreak/checker outside, CVE≠none); 004 scoped npm; 005 clean header; 007 path split; 008/009 bounded limitations; 010 pseudocode labels. 8 packages, 31-baseline 20/11, 5-para recap (content-qualified only, still 5 paras, no P9), r3.3 bytes, 96 IDs, 29 claims. Reader table rows byte-identical r3.3→r3.4 (diff shows 0 ｜-line changes).

## 4. Invariants + stop

Untouched: r1–r3.3 bytes, Architecture r6, Selection, accepted Evidence/Views, production-state.json, gates/reviews + approvals, reviewed main, Frozen Core v2, shared roots. No TeX/PDF/Stage/Gate/Freeze/Release.

Terminal: `MUSE_W43_R34_BOUNDED_ROW_JOIN_FAQ_REPAIR_READY_FOR_SOL_EDITORIAL_RECHECK`
