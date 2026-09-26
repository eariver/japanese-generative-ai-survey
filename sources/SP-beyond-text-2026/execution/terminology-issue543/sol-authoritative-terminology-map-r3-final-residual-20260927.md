# TS-002 Issue #543 — Sol authoritative terminology map r3 (final residual)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / FINAL_RESIDUAL / APPLY_WITHOUT_REINTERPRETATION`

## 1. Authority

This file is the Sol editorial authority for the residual terminology pass after Human Publication Preview r8.

It **supplements and supersedes only where explicitly stated**:

- `sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r2-20260926.md`

All correct r2 decisions remain frozen. Muse MUST NOT reinterpret either map.

Muse's role in the next repair is limited to exact application, ledger synchronization, invariant checks, build, rendered-text audit, and visual QA. If a reader-facing term is not covered by r2 or this r3 map, Muse MUST NOT invent a wording; it must return the occurrence to Sol.

Issue #529 semantic depth, Evidence status, claim boundaries, Architecture, section order, numerical meaning, vendor attribution, closed-system boundaries, and Frozen Core v2 remain unchanged.

## 2. Source-readback basis used by Sol

The following identities were resolved by Sol against the already-consumed primary/source authorities before writing this map:

- `btd059` VALL-E 2: **Grouped Code Modeling** and **Repetition Aware Sampling**.
- `btd064` DiffWave: float32 runtime wording and diffusion waveform synthesis context.
- `btd067` AudioLDM: table columns **FD / IS / KL / FAD / OVL / REL**.
- `btd068` Stable Audio Open: **FD_openl3 / KL_passt / CLAP score**; autoencoder reconstruction metrics **STFT distance / MEL distance / SI-SDR**.
- `btd069` Mustango: objective metrics **FD / FAD / KL** and controllability metric **PCM** among the music-theory control metrics.
- `btd070` Video Diffusion Models: UCF-101 **FID / IS**; image-video joint-training table **FVD / FID-avg / IS-avg / FID-first / IS-first**.
- `btd071` Imagen Video: **oscillating guidance**; distillation table **CLIP Score / CLIP R-Precision / Sampling Time**; original 618 s versus distilled 35 s (~18x).
- `btd073` Make-A-Video: MSR-VTT **CLIP-FID / CLIPSIM**; UCF-101 **FVD / IS**.
- `btd133` CosyVoice 2: **chunk-aware causal flow matching**.
- `btd134` Moshi/Mimi: **split residual vector quantization (split RVQ)** and semantic/acoustic token separation.

No new technical authority is created by this file; this is editorial/source read-back over already accepted authority.

## 3. Muse-returned candidates — final Sol decisions

### SOL-R3-C001 — `自然さ得点`

Capstone summary sentence currently says `A/B選好や可用率や自然さ得点...`.

Decision:

- replace `自然さ得点` with `Naturalness MOS（自然さMOS）` when summarizing the Seed Audio vendor evaluation already discussed in the same capstone block;
- retain the vendor-attribution and independent-validation boundary;
- do not imply that Lyria/Stable Audio use the same metric unless their cited source explicitly does.

Preferred sentence shape:

> A/B選好や可用率、Naturalness MOS（自然さMOS）などのベンダー図表は、各提供元の条件付き主張として読む。

### SOL-R3-C002 — `群化後継`

Context: `btd059` VALL-E 2.

Decision:

- prose `群化後継の数値的主張...` -> `VALL-E 2の数値的主張...`;
- table row label `群化後継` -> `VALL-E 2`;
- mechanism column remains `Grouped Code Modeling（グループ化コードモデリング）＋Repetition Aware Sampling（反復回避サンプリング）`.

Do not use `群化後継`.

### SOL-R3-C003 — AudioLDM metric identity (`btd067`)

The current generic nouns lose metric identity. Preserve the exact existing numbers and restore only their labels.

Required number-to-metric binding:

- `23.31` / `47.68` -> `FD`;
- `8.13` / `4.01` -> `IS`;
- `1.59` / `2.52` -> `KL`;
- `1.96` / `7.75` -> `FAD`;
- `65.91` / `45.0` -> `OVL`.

Therefore the comparison sentence must read semantically as:

> AudioCaps検証条件でFD $23.31$対$47.68$、IS $8.13$対$4.01$、KL $1.59$対$2.52$、FAD $1.96$対$7.75$、OVL $65.91$対$45.0$と報告された。

Do **not** add new numeric tokens such as the REL values that are not already present in the manuscript.

Corresponding summary/table occurrences using generic `距離 / 指標 / 乖離 / 全体` with these same numbers must be normalized to the same metric identities.

### SOL-R3-C004 — Stable Audio Open metric identity (`btd068`)

For AudioCaps:

- `78.24` -> `FD_openl3 78.24`;
- `2.14` -> `KL_passt 2.14`;
- `0.29` -> `CLAP score 0.29`;
- baseline `103.66` / `101.11` in the same table are also `FD_openl3` values, not generic `距離`.

For Song Describer instrumental reconstruction / autoencoder quality where existing numbers are already present:

- use canonical `STFT distance`, `MEL distance`, and `SI-SDR` identities when the sentence binds those values;
- do not introduce additional numbers absent from the manuscript.

Replace malformed summaries such as `開放距離` with the actual metric name, e.g. `FD_openl3`.

### SOL-R3-C005 — Mustango metric identity (`btd069`)

The existing three-number sequences are TestA / TestB / FMACaps results.

- `26.35 / 25.97 / 25.18` -> `FD`;
- `1.21 / 1.12 / 1.16` -> `KL`;
- `11.64 / 17.99` in the cited controllability comparison -> `PCM` values, not generic `拍クロマ`.

Where existing text names `専門家音楽性`, retain that subjective axis if it is already bound to the source; do not conflate it with PCM.

### SOL-R3-C006 — `集合` variants

Decisions by semantic context:

- StyleGAN evaluation `非構造集合` -> `非構造データセット`;
- SVD `厳選千万部分集合` / `厳選千万` -> `LVD-10M-F`;
- SVD `網全体` when it means the unfiltered source set -> `未選別のLVD-10M`;
- FID definition `生成集合` -> `生成サンプル集合`;
- FID definition `大規模実集合` / `実集合` -> `実データ集合`;
- FID paragraph `試行集合` when it names CelebA/CIFAR-10/SVHN/LSUN -> `評価データセット`.

Do not replace mathematical set terminology outside these bound contexts.

### SOL-R3-C007 — Flow Matching `標本ごとの条件付き場`

Context: `btd027`.

Decision:

- `周辺場` -> `周辺ベクトル場`;
- `標本ごとの条件付き場` -> `条件付きベクトル場`.

Preferred sentence:

> Flow Matching（フローマッチング）は、周辺ベクトル場を直接扱う代わりに条件付きベクトル場への回帰で学習できるsimulation-freeな定式化を置く。

Do not invent a new sample-level interpretation beyond the consumed source.

### SOL-R3-C008 — `開放重みの混合専門家配置`

Decision:

- first use -> `開放重みのMixture-of-Experts（MoE）`;
- subsequent -> `開放重みMoE`.

This is the same concept already decided in r2 SOL-V-006; apply it to the remaining grammatical variant.

### SOL-R3-C009 — `一括要点標本`

Context: `btd073` video-generation cost boundary.

Decision:

- `一括要点標本` -> `高品質動画のサンプリング`.

Do not create a named technique from this malformed phrase.

### SOL-R3-C010 — `開放凍結`

In the capstone lifecycle sentence, do not use `開放凍結`.

Rewrite the aggregate lifecycle statement using only facts already established in the same subsection:

> 提供終了・API廃止・製品ハブへの移管といったlifecycle上の変化は製品の事実であり、統合への必然性の証拠にはしない。

Do not infer an open-weight freeze unless a specific source says so.

### SOL-R3-C011 — `公開系列の線引き`

The Wan boundary must use the already-authorized r2 wording:

> 本稿が確認した開放重み系はWan2.2までであり、それ以降の系譜は本稿では確立しない。

The current uncited front-matter occurrence must not remain as `公開系列の線引きは二・二まで`.

See `SOL-CIT-002` below for the required citation binding.

### SOL-R3-C012 — mathematical/image smoothing

`平滑化` / `過度の平滑化` in the btd028 / btd046 / btd081 contexts is standard reader-facing Japanese and is **RETAIN**.

Do not replace it merely because it appeared in the candidate list.

### SOL-R3-C013 — `開放線`

Both residual uses are reader-awkward.

- Wan context -> `開放重み系`;
- Stable Audio Open / open-model context -> `開放重み系` or grammatically `オープンウェイト系`.

Do not retain `開放線`.

### SOL-R3-C014 — Seed-TTS descriptor unification

All Seed-TTS descriptor variants in the manuscript must use:

- first/heading: `Seed-TTS（多用途・高品質音声生成モデル）`;
- subsequent generic: `多用途・高品質音声生成モデル`.

Remove residual `多用途・高忠実音声生成` and `多能` variants.

## 4. Sol independently discovered residuals

### SOL-R3-S001 — residual `端末間` variants

In the VITS / end-to-end TTS lineage:

- table label `端末間` -> `End-to-End`;
- `話者条件端末間` -> `話者条件付きEnd-to-End`;
- any residual `端末間統合` remains governed by r2 -> `End-to-End（エンドツーエンド）統合`.

Do not use `端末間` as a translation of end-to-end.

### SOL-R3-S002 — CosyVoice 2 causal flow terminology

Context: `btd133`.

Canonical term: **chunk-aware causal flow matching**.

Replace:

- `区画因果Flow Matching` / `区画因果流れ`

with:

- first use: `chunk-aware causal Flow Matching（チャンク認識型因果フローマッチング）`;
- subsequent: `chunk-aware causal Flow Matching`.

### SOL-R3-S003 — Moshi/Mimi quantization terminology

Context: `btd134`.

Canonical term: **split residual vector quantization (split RVQ)**.

Replace:

- `分割残差符号化` -> `split RVQ（分割残差ベクトル量子化）`.

For semantic/acoustic code wording:

- `神経符号` -> `ニューラルコーデック符号` when it denotes neural codec tokens/codes;
- synthesis summary `RVQ神経符号` -> `RVQベースのニューラルコーデック符号`.

Do not use `神経符号` as a standalone reader-facing technical term.

### SOL-R3-S004 — codebook terminology

MusicLM / MusicGen residual literalization:

- `残差12帳` -> `12段のRVQコードブック` where the source context is the 12 residual quantizer/codebook levels;
- `各帳を一段ずつずらして` -> `各コードブックを1ステップずつずらして`;
- other codec-codebook `帳` in the same contexts -> `コードブック`.

Do not globally replace ordinary Japanese `帳` outside codec contexts.

### SOL-R3-S005 — `float32`

DiffWave runtime context:

- `浮動32` -> `float32`.

### SOL-R3-S006 — waveform / mel terminology

In TTS/audio model descriptions:

- `声素材` when it means speech/audio material -> `音声` or `音声データ`;
- `帯域メル` when it denotes mel targets -> `メルスペクトログラム` (retain an explicit band count where already present, e.g. `80バンドのメルスペクトログラム`);
- `対数メル` -> `log-melスペクトログラム` or `対数メルスペクトログラム`, consistently within the section.

Do not alter numerical dimensions or frame settings.

### SOL-R3-S007 — PixelRNN identity

Context: `btd017`.

Replace reader-facing `画素再帰網` with:

- `PixelRNN/PixelCNN系` where the sentence discusses the paper family and its row/diagonal recurrent and masked-convolution variants;
- use `PixelRNN` or `PixelCNN` only where the specific architecture is unambiguous.

Do not leave the pseudo-name `画素再帰網`.

### SOL-R3-S008 — generic network residuals

Bound, unambiguous ML-network contexts:

- `既存拡散網` -> `既存の拡散モデル`;
- `雑音予測網` -> `ノイズ予測ネットワーク`;
- `音楽制御網` -> `音楽制御ネットワーク`;
- `事前学習網` / `制御網` -> `事前学習ネットワーク` / `制御ネットワーク`.

Named architectures/components continue to use their canonical names.

### SOL-R3-S009 — `連合学習`

Context: `btd070` Video Diffusion Models jointly training images and videos.

Canonical source wording is **joint training**.

Replace:

- `連合学習` -> `画像・動画の共同学習` or grammatically `共同学習`.

Do not imply federated learning.

### SOL-R3-S010 — Video Diffusion Models metrics (`btd070`)

Restore metric identities without changing numeric tokens:

- UCF-101 `295` -> `FID 295`;
- UCF-101 `57` -> `IS 57`;
- real-data `60.2` -> `IS 60.2`;
- prediction values `68.19 / 66.92` -> `FVD` values in the cited prediction context;
- text-conditioned image-video joint-training `202.28 / 205.42 -> 57.84 / 60.72` -> `FVD`;
- where the manuscript retains the corresponding `37.52 / 37.40 -> 15.57 / 15.44`, label them `FID-avg`;
- where `7.91 / 7.58 -> 9.32 / 8.82` are retained, label them `IS-avg`.

Do not use generic `距離 / 指標 / 整合` for these named metrics.

### SOL-R3-S011 — Imagen Video terminology and metrics (`btd071`)

Replace:

- `振動誘導` -> `oscillating guidance（振動型ガイダンス）`;
- `整合 25.03 / 25.19` -> `CLIP Score 25.03 / 25.19` in the distillation comparison;
- `618秒 -> 35秒` remains `Sampling Time` / sampling time;
- `約18倍速` may remain as the source's approximately 18x faster sampling statement.

Where the manuscript says `256と128段階`, clarify only grammatically as original base/SR sampling steps; do not change the numbers.

### SOL-R3-S012 — Make-A-Video metrics (`btd073`)

Restore named identities:

- `13.17` -> `CLIP-FID 13.17` in the zero-shot MSR-VTT context;
- `0.3049` -> `CLIPSIM 0.3049`;
- `367.23` -> `FVD 367.23` in the zero-shot UCF-101 context;
- `33.00` -> `IS 33.00`;
- fine-tuned `82.55 / 81.25` must be bound according to the existing sentence/source table as `IS 82.55 / FVD 81.25`, without reordering the existing numeric tokens beyond grammatical clarity.

Replace `分別条件の指標` with the actual `IS` wording in this context.

### SOL-R3-S013 — text/media terminology family

In ML/media technical prose where `文章` is a literal translation of English `text`, use `テキスト`.

Bound replacements include:

- `文章条件` -> `テキスト条件`;
- `文章埋め込み` -> `テキスト埋め込み`;
- `文章画像` -> `テキスト・画像`;
- `文章動画` -> `テキスト・動画`;
- `対文章動画データ` -> `テキスト・動画ペアデータ`;
- `文章音響` -> `テキスト・音響`;
- `文章音楽` -> `テキスト・音楽`;
- `文章からの画像生成` -> `テキストからの画像生成`;
- `文章整合` -> `テキスト整合`.

Retain ordinary prose uses of Japanese `文章` where the object truly is a written sentence/document rather than a model text modality.

### SOL-R3-S014 — AudioLDM CLAP / mixup wording

Context: `btd067`.

Replace malformed literalizations where present:

- `対照言語音響整合` -> `CLAPによるテキスト・音響アライメント`;
- `音響のみ混合` when it denotes the paper's audio-domain mixup augmentation -> `audio mixup augmentation（音響mixup）`.

Do not infer a different training mechanism.

### SOL-R3-S015 — editing terms in AudioLDM context

Where `btd067` refers to the paper's zero-shot audio manipulations:

- `塗り足し` -> `inpainting（インペインティング）`;
- `浅い逆行` -> `shallow reverse diffusion（浅い逆拡散）` when referring to style-transfer initialization.

### SOL-R3-S016 — `joint` product wording

Capstone video/audio product prose:

- section heading `映像：joint化と短区間・長距離の分離` -> `映像：音声・映像統合と短区間・長距離の分離`;
- `音声映像のjoint生成` -> `音声・映像の同時生成`.

Do not infer architecture from this product-surface wording.

### SOL-R3-S017 — Ray keyframe wording

Context: `btd122` Ray3.

- `首尾keyframe` -> `開始・終了キーフレーム`;
- `16 keyframe` -> `16キーフレーム`.

### SOL-R3-S018 — reception prose defects

Context: `btd139` reception record.

- `制作者管への導入` -> `制作者workflowへの導入`;
- duplicated `ベンダーによる人間評価への言及への言及` -> `ベンダーによる人間評価への言及`.

These are editorial corrections only; X remains reception/deployment/failure evidence and is not promoted to technical authority.

### SOL-R3-S019 — synthesis English/Japanese residuals

In the concluding synthesis:

- media list `frame` -> `フレーム`;
- `RVQ神経符号` -> `RVQベースのニューラルコーデック符号`;
- `token rate` -> `トークンレート` or `token rate（トークンレート）` on first use;
- `tractable な系列` -> `計算可能な規模の系列`.

### SOL-R3-S020 — product/lifecycle residual wording

Bound capstone cleanup:

- `多能hub` -> `統合型hub`;
- `秒歩` in Runway pricing/generation context -> `秒単位の生成条件`;
- `subversion drift` -> `サブバージョン間の差分`;
- GPT-Live `同時聴話` -> `同時リスニング・発話`;
- `生翻訳` -> `リアルタイム翻訳`.

Do not change named API/product terminology otherwise.

## 5. Citation-binding exceptions

### SOL-CIT-001 — retained from r2

DAC Balanced data sampling claim must bind to `btd008`, while the EnCodec boundary remains bound to `btd007`.

### SOL-CIT-002 — Wan2.2 open-weight boundary

The residual front-matter claim about the verified open-weight lineage must be rewritten to the r2 SOL-V-008 wording and bound to `btd124`:

> 本稿が確認した開放重み系はWan2.2までであり、それ以降の系譜は本稿では確立しない\autocite{btd124}。

This is an explicit Sol-authorized citation insertion because the existing sentence has no local citation despite making a source-bounded lineage claim.

No other citation addition/removal/rebinding is authorized. Any additional citation need requires stop-and-report.

## 6. Retain decisions

The following are intentionally retained when used in their genuine meanings:

- mathematical/image `平滑化` and `過度の平滑化`;
- statistical `標本` where it truly means a statistical sample rather than a generated artifact;
- `母集団` for statistical population;
- `符号器` / `復号器` where established Japanese is clearer and no named component identity is lost;
- `枠` for conceptual/boundary/layout uses;
- ordinary Japanese `文章` where it means prose/sentence/document rather than the ML text modality.

## 7. Required zero/residual scans after application

In addition to all r2 forbidden-term scans, the next worker pass must verify reader-facing zero or no-malformed-use for:

- `群化後継`
- ML end-to-end sense `端末間`
- `区画因果`
- neural-codec sense `神経符号`
- codec sense `帳`
- `浮動32`
- `画素再帰網`
- ML network sense residual `雑音予測網 / 音楽制御網 / 事前学習網 / 制御網`
- video joint-training sense `連合学習`
- Imagen Video sense `振動誘導`
- `分別条件`
- ML-text modality compounds `文章画像 / 文章動画 / 文章音響 / 文章音楽`
- `対照言語音響整合`
- audio-editing sense `浅い逆行`
- capstone `joint化`
- `首尾keyframe`
- `制作者管`
- duplicated `への言及への言及`
- synthesis raw `frame`
- `RVQ神経符号`
- `多能hub`
- `秒歩`
- `開放線`
- `開放凍結`
- `自然さ得点`
- `公開系列の線引き`

Named metric numbers listed in sections 3–4 must also be checked so that none remain attached only to generic `距離 / 指標 / 乖離 / 整合 / 全体` where the canonical metric identity has been decided above.

## 8. Execution boundary

This map does not itself create a Human Gate decision.

The current r8 candidate is already at `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending`. Frozen Core v2 has no legal route back to `DRAFT_COMPLETE` without a new Human Publication Preview revision.

Therefore the next editing execution must not begin until the Human Owner explicitly authorizes the next Publication Preview `REQUEST_CHANGES` revision for this final residual map.

When that authority exists, the worker may use only the existing Frozen Core v2 mechanism, edition-local writes, and the exact r2+r3 Sol maps. No Core v2 modification is permitted.
