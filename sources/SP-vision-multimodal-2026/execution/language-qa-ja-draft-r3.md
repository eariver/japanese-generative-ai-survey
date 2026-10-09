# TS-003 Language QA r3 — cumulative terminology repair

Status: `PASS_WITH_NOTES / MAP_R3_APPLIED / SOL_R3_PENDING`

Date: `2026-10-02`

Authority: `execution/drafting-terminology-map-ja.md`
(starting blob `37bfd73c838bde51a170572989e73166df5dfb51`,
status `DRAFT_R3_BINDING`,
terminal `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R3_BINDING`).

Scope: all 16 r3 Draft Results (headline + deck + PARAGRAPH + CLAIM_BOUNDARY) +
profile synthesis payload. Reader text ~52.5k chars.

## 1. Exact duplicate sentences (§7 acceptance)

Per package: P01 30/0, P02 39/0, P03 30/0, P04 30/0, P05 90/0, P06 74/0,
P07A 53/0, P07B 135/0, P08 64/0, P09 103/0, P10 44/0, P11 70/0, P12 53/0,
P13 77/0, P14 80/0, P15 121/0 (sentences/duplicates). Cross-package repeats: 0.
r2 zero-duplicate gain preserved; no re-padding (52.2k → 52.5k chars, delta is repairs only).

## 2. Pass A — preferred/avoid conformance (map §§1–2, all rows)

Scanned headline/deck/PARAGRAPH/CLAIM_BOUNDARY/synthesis per row; hits classified:

- grounding/alignment/perception/reasoning/detection/recognition: kept distinct
  (P07A zero 接地; P12 grounding-vs-task separation intact).
- segmentation: 16 セグメンテーション-family uses present; 8 segmentation-substitute
  uses repaired (P01 deck, P03 deck/b1/b2/b3/b4). Remaining 切り分け hits are
  ordinary distinguish/separate senses (§0.2: P06 b5, P07A deck, P07B b2/b9,
  P09 b2, P10 all, P12 all, P15 b3) or short-clip senses (P11) — ORDINARY_JAPANESE_ALLOWED.
- benchmark/evaluation, World Model/predictive representation, capability/evidence,
  architecture/deployment: distinct. deployment standardized to デプロイ (7 uses;
  2 boundary 配備 repaired).
- multimodal: 9 マルチモーダル; 4 多様式 repaired (P09 b1/b2, P11 b3).
- teacher/student: 17 教師モデル, 3 生徒モデル, 22 教師信号; 19 教員 + 3 生徒
  repaired (P06 b1/b3, P07B b2/b3/b9 + boundary). No school personification remains.
- post-training: ポストトレーニング present; 1 事後学習 repaired.
- hallucination: 8 ハルシネーション; 3 幻覚 + 1 幻のふるい repaired (P15 b3, P10 b3).
- code: コード-family present throughout; 13 code-sense 符号 repaired
  (P08 b3/b4/b5, P09 b2/b4/b6/b7, P10 b2, P11 b3/b4). Encoding 符号化 untouched.
- interface/input: インターフェース/入力側 present; 2 受け口 repaired.
- masked reconstruction: マスク再構成 present; 1 当て戻し repaired.
- trajectory (軌道), RL policy (方策), repository (リポジトリ), model card
  (モデルカード), checkpoint-release katakana (検査点の変換 etc.): conforming.

## 3. Pass B — known-failure regression audit (map §3)

- §3.1 r1 registry: zero TECHNICAL_SUBSTITUTION hits in r3 (網/処方/証し/躾/構え/
  運ぶ/棚/凱歌/土俵/物差し/顔つき/段取り/宿題/持ち場/見取り図/務め/模型 all 0,
  including the 3 boundary 物差し and boundary 仕事 introduced by the r2 repair itself).
- §3.2 r2 registry: all Sol-flagged items repaired (list in §5); 枠 hits are
  枠組み/クエリ枠/共通の枠/枠数 senses only — ORDINARY_JAPANESE_ALLOWED
  (map Avoid covers 枠 as box-substitute; no box-sense 枠 exists).
- 極: P14 四極 is Architecture-mandated vocabulary (map §7 keeps it); remaining
  極 uses (P03/P05/P13/P15) name explicit axes — ORDINARY/DEFINED, noted.
  Only 配りの極 (registry-listed) repaired.

## 4. New failures found in Pass C → map updated FIRST (§3.3 added)

| Failure | Concept | Repair | Hits |
|---|---|---|---|
| encoder-sense 目 | vision encoder | 視覚エンコーダ/エンコーダ | 6 (P06 b4/b5, P14 b4) |
| データ管/較正の配管 | pipeline | データパイプライン/パイプライン | 2 (P06 b3, P04 b4) |
| 多作物 | multi-crop | マルチクロップ | 1 (P06 b3) |
| 汎用手 | general-purpose model | 汎用モデル | 1 (P13 b3) |
| 早い/遅い/固い融合 variants | early/late/tight fusion | 早期融合/後段融合/密な融合 | 6 (P07B b5/b6/b9) |

All occurrences repaired; re-audit confirms zero residue. No new-synonym
replacement used anywhere (concept-level repair per §3.4 regression principle).
Ordinary 目/管 senses (見た目、目の前、管理) untouched per §0.2.

## 5. Sol r2 finding closure mapping

- F1 map violations: 多様式4, 事後学習1, 幻覚3, segmentation-paraphrase 8,
  boundary 配備2 → all repaired. 切り分け retained only in ordinary senses.
- F2 teacher/student: 22 hits → 教師モデル/生徒モデル/教師信号.
- F3 code/受け口/当て戻し/袋詰め: 13 + 2 + 1 + 4 → コード/入力側/マスク再構成/
  画像全体のアライメント + direct compositional explanation.
- F4 metaphors: 契約の家, P07B b9 closing (語彙の足し/遅い渡し/固い混ぜ/
  規模の回し/レア側の埋め + fusion variants), 幻のふるい, 投票の素描/
  二言語の輪切り, 配りの極, 錨4, 値打ち1 → all rewritten directly.
- F5 QA process: this report is the repaired process (map-driven Pass A/B/C,
  full-text read, sentence-level evidence for every claim).

## 6. Considered but not repaired (with rationale; non-blocking notes)

- 例 chains (P04 etc.), 装置, 箱 (literal, consistent), 枠 (non-box senses),
  鎖/家系/第二の家/芸/手足と目/まだら/追加試料/各周/水増し/写し/指し示し/素子/
  フューショット, P14 収益の極 + この極の位置 phrasing, P13 一つの芸,
  P01 著者公開PDF wording, P07B チェックポイント (model-checkpoint katakana):
  ordinary/clear-in-context or Architecture-owned vocabulary; no map/Sol authority
  to change; changing them would risk churn without a failure basis.

## 7. Preserved r2 gains (§7)

網 absent; zero duplicates; no padding (52.5k chars); Japanese boundary blocks
(53 EXPLICIT concise + 104 OMISSION, sets unchanged); evaluator roles explicit;
P07B grouping; P09 protocol-bound comparisons; P15 density. G01–G06/PARTIAL
semantics intact; no cross-task ranking; no new research.

Terminal QA state: `TS-003_LANGUAGE_QA_R3_COMPLETE / PASS_WITH_NOTES`
