# TS-003 Language QA r8 — bidirectional terminology repair

Status: `PASS_WITH_NOTES / MAP_R8_APPLIED / SOL_R8_PENDING`

Date: `2026-10-02`

Authority: `execution/drafting-terminology-map-ja.md`
(starting blob `fcc0c6224ac400a3f0f3ba42016d66190a67bfc9`,
status `DRAFT_R8_BINDING`,
terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R8_BINDING`).

Scope: all 16 r8 Draft Results (headline + deck + PARAGRAPH + CLAIM_BOUNDARY) +
canonical profile synthesis result payload. Reader text ~53.3k chars.

## 1. Exact duplicate sentences

Zero per package and cross-package (re-verified post-regeneration).
No re-padding.

## 2. Bidirectional Section-2 audit

Direction A (concept → preferred): all §3.7/§3.8 target concepts now use
preferred forms (ボックス, オープンボキャブラリー, デコーダ, キャリブレーション不要,
スケーリング, オープンウェイト, 構成要素/部位/要素名, クエリ, アテンション,
ショートカット接続, one-stage/two-stage, 特徴マップ, デュアルエンコーダ, MoE,
dense構成, コールドスタート, チェックポイント, 学習可能パラメータ, バリアント,
カテゴリ, マスクされた離散, 音声系, 教師モデル/生徒モデル, 自己教師あり,
マルチモーダル, デプロイ, モデルカード, ファインチューニング, 系譜).

Direction B (preferred token → correct concept), spot-verified per family:
アテンション 4 (all attention mechanisms/maps), クエリ 6 (all model queries),
チェックポイント 2 (both model checkpoints), 教師モデル 6 (all teacher models),
自己教師あり 9 (all self-supervised senses), マルチモーダル 7, デプロイ 10,
オープンウェイト 5, モデルカード 5, ファインチューニング 13, one-stage 4,
特徴マップ 1, MoE 3, コールドスタート 2, バリアント 7, カテゴリ 8,
ショートカット接続 1, 対照学習 5, 軌道 5, 系譜 24 — each occurrence read in
context; no preferred token stands for a different underlying concept.

## 3. Residual classification table (every occurrence + synthesis)

### ボックス — all bounding-box/box semantics (ALLOWED)
P02 headline/deck/b1/b2(×3)/b3(×4)/b4(×2)/b5(×2): detection boxes, default boxes,
grid cells, loss terms, anchor boxes, output boxes. P03 deck(×2)/b1/b2(×5)/b3 +
boundary(×2): box lineage, output branches, box-dependence, prompted points.
P04 deck/b1/b3(×2): box labels, box I/O. P06 b1 (box AP metric)/b3 (detection boxes).
P07B headline/deck/b1(×2)/b2/b4(×3)/b5/b7/b9(×2): grounding boxes, annotation boxes,
box-free labels. P09 b1 (grounding boxes). — No non-box use remains (P13 b3/b5
repaired to 別系統分離 / 一モデル扱い).

### 箱 — ZERO occurrences (ALLOWED trivially; Direction A complete)

### 鎖
- P05 b2 「誤読が後段へ波及する連鎖」 — ordinary causal chain (ALLOWED).
- P07B b1 「244Kの共参照鎖」「同じ物を指す言い回しの鎖」 — technical coreference
  concept (ALLOWED per map exception).
- P13 lineage organizer — ABSENT after repair (was b7).

### 極
- P02 b3 「極端な不均衡」 — ordinary adjective (ALLOWED).
- P11 b4 「極めて長い」 — ordinary adverb (ALLOWED).
- P14 deck(×2)/b2(×3)/b3(×2)/b4/b6 — Architecture-approved four-pole
  classification (ALLOWED exception).
- SYN branch_transition_synthesis 「歴史的定式・潜在ダイナミクス・予測表現・
  生成的環境の四極」 — explicitly names all four P14 poles (ALLOWED).
- Non-P14 organizers (P03/P05/P07B/P13/P15) — ABSENT after repair.

### 話し言葉 — ZERO occurrences (P09 boundary now 音声認識の範囲; scope preserved)

### 部品 — ZERO occurrences (packages + synthesis; synthesis now 構成要素/モジュール構成)

### 橋 / 橋渡し — ZERO occurrences (packages + synthesis)

No unclassified hit remains.

## 4. Full registry re-audit (§§3.1–3.8)

Zero TECHNICAL_SUBSTITUTION_BLOCKING hits across all 138 corpus rows
(16 results + 4 synthesis fields), with 生徒モデル/符号化 disambiguation.
Prior-round gains intact (網/教員/符号/多様式/幻覚/物差し/錨/一段階-family etc.).

## 5. Package + synthesis scope proof

Repaired: P13 b3/b5/b6/b7, P03 b2 + boundary, P05 b5, P07B b6 (+渡し/混ぜ variants
as same-class fusion metaphors, documented), P09 boundary, P13→P15 b7,
synthesis branch_transition (部品の橋渡し→構成要素の接続, 四極 clarified to all
four poles) + parallel (部品の組み立て→モジュール構成, 後期→後段).
All other prose byte-identical to r7. No new synonym/metaphor introduced
(verified: repaired regions contain only map-preferred or ordinary terms).

## 6. Preserved gains + integrity

Zero duplicates; no padding; r1–r7 repairs intact; boundary sets unchanged
(53 EXPLICIT + 104 OMISSION, P03/P09 boundary wording repaired per F3/F4);
evaluator roles explicit; G01–G06/PARTIAL intact; P07B grouped, P09
protocol-bound, P15 synthesis-led; packages byte-identical; no new research.

## 7. New failures in r8

None beyond §3.8. Map-first rule not triggered; map unchanged
(final blob == starting blob, recorded in r8 report §13).

Terminal QA state: `TS-003_LANGUAGE_QA_R8_COMPLETE / PASS_WITH_NOTES`
