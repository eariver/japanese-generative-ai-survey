# SP-2024-H2 Architecture Review v0.2

Status: **AWAITING HUMAN GATE 1**

This replaces the superseded v0.1 review. No reader-facing drafting has started.

## 1. Recovery basis and Source Intake coverage

The first v0.1 attempt is not an approval basis because it treated a manually curated 36-item reconstruction as if it were the complete Source Intake. The edition was reset to the canonical Source Intake / Screening / Evidence path before any Human Gate approval or reader-facing drafting.

The recovered Source Intake is:

- canonical base Source Intake: **5,881 records**;
  - papers: 5,738;
  - GitHub releases: 41;
  - official feed items: 81;
  - official index snapshots: 21;
- supplemental gap-fill through the same Raw → Screening → Evidence boundary: **74 records**;
  - v0.1: 51 item-level first-party vendor/model/API/research events;
  - v0.2: 9 additional full-duplex speech / hybrid SSM-MoE / attention-kernel / open-video sources;
  - v0.3: 14 load-bearing H2 papers known to be absent because of arXiv truncation;
- audited Source Intake total: **5,955 records**.

The base arXiv intake is explicitly **BROAD_SEED_NOT_EXHAUSTIVE**. Calendar-month partitioning repaired the original December-collapse defect, but all 36 month/category queries still reached `max_results=200`. The coverage audit therefore does not claim exhaustive capture; it records the residual limitation and gap-fills material known omissions without replacing the canonical base intake.

The reusable Source Intake contract was also hardened on `main`: standard collectors are now a broad seed rather than a completeness proof; half-year retrospectives require a period-specific coverage audit; material gaps must be supplemented as preserved first-party Raw sources; long-window arXiv intake is temporally partitioned; and supplemental item metadata survives canonical Screening normalization.

## 2. Screening, Evidence, and Candidate Selection basis

Canonical Screening reviewed all **5,955** Source Intake records:

- KEEP: 89
- DROP: 5,866
- MAYBE / INSPECT: 0
- verification queue: 89

Canonical Evidence normalization produced **85 accepted Evidence Tasks**:

- VERIFIED: 85
- CANDIDATE recommendation: 73
- HOLD recommendation: 12
- PARTIAL / NEEDS_MORE / REJECTED: 0

Candidate Selection is an internal editorial checkpoint rather than a Human Gate. The resulting selection contains **73 selected items**; **53** are primary-placement-required roles and **20** are supporting-only roles.

## 3. Editorial thesis

> 2024年後半は、生成AIの競争単位が「単体の基盤モデル」から、open/training artifacts、inference-time compute、multimodal I/O、検索・GUI・tool/protocol接続、serving/quantization/local deployment、grounding/evaluation/controlを組み合わせる execution / deployment stack へ拡張した半年だった。

The retrospective is intentionally not a vendor-by-vendor or month-by-month digest. It separates model capability, inference-time compute, execution surfaces, deployment/runtime form, multimodal interfaces, and control/evaluation boundaries, then reconnects them in the half-year synthesis.

## 4. Proposed issue architecture

Planned total: **64 pages**. Every package is **8 pages or fewer**.

| Order | Package | Type | Pages | Editorial role |
|---:|---|---|---:|---|
| 1 | 2024年後半の技術地図と読み方 | FRONTMATTER | 4 | Coverage auditと評価座標を提示 |
| 2 | Openは「重み公開」から配備・再現性の設計問題へ | LEAD | 8 | Llama/Qwen/DeepSeek/Ai2/Jamba等をdeployment choiceとして比較 |
| 3 | Inference-time Computeが新しい能力軸になる | FEATURE | 8 | o1/QwQ/DeepSeek preview/test-time scaling/FrontierMath |
| 4 | 回答から検索・操作・接続へ | FEATURE | 8 | Search/Computer Use/Structured interfaces/MCP/tool-use evaluation |
| 5 | Multimodalityが理解からRealtime・統合生成・Videoへ広がる | FEATURE | 8 | vision/audio/unified multimodality/image/videoを分離比較 |
| 6 | 能力密度・Serving・Localityを再設計する | COMPARISON | 7 | small model/kernel/caching/distillation/efficient media |
| 7 | Execution Surfaceの拡大にGrounding・Evaluation・Controlが追いつく | DEEP_DIVE | 7 | retrieval/moderation/prompt injection/factuality/alignment |
| 8 | Half-year Synthesis — Model単体からExecution / Deployment Stackへ | SECTION | 6 | cross-month reclassificationとcross-layer synthesis |
| 9 | Detailed Chronology | WATCHLIST_CHRONOLOGY | 5 | release/preview/product/API/evaluation lifecycleを独立保持 |
| 10 | References and Evidence Notes | REFERENCES | 3 | evidence class / primary sources / coverage limitations |

The 64-page figure is a planning target, not a padding requirement. Drafting may later come in shorter; material Evidence must not be dropped merely to force a page count.

## 5. Required identity and claim boundaries

The following distinctions are mandatory in drafting and chronology:

- SearchGPT prototype and ChatGPT search are separate events.
- o1-preview / o1-mini, full o1 product availability, and o1 API availability are separate lifecycle events.
- Llama 3.1, 3.2, quantized 3.2, and 3.3 are not collapsed into one release.
- DeepSeek-V3 is a 2024-H2 event; DeepSeek-R1 public release belongs to 2025 and must not be back-projected.
- Computer Use public beta, structured tool interfaces, MCP protocol, and agent evaluation are different execution primitives; MCP is not evidence that agent reliability was solved.
- Realtime API and Moshi are different speech-system surfaces.
- Sora product rollout, Movie Gen research, and open-video ecosystems are different availability/deployment classes.
- `open` must be decomposed into weights, license, training artifacts, code/runtime support, hosted API, and local/edge deployment rather than used as one binary label.
- vendor/project/author benchmark or performance claims remain attributed claims unless independently reproduced.
- later edits, deprecations, or mature adoption visible on living pages must not be written as if already established in 2024.
- alignment-faking and other safety findings remain bounded to their experimental setup; research evidence is not a deployed guarantee.

## 6. Architecture validation

The proposed plan was checked against the actual Architecture Input on a temporary validation-only PR and was **not merged**. The first validation correctly failed because Evidence boundaries had been paraphrased rather than preserved exactly. After repair, repository CI passed with:

- selected items: 73;
- required primary placements: **53 / 53**;
- missing primary placements: 0;
- duplicate primary placements: 0;
- planned pages: 64;
- maximum package size: 8 pages;
- `this_week_summary_written_last = true`;
- exact Evidence boundaries preserved.

A separate reusable validator defect was also repaired on `main`: the JSON schema already capped each Architecture package at 8 pages, but the Python validator had not enforced that limit. The validator and regression test now agree with the schema.

## 7. Human Gate 1 decision

Current pipeline state remains **SELECTION_COMPLETE**:

- Source Intake preserved: passed
- Candidate inventory: passed
- Evidence normalized: passed
- Candidate Selection: passed
- Issue Architecture: **pending Human Gate 1**
- Article Draft and all later stages: pending

Approval at this gate approves the proposed Architecture and authorizes Draft Package preparation. It does **not** authorize publication; Publication Preview remains the second Human Gate.

To approve this Architecture, record an explicit Human Gate 1 approval for **SP-2024-H2 Architecture v0.2**. If a chapter balance, thesis, package boundary, or emphasis should change, revise it here before drafting begins.
