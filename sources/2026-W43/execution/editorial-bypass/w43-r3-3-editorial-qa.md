# W43 Core-free editorial QA r3.3 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE / R3.3_ONE_BATCH`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only).
r3.3 preview: `execution/editorial-bypass/w43-r3-3-reader-preview-UNVALIDATED-20261026.md`
Ledger: `execution/editorial-bypass/w43-r3-3-citation-confidence-ledger.json` (96 block IDs preserved; 20/20 tables; 80 table sub-rows + 3 figure rows; 29 claims all with `row_id`)
Crosswalk: `execution/editorial-bypass/w43-r3-3-source-crosswalk.md` (36 keys + tanstack-npm scoped row)
Join check: `execution/editorial-bypass/w43-r3-3-table-join-check.py` (edition-local, Frozen Core independent) → `w43-r3-3-table-join-result.json` **STRUCT_PASS 33/33**
Basis: independent comprehensive audit receipt `20261026022400_SolReview.md` (45,043B, SHA256 `78a61517d59c8140f1c32eff21376657374ab2d7d37af7a4939e63f7bfb1846f`) — **原文未読** (not retrievable in-session; standing limitation). Adjudication + sole contract `sol-w43-r33-one-batch-comprehensive-editorial-repair-for-corefree-pdf-preview-20261026.md` used instead. Fixed audit subject r3.2 HEAD `efac8324ff7a9f35ad34be391ba2ea328cfc1722` / Tree `61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43`.
Method: one-batch repair of all 10 received issues (P1×3 + P2×7). No breadth expansion, no guessing. r1/r2/r3/r3.1/r3.2 byte-untouched.

## 0. Moved operational info (removed from reader header per R32-FULL-005)

r3.2 header carried (now stored here, filename keeps UNVALIDATED): prior state `r3.1改訂版を起点とするedition-local r3.2限定修正（独立監査4点）`, lifecycle `ARCHITECTURE_ESTABLISHED`, Human Architecture Review APPROVED, Draft checkpoint PENDING, provenance pointer to r3.2 QA. r3.3 basis: r3.2 → r3.3 one-batch (R32-FULL-001..010). Formal lifecycle unchanged (see §6).

## 1. Ten-issue closure (independent verdict REQUEST_CHANGES, P0=0)

| ID | Sev | Verdict | Evidence / acceptance test |
|---|---|---|---|
| R32-FULL-001 MemT 66x | P1 | FIXED | `memt-readme-e75c13d.md:24` = storage ~66x vs full-context KV @128K. Reader ¶116/table/¶164 now state 保存容量約66倍削減, deny speed/throughput/sustained reading. 11bench scoped to evaluated parametric-memory methods + textual-memory caveat (`:55`). 1.86x absent from saved README → SOURCE_UNVERIFIED (paper-derived AUTHOR_CLAIM per accepted Evidence claim-2) or excluded from body claims. Ledger p2-t2 rows renamed + notes; crosswalk MEMT-README annotated. Join check S5-memt-*/S6-reader-66x/parametric PASS. Test: `grep -c 保存容量約66倍削減 reader` ≥3 AND `持続（sustained）vs KV` absent AND `SOURCE_UNVERIFIED` present. |
| R32-FULL-002 開示五段階 | P1 | FIXED | `openai-patch-planet-rendered-20261025.md:17-22` verbatim 5 stages adopted 1:1 in prose (§6.1/§6.3) + p6-f1 figure. Daybreak $1B + Codex PHP checker moved to 工程外の関連施策 (no longer stage 4). Roles separated (発見=Calif / 独立双方確認=Wiz / 主導=maintainer / 貢献=Wiz・Cloudflare等). CVE = 識別子未特定≠不存在証明. RENDERED_TEXT vs 原HTML distinguished. Test: `影響製品の更新準備` + `パッチ利用可能後の案内公表と展開支援` + `工程外の関連施策` present; `[4 prepare] $1B Daybreak` absent. |
| R32-FULL-003 全20表双方向完全性 | P1 | FIXED (structural) | All 20 TABLE blocks carry `table_rows[].row_id` (`{block}-{nn}`, 80 table sub-rows + 3 figure rows, unique, S2 PASS). All 29 claims carry `row_id` → existing DATA row (S3 PASS, orphans 0). NOTE typing: p1-t2 注意 + p4-t1 22x見出し (S4 PASS, excluded from data joins). p3-t2 classifier row added (3→4). p1-t2/Flint/Nemotron, p2-t2, p4-t1, p5-t1 `STT Small Transcribe 3` exact, p5-t2 `Controlled Voice` exact, p8-f2 scoped npm fixed. Join script executed, `w43-r3-3-table-join-result.json` STRUCT_PASS 33/33. Authenticity of primary sources judged separately (§5). Test: rerun `python3 w43-r3-3-table-join-check.py` → exit 0. |
| R32-FULL-004 TanStack | P2 | FIXED | Unscoped `https://registry.npmjs.org/ai` removed everywhere (reader had none; ledger p8-f2 row fixed to `https://registry.npmjs.org/@tanstack%2Fai`). Clocks: GH `2026-10-22T15:18:14Z` (own ref, archived json) vs npm `time["1.0.0"]=2026-10-22T15:21:49.491Z` (r6 crosswalk; own ref). npm body RAW_NOT_ARCHIVED — no fabricated direct verification. Crosswalk adds tanstack-npm row. Test: `registry.npmjs.org/ai` absent (modulo scoped form) in reader+ledger. |
| R32-FULL-005 冒頭運用情報 | P2 | FIXED | Reader header stripped to clean title (UNVALIDATED/Stage/実行根拠/SHA removed from prose; kept in filename + this QA §0). Recap 5 paragraphs byte-identical, no P9, no editor note (S7 PASS). |
| R32-FULL-006 FLUX FAQ | P2 | FIXED (qualified) | `UNRESOLVED_FAQ_ATTRIBUTION` kept; no upgrade to verified official-vs-official contradiction. live/schema/GA UNKNOWN kept. Real fal PR/blog numbers preserved (10.95/12.45s, Elo +47/+50 versioned, 25.37x/22.31x/95.52% recomputed, 26.5x/96.2% inconsistent). Test: `UNRESOLVED_FAQ_ATTRIBUTION` present; 確定した…矛盾に格上げしない present. → QUALIFIED_WITH_LIMITATION (raw FAQ originals never archived). |
| R32-FULL-007 Duet/1Password | P2 | FIXED | p6→p3-f1 figure split into 経路A (live VM/browser boundary, Duet 2026-10-21) vs 経路B (coming-soon 1Password 2026-10-22, NOT_LIVE_VERIFIED, vendor design claim). Never-visible-secrets applies to both as design claim, independent test absent. Test: `経路A` + `経路B` + `NOT_LIVE_VERIFIED` present. |
| R32-FULL-008 Voxtral | P2 | FIXED (qualified) | Variant/sample/comparator kept per r3.2 qualification (WER/recall内訳 COMPARATOR_UNVERIFIED, cpWER vs Pyannote explicit, Small/Realtime/agent UNIT_UNVERIFIED, Mini $0.0035/min + Speech $13/M verified, STT/Realtime/TTS counts + 11-lang sample separated, TTS conflict UNRESOLVED). p5-t1 variant name exacted. → QUALIFIED_WITH_LIMITATION (voxtral raw bytes never archived; accepted Evidence task-18a859ebb1ef50040078 only). |
| R32-FULL-009 P7/P8証拠 | P2 | FIXED (qualified) | COBOL 72.1% as the sole <83% exception of 19/20≥83% (prose+tables consistent); hidden 86.6/97.9 as separate vendor-held test; Luna $0.77/Sol $3.48 cost gap ≠ quality parity (explicit). DeepSeek MIT as vendor-published; per-artifact LICENSE bytes/SHA unverified explicit; API/harness license not conflated. → QUALIFIED_WITH_LIMITATION (hidden tests vendor-held; weight bytes/SHA unhashed). |
| R32-FULL-010 DeepInfer/日本語 | P2 | FIXED | SamplingParams example labeled PSEUDOCODE/NONRUNNABLE/NOT_EXECUTED/IMPORT_UNVERIFIED (import path unwritten, not copy-paste runnable). `程序` → `プログラム` (+PSEUDOCODE note). No new duplicated caveats added; unique limits preserved. |

No P1 left unrepaired. P2 = 4 FIXED + 3 QUALIFIED_WITH_LIMITATION (006/008/009, each with evidence-grounded limitation, none coerced).

## 2. 20-table join summary

`w43-r3-3-table-join-result.json`: STRUCT_PASS, 33/33 checks (S1–S8). 96 blocks, 20 tables all with rows, 83 row_ids unique (80 table + 3 figure), 29/29 claims linked to DATA rows, 2 NOTE rows excluded, 7 known-defect spot checks PASS, 16 reader-string checks PASS, recap 5-para + no-P9 PASS, label traceability PASS. Count-only PASS explicitly NOT claimed (§4 r3.2 row-quality separation carried).

## 3. 31-requirement matrix (independent 20/11 baseline adopted per contract)

`SUBSTANTIVE_COMPLETE=20 / PARTIAL=11 / MENTIONED_ONLY=0 / NOT_ADDRESSED=0 / NOT_VERIFIABLE=0` (independent audit's grading adopted; Muse self-scores superseded). PARTIAL truthfully limited: §1.4 vendor-only comparators · §2.2 NOT_EXECUTED recipes + SOURCE_UNVERIFIED 1.86x · §4.1 UNRESOLVED_FAQ_ATTRIBUTION · §5.1 TTS count UNRESOLVED · §5.2 COMPARATOR/UNIT_UNVERIFIED + 009/010 limitations. 19 placements, 8 packages, 5 LIMITED, 68 Attention inherited unchanged (not re-verified without execution — no such claim).

## 4. Confidence breakdown (96 blocks)

VERIFIED_DIRECT 16 (recomputed arithmetic + exact clocks + archived-byte reads, unchanged scope) / SOURCE_REPORTED 69 / LIMITED 7 / UNRESOLVED 4. Tiers: FIRST_PARTY 79 / DERIVED_ONLY 14 / UNAVAILABLE 3. 1.86x row tier set DERIVED_ONLY/SOURCE_UNVERIFIED; npm row tier FIRST_PARTY_METADATA/RAW_NOT_ARCHIVED. None implies replicated vendor benchmarks.

## 5. Source-authenticity separation (not covered by STRUCT_PASS)

Read-but-unarchived: voxtral announcement, duet/1Password/automode blogs, eleven blog, ming AA tables, deepseek news, securing/bio/lowres pages (accepted Evidence record only). Rendered-only: patch page (bot-wall, 9946B). Raw-archived + read: MemT README (66x storage line 24, rank line 55, license 208–219), DeepInfer README+environ @9bd9cf24, Flint card+announce, Nemotron card+commits, Kimi X+blog, fal flux pages, tanstack GH release json, decisions changelog + Oct25 guide snapshot (post-cutoff secondary). 32 accepted sources / 68 Attention NOT re-verified in this unit — not claimed.

## 6. Reader length, same method (R3-SOL-02 method reused)

r3.2 full 68,768B / prose-only 51,966B → r3.3 full 71,499B / prose-only 52,872B (delta +2,731 / +906: qualifying clauses + stage exact wording + path split + row keys, no padding). Deleted substantive claims: none (1.86x limited, not deleted; header meta moved here). Recap: 5 paragraphs after P8, byte-identical to r3.2.

## 7. Residual risks + invariants

Vendor-only numbers, DRAFT_TEXT layouts (not typeset/renderer-validated), BLOCKED native Stage, unread original report (§Basis), RENDERED_ONLY patch, post-cutoff Oct25 observations not promoted to W43 facts, TTL 30m not a W43 fact. Untouched: r1/r2/r3/r3.1/r3.2 bytes, Architecture r6, 19 SELECTED, candidate matrix/selection, accepted Evidence/Views, production-state.json, gates/reviews + approvals, reviewed main (`041a08df…`), Frozen Core v2 (`774dd39a…`/tree `cd46a6f…`), shared roots (`AGENTS.md config/ schemas/ scripts/ .github/workflows/ docs/survey-production-core-v2-*.md`). No Stage/TeX/PDF/Preview/Freeze/Release in this unit. Noncanonical PDF preview NOT built (contract §4).

## 8. Terminal

All P1 repaired with evidence; P2 FIXED or QUALIFIED_WITH_LIMITATION; full 20-table structural join demonstrated. `SOL_W43_CORE_FREE_EDITORIAL_R3_3_BATCHED_REPAIR_READY_FOR_INDEPENDENT_CLOSURE`
