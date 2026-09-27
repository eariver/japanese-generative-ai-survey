# TS-002 Issue #543 — Sol authoritative terminology map r8 (r10 candidate resolution)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / HUMAN_R10_CONTINUATION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope

This map resolves every candidate in:

`sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r10.md`

It is a continuation of the already-recorded Human Publication Preview r10 `REQUEST_CHANGES` at `DRAFT_COMPLETE`. It does not create r11 and does not authorize any Core v2 change.

Muse is executor/validator only. Do not reinterpret these decisions or substitute alternate wording.

## 2. Source readback used by Sol

- `btd005` / DALL-E: the model represents captions as up to 256 BPE-encoded text tokens and images as 1024 tokens in one autoregressive stream.
- `btd023` / Latent Diffusion Models: cross-attention accepts general conditioning such as text or bounding boxes / semantic layouts.
- `btd039` / DreamBooth: input images are labeled with prompts of the form `a [identifier] [class noun]`; the identifier is tied to the subject and the class noun is a coarse class descriptor.
- `btd073` / Make-A-Video: the method builds on a pretrained Text-to-Image model by adding spatiotemporal modules, including pseudo-3D convolution/attention, rather than a canonical mechanism called a `multilayer network`.
- `btd138` / FiVE: Pyramid-Edit and Wan-Edit are described as training-free and inversion-free video editing models.

No new technical claims are authorized by this map.

## 3. Candidate decisions

### SOL-R8-C001 — four-category heading

Original:
`四区分の使い分け：条件と誘導と適合と参照`

Decision: `REPLACE`

Final:
`四区分の使い分け：条件づけ・ガイダンス・アダプター・参照`

Rationale: this heading names the same four categories already established in the section: learning-time conditioning, inference-time guidance, adapter-based extension, and context/reference use. `適合` is reserved elsewhere for fit/alignment and must not carry adapter/adaptation meaning.

### SOL-R8-C002 — T2I-Adapter lineage bare `軽量適合`

Decision: `REPLACE`

Apply in the three candidate contexts only:

- lineage enumeration `軽量適合` -> `軽量制御アダプター`
- heading `配置の前史と軽量適合：洗い流さない工夫` -> `配置の前史と軽量制御アダプター：洗い流さない工夫`
- boundary sentence `軽量適合の境界` -> `軽量制御アダプターの境界`

Do not change unrelated statistical/distributional `適合`.

### SOL-R8-C003 — `画像参照`

Decision: `SPLIT / RETAIN + REPLACE`

- In ordinary mechanism descriptions (`画像参照の分離注意`, `画像参照は内容と様式の類似に留まり...`), `画像参照` is natural and canonical enough: `RETAIN`.
- In the lineage enumeration paired with adapter families, replace bare `画像参照` with `画像参照アダプター`.

Do not globally rewrite every `画像参照` occurrence.

### SOL-R8-C004 — `適合の視点`

Decision: `REPLACE`

`本節の五転換を適合の視点で振り返る。`
->
`本節の五転換をアダプター／適応の視点で振り返る。`

### SOL-R8-C005 — FiVE training-free / inversion-free condition

Original:
`訓練や反転なしの適合の条件で`

Decision: `REPLACE`

Final:
`学習・反転不要の編集条件で`

Canonical source meaning: training-free and inversion-free video editing. Do not call this `適合` or `adaptation`.

### SOL-R8-C006 — CFG guidance-scale sweep

Original:
`誘導尺度の掃引`

Decision: `REPLACE`

Final:
`ガイダンススケールのスイープ`

This is the same source-bound concept already normalized in r7.

### SOL-R8-C007 — technical `画像と文`

Decision: `REPLACE`

In the two candidate technical-modality contexts only:
`画像と文` -> `画像とテキスト`

Do not alter ordinary Japanese `文` outside technical modality contexts.

### SOL-R8-C008 — DALL-E BPE text

Original:
`二百五十六トークン以内のバイト対符号化文`

Decision: `REPLACE`

Final:
`最大256トークンのBPE符号化テキスト`

Preserve all adjacent image-token/vocabulary claims unchanged.

### SOL-R8-C009 — LDM text/layout conditioning

Decision: `REPLACE`

- `文や配置のcross-attention（クロスアテンション）`
  -> `テキストやレイアウトのcross-attention（クロスアテンション）`
- `文や配置の条件`
  -> `テキストやレイアウトの条件`

The accepted LDM source supports text and bounding-box/semantic-layout conditioning through cross-attention.

### SOL-R8-C010 — section-intro rhetorical modality wording

Original:
`文から絵や音を生むとき、条件づけはどこで行われるのか。`

Decision: `REPLACE`

Final:
`テキストから画像や音を生成するとき、条件づけはどこで行われるのか。`

This is reader-facing technical prose, not ordinary prose where `文` should be retained.

### SOL-R8-C011 — DreamBooth class-noun prompt

Original bound phrase:
`稀少識別子と類名詞の文を添え`

Decision: `REPLACE`

Final bound phrase:
`稀少識別子とクラス名詞を含むプロンプトを添え`

Canonical source form is `a [identifier] [class noun]`.

### SOL-R8-C012 — Make-A-Video base T2I model

Original bound phrase:
`テキスト・画像多層網に擬似三次元畳み込みと注意を拡張し`

Decision: `REPLACE`

Final bound phrase:
`事前学習済みText-to-Image（T2I）モデルに擬似3D畳み込みと時間方向のアテンションを拡張し`

Rationale: the source explicitly builds on a pretrained T2I model and adds spatiotemporal modules; `多層網` loses the model identity and is not a canonical mechanism name.

## 4. Copy-edit defect observed by Sol

The current source contains:
`3D一貫性は厳密ではなく、、偏り危険を伴い`

This is not a terminology judgment. It is an obvious reader-facing copy-edit defect introduced/preserved in the same edited surface.

Authorized nonsemantic correction:
`3D一貫性は厳密ではなく、偏りの危険を伴い`

No citation or claim change is implied.

## 5. Citation and Core boundary

No new citation correction is authorized by r8.

Existing bounded citation authority remains exactly:

- `SOL-CIT-001` DAC Balanced data sampling -> `btd008`
- `SOL-CIT-002` Wan2.2 open-weight boundary -> `btd124`
- `SOL-CIT-003` SPADE/GauGAN Section 4 claims -> `btd041`
- `SOL-CIT-004` T2I-Adapter Section 4 claims -> `btd037`

`references.bib` remains frozen.

Frozen Core v2 remains immutable. No shared Core script/schema/contract/config/template/stage-plan/transition/compatibility change is authorized.

## 6. Ledger and closure requirements

Add these decisions to the terminology ledger with discovery source:
`SOL_R10_R8_CANDIDATE_RESOLUTION`

The ledger summary must be recomputed from the actual JSON row set; do not leave stale summary counts or stale `Unresolved terms` pointers.

After applying r8, perform the same pre-validation full-source scan required by the r10 execution contract.

If any new unmapped suspicious term remains, report it without editing and stay at `DRAFT_COMPLETE` under the same r10 authority.

If unresolved count is zero, continue via the frozen Core to `VALIDATED_DRAFT` and `RELEASE_CANDIDATE`, then stop at Publication Preview pending.
