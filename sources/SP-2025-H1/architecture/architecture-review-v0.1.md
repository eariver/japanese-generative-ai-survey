# SP-2025-H1 Architecture Review v0.1

Status: **HUMAN GATE 1 — awaiting Architecture approval**  
Coverage: **2025-01-01 00:00:00 UTC — 2025-06-30 23:59:59 UTC**  
Retrospective as of: **2026-08-14T05:38:00Z**

## Intake / Evidence status

- Source Intake: **31** item-level first-party records
- Screening: **31 ACCEPT / 0 HOLD / 0 REJECT**
- Normalized Evidence: **31** records
- Candidate Selection: **31 assigned**
  - FEATURE_CORE: 11
  - SECTION_CORE: 8
  - SUPPORTING_EVIDENCE: 8
  - CHRONOLOGY: 3
  - PAPER_WATCH: 1
- Proposed reader-facing chronology: **approximately 26–30 objective events**

### Material limitations

This Architecture pass is a curated primary-source reconstruction, not an exhaustive crawl of every arXiv paper, GitHub release, vendor changelog, or regional availability event. Living pages are bounded to explicitly dated H1 entries. Vendor benchmark and superlative claims remain attributed and are not treated as independent reproduction.

## Cross-period normalization / identity decisions

1. **DeepSeek-R1 API availability** is kept separate from the late-2024 DeepSeek-V3 event.
2. **GPT-4.5 research preview** and the **April 14 announcement of its API retirement** are separate lifecycle events.
3. **Gemini 2.5 Pro Experimental (Mar 25)** and **Gemini 2.5 Pro/Flash GA (Jun 17)** remain separate chronology events.
4. **Claude 3.7 + Claude Code** is one announcement containing distinct model and coding-agent identities; the narrative may group them, chronology does not erase the distinction.
5. **Operator**, **Deep Research**, **Responses API/Agents SDK**, **Codex**, and **Jules** are not treated as equivalent “agents”: browser action, research, orchestration primitives, and coding sandboxes are distinct action surfaces.
6. **Llama 4 release**, **Llama API preview**, and **Llama Guard 4** are three distinct model/platform/control events.
7. **Qwen2.5-VL**, **Qwen2.5-Omni**, **QVQ-Max**, and **Qwen3** remain separate model identities despite family continuity.
8. Open-weight availability is not equated with hosted API availability or full training/data transparency.

## Proposed editorial thesis

**2025年前半は、生成AIの競争軸が「単体モデルの知識・会話性能」から、推論時に考え、外部情報を調べ、ツールを呼び、ブラウザやコード環境で行動する実行系へ急速に移った半年だった。** 同時に、open-weight MoE・長文脈・native multimodality・生成メディアが並行して進み、model capability・agent harness・tool protocol・deployment形態を分離して読む必要が生じた。

## Proposed packages

| Order | Package | Pages | Primary anchors |
|---|---|---:|---|
| 1 | 2025年前半の技術地図と読み方 | 4 | period / Evidence boundaries |
| 2 | **Reasoningが標準機能になる** | 8 | DeepSeek-R1, o3-mini, Claude 3.7, Gemini 2.5, o3/o4-mini |
| 3 | **ModelからActionへ** | 8 | Operator, Deep Research, Responses API/Agents SDK, Codex |
| 4 | **Model Family Lifecycleが速くなる** | 7 | GPT-4.5→4.1, Claude 3.7→4, Gemini 2.5 Experimental→GA |
| 5 | **Open-weightの再加速** | 8 | DeepSeek, Qwen3, Llama 4, Gemma 3 |
| 6 | **Native Multimodalityと生成Media** | 8 | 4o Image, Qwen2.5-Omni, Veo 3/Imagen 4 |
| 7 | **Execution LayerにはControlが要る** | 5 | MCP, web search, Llama Guard 4, interpretability |
| 8 | **Half-year Synthesis — ReasoningからExecution Stackへ** | 5 | cross-layer synthesis |
| 9 | Detailed Chronology | 4 | selected objective events |
| 10 | References / Source Notes | 3 | provenance / claim boundaries |

Planned envelope: **60 pages** against manifest soft target 64 / hard max 96. Page count remains an output rather than a quota.

## Required half-year analysis

### Cross-month comparison

- **Jan–Feb:** reasoning models and browser/research agents emerge as largely separate product lines.
- **Mar–Apr:** reasoning becomes connected to platform primitives, built-in tools, multimodal generation, and explicit agent SDKs.
- **May–Jun:** coding agents, remote MCP/tool surfaces, and preview→GA lifecycle management make the execution stack persistent rather than experimental decoration.

### Half-year reclassification

- “Reasoning model” is reclassified from an isolated model category into a **capability layer for agent execution**.
- “Open models” are reclassified by **weights/license + MoE + multimodality + deployment portability**, not parameter count alone.
- “Multimodal” is reclassified from input modality support into **interaction/media workflow expansion**, including native image/video/audio generation.

### Cross-layer synthesis

- Better reasoning made tool calling and agent harnesses more useful; broader harnesses then demanded search, MCP, computer use, sandboxing, tracing, and control surfaces.
- Open-weight MoE and native multimodality widened deployment choices while increasing the importance of precise lifecycle, license, safety, and runtime boundaries.

### Unresolved at 2025-06-30

- long-horizon agent reliability and evaluation;
- tool/MCP security boundaries and prompt-injection exposure;
- reproducibility of vendor benchmark claims;
- license/data-transparency differences hidden by the phrase “open model”;
- operational burden from accelerated preview→GA→deprecation API lifecycles.

## Notable hold / exclude decisions

- Do **not** back-project H2 outcomes such as Operator later becoming ChatGPT agent into H1 chronology.
- Do **not** treat later H2 model releases as evidence of H1 capability.
- Do **not** create standalone stories solely from benchmark leaderboard rank.
- Research interpretation is used only where it helps explain the period; `PAPER_WATCH` is not proposed as a separate reader-facing chapter at this stage.

## Human Gate 1 decision

Approval authorizes conversion of `issue-architecture-v0.1.json` from `PROPOSED` to the approved Architecture revision and then preparation of Draft Packages. **No reader-facing drafting has started.**
