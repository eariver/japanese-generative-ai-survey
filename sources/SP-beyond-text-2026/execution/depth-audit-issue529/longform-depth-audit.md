# TS-002 Issue-#529 LONGFORM depth audit

Authority: GitHub Issue #529 + Sol execution-boundary comment; LONGFORM_SPECIAL reader-depth bar (TS-001-comparable). Prior r2 classes NOT auto-inherited.

## Counts

- BOUNDARY_LIMITED: 7
- EVIDENCE_BLOCKED: 3
- LONGFORM_SUBSTANTIVE: 33

## EVIDENCE_BLOCKED (reported to Sol, not filled by inference)

### T-PAR-06
SDE脚は実質的(時間依存得点網・予測子修正子・確率流ODE適応積分+厳密尤度・無条件得点からの条件生成、1000-2000評価費用の代償、流れ整合への継承)。EDM脚は要旨水準の framing(部品化・35評価)のみで、要求される設計空間深度(前処理/日程/解法の内訳ablation・backbone対目的分離)の本文典拠が不在。不足典拠=EDM full body(Karras et al. 2022, arXiv:2206.00364 のpreconditioning/schedule/solver ablation)+BT-D ID: BT-D022。SDE脚の条件付き exact 数値(IS 9.89/FID 2.20/NLL 2.99等)も本文は定性的。

### T-EV-01
thinness traces to absent authority, not authorial omission: D083 full text unreachable (abstract plus cross-description only) and D086 per-model tables unconsumed; manuscript marks consumption levels and refuses rank inference. Expansion without new retrieval is forbidden, so EVIDENCE_BLOCKED is the correct LONGFORM verdict; repair is evidence-side re-consumption (out of scope), not prose repair.

### T-EV-02
Residual thinness traces to absent authority: D089 recorded locator does not resolve to the corpus paper (snippet-only) and D091 full text is gated; manuscript marks fragment/gated consumption and refuses corpus-fact-to-baseline promotion. EVIDENCE_BLOCKED; repair is evidence-side re-consumption (out of scope).

## Per-transition classifications

| transition | class | delta |
|---|---|---|
| T-CLOSED-01 | BOUNDARY_LIMITED | unchanged (containment verified) |
| T-COND-01 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-COND-02 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-COND-03 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-COND-04 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-CTRL-01 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-CTRL-02 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-CTRL-03 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-CV-01 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-EDIT-01 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-EDIT-02 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-EV-01 | EVIDENCE_BLOCKED | unchanged (containment verified) |
| T-EV-02 | EVIDENCE_BLOCKED | unchanged (containment verified) |
| T-MU-01 | LONGFORM_SUBSTANTIVE | Unconditioned babble / semantic-only non-vocodable -> 3-level hierarchical raw s |
| T-MU-02 | LONGFORM_SUBSTANTIVE | Slow weakly-controllable cascades -> single-stage controllable (FAD 3.1 vs 7.5,  |
| T-MU-03 | BOUNDARY_LIMITED | Unvalidated auto metrics (local vs long-form conflated) -> 12-model x 500-clip / |
| T-PAR-01 | LONGFORM_SUBSTANTIVE | r1記録(SUBSTANTIVE)の内容を維持し、六軸分離表と設計指針の欄分け(畳み込み指針は骨格、競合損失は目的)で深化。数値・代償・継承とも保持。 |
| T-PAR-02 | LONGFORM_SUBSTANTIVE | r1記録(SUBSTANTIVE)を維持し、改訂版の骨格側(配置見直し・重み復調・跳躍生成器)と目的側(遅延R1・経路長正則化)の分離で深化。FID/経路長の二 |
| T-PAR-03 | LONGFORM_SUBSTANTIVE | r1記録(SUBSTANTIVE)を維持し、六軸 framing(表現・骨格・目的・経路・抽出・短縮)で深化。尤度数値・逐次費用・継承とも保持。 |
| T-PAR-04 | LONGFORM_SUBSTANTIVE | r1記録が報告した条件付きFID対比(ImageNetでBigGANを下回る等)がNEW S02では定性的記述に後退し exact 数値が欠落。btd020/b |
| T-PAR-05 | LONGFORM_SUBSTANTIVE | r1記録の段階別FID表がNEW S02では短縮率の要約(10-50x)に圧縮され、CIFAR-10条件の段階別FID階段が欠落。T-PAR-04と同一起源の引 |
| T-PAR-06 | EVIDENCE_BLOCKED | SDE統一機構の記述はr1から維持され要旨限定の扱いも正しい。ただしIssueがEDM設計空間深度を要求するため、本文典拠不在が確定し遷移級ではEVIDENCE |
| T-PAR-07 | LONGFORM_SUBSTANTIVE | D023機構の記述とD024-HOLD境界(実装庫に機構の重みを置かない)はr1から正しく維持。ただしr1記録の無条件/COCO条件付きFID数値がNEW S0 |
| T-PAR-08 | LONGFORM_SUBSTANTIVE | r1記録(COMPRESSED_BUT_SUFFICIENT)を上回り、同一backbone同一計算量の条件付き exact 対比を備えてLONGFORM充足へ |
| T-PAR-09 | LONGFORM_SUBSTANTIVE | r1記録を維持し、模擬なし回帰・OT直線化・整流/再流・一段階蒸留の機構とNFE/FID exact 対比を保持。後継比較の非確立宣言も維持。 |
| T-REP-01 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-02 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-03 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-04 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-05 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-06 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-REP-07 | LONGFORM_SUBSTANTIVE | unchanged (containment verified) |
| T-RT-01 | BOUNDARY_LIMITED | r1はSection 10(実行章)でSUBSTANTIVE。NEW S02の接続節は無撞着核の橋渡しとして正確で、半減/LCM-LoRA/敵対/携帯の各論と遅 |
| T-SP-01 | LONGFORM_SUBSTANTIVE | 16 kHz sample-by-sample AR (slow, 240-300 ms receptive ceiling) -> frame-level a |
| T-SP-02 | LONGFORM_SUBSTANTIVE | Two-stage parallel (fixed-mel finetune, single-speaker) -> end-to-end 67x real-t |
| T-SP-03 | BOUNDARY_LIMITED | Mel-regression studio TTS (YourTTS WER 7.7/sim 0.337) -> codec-LM zero-shot (WER |
| T-SP-04 | BOUNDARY_LIMITED | Studio/closed zero-shot -> versatile controllable (ICL WER 2.249/sim 0.762 ~huma |
| T-VI-01 | LONGFORM_SUBSTANTIVE | Image-only diffusion (no temporal) -> factorized video (FVD 68.19/18.6, joint 20 |
| T-VI-02 | LONGFORM_SUBSTANTIVE | Per-model tuning / uncurated training / closed-only deploy -> tuning-free animat |
| T-VI-03 | BOUNDARY_LIMITED | Research clip models (16f blocks, 5.3 s cascade, README open) -> closed joint-AV |
| T-VI-04 | LONGFORM_SUBSTANTIVE | One-shot editing (consistency 92.40, pref 87.86%, occlusion/drift/flicker ablati |
| T-VI-05 | LONGFORM_SUBSTANTIVE | Single-valued quality (one good sample) -> decomposed validity-bounded eval: sub |
| T-X-01 | BOUNDARY_LIMITED | unchanged (containment verified) |

## Focus-chapter acceptance (Issue #529 criteria)

- S2: six-axis separation + T-PAR-04/05/07/08/09 LONGFORM re-review; citation swap btd020/btd030 repaired; DDPM/ADM/DDIM/LDM condition-bound numbers restored; T-PAR-06 EDM leg EVIDENCE_BLOCKED (abstract-only correct).
- S6: modeling-position axis + streaming-vs-full-duplex constraint separation; PARTIAL D059/D134 fenced.
- S7: fidelity-vs-structure + generation/continuation/editing/control + 4-way eval split.
- S8: spatial/temporal latent, factorization vs 3D vs transformer, image-prior limits, fidelity/motion/consistency/identity axes, duration!=coherence spine kept.
- Non-focus chapters byte-identical (containment verified per-section).