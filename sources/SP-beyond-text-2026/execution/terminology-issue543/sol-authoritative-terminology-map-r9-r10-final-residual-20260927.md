# TS-002 Issue #543 — Sol authoritative terminology map r9 (r10 final residual)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_INDEPENDENT_FINAL_AUDIT / HUMAN_R10_CONTINUATION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope and disposition

This map records the final seed-independent residuals found by Sol after Muse completed the r8 continuation and regenerated the Release Candidate at:

- reviewed branch commit: `53e89dccd7d9a5726c801357d51a7e0cdfc950cc`
- reviewed tree: `b4161ee69c16c87ce0a7b82cfc727c8f2a3021a2`
- candidate SHA-256: `33750d01e656d8fa8d32b39019f0518480fb98cef41d6d45da33414e9c328429`
- exact PDF SHA-256: `75bc73275b045da2fb1a471b96792b1e2e5fbc7861df0528208b222033d26886`
- PDF pages: `78`

Sol independently obtained the exact CI artifact, verified the PDF SHA, rendered and visually reviewed all 78 pages, and performed an independent rendered-PDF terminology scan.

The r8 application itself is accepted. The candidate is **not yet eligible for Issue #543 closure** because a final seed-external family remains in reader-facing prose, concentrated in the video initialization summary plus one hardware acronym residual and three nonsemantic `零` numeral literalizations.

Disposition:

`REQUEST_CHANGES / FINAL_RESIDUALS_FOUND / SAME_HUMAN_R10_AUTHORITY / NO_R11`

This does **not** create a new Human Publication Preview revision. Publication Preview r10 `REQUEST_CHANGES` remains the Human authority. Architecture approval remains preserved. Publication approval remains absent. Freeze / Release / merge remain unauthorized.

## 2. Source readback used by Sol

### btd073 — Make-A-Video

Primary source: Singer et al., *Make-A-Video: Text-to-Video Generation without Text-Video Data*.

The source states that:

- the temporal 1D convolution following each spatial 2D convolution is initialized with an **identity function**;
- the temporal attention projection is initialized to **zero**, making the temporal attention block initially an identity function;
- the method adds the temporal dimension to a pretrained T2I model rather than using a generic concept called `零初期値`.

Therefore the current phrase `恒等や零初期値` loses the component identity and the actual initialization operation.

### btd075 — Stable Video Diffusion

Primary source: Blattmann et al., *Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets*.

The source describes using a pretrained image/T2I model and inserting temporal convolution and attention layers after the corresponding spatial convolution and attention layers. `空間初期値` is not a canonical mechanism name and obscures this architecture relation.

### btd074 — AnimateDiff

Source-bound paper / official implementation material describes the Motion Module as temporal Transformer blocks with positional encoding; the output projection is zero-initialized and used with a residual connection so that the inserted module initially does not disrupt the pretrained image model.

The official implementation also states that the Domain Adapter can be removed at inference and its effect adjusted by a LoRA scaler. Thus `零初期値残差` and `係数を操作し零で除去でき` are reader-facing literalizations rather than canonical technical wording.

### btd055 — HiFi-GAN

Primary paper / official implementation reports synthesis speed on a **V100 GPU** and CPU. Table 1 identifies HiFi-GAN V1 speed as `3701 kHz` on GPU. The current `画像処理装置` loses the canonical hardware acronym and is inconsistent with the rest of TS-002, which already uses `GPU`.

No new claim is authorized by this map; these are source-preserving terminology/copy edits.

## 3. Authoritative decisions

### SOL-R9-C001 — Make-A-Video initialization wording

Current bound phrase:

`データ効率化は擬似三次元畳み込みと注意を恒等や零初期値で拡張し毎秒フレーム数条件を加え`

Decision: `REPLACE`

Final bound phrase:

`データ効率化は擬似3D畳み込みの時間1D畳み込みを恒等写像で初期化し、時間アテンションの時間方向射影をゼロ初期化して毎秒フレーム数条件を加え`

Rationale: preserve the source distinction between identity initialization of the temporal 1D convolution and zero initialization of the temporal attention projection.

Do not broaden to unrelated `恒等` or `ゼロ初期化` occurrences.

### SOL-R9-C002 — Stable Video Diffusion `空間初期値` family

Decision: `REPLACE`, all four source-bound SVD occurrences.

1. Current:

`SVDは空間初期値に時間畳み込みと注意を挿入し`

Final:

`SVDは事前学習済み画像モデルの各空間畳み込み・アテンション層の後に時間畳み込み・アテンション層を挿入し`

2. Current:

`SVDは空間初期値に時間挿入を行う潜在側の統一であり`

Final:

`SVDは事前学習済み画像モデルに時間層を挿入する潜在側の統一であり`

3. Table cell current:

`空間初期値＋時間挿入、三段階`

Final:

`事前学習済み画像モデル＋時間層挿入、三段階`

4. Current:

`第一に、空間初期値に時間畳み込みと注意を挿入し`

Final:

`第一に、事前学習済み画像モデルの各空間畳み込み・アテンション層の後に時間畳み込み・アテンション層を挿入し`

Rationale: `空間初期値` is not a canonical architecture term. The source relationship is pretrained image-model spatial layers plus inserted temporal convolution/attention layers.

### SOL-R9-C003 — AnimateDiff zero-initialized output projection / residual connection

Current bound phrase:

`Motion Moduleは時間Transformer注意を正弦位置と零初期値残差で挿入する`

Decision: `REPLACE`

Final bound phrase:

`Motion Moduleは時間Transformer注意に正弦位置符号化を加え、ゼロ初期化した出力射影と残差接続を用いて挿入する`

Rationale: preserve the actual components: positional encoding, zero-initialized output projection, and residual connection. `零初期値残差` is not a canonical component name.

### SOL-R9-C004 — AnimateDiff Domain Adapter scaler zero

Current:

`アダプターは推論時尺度で係数を操作し零で除去でき`

Decision: `REPLACE`

Final:

`アダプターは推論時の係数を0にすると除去でき`

Rationale: the source describes adjusting the adapter scaler from 1 to 0 / removing the adapter at inference. This is a numeric zero, not a technical term `零`.

### SOL-R9-C005 — FastSpeech hard-sentence error count zero

Current:

`難文$50$文での誤りは零となり`

Decision: `NONSEMANTIC_COPY_EDIT`

Final:

`難文$50$文での誤りは$0$となり`

No claim, citation, or numeric meaning change.

### SOL-R9-C006 — FastSpeech table zero

Current table text:

`難文誤り零`

Decision: `NONSEMANTIC_COPY_EDIT`

Final:

`難文誤り$0$`

No claim, citation, or numeric meaning change.

### SOL-R9-C007 — HiFi-GAN GPU acronym

Current bound phrase:

`画像処理装置で$3701$キロヘルツ、軽量版はCPUでも実時間超えを達成した`

Decision: `REPLACE`

Final bound phrase:

`V100 GPUで$3701$キロヘルツ、軽量版はCPUでも実時間超えを達成した`

Rationale: the source explicitly reports the GPU result on a single V100 GPU; `画像処理装置` is an overtranslation and loses the canonical hardware acronym.

The adjacent HiFi-GAN table row may remain `3701キロヘルツ` because the hardware identity is already established in the immediately preceding prose. Do not add or alter citation keys.

## 4. Regression requirements

After applying r9, the following must be zero in reader-facing source and exact rendered PDF, except where an explicitly retained ordinary-language context exists:

- `零初期値`
- `零初期値残差`
- `空間初期値`
- `画像処理装置`
- `難文誤り零`
- `誤りは零`
- `係数を操作し零で`

Also rerun all prior r2-r8 terminology regression scans. Do not stop merely because this r9 list is zero; perform the same seed-independent broad suspicious-translation scan once more.

## 5. Citation boundary

No new citation correction is authorized.

The complete allowed citation correction set remains exactly:

- `SOL-CIT-001`: DAC Balanced data sampling -> `btd008`
- `SOL-CIT-002`: Wan2.2 open-weight boundary -> `btd124`
- `SOL-CIT-003`: SPADE/GauGAN Section 4 claims -> `btd041`
- `SOL-CIT-004`: T2I-Adapter Section 4 claims -> `btd037`

Do not add, delete, substitute, regroup, or rebind citation keys while applying r9.

`references.bib` remains frozen.

## 6. Ledger requirements

Add r9 decisions to the Issue #543 terminology ledger JSON and Markdown with discovery source:

`SOL_R10_R9_FINAL_INDEPENDENT_AUDIT`

JSON/MD row sets must remain exactly synchronized. Recompute all summary counts from the actual JSON row set. Do not trust stale Markdown summary counts or stale unresolved pointers.

For the context-bound SVD family, record the four occurrences under the r9 authority without inventing duplicate semantic decisions.

## 7. Frozen Core v2 — immutable

Frozen Core v2 remains absolutely immutable.

Core implementation SHA:
`95c03bf5285cb4b2c1103a14c460574183a8cb93`

Pipeline contract SHA-256:
`ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`

Quality contract SHA-256:
`b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`

Research profile SHA-256:
`0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`

Publication profile SHA-256:
`a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

No shared Core script/schema/contract/config/template/stage-plan/transition/compatibility change is authorized. If the frozen Core cannot execute the continuation, stop and report; do not repair Core.

## 8. Lifecycle / closure rule

This is the same Human Publication Preview r10 continuation. Do not create r11.

Apply r9 from the current Release Candidate by using the existing frozen Core Human-Gate/regeneration semantics only as already authorized by r10. Do not synthesize a new Human decision.

If a new unmapped suspicious term is found after r9, report it to Sol and remain within the same r10 authority.

If unresolved count becomes zero, regenerate and validate the exact candidate/PDF via the frozen Core path, stop at:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

and return the candidate to Sol for one final independent source/PDF audit.

Issue #543 must remain OPEN until that Sol audit passes.

## 9. Independent visual-build observation

The exact reviewed 78-page PDF showed no visible clipping, overflow, broken glyph, blank-page defect, or table-layout blocker in Sol's all-page render inspection.

The raw LaTeX build log nevertheless contains two `Overfull \\vbox` messages (approximately 4.034 pt and 0.234 pt). The frozen existing PDF workflow currently scans `Overfull/Underfull \\hbox` but not `\\vbox`; therefore generated validation metadata reported no layout-log findings.

This is recorded as a **nonblocking audit observation**, because the affected rendered pages were manually inspected and show no visible defect. It is **not authority to modify Frozen Core v2**. Do not change the shared workflow or validator in this edition-local repair.