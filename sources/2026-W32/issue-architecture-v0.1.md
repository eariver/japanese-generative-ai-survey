# 2026-W32 Issue Architecture v0.1

Status: **architecture established; article drafting not started**  
Issue: `2026-W32`  
Target length: **approximately 18 pages**  
Allowed range: approximately 16–24 pages per Editorial Specification.

This architecture is derived from `candidate-selection-v0.1.md`. It groups selected records into editorial packages before prose drafting begins.

## Architecture goals

1. Preserve W32 chronology and clearly separate post-cutoff Late Breaking.
2. Avoid a magazine dominated by repeated model-release summaries.
3. Use community evidence to explain what practitioners actually cared about without treating X as technical-fact authority.
4. Use reviewed papers to deepen themes rather than force six isolated paper summaries.
5. Keep at least one distinct item for multimodal/media, memory, agent systems, serving/inference, and safety/security when the evidence supports it.
6. Fit the issue into a readable weekend-magazine format rather than maximizing candidate count.

## Proposed page map

### p.1 — Cover
No substantive article text.

Possible cover anchors:
- OpenAI Astra: scientific reasoning results
- MiniMax H3: omni-modal model → local workflow transition
- Safety boundary beyond the model

Cover choice will be made after article headlines are drafted.

---

### p.2 — Contents + This Week in AI

Purpose: one-page orientation to the issue.

Include approximately 4–5 high-level signals, not mini-articles:

1. Astra makes scientific-reasoning capability concrete through formalized mathematics results.
2. Open/open-weight model discussion is increasingly about what happens **after release**: local workflows, serving integration and harnesses.
3. Multimodal generation receives a real W32 technical story through MiniMax H3 rather than forced category balancing.
4. Safety questions move beyond model behavior into evaluation environments, review harnesses and serving infrastructure.
5. Agent products increasingly create evaluation/governance questions around persistent team agents and open/self-host alternatives.

These are editorial synthesis statements and must be supported in final drafting by the selected records; they are not standalone factual claims.

---

### pp.3–4 — Lead Story: OpenAI Astra — scientific reasoning becomes inspectable

**Primary record:** `openai-astra`

**Supporting evidence:**
- Astra normalized X reaction evidence
- OpenAI primary mathematics publication

**Editorial angle:**
Not "AI solved 10 math problems" as a headline simplification. The story is that OpenAI presented concrete long-horizon mathematical/theoretical-CS outputs, manuscripts and Lean certificates attributed to an internal Astra model, creating an unusually inspectable scientific-reasoning claim.

**Must cover:**
- objective Aug-1 event
- what OpenAI actually claims
- role of human manuscript preparation / model formalization
- why Lean certificates matter
- community reaction: excitement, cost discussion, formal-proof scrutiny, research-taste/human-contribution skepticism
- independent-assessment boundary

**Do not include here:**
- Astra Critical cyber update as if it happened before cutoff; cross-reference Late Breaking instead.

**Target:** ~2 pages.

---

### pp.5–6 — Multimodal Feature: MiniMax H3 — from release to local workflow

**Primary record:** `minimax-h3`

**Supporting records:**
- H3 normalized X reaction evidence
- `sglang-v0.5.17` as post-cutoff infrastructure follow-through

**Editorial angle:**
Use H3 to illustrate the distinction between artifact release and technical-community momentum. The Jul-31 model release becomes a W32 story as open weights/local tooling and hands-on workflows emerge around the cutoff.

**Must cover:**
- omni-modal scope: text/image/video/audio context and generation
- native stereo audio, multi-shot/video context, launch limitations as stated by MiniMax
- exact chronology: Jul-31 release vs W32 community activity
- ComfyUI / distilled LoRA / timing / multi-shot+audio community observations, clearly attributed as social evidence
- core-model vs prompt-rewriter/LoRA GGUF boundary
- brief post-cutoff note that SGLang v0.5.17 adds day-0 H3 support

**Target:** ~2 pages.

---

### pp.7–8 — Model & Open Weight: three different forms of "frontier outside the closed API"

**Core records:**
- `qwen3.8-max-preview`
- `deepseek-v4-flash-0731`
- `kimi-k3`

**Supporting records/evidence:**
- Qwen/Kimi normalized X reaction evidence
- `sglang-v0.5.17` cross-reference
- `kimi-k3-open-weight-retrospective` only as optional narrative context

**Editorial angle:**
This is a comparison package, not three isolated release notes. The three candidates should be differentiated by what W32 made salient:

- Qwen3.8-Max: preview predates the week; W32 interest centers on agent/coding evaluation and open-weight expectations.
- DeepSeek-V4-Flash-0731: Jul-31 official re-post-trained update/weights with agent-focused positioning; community evidence collected after cutoff.
- Kimi K3: large open-weight multimodal/agentic model plus a viral low-memory community implementation claim that exposes the difference between "can run" and "practical to use."

**Must include claim boundaries:**
- vendor benchmark attribution
- preview/release chronology
- Kimi ~8.24 GB claim as community experiment, not established model requirement
- post-cutoff reaction markers where relevant

**Target:** ~2 pages total, preferably comparative table + short analysis rather than three full articles.

---

### p.9 — Agent & Coding: product, harness, evaluation

**Core records:**
- `claude-tag`
- `grok-build-harness-open-source`
- `google-agent-evaluation-flywheel`

**Supporting paper:**
- `paper-from-social-coding-to-agentic-coding` as a short simulation/context box if space allows

**Editorial angle:**
Move beyond "which coding model is best." This page should show three different layers of agent systems:

1. persistent team agent/product surface (`Claude Tag`),
2. orchestration/harness control (`Grok Build`),
3. evaluation/improvement loop (`Agent Evaluation Flywheel`).

**Community angle:**
Claude Tag reaction can introduce self-hosting/model choice/data-governance concerns through Open Tag and related discussion.

**Boundary:**
Claude Tag and Grok Build predate W32; their inclusion is W32 relevance/resurfacing, not launch chronology.

**Target:** ~1 page.

---

### pp.10–11 — Deep Dive: Safety moves outside the model boundary

**Core record:**
- `openai-external-cyber-eval-boundary-event`

**Reviewed supporting papers/models:**
- `paper-prweaver`
- `paper-sparseety`
- `mistral-shieldstral`

**Editorial thesis to test, not assume:**
Several independent W32 sources suggest that AI safety/evaluation increasingly depends on the surrounding environment: evaluation setup, review window, serving optimization and runtime policy machinery. This is an editorial synthesis and must be presented as such.

**Subsections:**

#### A. Evaluation environment
OpenAI Aug-4 third-party cyber evaluation incidents: reduced safeguards / environment misconfiguration can alter observed behavior. Do not label as production sandbox escape.

#### B. Review harness
PRWeaver: detection degradation is strongest when benign and malicious changes coexist in the active review context; long history alone is not the result.

#### C. Serving infrastructure
SparSEEty: sparsity-exploiting serving can create a deterministic side channel under the paper's specific TDX/threat-model assumptions.

#### D. Runtime policy layer
Shieldstral: small policy-adaptive multimodal classifier as a contrasting attempt to put policy enforcement into an explicit runtime component.

**Target:** ~2 pages.

---

### p.12 — Inference / Serving: what production systems actually optimize

**Reviewed records:**
- `paper-llm-serving-in-the-wild`
- `paper-when-does-disaggregation-pay`

**Supporting Late Breaking:**
- `sglang-v0.5.17`

**Editorial angle:**
Pair empirical adoption with architecture trade-offs:

- Serving in the Wild: what framework/method patterns appear in the authors' sampled public Python/GitHub repositories.
- When Does Disaggregation Pay?: when prefill/decode/PDAF separation helps, and when non-disaggregated serving can still win.

This prevents the section from becoming an SGLang/vLLM release-note list.

**Boundary:**
Repository counts are not market share; disaggregation gains are simulation/hardware/workload dependent.

**Target:** ~1 page.

---

### p.13 — Memory Spotlight + Research Paper Watch

#### Primary spotlight: `paper-livemem`
Allocate roughly half to two-thirds of the page.

**Angle:** persistent state continuity under active-context turnover, with explicit limits: finite tested horizon, lossy state, not exact archive/RAG replacement.

#### Short Paper Watch capsules
Use the remaining space for papers not already given substantial treatment:
- `paper-from-social-coding-to-agentic-coding` — simulation result, not causal field evidence.
- optionally a very short reminder/link to Shieldstral if its full treatment is compressed in the Deep Dive.

Papers already embedded deeply in another section (`PRWeaver`, `SparSEEty`, serving papers) should not be summarized again merely to satisfy a Paper Watch quota.

**Target:** ~1 page.

---

### p.14 — X Community Watch: what practitioners actually did

This should be a cross-topic synthesis rather than five repeated mini-articles.

**Evidence source:** normalized Reaction Pass.

Suggested signal groups:

1. **Astra:** initial excitement turned into proof-detail and attribution scrutiny.
2. **MiniMax H3:** attention moved from announcement to local workflows, LoRA and timing experiments around/after cutoff.
3. **Kimi K3:** extreme low-memory execution claim attracted high attention, followed by practicality/throughput caveats.
4. **Qwen3.8-Max:** rankings/open-weight expectation attracted both interest and benchmark/commercial skepticism.
5. **Claude Tag:** persistent team agent discussion quickly connected to self-hosting, model choice and governance.

Every paragraph must remain scoped as X/social observation. Do not use this page to establish technical capability.

**Target:** ~1 page.

---

### p.15 — Late Breaking

#### OpenAI Astra cyber capability update
Record: `openai-astra-cyber-critical-late`

Brief treatment only:
- Aug-7 post-cutoff
- OpenAI says it cannot rule out Critical cyber capability
- internal activity not satisfying controls was paused
- strengthened monitoring/isolation/weight-protection controls
- cross-reference Astra Lead Story without merging the timelines

#### SGLang v0.5.17
Record: `sglang-v0.5.17`

Brief treatment only:
- Aug-8 release
- day-0 support for Kimi K3 and MiniMax H3
- model-specific serving/cookbook support
- cross-reference Multimodal and Open Weight sections

**Target:** ~1 page total.

---

### p.16 — Watchlist + Chronology

#### Watchlist
- `qwen-image-3.0` — real signal, weak independent W32 testing
- `claude-opus-5-community-demos` — optional downstream-use signal
- `local-ai-worlds-fair-track` — broader narrative, overlaps stronger local-model evidence

#### Chronology / small update
- `xai-grok-voice-think-fast-2.0-alias-switch` — Aug-5 default alias switch

#### Explicitly not promoted
A tiny provenance note may mention that several initially collected items were rejected after primary-source verification, but the magazine should not waste normal reader space listing every false positive. Full provenance remains in the repository.

**Target:** ~1 page.

---

### pp.17–18 — References / Source Notes

Contents:
- primary-source references
- reviewed-paper references
- source-class markers where useful
- note explaining that X posts are Social Observation Evidence
- claim-boundary notes for vendor benchmarks, simulation results and post-cutoff items

Target may expand to 3 pages if citation density requires it; the issue remains within the provisional 24-page maximum.

---

## Candidate-to-package map

| Candidate | Package |
|---|---|
| `openai-astra` | Lead Story |
| `minimax-h3` | Multimodal Feature |
| `qwen3.8-max-preview` | Model & Open Weight comparison |
| `deepseek-v4-flash-0731` | Model & Open Weight comparison |
| `kimi-k3` | Model & Open Weight comparison |
| `claude-tag` | Agent & Coding |
| `grok-build-harness-open-source` | Agent & Coding |
| `google-agent-evaluation-flywheel` | Agent & Coding |
| `openai-external-cyber-eval-boundary-event` | Safety Deep Dive |
| `paper-prweaver` | Safety Deep Dive |
| `paper-sparseety` | Safety Deep Dive |
| `mistral-shieldstral` | Safety Deep Dive / Paper context |
| `paper-llm-serving-in-the-wild` | Inference / Serving |
| `paper-when-does-disaggregation-pay` | Inference / Serving |
| `paper-livemem` | Memory Spotlight |
| `paper-from-social-coding-to-agentic-coding` | Paper Watch / Agent context |
| `openai-astra-cyber-critical-late` | Late Breaking |
| `sglang-v0.5.17` | Late Breaking + cross-reference |
| `xai-grok-voice-think-fast-2.0-alias-switch` | Chronology |
| `qwen-image-3.0` | Watchlist |
| `claude-opus-5-community-demos` | Watchlist / optional X note |
| `local-ai-worlds-fair-track` | Watchlist/context |
| `kimi-k3-open-weight-retrospective` | absorbed into Kimi context; no separate slot |

## Expected editorial balance

Approximate substantive page allocation excluding cover/contents/references:

- Scientific reasoning: 2 pages
- Multimodal/media: 2 pages
- Model/Open Weight/Local: 2 pages
- Agents/Coding: 1 page
- Safety/Security Deep Dive: 2 pages
- Inference/Serving: 1 page
- Memory/Paper Watch: 1 page
- X Community Watch: 1 page
- Late Breaking: 1 page
- Watchlist/Chronology: 1 page

This distribution emerges from the evidence pool; it is not a quota system.

## Drafting order

Article drafting should proceed in this order because later packages depend on facts/definitions established earlier:

1. Lead Story — Astra
2. Multimodal Feature — H3
3. Model & Open Weight comparison
4. Safety Deep Dive
5. Agent & Coding
6. Inference / Serving
7. Memory / Paper Watch
8. X Community Watch
9. Late Breaking
10. Watchlist / Chronology
11. This Week in AI summary written **last**, after all article claims are stable
12. References / Source Notes finalization

## Architecture gate

Article construction may begin after this architecture is accepted. Drafts must consume evidence records rather than raw collector output whenever a normalized/verified layer exists.
