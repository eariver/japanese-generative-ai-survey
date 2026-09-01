---
issue_id: "2026-W32"
candidate_id: paper-livemem
evidence_type: full-paper-review
review_status: full-reviewed
primary_source: "https://arxiv.org/abs/2608.02515"
publication_date: "2026-08-03"
claim_authority: author-reported-paper-results
---

# LiveMem — Full Paper Evidence Review

## Paper
**LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference**  
arXiv:2608.02515

## Research question
The paper asks whether an LLM can maintain a persistent latent memory state across **context turnover**: old KV-cache content is evicted from the active attention window, but task-relevant historical influence remains available through a fixed-size recurrent state.

The authors distinguish this from reconstructive memory systems such as external retrieval. Their target is not exact archival storage, but a continuously updated inference state that persists as the working context changes.

## Method
LiveMem augments a pretrained decoder transformer with a recurrent side branch attached to each attention layer.

- Main attention provides precise access to a bounded active context.
- A Gated DeltaNet-2 (GDN2) branch maintains a fixed-size recurrent state and updates it per token.
- Side-branch output is added to the normal attention output.
- Context is processed in chunks. Old KV pages are evicted FIFO once the active-context budget is exceeded, while the recurrent state remains.
- The system prompt is retained as an attention sink.
- The pretrained backbone is frozen for the primary memory-oriented post-training; the memory branch is trained.
- The paper explores both supervised fine-tuning and an RL stage using a GRPO-style objective.

Primary locator: Sections 2–3; especially §3.1–3.3.

## Serving implementation
Appendix C.3 describes a concrete paged serving lifecycle:

- the normal attention manager stores recent KV pages plus the instruction sink;
- a separate per-request paged slot stores recurrent state for memory-augmented layers;
- evicted complete KV pages are returned to the allocator while recurrent state persists;
- recurrent state is gathered/updated/scattered per serving step;
- the recurrent slot is released when generation finishes, explicitly preventing accidental state leakage across requests.

This is important because the paper is not only an architectural proposal; it specifies how context turnover and state lifecycle map into serving.

## Evaluation setup
All systems use Qwen3-4B-Instruct-2507 as the base model. Active context is restricted to 32K tokens, or 8K for shorter datasets, to force turnover.

Evaluation groups include:
- Wiki QA: 2WikiMultiHopQA, HotpotQA, MuSiQue and packed multi-question variants;
- Conversation: LoCoMo, LongMemEval and FactConsolidation;
- Test-Time Learning (TTL): six MemoryAgentBench subsets;
- Long QA: InfinityBench QA, EventQA and NarrativeQA.

Comparisons include direct Qwen3-4B, RAG, a recurrent text-memory baseline, Context2LoRA, delta-Mem, LiveMem-SFT and LiveMem-RL.

Primary locator: §4.1, Table 1.

## Main author-reported results
Table 1 reports overall bounded-context scores:

- RAG: 0.458
- Recurrent: 0.389
- Context2LoRA: 0.281
- delta-Mem: 0.327
- base Qwen3-4B: 0.451
- LiveMem-SFT: 0.505
- LiveMem-RL: 0.519

However, LiveMem is **not universally best**. Examples:
- On TTL overall, Context2LoRA reports 0.739 versus LiveMem-RL 0.678.
- Several individual QA tasks favor the base/RAG/other baselines.

The paper itself explicitly states that LiveMem is not universally optimal and that retrieval and parametric-memory approaches retain complementary strengths.

## Evidence after active-context eviction
The paper directly compares LiveMem with and without historical information encoded in the recurrent state after old evidence has left active attention. Across the reported state-vs-truncation comparisons, the authors report positive gains for the RL variant, supporting the narrower claim that task-relevant historical influence can persist across turnover.

Primary locator: §4.3 / Table 2 and associated LongMemEval analyses.

## Critical limitation: lossy state is not an archive
Appendix E.1 is a publication gate for any editorial claim.

On needle-in-a-haystack variants:
- with a fully materialized 256K context, systems are near ceiling on most variants;
- under a bounded 32K context after needles have left accessible KV, LiveMem, base Qwen3-4B and delta-Mem all obtain the same low scores (0.19/0.18/0.21/0.23 in Table 6).

The authors conclude that current LiveMem does **not reliably reconstruct arbitrary token-level needles after their KV entries are released**.

They characterize the memory as a fixed-size lossy state optimized to preserve useful features, not verbatim history. For exact archival recall, the paper recommends combining LiveMem with retrieval or an external store.

## Additional limitation: finite positional horizon
Although recurrent-state size and active-KV budget do not grow with total history, the tested Qwen3 backbone retains a configured positional maximum of 262,144 tokens. The experiments therefore process at most 256K input tokens. The system is not literally unbounded in the demonstrated implementation.

Primary locator: Appendix E.2.

## Evidence assessment
### Supported by the paper
- LiveMem implements a persistent recurrent state alongside bounded attention.
- The authors demonstrate measurable task-relevant influence after evidence is evicted from active context.
- Their aggregate bounded-context evaluation favors LiveMem-RL overall in the tested setup.
- A concrete paged serving lifecycle is described.
- The mechanism is lossy and does not preserve arbitrary exact historical tokens.

### Author-reported quantitative claims only
All benchmark scores and superiority comparisons remain results of this paper's setup, not independently reproduced facts.

## Safe editorial statements
- LiveMem explores **state continuity**, not simply a larger context window: KV can be released while a recurrent latent state persists.
- In the authors' Qwen3-4B experiments, LiveMem-RL has the strongest aggregate score across the tested bounded-context suites, but individual tasks favor other memory approaches.
- The paper explicitly shows the memory state is lossy; it should be paired with retrieval/external storage when exact historical recall is required.

## Do not claim
- “LiveMem remembers everything after context eviction.”
- “LiveMem replaces RAG.”
- “LiveMem provides unlimited context.”
- “LiveMem is best on every memory benchmark.”

## Editorial significance before selection
Technically distinct from generic long-context/RAG stories because the central object is a persistent **inference state lifecycle**. It can support a Memory topic if the issue architecture later has room, but this record does not itself decide inclusion.