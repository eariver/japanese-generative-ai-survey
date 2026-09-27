# Japanese Technical Terminology Overtranslation Seed Corpus

Status: `GENERIC QA SEED / READ-ONLY AUTHORITY / NO AUTO-REWRITE`
Date: `2026-09-28`
Scope: Weekly + Special (generic, reusable)
Tracking: `CV2-DM-006` in `docs/core-v2-deferred-maintenance-summary.md`
Prevention tracker: Issue #534 (open)
Origin tracker: Issue #501 (open, W36)
TS-002 edition evidence: Issues #533 / #539 / #543 (all closed as edition-local)
TS-002 source edition: `SP-beyond-text-2026` (`special/beyond-text-2026-work`, released `special/beyond-text-2026`)
Sol/Muse authority: `sources/SP-beyond-text-2026/execution/terminology-issue543/` + `sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue543-*.md`

## 0. What this document is and is not

This document preserves actually observed J-GAS production literalizations as a **generic QA seed corpus** for future Weekly/Special terminology review and for a future read-only lint authority seed.

It is explicitly:

- **not** an automatic replacement dictionary;
- **not** a style policy that prohibits kanji / Sino-Japanese wording;
- **not** an instruction to revert established Japanese technical terminology back to English;
- **not** a substitute for semantic correctness review.

Technical invariant (same as `CV2-DM-006`):

> technically established Japanese wording is allowed; the defect is forced, non-standard, or identity-destroying translation that makes a technically literate Japanese reader reconstruct the English source term.

Established Japanese (e.g. `符号器` / `復号器` / `潜在` / `写像` / `尤度` / `事前分布` / `自己回帰` / `平滑化` in genuine smoothing contexts) must not be blindly reverted. Named entities must not be dissolved into generic Japanese. Every future decision remains source/entity/context-bound with human/Sol review. `auto-rewrite allowed` is always `false` in this corpus.

## 1. Classification vocabulary

- `PROHIBITED_HIGH_CONFIDENCE` — observed form is effectively never acceptable as the technical translation in its stated context; flag unconditionally for review/replacement with the preferred form.
- `REVIEW_REQUIRED` — observed form may be acceptable in some senses but is high-risk in the stated technical sense; requires source/context adjudication (`REPLACE` / `RETAIN` with reason).
- `CANONICAL_IDENTITY_RISK` — observed form destroys or obscures a named model / architecture / method / metric / benchmark / dataset identity, harming searchability and entity binding.
- `SEMANTIC_COLLISION_RISK` — observed form collides with a different established concept (e.g. projection vs zero-shot, sign language vs codec language model, volume-preserving vs normalizing flow).

Multiple classifications may apply to one entry. All entries: `auto-rewrite allowed: false`.

## 2. Seed families

Conventions below:

- `observed`: reader-facing literalization actually seen in TS-002 pre-repair snapshots.
- `canonical`: intended technical concept / source English.
- `preferred`: reader-facing direction actually adopted in TS-002 repair, or review direction for future editions (not a blind substitution rule).
- `provenance`: TS-002 issue / Sol map / Muse candidate source. Counts in §7 are snapshot-only.

### 2.1 zero-shot / speech / codec / consistency

#### 零射影
- observed: `零射影` (e.g. `零射影分類`, `零射影複製`, `零射影の条件づけ`)
- canonical: `zero-shot`
- preferred: `ゼロショット分類` / `ゼロショット音声／話者複製` / `ゼロショット条件`; unify with existing `ゼロショット` / `zero-shot` in-edition
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` (`射影` = projection, distinct concept)
- context/domain: speech / vision / generative conditioning
- provenance: #533 §1; Sol r2 frozen-regression; #534 initial seed
- rationale: `射影` reads as projection; zero-shot meaning unrecoverable without reverse-engineering English
- auto-rewrite allowed: `false`

#### 声器
- observed: `声器` (e.g. `神経声器`, `波形網声器`, `敵対的声器`)
- canonical: `vocoder` / `neural vocoder` / `WaveNet vocoder` / adversarial/GAN vocoder
- preferred: `ボコーダ` / `ニューラルボコーダ` / `WaveNetボコーダ`; source-specific for adversarial/GAN variants
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: speech synthesis / neural vocoding
- provenance: #533 §2
- rationale: non-standard as Japanese speech-tech term; meaning opaque
- auto-rewrite allowed: `false`

#### 符号言語模型 / 符号言語
- observed: `符号言語模型`, `符号言語`
- canonical: `codec language model` / `neural codec language model` / discrete speech-token language model
- preferred: `コーデック言語モデル` / `ニューラルコーデック言語モデル`; contextually `離散音声トークン言語モデル` after source-unit check
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` (misreadable as sign language), `CANONICAL_IDENTITY_RISK`
- context/domain: speech / music token modeling
- provenance: #533 §3
- rationale: `符号言語` collides with sign language; loses codec/token identity
- auto-rewrite allowed: `false`

#### 無撞着模型 / 自己無撞着関数 / 無撞着蒸留 (+ 一致性 residual)
- observed: `無撞着模型`, `自己無撞着関数`, `無撞着蒸留`; residual `一致性` for same family
- canonical: `Consistency Model` / `consistency function` / `consistency distillation`
- preferred: `Consistency Model（整合性モデル）` / `consistency function` / `consistency distillation`; residual `一致性` → `整合性` for this family only
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: generative objectives / distillation
- provenance: #533 §4; Sol r2 SOL-P-005
- rationale: `無撞着` is non-standard as the proper model name and destroys searchability; ordinary logical-consistency uses are out of scope without explicit mapping
- auto-rewrite allowed: `false`

#### ゼロショット素体
- observed: `ゼロショット素体`
- canonical: `zero-shot base / base model / baseline` (source-bound)
- preferred: `ゼロショットのベースモデル` / `ゼロショットベースライン` after rebinding the referent
- classification: `REVIEW_REQUIRED`
- context/domain: speech / capstone baseline wording
- provenance: #533 §8
- rationale: `素体` is unnatural as reader-facing model/baseline wording
- auto-rewrite allowed: `false`

### 2.2 sampling / score / flow / diffusion

#### 抽出推論
- observed: `抽出推論`
- canonical: `sampling` / `inference-time sampling`
- preferred: `推論時サンプリング` / `サンプリング` / `生成手順` by context; do not confuse with statistical extraction or signal sampling
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: generation procedure
- provenance: #533 §5
- rationale: opaque as Japanese; collides with extraction senses
- auto-rewrite allowed: `false`

#### generative contextの標本化
- observed: `標本化` in generative-model context
- canonical: generative `sampling`
- preferred: `サンプリング`; retain `標本化` only for genuine signal-sampling contexts after check
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: generation vs signal processing
- provenance: #533 additional candidates
- rationale: collides signal `標本化` with generative sampling
- auto-rewrite allowed: `false`

#### 標本 (generated-sample sense) / 良質標本 / 単一良標本 / 標本の鮮明さ
- observed: `標本`, `良質標本`, `単一良標本`, `標本の鮮明さ`, `単一良標本` (video), `要点一括標本` / `一括要点標本`
- canonical: generated sample / output; expensive video sampling
- preferred: `サンプル` / `高品質なサンプル` / `単一の良好な生成例` / `サンプルの鮮明さ`; `要点一括標本` / `一括要点標本` → `高品質動画のサンプリング` (no new mechanism claim)
- classification: `REVIEW_REQUIRED`
- context/domain: generative outputs / video cost boundary
- provenance: Sol r2 SOL-G-001, SOL-V-009; Sol r3 SOL-R3-C009
- rationale: `標本` for generated artifacts forces statistical reading
- auto-rewrite allowed: `false`

#### 祖先抽出 (+ 祖先サンプリング concept)
- observed: `祖先抽出`
- canonical: `ancestral sampling`
- preferred: `ancestral sampling（祖先サンプリング）` / `サンプリング` / `生成手順`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: diffusion / score-SDE samplers
- provenance: #543 sampling family
- rationale: `抽出` alone loses sampler identity
- auto-rewrite allowed: `false`

#### 得点整合 / 得点蒸留 / 得点導出
- observed: `得点整合`, `得点蒸留`, `得点導出`
- canonical: `score matching` / `score distillation` / source-specific score-derived objective
- preferred: `score matching（スコアマッチング）` / `score distillation（スコア蒸留）` or source formal name
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: score-based generative modeling
- provenance: #543 score family
- rationale: generic `得点` obscures score-method identity
- auto-rewrite allowed: `false`

#### 得点網
- observed: `得点網`
- canonical: `score network` / `score model`
- preferred: `スコアネットワーク`; optionally `score network（スコアネットワーク）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: score-based modeling architecture
- provenance: #539 §4
- rationale: loses canonical score-network terminology
- auto-rewrite allowed: `false`

#### 流れ整合
- observed: `流れ整合`
- canonical: `Flow Matching`
- preferred: `Flow Matching` / `フローマッチング`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: flow objectives
- provenance: #533 additional candidates
- rationale: proper method name dissolved into generic nouns
- auto-rewrite allowed: `false`

#### 整流流れ
- observed: `整流流れ`
- canonical: `Rectified Flow`
- preferred: `Rectified Flow` / `整流フロー`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: flow objectives
- provenance: #533 additional candidates
- rationale: same as above
- auto-rewrite allowed: `false`

#### 量保存流れ
- observed: `量保存流れ`
- canonical: `normalizing flow(s)` (VITS context; semantic-risk)
- preferred: `normalizing flow（正規化フロー）` with source-specific wording
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` (reads as volume-preserving flow, distinct concept)
- context/domain: speech / VITS lineage
- provenance: #543 §2 (semantic-risk, primary-source read-back required)
- rationale: colliding with `volume-preserving flow`; correctness-critical
- auto-rewrite allowed: `false`

#### 予測子修正子 (+ 修正子)
- observed: `予測子修正子`, bare `修正子` in same context
- canonical: `predictor-corrector` / `corrector`
- preferred: `predictor-corrector（予測子・修正子）`; same-context bare `修正子` → `corrector（修正子）` where needed
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: score-SDE (`btd021`)
- provenance: Sol r2 SOL-P-002
- rationale: sampler proper name split into generic nouns
- auto-rewrite allowed: `false`

#### 再流
- observed: `再流`
- canonical: Rectified Flow `reflow`
- preferred: `reflow（再フロー）`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: Rectified Flow
- provenance: Sol r2 SOL-P-004
- rationale: opaque without method identity
- auto-rewrite allowed: `false`

#### 周辺場 / 標本ごとの条件付き場
- observed: `周辺場`, `標本ごとの条件付き場`
- canonical: Flow Matching marginal / conditional vector fields (`btd027`)
- preferred: `周辺ベクトル場` / `条件付きベクトル場`; sentence: `Flow Matching（フローマッチング）は、周辺ベクトル場を直接扱う代わりに条件付きベクトル場への回帰で学習できるsimulation-freeな定式化を置く`
- classification: `REVIEW_REQUIRED`
- context/domain: Flow Matching formulation
- provenance: Sol r3 SOL-R3-C007; Muse r2 C-005
- rationale: missing `ベクトル場` loses formulation meaning; do not invent sample-level interpretation
- auto-rewrite allowed: `false`

#### 尺度の掃引 / 尺度感度 / 誘導尺度 (technical guidance-scale sense)
- observed: `尺度の掃引`, `尺度感度`, `誘導尺度`, `誘導尺度の掃引`, `潜在拡散の誘導尺度`, `符号器規模と誘導尺度`
- canonical: `guidance-scale sweep` / `guidance scale` / scale sensitivity in CFG context (`btd032`)
- preferred: `ガイダンススケールのスイープ` / `ガイダンススケール`; do not use bare `尺度` for technical guidance scale
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: classifier / classifier-free guidance
- provenance: Sol r10 R10-C006 lineage; Sol r7 scale mappings; #534 context list
- rationale: generic `尺度` obscures CFG parameter identity
- auto-rewrite allowed: `false`

### 2.3 model / network / architecture / component

#### 模型 (+ 生成模型 / 言語模型 / 拡散模型 / 基盤模型 / 判定模型 / 選好模型 / 模型群)
- observed: `模型` across ML `model` contexts
- canonical: ML `model`
- preferred: `モデル` family (`生成モデル`, `言語モデル`, `拡散モデル`, `基盤モデル`, `判定モデル`, `選好モデル`, `モデル群`); retain only if genuinely non-ML general-word context with recorded reason
- classification: `PROHIBITED_HIGH_CONFIDENCE` in ML contexts, otherwise `REVIEW_REQUIRED`
- context/domain: ML models generally
- provenance: #539 §1
- rationale: `模型` is unnatural as ML-model Japanese and harms searchability
- auto-rewrite allowed: `false`

#### 模型票
- observed: `模型票`
- canonical: `model card`
- preferred: `モデルカード`; keep canonical English where the formal artifact is meant
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: model documentation artifact
- provenance: #539 §§1/5
- rationale: over-literalization of proper artifact name
- auto-rewrite allowed: `false`

#### U 網
- observed: `U 網` (e.g. `時刻条件 U 網か Transformer か`)
- canonical: `U-Net`
- preferred: `U-Net`; contextually `時刻条件付きU-Net`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: diffusion / segmentation backbones
- provenance: #539 §2
- rationale: architecture proper name split into generic nouns
- auto-rewrite allowed: `false`

#### 波形網
- observed: `波形網`
- canonical: named `WaveNet` vs generic waveform-generation network (source-bound)
- preferred: `WaveNet` where the named model is meant; otherwise `波形生成ネットワーク`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: speech synthesis lineage
- provenance: #539 §3
- rationale: must not dissolve `WaveNet` identity into generic wording
- auto-rewrite allowed: `false`

#### 単一網
- observed: `単一網` in ML-network context
- canonical: single network
- preferred: `単一ネットワーク`
- classification: `REVIEW_REQUIRED`
- context/domain: generic network wording
- provenance: Sol r2 SOL-P-006
- rationale: `網` alone for network is non-standard in this context
- auto-rewrite allowed: `false`

#### 写像網 / 合成網 / 復元網 / 後段処理網 / 空間制御網 / 音楽制御網 / 雑音予測網
- observed: `写像網`, `合成網`, `復元網`, `後段処理網`, `空間制御網`, `音楽制御網`, `雑音予測網`
- canonical: `mapping network` / `synthesis network` / `reconstruction network` or decoder-side component / `post-processing network` / ControlNet-spatial control / music control component / `noise prediction network`
- preferred: canonical English or natural `〜ネットワーク` after source check (e.g. `mapping network`, `synthesis network`, `ControlNet` where applicable)
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: image / audio / control architectures
- provenance: #543 §11
- rationale: named components dissolved into generic `網`
- auto-rewrite allowed: `false`

#### 事前学習網 (+ 既存拡散網 / 多層網)
- observed: `事前学習網`, `既存拡散網`, `多層網`
- canonical: pretrained network / existing diffusion network / multilayer (T2I backbone) network
- preferred: `事前学習ネットワーク` / source-specific network wording; do not auto-expand
- classification: `REVIEW_REQUIRED`
- context/domain: generic backbone wording
- provenance: Sol r2 network family; Muse r10 R10-C012
- rationale: same `網` overtranslation family
- auto-rewrite allowed: `false`

#### 制御網
- observed: `制御網`
- canonical: control network / ControlNet-adjacent component (source-bound)
- preferred: source-specific canonical or `制御ネットワーク`
- classification: `REVIEW_REQUIRED`
- context/domain: controllable generation
- provenance: mission mandatory family (control section)
- rationale: generic `網` obscures control-component identity
- auto-rewrite allowed: `false`

#### 画素再帰網
- observed: `画素再帰網`
- canonical: `PixelRNN` / `PixelCNN` (source-bound)
- preferred: preserve `PixelRNN` / `PixelCNN`; do not dissolve into generic pixel-recurrence wording
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: autoregressive image modeling
- provenance: Sol r3 final residual (PixelRNN/PixelCNN identity)
- rationale: named model identity at stake
- auto-rewrite allowed: `false`

#### 動作接続器 / 領域接続器
- observed: `動作接続器`, `領域接続器`
- canonical: AnimateDiff `Motion Module` / `Domain Adapter` (`btd074`)
- preferred: `Motion Module（モーションモジュール）` / `Domain Adapter（ドメインアダプター）`; `運動 LoRA` → `Motion LoRA`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: video personalization / adaptation
- provenance: Sol r2 SOL-V-002
- rationale: proper component names literalized into generic connectors
- auto-rewrite allowed: `false`

#### 課題別頭部
- observed: `課題別頭部` (pp.6, 60, 61)
- canonical: task-specific heads / task heads
- preferred: `タスク別ヘッド` or equivalent canonical wording, not anatomical `頭部`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: multitask heads
- provenance: Sol r10 final seed-external audit (f8169436)
- rationale: anatomical literalization of attention/model heads
- auto-rewrite allowed: `false`

#### 問い合わせ行列
- observed: `問い合わせ行列`
- canonical: attention query projection matrix
- preferred: `query projection（クエリ射影）` or `クエリ射影行列`; Tune-A-Video context: `クエリ射影行列（W^Q）`
- classification: `REVIEW_REQUIRED`
- context/domain: attention mechanisms
- provenance: Sol r2 SOL-P-007, SOL-E-002
- rationale: ordinary-Japanese `問い合わせ` for attention queries is opaque
- auto-rewrite allowed: `false`

#### 膨張形式
- observed: `膨張形式`
- canonical: Tune-A-Video `network inflation` (2D `3×3` → pseudo-3D `1×3×3` + temporal attention, `btd050`)
- preferred: `擬似3D畳み込みへのnetwork inflation（3×3→1×3×3）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: video editing architecture
- provenance: Sol r2 SOL-E-001
- rationale: method name replaced by vague form noun
- auto-rewrite allowed: `false`

#### 変換器系 literalization
- observed: `変換器雑音除去器`, `補間変換器`, bare `変換器` for named `Transformer` (55 occurrences reviewed)
- canonical: `Transformer denoiser` / `Diffusion Transformer (DiT)` / `Scalable Interpolant Transformer (SiT)`
- preferred: preserve canonical (`Transformer denoiser`, `Diffusion Transformer (DiT)`, etc.); review only proper-name occurrences source-specifically, not blind global replace
- classification: `PROHIBITED_HIGH_CONFIDENCE` for proper names, otherwise `REVIEW_REQUIRED`; `CANONICAL_IDENTITY_RISK`
- context/domain: named architectures
- provenance: #533 §7
- rationale: proper architecture name confused with generic converter noun
- auto-rewrite allowed: `false`

### 2.4 data / representation / evaluation

#### 類別条件 / 類別脱落 (+ 時刻と類別の条件づけ)
- observed: `類別条件`, `類別脱落`, `時刻と類別の条件づけ`
- canonical: `class conditioning` / `class dropout` / time-and-class conditioning
- preferred: `クラス条件` / `クラスドロップアウト` / `時刻とクラスの条件づけ`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: conditioning / guidance
- provenance: #533 §6
- rationale: `類別` is non-standard for ML class conditioning
- auto-rewrite allowed: `false`

#### 枠 / 枠間 in video-frame sense
- observed: `枠`, `枠間` where video frame is meant
- canonical: `frame` / `inter-frame`
- preferred: `フレーム` / `フレーム間`; retain `枠` only for framework / boundary / box / conceptual-frame senses with reason
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: video frames vs generic frames
- provenance: #539 §§6/frames; Sol r2 SOL-G-003
- rationale: generic `枠` collides distinct frame senses
- auto-rewrite allowed: `false`

#### 文章符号器 (+ 凍結大規模文符号器 / 大規模文符号器 / 文符号器 variants)
- observed: `文章符号器` and large-scale / frozen variants
- canonical: `text encoder`
- preferred: `テキストエンコーダ`; first use may keep `text encoder（テキストエンコーダ）`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: named text-conditioning component
- provenance: #539 §8
- rationale: named component overtranslated; do not ban established `符号器` itself
- auto-rewrite allowed: `false`

#### 交叉注意
- observed: `交叉注意`
- canonical: `cross-attention`
- preferred: `クロスアテンション` or natural `交差注意`; unify in-edition; keep canonical English at first use where needed
- classification: `REVIEW_REQUIRED`
- context/domain: attention conditioning
- provenance: #539 §9
- rationale: consistency + searchability; `交叉` variant is non-standard
- auto-rewrite allowed: `false`

#### 母数 in ML model-parameter sense
- observed: `母数` where ML model parameters are meant
- canonical: model parameters
- preferred: `パラメータ` in ML-parameter contexts; retain `母数` only for genuine statistics-population senses (see §6)
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: parameters vs statistical population
- provenance: #539 context candidates
- rationale: collides statistics `母数` with ML parameters
- auto-rewrite allowed: `false`

#### 資料 in dataset/training-data/corpus sense
- observed: `資料` where training data / dataset / corpus is meant
- canonical: `training data` / `dataset` / `corpus` / source document
- preferred: `学習データ` / `データセット` / `コーパス` by source; retain `資料` only for documents/reference material
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: data terminology
- provenance: #539 context candidates
- rationale: generic `資料` obscures data-identity and training-data boundary
- auto-rewrite allowed: `false`

#### 蔵書 in corpus sense
- observed: `蔵書` (e.g. `LibriSpeech に関する蔵書事実`, `蔵書の目録的事実`)
- canonical: corpus existence / scale / catalog facts
- preferred: `コーパス` / `コーパスの存在・規模` / `目録情報` without upgrading evidence depth
- classification: `PROHIBITED_HIGH_CONFIDENCE` in corpus contexts
- context/domain: speech corpora
- provenance: Sol r10 final seed-external audit
- rationale: library-collection wording unnatural for corpus facts
- auto-rewrite allowed: `false`

#### 標識 / 無標識 / 標識付き in ML label sense
- observed: `標識`, `無標識動画`, `標識付きアライメント`, `雑音付き擬似音素標識`
- canonical: `label` / `unlabeled` / `labeled` (source-by-source)
- preferred: `ラベル` / `ラベルなし` / `ラベル付き` or source-specific equivalent
- classification: `REVIEW_REQUIRED`
- context/domain: labeling / alignment
- provenance: Sol r10 final seed-external audit (distinct from resolved `標識三重`)
- rationale: signage-sense kanji for ML labels is opaque
- auto-rewrite allowed: `false`

#### 問答 in QA/VQA sense
- observed: `問答` (T2I-CompBench / BLIP / multimodal eval, 10 occurrences)
- canonical: `VQA` / `question answering`
- preferred: `VQA（Visual Question Answering／視覚質問応答）` or `質問応答` by source identity
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: multimodal evaluation
- provenance: Sol r10 final seed-external audit
- rationale: generic `問答` loses VQA mechanism identity
- auto-rewrite allowed: `false`

#### 基線 in ML baseline sense
- observed: `基線` in VBench-baseline context
- canonical: `baseline`
- preferred: `ベースライン`; preserve no-ranking boundary
- classification: `REVIEW_REQUIRED`
- context/domain: evaluation baselines
- provenance: Sol r10 final seed-external audit
- rationale: baseline identity + evaluation-boundary clarity
- auto-rewrite allowed: `false`

#### 短片
- observed: `短片` (e.g. `同一装置・短片条件`)
- canonical: short clip / segment (source-bound speech context)
- preferred: `短い音声クリップ条件` / `短区間条件` as source supports
- classification: `REVIEW_REQUIRED`
- context/domain: speech segmentation
- provenance: Sol r10 final seed-external audit
- rationale: Chinese-like literalization of clip/segment
- auto-rewrite allowed: `false`

#### technical 区画 (+ 区画長 / 画素区画 / 16フレーム区画 / 区画自己回帰延長 / 学習区画 / 区画限定)
- observed: `区画` family where chunk / clip / segment / interval is meant
- canonical: `chunk` / `clip` / `interval` (source-by-source)
- preferred: resolve among `チャンク`, `クリップ`, `区間`; existing `区画因果Flow Matching` decision does not adjudicate the broader family
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: temporal / spatial partitioning
- provenance: Sol r10 final seed-external audit
- rationale: one kanji covers distinct partitioning concepts
- auto-rewrite allowed: `false`

#### 多峰入出力
- observed: `多峰入出力`
- canonical: multimodal input/output
- preferred: `マルチモーダル入出力`; do not apply to statistical multimodality
- classification: `REVIEW_REQUIRED`
- context/domain: multimodal I/O
- provenance: Sol r2 SOL-R-004
- rationale: statistical vs multimodal-input collision
- auto-rewrite allowed: `false`

### 2.5 hardware / runtime

#### 民生画像処理装置
- observed: `民生画像処理装置` (e.g. `民生画像処理装置の単一24GB`)
- canonical: consumer GPU hardware
- preferred: `24GBの民生GPU 1基` / `consumer GPU` / `民生向けGPU` preserving source fact
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: GPU hardware
- provenance: #539 §7
- rationale:逐語 hardware description unnatural as reader-facing GPU wording
- auto-rewrite allowed: `false`

#### 消費者用図形処理装置
- observed: `消費者用図形処理装置`
- canonical: consumer GPU
- preferred: `民生GPU`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: GPU hardware
- provenance: Sol r1 readback residual; Sol r2 SOL-G-002
- rationale: same GPU literalization family
- auto-rewrite allowed: `false`

#### 図形処理装置 in GPU sense / 画像処理装置
- observed: `図形処理装置`, `画像処理装置` where GPU is meant
- canonical: `GPU`
- preferred: `GPU`; do not expand into literal component names
- classification: `REVIEW_REQUIRED` (must check non-GPU graphics-hardware senses)
- context/domain: accelerators
- provenance: Sol r2 SOL-G-002
- rationale: generic graphics-device wording for GPU obscures accelerator identity
- auto-rewrite allowed: `false`

#### 中央処理装置
- observed: `中央処理装置`
- canonical: `CPU`
- preferred: `CPU`
- classification: `REVIEW_REQUIRED`
- context/domain: CPUs
- provenance: Sol r2 SOL-G-002; #543 implementation terms
- rationale: same hardware-name family
- auto-rewrite allowed: `false`

#### technical compute senseの装置 (+ 単一装置 / 装置や段階数の拘束)
- observed: `装置` where accelerator / compute device is meant
- canonical: GPU / accelerator / device (source-bound)
- preferred: resolve source-specifically; retain `装置` only for genuine device senses
- classification: `REVIEW_REQUIRED`
- context/domain: runtime hardware
- provenance: Sol maps device contexts; §6 context list
- rationale: generic device noun for compute identity
- auto-rewrite allowed: `false`

#### 浮動32
- observed: `浮動32`
- canonical: `float32`
- preferred: `float32`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: runtime precision (`btd064` DiffWave)
- provenance: Sol r3 source-readback basis
- rationale: precision-identity formatting
- auto-rewrite allowed: `false`

#### 基準測定 in benchmark sense
- observed: `基準測定`
- canonical: `benchmark`
- preferred: `ベンチマーク評価`
- classification: `REVIEW_REQUIRED`
- context/domain: evaluation
- provenance: Sol r2 SOL-G-003, SOL-V-007
- rationale: generic measurement wording for benchmark evaluation
- auto-rewrite allowed: `false`

### 2.6 speech / audio / music

#### 位置鋭敏注意
- observed: `位置鋭敏注意`
- canonical: Tacotron 2 `location-sensitive attention`
- preferred: `location-sensitive attention（位置依存アテンション）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: TTS attention
- provenance: Sol r2 SOL-S-001
- rationale: proper attention-name literalization
- auto-rewrite allowed: `false`

#### 読書音声 (+ 読書英語 / 読み上げ英語音声)
- observed: `読書音声`
- canonical: `read speech`
- preferred: `読み上げ音声`; optionally `read speech（読み上げ音声）`
- classification: `REVIEW_REQUIRED`
- context/domain: speech data
- provenance: #543 §9
- rationale: reading-activity wording for read-speech data
- auto-rewrite allowed: `false`

#### 話声
- observed: `話声`
- canonical: `speech` / voiced speech / utterance (context-bound)
- preferred: `音声` / `発話音声` after checking whether speech / voice / utterance is meant
- classification: `REVIEW_REQUIRED`
- context/domain: speech generally
- provenance: #533 additional candidates
- rationale: ambiguous speech-voice literalization
- auto-rewrite allowed: `false`

#### 三膨張循環
- observed: `三膨張循環`
- canonical: WaveNet `3 dilation cycles`
- preferred: `3回のdilation cycle（膨張畳み込みサイクル）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: WaveNet baseline
- provenance: Sol r2 SOL-S-001
- rationale: proper architectural parameter literalization
- auto-rewrite allowed: `false`

#### 十要素混合
- observed: `十要素混合`
- canonical: `10-component mixture of logistics`
- preferred: `10成分のlogistic mixture（ロジスティック混合）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: Tacotron 2 output distribution
- provenance: Sol r2 SOL-S-001
- rationale: same distribution-name family
- auto-rewrite allowed: `false`

#### 系列網
- observed: `系列網`
- canonical: WaveNet-paper RNN baseline (`LSTM-RNNパラメトリック音声合成`) where that source is meant
- preferred: source-bound; do not auto-apply to other `系列網` occurrences
- classification: `REVIEW_REQUIRED`
- context/domain: speech baseline
- provenance: Sol r2 SOL-S-002
- rationale: generic sequence-network wording for a specific baseline
- auto-rewrite allowed: `false`

#### 群化符号 / 群化後継
- observed: `群化符号`, `群化`, `群化後継`
- canonical: VALL-E 2 `Grouped Code Modeling` + `Repetition Aware Sampling`; units vs method distinction
- preferred: method → `Grouped Code Modeling（グループ化コードモデリング）`; units → `グループ化したcodec code`; prose/model-label `群化後継` → `VALL-E 2` with mechanism column preserved
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: codec language modeling (`btd059`)
- provenance: Sol r2 SOL-S-003; Sol r3 SOL-R3-C002; Muse r2 C-002
- rationale: method-vs-model ambiguity plus proper-name loss
- auto-rewrite allowed: `false`

#### 多能高忠実モデル / 多能 variants
- observed: `多能高忠実モデル`, `多能`, `多用途・高忠実音声生成`
- canonical: `Seed-TTS: A Family of High-Quality Versatile Speech Generation Models`
- preferred: first/heading `Seed-TTS（多用途・高品質音声生成モデル）`; subsequent `多用途・高品質音声生成モデル`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: Seed-TTS descriptor
- provenance: Sol r2 SOL-S-004; Sol r3 SOL-R3-C014; Muse r2 C-012
- rationale: title descriptor inconsistency + proper-name handling
- auto-rewrite allowed: `false`

#### 自然さ得点
- observed: `自然さ得点`
- canonical: `Naturalness MOS` (Seed Audio vendor evaluation, `btd110`)
- preferred: `Naturalness MOS（自然さMOS）` with vendor-attribution boundary preserved
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: speech evaluation
- provenance: Sol r2 SOL-S-005; Sol r3 SOL-R3-C001; Muse r2 C-001
- rationale: metric identity + vendor-claim boundary
- auto-rewrite allowed: `false`

#### 音楽 caps / 音響 caps
- observed: `音楽 caps`, `音響 caps`
- canonical: `MusicCaps` / `AudioCaps`
- preferred: preserve `MusicCaps` / `AudioCaps`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: audio datasets
- provenance: Sol r2 SOL-M-001; Sol r1 residuals
- rationale: dataset proper-name identity loss
- auto-rewrite allowed: `false`

#### 帯域収束
- observed: `帯域収束` where the reported Jukebox metric is meant
- canonical: `spectral convergence`
- preferred: `spectral convergence（スペクトル収束）`
- classification: `REVIEW_REQUIRED`
- context/domain: music evaluation (`btd063`)
- provenance: Sol r2 SOL-M-006
- rationale: metric-name wording
- auto-rewrite allowed: `false`

#### 節 / 副歌 in verse/chorus sense (+ 節・副歌)
- observed: `節`, `副歌`
- canonical: musical `verse` / `chorus`
- preferred: `ヴァース` / `コーラス`; `節・副歌` → `ヴァース／コーラス`; do not apply where `節` is non-musical prose
- classification: `REVIEW_REQUIRED`
- context/domain: music structure
- provenance: Sol r2 SOL-M-007
- rationale: section-meaning collision
- auto-rewrite allowed: `false`

#### 流派 in genre sense
- observed: `流派`
- canonical: musical `genre`; product-control genre/mood/instrument/vocals
- preferred: `ジャンル`; aggregate `音声言語流派音響の制御` → `ジャンル・ムード・楽器・歌声などの制御` only where product context supports it
- classification: `REVIEW_REQUIRED`
- context/domain: music generation control
- provenance: Sol r2 SOL-M-008, SOL-C-004
- rationale: school/sect wording for genre is opaque
- auto-rewrite allowed: `false`

#### 刈込
- observed: `刈込`
- canonical: trimming (Suno editing)
- preferred: `トリミング`
- classification: `REVIEW_REQUIRED`
- context/domain: audio editing
- provenance: Sol r2 SOL-M-008
- rationale: agricultural literalization of edit operation
- auto-rewrite allowed: `false`

#### 続成
- observed: `続成`
- canonical: Stable Audio `continuation`
- preferred: `continuation（継続生成）`
- classification: `REVIEW_REQUIRED`
- context/domain: audio continuation
- provenance: Sol r2 SOL-M-008
- rationale: coined continuation noun
- auto-rewrite allowed: `false`

#### 分割残差符号化
- observed: `分割残差符号化`
- canonical: Moshi/Mimi `split residual vector quantization (split RVQ)` (`btd134`)
- preferred: `split RVQ（分割残差ベクトル量子化）`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: neural codecs
- provenance: Sol r3 SOL-R3-S003
- rationale: proper quantization-method identity
- auto-rewrite allowed: `false`

#### 神経符号 (+ RVQ神経符号)
- observed: `神経符号`, `RVQ神経符号`
- canonical: neural codec tokens/codes; RVQ-based neural codec codes
- preferred: `ニューラルコーデック符号`; `RVQベースのニューラルコーデック符号`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: neural codecs
- provenance: Sol r3 SOL-R3-S003
- rationale: standalone `神経符号` is opaque as a technical term
- auto-rewrite allowed: `false`

#### 残差12帳 / codec contextの帳
- observed: `残差12帳`; codec-context `帳`
- canonical: 12 residual quantizer/codebook levels (MusicLM/MusicGen context)
- preferred: `12段のRVQコードブック` where that source context applies; reception `台帳` senses are out of scope
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: audio codebooks
- provenance: Sol r3 SOL-R3-S004; Muse r10 ledger notes
- rationale: ledger-book kanji for codebook levels
- auto-rewrite allowed: `false`

#### 声素材
- observed: `声素材`
- canonical: voice material / speaker material (source-bound)
- preferred: resolve source-specifically (e.g. voice data / speaker material); do not retain as a standalone technical term without check
- classification: `REVIEW_REQUIRED`
- context/domain: voice data
- provenance: mission mandatory speech family
- rationale: material-noun literalization
- auto-rewrite allowed: `false`

#### 帯域メル / 対数メル (+ MEL distance)
- observed: `帯域メル`, `対数メル`
- canonical: mel-band / log-mel; `MEL distance` where Stable Audio autoencoder quality is meant
- preferred: preserve `MEL distance` identity where the metric is meant; otherwise source-specific mel wording
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: audio features / metrics
- provenance: Sol r3 metric basis (`btd068`); mission mandatory family
- rationale: feature/metric identity formatting
- auto-rewrite allowed: `false`

### 2.7 video / multimodal

#### 外観凍結
- observed: `外観凍結`
- canonical: Make-A-Video appearance/motion split learning (`btd073`)
- preferred: `外観と運動の分離学習`; explanatory: `画像側の外観・テキスト対応を活用し、未ラベル動画から運動を学ぶ分離`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK`
- context/domain: video generation
- provenance: Sol r2 SOL-V-001
- rationale: freeze wording misdescribes split learning
- auto-rewrite allowed: `false`

#### 網データ (+ 網全体)
- observed: `網データ`, `網全体`
- canonical: web data; unfiltered `LVD-10M`
- preferred: `Webデータ`; `網全体` → `未選別のLVD-10M` where that source set is meant
- classification: `REVIEW_REQUIRED`
- context/domain: video datasets
- provenance: Sol r2 SOL-V-001; Sol r3 SOL-R3-C006; Muse r2 C-004
- rationale: net-as-web literalization
- auto-rewrite allowed: `false`

#### 長多場面
- observed: `長多場面`
- canonical: long / multi-scene video
- preferred: `長尺・マルチシーン`
- classification: `REVIEW_REQUIRED`
- context/domain: video data
- provenance: Sol r2 SOL-V-001
- rationale: compressed coined musculature for duration/scene wording
- auto-rewrite allowed: `false`

#### 厳選潜在動画 (+ 厳選千万 / 厳選千万部分集合 / 厳選千万の序列)
- observed: `厳選潜在動画`, `厳選千万`, `厳選千万部分集合`
- canonical: `Stable Video Diffusion (SVD)`; curated subset `LVD-10M-F`
- preferred: `Stable Video Diffusion（SVD）`; `LVD-10Mから得た厳選サブセットLVD-10M-Fが、未選別のLVD-10Mを上回る`; heading must keep named identities
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: video diffusion models
- provenance: Sol r2 SOL-V-003/V-004; Sol r3 SOL-R3-C006; Muse r2 C-004
- rationale: pseudo-proper-name plus dataset-identity loss
- auto-rewrite allowed: `false`

#### 一括要点標本 (see also §2.2)
- observed: `一括要点標本`
- canonical: expensive video sampling/generation boundary (`btd073`)
- preferred: `高品質動画のサンプリング`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: video sampling cost
- provenance: Sol r3 SOL-R3-C009; Muse r2 C-007
- rationale: malformed coined technique-like phrase
- auto-rewrite allowed: `false`

#### 開放重みの混合専門家配置
- observed: `開放重みの混合専門家配置`
- canonical: open-weight `Mixture-of-Experts (MoE)`
- preferred: first `開放重みのMixture-of-Experts（MoE）`; subsequent `開放重みMoE`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: open-weight models
- provenance: Sol r3 SOL-R3-C008 (= r2 SOL-V-006 variant); Muse r2 C-006
- rationale: MoE proper-name dissolution
- auto-rewrite allowed: `false`

#### 開放凍結
- observed: `開放凍結`
- canonical: product lifecycle facts (discontinuation / API retirement / hub migration), not an open-weight freeze
- preferred: `提供終了・API廃止・製品ハブへの移管といったlifecycle上の変化は製品の事実であり、統合への必然性の証拠にはしない`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK`
- context/domain: product capstone
- provenance: Sol r3 SOL-R3-C010; Muse r2 C-008
- rationale: invents an open-weight freeze without source
- auto-rewrite allowed: `false`

#### 開放線 (+ 開放線は2.2で凍結)
- observed: `開放線`, `開放線は2.2で凍結`
- canonical: open-weight lineage (`開放重み系` / `オープンウェイト系`); Wan2.2 boundary
- preferred: `開放重み系`; Wan: `本稿が確認した開放重み系はWan2.2までであり、それ以降の系譜は本稿では確立しない`
- classification: `REVIEW_REQUIRED`
- context/domain: open-weight lineage
- provenance: Sol r3 SOL-R3-C013; Sol r2 SOL-V-008; Muse r2 C-011
- rationale: line-geometry wording for weight-release lineage
- auto-rewrite allowed: `false`

#### 公開系列の線引き
- observed: `公開系列の線引きは二・二まで`
- canonical: Wan2.2 open-weight boundary (same as above)
- preferred: same Wan2.2 boundary sentence with `SOL-CIT-002` binding
- classification: `REVIEW_REQUIRED`
- context/domain: open-weight lineage
- provenance: Sol r3 SOL-R3-C011; Muse r2 C-009
- rationale: uncited front-matter lineage wording
- auto-rewrite allowed: `false`

#### 区画因果流れ / 区画因果Flow Matching
- observed: `区画因果流れ`, `区画因果Flow Matching`
- canonical: CosyVoice 2 `chunk-aware causal flow matching` (`btd133`)
- preferred: first `chunk-aware causal Flow Matching（チャンク認識型因果フローマッチング）`; subsequent `chunk-aware causal Flow Matching`
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: speech synthesis flow
- provenance: Sol r3 SOL-R3-S002
- rationale: chunk/causal/flow identities literalized
- auto-rewrite allowed: `false`

### 2.8 prose / evaluation literalization

#### 人文横並べ
- observed: `人文横並べ`
- canonical: human side-by-side evaluation
- preferred: `人間によるside-by-side評価`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: human evaluation
- provenance: Sol r2 SOL-M-009; Sol r1 residuals
- rationale: humanities wording for human eval is opaque
- auto-rewrite allowed: `false`

#### 人文・自動評価
- observed: `人文・自動評価`
- canonical: human and automatic evaluation
- preferred: `人間評価・自動評価`
- classification: `PROHIBITED_HIGH_CONFIDENCE`
- context/domain: evaluation wording
- provenance: Sol r2 SOL-M-009
- rationale: same human-eval family
- auto-rewrite allowed: `false`

#### 多巡回
- observed: `多巡回`
- canonical: `multi-turn`
- preferred: source-specific `マルチターン` / `multi-turn` wording
- classification: `REVIEW_REQUIRED`
- context/domain: dialogue / extension rounds
- provenance: #543 implementation terms
- rationale: round/turn wording family (see `多回合` below; do not confuse Seedance extension rounds with dialogue turns)
- auto-rewrite allowed: `false`

#### 多回合 / 多回合延長 (+ 多回合振る舞い)
- observed: `多回合`, `多回合延長`, `多回合振る舞い`
- canonical: dialogue `multi-turn` / Seedance `multi-round extension` / multi-turn behavior
- preferred: dialogue → `マルチターン` / `マルチターン挙動`; Seedance product → `multi-round extension（複数回の延長）`; do not convert Seedance rounds into dialogue turns
- classification: `REVIEW_REQUIRED`
- context/domain: dialogue vs product extension
- provenance: Sol r2 SOL-G-003, SOL-V-011, SOL-C-002; Sol r1 residuals
- rationale: same CJK round wording covers distinct turn/round concepts
- auto-rewrite allowed: `false`

#### 区切評価
- observed: `区切評価`
- canonical: `turn-level evaluation`
- preferred: source-specific turn-level wording
- classification: `REVIEW_REQUIRED`
- context/domain: dialogue evaluation
- provenance: #543 implementation terms
- rationale: truncated turn-evaluation wording
- auto-rewrite allowed: `false`

#### 管線
- observed: `管線`
- canonical: `pipeline`
- preferred: `パイプライン`
- classification: `REVIEW_REQUIRED`
- context/domain: system / implementation
- provenance: #543 §10; Sol r2 SOL-C-003
- rationale: plumbing literalization of pipeline
- auto-rewrite allowed: `false`

#### 零初期化
- observed: `零初期化`
- canonical: `zero initialization`
- preferred: `ゼロ初期化`
- classification: `REVIEW_REQUIRED`
- context/domain: initialization wording
- provenance: #543 §10
- rationale: zero-kanji variant inconsistency
- auto-rewrite allowed: `false`

#### 零終端SNR
- observed: `零終端SNR`
- canonical: `zero-terminal SNR`
- preferred: `zero-terminal SNR` / `ゼロ終端SNR`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: diffusion noise schedule
- provenance: #543 §10
- rationale: schedule/terminal-SNR identity formatting
- auto-rewrite allowed: `false`

#### 日程 in scheduler sense
- observed: `日程` where noise/sampling schedule is meant
- canonical: `schedule` / `noise schedule` / `sampling schedule`
- preferred: `スケジュール` / `ノイズスケジュール` / context-specific canonical name
- classification: `REVIEW_REQUIRED`, `SEMANTIC_COLLISION_RISK`
- context/domain: diffusion schedulers
- provenance: #543 §4
- rationale: calendar-schedule wording for technical schedules
- auto-rewrite allowed: `false`

#### 規模則
- observed: `規模則`
- canonical: model `scaling law`
- preferred: `スケーリング則`
- classification: `REVIEW_REQUIRED`
- context/domain: DiT / model scaling
- provenance: Sol r2 SOL-P-003
- rationale: scale-law wording non-standard in this context
- auto-rewrite allowed: `false`

#### 級上げ / 級上げ器
- observed: `級上げ`, `級上げ器`
- canonical: `upsampling` / `upsampler`
- preferred: `アップサンプリング` / `アップサンプラー`
- classification: `REVIEW_REQUIRED`
- context/domain: generation upsampling
- provenance: Sol r2 SOL-P-006
- rationale: grade-raising literalization
- auto-rewrite allowed: `false`

#### 長い結構
- observed: `長い結構`
- canonical: AudioLM `long-term structure` (`btd009`)
- preferred: `長期構造`
- classification: `REVIEW_REQUIRED`
- context/domain: music structure
- provenance: Sol r2 SOL-R-003
- rationale: structure-wording literalization
- auto-rewrite allowed: `false`

#### 鍵盤継続
- observed: `鍵盤継続`
- canonical: AudioLM `piano continuation` (`btd009`)
- preferred: `ピアノ継続`
- classification: `REVIEW_REQUIRED`
- context/domain: music continuation
- provenance: Sol r2 SOL-R-003
- rationale: keyboard-mechanism wording for piano continuation
- auto-rewrite allowed: `false`

#### 基底路
- observed: `基底路`
- canonical: `base channels`
- preferred: source-specific base-channel wording
- classification: `REVIEW_REQUIRED`
- context/domain: diffusion architectures
- provenance: #543 implementation terms
- rationale: path/road literalization of channels
- auto-rewrite allowed: `false`

#### 残差組立て
- observed: `残差組立て`
- canonical: `residual block(s)`
- preferred: source-specific residual-block wording
- classification: `REVIEW_REQUIRED`
- context/domain: residual architectures
- provenance: #543 implementation terms
- rationale: assembly wording for blocks
- auto-rewrite allowed: `false`

#### 整流化線形
- observed: `整流化線形`
- canonical: `ReLU`
- preferred: preserve `ReLU`
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: activations
- provenance: #543 implementation terms
- rationale: activation proper-name dissolution
- auto-rewrite allowed: `false`

#### 検査点 (+ 版と検査点の通貨拘束 / 検査点の通貨拘束)
- observed: `検査点`, `版と検査点の通貨拘束`, `検査点の通貨拘束`
- canonical: model/version `checkpoint`; fixed version/checkpoint/evaluation-time reading boundary
- preferred: `チェックポイント`; `版・チェックポイント・評価時点を固定して読む必要がある`; `版・チェックポイント・母集団を明示して読む`; `通貨拘束` must be zero
- classification: `PROHIBITED_HIGH_CONFIDENCE` for `通貨拘束` phrases, otherwise `REVIEW_REQUIRED`
- context/domain: checkpoints / evaluation boundaries
- provenance: Sol r2 SOL-G-003, SOL-V-007; Sol r1 `検査点の通貨拘束` residual
- rationale: inspection-point wording plus semantically invalid currency-binding literalization
- auto-rewrite allowed: `false`

#### 均衡ある全帯域抽出
- observed: `均衡ある全帯域抽出`
- canonical: DAC / Improved RVQGAN `Balanced data sampling` (`btd008`; EnCodec boundary stays `btd007`)
- preferred: `Balanced data sampling（均衡データサンプリング）` with `SOL-CIT-001` binding
- classification: `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK`
- context/domain: neural codecs (`SOL-CIT-001`)
- provenance: Sol r2 SOL-R-002 / SOL-CIT-001
- rationale: method-name plus citation-binding defect, not wording alone
- auto-rewrite allowed: `false`

## 3. Canonical identity preservation (generic rule)

Generic rule: named models / datasets / metrics / benchmarks / benchmark dimensions keep canonical English / acronyms in reader-facing prose. Do not dissolve them into generic Japanese nouns. Japanese glosses may supplement but must not replace the identity on first use.

### 3.1 TS-002 observed identities (non-exhaustive)

- `MusicCaps`, `AudioCaps` — never `音楽 caps` / `音響 caps` (Sol r2 SOL-M-001).
- `Classification Accuracy Score (CAS)` — never bare `分類得点` in VQ-VAE-2 context (Sol r2 SOL-R-001).
- `Naturalness MOS` — never bare `自然さ得点` for Seed Audio vendor eval (Sol r2 SOL-S-005).
- `FAD` / `KLD` / `CLAP score` — MusicGen canonical metric names, not generic distance/alignment nouns (Sol r2 SOL-M-003).
- `FD` / `IS` / `KL` / `FAD` / `OVL` (+ `REL` where present) — AudioLDM identities (Sol r3 SOL-R3-C003).
- `FD_openl3` / `KL_passt` / `CLAP score` (+ `STFT distance` / `MEL distance` / `SI-SDR`) — Stable Audio Open identities (Sol r3 SOL-R3-C004).
- `FD` / `KL` / `PCM` — Mustango identities (Sol r3 SOL-R3-C005).
- `PixelRNN` / `PixelCNN` — never generic pixel-recurrence wording.
- `Flow Matching` — never `流れ整合`.
- `Rectified Flow` (+ `reflow`) — never `整流流れ` / bare `再流`.
- `Grouped Code Modeling` (+ `Repetition Aware Sampling`) — never `群化符号` / `群化` alone for the method.
- `Motion Module` (+ `Motion LoRA`, `Domain Adapter`) — never `動作接続器` / `領域接続器`.
- `U-Net` — never `U 網`.
- `WaveNet` — never `波形網` where the named model is meant.
- `MuLan Cycle Consistency (MCC)`, `FD`, `OVL`, `REL` — MusicLM identities (Sol r2 SOL-M-002).
- `CLIP-FID` / `CLIPSIM`, `FVD` / `IS`, `FID` / `IS`, `FID-avg` / `IS-avg`, `FID-first` / `IS-first` — Make-A-Video / Video Diffusion Models / Imagen Video table identities (Sol r3 basis).
- `chunk-aware causal flow matching`, `split residual vector quantization (split RVQ)` — CosyVoice 2 / Moshi-Mimi identities.
- `End-to-End` — never `端末間統合` / `端末間`.
- `Batch Normalization` — never `集合同期` where the component is meant.
- `Inception Score (IS)`, `Fréchet Inception Distance (FID)`, `Perceptual Path Length (PPL)` — never generic `識別得点` / `分類得点` / `分布距離` / `知覚経路` where the metric is meant.
- `Mean Opinion Score (MOS)`, speaker-similarity MOS, `intelligibility` — never `平均意見値` / `類似度意見値` / `可知度` where the metric is meant.
- `Griffin-Lim`, `location-sensitive attention`, dilation-cycle / logistic-mixture parameters — Tacotron-family identities.
- `Balanced data sampling` — DAC identity with `btd008` binding.

Policy: converting benchmark / metric / dataset / model identity into generic reader-facing kanji loses entity identity and searchability. Always preserve the canonical identity; add Japanese explanation only as a supplement.

### 3.2 VBench / VBench-2.0 dimension literalization seeds

Observed in TS-002 evaluation chapter; all require source-bound review against accepted VBench / VBench-2.0 authority rather than word-for-word patching:

- `RAFT 動態`
- `LAION 美観`
- `MUSIQ 撮像`
- `主体整合` (cf. canonical `Subject Consistency`)
- `複雑筋`
- `動空間` (cf. canonical `Dynamic Degree`)
- `CoTracker 撮影法`
- `個体保持`
- `均一プロンプト精製`

Each entry:

- observed: as listed
- canonical: corresponding official VBench / VBench-2.0 dimension identity (source-bound; do not guess beyond consumed authority)
- preferred: preserve official dimension English identity; add Japanese gloss only as supplement
- classification: `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK`
- context/domain: video evaluation dimensions
- provenance: Sol r10 final seed-external audit (f8169436)
- rationale: literalized / identity-losing dimension labels harm benchmark comparability
- auto-rewrite allowed: `false`

## 4. Context-dependent terms (never global-deny)

The following are **not** globally prohibited. Each lists the technical sense that makes it review-required.

- `母数` — review-required only when ML model parameters are meant (`パラメータ` preferred); retain for genuine statistics-population senses.
- `案内` — review-required only when generative `guidance` (e.g. classifier / classifier-free guidance) is meant; named methods keep canonical English on first use.
- `資料` — review-required only when training data / dataset / corpus is meant; retain for documents/reference material.
- `枠` — review-required only when video/image `frame` is meant; retain for framework / boundary / box / conceptual-frame senses.
- `標本` — review-required only when generated samples/outputs are meant (`サンプル` / `生成例` preferred); retain for genuine statistical-sampling terminology.
- `真値` — review-required; distinguish `ground truth` / reference / natural-speech senses source-specifically.
- `呼び水` — review-required; distinguish `priming` / `prompt` / continuation-context senses.
- `立体化` — review-required; distinguish `stereo` / stereo-generation senses.
- `抽出` — review-required; distinguish `sampling` / generation-procedure / extraction senses; do not blind-replace bare nouns.
- `得点` — review-required; distinguish score-based-modeling / metric-score / ordinary-score senses.
- `分布距離` — review-required; distinguish named-metric (e.g. FID-family) vs generic-concept uses.
- `集合` — review-required only when datasets (e.g. CIFAR-10 / ImageNet-64 / LSUN-128, StyleGAN eval sets, FID eval sets) are meant (`データセット` preferred); retain mathematical-set uses.
- `装置` — review-required only when accelerator/compute-device identity is meant; retain genuine device senses.
- `区画` — review-required only when chunk / clip / segment / interval is meant; existing `区画因果Flow Matching` decision does not cover the broader family.
- `基線` — review-required only when ML `baseline` is meant (`ベースライン` preferred).
- `標識` — review-required only when ML `label` is meant (`ラベル` family preferred).

All: `auto-rewrite allowed: false`. Every `REPLACE` / `RETAIN` needs a recorded source/context reason. Do not promote these to global prohibited terms.

## 5. Historical occurrence counts (snapshot-only, not generic frequency)

Counts below are **observations in specific `SP-beyond-text-2026` candidate snapshots** (#533 / #539 era), not generic cross-edition frequencies. Do not treat them as expected rates.

- `零射影`: 32 (#533)
- `声器`: 34 (#533)
- `符号言語系`: 14 (#533)
- `無撞着系`: 11 (#533)
- `抽出推論`: 27 (#533)
- `模型`: 約137 (#539)
- `U 網`: 約14 (#539)
- `波形網`: 約5 (#539)
- `得点網`: 約2 (#539)
- `枠間`: 約6 (#539)
- `民生画像処理装置`: 約5 (#539)
- `文章符号器`: 約3 (#539)
- `交叉注意`: 約19 (#539)
- `母数`: 約10 (#539, context-dependent)
- `案内`: 約25 (#539, context-dependent)
- `資料`: 約81 (#539, context-dependent)

Future lint corpus scans must collect **edition-crossing recurrence frequency separately** (e.g. per-edition scan records with edition ID, candidate SHA, PDF SHA, term, count, disposition). Snapshot counts above must not be copied as thresholds. Structure future records as:

```text
edition / candidate_sha / pdf_sha / term / classification / count / disposition / scan_tool_version
```

## 6. Provenance and maintenance

- Primary TS-002 ledger: `sources/SP-beyond-text-2026/execution/terminology-issue543/terminology-decision-ledger.{json,md}` (276 rows at closure: `REPLACE 262 / RETAIN 14 / ESCALATE 0`).
- Sol authoritative maps r2–r10: `sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-*.md`.
- Muse candidate returns: `sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-*.md`.
- Sol readbacks: `sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue543-*.md`, including final seed-external audit `sol-terminology-readback-issue543-r10-final-seed-external-20260927.md` + `sol-authoritative-terminology-map-r10-r11-final-seed-external-20260927.md`.
- Human disposition closing #543 and transferring residuals to #534 is recorded in Issue #543 comments (2026-09-27).
- This seed de-duplicates #533 / #539 / #543 + post-seed Sol/Muse findings. If future editions find contradictions, do not edit history; append a reviewed exception record with provenance.
- Future machine-readable glossary / read-only lint must consume this file as an **authority seed only**, with a reviewed exception mechanism and no auto-rewrite.
- Shared Core remains frozen; no implementation is authorized by this document.
