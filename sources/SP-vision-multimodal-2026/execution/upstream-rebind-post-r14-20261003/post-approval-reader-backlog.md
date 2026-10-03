# Post-approval reader repair backlog (recorded, NOT executed — §14–§17)

To be executed only after fresh Human Architecture Review approves the v4 (or later) Architecture. No r15 created this turn. r14 stays the historical candidate.

## P11 — Something-Something V2 → V1

- r14 P11 sentence: `Something-Something V2は順序に敏感な前例である。` (+ `10万超の動画に174種の文型…ICCV 2017` context, already V1-correct, keep)
- Repair: one-token substitution `V2→V1` only. Same for coverage technique label, TeX, references.bib vmd084 title.

## P02 — DETR assignment cost → matching → training loss

- Rewrite per r8 Evidence (matching costs → Hungarian assignment → matched-pair NLL+L1+GIoU loss; aux as standard recipe, never mandatory).

## P12 — 318 tool calls condition binding

- Bind `Claude Opus 4.7 + maximum thinking + single-action` to the 318.4 average (108 tasks); keep 20.6/54.8 bound to `Opus 4.8 + max thinking + batched + 500 steps` (481.8 calls); do not present 318 as generic task complexity.

## P13 — OpenVLA / RT-2 causal ceiling

- OpenVLA: drop `小さくても届く` generalization; ceiling = 7B beats 55B RT-2-X task success under the 29-task multi-embodiment eval conditions.
- RT-2: no necessity-claims (`Web knowledgeがなければgeneralizationできない` forbidden); ceiling = co-fine-tune report.

## P14/P15 — Genie 3 / SIMA sync to new Evidence

- Replace `SIMA-agent training` readings with r8 scope (executed compatibility test; goal-unaware simulation from actions).

## P09 — living repository claims

- Add commit/tag, access date, immutable release identifiers to living-repo claims where source supports.

## P01 — Option B (no Architecture change)

- Cut 2 DeiT/Swin body sentences in p01-b2 + 1 concrete clause in p01-b3; append P06-deferral boundary sentence (exact texts in upstream-rebind report record); body refs stay package-local; boundary LIMITATION refs only.

## Future dedup (all packages, mechanism-first ordering)

- P03/P05/P06/P07A/P08/P09/P10/P11/P14/P15: first occurrence = mechanism + evidence + limitation; later = comparison/transition/synthesis only. Remove `前段の記録のとおり`-while-restating paragraphs.

## Future terminology batch

- 戻す目的関数→再構成目的/再構成損失; 一対判定→pairwise sigmoid loss/ペアごとのシグモイド損失; 伸ばせる潜在行動モデル→scalable latent action model/スケーラブルな潜在行動モデル; 受け側→入力側/入力処理系; 対応の密さ→dense alignment/密なアラインメント; 指し示す力→grounding能力/空間グラウンディング能力; 一コマ→1フレーム.
