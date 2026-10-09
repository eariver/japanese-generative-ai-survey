# TS-003 Language QA r4 — cumulative terminology repair

Status: `PASS_WITH_NOTES / MAP_R4_APPLIED / SOL_R4_PENDING`

Date: `2026-10-02`

Authority: `execution/drafting-terminology-map-ja.md`
(starting blob `d17d04e3574a33a263f7f10738a601471f6b095d`,
status `DRAFT_R4_BINDING`,
terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R4_BINDING`).

Scope: all 16 r4 Draft Results (headline + deck + PARAGRAPH + CLAIM_BOUNDARY) +
profile synthesis payload. Reader text ~52.7k chars.

## 1. Exact duplicate sentences

Zero per package and cross-package (counts re-verified post-regeneration;
P07B b9 one-word fix did not introduce repetition). No re-padding.

## 2. Pass A — preferred/avoid conformance (map §§1–2 + §3.4)

All §3.1–3.3 prior gains hold (網/教員/符号/多様式/幻覚/物差し/錨 etc. remain 0).
§3.4 repairs verified present in canonical bytes.

## 3. Pass B — registry audit with per-hit classification

### 5.1 segmentation (P07B mandatory review + volume)
- Repaired to セグメンテーション-family: P07B deck ×2 (機構群, 六群),
  b8 ×6 (枝, 固定ラベルセグメンテーションモデル, 指示×2, パノプティック, 一群),
  b9 ×2 (六群列挙, まとめ文).
- Retained as ORDINARY_JAPANESE_ALLOWED (dataset split, map exception):
  レア・コモン・フリークエントの分割, レア分割 (b1/b2/b4/b7 + boundary),
  試験分割/学習分割/どの分割 (b6), 学習分割 (deck/b9/boundary, P07A b2 + boundary),
  語彙空間と分割の定義 (b9, split-protocol sense in label-space discussion).

### 5.2 bare 測り
- Repaired: P07A deck/b2, P07B deck/b1/b2/b3/b5/b9 (→評価指標/評価方法/評価値/評価).
- Retained: 測り方 explanatory (P07A b2, P07B b1, P14 deck/b6, P15 deck/b9),
  測り手 measurer (P15 b7/b8 + boundary), verbs 測る (P11 b3/b5, P14 b2, P15 b1–b5).

### 5.3 決め/家/家系
- Repaired: P07A b2 ×2 + boundary (→評価条件の定め/抽出規則/取り出し規則),
  P07B b1 OVD評価の家 (→基準), P09 家系×2 + 第二の家 (→モデル系列).
- Retained: 決める/決めない verbs, 位置決め (positioning term) — ordinary.

### 5.4 水増し/足場/土台
- Repaired: augmentation 水増し P03 b1 + P06 b1 (→データ拡張);
  足場 P15 b3 (→scaffold（補助的手順）);
  technical 土台 P02 b2, P05 b3, P06 deck/b3/b5, P07A b3, P07B b8 ×3,
  P13 b2/b5, P14 b1/b4 ×2, P15 b2/b8 (→基盤/ベースライン).
- Retained: inflation 水増し P15 b2; idiom 読みの土台 P15 b1 (map exception).

### 5.5 metaphor phrases
- Repaired: 載せ方/組み方/式と移し P06 deck/b5 (→トークン化/アーキテクチャ/
  目的関数/蒸留); 呼びの到達/結びの仕組み P07A b3; 写しの産物 P07B b3;
  流れの契約/オムニ P09 b5/b6 (→ストリーミング処理/対応);
  配り方 P13 b6/P14 b5/P15 b6 (→提供形態/提供) + 配りの範囲 P15 b8 (→提供範囲);
  軸の勘定 P15 b8 (→別々の評価軸); 一つの芸 P13 b2 (→単一タスクへの特化);
  追加試料 P07B b8 (→追加の学習データ); フューショット P05 b1/P07B b5
  (→few-shot); 素子 P01 b1 ×2 (→ユニット); まだら P09 b7 (→混在).

## 4. Pass C — full-text read

All 16 packages + synthesis + boundaries read in r4 bytes. No genuinely new
technical-substitution failure found beyond §3.4; therefore no map addition in
r4 (map-first rule had nothing to trigger). Considered-but-rejected items
(例 chains, 装置, literal 箱, non-box 枠, Architecture-owned 四極,
axis-defined 極, 鎖/家系-lineage/芸/手足と目/水増し-inflation/写し-ordinary/
指し示し/素子-established-unit-sense/追加試料-ordinary) documented with
rationale: ordinary/clear-in-context or Architecture-owned vocabulary, no
map/Sol authority to change.

## 5. Preserved gains + integrity

Zero duplicates; no padding; r1–r3 lexicon gains intact; boundary sets unchanged
(53 EXPLICIT concise Japanese + 104 OMISSION); evaluator roles explicit;
P07B grouped, P09 protocol-bound, P15 synthesis-led; G01–G06/PARTIAL semantics
intact; no cross-task ranking; packages byte-identical; no new research.

Terminal QA state: `TS-003_LANGUAGE_QA_R4_COMPLETE / PASS_WITH_NOTES`
