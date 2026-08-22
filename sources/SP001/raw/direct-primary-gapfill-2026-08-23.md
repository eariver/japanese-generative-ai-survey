# SP001 direct primary-source gap fill — 2026-08-23

Status: `RAW_OPERATOR_OBSERVATION`

Issue: `SP001`  
Purpose: close residual Source Intake questions left by `sources/SP001/raw/direct-primary-intake-2026-08-23.md` before Discovery acceptance.

This is an operator research note, not publication-grade Evidence. Version-specific technical claims retained downstream still require normal Evidence artifacts and subject/entity/property binding.

## 1. GLM-4 version-specific lineage gap — CLOSED for Source Intake

### SRC-GLM4-REPORT-2024

- Title: `ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools`
- URL: https://arxiv.org/abs/2406.12793
- Source class: PRIMARY_PAPER
- Submitted: 2024-06-18; revised 2024-07-30
- Obligations: SP001-O01, SP001-O02, SP001-O03, SP001-O05
- Observation:
  - the report explicitly reconstructs the GLM family through GLM-4, GLM-4-Air and GLM-4-9B rather than relying on later repository retrospection;
  - it states GLM-4 was pretrained on roughly ten trillion tokens, mostly Chinese and English plus material from 24 additional languages, followed by multi-stage post-training;
  - `GLM-4 All Tools` is explicitly aligned to autonomously choose among web browsing, Python, text-to-image and user-defined functions;
  - the report also records open releases including GLM-4-9B 128K/1M variants and GLM-4V-9B, and reports more than ten million Hugging Face downloads for open ChatGLM-family models in 2023.
- Disposition: use this paper as the canonical GLM-4 lineage/agent-tools primary source. Benchmark claims in the paper remain vendor/author evaluations and must not be merged into a cross-family global ranking.

### SRC-GLM4-OPEN-REPO-2024

- Title: `GLM-4 repository / June 5, 2024 open series`
- URL: https://github.com/zai-org/GLM-4/blob/main/README_20240605.md
- Source class: PRIMARY_REPOSITORY
- Obligations: SP001-O03, SP001-O05, SP001-O06
- Observation:
  - records the June 5, 2024 open GLM-4-9B family and 128K / 1M context variants;
  - provides transformers/vLLM/OpenAI-compatible serving paths, fine-tuning demonstrations, and All Tools examples;
  - explicitly separates model-weight licensing from Apache-2.0 repository code.
- Disposition: supporting ecosystem/license-boundary source; article must keep model-license and repository-code-license subjects distinct.

## 2. Kimi K3 exact license gap — CLOSED for Source Intake

### SRC-KIMI-K3-LICENSE-2026

- Title: `Kimi K3 License`
- URL: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE
- Source class: PRIMARY_OFFICIAL
- Copyright: 2026 Moonshot AI
- Obligations: SP001-O06
- Observation:
  - the license grants broad rights to use, copy, modify, distribute, sublicense, sell, deploy and fine-tune the covered software/weights, subject to stated conditions;
  - a licensee (including affiliates) operating a defined `Model as a Service` business with aggregate revenue above USD 20 million over any consecutive 12 months must enter a separate agreement with Moonshot AI before commercial use of the software or derivatives;
  - commercial products/services above 100 million MAU or USD 20 million monthly revenue must prominently display `Kimi K3` in the UI;
  - the specified requirements have exclusions for internal use and use through Moonshot official products/certified inference partners.
- Disposition: the Kimi K3 license is materially different from unmodified MIT/Apache-2.0 and merits explicit treatment in the Open Weight/license section. Do not paraphrase it merely as `permissive` without the service/revenue conditions.

## 3. MiniMax current-frontier check — MATERIAL PARALLEL BRANCH

### SRC-MINIMAX-M25-2026

- Title: `MiniMax M2.5: Built for Real-World Productivity`
- URL: https://www.minimax.io/news/minimax-m25
- Source class: PRIMARY_OFFICIAL
- Published: 2026-02-12
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O07
- Observation:
  - M2.5 is explicitly positioned around coding, agentic tool use/search and professional work;
  - MiniMax describes large-scale RL over hundreds of thousands of real-world environments, an agent-native RL framework (`Forge`), and emphasis on task-completion efficiency/cost rather than only token-level benchmark performance;
  - official distribution includes downloadable weights and common local/serving integrations in the associated model repository.

### SRC-MINIMAX-M27-2026

- Title: `MiniMax M2.7: Early Echoes of Self-Evolution`
- URL: https://www.minimax.io/news/minimax-m27-en
- Source class: PRIMARY_OFFICIAL
- Published: 2026-03-18
- Obligations: SP001-O03, SP001-O05, SP001-O07
- Observation:
  - M2.7 extends the M2 line toward complex agent harness construction, Agent Teams, skills and dynamic tool search;
  - MiniMax explicitly describes the model as participating in aspects of its own development workflow, making it a useful parallel/counterexample to the four primary families' 2026 agentic endpoints.

### SRC-MINIMAX-M27-HF-2026

- Title: `MiniMaxAI/MiniMax-M2.7`
- URL: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
- Source class: PRIMARY_OFFICIAL
- Obligations: SP001-O05, SP001-O06
- Observation:
  - open weights are distributed for Transformers/vLLM/SGLang and local quantization-compatible tooling;
  - repository/model card identifies a Modified-MIT licensing regime rather than Apache-2.0;
  - official card describes M2.7 as an open-weight model and provides local deployment paths.
- Disposition: MiniMax should no longer be treated only as a 2025 long-context footnote. It is a **material parallel 2026 frontier branch**, but TS-001 still designates DeepSeek/Qwen/GLM/Kimi as the four central families. Architecture should therefore give MiniMax a compact competing/parallel-strategy section or comparative callout rather than silently promote it to a fifth co-equal family chapter without Owner review.

## 4. Yi current-lineage check — HISTORICAL/BRIDGE, not current primary frontier

### SRC-YI15-2024

- Title: `Yi-1.5`
- URL: https://github.com/01-ai/Yi-1.5
- Source class: PRIMARY_REPOSITORY
- Released: 2024-05-13
- Obligations: SP001-O01, SP001-O05, SP001-O06
- Observation:
  - Yi-1.5 upgraded the Yi line in coding/math/reasoning/instruction following and provided 34B/9B/6B variants;
  - official repository documents Ollama/local use, fine-tuning ecosystem integrations, and Apache-2.0 code/weights with attribution guidance;
  - the official 01.AI Hugging Face model catalog shows the public Yi LLM line concentrated in 2023–2024 (Yi, Yi-1.5, Yi-Coder), with no later general Yi checkpoint visible as a 2025–2026 co-equal frontier branch.
- Disposition: retain Yi as an important 2023–2024 open-weight/distribution bridge and coding branch, not a main 2026 endpoint.

## 5. Baichuan current-lineage check — ACTIVE but domain-specialized / derivative branch

### SRC-BAICHUAN-M2-2025

- Title: `Baichuan-M2-32B`
- URL: https://huggingface.co/baichuan-inc/Baichuan-M2-32B
- Source class: PRIMARY_OFFICIAL
- Published lineage point: 2025
- Obligations: SP001-O01, SP001-O03, SP001-O05, SP001-O06
- Observation:
  - current Baichuan M2 is a medical-enhanced reasoning model built on `Qwen/Qwen2.5-32B`, not a continuation of the earlier Baichuan2 foundation-model architecture as an independent general-frontier base;
  - model is Apache-2.0 and documents vLLM/SGLang deployment.

### SRC-BAICHUAN-M3-2026

- Title: `Baichuan-M3-235B`
- URL: https://huggingface.co/baichuan-inc/Baichuan-M3-235B
- Source class: PRIMARY_OFFICIAL
- Published lineage point: 2026
- Obligations: SP001-O03, SP001-O05, SP001-O06
- Observation:
  - Baichuan-M3 is explicitly a medical-enhanced clinical-inquiry model;
  - official model metadata identifies Qwen3-MoE ancestry / acknowledgement and Apache-2.0 licensing;
  - it remains technically active and relevant as evidence of specialization/derivative ecosystem behavior, but its current trajectory is not a direct independent general-frontier competitor comparable to DeepSeek/Qwen/GLM/Kimi/MiniMax.
- Disposition: retain Baichuan as an early independent 2023 bridge followed by a later specialization/derivative example. This transition is more informative than treating `Baichuan` as a continuous co-equal general model family through 2026.

## 6. Updated research saturation / Architecture implications

The previous residual questions are now narrowed materially:

- GLM-4 has a version-specific primary technical report and open-repository source.
- Kimi K3 licensing has exact primary text suitable for later Evidence verification.
- MiniMax is confirmed to remain a material general/frontier open-weight agentic branch through M2.7 in 2026 and should appear visibly, but still subordinate to TS-001's four named central families.
- Yi is best treated as a 2023–2024 bridge/open-distribution lineage.
- Baichuan remains active but has moved into medical-specialized models using Qwen-family bases, making it useful as a specialization/ecosystem case rather than a fifth/sixth general-frontier family.

The conventional/direct Source Intake is therefore considered **structurally saturated enough for Discovery closure**, subject to the still-required Grok/X return and final X disposition. Further source expansion should now be driven by concrete Screening/Evidence gaps rather than broad undirected collection.
