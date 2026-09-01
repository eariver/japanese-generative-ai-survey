# Thematic Special Backlog

Status: planning backlog  
Established: 2026-08-12

## 1. Purpose

This document records candidate topics for future **Thematic Special** editions of the Japanese Generative AI Technical Survey.

Thematic Special itself is defined in `docs/special-editions.md` as an edition that reconstructs the technical history or current state of one topic, model family, ecosystem, region, or architectural trend. This backlog is intentionally separate from the issue tracker: entries here are editorial ideas, not defects, review findings, or active production tasks.

An entry in this document does **not** mean that publication has been scheduled. Evidence collection, issue architecture, drafting, validation, visual review, Freeze, and Release remain governed by the normal Special lifecycle.

## 2. Status model

- `IDEA` — initial editorial concept; scope may still change substantially.
- `SCOPED` — core question, approximate boundaries, and major angles are defined.
- `SELECTED` — chosen for future production; create the production issue / working artifacts at this point.
- `ACTIVE` — evidence collection, architecture, drafting, or publication work is in progress.
- `RELEASED` — published as a Thematic Special.
- `PARKED` — intentionally deferred without discarding the concept.

The backlog should remain lightweight. GitHub Issues are used once an edition becomes an actionable production task rather than merely an editorial candidate.

---

## TS-001 — 中国Generative AIの台頭

**Status:** `SCOPED`

### 仮題

**中国Generative AIの台頭 — DeepSeek・Qwen・GLM・KimiとOpen Weight**

### Core question

中国発のGenerative AIは、どのような技術的・ecosystem上の発展を経て、現在のFrontier AI競争における主要勢力となったのか。

### Scope

中心となるmodel family / ecosystem:

- DeepSeek
- Qwen
- GLM
- Kimi

必要に応じて系譜上の補助線として扱う候補:

- MiniMax
- Yi
- Baichuan
- その他、中国LLM / foundation model史を理解するために必要なmodel family

横断して扱う論点:

- 中国LLM / foundation modelの技術史
- reasoning、coding、long context、agentic capabilityへの展開
- training / inference efficiencyとserving ecosystem
- 中国国内のcloud / developer ecosystem
- Open Weight modelの普及と競争上の意味
- local inference、fine-tuning、research reproducibilityへの波及
- Open SourceとOpen Weightの区別
- license、redistribution、commercial use、再現可能性の境界
- closed frontier modelとの競争関係

### Key angle

単純な「米国対中国」の性能競争としてではなく、**model、weights、inference stack、developer ecosystem、distribution strategyがどのように結び付き、現在の競争構造を形成したか**を追う。

Open Weightは末尾の補足論点ではなく、中国勢の成長と国際的なdeveloper adoptionを理解するための横断軸として扱う。

### Boundary / caution

- model capabilityの比較は、異なるbenchmark・version・evaluation conditionを安易に横断しない。
- 「中国勢」という地理的括りだけで技術戦略を同質化せず、各organization / model familyの差を維持する。
- policy / geopoliticsを扱う場合も、技術史の説明に必要な範囲へ限定し、政治的評価とtechnical evidenceを分離する。

---

## TS-002 — Beyond Text: Generative Media

**Status:** `SCOPED`

### 仮題

**Beyond Text — 画像・音声・音楽・映像生成AIの技術史**

### Core question

LLMとは異なる系譜を持つ非テキスト生成AIは、どのように発展し、現在どこへ向かっているのか。

### Scope

基盤技術・architecture:

- VAE
- GAN
- autoregressive media generation
- Diffusion Model
- latent diffusion
- multimodal / text-conditioned generation

主要modal:

- image generation
- image editing / controllable generation
- speech synthesis / voice generation / voice cloning
- music generation（例: Suno等）
- video generation（例: Sora等）

横断して扱う論点:

- GANからDiffusionへの主流技術の変化
- text conditioningとmultimodal representation
- fidelity / diversity / controllability
- consistencyとidentity preservation
- long-form audio / music generation
- temporal consistencyとlong-horizon video generation
- high-resolution generationと計算資源
- editing / inpainting / instruction-based transformation
- generationとworld modelingの接近
- non-text generationとLLM / Agentの統合

### Key angle

現在のGenerative AIをLLM中心の歴史としてのみ見るのではなく、**画像・音声・音楽・映像では別々の技術的課題とarchitectureの系譜が存在した**ことを再構成する。

そのうえで、各modalのmodelが統合されつつある現在を読み、Generative AIが「text model + media tools」へ進むのか、それともmodalをまたぐunified architectureへ収束するのかを考察する。

### Out of scope

以下は原則としてTS-003を主な収容先とする。

- object detection
- segmentation
- OCR / general vision recognition
- non-generative computer visionの技術史
- multimodal understandingを主目的とするVLM

生成と理解の境界に位置する技術は必要に応じてcross-referenceするが、本号の主眼は**生成そのもの**に置く。

---

## TS-003 — Vision & Multimodal AI

**Status:** `SCOPED`

### 仮題

**Vision & Multimodal AI — 検知・認識からVLM・World Modelへ**

### Core question

AIは画像や現実世界を「検知・認識する」段階から、複数modalを統合して「理解する」段階へどのように発展してきたのか。

### Scope

Computer Visionの主要系譜:

- CNN
- ImageNet era
- object detection
- YOLO family
- segmentation
- OCR / visual recognition
- Vision Transformer

Vision-Language / Multimodalへの展開:

- vision-language alignment
- CLIP系architecture / contrastive representation
- VLM
- document / chart / UI understanding
- video understanding
- multimodal reasoning
- unified multimodal model
- embodied / spatial understandingへ接続する技術
- world model

### Key angle

**Perception → Recognition → Understanding → Multimodal reasoning** という流れを中心に、AIが非テキスト情報を扱う能力の変遷を追う。

YOLOのような検知系をGenerative Mediaへ無理に含めず、Computer VisionからVLM、video / spatial understanding、world modelへ至る技術史として整理する。

### Boundary with TS-002

- TS-002: 「何を、どのように生成できるようになったか」
- TS-003: 「世界を、どのように知覚・認識・理解できるようになったか」

image / video generationとmultimodal understandingが融合する領域では重複を許容するが、同一内容を二重に再録せず、それぞれの問いに必要な角度から扱う。

---

## 3. Promotion rule

A backlog item may remain `IDEA` / `SCOPED` without any GitHub Issue.

When an item becomes `SELECTED`:

1. decide a stable Thematic Special slug;
2. create the production / planning Issue;
3. fix the reader-facing `why this Special` rationale;
4. define scope and explicit exclusions;
5. begin the normal Special Source Intake and Evidence workflow;
6. create the corresponding `specials/<slug>/`, `surveys/special/<slug>/`, and `sources/SP-<slug>/` artifacts as required by the Special pipeline.

This separation keeps the Issue tracker focused on actionable work while allowing long-lived editorial ideas to accumulate without being lost.
