# Architecture Review Preparation Package r1 — SP-efficient-llm-2026 (operator package for Sol)

Status: `OPERATOR_PACKAGE_FOR_SOL / NOT_THE_HUMAN_DOSSIER`
Date: `2026-09-22`
Prepared by: Muse (Luna/Work execution role) from Sol-reviewed Selection semantics.
Sol will independently review this package and owns the Human-facing dossier.
No Human decision is recorded or implied anywhere in this run.

## 1. Reviewed branch HEAD

- Branch: `special/efficient-llm-2026-work`
- HEAD at execution: `cca2b71e82861d479ce070c65edd5bcf95a9e8e0` (exact starting SHA; unchanged during this run until the closing commits below)
- Remote `main` guard: `175b327f6126e2f0759861067852105ee5a290aa`; delta from the edition's start-of-run reviewed main (`f85539c3…`) is documentation-only (`docs/core-v2-deferred-maintenance-summary.md` recording CV2-DM-016/017); no merge performed.

## 2. Active Evidence/View authority

- Evidence acceptance: `sources/SP-efficient-llm-2026/evidence/v2/accepted/dba89409c1cdcfb6a8b319ef35e0e1ee1b5ffdc74cad4715dbe44e10345e5603/evidence-accepted.json` (SHA `72ba3407…`, 160 Cards)
- Edition Views acceptance: `sources/SP-efficient-llm-2026/evidence/v2/views/accepted/2bf475f518d80c8088dff7a67a0bc5cae5e2fa5c9a309d56695e66b1d54d7762/edition-views-accepted.json` (SHA `364d484a…`, 160 views)
- Materiality Ledger: `sources/SP-efficient-llm-2026/materiality-ledger-v2.json` (SHA `ad750936…`)
- Profile Completeness: `sources/SP-efficient-llm-2026/profile-completeness-v2.json` (SHA `aeeadd19…`, LIMITED)
- Sol Evidence Review: `sources/SP-efficient-llm-2026/execution/reviews/sol-evidence-review-pass-20260922.md` (Sol / GPT-5.6, PASS / PROCEED_TO_SELECTION_WITH_SCOPE_BOUNDARIES)

## 3. Discovery / Screening / Evidence counts

- Discovery: 165 records (EFF-D001–D165); acceptance SHA `7074cef2…`
- Screening: 135 KEEP / 20 MAYBE / 5 INSPECT / 5 DROP (acceptance `24bac6aa…`)
- Evidence: 160 Cards — 12 VERIFIED / 148 PARTIAL / 0 NEEDS_MORE / 0 REJECTED
- Materiality: 137 MATERIAL / 23 CONTEXT / 5 EXCLUDED (the 5 DROPs)
- Completeness: LIMITED (15 obligations: 3 SATISFIED / 12 LIMITATION)

## 4. Selection disposition counts

- Candidates: 160 (Matrix SHA `1dcc2902…`); Selection SHA `f91af7cf…`
- SELECTED 112 (53 PRIMARY / 59 SUPPORTING) / HOLD 12 / REJECT 33 / INSPECT 3
- Count safeguards: selected_count 112 is within [40, 120]; neither the compression (<40) nor the redundancy (>120) audit trigger fired. Explicit compression rationale is nevertheless recorded per-candidate (see §8–§10).

## 5. Complete selected candidate IDs

PRIMARY (53): D001 D002 D003 D005 D006 D007 D008 D010 D011 D012 D014 D015 D018 D019 D020
D026 D027 D028 D030 D032 D033 D036 D038 D041 D042 D045 D048 D050 D053 D055 D059 D061
D062 D070 D071 D092 D093 D094 D098 D118 D123 D125 D128 D141 D143 D148 D149 D150 D151
D153 D154 D155 D157.
SUPPORTING (59): D004 D013 D024 D025 D029 D034 D035 D037 D039 D040 D043 D044 D047 D049
D051 D056 D064 D065 D066 D067 D068 D069 D072 D073 D078 D080 D081 D100 D101 D103 D109
D110 D112 D113 D114 D115 D116 D117 D119 D120 D121 D122 D126 D127 D129 D130 D131 D132
D133 D135 D136 D139 D142 D144 D145 D162 D163 D164 D165.

## 6. HOLD / REJECT / INSPECT IDs

- HOLD (12): D074 D076 D079 D082 D086 D087 D097 D099 D146 D147 D152 D156.
- REJECT (33): D009 D016 D017 D021 D022 D023 D031 D046 D052 D054 D057 D058 D060 D063
  D075 D083 D088 D089 D090 D091 D095 D096 D102 D104 D105 D106 D107 D108 D111 D124
  D134 D137 D138.
- INSPECT (3): D077 D084 D085.
- Screening DROPs (not in Matrix, remain screening-REJECT, no resurrection): D140 D158 D159 D160 D161.

## 7. Major candidate map

- Bottleneck contract (P1): Kaplan/Chinchilla/Orca primaries.
- Conditional compute (P2): Shazeer/GShard/Switch origins, DeepSeekMoE/V2 modern line, V3-FP8/MTP, Muon; ZeRO/Megatron context; data-mixture support.
- Attention/memory (P3): MQA/GQA, FlashAttention exact-IO, NSA, Kimi Linear (body-consumed), DSA trace + V3.2 mechanism primary, Engram conditional memory, KV-budgeting quartet minus SnapKV, prefix/LMCache, MoD/LayerSkip, DeeBERT bound.
- Precision/local (P4): int8/GPTQ/QLoRA/GGUF/llama.cpp primaries, FP8/MX/spec support, Unsloth bounded, llama.cpp Qwen port, X ledger bounded.
- Decode/TTC (P5): spec-decoding origins, EAGLE/MTP primaries, Snell/s1/ThinkPrune/overthinking VERIFIED core, effort-control binding, R1-distill context.
- Serving (P6): PagedAttention/vLLM, SGLang paper, Splitwise, Mooncake, SARATHI primaries; DeepEP/DeepGEMM/FlashInfer/vLLM-recipe support.
- Routing/Jev (P7): FrugalGPT/RouteLLM/fragility primaries; Jev launch+concepts+Models primaries with bounded vendor claims; API-ref/community corroboration.
- Capstones (P8): V4.1 report+card, Qwen report, Kimi repo, GLM-5 report (abstract-scope) primaries; full first-party doc/repo/card/runtime/X support ring.
- Methodology (P9): SWE-bench/Pro, T-Bench, RULER, MLPerf primaries; harness/tooling/caveat support.

## 8. High-signal unselected candidates and reasons

All 32 MATERIAL REJECTs carry named-supersession rationale in the canonical
input (no bare `redundant` without a named superseding source; two rationales
use `redundant` only as a summary adjective AFTER naming D004/D163 and
D136/D005/D049 respectively):
training-parallelism depth D102/D104/D105/D106/D107/D108 → D101/D103 (+D098/D026/D027
for inference long-context); Qwen/GLM/V4.1 announcement and predecessor duplication
D009/D016/D017/D031/D083/D124 → body-consumed first-party anchors D008/D123/D128-D131;
FA version intermediates D021/D022 → D020+D056; Mamba D023 → D024+D027; SparseGPT
D046 → GPTQ/AWQ+D150; serving-stack depth D054/D057/D058/D060/D063 → D055/D056/D066/
D059/D061/D004/D163; benchmark-definition pages D088/D089/D090/D091/D095/D096 →
P9 validity exhibits D092/D093/D094/D098/D118 (P8 compares stacks, not ranks);
SnapKV D111 → D109+D112; MX paper D137 → D136 spec; dedup D138 → D139; Ascend
tutorial D052 → D163+D129. One CONTEXT REJECT (D075 provider page → first-party
cards + quarantine). Full text in the archived interactive input.

## 9. Former MAYBE outcomes (20)

SELECTED-SUPPORTING (7): D072 (timeline corroboration, not spec authority), D073
(community-attempt signal), D080 (prefix-hit-conditioned deployment existence),
D100 (harness-dependence exhibit), D117 (one-line early-exit bound), D119 (tooling
authority, AIPerf open), D120 (incomparability exhibit). HOLD (12): D074 D076 D079
D082 D086 D087 D097 D099 D146 D147 D152 D156 (park/watch/follow-up-pool reasons
per-candidate). INSPECT (2): D084 (harness warning), D085 (KDA collision).
REJECT (1): D075 (superseded + quarantined). No MAYBE was promoted to PRIMARY;
none was discarded without a named reason.

## 10. Former INSPECT outcomes (5)

D032 → SELECTED PRIMARY (VERIFIED, launch Raw + supplement). D093 → SELECTED
PRIMARY (identity + full text captured, section consumption outstanding as stated
boundary). D150 → SELECTED PRIMARY (VERIFIED body results + protocol). D119 →
SELECTED SUPPORTING (docs bound, AIPerf open). D077 → INSPECT retained (AI-drafted
UNEDITED derivations genuinely need inspection; not silently promoted).

## 11. Capstone assignments

- DeepSeek V4.1 Flash: D123 PRIMARY (body-consumed) + D030 PRIMARY (card) + D031
  rejected as announcement-duplicate + D004/D040/D078/D163 runtime support + D162 reception.
- Qwen3.8-Flash-Next: D008 PRIMARY (body-consumed) + D127/D029/D081 support + D165
  VERIFIED port + D080 conditioned deployment.
- Kimi Linear: D027 PRIMARY in P3 (body-consumed) + D028 PRIMARY in P8 (repo ground)
  + D132/D024 lineage support; independent reproduction limited (stated).
- GLM-5.3-Flash: D128 PRIMARY with abstract-scope boundary + D129/D130/D131 support
  + D164 bounded local + D052 rejected as tutorial-duplicate.
- No capstone lost first-party technical authority; GLM depth is mixed and labeled.

## 12. Jev assignments

D070/D071/D141 PRIMARY (VERIFIED first-party), D142/D072/D073 SUPPORTING (contract
derivation, timeline corroboration, community-attempt signal), D074 HELD as
secondary-duplicate. Vendor claims bounded; thin reproduction + unresolved public
calibration stated in P7 boundaries. Jev is a specialization case, never a
generative-LLM replacement.

## 13. X / community usage

D162 SELECTED SUPPORTING in P4+P8 ONLY as reception/deployment evidence, never
PRIMARY technical authority; configuration-bound self-reports. D073 community hub
as attempt-activity signal in P7. No headline community number is load-bearing.

## 14. Benchmark-methodology usage

P9 primaries D092 (Verified/Pro anchor), D093 (validity evolution), D094 (agentic),
D098 (long-context), D118 (measurement standard); support D119/D121/D122 (tooling/
harness/holistic), D120 (incomparability), D100 (harness dependence). Six
benchmark-definition authorities rejected with methodology-without-rank rationale;
no naked cross-condition comparison survives (validity exhibits travel with every
comparison; capstone scores cite Evidence-Card conditions).

## 15. Package-by-package primary / supporting IDs

- P1 bottleneck (order 1): PRI D001 D002 D003; SUP —.
- P2 scaling→MoE (2): PRI D006 D007 D010 D011 D012 D014 D015; SUP D013 D065 D067 D068 D101 D103 D133 D139.
- P3 attention/memory (3): PRI D018 D019 D020 D026 D027 D032 D125 D143; SUP D024 D025 D029 D056 D109 D110 D112 D113 D114 D115 D116 D117 D126 D132 D144 D145.
- P4 bits/local (4): PRI D005 D041 D042 D045 D048 D050; SUP D043 D044 D047 D049 D051 D135 D136 D162 D164 D165.
- P5 decode/TTC (5): PRI D033 D036 D038 D148 D149 D150 D151 D153; SUP D034 D035 D037 D039 D069.
- P6 serving (6): PRI D053 D055 D059 D061 D062; SUP D040 D056 D064 D065 D066 D078 D113 D114 D163.
- P7 routing/Jev (7): PRI D070 D071 D141 D154 D155 D157; SUP D072 D073 D142.
- P8 2026 stacks (8): PRI D008 D028 D030 D123 D128; SUP D004 D029 D040 D078 D080 D081 D126 D127 D129 D130 D131 D132 D162 D163 D164 D165.
- P9 measure (9): PRI D092 D093 D094 D098 D118; SUP D100 D119 D120 D121 D122.
- Selected exceptions: none (every SELECTED candidate has its required placement).

## 16. Page plan

Target 76 / max 96 (soft minimum ~64; no padding): P1 7, P2 9, P3 11, P4 9, P5 8,
P6 9, P7 7, P8 11, P9 6. Titles: P1「効率」とは何を減らすことなのか / P2 Scaling
からConditional Computeへ / P3 AttentionとMemoryを減らす / P4 Bitを減らし、巨大
モデルを手元で動かす / P5 1 tokenずつ待たない / P6 Servingで消える無駄 /
P7「大きなモデルを毎回呼ぶ」必要はあるか / P8 2026年の実装点 / P9 数字をどう読むか.
Reader-facing Japanese title: Efficient Intelligence — LLMを速く、軽く、安くする技術史.
Thesis: layered-systems evolution (training sparsity, partial activation, memory
movement, state retention, serial steps, cheapest-adequate routing, specialization);
no single technique makes a model efficient; not a model ranking.

## 17. Inherited Evidence boundaries

Every package auto-inherits per-candidate remaining_boundaries (limitations +
unresolved questions + contradictions) via the frozen runner on top of the
package-level boundaries stated in the Architecture artifact. Key inherited
classes: abstract-scope paper sections, captured-but-unconsumed repo/doc/spec
bodies, supplement-bound wrong-identity locators, 40 UNRESOLVED verification
targets, vendor-quarantine, per-figure pins open.

## 18. D128 scope correction (propagated)

Recorded in Sol Evidence Review §4, in the D128 SELECTED rationale
(`PRIMARY but abstract-scope for the material claims presently consumed`),
in P8 package boundaries (mixed GLM authority depth; never full-body-verified
language), and here. The Completeness artifact was not mutated for prose.

## 19. Known unresolved authority

Jev independent reproduction + public calibration; AIPerf product surface; F4
independent writeup; capstone ablation/per-figure pins; GLM vendor ratios;
Kimi independent reproduction; D157 summary-scope; SWE-Pro section consumption;
captured-but-unconsumed bodies; 40 UNRESOLVED targets; MiniMax/gpt-oss mechanism
contributions; KDA-label collision (D085); LM Studio harness warning (D084);
AI-drafted V4.1 study derivations (D077).

## 20. Alternative architectures considered (Sol to judge)

- A (mechanism encyclopedia): rejected — good reference shape but weak
  historical/system synthesis and excessive compartmentalization; chosen plan
  keeps mechanisms but orders them as a bottleneck-to-system narrative.
- B (2026 model-by-model spine): rejected — product-comparison risk, mechanism
  duplication, fast aging; chosen plan isolates model comparison to P8 and
  builds mechanisms first.
- C (pure bottleneck-first): rejected as sole spine — strong systems thesis but
  chronology and technology lineages get hard to follow; chosen plan combines
  chronology/mechanism packages (P2–P7) with bottleneck framing (P1 contract,
  P6/P9 payoff).

## 21. Architecture validation / readiness result

- Runner: frozen `run_selection_architecture_v2_interactive.py` → Matrix SHA
  `1dcc2902…`, Selection SHA `f91af7cf…`, Architecture SHA `e214040b…`,
  Review Summary SHA `bc4a40d8…` (READY_FOR_ARCHITECTURE_REVIEW, zero errors),
  Review Attention SHA `970c3231…`.
- Selection checkpoint: `orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json`
  (SHA `f0255d39…`); Architecture checkpoint:
  `orchestration/v2/checkpoints/SELECTION_COMPLETE.json` (SHA `6f5f3fa1…`).
- Lifecycle `ARCHITECTURE_ESTABLISHED`; next_action `ARCHITECTURE_REVIEW`;
  Architecture Review pending, Publication Preview pending, no approval
  provenance; drafting not started; Architecture status PROPOSED with null
  human_review.

## 22. Why the Human should or should not hesitate (operator view; Sol decides)

Hesitate-less: full 160-candidate coverage with explicit non-generic rationale;
all mandatory lanes retain substantive first-party authority; boundaries
(D128, X, Unsloth, Jev, benchmark conditions) are structural, not footnotes;
deterministic validation is clean. Hesitate-more: 148 PARTIAL means most paper
claims rest on abstract-scope plus bounded body consumption; GLM depth is
visibly mixed; Jev specialization claims await independent reproduction; three
records sit in INSPECT and twelve in HOLD by design. Sol's independent review
of this package — not this package itself — is the basis for any Gate
recommendation.

## Appendix — negative-space audit (operator, pre-stop)

Checked programmatically against Matrix/Selection bytes: (a) no primary body is
used more richly elsewhere than its selected placement claims; (b) every
unselected MATERIAL candidate names its superseding selected source or the
unnecessary editorial role; (c) no vague cluster rejection (only two uses of
`redundant`, both post-naming summaries); (d) every mandatory lane holds PRIMARY
first-party authority (no secondary-only lane); (e) all four capstones plus Jev
retain first-party technical authority; (f) benchmark validity exhibits are
selected while no naked benchmark number is. No structurally serious case found;
no Selection/Architecture repair required before stopping. HOLD/INSPECT items
are intentional deferrals/inspections for Sol, not hidden gaps.
