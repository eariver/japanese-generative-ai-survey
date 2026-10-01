# TS-003 Sol Draft Review r3

Status: `SOL_DRAFT_REVIEW_R3 / REQUEST_CHANGES / RESIDUAL_TERMINOLOGY_AND_READER_SURFACE_REPAIR`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft r3 authority commit:

`5e16392d84956b70ee4192657918feb4c4ead265`

Reviewed tree:

`0f4b1d3c4f36d911355ed3991ce9416847a79293`

Decision:

`REQUEST_CHANGES`

Draft r3 is materially improved and closes the previously known r1/r2 terminology failures. However, independent Sol review found additional over-domestication / technical-term substitution patterns that the r3 Worker QA classified as non-blocking or did not classify at all. The cumulative terminology authority therefore required another update before the next drafting execution.

The cumulative map has been updated after this review at commit:

`324d7d7933db2b61c7712b48006480d9b20f6638`

Map blob:

`d17d04e3574a33a263f7f10738a601471f6b095d`

Terminal map state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R4_BINDING`

## 1. What passed

- r3 launch guards matched the authorized start.
- main remained `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`.
- Frozen Core remained `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- lifecycle remains `DRAFT_COMPLETE`.
- Architecture Review remains approved; Publication Preview remains pending.
- validation/publication_preview/freeze/release remain pending.
- all 16 canonical Draft Results are r3 / REVISED.
- exact duplicate sentence scan independently confirms zero duplicates in all 16 packages.
- previously known r1/r2 blocking forms are absent from canonical r3, including:
  - neural-network `網`;
  - `多様式 / 多模式`;
  - `教員 / bare 生徒`;
  - technical `幻覚`;
  - post-training `事後学習`;
  - source-code `符号`;
  - `受け口`;
  - `当て戻し`;
  - `袋詰め`;
  - `契約の家`;
  - `語彙の足し`;
  - `遅い渡し`;
  - `固い混ぜ`;
  - `規模の回し`;
  - `レア側の埋め`;
  - `幻のふるい`;
  - `投票の素描`;
  - `二言語の輪切り`;
  - `配りの極`.
- r3 correctly added and repaired new failures discovered during its own Pass C:
  - encoder-sense `目`;
  - `データ管 / 較正の配管`;
  - `多作物`;
  - `汎用手`;
  - `早い/遅い/固い融合`.
- preferred forms are present, including `教師モデル`, `生徒モデル`, `マルチモーダル`, `ポストトレーニング`, `ハルシネーション`, `セグメンテーション`, `デプロイ`, `マルチクロップ`, `パイプライン`.
- no internal workflow labels leak into ordinary reader prose.
- P07B/P09/P15 structural improvements remain intact.
- no new research was performed.

These passes do not override the residual blocking findings below.

## 2. Blocking finding F1 — technical segmentation is still rendered as 分割

The r3 QA says the segmentation family is repaired, but P07B still uses `分割` as the technical name of segmentation in multiple places, including:

- deck: `自己学習と分割の機構群`;
- `定式から分割までの六群`;
- `開いた語彙の分割の枝`;
- `固定ラベル分割器`;
- `指示の分割`;
- `汎用分割と指示分割`;
- `パノプティック分割`;
- `分割の枝が画素と言葉の照合のまとめを示す`.

These are not dataset split/partition uses. They refer to segmentation as the computer-vision task family and therefore violate the map's load-bearing distinction.

Required repair: use the source-appropriate established terms such as `セグメンテーション`, `オープンボキャブラリーセグメンテーション`, `パノプティックセグメンテーション`, and `セグメンテーションモデル`.

Dataset split uses such as `学習分割`, `試験分割`, `レア分割` remain valid.

## 3. Blocking finding F2 — bare 測り still substitutes for metric/evaluation protocol

Reader-facing r3 repeatedly uses `測り` as a noun in places where the intended concept is an evaluation metric, evaluation protocol, or evaluation condition.

Examples:

- P07A deck: `測りの切り分けを守る`;
- P07A b2: `測りの同一性を保ち`;
- P07B b1: `三つ目の測りがLVISである`;
- P07B b1: `三つの測りは混ぜない`;
- P07B b2: `レアの測りを押し上げる`;
- P07B b5: `接地の測りは…`;
- P07B b9: `測りは契約ごとに分ける`.

This is the same class as the previously banned `物差し`: a technical evaluation concept is replaced by a short everyday metaphor-like noun.

Required repair: name the actual concept directly: `評価指標`, `評価方法`, `評価条件`, `測定方法`, `評価プロトコル` as appropriate.

Ordinary verbs such as `測る` and natural explanatory `測り方` may remain when they do not replace a technical noun.

## 4. Blocking finding F3 — evaluation/protocol language is still over-domesticated

P07A contains:

- `決めなしの数値は、意味をもたない。`
- `分割と抽出の決めを数値と組で読む。`

Here `決め` substitutes for evaluation/extraction conditions or rules. Use direct technical wording such as `評価条件`, `抽出規則`, `手順`, or `定義`.

P07B contains:

- `LVIS-rare APをOVD評価の家にし`.

This reproduces the same failure class as the r2 `契約の家`, despite the literal string having changed. Use a direct description of LVIS-rare AP's role as an OVD evaluation metric/benchmark condition.

P09 contains:

- `一つの家系だけを追わない`;
- `二つの家系で確かめる`;
- `第二の家の開放を示し`.

Where the intended concept is a model family, lineage, or repository family, use `モデル系列`, `モデルファミリー`, or `系譜`.

## 5. Blocking finding F4 — technical concepts are still replaced by everyday-language metaphors

Representative residuals include:

### data augmentation

- P03: `弾性変形の水増し`
- P06: `水増しと正則化の学習レシピ`

When the technical concept is data augmentation, use `データ拡張`. Ordinary “numerical inflation” uses of `水増し` may remain.

### scaffold

- P15: `足場のアブレーション`

The binding map already prefers `scaffold（補助的手順）`. `足場` is an over-literal everyday translation in this context.

### foundation/base/backbone

Technical uses of `土台` remain, e.g.:

- P06: `視覚の土台`, `土台の特徴`;
- P07B: `拡散土台`, `CLIP識別土台`;
- P14: `凍結した土台`;
- P15: `学習の土台の名`.

When the concept is a foundation model, base model, backbone, or base representation, use `基盤モデル`, `基盤`, `バックボーン`, or `基盤表現` according to the Evidence. Ordinary nontechnical `土台になる` is not automatically prohibited.

### source/release availability

- P13/P14/P15: `配り方`, `配りの範囲`

Where the concept is release/availability/deployment scope, use `提供形態`, `提供範囲`, `公開形態`, or `デプロイ形態`.

### single-task specialization

- P13: `一つの芸だけを磨く`

Use `単一タスクへの特化` or another direct technical description.

### evaluation axes

- P15: `別の軸の勘定`

Use a direct statement such as `別々の評価軸として扱う`.

## 6. Blocking finding F5 — opaque shorthand remains in high-value sections

Several sentences are grammatically valid but still read like compressed generated prose rather than technical Japanese.

Examples:

- P06 deck: `載せ方と組み方と式と移しを分けて読む`;
- P06 b5: repeated `載せ方 / 組み方` as unnamed technical axes;
- P07A b3: `呼びの到達の上に結びの仕組みを積む`;
- P07B b3: `教師モデルの写しの産物`;
- P09: `流れの契約`, `流れのオムニ` where the intended concept is streaming;
- P15: `軸の勘定`.

These must be rewritten with the actual technical concept, not replaced with another metaphor.

## 7. Blocking finding F6 — r3 QA overstates semantic closure

The r3 QA explicitly lists items such as `家系/第二の家`, `水増し`, `写し`, and `一つの芸` as considered-but-not-repaired and classifies them as non-blocking.

Independent Sol review disagrees for the contexts above.

The QA also says segmentation substitutes were repaired, but technical segmentation-as-`分割` remains in P07B.

Therefore r3 language QA is not yet sufficient to support publication validation.

## 8. Non-blocking observations

- P14's Architecture-owned four-pole classification (`四つの極`) may remain.
- `学習分割 / 試験分割 / レア分割` are valid dataset partition terms and must not be globally replaced.
- ordinary verb uses of `測る` are valid.
- ordinary numerical-inflation use of `水増し` is valid when it does not mean data augmentation.
- ordinary literal `家` meanings are unaffected.
- r3's total length and zero-duplicate state are acceptable; do not re-pad.

## 9. Cumulative map update

Per the cumulative-map maintenance rule, the new failures above were added to:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

at commit:

`324d7d7933db2b61c7712b48006480d9b20f6638`

with blob:

`d17d04e3574a33a263f7f10738a601471f6b095d`

and terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R4_BINDING`.

The map also records context exceptions to prevent blind replacement.

## 10. Required Draft r4 boundary

This remains a bounded Draft-only reader-surface repair.

Immutable:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Human Architecture r2 approval;
- all Draft Packages;
- source set;
- main;
- Frozen Core.

Do not perform new research.

Revise only Draft Results / synthesis / terminology QA / review report / cumulative map if genuinely new failures are discovered.

## 11. Draft r4 acceptance criteria

Before returning to Sol:

1. all cumulative-map `TECHNICAL_SUBSTITUTION_BLOCKING` hits are repaired;
2. technical segmentation uses `セグメンテーション`, not `分割`;
3. bare `測り` does not substitute for a metric/protocol;
4. evaluation/extraction `決め` is replaced by direct technical wording;
5. `評価の家 / 第二の家 / model-family 家系` are removed in technical contexts;
6. data augmentation uses `データ拡張`, not `水増し`;
7. scaffold uses `scaffold（補助的手順）`, not `足場`;
8. technical foundation/base/backbone uses no casual `土台`;
9. availability/release/deployment uses no casual `配り方 / 配りの範囲`;
10. `一つの芸`, `軸の勘定`, `呼びの到達`, `結びの仕組み`, `写しの産物`, streaming-sense `流れの契約 / 流れのオムニ`, and similar substitutes are removed;
11. new failures discovered during r4 are first added to the cumulative map, then repaired and re-audited;
12. zero exact duplicates remains true;
13. no re-padding;
14. Evidence refs, source roles, CLAIM_BOUNDARY semantics and G01-G06/PARTIAL limitations remain intact;
15. no reader-publication validation / Publication Preview / Freeze / Release.

## 12. State boundary

Current `DRAFT_COMPLETE` remains valid.

Terminal target:

`TS-003 DRAFT_R3_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R4_CUMULATIVE_TERMINOLOGY_REPAIR_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R4`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
