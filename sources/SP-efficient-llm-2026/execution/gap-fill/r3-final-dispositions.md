# Sol final gap-fill ledger — Discovery expansion r3 (append-only; r1/r2 ledgers preserved)
# Edition: SP-efficient-llm-2026 | collector_run: efficient-llm-discovery-r3 | observed: 2026-09-21
# r3 graph: discovery/discovery-v2-r3.jsonl (EFF-D143–EFF-D161, GAP_FILL/pass 2) + discovery-accepted-v2-r3.json
# r1/r2 files untouched. New obligation IDs EFF-O13/14/15 introduced (valid non-empty strings per Core
# mechanics; no scope-membership constraint exists pre-Screening; Sol may formalize them into scope at
# Architecture). Lifecycle NOT advanced.

## G21 Conditional Memory — findings
- Engram paper (2601.07372, 2026-01-12) + official repo retrieved. Computation-vs-memory distinction
  established as authors frame it: MoE = sparse activation for dynamic logic; Engram = sparse lookup for
  static knowledge (early layers waste depth reconstructing static patterns otherwise).
- Mechanism: O(1) N-gram lookup, deterministic addressing -> host-memory prefetch, negligible overhead;
  U-shaped Sparsity Allocation law; iso-param/iso-FLOP MoE wins (knowledge/reasoning/code/math);
  long-context training + results.
- Four-way split recorded (MoE weights / attention-KV / RAG / static lookup); Engram-is-RAG prohibited.
- Qwen N-gram linkage verdict: PARALLEL_OR_UNRESOLVED_LINEAGE (no derivation statement; temporal order
  alone proves nothing). Shared design pressure confirmed.
- Precedents bounded at kNN-LM + RETRO (contrast objects only; no RAG history).

## G22 Test-Time Compute — taxonomy and authorities
- Authorities: Snell 2408.03314 (origin) / s1 2501.19393 (budget forcing + sequential-parallel taxonomy,
  benchmark-specific) / ThinkPrune 2504.01296 (RL pruning; body unread, confirm-or-substitute) /
  Overthinking 2604.10739 (peak-then-decline, flip mechanism, 16x cost arithmetic, adaptive stopping) /
  survey 2507.02076 (secondary) / effort-binding record (V4.1 1–100 + Qwen reasoning_effort).
- Six-way distinction recorded: faster generation / fewer reasoning tokens / parallel samples-search /
  difficulty-adaptive / learned stopping / explicit budget. tokens/sec vs tokens/task separation explicit.

## G23 Model Routing — taxonomy and authorities
- Authorities: FrugalGPT 2305.05176 (cascade) / RouteLLM 2406.18665 (single-query preference router, CPT) /
  survey 2603.04445 (unifier; Routoo/speculative-cascade follow-ups parked as survey pointers) /
  fragility EACL-2026 (limitation counterweight) / MoA 2406.04692 (park-leaning boundary probe).
- Five-way taxonomy recorded: MoE routing / MoD / speculative decoding / model routing-cascade /
  Jev specialization. Agent-survey risk contained (MoA parked pending Sol).

## D09 final bounded disposition
- Added DistilBERT + MiniLM + Wanda (metric-not-pipeline). Verdicts: PARK_WITH_REASON for encoder-era
  bridges and structured-pruning pipeline claims; modern reasoning distillation already triangulated
  (R1-distills + OPD-40 + s1K-Gemini-distill). No standalone compression survey.

## Cross-cutting synthesis observation (Discovery-level hypothesis, NOT Selection)
- Inventory now spans nine potentially orthogonal sparsity/allocation axes: parameter-expert / attention /
  depth-token / memory-lookup / precision / decoding-speculation / reasoning-budget / model-routing /
  task-specialization. Candidate framing device for later Sol Architecture review only.

## Carried-forward limitations (known and bounded; completeness does not require resolving all)
- DSpark standalone paper; Jev independent reproduction (+RLCD algorithm); capstone cost-claim
  independence; mHC equivalence; IndexPool confirm-or-drop; FP4 training evidence; DeepSWE/BrowseComp
  standalone methodologies; GGUF/imatrix doc-level bodies; report PDF full-body reads (V4.1/V4/V3.2/
  GLM-5/Engram); ThinkPrune body; MoA materiality; MoD real-LLM adoption; s1-benchmark specificity
  beyond math; cascade price-table staleness (FrugalGPT API-era costs).

## r3 source classes
- 19 records: PRIMARY_PAPER 16, PRIMARY_REPO 2, PRIMARY_MODEL_CARD 1. Zero secondary (survey 2507.02076
  typed as paper-survey but flagged secondary-by-design in raw; mechanism authority never claimed).
