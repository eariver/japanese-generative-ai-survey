# TS-003 Sol Draft Review r8

Status: `SOL_DRAFT_REVIEW_R8 / REQUEST_CHANGES / FINAL_MICRO_CLEANUP`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft r8 worker commit:

`45e1aae18883983bfb852ac95bfd78d6a4d2fcf1`

Reviewed tree:

`d5113b2a2d58e8b016a2e3e74fc596c297625fd4`

Decision:

`REQUEST_CHANGES`

Draft r8 closes the material semantic failures found in r7 and the bidirectional terminology audit is substantially stronger. Independent Sol review found only four remaining reader-surface defects. They are narrow enough for a final micro-cleanup; no broad rewrite is authorized.

The cumulative terminology authority has been advanced to r9:

- path: `sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`
- commit: `52d8635822bce38ea9569249f3b860fa360064dd`
- blob: `cf39a5860d64b5d85a3a382911680dcadaa954a1`
- status: `DRAFT_R9_BINDING`
- terminal: `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R9_BINDING`

## 1. What passed

Independent Sol checks confirm:

- r8 worker output is one normal child of the authorized start `8aacf0c8bb403d658e38b97a0584e579f03c44b4`;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- production state remains byte-identical at `DRAFT_COMPLETE`;
- Architecture Review remains approved;
- Publication Preview remains pending;
- validation/publication_preview/freeze/release remain pending;
- all 16 canonical Draft Results are `REVISED` / `draft_version=r8`;
- Draft Packages remain byte-identical;
- exact duplicate sentence scan remains zero per package and cross-package;
- no internal production labels leak into reader prose;
- P13's non-box `ボックス` regression is fixed;
- P13 lineage `鎖` organizer is fixed;
- non-P14 `極 / 両極` organizers targeted by r8 are fixed;
- P09 boundary now uses `音声認識` while preserving the speech-vs-general-audio distinction;
- canonical synthesis no longer contains `部品 / 橋 / 橋渡し`;
- all remaining `ボックス` hits checked by Sol are actual box/bounding-box semantics;
- remaining `鎖` hits are ordinary `連鎖` or technical `共参照鎖`;
- remaining `極` hits are ordinary adjective/adverb or the Architecture-approved P14 four-pole classification.

These passes do not override the four residual findings below.

## 2. Blocking F1 — backbone is still translated as 背骨

Canonical P03 b1 says:

`拡散の背骨としての来歴はTS-002の範囲として本書では扱わない。`

This is a technical backbone concept.

The Terminology Map already defines:

`encoder / decoder / backbone -> エンコーダ / デコーダ / バックボーン`.

Required repair:

`拡散モデルのバックボーンとしての来歴は…`

or another meaning-preserving direct form.

This is a direct preferred-form miss.

## 3. Blocking F2 — tight/deep fusion metaphor remains in P07B

Canonical P07B b6 says:

`特徴増強と言語誘導クエリ選択とcross-modalityデコーダの三段で固く混ぜる。`

The cumulative registry already prohibits the same class:

- `固い混ぜ`;
- `固い融合`;
- technical fusion rendered through mixing metaphors.

Required repair must state the actual mechanism directly, e.g.:

`特徴増強、言語誘導クエリ選択、cross-modalityデコーダの三段階で密に融合する。`

Use the exact source-supported relationship.

Do not replace `固く混ぜる` with another mixing metaphor.

## 4. Blocking F3 — technical adaptation is still expressed as 渡す

Canonical P07B b6 also says:

`構成を足さず、学習手順で検出に渡す。`

This is not ordinary handoff prose; it describes adapting the pretrained model to detection.

Required direction:

- `追加モジュールなしで検出へファインチューニングする`;
- `学習手順のみで検出へ適応する`;

or another source-accurate direct technical formulation.

This is the same class as the previously prohibited technical `渡し` wording.

## 5. Blocking F4 — punctuation regression in P15

Canonical P15 b7 contains:

`マルチモーダルの代表例で、、文と画像と音声と動画を入力し…`

The double Japanese comma is a reader-facing copy defect introduced by the r8 repair.

Required repair:

`マルチモーダルの代表例で、文と画像と音声と動画を入力し…`

No substantive wording change is required.

## 6. Non-blocking observations

The following are acceptable and must not be blindly changed:

- heuristic `近道` in `抜き出しの近道 / 言語先行の近道`;
- learning/procedure `第一段階 / 第二段階 / 二段階`;
- technical `共参照鎖`;
- ordinary causal `連鎖`;
- P14 Architecture-defined `四つの極 / 四極`;
- ordinary `極端 / 極めて`;
- ordinary `混ぜる` when literally comparing or combining evaluation conditions rather than naming a fusion mechanism;
- ordinary narrative `渡す` when not used as the technical name of adaptation/transfer.

## 7. Required r9 scope

Draft r9 is a four-edit micro-cleanup.

Authorized reader-text changes:

1. P03 b1 backbone wording;
2. P07B b6 fusion wording;
3. P07B b6 detection-adaptation wording;
4. P15 b7 punctuation.

Canonical synthesis should remain textually unchanged unless regeneration metadata requires hash updates.

Other package prose must remain textually identical to r8.

No new research, sources, evidence, selection, architecture, or substantive claim changes.

Draft Packages remain byte-identical.

## 8. r9 acceptance criteria

Before returning to Sol:

1. no technical backbone sense `背骨`;
2. no fusion-mechanism `固く混ぜる / 固い混ぜ / 固い融合`;
3. no P07B technical adaptation `検出に渡す`;
4. no duplicate punctuation `、、 / 。。 / ，， / ,,`;
5. all r8 bidirectional terminology passes remain intact;
6. exact duplicate sentences remain zero;
7. no re-padding;
8. source roles, Evidence refs, CLAIM_BOUNDARY semantics, G01-G06/PARTIAL semantics unchanged;
9. publication candidate r1 remains stale and untouched;
10. Core checkpoint-staleness remains untouched;
11. production state remains byte-identical at `DRAFT_COMPLETE`;
12. no publication regeneration, stage validation/advance, Human Preview, Freeze, or Release.

## 9. State boundary

Terminal:

`TS-003 DRAFT_R8_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R9_FINAL_MICRO_CLEANUP_REQUIRED`

`PUBLICATION_CANDIDATE_R1_REMAINS_STALE`

`CORE_CHECKPOINT_STALENESS_UNCHANGED`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
