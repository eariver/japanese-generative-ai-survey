# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://ifm.ai/blog/k2/
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-03
- retrieval: webfetch markdown of Institute of Foundation Models announcement introducing K2 Horizon; stored verbatim as returned.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

Introducing K2 Horizon: Frontier Performance, Radically Open                                    [Skip to article](#article)

[![Institute of Foundation Models](/blog/k2/assets/ifm-logo.svg)](https://ifm.ai/)

# Introducing K2 Horizon: Frontier Performance, Radically Open

September 3, 2026 · Institute of Foundation Models

Artifacts: Hugging Face collection IFM/k2-horizon, GitHub code, Weights & Biases.

Today IFM is releasing K2 Horizon, a connected fleet of six models: 375B-A23B, 36B-A4B, 32B, 7B, 3.7B, and 0.9B. Across reasoning, mathematics, coding, agentic tasks, and general capabilities, K2 Horizon delivers top-tier performance in every size class—with the 0.9B, 3.7B, and 7B models setting new state of the art at their respective scales.

K2 Horizon is also our most comprehensive open release to date. For every model, we are opening the training lifecycle from pretraining through reasoning and agentic post-training. We are releasing intermediate checkpoints, training data or detailed data-construction recipes, open architecture, mixture compositions, training code, configurations, fine-grained logs, evaluation results, and final weights.

The models and code are released under the Apache 2.0 license. Datasets are released under their applicable licenses, such as ODC-BY; We disclose how the data was constructed and mixed when redistribution is not possible.

Together, K2 Horizon represents the most comprehensive open model release to date:

-   **A new performance frontier across scales.** The 0.9B, 3.7B, and 7B models achieve world-leading performance in their size classes across widely used evaluations. The 36B-A4B model, equipped with our new Mixture-of-Value-Attention (MoVA) mechanism, delivers exceptional capability per active parameter, outperforming some much larger models. The 32B and 375B-A23B models rank among the top models in their respective classes.
-   **The first fully [open model](https://arxiv.org/abs/2312.06550) fleet for agents.** K2 Horizon is the first open model family to expose the complete development process through agentic post-training. By releasing checkpoints, data (or data recipe), code, configurations, and training logs across every stage, K2 Horizon makes it possible to study how reasoning, tool use, planning, and agentic capabilities emerge.
-   **Six models spanning edge to enterprise.** The 0.9B model is designed for highly constrained environments such as watches and glasses, while the 3.7B and 7B models bring advanced capabilities to phones and other on-device applications. The dense 32B model and sparse 36B-A4B model provide powerful options for local workstations and efficient serving. The 375B-A23B model brings the fleet’s strongest capabilities to demanding enterprise deployments. All six models include quantization support.
-   **One connected fleet.** The six models share core architecture, vocabulary, training methodology, interfaces, evaluation infrastructure, and deployment tooling, with a smaller vocabulary for the 0.9B model.

## World-leading performance across the scales

The 0.9B, 3.7B, and 7B models achieve state-of-the-art results in their respective classes across mathematics, reasoning, general capability, coding, and agentic tasks.

The 36B-A4B model performs beyond the level normally expected from its active parameter count, demonstrating the efficiency of our unique Mixture-of-Expert design when computing attention values. The 32B and 375B-A23B models place among the top models in their respective comparison classes.

The small models are especially notable. K2 Horizon 0.9B achieves an AIME 2026 score above 48, along with strong reasoning, tool-use, and agentic capabilities. K2 Horizon 3.7B and 7B extend these capabilities to more demanding software-engineering and multi-step environments, demonstrated on strong performance in SWE-bench and BrowseComp.

### Why the Horizon Fleet matters

A transparent model that falls far behind the capability frontier has limited value as a foundation, even for research. At the same time, a powerful model released only as final weights allows people to run it, but provides little insight into how its capabilities were created.

K2 Horizon brings these two together. The fleet provides highly competitive models and releases the recipes used to train them.

Since introducing the fully open principle in our 2023 [LLM360 paper](https://arxiv.org/abs/2312.06550), we have released open models every year while extending that commitment to larger scales, stronger capabilities, and now the complete lifecycle through agentic post-training.

### For every Horizon model, we will release:

-   Training data or recipe, such as construction methods, and mixture compositions
-   Training code
-   Model configurations and training recipes
-   Intermediate checkpoints throughout training
-   Fine-grained training logs
-   Evaluation results across general and specialized capabilities
-   Final model weights

## A Deep Dive into The K2 Horizon Fleet

### K2 Horizon 375B-A23B: the enterprise powerhouse

K2 Horizon 375B-A23B is the fleet’s largest and most capable model. Its sparse MoE architecture provides 375 billion parameters of total capacity while activating approximately 23 billion parameters for each token, allowing it to draw on the capacity of a much larger model without using every parameter for every token.

The model ranks among the top models below 400 billion parameters across general, reasoning, coding, and agentic evaluations. It is designed for demanding workloads where model quality matters most, including complex reasoning, software engineering, research, and long-horizon agentic tasks.

### K2 Horizon 32B and 36B-A4B: strong performance for local deployment

Horizon 32B is the fleet’s most powerful dense model, providing a strong balance of capability, adaptability, and local deployability. It ranks among the top dense models below 40 billion parameters.

Horizon 36B-A4B reaches nearly the performance of the dense 32B model while activating only approximately 4 billion parameters per token. Its efficiency comes from MoVA, our new sparse attention architecture, together with MoE feed-forward layers.

### K2 Horizon 7B, 3.7B, and 0.9B: frontier capability at small scale

K2 Horizon 7B and 3.7B deliver strong reasoning, mathematics, coding, tool-use, and agentic performance while remaining suitable for local and on-device deployment.

K2 Horizon 0.9B carries many of the same capabilities into highly constrained environments. It can perform mathematical reasoning, use tools, and complete simple agentic tasks while remaining compact enough for applications on watches, glasses, and other edge devices under quantization.

## Designing K2 Horizon

### One family from the beginning

Horizon was designed as a connected family rather than a collection of unrelated models. The six models share core architectural decisions, training methodology, interfaces, evaluation infrastructure, and deployment tooling. Each model is pretrained on approximately 20 trillion tokens using carefully constructed and documented mixtures. Intermediate checkpoints and their corresponding fine-grained logs are captured throughout training.

### MoVA: scaling attention with sparse experts

Our new architecture, **MoVA—Mixture-of-Value Attention, extends this principle to attention**. MoVA integrates expert routing into multi-head attention while remaining compatible with efficient techniques including FlashAttention, grouped-query attention, and sparse attention.

The result is K2 Horizon MoVA 36B-A4B: a model with 36 billion total parameters but approximately 4 billion active parameters per token.

### Training Data

Horizon’s pre-training mixture combines diverse web, code, mathematical, scientific, multilingual, and domain-specific sources with synthetic data. Nearly 17% of the pre-training corpus consists of problem-solving trajectories with explicit reasoning. In total, we used approximately 10 trillion synthetic tokens during pre-training.

Our post-training data is introduced from the beginning of mid-training. A main pillar is large-scale task synthesis grounded in task taxonomies, diversity knobs, and web-search seeding, resulting in over 100 million unique tasks.

### Post-training for reasoning and agents

Most of K2 Horizon’s advanced reasoning and agentic capabilities emerge during post-training. The complete pipeline includes mid-training, supervised fine-tuning, model merging, reinforcement learning with specialized agent training.

### Uno Diffusion: plug-and-play lossless speedup for Horizon

Uno keeps Horizon’s autoregressive parameters frozen and fully responsible for the model’s output distribution, while a lightweight set of diffusion parameters learns only how to generate more efficiently. Uno is delivered as a simple **LoRA adapter**.

## From Open Source to Open Science

We ran K2 Horizon 375B-A23B on 89 TerminalBench 2.1 tasks with eight attempts each, producing 712 trials. Of these, 500 passed the task verifier (70.2% reported accuracy). Audit flagged 24 trials across 10 tasks. Removing them lowers the accuracy from 70.2% to 66.9%, a correction of 3.37 percentage points.

## Get Started with K2 Horizon Today!

All six K2 Horizon sizes are released as open weights under Apache 2.0, with day-zero support from vLLM, SGLang, and Ollama. Get the models from: [https://huggingface.co/IFM](https://huggingface.co/IFM).

[truncated for edition-local storage]
