# SOL_W43_CORE_FREE_EDITORIAL_R3_3_BATCHED_REPAIR_HANDOFF

Status: `SOL_W43_CORE_FREE_EDITORIAL_R3_3_BATCHED_REPAIR_READY_FOR_INDEPENDENT_CLOSURE`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `execution/instructions/sol-w43-r33-one-batch-comprehensive-editorial-repair-for-corefree-pdf-preview-20261026.md`
Basis: independent comprehensive `20261026022400_SolReview.md` (45,043B, SHA256 `78a61517…`, **原文未読** in-session — standing limitation); receipt + consolidated adjudication + contract as binding basis. Fixed audit subject r3.2 `efac8324…`/`61e33ad8…`. Own-environment 6-way re-verified PASS (work `1dc4e1e8…`/`b299e4ed…`, main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…`); local clean, fetch + ff-only (8cb1e48→1dc4e1e8, 1 Sol commit). No prohibited ops.

## Ten-issue closure (REQUEST_CHANGES, P0=0; no P1 left unrepaired)

| ID | Verdict | What changed |
|---|---|---|
| R32-FULL-001 MemT 66x | P1 FIXED | 66x → 保存容量約66倍削減 (128K・full-context KV cache比, 原README 24行); 11bench → parametric-memory方式内順位 + textual-memory caveat; 1.86x → SOURCE_UNVERIFIED (保存README記載なし・論文派生AUTHOR_CLAIM). Prose+table+ledger+crosswalk changed together |
| R32-FULL-002 開示五段階 | P1 FIXED | Exact 5 stages per raw 17-22行 (upstream validate+fix / 時間確保 / 政府調整 / 更新準備 / 公開後支援); Daybreak+checker → 工程外の関連施策; Calif/Wiz/maintainer roles separated; CVE 未特定≠不存在証明 |
| R32-FULL-003 全20表完全性 | P1 FIXED (structural) | `row_id` on all 83 rows (unique) + on all 29 claims (0 orphans); NOTE typing (p1-t2 注意, p4-t1 22x); p3-t2 classifier row added; STT/Controlled Voice exact; npm scoped. Join script executed → STRUCT_PASS 33/33 |
| R32-FULL-004 TanStack | P2 FIXED | Unscoped `/ai` → `@tanstack/ai` scoped; GH 15:18:14Z vs npm 15:21:49.491Z kept as separate refs; npm RAW_NOT_ARCHIVED |
| R32-FULL-005 冒頭運用情報 | P2 FIXED | Header stripped to clean title (info moved to r3.3 QA §0; UNVALIDATED kept in filename); recap 5 paras identical |
| R32-FULL-006 FLUX FAQ | P2 QUALIFIED_WITH_LIMITATION | UNRESOLVED_FAQ_ATTRIBUTION kept, no promotion; live/schema/GA UNKNOWN; real numbers preserved (limitation: FAQ originals never archived) |
| R32-FULL-007 Duet/1Password | P2 FIXED | p3-f1 split to 経路A live vs 経路B coming-soon NOT_LIVE_VERIFIED |
| R32-FULL-008 Voxtral | P2 QUALIFIED_WITH_LIMITATION | r3.2 qualification kept + variant exacted (limitation: voxtral raw never archived) |
| R32-FULL-009 P7/P8証拠 | P2 QUALIFIED_WITH_LIMITATION | COBOL exception consistent; hidden separate; cost≠quality explicit; MIT per-artifact unverified explicit (limitation: hidden vendor-held, SHA unhashed) |
| R32-FULL-010 DeepInfer/日本語 | P2 FIXED | PSEUDOCODE/NONRUNNABLE labels; 程序→プログラム; no new duplicated caveats |

31-matrix on independent 20/11 baseline (contract §1): 20 COMPLETE / 11 PARTIAL, each PARTIAL grounded, none coerced. 96 block IDs preserved; 19 placements / 8 packages / 5 LIMITED / 68 Attention inherited (not re-verified, not claimed).

## Deliverables (NEW r3.3 only; r1–r3.2 untouched)

- `execution/editorial-bypass/w43-r3-3-reader-preview-UNVALIDATED-20261026.md` (full 71,499B / prose 52,872B; P1–P8 + 5-para recap, no P9)
- `execution/editorial-bypass/w43-r3-3-citation-confidence-ledger.json` (96 blocks, 20/20 tables, 80 table sub-rows + 3 figure rows, 29 claims with row_id)
- `execution/editorial-bypass/w43-r3-3-source-crosswalk.md` (36 keys + tanstack-npm scoped row)
- `execution/editorial-bypass/w43-r3-3-editorial-qa.md` (10-issue matrix + join summary + 20/11 matrix + lengths + residuals)
- `execution/editorial-bypass/w43-r3-3-table-join-check.py` + `w43-r3-3-table-join-result.json` (STRUCT_PASS 33/33, edition-local)
- session `execution/sessions/muse-w43-core-free-r3-3-20261026.md` + index entry (this handoff)

## Invariants + stop

Untouched: r1/r2/r3/r3.1/r3.2 bytes, Architecture r6, Selection, accepted Evidence/Views, production-state.json, gates/reviews + approvals, reviewed main, Frozen Core v2, shared roots. No TeX/PDF, no formal Draft Stage, no Publication Preview, no Freeze/Release. Noncanonical PDF preview NOT built in this unit.

Next: editorial Sol check + one limited independent closure audit on fixed SHA diff. `SOL_W43_CORE_FREE_EDITORIAL_R3_3_BATCHED_REPAIR_READY_FOR_INDEPENDENT_CLOSURE`
