# TS-003 Draft r7 review report (for Sol Draft Review r7)

Status: `DRAFT_R7_REVIEW_PACKAGE / AWAITING_SOL_DRAFT_REVIEW_R7 / NO_READER_PUBLICATION_VALIDATION`

Date: `2026-10-02`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

Lifecycle unchanged: `DRAFT_COMPLETE` (no advance, no rollback faked).
Architecture Review `approved`, Publication Preview `pending`,
draft checkpoint `passed`, validation/publication_preview/freeze/release `pending`.

## 1. Startup guards

- remote work HEAD `5a264270591d1ecfb8fa8b590b1e46a4092aaa1a` / tree `7566982aa7d2a7789ee7c339443cffe929b88508` ✓
- remote main `d6381568…` / `83ce3a21…` ✓, Core `774dd39a…` / `cd46a6f7a…` ✓
- map blob `4674bca4f8164fa9fd371b51410ea078160be93d`,
  status `DRAFT_R7_BINDING`, terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R7_BINDING` ✓
- lifecycle/gates/checkpoints per contract ✓; arch `d2f133bc…`, selection `378b818e…` ✓

## 2. Authorities

- Rejected publication candidate r1: commit `1f76b015c…` / tree `3129eb06…` /
  PDF `9f27aeae…` (STALE_AFTER_DRAFT_R7; left untouched, not regenerated).
- Sol Reader/Publication Review r1: REQUEST_CHANGES (F1–F5 + F6 Core staleness).
- Execution authority: `execution/requests/sol-ts003-draft-r7-preferred-terminology-conformance-20261002.md`.
- Draft r6 preserved: git history + `execution/draft-r6-20261002/snapshot-r6/`.

## 3. Cumulative map start/end

- Start: blob `4674bca4…`, status `DRAFT_R7_BINDING`, terminal `…_R7_BINDING`.
- Map UNCHANGED during r7 (follow-up finds were all covered by existing §2
  preferred forms; map-first rule not triggered). Final blob == starting blob (§13).

## 4. Draft Package hashes

All 16 byte-identical to r6 (verified by diff; only results/synthesis changed).

## 5. r7 Draft Result hashes (status REVISED, draft_version r7)

P01 2c521c8b83da / P02 6d62991b9377 / P03 5f9708551234 / P04 0f2dae534953 /
P05 221bb3944d75 / P06 dc85afd346e6 / P07A 05b4e0dfc8fb / P07B 82940f6d61a8 /
P08 ced145f357ab / P09 f050f1ce5e5e / P10 555ebd8877ab / P11 b8c082608840 /
P12 48eb810303a9 / P13 e548bf73feb7 / P14 12e15ee403d3 / P15 b231ed6e6f9b.
Synthesis input `a86e7b79…`, synthesis result `085643ef…` (REVISED).

## 6. Reader-text changes by package (prose only; 11 packages)

- P01: 近道→ショートカット接続 (ResNet mechanism).
- P02: headline 箱/開かれた語彙→ボックス/オープンボキャブラリー; deck 同+一段/二段→one-stage/two-stage; b2 two-stage/特徴マップ/ボックス; b3 ボックス/バリアント/1セル2ボックス/小さなボックス/one-stage/two-stage; b4 ボックス; b5 適用拡張/ボックス/バリアント/オープンボキャブラリー.
- P03: deck ボックス+接続/拡張; b2 統合/ボックス; b3 ボックス/構成要素; b4 拡張; boundary ボックス×2.
- P04: deck/blog ボックス; deck/b1/b4 較正なし→キャリブレーション不要; b4 接続点; b2 部位.
- P05: b3 要素名.
- P06: b1 先行事例 + スケーリング(b3); b3 アテンション注意2件 (follow-up).
- P07A: b1 カテゴリ×2; b3 デュアルエンコーダ×2/バリアント×3.
- P07B: headline ボックス; b1 ボックス/オープンボキャブラリー/カテゴリ; b2 two-stage/オープンボキャブラリー/カテゴリ×3; b4 オープンボキャブラリー/カテゴリ×3/ボックス×3; b5 カテゴリ; b7 ボックス; b8 オープンボキャブラリー/デコーダ×2/バリアント×3/未見カテゴリ; b9 ボックス×2.
- P08: headline→凍結した視覚・言語モデルを接続する; b2 クエリ×2/学習可能パラメータ×2; b3 クエリ×2; b5 構成要素×2/クエリ/バリアント.
- P09: b1 ウィンドウアテンション/MoE; b2 モデル系列/dense構成+MoE/バリアント/一段階×2; b3 バリアント×2; b4 デュアルエンコーダ/マスクされた離散/音声系×4; b5 MoE/コールドスタート/音声系×2; b7 チェックポイント.
- P13: deck 系譜; b1/b2 系譜; b3/b5 ボックス; b6/b7 オープンウェイト.
- P10/P11/P12/P14/P15: prose-identical (hash deltas are runner metadata only).
- Follow-up (audit-driven): CLS注意マップ/注意×3→アテンション系; 一段→一段階 ×2 (P09 b2); 二段→二段階 (P15 b4); ファインチューニング ×6 (P06 b3, P07B b1/b4/b5/boundary); P03-boundary 箱×2.

## 7. Synthesis changes

None (payload bytes rebuilt identically; hashes change only via embedded result shas).

## 8. Terminology conformance

Full Section-2 table in QA r7 §2 (every row: preferred count, nonpreferred hits,
classification, retained exceptions, verdict). Registry re-audit: 0 BLOCKING.
P07B 分割 check: remaining hits are dataset-split senses only.

## 9. Duplicate scan

Zero per package and cross-package. No padding (53.0k→53.2k chars).

## 10. Source roles / boundaries / G-PARTIAL

Evaluator classes explicit; 53 EXPLICIT + 104 OMISSION (sets unchanged; P03
boundary wording repaired); G01–G06/PARTIAL intact; P07B grouped, P09
protocol-bound, P15 synthesis-led.

## 11. Language QA r7

`execution/language-qa-ja-draft-r7.md` (`8936da86…`): PASS_WITH_NOTES
(notes genuinely non-blocking; F5 methodology addressed via full table).

## 12. Deterministic validation + limitations

Canonical per-package derivation + runner result builder + validate_draft_result
×16 + extension propagation ×16 + rebuilt synthesis + validate_synthesis_result:
ALL PASS (driver `execution/draft-r7-20261002/build_draft_r7.py`).
Stage validation/advance not run (contract-forbidden). Core checkpoint staleness
left untouched (no ARCHITECTURE_ESTABLISHED.json rewrite, no fake PASS).

## 13. Terminal + final blob

- Map final blob SHA: `4674bca4f8164fa9fd371b51410ea078160be93d` (unchanged).
- Publication candidate r1: STALE_AFTER_DRAFT_R7 (not regenerated, not deleted).
- Publication Preview pending; no freeze/release; main/Core unchanged (verify at push).
  Final HEAD/tree reported after push.

`TS-003 DRAFT_R7_PREFERRED_TERMINOLOGY_CONFORMANCE_COMPLETE` /
`TS-003 LANGUAGE_QA_R7_COMPLETE` /
`PUBLICATION_CANDIDATE_R1_STALE_AFTER_DRAFT_R7` /
`CORE_CHECKPOINT_STALENESS_UNCHANGED` /
`AWAITING_SOL_DRAFT_REVIEW_R7`
