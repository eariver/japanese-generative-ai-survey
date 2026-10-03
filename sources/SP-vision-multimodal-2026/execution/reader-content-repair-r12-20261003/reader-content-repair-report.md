# TS-003 r12 Bounded Content Repair — Repair Report

- Date: 2026-10-03 JST
- Authority: `EXECUTION_AUTHORITY / R11_INDEPENDENT_REVIEW_REQUEST_CHANGES / BOUNDED_CONTENT_REPAIR / STOP_BEFORE_TEX`
- Branch (existing only): `special/vision-multimodal-2026-work`
- Basis: independent review `REQUEST_CHANGES` on r11 (depth improved, Architecture frame holds; bounded repair only, no re-research, no rewrite)
- Terminal: `FRESH_CONTENT_REVIEW_REQUIRED` (READER_JSON_ONLY, no TeX/PDF)

## 1. Start guard (read-only, pre-write)

- Expected HEAD `ba99868603a5a795ba56443d9a0f8b6de9f51e62` — remote HEAD MATCH
- Expected tree `e9027328e1e8c6ddd3a8fc24ec81056323d74fd0` — remote tree MATCH
- Local HEAD identical, clean tree. No new branch created.

## 2. Authorities read (§3)

architecture-v2.json; r11 reader JSON (146 blocks) + r11 coverage (124 nodes) + r11 execution report; r10 reader JSON; P01–P15 draft packages + draft results; stored Evidence results (111 files indexed; every cited triple machine-verified); drafting-language-policy-ja.md; drafting-terminology-map-ja.md (binding); Sol draft reviews r1–r9 (principles). r10/r11/checkpoints never overwritten.

## 3. Semantic integration per package (§5 + §16A)

Principle applied: `existing useful explanation + new mechanism detail − semantic duplication = one coherent treatment`. Same proposition stated once; comparison/taxonomy frames kept only where they do not exist elsewhere. 11 targeted deletions (each with proposition-retention mapping below); no blanket deletion.

| Pkg | before | after | merged / repaired | removed dups | retained uniques |
|-----|--------|-------|-------------------|--------------|------------------|
| P01 | 4 | 4 | — (cap, untouched) | — | — |
| P02 | 9 | 7 | b2/b4/b7 replaced (RPN/objectness/anchors/NMS fix, DETR causal split, DINO-detector consolidation) | b8 (all props in new b4), b9 (100% restatement of b5) | b5 full YOLO-World exhibit; b7 reference-point synthesis |
| P03 | 7 | 7 | b7 rewritten to challenge-frame + pointer; b3 算法→アルゴリズム | — | b6 three-level table; b4 exhibit + handoff |
| P04 | 5 | 5 | — (cap, untouched) | — | — |
| P05 | 11 | 8 | b6 文字の理論→光学文字認識の一般理論 / 設計の選び→設計上の選択 | b8/b9/b10 (verified zero-unique-proposition subsets of b1/b2/b3; b10 fencing ≈ b3 subordination) | b1/b2/b3 full exhibits incl. author detail, Qwen retrieval, handoff |
| P06 | 8 | 8 | b3/b7 teacher-network fix; b4/b5/b8 SigLIP2 lineage confirmed (hedge excised incl. P06-boundaries) | — | b7 three-way taxonomy (unique frame) |
| P07A | 6 | 6 | b1/b5 CLIP contrastive-correspondence fix; b5 trimmed (ResNet/30+ → b1 only); b6 rewritten to variant-pointer | — | b3 ALIGN exhibit; b6 variant position |
| P07B | 16 | 16 | — (wording-level; §5 keep-list preserved: MLM/ITM/grounding split, ViLD≠RegionCLIP, GLIP classifier→phrase, fusion depths, vocab supervision, distillation, web self-training, segmentation branch) | — (r11 exact-dup removal already applied) | all r11 mechanism unpacks |
| P08 | 9 | 8 | b4/b9 LLaVA stage fix (vision always frozen; LLM-update axis vs MiniGPT-4); b9 trimmed to condition-labels + Molmo pointer; b5 lineage-line + 選び方 fix | b7 (100% restatement of b1) | b5 Molmo exhibit; b8 three-interface contrast |
| P09 | 12 | 12 | — (LIMIT sentences retained; PARTIAL kept, see §5 gaps) | — | DeepStack/MRoPE, joint-paradigm axis, TM-RoPE sync, Molmo2 comparator + explicit gap statements |
| P10 | 7 | 6 | b5→ordering discipline rewrite; b6→standard + composite-discipline rewrite | b7 (MMMU-head→b1, MMBench/MathVista→b3, 四者→b3 closing; zero uniques) | b1/b2/b3 exhibits; b5 order rule + numerical-scope; b6 composite discipline |
| P11 | 8 | 8 | — (r11 trims stand) | — | referred-context vs breadth; streaming contract |
| P12 | 7 | 5 | b3 transfer kept + 言い当て→特定; b4 言い当て fix | b6 (strict subset of b2), b7 (specs→b3, thesis→b4; 100% restatement) | b1/b2/b4 exhibits; b3 grounding + transfer |
| P13 | 11 | 10 | b2 vocab-unification guard; b6 embodiment fix (埋め込み→エンボディメント実機評価); b11→D097-only two-stage lens; b9→contrast-only trim | b10 (all props in b2/b4/b5) | b1/b3/b4/b5 exhibits; b7 synthesis; b9 contrast frame; b11 dependence lens |
| P14 | 10 | 9 | b9/b10 separation fixes (return≠world-model target; controllability as consequence); b3 言い当て→予測 + record-bundle folded in; b1/b2/b5/b6 §10 fixes | b8 (bundle folded to b3; rest in b3) | b1/b2/b4/b5/b6 exhibits; b6 four-pole table; non-ancestry guard |
| P15 | 16 | 16 | b9→pure gap declaration (refs legitimately empty); b13→evaluation-contract taxonomy (rewritten, not spec recital); b16→capability/architecture split rewrite; b5→P12 cross-package binding + 特定 fix | — | b1–b4/b6–b8/b10–b12/b14/b15 exhibits; b12 checklist; b15 attribution |

Net: 146 → 135 blocks; 72,337 → 67,334 chars (−5,003 from duplication removal; depth propositions retained).

## 4. Technical correction matrix (§6)

- CLIP (p07a-b1/b5): issue = generative-caption-prediction wording. Source = arXiv:2103.00020 abstract (predicting which-caption-goes-with-which-image) + Evidence 20d1ebc2. Repair = dual-encoder contrastive correspondence; captioning-vs-contrastive distinction kept. Refs unchanged. Remaining: bag-of-words limit stays as P07B motivator.
- LLaVA (p08-b4/b9 + p08-b5 lineage line): issue = vision-encoder end-to-end misstatement. Source = arXiv:2304.08485 §4.2 (S1 vision+LLM frozen→projection only; S2 vision frozen→projection+LLM) + Evidence 48f42e29. Repair = per-stage frozen/trainable axes; MiniGPT-4 contrast on LLM-update axis. Refs unchanged. Remaining: none (85.1/92.53 kept in b4 as primary carrier).
- DINO (p06-b3/b7): issue = 教師モデルなし obscuring teacher network. Source = arXiv:2104.14294 abstract (self-distillation with no labels; momentum teacher exists) + Evidence 9dce7c29. Repair = labels-vs-network distinction explicit. Remaining: none.
- RT-1 (p13-b2): issue = language-vocabulary unification pre-emption + 吸い上げ. Source = arXiv:2212.06817 abstract (no tokens/vocabulary) + Evidence b57c9615 claim-2 (tokenized-trajectory conditioning kept, fenced). Repair = conditioning-only wording + 取り込んだ/学習に用いた. Remaining: policy-mechanism detail stays RT-2-side per Evidence limitation.
- RT-2 (p13-b5 KEEP, p13-b11 lens): formulation verified against arXiv:2307.15818 abstract + Evidence ea37cef9. No overreach beyond RT-2's own record. Remaining: deployment scope stays endpoint-side.
- OpenVLA (p13-b6): issue = 埋め込み評価 (embedding lad for embodiment). Source = arXiv:2406.09246 abstract (multiple robot embodiments) WINS over Evidence claim text '29 tasks/embeddings' (defect recorded; canonical Evidence repair filed as follow-up need, reader not blocked). Repair = 29課題・複数の機体（エンボディメント）にわたる実機評価 + オープンウェイト normalization. Remaining: G01 scarcity kept.
- DreamerV3 (p14-b10): issue = return as world-model target. Source = Evidence a6411d38 (RSSM + imagination policy improvement; return-gains pole). Repair = world-model side vs behavior side split; 算法→アルゴリズム. Remaining: continuation omitted (not in Evidence).
- Genie (p14-b9): issue = 操作可能性 as prediction target + 潜ませ/言い当て. Source = Evidence 8025f5dd (latent-action imitation). Repair = objective/conditioning/generation/representation/controllability-as-consequence split. Remaining: latent-action extraction internals still gap (PARTIAL kept).
- Faster R-CNN/RPN (p02-b2/b7): issue = 物の輪郭. Source = arXiv:1506.01497 abstract (objectness + bounds per position) + Evidence 2ca2b01d. Repair = objectness/anchors/offsets wording; 代表値→アンカー配置, 後始末→NMS重複除去. Remaining: training breakdown still gap (PARTIAL kept).
- DETR (p02-b4): issue = self-attention causality assertion. Source = arXiv:2005.12872 abstract (silent on APL/APS cause) wins over Evidence claim-2 gloss. Repair = result/interpreta
...[truncated 4471 chars]