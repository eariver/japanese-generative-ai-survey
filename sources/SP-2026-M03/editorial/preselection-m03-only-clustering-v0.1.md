# SP-2026-M03 — M03-only preselection clustering v0.1

Status: editorial working analysis only. This document does **not** approve Candidate Selection or Issue Architecture.

## Method

This pass intentionally excludes M04 and later issue theses, architectures, and narrative continuity from the selection basis. The only input is the 57 `CANDIDATE` records in the accepted SP-2026-M03 Evidence run `3e77733c01d893050196aaf946600ebe8f2a08b5a973cc6903a075b2008f306c`.

Primary clustering criteria:
1. technical subject matter visible in the March Evidence itself;
2. density of independent primary sources within March;
3. strength of chronology/source attribution;
4. distinct editorial value within M03.

Cross-cluster links are noted conceptually, but every Candidate receives one primary cluster for counting so that a later narrative cannot inflate a preferred theme by double-counting. Cluster counts describe the accepted Candidate surface; they are not a claim about the complete universe of March 2026 AI activity.

## Primary-cluster result

| Cluster | Count | Share of 57 | M03-only interpretation |
|---|---:|---:|---|
| Inference / Serving / Systems | 15 | 26.3% | The densest technical cluster: serving architecture, KV cache, routing, MoE communication, runtime overhead, heterogeneous/multimodal serving, and production frameworks. |
| Safety / Security / Control | 14 | 24.6% | A similarly dense cluster around prompt injection, agent privilege, malicious skills, system-prompt configuration, monitoring, and coding/security agents. |
| Frontier Models / Developer Platform | 9 | 15.8% | Major model and API/platform chronology remains a strong first-party backbone, including GPT, Claude, Gemini, GLM, Alibaba/Qwen, and open ecosystem releases. |
| Multimodal / Generation | 9 | 15.8% | A substantial independent theme: unified multimodal modeling, visual-memory/efficiency, image generation/editing, multimodal agents, and generation workflow infrastructure. |
| Agents / Runtime / Long-horizon Work | 6 | 10.5% | Material but not numerically dominant by itself: agent runtime, agentic RL orchestration, memory, deep research, coding agents, and long-horizon reliability. |
| Reasoning / Evaluation / Training | 4 | 7.0% | Smaller but distinct methodological cluster around post-training curricula, reasoning-at-generation, benchmark quality, and deep-research evaluation. |

Inference/Serving/Systems + Safety/Security/Control account for 29/57 Candidates. This is the strongest bottom-up signal in the accepted Candidate surface. Agent-related evidence cuts across several clusters, but treating all systems/security/multimodal items as one single “agent” cluster would overstate the agent narrative.

## Candidate titles by primary cluster

### Inference / Serving / Systems — 15
- Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models
- TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition
- Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity
- NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL
- Parallelizing Tool Execution and LLM Generation for Low-Latency Agent Serving
- The Workload-Router-Pool Architecture for LLM Inference Optimization: A Vision Paper from the vLLM Semantic Router Project
- TCM-Serve: Modality-aware Scheduling for Multimodal Large Language Model Inference
- KVSculpt: KV Cache Compression as Distillation
- IsoQuant: Hardware-Aligned SO(4) Isoclinic Rotations for LLM KV Cache Compression
- Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference
- VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference
- TensorRT-LLM v1.2.0
- vLLM v0.18.0
- vLLM v0.17.0
- TensorRT-LLM v1.3 release-candidate series

### Safety / Security / Control — 14
- The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs
- The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities
- “Elementary, My Dear Watson.” Detecting Malicious Skills via Neuro-Symbolic Reasoning across Heterogeneous Artifacts
- A Security Analysis of the OpenClaw AI Agent Framework
- Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers
- Evaluating Privilege Usage of Agents with Real-World Tools
- Covert Visual Prompt Injection against Commercial Multimodal Large Language Models
- Improving instruction hierarchy in frontier LLMs
- Reasoning models struggle to control their chains of thought, and that’s good
- Designing AI agents to resist prompt injection
- Monitoring internal coding agents for misalignment
- Codex Security research preview
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?

### Frontier Models / Developer Platform — 9
- GPT-5.3 Instant: Smoother, more useful everyday conversations
- GPT-5.4
- GPT-5.4 mini and nano
- Claude Sonnet 4.6
- GLM-5-Turbo
- Gemini API March 2026 model and tool updates
- Alibaba Model Studio March 2026 model updates
- Transformers v5.3.0
- Transformers v5.4.0

### Multimodal / Generation — 9
- LongCat-Next: Lexicalizing Modalities as Discrete Tokens
- CDH-Bench: A Commonsense-Driven Hallucination Benchmark for Evaluating Visual Fidelity in Vision-Language Models
- Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model
- ResAdapt: Adaptive Resolution for Efficient Multimodal Reasoning
- DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing
- Gen-Searcher: Reinforcing Agentic Search for Image Generation
- Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism
- Unify-Agent: A Unified Multimodal Agent for World-Grounded Image Synthesis
- ComfyUI v0.18.0

### Agents / Runtime / Long-horizon Work — 6
- ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning
- Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design
- MemFactory: Unified Inference & Training Framework for Agent Memory
- Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents
- From model to agent: Equipping the Responses API with a computer environment
- KAT-Coder-V2 Technical Report

### Reasoning / Evaluation / Training — 4
- Rethinking Easy-to-Hard: Limits of Curriculum Learning in Post-Training for Deductive Reasoning
- MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome
- ELT-Bench-Verified: Benchmark Quality Issues Underestimate AI Agent Capabilities
- Think Anywhere in Code Generation

## Thesis test

The earlier working thesis was:

> 2026年3月は、frontier model の更新競争と、agent runtime・tool use・security・serving infrastructure が結びつき始め、“モデルから実行するAIへ”という転換が輪郭を現した月だった。

M03-only review supports part of this thesis but not its strongest wording:
- `serving infrastructure` and `security/control` are genuinely dominant in the Candidate surface;
- major model releases/platform updates are also a strong first-party backbone;
- agent/runtime is material and connects several clusters, but is not the largest standalone cluster;
- multimodal/generation is too substantial to subordinate to an agent-only narrative.

Therefore the preferred M03-only thesis is broader:

> **2026年3月は、frontier modelの更新が相次ぐ一方、技術的な焦点が推論・配備、安全性、マルチモーダル、エージェント実行へ同時に広がり、モデル単体の性能だけでなく「AIをどう動かし、つなぎ、守るか」が前景化した月だった。**

A retrospective bridge to later months may state that this breadth *in hindsight* foreshadowed later execution-environment/full-stack developments, but that observation must not be used to promote or demote March Candidates.

## Candidate Selection consequence

Candidate Selection should preserve all six clusters according to their March-only density and source strength. In particular:
- do not make Agent/Runtime the sole organizing axis;
- give Inference/Serving/Systems and Safety/Security/Control independent major space;
- retain Multimodal/Generation as an independent substantial theme;
- use model/platform releases as the chronology backbone rather than as the entire issue;
- keep later-month continuity as retrospective interpretation only, applied after M03 roles are chosen.
