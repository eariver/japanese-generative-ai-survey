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

**Status:** `ACTIVE`

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

## TS-001-REISSUE-2026 — Efficient Intelligence (TS-001 reissue/successor, standalone Thematic)

**Status:** `RELEASED`

**Planning identifier:** `TS-001-REISSUE-2026`

**Reader-facing editorial lineage:** `TS-001 Reissue`

**Working title:** `Efficient Intelligence — LLMを速く、軽く、安くする技術史`

### Identity and lineage (normative)

- Historical `TS-001 -> SP001` (`中国Generative AIの台頭`) remains a released, immutable historical edition. This entry does not rename, rewrite, or revise it in place.
- This is a **new standalone Thematic edition** that reconstitutes LLM efficiency — visible inside SP001 as one supporting dimension — as an independent technical subject.
- Machine identity: `SP-efficient-llm-2026`
- Stable slug: `efficient-llm-2026`
- Canonical source root: `sources/SP-efficient-llm-2026/`
- Canonical survey root: `surveys/special/efficient-llm-2026/`
- Canonical work branch: `special/efficient-llm-2026-work`
- Temporal mode: `OPEN_HISTORY_AS_OF`
- Eventual target gate: `ARCHITECTURE_REVIEW` (first execution stops at `DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`; Screening and later stages are out of scope for the first run).

### Core question

> Large Language Modelsは、dense scalingとfull-attention Transformerを単純に巨大化する段階から、どのように「必要な計算だけを行う」「必要なmemoryだけを保持する」「生成を高速化する」「serving wasteを削る」「必要なら生成そのものを行わない」というarchitecture / systems co-designへ進化してきたのか。
>
> 各効率化技術はどこで生まれ、どのモデルへ採用され、compute・memory・latency・throughput・costとmodel capabilityへどのような測定可能な効果とtrade-offをもたらしたのか。

### Reader-facing why-this-Special

Frontier LLMの競争軸はparameter countや単一benchmark scoreだけでは説明できなくなった。現在のmodelは、sparse activation、compressed / selective memory、hybrid attention、low precision、speculative decoding、highly optimized kernels、KV-cache-aware serving、heterogeneous local inference、specialized non-generative decision modelsなどを重ねることで、能力を維持・向上させながらtraining / inference / deployment costを下げている。本Specialは個別model rankingではなく、これらを成立させる技術の系譜と相互関係を一次資料中心に再構成する。

### Mandatory research dimensions (D01–D10)

- **D01** Efficiency fundamentals / bottleneck model: training vs inference; prefill vs decode; compute-bound vs memory-bandwidth-bound vs communication-bound; latency vs throughput; model FLOPs vs memory movement; total vs active parameters; KV-cache footprint; weight footprint; energy/hardware utilization; token cost vs completed-task cost. Do not collapse into「高速化」.
- **D02** Scaling and training efficiency: scaling laws; Chinchilla/compute-optimal; data/model allocation; low-precision/FP8 training; optimizer efficiency; Muon; architecture-specific scaling-law refits; training-token reduction where documented. Link to Qwen3.8-Flash-Next and DeepSeek-family evidence where applicable.
- **D03** Conditional computation / MoE: Shazeer sparsely-gated MoE; GShard; Switch Transformer; later routing/load-balancing; Mixtral; DeepSeekMoE; DeepSeek V2/V3/V4.1 lineage; Qwen MoE lineage; current GLM/MiniMax/other material MoE models. Cover routing, top-k, shared vs routed experts, fine-grained experts, load balance, communication, expert memory residency, total vs active ratio, training/serving implications.
- **D04** Attention, sequence and KV-cache efficiency (major lane): MHA baseline; MQA; GQA; FlashAttention 1/2/3; MLA; sparse attention; sliding-window/local attention; Mamba/selective SSM; Gated DeltaNet; Kimi Delta Attention / Kimi Linear; DeepSeek Sparse Attention; Qwen Sparse Attention; hybrid linear + sparse/full attention; DeepSeek V4.1 Causal Encoder–Decoder; SWA replay/reconstructed cache where verified. Keep IO-efficient exact attention (FlashAttention) distinct from compute/storage-changing architectures.
- **D05** Decoding acceleration: speculative decoding; draft/target relationship; EAGLE; Medusa where material; Multi-Token Prediction and current MTP adoption; DeepSeek DSpark or verified equivalent; Qwen MTP. For each: distribution preservation, retraining need, acceptance, latency/throughput gain, hardware/batching constraints, quality interaction.
- **D06** Precision, quantization and compression: LLM.int8(); GPTQ; SmoothQuant; AWQ; FP8; FP4/MXFP4 where adopted; QLoRA; SparseGPT/pruning; BitNet/native low-bit; importance-matrix/mixed quantization where relevant. Separate PTQ vs QAT/native low-bit; weight-only vs weight+activation; KV-cache quantization; optimizer/training precision; file/storage encoding. GGUF is a format, not a quantization algorithm.
- **D07** Model representation and local inference: GGML history where needed; GGUF spec; llama.cpp; GGUF metadata/tensors; mmap/local loading; llama.cpp quantization families; CPU/GPU split; consumer hardware only when material; KTransformers; heterogeneous CPU/GPU MoE execution. Explain why huge-total/low-active MoE still has a large weight-memory problem. Keep size, active compute, memory capacity, bandwidth separate.
- **D08** Inference kernels and serving systems: Orca iteration-level scheduling; continuous/inflight batching; PagedAttention/vLLM; prefix/KV reuse; SGLang/RadixAttention; FlashMLA; TensorRT-LLM where material; Splitwise; DistServe; Mooncake; prefill/decode disaggregation; KV-cache offload/distributed cache; chunked prefill; scheduler/SLO tradeoffs. Mandatory because architecture alone does not determine cost/throughput.
- **D09** Distillation, pruning and adaptation efficiency: distillation history sufficient for current usage; reasoning-model distillation where material; DeepSeek R1 distilled models; pruning+retraining examples; LoRA/QLoRA for fine-tuning efficiency; quality/capacity tradeoffs. Not a generic fine-tuning tutorial.
- **D10** Specialization instead of generation: Jev (TypeSafe AI System One Model) as mandatory current case — typed probabilistic outputs, architecture claims, RLCD, parallel sampler, latency/price/throughput claims, exact evaluation methodology, limitations, availability, independent reproduction or lack thereof. Vendor benchmark is a vendor claim until independently reproduced. Ask why generate tokens at all for classification/routing/ranking/structured probabilistic decisions. Seek earlier/parallel precedents without forcing ancestry.

### 2026 capstone model case studies

Independently investigate at minimum: DeepSeek V4.1 Flash (552B MoE; asymmetric active prefill/input vs decode/output; Causal Encoder–Decoder; KV-cache reduction; sparse attention; FP8/FP4; MTP/DSpark or verified equivalent; native multimodality where relevant; serving/kernel support; API economics; official benchmark methodology; independent deployment/community evidence); Qwen3.8-Flash-Next (125B main / 6B active; 51B n-gram embedding; host-memory offload; Gated DeltaNet; Qwen Sparse Attention; Gated Residual; Muon+AdamW; scaling-law refit; MTP; context length; training-cost claim vs Qwen3.7-Plus; SGLang/vLLM/runtime support; official and independent evidence); Kimi Linear (KDA; Gated DeltaNet relationship; hybrid KDA+MLA; 48B/3B active; KV-cache saving; long-context decode throughput; released kernel; vLLM support; fair-comparison methodology; limitations); GLM-5.3-Flash (320B total/18B active; hybrid sparse/linear attention; mHC; training/data changes; serving/local deployment; API-cost claims; benchmark setup; comparison with prior GLM generation). Secondary modern cases (MiniMax-M2.x, gpt-oss, other 2025–2026 models with a materially distinct efficiency mechanism) investigated for materiality, not auto-selected. Nationality is not a selection criterion.

### Benchmark methodology lane (mandatory, not a leaderboard)

Taxonomy at minimum: broad knowledge/reasoning; expert science; mathematics; code generation; repository-level SWE; terminal/environment interaction; tool/function calling; interactive agents; web/browsing/research; long-context retrieval/reasoning; multimodal capability where needed; inference/system efficiency. Mandatory seeds: MMLU-Pro; GPQA Diamond; Humanity's Last Exam; AIME/relevant math generation; LiveCodeBench; SWE-bench family; Terminal-Bench; BFCL; τ-bench; BrowseComp; RULER; materially relevant current agent/coding benchmarks in selected model reports. Efficiency metrics: TTFT; TPOT/inter-token latency; tokens/sec/user; aggregate throughput; batch/concurrency; prefill/decode throughput; KV-cache bytes; HBM/DRAM/storage footprint; total/active parameters; FLOPs/token where available; energy where authoritative; API input/output/cache-hit price; cost per completed task where reproducible. Every benchmark number must bind exact model/version, benchmark version, eval date if available, harness, scaffold/tool access, reasoning effort/thinking budget, sampling params where material, context/output limits, pass@k/pass^k semantics, hardware for performance benchmarks, source authority, vendor vs independent status. No cross-model table may imply comparability when conditions differ. Benchmark validity is first-class: saturation, contamination, version drift, broken tasks, hidden scaffolds, vendor harnesses, test-time compute, tool access, public vs private subsets, self-reported scores, independent reproduction; SWE-bench Verified/Pro evolution is a mandatory example.

### Explicit exclusions

Not the main purpose: simple strongest-LLM ranking; leaderboard across unnormalized benchmark conditions; parameter-count-only comparison; nation-unit political superiority evaluation; exhaustive semiconductor-architecture history; general datacenter infrastructure; prompt-engineering tip catalogs; consumer model recommendations; generic agent-framework lists; multimodal generation history itself; complete history of all LLM benchmarks. Hardware only as needed for algorithm/runtime co-design; benchmarks only as taxonomy/methodology/failure-modes needed to read this issue's comparisons.

### Evidence shape, source priority, anti-thinness, page depth, X policy

- Per major technology, attempt origin, mechanism, adoption, efficiency evidence (measured benefit with exact baseline/conditions), capability evidence, trade-offs, independent implementation/reproduction, current deployment evidence, and community/reception as contextual signal only. Record missing independent evidence as limitation.
- Primary-source priority: original papers; official technical reports; model/system cards; official repos and exact configs; official runtime/spec docs; benchmark official papers/repos/methodology; independent systems/reproduction papers; high-quality independent implementation reports. Secondary media never replaces accessible primary authority. For open-weight models, go beyond launch blogs to reports/cards/configs/kernels.
- Anti-thinness: no one-paragraph-per-technology; no unexplained「MoE reduces compute」/「FlashAttention is faster」/「GGUF is quantization」; no single aggregate score as general-capability proof; no single vendor chart as independent validation; no unrelated-mechanism bundling to save pages; no page-budget excuse for dropping mechanisms; no model name as substitute for internal technologies. Discovery intentionally over-collects; Selection later.
- Page-depth expectation at planning time: approximately 64 pages soft target, up to approximately 96 pages acceptable if Evidence justifies. Not padding targets. Final page plan owned by Sol/Human Architecture Review after Evidence. If the manifest/schema supports a custom page budget cleanly, record an edition-specific longform budget; otherwise record the requirement and leave the exact plan for Architecture. Never compress scope to fit the historical SP001 18/24 plan.
- X/Grok for the first Discovery run: NOT_REQUIRED (primary technical map first). Later bounded X/community pass likely useful for 評判 but designed by Sol after Discovery completeness review; then X/community = reception/deployment/observed-problems only, never technical-spec/sole-benchmark/sole-release-license authority. No Grok task is created in the first run.

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
