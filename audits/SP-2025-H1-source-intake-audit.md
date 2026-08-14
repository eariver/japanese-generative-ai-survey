# SP-2025-H1 Source Intake retrospective audit

Status: research-only audit; **no change to frozen SP-2025-H1 publication state**

Audit branch: `audit/2025-H1-source-intake`  
Audit workflow run: `31805596602`  
Audit branch head used for successful run: `ca19433795f8718662120cc5bf0eafc47697a296`  
Workflow artifact: `SP-2025-H1-source-intake-audit` (`sha256:0ca6125dc9821a8f9c832a1e2a1746cb2f139f9f869b2528988d86aecb3d962b`)

## Question

The frozen 2025-H1 edition was built from a 31-record `CURATED_PRIMARY_SOURCE_RECONSTRUCTION`. This audit asks whether rerunning the **current** broad Source Intake and performing a targeted first-party coverage review reveals a technical story materially different from the published edition, or a major omitted information surface.

This audit does not reopen Screening, Evidence, Architecture, Freeze, or Release. It is diagnostic only.

## Current base Source Intake rerun

The current Special collector was run over the exact frozen H1 window, `2025-01-01T00:00:00Z` through `2025-06-30T23:59:59Z`, with all enabled base collectors.

Result: **success** for all eight collector runs.

### arXiv temporal collection

The current long-window collector correctly partitioned the six-month period into calendar months.

| Month | Unique normalized paper records |
|---|---:|
| 2025-01 | 976 |
| 2025-02 | 952 |
| 2025-03 | 961 |
| 2025-04 | 976 |
| 2025-05 | 954 |
| 2025-06 | 965 |
| **Total** | **5,784** |

Important limitation: **all 36 category × month arXiv queries reached the configured 200-result cap**. The current collector correctly records all 36 as `possible_truncation=true`. Therefore 5,784 is a broad research seed, not an exhaustive paper corpus. A period-specific coverage audit remains mandatory.

The broad paper pool independently exposes themes already central to the published H1 narrative, including test-time scaling/reasoning, tool protocols, agent security, multimodal systems, and deployment/runtime work. Examples include `s1: Simple test-time scaling` (2025-01-31) and multiple MCP/A2A security and protocol papers in March-June.

### GitHub release collection

The configured runtime/framework watchlist produced **89 release records**:

- SGLang: 6
- vLLM: 18
- Hugging Face Transformers: 38
- TensorRT-LLM: 15
- ComfyUI: 12
- llama.cpp: 0 release objects in the API window
- FlashInfer: 0 release objects in the API window

This is a meaningful difference from the original 31-record reconstruction, which contained no dedicated serving/runtime event. In particular, vLLM V1 was announced as a core-architecture redesign on 2025-01-27 and became the default engine around the v0.8.0 transition in March. This does not overturn the published H1 thesis, but it shows that the execution/deployment layer deserved at least explicit supporting treatment.

### Official-source collection

All **22 configured official source surfaces** were fetched with zero collector errors.

After normalization the base audit index contains:

- official feed items: 121
- official index snapshots: 21
- GitHub releases: 89
- papers: 5,784
- **total Screening input records: 6,015**
- Screening batches: 41

Ordinary index snapshots still require item-level historical extraction; a successful index fetch is not itself a completeness proof.

## Targeted first-party coverage audit against the frozen 31-record reconstruction

The following H1 events/surfaces were absent from the frozen 31-record curated intake but are material enough that the current coverage policy would require them to enter Screening/Evidence consideration.

### Material omissions

1. **xAI Grok 3 Beta — 2025-02-19**
   - First-party: https://x.ai/news/grok-3
   - Reasoning models (`Grok 3 (Think)` / `Grok 3 mini (Think)`), DeepSearch and an explicitly agent-oriented product direction.
   - Editorial effect: strengthens the published `Reasoning -> execution` thesis; does not contradict it, but omission removes a major vendor from the reasoning comparison.

2. **Google Gemini 2.0 general availability / model-family update — 2025-02-05**
   - First-party: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-updates-february-2025/
   - Gemini 2.0 Flash GA plus Flash-Lite / Pro Experimental context, following the earlier agentic-era framing.
   - Editorial effect: a material lifecycle/model-family event between late-2024 Gemini 2.0 and the published H1 emphasis on Gemini 2.5.

3. **Google Agent2Agent protocol (A2A) — 2025-04-09**
   - First-party: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
   - Cross-vendor agent interoperability protocol.
   - Editorial effect: strongly reinforces the published transition from isolated agent products toward an execution/tool/protocol stack. Under the published H1 Architecture this would likely be SECTION/SUPPORTING evidence in the Agent or Control package, and potentially chronology-worthy.

4. **Mistral H1 release sequence — January through June 2025**
   - First-party index: https://mistral.ai/news/
   - Material H1 items include Mistral Small 3, Mistral OCR, Small 3.1, Medium 3, Devstral, Agents API, Mistral Code, Magistral, and Mistral Compute.
   - Particularly relevant:
     - Agents API (2025-05-27): built-in connectors for code execution, web search, image generation and MCP tools, memory and orchestration.
     - Devstral (2025-05-21): open agentic software-engineering model.
     - Magistral (2025-06-10): reasoning-family development.
   - Editorial effect: this is the clearest vendor-level hole in the original reconstruction. It still points in the same reasoning/agent/execution direction, but the omission is too large to call the original intake ecosystem-complete.

5. **vLLM V1 — 2025-01-27 and March default transition**
   - First-party: https://vllm.ai/blog/2025-01-27-v1-alpha-release
   - Core serving architecture redesign covering scheduler, KV-cache management, API server/execution loop, multimodal support and other inference concerns.
   - Editorial effect: adds a runtime/deployment axis that the frozen H1 architecture only treated indirectly. It does not require discarding the thesis, but suggests execution-stack synthesis should explicitly include runtime.

6. **GitHub Copilot coding agent — 2025-05-19 public preview**
   - First-party: https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/
   - Background coding agent in a GitHub Actions-powered cloud environment, issue delegation and PR-based review.
   - Editorial effect: directly comparable with Codex and Jules; omission weakens vendor breadth of the published coding-agent comparison.

### Additional omissions that mainly strengthen existing packages

- **Runway Gen-4 — 2025-03-31**: world-consistent controllable video/media generation; supports the published `multimodal -> creative workflow` reclassification. First-party: https://runwayml.com/research/introducing-runway-gen-4
- **Apple Foundation Models framework — 2025-06-09**: on-device foundation-model API with guided generation and tool calling, adding an on-device/private/offline execution surface. First-party: https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/
- **Open research such as `s1: Simple test-time scaling`**: the broad arXiv pool contains important reasoning research that was not represented by the original single PAPER_WATCH item. This strengthens the test-time/reasoning arc rather than changing its direction.

There are other candidate surfaces (MiniMax, NVIDIA model/runtime work, Cohere, Baidu/Tencent families, Adobe generative media, etc.) that would deserve Screening under the current policy, but the items above are sufficient to decide the audit question.

## Comparison with published H1 architecture

### Reasoning

**Published conclusion remains directionally correct and is strengthened.**

The original R1/o3/Claude 3.7/Gemini 2.5/Qwen reasoning story is supported by the broader intake. Grok 3, Magistral, test-time-scaling research and other reasoning work expand vendor/research breadth but do not reveal an opposing trend.

### Agents / execution

**Published conclusion remains correct, but the ecosystem was under-sampled.**

A2A, Mistral Agents API, GitHub Copilot coding agent, and additional protocol/security research all reinforce the shift from model response to action surfaces, orchestration and interoperability. Their absence means the chapter was narrower than the H1 ecosystem actually was.

### Open-weight / deployment

**Published reclassification remains useful, with one missing layer.**

The broader intake supports the need to separate weights, APIs, model architecture and deployment. However, vLLM V1 and the 89 watched runtime/framework releases show that serving/runtime evolution was material enough to be named explicitly in the cross-layer synthesis.

### Native multimodality / generative media

**Published conclusion remains correct.**

Runway Gen-4 and other media-generation systems broaden the vendor set but reinforce the same movement from multimodal input capability toward production/creative workflows.

### Overall half-year synthesis

The frozen synthesis — `reasoning + agent primitives + open-weight multimodality + tool protocol -> execution stack` — is **not falsified by the broader audit**. Most important newly identified evidence points in the same direction.

A more complete reconstruction would broaden that synthesis to make **agent interoperability and serving/runtime/on-device execution** more explicit.

## Verdict

Two different questions need different answers:

1. **Does the published SP-2025-H1 broadly describe the correct technical arc of 2025-H1? — YES.**
   - The central thesis and chapter-level reclassifications remain well supported by the much broader intake and targeted first-party audit.
   - No omitted counter-trend was found that requires replacing the issue's overall Architecture.

2. **Can we certify that there was no major information omission? — NO.**
   - The original 31-record intake omitted several material vendor/event surfaces: Grok 3, Gemini 2.0, A2A, the Mistral H1 sequence, vLLM V1, and GitHub Copilot coding agent are the clearest examples.
   - These omissions mostly strengthen or broaden existing chapters rather than overturning them, but they are significant enough that the frozen 31-record reconstruction would **not satisfy the current half-year Source Intake coverage contract**.

Therefore the appropriate characterization is:

> **Architecture-level interpretation: broadly sound. Event/ecosystem coverage: materially incomplete.**

No publication correction is proposed by this audit alone. Reopening the frozen edition would be a separate editorial decision and is outside this research-only branch.
