# TS-002 Issue #543 — Sol authoritative terminology map r7 (final independent full-text scan)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / FINAL_INDEPENDENT_FULLSCAN / APPLY_WITHOUT_REINTERPRETATION`

## 1. Why r7 exists

The r9/r6 worker path completed mechanically and regenerated a 78-page publication candidate, but Sol independently re-read the rendered PDF and reader-facing source rather than accepting the worker zero-count scan as editorial closure.

That independent scan found four residual classes outside the r2-r6 worker dictionaries:

1. text-modality terminology still written as literalized `文*` compounds;
2. adapter/adaptation terminology incorrectly written as `適合`, conflicting with this edition's own glossary (`適合` = distributional fit/closeness);
3. source-specific literalizations in audio/music/video/convergence sections;
4. one actual edition-local citation-binding defect: SPADE/GauGAN and T2I-Adapter keys are swapped in Section 4.

This map is Sol's final editorial/source-binding decision. Muse MUST apply it mechanically and MUST NOT reinterpret, expand, or replace it with alternate wording.

Frozen Core v2 remains immutable. No Core implementation, script, schema, contract, stage plan, transition rule, compatibility logic, template, or shared configuration may be modified.

## 2. Source readback used by Sol

Sol re-read the relevant accepted/primary authorities before issuing r7:

- CLIP: image encoder + text encoder projected into a joint multimodal embedding; prompt-template ensembling is part of the zero-shot procedure.
- eDiff-I: conditioning includes T5 text, CLIP text, and CLIP image embeddings; expert denoisers are specialized by synthesis stage.
- CLAP: separate audio and text encoders are trained contrastively into a joint multimodal space.
- T2I-Adapter: lightweight T2I-Adapters align external control signals to a frozen original T2I model; composability/generalization are explicit.
- IP-Adapter: decoupled cross-attention separates text and image features; the pretrained diffusion model is frozen.
- LoRA: canonical term is Low-Rank Adaptation; pretrained weights are frozen and trainable low-rank decomposition matrices are injected.
- ControlNet: the locked pretrained model is reused as a backbone and is connected through zero convolutions (zero-initialized convolution layers).
- MusicGen: the 32 kHz EnCodec tokenizer uses four codebooks at 50 Hz; the monophonic EnCodec path has total stride 640.
- Music ControlNet: controls are melody, dynamics, and rhythm; global text controls concern attributes such as genre/mood/tempo. The source does not establish a chord-prediction mechanism.
- MuSTANGO: its core guidance module is MuNet, a Music-Domain-Knowledge-Informed UNet; music-specific conditions are predicted from the text prompt and used with the general text embedding.
- Imagen Video: the source discusses object rotation with imperfect 3D consistency; `回転整合` is not a canonical mechanism/metric name.
- Unified-IO: heterogeneous inputs/outputs are homogenized into discrete vocabulary-token sequences and handled by a single transformer architecture; dense outputs are subject to the representation/tokenization bottleneck.
- SPADE/GauGAN and T2I-Adapter bibliography identities were re-read directly from `references.bib`; the current Section 4 bindings are reversed.

No new technical authority is created by this map. These are editorial corrections over accepted authority.

---

# 3. Text-modality canonicalization

## SOL-R7-T01 — technical `文*` compounds

In ML/modality contexts, `文` is not the reader-facing canonical term for `text`. Apply the following bound mappings wherever the occurrence carries the same technical meaning:

- `文条件づけ` -> `テキスト条件づけ`
- `大規模な文条件づけ` -> `大規模なテキスト条件づけ`
- `文条件` -> `テキスト条件`
- `文条件超解像` -> `テキスト条件付き超解像`
- `文条件生成` -> `テキスト条件生成`
- `文条件転移` -> `テキスト条件への転移`
- `文誘導拡散` -> `テキスト誘導拡散`
- `文ドロップアウト` -> `テキスト条件ドロップアウト`
- `空文割合` -> `空テキスト条件の割合`
- `文整合` -> `テキスト整合`
- `文への従順さ` -> `テキスト条件への追従性`
- `文有用性` -> `テキスト条件の有用性`
- `凍結大規模文符号器` / `大規模文符号器` -> `凍結大規模テキストエンコーダ` / `大規模テキストエンコーダ`
- technical `文符号器` -> `テキストエンコーダ`
- `文のみ条件` -> `テキストのみの条件`
- `文能力` -> `テキスト条件能力`
- `文枝` -> `テキスト枝`
- `文類似` -> `テキスト類似度`
- `文品質` -> `テキスト記述の品質`
- `文から画像` -> `テキストから画像`
- technical `文と画像` -> `テキストと画像`

Do NOT replace ordinary Japanese `文` where it genuinely means a sentence, wording, prose, or document text rather than a model modality/conditioning signal.

## SOL-R7-T02 — CLIP / eDiff-I / CLAP source-bound wording

### CLIP (`btd031`)

Replace `プロンプトテンプレートと集成` / `埋め込み集成` with:

- `プロンプトテンプレートとアンサンブル`
- `埋め込みアンサンブル`

`joint 空間` in CLIP context -> `共同埋め込み空間`.

### eDiff-I (`btd034`)

Replace the literalized three-encoder wording with the source identity:

> `T5テキスト、CLIPテキスト、CLIP画像の3種の埋め込みを独立ドロップアウトで条件づける`

Do not retain `大規模文符号器と対照文と対照画像の三符号器`.

`共有 baseline` -> `共有ベースライン`.

### CLAP (`btd035`)

Use:

> `音声エンコーダとテキストエンコーダを対照学習し、共同マルチモーダル埋め込み空間へ写像する`

Do not retain `畳み込み音響符号器と文符号器` or `joint 空間` in this context.

Where `百二十八対の束` / `束規模` refers to the accepted training batch statement, use `128ペアのバッチ` / `バッチサイズ`.

Where `対規模` means number of paired training examples, use `学習ペア数`.

## SOL-R7-T03 — CFG / generic English residue

- `尺度掃引` in classifier-free-guidance context -> `ガイダンススケールのスイープ`
- ML-training `jointly` -> grammatical Japanese `共同で` / `共同学習する`
- simultaneous MotionCtrl condition use `jointly` -> `同時に`
- SDE/score-model `framing` -> `定式化`
- ControlNet `単一制御の framing` -> `単一制御という設定`

The technical term `joint` may remain only when it is part of an explicit proper/source term that Sol maps separately. Do not leave reader-facing English filler `jointly` or `framing`.

---

# 4. Adapter / adaptation family — do not misuse `適合`

This edition explicitly uses `適合` for distributional closeness/fit. It MUST NOT also be used as the translation of adapter/adaptation.

Apply only in adapter/adaptation contexts:

- Section wording `音響の言語整合と空間制御の適合` -> `音響の言語整合と空間制御アダプター`
- `適合の系譜` when discussing adapters/LoRA -> `アダプター／適応の系譜`
- `適合の形` table header -> `拡張・適応の形`
- `軽量配置適合` -> `軽量制御アダプター（T2I-Adapter）`
- `画像参照適合` -> `画像参照アダプター（IP-Adapter）`
- `低ランク適合` -> `Low-Rank Adaptation（LoRA／低ランク適応）`
- `多適合` -> `複数アダプター`
- `適合規模` -> `アダプター規模`
- `参照適合` -> `参照アダプター`
- `空間適合` -> `空間制御アダプター`
- `動作適合` -> `モーション制御`
- `制御適合` -> `制御アダプター`
- `効率適合` in the LoRA continuation sentence -> `効率的な適応`

Do NOT globally replace ordinary/statistical `適合`, distributional fit, benchmark alignment, or other contexts not referring to adapters/adaptation.

## SOL-R7-A01 — IP-Adapter text wording

In the IP-Adapter subsection (`btd038`):

- `文能力を壊さず` -> `テキストプロンプト能力を壊さず`
- `文枝` -> `テキスト枝`
- `文類似` -> `テキスト類似度`

Preserve the source distinction: decoupled cross-attention has separate text-feature and image-feature paths.

## SOL-R7-A02 — LoRA

Use canonical `Low-Rank Adaptation（LoRA／低ランク適応）`; do not call the mechanism `低ランク適合`.

Keep the existing evidence boundary that this edition's cited LoRA authority is language-model-domain evidence; do not infer diffusion-specific LoRA quality from it.

---

# 5. ControlNet terminology

## SOL-R7-C01 — conditioning encoder

`微小条件符号器` is noncanonical.

Replace with:

> `条件入力を潜在解像度へ写像する小規模畳み込みネットワーク`

where that sentence describes the ControlNet condition-input preprocessing path.

## SOL-R7-C02 — zero convolution

- `零畳み込み` -> `zero convolution（ゼロ畳み込み）`
- `零から育てる` in ControlNet parameter-growth context -> `ゼロ初期化された重みから学習する`

Do not change unrelated ordinary `ゼロ` prose.

## SOL-R7-C03 — class terminology

In ML class-conditioning contexts:

- `類別` -> `クラス` or `クラスラベル`, according to grammar.
- `時刻と類別の条件づけ` -> `時刻とクラスの条件づけ`
- `類別を超える文条件` -> `クラス条件を超えるテキスト条件`
- representation-section `課題 prompt と類別` -> `タスクプロンプトとクラスラベル`

---

# 6. Audio-codec / listening terminology

## SOL-R7-AUD01 — subjective evaluation wording

The reader-facing phrases `群衆方式` and `聴取得点` are nonstandard literalizations.

In the neural-audio-codec comparison context:

- `群衆方式` -> `クラウドソーシングによる聴取評価`
- `聴取得点` -> `主観聴取評価スコア`

Preserve the existing source boundary. Do not promote these observations into a claim about standardized laboratory MUSHRA unless the cited source explicitly establishes it for that sentence.

---

# 7. Music / audio source-specific corrections

## SOL-R7-M01 — Jukebox rate wording (`btd063`)

- `8や32や128の間引き率` -> `ダウンサンプリング率8・32・128`

Keep the hierarchy and all numeric values unchanged.

## SOL-R7-M02 — MusicGen tokenizer wording (`btd066`)

Replace:

> `32キロヘルツ単一信号を640間隔で50ヘルツの四重残差符号に落とし`

with:

> `32 kHzモノラル音声を総ストライド640のEnCodecで、50 Hz・4コードブックの離散トークン列へ符号化し`

Preserve the delay-pattern Transformer, text cross-attention, chroma conditioning, CFG, stereo fine-tuning, and all accepted numerical values.

## SOL-R7-M03 — Music ControlNet (`btd043`)

The source supports time-varying control of **melody, dynamics, and rhythm**, plus global text attributes such as genre/mood/tempo. It does not establish a chord-prediction mechanism.

Therefore:

- remove `拍弦予測の文駆動`;
- replace the bound idea with `ジャンル・ムード等のグローバルなテキスト条件と、旋律・ダイナミクス・リズムの時間変化制御を組み合わせる`;
- `タグのみ文` -> `ジャンル・ムード等のグローバルなテキストタグ条件`;
- `零畳み込み` in this subsection -> `zero convolution（ゼロ畳み込み）`.

Do not introduce chord control into Music ControlNet.

## SOL-R7-M04 — MuSTANGO (`btd069`)

Replace:

- `潜在拡散に対照音楽ネットワークを重ね` -> `潜在拡散にMuNet（Music-Domain-Knowledge-Informed UNet）を組み込み`

Preserve the accepted text/beat/chord conditioning, MusicBench augmentation, PCM/FD/KL metrics, and 10-second boundary.

## SOL-R7-M05 — `標識三重`

If the human-preference paragraph still contains `標識三重の楽曲組合せ`, do not retain that literalization. Rewrite only the local phrase as:

> `3種類のラベル情報を持つ楽曲組合せ`

if that is exactly what the already-consumed source/evidence binds; otherwise remove the adjective and retain the source-supported `楽曲組合せ` without adding a new claim. Muse MUST NOT infer a new labeling scheme.

---

# 8. Video / evaluation terminology

## SOL-R7-V01 — Imagen Video 3D consistency (`btd071`)

Replace:

- `三次元回転整合は不精密` -> `物体回転中の3D一貫性は厳密ではない`
- summary `回転整合` -> `回転中の3D一貫性`

This is a limitation statement, not a named metric.

## SOL-R7-V02 — VBench backbone wording (`btd092` and bound evaluation prose)

- `背骨` in model/evaluation contexts -> `バックボーン`
- `背骨三種` -> `3種類のバックボーン`
- `背骨偏り` -> `バックボーン依存の偏り`

Do not replace the edition's intentional editorial term `骨格`; only the literalized `背骨` family is targeted.

## SOL-R7-V03 — product/workflow phrase

- `自然文区間編集` -> `自然言語による区間編集`

Do not expand product capability beyond the cited product/release surface.

---

# 9. Unified-IO conservative rewrite (`btd094`)

The phrase `純粋Transformerは金字塔と損失事前を欠き` is not sufficiently source-transparent and contains an obvious mistranslation (`金字塔`). Do not attempt to repair it word-for-word.

Replace the bound limitation sentence with a source-supported formulation:

> `単一Transformerで多様な入出力を離散トークン列へ統一するため、密な予測もトークナイザ／VQ-GANの表現上限に依存する。`

Preserve the existing `Unrestricted` evaluation-track boundary if independently supported by the accepted source/evidence. Do not invent a feature-pyramid or loss-prior claim.

---

# 10. Citation-binding repair — explicit exceptions

The current Section 4 has SPADE/GauGAN and T2I-Adapter citation keys reversed.

Bibliography identity is authoritative:

- `btd037` = T2I-Adapter
- `btd041` = SPADE/GauGAN

This is an edition-local source-binding defect, not a Core issue.

## SOL-CIT-003 — SPADE/GauGAN claims

For Section 4 statements specifically about:

- semantic-mask-to-photorealistic synthesis;
- spatially-adaptive normalization;
- mask-derived spatial modulation parameters;
- SPADE/GauGAN generator/discriminator design;
- paired semantic-mask/image training;
- the SPADE predecessor/boundary;

replace the incorrect `btd037` binding with `btd041`.

## SOL-CIT-004 — T2I-Adapter claims

For Section 4 statements specifically about:

- lightweight T2I-Adapters on a frozen text-to-image model;
- adapter features injected at multiple scales;
- adapter composability/generalization;
- adapter scale/size and control behavior;

replace the incorrect `btd041` binding with `btd037`.

### Mixed sentences

If one sentence genuinely compares or connects SPADE and T2I-Adapter, it may cite both `btd041,btd037` in claim order. Do not blindly swap every occurrence repository-wide.

No other citation change is authorized by r7. Existing SOL-CIT-001 and SOL-CIT-002 remain authorized and frozen.

---

# 11. Retain rules

The following are NOT global replacement targets:

- ordinary Japanese `文` meaning sentence/prose/document;
- statistical/distributional `適合` consistent with the edition glossary;
- the edition's intentional architecture-layer term `骨格`;
- ordinary `序列` where it simply means ranking/order;
- `文章化` when it means verbalizing/describing a phenomenon in prose;
- source-bound English/acronyms that are already canonical.

# 12. Closure and execution rule

After r7 is applied, the executor must:

1. update the Issue #543 terminology ledger JSON/MD with `SOL_FINAL_INDEPENDENT_R7` decisions;
2. perform a new full reader-facing source scan, not a seed-only scan;
3. verify r2-r7 prohibited left-hand forms in their bound technical senses are zero;
4. verify SOL-CIT-001 through SOL-CIT-004 are the only authorized citation-binding changes;
5. preserve 139/139 bibliography coverage and all Evidence/PARTIAL/NEEDS_MORE boundaries;
6. rebuild and inspect the exact PDF;
7. keep Frozen Core v2 byte/contract/implementation identities unchanged.

If any new semantically uncertain technical term is found, Muse must report it without editing it.

Because the current edition is already back at `RELEASE_CANDIDATE`, this map itself does **not** authorize a new regeneration transition. A new explicit Human Publication Preview revision is required by Frozen Core before r7 may be applied.

No Freeze, Release, merge, or Human publication approval is authorized by this file.
