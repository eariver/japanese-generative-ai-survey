# 2026-W32 Candidate Selection v0.1

Status: **selection complete for issue architecture**  
Issue: `2026-W32`  
Basis: `candidate-matrix-v0.2.md`, reviewed paper evidence, normalized X reaction evidence, and verified primary-source screening.

This document decides the editorial role of each inventory record. It does **not** draft articles and does not yet prescribe exact page layout.

## Selection principles

1. **Technical significance over source volume.** A topic is not selected merely because many posts or sources exist.
2. **W32 relevance may come from either a main-window event or meaningful W32 technical momentum.** Objective chronology and community timing remain separate.
3. **One underlying topic should not occupy multiple standalone slots simply because it appeared in multiple collectors.** Related X reactions, OSS integrations, and retrospective posts may become supporting evidence rather than separate articles.
4. **Post-cutoff events remain explicitly Late Breaking.** They may support a main-window story but should not be silently backdated into the main issue.
5. **Reviewed papers can be selected for Paper Watch or promoted into a thematic feature when their technical contribution is more useful there.**
6. **HOLD records are excluded from the planned issue unless the issue architecture later makes their unresolved claim material enough to justify candidate-specific verification.**
7. **Rejected false positives remain in the inventory for provenance but do not consume editorial space.**

## Editorial-role vocabulary

- `FEATURE_CORE`: substantial standalone coverage is justified.
- `SECTION_CORE`: a substantive but shorter standalone item is justified inside a topical section.
- `PAPER_WATCH`: selected for concise reviewed-paper coverage.
- `SUPPORTING_EVIDENCE`: useful evidence/context to merge into another selected topic; not a separate article.
- `X_REACTION_SUPPORT`: community evidence to integrate into another selected topic or X Community Watch synthesis.
- `LATE_BREAKING`: post-cutoff item selected for brief treatment.
- `CHRONOLOGY`: valid event selected for chronology / release-notes style coverage rather than a substantive article.
- `WATCHLIST`: retain as a weak/secondary signal without forcing a main article.
- `HOLD_OUT`: not selected unless its unresolved claim is later made material by the architecture.
- `EXCLUDE_W32`: not a valid W32 editorial candidate under current evidence.

## Selected editorial pool

### FEATURE_CORE

#### `openai-astra`
**Why retain:** A main-window OpenAI research event with unusually concrete mathematical/theoretical-CS outputs, Lean formalization, clear technical novelty, and meaningful expert/community scrutiny. It is distinct from ordinary benchmark/model-release coverage.

**Boundary:** OpenAI's characterization of the ten advances must be separated from independent mathematical judgment. Model-vs-human contribution remains a caveat.

**Supporting records:**
- `openai-astra-cyber-critical-late` — separate post-cutoff safety event, not factual support for the mathematics claims.
- X reaction evidence for Astra — integrate as community scrutiny, not technical validation.

#### `minimax-h3`
**Why retain:** Provides the strongest W32 multimodal/media-generation story and a concrete example of release-to-local-ecosystem transition. The technical scope is materially different from the LLM/agent-heavy candidates.

**Boundary:** Separate the Jul-31 artifact release from W32/post-cutoff local workflow activity. Do not generalize prompt-rewriter/LoRA GGUF evidence into a claim about H3 core-model GGUF availability.

**Supporting records:**
- `sglang-v0.5.17` — Late Breaking serving integration.
- H3 X reaction evidence — local ComfyUI, LoRA, timing and multi-shot/audio workflow activity.

#### `openai-external-cyber-eval-boundary-event`
**Why retain:** A verified Aug-4 main-window event that exposes a technically important evaluation-boundary problem: reduced safeguards and environment misconfiguration can alter what an advanced model appears to do. This is operationally distinct from model-level capability scoring.

**Boundary:** Do not describe either incident as a production sandbox escape. Preserve the exact evaluation-environment context.

#### `paper-livemem`
**Why retain:** It adds a genuinely distinct memory/state-continuity topic not otherwise represented in the candidate pool. Full review shows that the interesting contribution is persistent lossy state continuity under KV turnover, not an "infinite memory" claim.

**Boundary:** Treat long-horizon memory as finite and lossy under the evaluated setup; do not equate it with exact archival recall or RAG replacement.

### SECTION_CORE

#### `qwen3.8-max-preview`
**Why retain:** Strong W32 community relevance around agent/coding evaluation and open-weight expectations, despite the preview debut predating the window. Useful as part of the model/open-weight landscape rather than as a false "new Aug release" story.

**Boundary:** Keep the Jul-19 preview chronology explicit; benchmark/harness and future weight/license claims require attribution.

#### `deepseek-v4-flash-0731`
**Why retain:** A verified Jul-31 official update/weights event immediately adjacent to the W32 window, with a technically meaningful re-post-training/agent capability angle and clear serving relevance.

**Boundary:** Reaction-Pass community evidence is post-cutoff only; vendor benchmark claims remain vendor claims.

#### `kimi-k3`
**Why retain:** A large open-weight multimodal/agentic model with W32-specific local-inference community salience. The viral low-memory pure-C experiment makes it editorially distinct from a generic model release.

**Boundary:** The ~8.24 GB RAM claim remains a community implementation claim until reproduced; large disk footprint and low throughput must travel with the discussion.

#### `claude-tag`
**Why retain:** Not a W32 launch, but the W32 reaction around persistent team agents, Open Tag, self-hosting, model choice and data governance provides a concrete agent-productization/governance story.

**Boundary:** Do not describe Aug 3 as the original Claude Tag launch without separate primary support.

#### `google-agent-evaluation-flywheel`
**Why retain:** Provides methodology rather than another product-release item: dataset generation, evaluation, failure analysis and improvement loops for agents. It helps the issue discuss how agent systems are evaluated, not only how they are launched.

**Boundary:** Treat W32 as relevance/discovery unless a distinct W32 release event is established; the underlying docs predate the window.

#### `grok-build-harness-open-source`
**Why retain:** Verified Jul-15 open-source harness underlying the W32 resurfacing. It is useful as an example of the model-to-harness shift and community control over coding-agent orchestration.

**Boundary:** W32 is resurfacing/community relevance, not the original open-source date. Downstream GUIs/extensions remain social unless separately verified.

### PAPER_WATCH

#### `mistral-shieldstral`
Selected for concise Safety/Paper coverage. The 3B policy-adaptive multimodal classifier is technically interesting, but community reaction is modest and independent adversarial validation is absent.

#### `paper-llm-serving-in-the-wild`
Selected as empirical serving-context coverage. Repository counts characterize the authors' public-GitHub/Python sample, not global market share.

#### `paper-when-does-disaggregation-pay`
Selected because the full review supports a nuanced systems result: disaggregation is workload/hardware dependent and can lose to non-disaggregated serving in some regimes. Avoid headline-only use of the maximum throughput gain.

#### `paper-sparseety`
Selected for serving/security coverage. The contribution is an architecture/threat-model-specific deterministic side channel in sparsity-exploiting serving, not a generic TDX or sparsity failure.

#### `paper-prweaver`
Selected for coding-agent/security coverage. The strongest result concerns detection degradation when benign and malicious changes coexist in the active review window, not merely "long PR history is hard."

#### `paper-from-social-coding-to-agentic-coding`
Selected for a short socio-technical note with a strong simulation disclaimer. Its quantitative results are simulation outputs, not observed causal effects in real GitHub communities.

## Selected Late Breaking

### `openai-astra-cyber-critical-late`
**Role:** `LATE_BREAKING`

OpenAI's Aug-7 post-cutoff Preparedness update is substantial enough that omitting it would make Astra coverage stale. The exact safe wording is that OpenAI **could not rule out** Critical cyber capability; do not write that Astra was formally classified Critical.

### `sglang-v0.5.17`
**Role:** `LATE_BREAKING`

Aug-8 release selected because it provides a concrete infrastructure follow-through for two already selected model stories: Kimi K3 and MiniMax H3. It should normally be brief and linked to those stories rather than inflated into an independent lead.

## Chronology selection

### `xai-grok-voice-think-fast-2.0-alias-switch`
**Role:** `CHRONOLOGY`

Valid Aug-5 default-alias change. Technically real but too small for substantive weekly coverage unless bundled into a release-note/chronology box.

## X / community evidence retained as support, not duplicate articles

The following reaction streams should be consumed by the selected topic they illuminate rather than counted as additional stories:

- Astra reactions: mathematical excitement, Lean scrutiny, human-contribution skepticism.
- Qwen3.8-Max reactions: agent/coding rankings, open-weight expectation, benchmark skepticism.
- MiniMax H3 reactions: local ComfyUI/LoRA/timing/multi-shot+audio activity; most hands-on posts are post-cutoff.
- Kimi K3 reactions: low-memory pure-C experiment and post-cutoff practicality caveats.
- Claude Tag reactions: Open Tag/self-hosting/model-choice/data-governance discussion.

## WATCHLIST

### `qwen-image-3.0`
Retain because it is a real image-model signal and standalone image coverage is otherwise thin, but independent W32 technical testing is too weak for normal promotion.

### `claude-opus-5-community-demos`
Interesting downstream use-case signal, but the Reaction Pass did not normalize it and the underlying model predates the window. Keep as optional small X note only.

### `local-ai-worlds-fair-track`
Useful as broad Local AI context but source/date normalization is incomplete and it overlaps heavily with the stronger H3/Kimi/SGLang evidence.

### `kimi-k3-open-weight-retrospective`
Retain only as narrative context for the selected Kimi K3 item; not a standalone event.

## HOLD_OUT — not selected unless later architecture makes them material

- `openai-gpt-5.6-w32-update` — distinct W32 update unresolved.
- `kimi-k3-github-copilot` — integration not primary-confirmed.
- `github-copilot-cloud-agent-w32` — exact August event unresolved.
- `claude-opus-4.1-api-retirement` — exact Anthropic retirement notice unresolved.
- `repowise-agent-tool-efficiency` — repo/method/numeric claims unresolved.
- `qwen3.8-27b-local-expectation-late` — speculative social claim without official model/weights confirmation.

These should not consume verification time unless the issue plan later depends on them.

## EXCLUDE_W32

- `grok-imagine-video-1.5` — product exists, but W32 technical-community momentum failed the Reaction-Pass threshold.
- `nvidia-voicechat` — March event misidentified as August.
- `meta-muse-code-spark-1.2` — collected W32 event not confirmed by Meta primary evidence.
- `anthropic-skill-plugin-security-scanning` — real related feature is March, not a new W32 event.
- `github-spark-retirement` — no matching W32 primary event found.
- `xai-imagine-image-2.0` — collected W32 event not confirmed by xAI primary evidence.

## Cross-topic consolidation constraints

### Do not double-count Astra
`openai-astra` and `openai-astra-cyber-critical-late` are two verified events tied to the same model but different domains and time positions. They may share a feature package, but the post-cutoff cyber item must remain visibly Late Breaking.

### Do not double-count H3/Kimi serving support
`sglang-v0.5.17` is best treated as post-cutoff infrastructure follow-through to H3/Kimi, not a third independent "open-model" story.

### Keep model facts separate from community experiments
Kimi low-memory inference and H3 local workflows are strong editorial evidence of what practitioners cared about, but their numerical performance/resource claims should remain attributed to the individual community implementations.

### Use papers to add orthogonal technical depth
Paper Watch should not become six isolated summaries if some papers are better used to deepen selected themes. In particular:
- `paper-sparseety` can deepen serving/security discussion.
- `paper-prweaver` can deepen agent/coding security discussion.
- `paper-llm-serving-in-the-wild` and `paper-when-does-disaggregation-pay` can jointly contextualize serving architecture.
- `paper-from-social-coding-to-agentic-coding` can contextualize team-agent/social-governance discussion.

## Selection result summary

- Feature core: **4**
- Section core: **6**
- Paper Watch: **6**
- Late Breaking: **2**
- Chronology: **1**
- Watchlist/context: **4**
- Hold out: **6**
- Exclude W32: **6**

Counts intentionally overlap editorial consumption roles only where explicitly stated; supporting X evidence is not counted as a separate candidate story.

## Gate

The pool is now sufficiently selected to design the issue architecture. Architecture should target approximately 16 pages and avoid forcing every selected item into a full standalone article. Some selected records should be synthesized into shared sections or sidebars.