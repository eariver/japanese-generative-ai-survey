# TS-002 Issue #543 — Sol authoritative terminology map r2

Date: 2026-09-26 JST
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Authority and execution rule

This file is the authoritative editorial mapping for the next Issue #543 repair pass.

Muse MUST NOT reinterpret, broaden, narrow, or substitute the decisions below. Muse's role is limited to:

1. locate occurrences that match the stated semantic context;
2. apply the exact Sol decision or a purely grammatical inflection that does not alter meaning;
3. update the Issue #543 terminology ledger so that JSON and Markdown views agree;
4. run invariants, build, rendered-text audit, and visual QA;
5. report any unmapped suspicious term as `CANDIDATE_FOR_SOL_REVIEW` without editing it.

If an occurrence does not clearly match the semantic context defined below, Muse MUST NOT decide the wording. Leave it unchanged, record the exact sentence / section / citation, and return it to Sol.

Issue #543 remains a terminology repair. Issue #529 semantic depth, Evidence status, claim boundaries, section architecture, numerical meaning, vendor attribution, and closed-system boundaries remain frozen.

## 2. Citation-binding exception

Citation sequence is normally frozen. One narrow exception is authorized because Sol readback found a source-binding defect exposed by the terminology audit.

### SOL-CIT-001 — balanced full-band sampling

Current reader text binds `均衡ある全帯域抽出` to `btd007` (EnCodec). The canonical concept is **Balanced data sampling** from the DAC / Improved RVQGAN authority (`btd008`), where known full-band sources are deliberately sampled to prevent high-frequency reconstruction cut-off.

Required rewrite of the relevant boundary passage:

> 参照水準との開きと環境音や特定音色での弱さはEnCodec側の境界である\autocite{btd007}。一方、DACでは高域再構成の欠落への対策としてBalanced data sampling（均衡データサンプリング）を導入し、full-band音源を各バッチに含める\autocite{btd008}。

The exact Japanese may be grammar-adjusted, but the semantic split and citation binding MUST remain as above.

This is the only pre-authorized citation-binding change in this pass. Any other citation change requires a stop-and-report to Sol.

## 3. Global editorial rules decided by Sol

### SOL-G-001 — generated sample

In generative-model prose, `標本` when it means a generated sample/output becomes `サンプル` or, where clearer, `生成例`.

Retain `標本` only when it is genuinely statistical-sampling terminology and not a generated artifact.

Examples:
- `良質標本` -> `高品質なサンプル`
- `単一良標本` -> `単一の良好な生成例`
- `標本の鮮明さ` -> `サンプルの鮮明さ`

### SOL-G-002 — hardware names

- `消費者用図形処理装置` -> `民生GPU`
- ML hardware sense of `図形処理装置` -> `GPU`
- `中央処理装置` -> `CPU`

Do not expand GPU/CPU into literal Japanese component names.

### SOL-G-003 — checkpoint / benchmark / multi-turn / frame

- model/version `検査点` -> `チェックポイント`
- `基準測定` when it means benchmark -> `ベンチマーク評価`
- dialogue `多回合` -> `マルチターン`
- video/image `frame` in Japanese prose -> `フレーム`

### SOL-G-004 — canonical dataset and metric identities

Never replace a named dataset or metric with a generic Japanese noun. Preserve canonical names such as `MusicCaps`, `AudioCaps`, `FAD`, `KLD`, `CLAP score`, `MuLan Cycle Consistency (MCC)`, `FD`, `OVL`, `REL`, `Classification Accuracy Score (CAS)`.

## 4. Representation / compression

### SOL-R-001 — VQ-VAE-2 classification metric

Context: `btd003` VQ-VAE-2.
Canonical: **Classification Accuracy Score (CAS)**.
Decision:
- `分類得点` -> `Classification Accuracy Score（CAS）`

### SOL-R-002 — DAC balanced sampling

See `SOL-CIT-001`.
- `均衡ある全帯域抽出` -> `Balanced data sampling（均衡データサンプリング）`
- bind this claim to `btd008`.

### SOL-R-003 — AudioLM long-form terminology

Context: `btd009` AudioLM.
Canonical concepts: **long-term structure**, **piano continuation**.
Decisions:
- `長い結構` -> `長期構造`
- `鍵盤継続` -> `ピアノ継続`

### SOL-R-004 — multimodal I/O

When `多峰入出力` means multimodal input/output:
- `多峰入出力` -> `マルチモーダル入出力`

Do not apply this mapping to statistical multimodality.

## 5. GAN / diffusion / score / flow

### SOL-P-001 — DCGAN long-training failure

Context: `btd014` DCGAN conclusion.
Canonical source statement: a subset of filters can collapse to a single oscillating mode during long training.
Decision:
- `濾波崩壊` -> `一部フィルタの単一振動モードへの崩壊`

Do not rewrite this as generic mode collapse; it is a narrower filter-level observation.

### SOL-P-002 — predictor-corrector

Context: score-SDE / `btd021`.
Decision:
- `予測子修正子` -> `predictor-corrector（予測子・修正子）`
- subsequent same-context bare `修正子` -> `corrector（修正子）` where needed for clarity.

### SOL-P-003 — scaling law

Context: DiT / model scaling.
- `規模則` -> `スケーリング則`

### SOL-P-004 — Rectified Flow reflow

Context: Rectified Flow.
- `再流` -> `reflow（再フロー）`

### SOL-P-005 — Consistency terminology

Consistency Model family has already been standardized to `整合性` in the edition.
- front-matter or residual `一致性` for this model family -> `整合性`

Do not change ordinary Japanese uses of logical/semantic consistency that are not the named model family without an explicit mapping.

### SOL-P-006 — generic network / upsampling

- `単一網` in ML-network context -> `単一ネットワーク`
- `級上げ器` when source means upsampler -> `アップサンプラー`
- `級上げ` when source means upsampling -> `アップサンプリング`

### SOL-P-007 — query projection

Attention `問い合わせ行列` -> `query projection（クエリ射影）` or grammatically `クエリ射影行列`.
Do not use the ordinary-Japanese `問い合わせ` for attention queries.

## 6. Editing / Tune-A-Video

### SOL-E-001 — Tune-A-Video network inflation

Context: `btd050` Tune-A-Video.
Canonical: **network inflation**, 2D `3×3` convolution expanded to pseudo-3D `1×3×3`, plus temporal attention.
Decision:
- `膨張形式` -> `擬似3D畳み込みへのnetwork inflation（3×3→1×3×3）`

This resolves the prior ESCALATE. Do not translate network inflation as `膨張形式`.

### SOL-E-002 — Tune-A-Video query

Same context:
- `問い合わせ行列` -> `クエリ射影行列（W^Q）` where the source refers to the query projection matrix.

## 7. Speech / TTS

### SOL-S-001 — Tacotron / Tacotron 2

Canonical source terms:
- Tacotron waveform reconstruction: **Griffin-Lim**
- Tacotron 2 attention: **location-sensitive attention**
- Tacotron 2 WaveNet: **3 dilation cycles**, **10-component mixture of logistics**

Decisions:
- `位置鋭敏注意` -> `location-sensitive attention（位置依存アテンション）`
- `近似波形合成` in Tacotron -> `Griffin-Limによる波形再構成`
- `三膨張循環` -> `3回のdilation cycle（膨張畳み込みサイクル）`
- `十要素混合` -> `10成分のlogistic mixture（ロジスティック混合）`

### SOL-S-002 — WaveNet comparison baseline

In the WaveNet baseline comparison, `系列網` does not mean a generic sequence network.
Decision:
- `系列網` -> `LSTM-RNNパラメトリック音声合成` when referring to the WaveNet paper's RNN baseline.

If another occurrence of `系列網` points to a different source/model, do not apply automatically; report it.

### SOL-S-003 — VALL-E 2 grouped codes

Canonical: **Grouped Code Modeling**, **Repetition Aware Sampling**.
Decision:
- `群化符号` / `群化` in the VALL-E 2 mechanism -> `Grouped Code Modeling（グループ化コードモデリング）`
- where the sentence refers to the units rather than the method -> `グループ化したcodec code`

### SOL-S-004 — Seed-TTS descriptor

Canonical title: **Seed-TTS: A Family of High-Quality Versatile Speech Generation Models**.
Decision:
- `多能高忠実モデル` -> `Seed-TTS（多用途・高品質音声生成モデル）`
- generic repeat if necessary -> `多用途・高品質音声生成モデル`

### SOL-S-005 — Seed Audio naturalness metric

Context: `btd110` Seed Audio 1.0 vendor evaluation.
Canonical metric: **Naturalness MOS**.
Decision:
- `自然さ得点` -> `Naturalness MOS（自然さMOS）`

Retain vendor-attribution and independence boundary.

## 8. Music / audio

### SOL-M-001 — dataset names

- `音楽 caps` -> `MusicCaps`
- `音響 caps` -> `AudioCaps`

### SOL-M-002 — MusicLM metric identity

Context: `btd065` MusicLM.
- `距離 4.0` etc -> `FAD 4.0` etc
- `乖離 1.01` etc -> `KLD 1.01` etc
- `整合 0.51` etc -> `MuLan Cycle Consistency（MCC）0.51` etc

Apply corresponding metric names to the related ablation values in the same MusicLM source context.

### SOL-M-003 — MusicGen metric identity

Context: `btd066` MusicGen.
Use the paper's canonical metric names rather than generic nouns:
- FAD for Fréchet Audio Distance values
- KLD for KL divergence values
- CLAP score for text-audio alignment values
- preserve named human-evaluation axes such as OVL / REL where the paper/report uses those labels.

### SOL-M-004 — AudioLDM metric identity

Context: `btd067` AudioLDM.
- `23.31` -> `FD 23.31`
- `65.91` -> `OVL 65.91`
- use `REL` for the corresponding relevance value where present.

Do not call these generic `distance` / `overall` without the metric identity.

### SOL-M-005 — Stable Audio Open metric identity

Context: `btd068`.
- `78.24` -> `FD_openl3 78.24` when this is the reported AudioCaps metric.

### SOL-M-006 — Jukebox spectral metric

Context: `btd063` Jukebox.
- `帯域収束` when it denotes the reported metric -> `spectral convergence（スペクトル収束）`

### SOL-M-007 — music structure terms

Where source meaning is verse/chorus:
- `節` -> `ヴァース`
- `副歌` -> `コーラス`
- `節・副歌` -> `ヴァース／コーラス`

Do not apply to Japanese prose where `節` is not a musical section.

### SOL-M-008 — genre / workflow terms

Music-generation control context:
- `流派` -> `ジャンル`

Suno editing context:
- `刈込` -> `トリミング`

Stable Audio continuation context:
- `続成` -> `continuation（継続生成）`

### SOL-M-009 — human evaluation wording

- `人文横並べ` -> `人間によるside-by-side評価`
- `人文・自動評価` -> `人間評価・自動評価`
- `ベンダー人文言及` if it means vendor mention of human evaluation -> `ベンダーによる人間評価への言及`

## 9. Video

### SOL-V-001 — Make-A-Video appearance/motion split

Context: `btd073` Make-A-Video.
The paper learns appearance/text correspondence from paired text-image data and motion from unlabeled video; `外観凍結` is misleading.
Decision:
- `外観凍結` -> `外観と運動の分離学習`
- where explanatory prose is needed: `画像側の外観・テキスト対応を活用し、未ラベル動画から運動を学ぶ分離`

Also:
- `網データ` -> `Webデータ`
- `長多場面` -> `長尺・マルチシーン`

### SOL-V-002 — AnimateDiff

Context: `btd074` AnimateDiff.
Canonical components:
- **Motion Module**
- **Motion LoRA**
- domain adapter / domain-specific adapter where applicable.

Decisions:
- `動作接続器` -> `Motion Module（モーションモジュール）`
- `運動 LoRA` -> `Motion LoRA`
- `領域接続器` in this source context -> `Domain Adapter（ドメインアダプター）`
- numeric `平滑` evaluation -> `motion smoothness（モーション滑らかさ）`

`深度制御の実演は乱雑音のみ` is not reader-safe. Replace the whole clause with a source-faithful boundary that does not invent a numeric claim. Required wording:

> 深度条件を含む制御例は定性的な実演に留まり、一般化された定量評価は本稿の消費範囲では確立していない。

### SOL-V-003 — Stable Video Diffusion

Context: `btd075`.
Do not use `厳選潜在動画` as a pseudo-name.
Decisions:
- `厳選潜在動画` -> `Stable Video Diffusion（SVD）`
- `厳選千万部分集合が網全体を上回る` -> `LVD-10Mから得た厳選サブセットLVD-10M-Fが、未選別のLVD-10Mを上回る`
- `人間序列` -> `人間選好評価`

### SOL-V-004 — section naming for AnimateDiff/SVD

Replace heading:
- `動作接続器と厳選潜在動画：個人化の動作化と段階学習`
with:
- `AnimateDiffのMotion ModuleとStable Video Diffusion：個人化の動作化と段階学習`

Equivalent punctuation is allowed; the named identities must remain.

### SOL-V-005 — proprietary/frontier/open-weight wording

Do not use `閉鎖頂点`.
Use:
- `非公開モデル`
or, in the section heading:
- `非公開モデル・開放重みMoEと編集ベンチマーク`

Do not claim `frontier` or SOTA unless the cited source does so and the claim boundary permits it.

### SOL-V-006 — MoE

- `開放混合専門家` -> `開放重みのMixture-of-Experts（MoE）`
- subsequent same-context -> `開放重みMoE`

### SOL-V-007 — benchmark/checkpoint/version wording

- `基準測定` -> `ベンチマーク評価`
- `検査点` -> `チェックポイント`
- `版と検査点の通貨拘束` -> `版・チェックポイント・評価時点を固定して読む必要がある`
- `版と検査点と母集団の三点拘束` -> `版・チェックポイント・母集団を明示して読む`

The phrase `通貨拘束` MUST be zero after repair.

### SOL-V-008 — Wan open-weight boundary

Do not state `開放線は2.2で凍結` unless a source explicitly says frozen.
Required reader-facing boundary:
- `本稿が確認した開放重み系はWan2.2までであり、それ以降の系譜は本稿では確立しない。`

### SOL-V-009 — generic sample/runtime wording

- `単一良標本` -> `単一の良好な生成例`
- `低速高記憶サンプリング` -> `低速・高メモリ消費のサンプリング`
- `乱雑音` when literal random noise -> `ランダムノイズ`
- `要点一括標本` is prohibited. Where it currently denotes expensive video sampling/generation, rewrite conservatively to `高品質動画のサンプリング` without adding a new mechanism claim.

### SOL-V-010 — Movie Gen

Context: `btd076`, abstract-level authority only.
`cast` in the title **A Cast of Media Foundation Models** is metaphorical; do not translate as casting/foundry.
Decision:
- `鋳造` -> remove and rewrite to `メディア基盤モデル群`

Stay within the abstract-level authority boundary.

### SOL-V-011 — Seedance 2.5

Context: `btd117` ByteDance first-party.
Canonical product wording includes single-pass generation, multi-round extension, one-take creation.
Decisions:
- `単走` -> `single pass（1回の生成）`
- `多回合延長` -> `multi-round extension（複数回の延長）`
- product `one-take` may be `ワンテイク` where the source uses that term.

Do not convert Seedance extension rounds into dialogue `マルチターン`.

### SOL-V-012 — first/last frame and outpainting

Product-surface context:
- `首尾frame` -> `開始・終了フレーム`
- `外側描画` when source means outpainting -> `outpainting（アウトペインティング）`

## 10. Product-capstone / API wording

### SOL-C-001 — parallel tool calls

API/tool context:
- `並列道具` -> `並列ツール呼び出し`

### SOL-C-002 — dialogue

- `多回合振る舞い` -> `マルチターン挙動`
- other dialogue `多回合` -> `マルチターン`

### SOL-C-003 — pipeline/storage/local execution

Where the source meaning is unambiguous:
- `管線` -> `パイプライン`
- `磁碟` -> `ディスク`
- runtime-local `局所実行` -> `ローカル実行`
- prose `bench` -> `ベンチマーク`

### SOL-C-004 — Lyria controls

Where `btd111`/`btd112` refer to genre/mood/instrument/vocals:
- `流派` -> `ジャンル`
- rewrite malformed aggregate `音声言語流派音響の制御` to `ジャンル・ムード・楽器・歌声などの制御` only where supported by the cited product/model-card context.

### SOL-C-005 — capability envelope

`包絡` when it means product/model capability envelope -> `対応範囲`.
Do not change mathematical envelope uses without a separate mapping.

### SOL-C-006 — multi-shot

Product video context:
- `多shot` -> `マルチショット`

## 11. Front matter / general prose cleanup decided by Sol

### SOL-F-001 — raw sequence

- `raw系列` -> `生の系列`

### SOL-F-002 — adapter

Technical component `adapter` -> `アダプター`, unless a named product/component is better preserved in English.

### SOL-F-003 — dataset rather than mathematical set

When `集合` denotes datasets such as CIFAR-10, ImageNet-64, LSUN-128:
- rewrite to `データセット`.

Do not change mathematical set usage.

### SOL-F-004 — student model

Distillation context:
- `生徒` when it denotes the student network/model -> `student model（生徒モデル）` on first use, thereafter `生徒モデル`.

## 12. Retain decisions

The following are not global errors and may remain when used in their genuine meanings:

- `母集団` for statistical population.
- `資料` for documents/reference material, not training data/dataset.
- `枠` for conceptual frame/boundary/layout frame, not video frame.
- `力学` for mechanics/physics.
- `符号器` / `復号器` as established Japanese for encoder/decoder where no named component requires English.
- `誘導` as a Japanese gloss for guidance where the edition already defines the relation; named methods such as classifier-free guidance may retain canonical English on first use.
- `版バインド` may remain as established edition-local editorial terminology, but malformed derivatives such as `通貨拘束` must not remain.

## 13. Post-application audit obligations

After applying this map, Muse MUST run all of the following:

1. exact search for every left-hand-side prohibited term above;
2. semantic-context search for variants/synonyms;
3. Issue #533/#539 frozen-regression scans;
4. `main.tex` broad suspicious-translation scan;
5. rendered PDF text broad suspicious-translation scan;
6. citation coverage and `\autocite` comparison, with the one explicit `SOL-CIT-001` exception documented;
7. number/unit semantic comparison;
8. section/label comparison;
9. all-page visual regression.

If Muse finds a suspicious reader-facing term that is not covered by this map, it MUST NOT modify it. Add it to:

`sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r2.md`

with:
- exact term;
- complete sentence;
- section;
- citation/Evidence ID;
- suspected canonical English if directly visible in the already-consumed source;
- no proposed final Japanese wording beyond quoting the source term.

Then continue applying already-authorized mappings; do not invent additional editorial decisions.

## 14. Completion boundary

A Muse execution based on this file does **not** close Issue #543 by itself.

Normal worker stop:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

with Issue #543 still open for Sol final readback.

No Freeze, Release, merge, new Human approval, or new architecture/evidence decision is authorized.
