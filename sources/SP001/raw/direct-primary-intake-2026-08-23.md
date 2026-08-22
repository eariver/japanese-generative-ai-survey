# SP001 direct primary-source intake — 2026-08-23

Status: `RAW_OPERATOR_OBSERVATION`

Observed at: `2026-08-22T15:08:47Z`  
Operator: ChatGPT GPT-5.6 Sol  
Issue: `SP001`

## Purpose and evidence boundary

This file is a repository-local observation note produced during direct web research. It preserves exact source locators, source identity, the operator's concise observations, relevance to SP001 obligations, and unresolved questions.

It is **not** a byte-for-byte replica of the external sources and is **not** by itself publication-grade Evidence. Claims selected for publication must still be represented in normal Evidence artifacts with subject/entity/property binding and source-specific verification.

The source map intentionally prefers primary papers, official model cards, official repositories, and official documentation. Secondary material is used only as ecosystem context or to locate primary sources.

## Research closure strategy

Thematic expansion was performed along the following lanes rather than a fixed source quota:

1. early Chinese foundation-model lineage;
2. DeepSeek lineage;
3. Qwen lineage;
4. GLM / ChatGLM / Z.ai lineage;
5. Kimi / Moonshot lineage;
6. bridge families (Yi, Baichuan, MiniMax) where they explain ecosystem or architecture transitions;
7. reasoning / coding / agentic transitions;
8. long-context, MoE, attention, inference-efficiency, and serving transitions;
9. Open Weight / Open Source / license boundaries;
10. 2026 frontier endpoint as of the Production Profile's `OPEN_HISTORY_AS_OF` timestamp.

## A. Historical lineage / early ecosystem

### SRC-GLM-2021

- Title: `GLM: General Language Model Pretraining with Autoregressive Blank Infilling`
- URL: https://arxiv.org/abs/2103.10360
- Source class: PRIMARY_PAPER
- Published: 2021-03-18
- Obligations: SP001-O01, SP001-O02
- Observation: establishes the original GLM pretraining framework based on autoregressive blank infilling and provides a genuine technical ancestor for the later GLM family. Do not retroactively treat every later ChatGLM/Z.ai design choice as a direct consequence of this paper without version-specific evidence.

### SRC-GLM130B-2022

- Title: `GLM-130B: An Open Bilingual Pre-trained Model`
- URL: https://arxiv.org/abs/2210.02414
- Source class: PRIMARY_PAPER
- Published: 2022-10-05
- Obligations: SP001-O01, SP001-O04, SP001-O05, SP001-O06
- Observation: 130B bilingual English/Chinese model; the paper explicitly frames the project as an attempt to open a 100B-scale model and reports training-stability engineering plus INT4 deployment on comparatively accessible multi-GPU systems. This is a strong pre-ChatGPT-era/open-model milestone in the Chinese lineage.

### SRC-CHATGLM6B-2023

- Title: `ChatGLM-6B: An Open Bilingual Dialogue Language Model`
- URL: https://github.com/zai-org/ChatGLM-6B/blob/main/README_en.md
- Source class: PRIMARY_REPOSITORY
- Published/observed lineage point: 2023-03
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation: 6.2B bilingual dialogue model with consumer-GPU-oriented INT4 deployment (~6GB reported by the project) and P-Tuning v2 guidance. The historical license was not a simple permissive OSI-style grant: academic use was open while commercial use had an additional questionnaire/permission path. This is useful evidence that "open" in the 2023 Chinese model ecosystem covered materially different legal regimes.

### SRC-QWEN-REPORT-2023

- Title: `Qwen Technical Report`
- URL: https://arxiv.org/abs/2309.16609
- Source class: PRIMARY_PAPER
- Published: 2023-09-28
- Obligations: SP001-O01, SP001-O02, SP001-O03, SP001-O05
- Observation: first Qwen technical report; describes base/chat models, RLHF-aligned chat models, and already emphasizes tool use/planning plus code-interpreter-style agent applications. Important to avoid portraying agentic capability as appearing only after the 2025 reasoning wave.

### SRC-QWEN72B-2023

- Title: `Qwen-72B model card`
- URL: https://huggingface.co/Qwen/Qwen-72B
- Source class: PRIMARY_OFFICIAL
- Published/lineage point: 2023
- Obligations: SP001-O01, SP001-O06
- Observation: Qwen's early large checkpoint used the Tongyi Qianwen license rather than the later Apache-2.0 regime. This provides a concrete license-evolution point within one family.

### SRC-BAICHUAN2-2023

- Title: `Baichuan 2`
- URL: https://github.com/baichuan-inc/Baichuan2/blob/main/README_EN.md
- Source class: PRIMARY_REPOSITORY
- Published: 2023
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation: 7B/13B base/chat releases, 2.6T-token training claim, quantization/fine-tuning/community integration guidance, and a model-specific commercial licensing path layered alongside Apache-2.0 repository code. Material mainly as a 2023 bridge showing that broad Chinese open-model participation predated the later DeepSeek/Qwen dominance and that code-license != model-use rights.

### SRC-YI34B-2023

- Title: `Yi-34B model card`
- URL: https://huggingface.co/01-ai/Yi-34B
- Source class: PRIMARY_OFFICIAL
- Published/lineage point: 2023-11
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation: 01.AI's bilingual open-weight Yi family provided 6B/34B checkpoints, including long-context variants, with Apache-2.0 metadata and explicit local deployment paths including llama.cpp. Material as a bridge/counterexample, but likely not a primary narrative branch after 2024 unless downstream evidence shows sustained strategic relevance.

## B. DeepSeek lineage

### SRC-DEEPSEEK-LLM-2024

- Title: `DeepSeek LLM: Scaling Open-Source Language Models with Longtermism`
- URL: https://arxiv.org/abs/2401.02954
- Source class: PRIMARY_PAPER
- Published: 2024-01
- Obligations: SP001-O01, SP001-O02
- Observation: early DeepSeek LLM family technical baseline. Use as the family starting point before DeepSeek-V2's efficiency architecture becomes the defining branch.

### SRC-DEEPSEEK-V2-2024

- Title: `DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model`
- URL: https://arxiv.org/abs/2405.04434
- Source class: PRIMARY_PAPER
- Published: 2024-05-07
- Obligations: SP001-O02, SP001-O04
- Observation: 236B total / 21B active MoE, 128K context, introduction of MLA and DeepSeekMoE. Paper claims 93.3% KV-cache reduction and 5.76x max generation throughput vs DeepSeek 67B under its evaluation setup. These numbers must remain explicitly bound to the paper's comparison conditions if used.

### SRC-DEEPSEEK-V3-2024

- Title: `DeepSeek-V3 Technical Report`
- URL: https://arxiv.org/abs/2412.19437
- Source class: PRIMARY_PAPER
- Published: 2024-12-27
- Obligations: SP001-O02, SP001-O04, SP001-O07
- Observation: 671B total / 37B active MoE; retains MLA/DeepSeekMoE, adds auxiliary-loss-free load balancing and multi-token prediction, reports 14.8T pretraining tokens and 2.788M H800 GPU-hours for full training. The training-cost narrative is central to DeepSeek's competitive story but should not be converted into generalized "China trains cheaper" claims.

### SRC-DEEPSEEK-R1-2025

- Title: `DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning`
- URL: https://arxiv.org/abs/2501.12948
- Source class: PRIMARY_PAPER
- Published: 2025-01-22
- Obligations: SP001-O02, SP001-O03, SP001-O07
- Observation: R1-Zero explores large-scale RL without preliminary SFT; R1 adds cold-start data and multi-stage training. The release also includes distilled Qwen/Llama-based models. This is a major reasoning transition point and must distinguish the native R1 model from distill variants.

### SRC-DEEPSEEK-R1-LICENSE

- Title: `DeepSeek-R1 model card — License`
- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1
- Source class: PRIMARY_OFFICIAL
- Published/observed: 2025
- Obligations: SP001-O06
- Observation: DeepSeek states code and R1 model weights are MIT licensed and permits commercial use/modification/distillation. Distill variants inherit important base-model lineage/license considerations (Qwen Apache-2.0 or Llama licenses), so the article must not collapse all R1-family weights into one legal subject.

### SRC-DEEPSEEK-V4-2026

- Title: `DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence`
- URL: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
- Source class: PRIMARY_OFFICIAL
- Published: 2026-04
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O07
- Observation: V4 preview includes Pro (1.6T total / 49B active) and Flash (284B total / 13B active), both 1M context. New hybrid attention combines CSA/HCA; project reports lower inference FLOPs/KV cache vs V3.2 at 1M context. The post-training description emphasizes domain experts plus unified consolidation/on-policy distillation.

### SRC-DEEPSEEK-V4-0731-2026

- Title: `DeepSeek-V4-Flash-0731 model card`
- URL: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
- Source class: PRIMARY_OFFICIAL
- Published: 2026-07-31
- Obligations: SP001-O03, SP001-O04, SP001-O05
- Observation: official V4-Flash update emphasizes substantially stronger agentic capability and documents vLLM deployment with DSpark speculative decoding. This supports an endpoint narrative of efficiency architecture becoming directly tied to long-horizon/agent serving rather than only training cost.

## C. Qwen lineage

### SRC-QWEN2-2024

- Title: `Qwen2 Technical Report`
- URL: https://arxiv.org/abs/2407.10671
- Source class: PRIMARY_PAPER
- Published: 2024-07-15
- Obligations: SP001-O02, SP001-O03, SP001-O05
- Observation: 0.5B–72B suite plus MoE variant, ~30-language support, open weights, and explicit quantization/fine-tuning/deployment resources. Qwen's competitive strategy is breadth of sizes + ecosystem usability, not only flagship benchmark performance.

### SRC-QWEN25-2024

- Title: `Qwen2.5 Technical Report`
- URL: https://arxiv.org/abs/2412.15115
- Source class: PRIMARY_PAPER
- Published: 2024-12-19
- Obligations: SP001-O02, SP001-O03, SP001-O05
- Observation: scales training corpus from 7T to 18T tokens and describes SFT + multi-stage RL; open-weight family plus hosted proprietary MoE variants. Also acts as foundation for Math/Coder/QwQ and multimodal branches, making Qwen a platform/family strategy rather than a single model line.

### SRC-QWEN3-2025

- Title: `Qwen3 Technical Report`
- URL: https://arxiv.org/abs/2505.09388
- Source class: PRIMARY_PAPER
- Published: 2025-05-14
- Obligations: SP001-O02, SP001-O03, SP001-O06
- Observation: dense + MoE family from 0.6B to 235B; integrates thinking and non-thinking modes into one model family and adds thinking-budget control. The paper states all Qwen3 models are publicly accessible under Apache-2.0.

### SRC-QWEN35-2026

- Title: `Qwen3.5-27B model card`
- URL: https://huggingface.co/Qwen/Qwen3.5-27B
- Source class: PRIMARY_OFFICIAL
- Published: 2026-02
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Observation: natively multimodal foundation model; hybrid Gated DeltaNet + full attention architecture; 262K native context with documented extension to ~1.01M; compatible with Transformers/vLLM/SGLang/KTransformers; Apache-2.0. Demonstrates Qwen moving from text-family breadth toward unified multimodal/agent foundations while maintaining broad deployment support.

### SRC-QWEN36-2026

- Title: `Qwen3.6-27B model card`
- URL: https://huggingface.co/Qwen/Qwen3.6-27B
- Source class: PRIMARY_OFFICIAL
- Published: 2026-04
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Observation: first open-weight Qwen3.6 variant; emphasizes community feedback, stability, agentic coding, repository-level reasoning, and preserving thinking context across historical messages. Architecture remains in the Qwen3.5 family and license is Apache-2.0.

## D. GLM / Z.ai lineage

### SRC-GLM4-2024

- Title: `GLM-4 / all-tools era`
- URL: https://github.com/THUDM/ChatGLM-6B/blob/main/README_en.md
- Source class: PRIMARY_REPOSITORY
- Published/lineage point: 2024
- Obligations: SP001-O02, SP001-O03
- Observation: repository history points to GLM-4 API functionality including system prompt, function call, retrieval, and web search. For publication, prefer a version-specific GLM-4 technical paper/repository if a concrete claim is retained; this locator is currently a lineage lead rather than sufficient final Evidence for all GLM-4 claims.

### SRC-GLM45-2025

- Title: `GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models`
- URL: https://arxiv.org/abs/2508.06471
- Source class: PRIMARY_PAPER
- Published: 2025-08-08
- Obligations: SP001-O02, SP001-O03, SP001-O04
- Observation: 355B total / 32B active MoE, hybrid thinking/direct response, 23T-token training, and explicit ARC framing (agentic, reasoning, coding). This is a family-strategy pivot comparable to the 2025 reasoning/agent transition in DeepSeek/Qwen/Kimi but not identical in training recipe.

### SRC-GLM5-2026

- Title: `GLM-5 model card`
- URL: https://huggingface.co/zai-org/GLM-5
- Source class: PRIMARY_OFFICIAL
- Published: 2026-02
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Observation: 744B-class / ~40B active scale, DSA long-context efficiency, asynchronous RL infrastructure (`slime`), explicit complex systems engineering and long-horizon agentic focus. Model card metadata marks model weights MIT; repository code licensing must be treated separately where it differs.

### SRC-GLM52-2026

- Title: `GLM-5.2 model card`
- URL: https://huggingface.co/zai-org/GLM-5.2
- Source class: PRIMARY_OFFICIAL
- Published: 2026-06
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Observation: current endpoint as of SP001 as-of date. 1M context, flexible thinking effort, IndexShare cross-layer sparse-attention index reuse with claimed 2.9x per-token FLOP reduction at 1M context. Official model card documents vLLM/SGLang deployment and MIT model license metadata.

## E. Kimi / Moonshot lineage

### SRC-KIMI-K15-2025

- Title: `Kimi k1.5: Scaling Reinforcement Learning with LLMs`
- URL: https://arxiv.org/abs/2501.12599
- Source class: PRIMARY_PAPER
- Published: 2025-01-22
- Obligations: SP001-O03, SP001-O04
- Observation: multimodal reasoning model trained with scaled RL; emphasizes long-context scaling, policy optimization, infrastructure optimization, and long2short transfer. Kimi's reasoning lineage should not be presented as merely following DeepSeek-R1; the papers are contemporaneous and use different disclosed techniques.

### SRC-KIMI-K2-2025

- Title: `Kimi K2: Open Agentic Intelligence`
- URL: https://arxiv.org/abs/2507.20534
- Source class: PRIMARY_PAPER
- Published: 2025-07-28
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O05
- Observation: 1T total / 32B active MoE; MuonClip optimizer; 15.5T-token pretraining; agentic data synthesis and joint RL through real/synthetic environments. Marks a major Moonshot transition from reasoning research to open agentic model distribution.

### SRC-KIMI-K2-LICENSE

- Title: `Kimi-K2-Base LICENSE`
- URL: https://huggingface.co/moonshotai/Kimi-K2-Base/blob/main/LICENSE
- Source class: PRIMARY_OFFICIAL
- Published: 2025
- Obligations: SP001-O06
- Observation: Modified MIT license. The material modification requires prominent `Kimi K2` display for covered commercial products/services exceeding the specified MAU or monthly-revenue thresholds. This is a clear example of why "open weights" must not be equated automatically with an unmodified OSI-style permissive license.

### SRC-KIMI-LINEAR-2025

- Title: `Kimi Linear: An Expressive, Efficient Attention Architecture`
- URL: https://arxiv.org/abs/2510.26692
- Source class: PRIMARY_PAPER
- Published: 2025-10-30
- Obligations: SP001-O04
- Observation: introduces Kimi Delta Attention (KDA), hybrid KDA/MLA design, and reports up to 75% KV-cache reduction / 6x decoding throughput at 1M context under its study. This becomes directly relevant to K3 architecture and shows long-context efficiency as a continuing Moonshot research branch.

### SRC-KIMI-K3-2026

- Title: `Kimi K3 — Open Frontier Intelligence`
- URL: https://github.com/MoonshotAI/Kimi-K3
- Source class: PRIMARY_REPOSITORY
- Published: 2026-07
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O05, SP001-O06, SP001-O07
- Observation: 2.8T total / 104B active, native multimodal, 1M context, KDA + gated MLA, Attention Residuals, Stable LatentMoE, MXFP4/MXFP8 quantization-aware training, and open weights under the Kimi K3 License. Explicitly positioned for long-horizon coding and agentic knowledge work. Current Moonshot endpoint as of SP001 as-of date.

## F. Bridge / competing approaches

### SRC-MINIMAX01-2025

- Title: `MiniMax-01: Scaling Foundation Models with Lightning Attention`
- URL: https://arxiv.org/abs/2501.08313
- Source class: PRIMARY_PAPER
- Published: 2025-01-14
- Obligations: SP001-O01, SP001-O04
- Observation: MiniMax-01 provides a parallel Chinese long-context/attention-efficiency branch. Retain only where it helps establish that the efficiency/long-context race was broader than the four primary families; avoid creating a fifth full family chapter unless later materiality evidence warrants it.

### SRC-YI34B-BRIDGE

- Title: `Yi-34B official model card`
- URL: https://huggingface.co/01-ai/Yi-34B
- Source class: PRIMARY_OFFICIAL
- Published: 2023
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation: useful bridge for early open-weight distribution, local inference, bilingual competition, and Apache-2.0 licensing. Current evidence does not yet justify equal narrative weight with DeepSeek/Qwen/GLM/Kimi in the 2025–2026 frontier section.

### SRC-BAICHUAN2-BRIDGE

- Title: `Baichuan 2 official repository`
- URL: https://github.com/baichuan-inc/Baichuan2
- Source class: PRIMARY_REPOSITORY
- Published: 2023
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation: useful bridge for the 2023 Chinese open-model wave and model-specific commercial-license constraints. Current evidence suggests historical/contextual rather than frontier-primary treatment.

## G. Current endpoint synthesis observations

### Endpoint 1 — family strategies remain distinct

- DeepSeek: efficiency architecture and sparse/MoE serving research are repeatedly tied to frontier-scale reasoning/agent deployment.
- Qwen: unusually broad size/model distribution and deployment ecosystem evolves into unified multimodal/agent foundations while retaining Apache-2.0 open-weight releases.
- GLM/Z.ai: lineage begins earlier with GLM/GLM-130B/ChatGLM and increasingly frames the frontier around coding/agentic engineering and long-horizon execution.
- Kimi/Moonshot: strong long-context/RL research branch evolves into open agentic MoE models and then KDA-based multimodal K3.

This distinction should survive Candidate Selection and Architecture; avoid a single homogeneous `中国勢` technical strategy.

### Endpoint 2 — 2025 is a transition, not the endpoint

The 2025 DeepSeek-R1 / Qwen3 / GLM-4.5 / Kimi-K2 generation is a major reasoning-agent transition but SP001's as-of date is 2026-08-22. Architecture therefore needs a final frontier section covering at least:

- DeepSeek V4 / V4-Flash 0731;
- Qwen3.5 / Qwen3.6;
- GLM-5 / GLM-5.2;
- Kimi K3.

### Endpoint 3 — architecture convergence is partial

Common directions include sparse MoE, long context, inference-efficiency work, reasoning-control mechanisms, coding/agentic optimization, and open-weight distribution. The underlying methods differ materially: MLA/CSA/HCA/DSA/IndexShare/KDA/Gated DeltaNet/etc. must remain bound to the correct family/version rather than being presented as one shared Chinese architecture.

### Endpoint 4 — `Open Source` != `Open Weight`

Observed license regimes across the lineage are heterogeneous:

- early ChatGLM: academic openness plus additional commercial-use permission path;
- early Qwen-72B: Tongyi Qianwen model license;
- Qwen3/Qwen3.5/Qwen3.6: Apache-2.0;
- DeepSeek-R1/V4: MIT for the named code/weights, with base-license caveats for some distills;
- Kimi K2: Modified MIT with a large-commercial-product attribution condition;
- Kimi K3: custom Kimi K3 License;
- GLM-5/5.2 model-card metadata: MIT for model artifacts, while associated repository code licensing may differ;
- Baichuan2: repository Apache-2.0 plus model community/commercial-use conditions.

The article should describe concrete rights/conditions per artifact and avoid using `open source` as a blanket synonym for publicly downloadable weights.

## H. Residual questions / gap-fill targets

1. Confirm the exact first-release dates and model-license transitions for Qwen1 → Qwen2 → Qwen3 using version-specific primary artifacts before a publication chronology is frozen.
2. Confirm GLM-4 version-specific technical source(s) rather than relying on later repository retrospection for tool/function/retrieval claims.
3. Verify Kimi K3 license terms from the exact LICENSE bytes before summarizing redistribution/commercial conditions.
4. Verify whether any MiniMax / Yi / Baichuan development after the bridge period materially changes the four-family-centered architecture.
5. Integrate the required Grok/X run specifically for real-world adoption/runtime/quantization/fine-tuning/community counter-signals; do not use X to establish technical specifications or historical priority.
6. For all benchmark comparisons, preserve model/version/evaluation-condition boundaries and avoid building a single cross-family rank table from incompatible evaluations.

## I. Preliminary saturation judgment

The direct primary-source pass has reached reasonable **structural saturation** for Architecture planning: each required Profile dimension has at least one credible primary-source lane, all four primary families have an early-to-current lineage, major bridge families have been checked, and the 2026 frontier endpoint is represented.

Discovery Acceptance is **not yet ready**, because the required Grok/X run remains pending and its exact returned bytes/disposition must be integrated before the Discovery boundary can close.
