# TS-003 Sol Draft Review r7

Status: `SOL_DRAFT_REVIEW_R7 / REQUEST_CHANGES / BIDIRECTIONAL_TERMINOLOGY_BINDING_REPAIR`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed worker commit:

`59f841121271d68154f9173d0826791215b261d4`

Reviewed tree:

`d57d7e028fd316926fb63716c2e43d896a5a3638`

Worker QA:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r7.md`

Worker report:

`sources/SP-vision-multimodal-2026/execution/draft-r7-20261002/draft-r7-review-report.md`

Decision:

`REQUEST_CHANGES`

Draft r7 is materially improved and closes most of the terminology defects found at publication candidate r1. It does not yet pass Sol review because independent semantic review found residual violations and one blind-replacement regression that the worker QA incorrectly classified as closed.

The cumulative terminology authority has therefore been updated for Draft r8:

- path: `sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`
- commit: `017ba7b8475fa45505fff7e57a3bf2a0e3e26bcb`
- blob: `fcc0c6224ac400a3f0f3ba42016d66190a67bfc9`
- status: `DRAFT_R8_BINDING`
- terminal: `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R8_BINDING`

## 1. What passed

Independent Sol checks confirm:

- work branch started from the exact authorized r7 start and worker output is one normal child commit;
- worker commit: `59f841121271d68154f9173d0826791215b261d4`;
- worker tree: `d57d7e028fd316926fb63716c2e43d896a5a3638`;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- lifecycle remains `DRAFT_COMPLETE`;
- Architecture Review remains approved;
- Publication Preview remains pending;
- validation/publication_preview/freeze/release remain pending;
- canonical Draft Packages were not modified;
- all 16 canonical Draft Results report `REVISED` / `draft_version=r7`;
- exact duplicate scan independently returns 0 per package and cross-package;
- no internal G01-G06/PARTIAL/SELECTED/checkpoint/stage labels were found in normal reader prose;
- the major r7 targets were repaired: technical `箱`, open-vocabulary paraphrases, decoder/calibration/scaling/open-weights, Q-Former query, attention, one-stage/two-stage, feature map, dual encoder, MoE, cold start, model checkpoint, trainable parameters, model variants, categories, masked labels, and most architecture-component wording.

These passes do not override the residual findings below.

## 2. Blocking F1 — blind preferred-term replacement created wrong semantics

The most important r7 regression is in P13.

Canonical r7 contains:

`見ることと考えることを別のボックスに閉じ込めず、一つの文の続きとして扱い…`

and:

`見ることと動かすことの間に別のボックスを置かず、一つのモデルで受けて出す。`

These are **not bounding boxes**.

The original metaphorical container word was mechanically changed to the preferred token `ボックス`, even though the underlying concept is subsystem separation / intermediate architecture boundaries.

This violates both:

- the no-blind-global-replacement rule;
- the preferred-form semantic rule.

Required repair must name the actual architecture relation directly, for example:

- `視覚と推論を別系統に分離せず…`;
- `視覚入力から行動出力までを一つのモデルで扱う…`.

Do not replace `ボックス` with another metaphor.

## 3. Blocking F2 — P13 lineage-chain metaphor remains

P13 b7 still begins:

`鎖を通して見ると、表現と行動の界面が段階を追って変わった。`

The r7 contract explicitly required repair of:

- `一本の鎖`;
- `鎖のなか`;
- equivalent lineage-chain wording.

This is the same prohibited organizer.

Required repair:

`この系譜を通して見ると…`

or an equally direct staged-progression formulation.

The following `鎖` occurrences are not part of this failure:

- `共参照鎖` as a technical coreference concept;
- ordinary causal `連鎖`.

## 4. Blocking F3 — non-P14 “極” metaphors remain as technical organizers

The cumulative anti-metaphor rule allows the Architecture-defined P14 `四つの極` as an explicit exception.

Independent r7 review found several **non-P14** uses where `極` still replaces a direct technical classification:

### P03

`ボックスなしの密な極はFCNやSAM側の資料に譲る。`

Also repeated in P03 CLAIM_BOUNDARY.

Required direction:

`ボックスに依存しない密な予測はFCNやSAM側の資料に譲る。`

### P05

`GOTはOCR-2.0という理論を掲げる特化型のもう一極である。`

Required direction:

`GOTは…別系統の特化型モデルである。`

### P07B

`融合の両極は、後段の最小構成と密な統一である。`

Required direction:

`融合方式は、後段融合の最小構成と密な融合に分かれる。`

### P13

`OpenVLAはオープンウェイトで確かめられる極だ。`

Required direction:

`OpenVLAはオープンウェイトで検証可能なVLAの事例である。`

### P15

`Gemini 3.1 Proは100万のコンテキストをもつ当初からのマルチモーダルの極で…`

Required direction:

state the model role directly, e.g. a native-multimodal / long-context capability example, without the `極` metaphor.

Do not change:

- `極端な不均衡`;
- `極めて長い`;
- P14's approved four-pole classification.

## 5. Blocking F4 — P09 boundary still uses the nonpreferred speech label

The r7 QA table reports:

`label話し言葉 0`

but canonical P09 CLAIM_BOUNDARY contains:

`Whisperの話は話し言葉の範囲に留まり、音全般の主張はしない。`

This sentence is explicitly setting the scope of Whisper/ASR, so it is a technical scope label, not incidental ordinary prose.

Required repair:

`Whisperの話は音声認識の範囲に留まり、音全般の主張はしない。`

or an equally precise speech/ASR formulation.

The underlying scope distinction must be preserved: speech/ASR != general audio.

## 6. Blocking F5 — canonical profile synthesis was not semantically repaired

The r7 execution contract explicitly required preferred-form audit over:

`all 16 Results + synthesis`.

The worker report states:

`Synthesis changes: None`.

Canonical `profile-synthesis-result.json` still contains:

`個別学習済み部品の橋渡し`

and:

`個別部品の組み立て`

These directly violate the already binding component/bridge rules.

Required repair must say what the architecture relation is, e.g.:

- separately pretrained components/modules are connected;
- modular composition;
- integration of independently pretrained components.

Do not preserve `部品` or `橋渡し` as technical organizers.

P14's Architecture-defined four-pole concept may remain in synthesis only if it is clearly and correctly referring to that approved classification.

## 7. Blocking F6 — r7 QA overstates closure

The r7 QA claims:

- full Section-2 conformance;
- zero blocking registry hits;
- component/bridge repair complete;
- technical speech-label repair complete.

Those claims are contradicted by canonical bytes.

Therefore the next QA must be **bidirectional**:

1. concept -> preferred term;
2. preferred term -> correct concept.

The P13 `ボックス` regression demonstrates why this is necessary.

A scan that finds every `箱` replaced does not pass if a non-box metaphor has been turned into `ボックス`.

The QA must also scan the canonical profile synthesis result with the same strictness as packages.

## 8. Non-blocking observations

The following remaining hits are contextually acceptable and should not be blindly rewritten:

- `抜き出しの近道`, `言語先行の近道`: heuristic shortcut, not ResNet shortcut connection;
- `第一段階 / 第二段階 / 二段階`: learning/procedure stages, not detector architecture labels;
- `共参照鎖`: established technical relation;
- `極端`, `極めて`: ordinary adjective/adverb;
- P14 `四つの極`: approved Architecture-defined exception;
- ordinary `土台になる` where it is not naming a foundation/base/backbone concept.

## 9. Required r8 scope

Draft r8 is a **small, bounded semantic terminology cleanup**.

No new research.

Do not change:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval;
- Draft Packages;
- factual claims;
- source/evaluator attribution;
- comparison protocols;
- CLAIM_BOUNDARY meaning;
- G01-G06/PARTIAL meaning;
- page/depth strategy.

Repair only the residual reader wording identified above plus any exactly equivalent residual discovered by the required audit.

The stale 38-page publication candidate remains stale.

Do not regenerate PDF/publication in r8.

The shared Core checkpoint-staleness issue remains separate and untouched.

## 10. r8 acceptance criteria

Before returning to Sol:

1. no non-bounding-box use of `ボックス`;
2. P13 lineage `鎖` organizer eliminated;
3. non-P14 technical-organizer `極 / 両極` eliminated;
4. P09 boundary uses `音声 / 音声認識` for the technical scope;
5. profile synthesis has no component/bridge metaphor residue;
6. full bidirectional Section-2 audit over all 16 Results + canonical profile synthesis result;
7. every remaining `ボックス` semantically confirmed as bounding-box/box concept;
8. every remaining `極` classified, with only ordinary adjective/adverb or P14-approved classification allowed;
9. every remaining `鎖` classified, with P13 lineage usage absent;
10. full cumulative known-failure registry re-audited;
11. zero exact duplicates remains true;
12. no new synonym/metaphor introduced;
13. no padding;
14. production state remains byte-identical at `DRAFT_COMPLETE`;
15. no stage validation/advance;
16. no Human Preview/Freeze/Release.

Terminal:

`TS-003 DRAFT_R7_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R8_BIDIRECTIONAL_TERMINOLOGY_REPAIR_REQUIRED`

`PUBLICATION_CANDIDATE_R1_REMAINS_STALE`

`CORE_CHECKPOINT_STALENESS_UNCHANGED`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
