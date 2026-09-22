# Screening Review Package r2 — SP-efficient-llm-2026 (CORRECTED / SUPERSEDES_R1_FOR_SOL_REVIEW)

Status: `CORRECTED / SUPERSEDES_R1_FOR_SOL_REVIEW`
Machine lifecycle: `CANDIDATES_NORMALIZED` (next `stage:evidence-materiality-completeness`, NOT entered)
Operator: Muse (Luna/Work execution role) under the Core v2 screening contract. Sol screening PASS recorded separately; Selection NOT authorized.

## 0. Correction scope

- Package r1 (`execution/reviews/screening-review-package-r1.md`, SHA `7f9ea672ab8e32825a7cd175ab4b32d0856bd13a496ceef45a4bfd11a9cfc4bf`) is preserved untouched as historical machine/operator output.
- This r2 corrects r1's factual summary errors. It does NOT regenerate, alter, or re-decide canonical Screening acceptance.
- All counts below were recomputed mechanically from the exact canonical bytes named in §1 (not hand-copied from r1 or from any supplied table). The supplied correction tables were used only as cross-check expectations; recomputation confirmed them exactly (see §13).

## 1. Canonical sources and provenance

- Canonical Discovery: `sources/SP-efficient-llm-2026/discovery/discovery-v2.jsonl` — 165 records (`EFF-D001–EFF-D165`), SHA-256 `7074cef2bfc3b2dd034addbd778055bc2fed962e9845c756f32f9b3c848199d3`.
- Canonical Screening acceptance: `sources/SP-efficient-llm-2026/screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json` — `record_count` 165, DIRECT basis, SHA-256 `65330476ff975c49fb4510f56d27942ec2b334b8ceed8a66b00639c659ec24fe`.
- Decision key in acceptance bytes: `decision` ∈ {KEEP, MAYBE, INSPECT, DROP}, keyed by `discovery_id`.
- Source class in Discovery bytes: `source.source_type`. Obligation binding in Discovery bytes: `provenance.obligation_ids`.
- Stage checkpoint: `sources/SP-efficient-llm-2026/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json` (SHA `3914fd8711c3766615342686735c0516bf5a0469fb5ec455fb08100e144f63e3`), `DISCOVERY_COLLECTED` → `CANDIDATES_NORMALIZED`.
- Production State: `sources/SP-efficient-llm-2026/production-state.json` (SHA `5b5f351762e183ea0aa4830d0f1a2b895d27aed6b71923bad78195f1be4dd7ae`), lifecycle `CANDIDATES_NORMALIZED`, screening passed, evidence/materiality/completeness/selection pending.

## 2. Screening input count

165 (DIRECT basis against the complete canonical Discovery; 165 effective records).

## 3. Exact disposition counts (recomputed)

- KEEP: 135
- MAYBE: 20
- INSPECT: 5
- DROP: 5
- non-DROP total: 160 / 165
- No compression trigger: 160 non-DROP records retain full breadth for this comprehensive Thematic.

## 4. KEEP records (135)

EFF-D001 EFF-D002 EFF-D003 EFF-D004 EFF-D005 EFF-D006 EFF-D007 EFF-D008 EFF-D009 EFF-D010 EFF-D011 EFF-D012 EFF-D013 EFF-D014 EFF-D015 EFF-D016 EFF-D017 EFF-D018 EFF-D019 EFF-D020 EFF-D021 EFF-D022 EFF-D023 EFF-D024 EFF-D025 EFF-D026 EFF-D027 EFF-D028 EFF-D029 EFF-D030 EFF-D031 EFF-D033 EFF-D034 EFF-D035 EFF-D036 EFF-D037 EFF-D038 EFF-D039 EFF-D040 EFF-D041 EFF-D042 EFF-D043 EFF-D044 EFF-D045 EFF-D046 EFF-D047 EFF-D048 EFF-D049 EFF-D050 EFF-D051 EFF-D052 EFF-D053 EFF-D054 EFF-D055 EFF-D056 EFF-D057 EFF-D058 EFF-D059 EFF-D060 EFF-D061 EFF-D062 EFF-D063 EFF-D064 EFF-D065 EFF-D066 EFF-D067 EFF-D068 EFF-D069 EFF-D070 EFF-D071 EFF-D073 EFF-D078 EFF-D081 EFF-D083 EFF-D088 EFF-D089 EFF-D090 EFF-D091 EFF-D092 EFF-D094 EFF-D095 EFF-D096 EFF-D098 EFF-D101 EFF-D102 EFF-D103 EFF-D104 EFF-D105 EFF-D106 EFF-D107 EFF-D108 EFF-D109 EFF-D110 EFF-D111 EFF-D112 EFF-D113 EFF-D114 EFF-D115 EFF-D116 EFF-D118 EFF-D121 EFF-D122 EFF-D123 EFF-D124 EFF-D125 EFF-D126 EFF-D127 EFF-D128 EFF-D129 EFF-D130 EFF-D131 EFF-D132 EFF-D133 EFF-D134 EFF-D135 EFF-D136 EFF-D137 EFF-D138 EFF-D139 EFF-D141 EFF-D142 EFF-D143 EFF-D144 EFF-D145 EFF-D148 EFF-D149 EFF-D151 EFF-D153 EFF-D154 EFF-D155 EFF-D157 EFF-D162 EFF-D163 EFF-D164 EFF-D165

## 5. MAYBE records (20)

EFF-D072 (Jev wiki snapshot, corroboration only) EFF-D074 (DataCamp Jev explainer, secondary) EFF-D075 (Lambda provider page) EFF-D076 (DeepInfra price sample) EFF-D079 (llm-stats Qwen analysis) EFF-D080 (NVIDIA GB300 blog, condition-bound) EFF-D082 (llm-stats GLM analysis) EFF-D084 (LM Studio GLM page) EFF-D085 (NIM GLM card, KDA collision) EFF-D086 (MiniMax watch) EFF-D087 (gpt-oss watch) EFF-D097 (BrowseComp, harness outstanding) EFF-D099 (AIME/MAA, conditions outstanding) EFF-D100 (DeepSWE harness note) EFF-D117 (DeeBERT minimal precedent) EFF-D120 (LLMPerf caveat exhibit) EFF-D146 (kNN-LM boundary precedent) EFF-D147 (RETRO boundary precedent) EFF-D152 (TTC survey, secondary) EFF-D156 (routing survey, secondary)

## 6. INSPECT records (5)

- EFF-D032 — DSA trace, homepage-only locator; isolate a dedicated first-party announcement/report/model-card URL.
- EFF-D077 — AI-drafted UNEDITED V4.1 parameter-accounting study; verify derivations against official report/config authority.
- EFF-D093 — SWE-bench-Pro; resolve exact benchmark/paper identity, Pro variant/version, harness conditions.
- EFF-D119 — GenAI-Perf / AIPerf identity; consume actual NVIDIA/Triton tooling authority; `AIPerf NOT_FOUND` preserved where applicable.
- EFF-D150 — ThinkPrune; read primary paper body (mechanism, policy-vs-heuristic, conditions, token/quality tradeoff).

## 7. DROP records (5)

- EFF-D140 — Textbooks Are All You Need (phi data-quality line; indirect capability-per-token context).
- EFF-D158 — Mixture-of-Agents (collaboration/model-pool boundary probe, not routing/cascading mechanism).
- EFF-D159 — DistilBERT (historical bridge; decoder/reasoning distillation history preserved via Hinton + current authorities).
- EFF-D160 — MiniLM (historical bridge; same rationale as D159).
- EFF-D161 — Wanda (pruning metric, not the pruning+recovery/deployment path; SparseGPT retained).

## 8. Dropped primary authorities (CORRECTED — r1 §8 was false)

r1 §8 stated `Dropped primary authorities: None` and characterized all five DROPs as secondary/bridge records. That is factually wrong.

Recomputed result: **5 dropped PRIMARY_PAPER records** — EFF-D140, EFF-D158, EFF-D159, EFF-D160, EFF-D161 (titles in §7; source-class evidence in §9).

No PRIMARY_DOC, PRIMARY_REPO, PRIMARY_ANNOUNCEMENT, PRIMARY_MODEL_CARD, or PRIMARY_SPEC record was dropped (all DROP dispositions are PRIMARY_PAPER; see §9).

Sol verdict (recorded separately) accepts these five DROP decisions as editorially acceptable under the current scope; they are not restored merely for being primary papers.

## 9. Source-class by disposition (CORRECTED — recomputed from canonical bytes)

| Source class | KEEP | MAYBE | INSPECT | DROP | Total |
|---|---:|---:|---:|---:|---:|
| PRIMARY_PAPER | 85 | 5 | 2 | 5 | 97 |
| PRIMARY_DOC | 13 | 0 | 0 | 0 | 13 |
| PRIMARY_REPO | 19 | 1 | 1 | 0 | 21 |
| PRIMARY_ANNOUNCEMENT | 5 | 2 | 1 | 0 | 8 |
| PRIMARY_MODEL_CARD | 5 | 1 | 0 | 0 | 6 |
| PRIMARY_SPEC | 3 | 1 | 0 | 0 | 4 |
| SECONDARY_REFERENCE | 1 | 7 | 0 | 0 | 8 |
| SECONDARY_TECHNICAL | 0 | 3 | 1 | 0 | 4 |
| x-community-signal | 1 | 0 | 0 | 0 | 1 |
| RUNTIME_RECIPE | 1 | 0 | 0 | 0 | 1 |
| PACKAGING_DOCS | 1 | 0 | 0 | 0 | 1 |
| RUNTIME_PR | 1 | 0 | 0 | 0 | 1 |
| **Total** | **135** | **20** | **5** | **5** | **165** |

ID-level detail (recomputed):

- PRIMARY_PAPER KEEP (85): EFF-D001 EFF-D002 EFF-D003 EFF-D005 EFF-D006 EFF-D008 EFF-D010 EFF-D011 EFF-D012 EFF-D013 EFF-D014 EFF-D015 EFF-D016 EFF-D018 EFF-D019 EFF-D020 EFF-D021 EFF-D022 EFF-D023 EFF-D024 EFF-D025 EFF-D026 EFF-D027 EFF-D033 EFF-D034 EFF-D035 EFF-D036 EFF-D037 EFF-D038 EFF-D041 EFF-D042 EFF-D043 EFF-D044 EFF-D045 EFF-D046 EFF-D047 EFF-D053 EFF-D055 EFF-D057 EFF-D059 EFF-D060 EFF-D061 EFF-D062 EFF-D067 EFF-D068 EFF-D069 EFF-D088 EFF-D089 EFF-D090 EFF-D091 EFF-D092 EFF-D094 EFF-D096 EFF-D098 EFF-D101 EFF-D102 EFF-D103 EFF-D104 EFF-D105 EFF-D106 EFF-D107 EFF-D108 EFF-D109 EFF-D110 EFF-D111 EFF-D112 EFF-D115 EFF-D116 EFF-D123 EFF-D124 EFF-D125 EFF-D128 EFF-D133 EFF-D134 EFF-D135 EFF-D137 EFF-D138 EFF-D139 EFF-D143 EFF-D148 EFF-D149 EFF-D151 EFF-D154 EFF-D155 EFF-D157
- PRIMARY_PAPER MAYBE (5): EFF-D117 EFF-D146 EFF-D147 EFF-D152 EFF-D156
- PRIMARY_PAPER INSPECT (2): EFF-D093 EFF-D150
- PRIMARY_PAPER DROP (5): EFF-D140 EFF-D158 EFF-D159 EFF-D160 EFF-D161
- PRIMARY_DOC KEEP (13): EFF-D004 EFF-D039 EFF-D040 EFF-D049 EFF-D052 EFF-D063 EFF-D071 EFF-D078 EFF-D083 EFF-D113 EFF-D131 EFF-D141 EFF-D142
- PRIMARY_REPO KEEP (19): EFF-D007 EFF-D028 EFF-D050 EFF-D051 EFF-D054 EFF-D056 EFF-D058 EFF-D064 EFF-D065 EFF-D066 EFF-D095 EFF-D114 EFF-D121 EFF-D122 EFF-D127 EFF-D129 EFF-D132 EFF-D144 EFF-D145
- PRIMARY_REPO MAYBE (1): EFF-D120
- PRIMARY_REPO INSPECT (1): EFF-D119
- PRIMARY_ANNOUNCEMENT KEEP (5): EFF-D009 EFF-D031 EFF-D070 EFF-D081 EFF-D126
- PRIMARY_ANNOUNCEMENT MAYBE (2): EFF-D087 EFF-D097
- PRIMARY_ANNOUNCEMENT INSPECT (1): EFF-D032
- PRIMARY_MODEL_CARD KEEP (5): EFF-D017 EFF-D029 EFF-D030 EFF-D130 EFF-D153
- PRIMARY_MODEL_CARD MAYBE (1): EFF-D100
- PRIMARY_SPEC KEEP (3): EFF-D048 EFF-D118 EFF-D136
- PRIMARY_SPEC MAYBE (1): EFF-D099
- SECONDARY_REFERENCE KEEP (1): EFF-D073
- SECONDARY_REFERENCE MAYBE (7): EFF-D072 EFF-D074 EFF-D075 EFF-D076 EFF-D084 EFF-D085 EFF-D086
- SECONDARY_TECHNICAL MAYBE (3): EFF-D079 EFF-D080 EFF-D082
- SECONDARY_TECHNICAL INSPECT (1): EFF-D077
- x-community-signal KEEP (1): EFF-D162
- RUNTIME_RECIPE KEEP (1): EFF-D163
- PACKAGING_DOCS KEEP (1): EFF-D164
- RUNTIME_PR KEEP (1): EFF-D165

## 10. Obligation coverage (CORRECTED — recomputed from canonical bytes; r1 §12 non-DROP tallies were wrong)

| Obligation | KEEP | MAYBE | INSPECT | DROP | Total |
|---|---:|---:|---:|---:|---:|
| EFF-O01 | 4 | 0 | 0 | 0 | 4 |
| EFF-O02 | 19 | 0 | 0 | 1 | 20 |
| EFF-O03 | 15 | 2 | 0 | 0 | 17 |
| EFF-O04 | 31 | 1 | 2 | 0 | 34 |
| EFF-O05 | 15 | 0 | 0 | 0 | 15 |
| EFF-O06 | 21 | 0 | 0 | 0 | 21 |
| EFF-O07 | 7 | 0 | 0 | 0 | 7 |
| EFF-O08 | 30 | 2 | 0 | 0 | 32 |
| EFF-O09 | 5 | 0 | 0 | 3 | 8 |
| EFF-O10 | 6 | 2 | 0 | 0 | 8 |
| EFF-O11 | 32 | 9 | 2 | 0 | 43 |
| EFF-O12 | 14 | 7 | 2 | 0 | 23 |
| EFF-O13 | 3 | 2 | 0 | 0 | 5 |
| EFF-O14 | 4 | 1 | 1 | 0 | 6 |
| EFF-O15 | 3 | 1 | 0 | 1 | 5 |

ID-level detail (recomputed):

- EFF-O01 KEEP: EFF-D001 EFF-D002 EFF-D003 EFF-D004
- EFF-O02 KEEP (19): EFF-D001 EFF-D002 EFF-D005 EFF-D006 EFF-D007 EFF-D008 EFF-D009 EFF-D038 EFF-D065 EFF-D101 EFF-D102 EFF-D103 EFF-D104 EFF-D105 EFF-D106 EFF-D107 EFF-D108 EFF-D138 EFF-D139; DROP (1): EFF-D140
- EFF-O03 KEEP (15): EFF-D010 EFF-D011 EFF-D012 EFF-D013 EFF-D014 EFF-D015 EFF-D016 EFF-D017 EFF-D051 EFF-D064 EFF-D115 EFF-D116 EFF-D124 EFF-D133 EFF-D134; MAYBE (2): EFF-D075 EFF-D117
- EFF-O04 KEEP (31): EFF-D008 EFF-D009 EFF-D015 EFF-D018 EFF-D019 EFF-D020 EFF-D021 EFF-D022 EFF-D023 EFF-D024 EFF-D025 EFF-D026 EFF-D027 EFF-D028 EFF-D029 EFF-D030 EFF-D031 EFF-D063 EFF-D083 EFF-D109 EFF-D110 EFF-D111 EFF-D112 EFF-D114 EFF-D123 EFF-D124 EFF-D125 EFF-D127 EFF-D128 EFF-D132 EFF-D165; MAYBE (1): EFF-D080; INSPECT (2): EFF-D032 EFF-D077
- EFF-O05 KEEP (15): EFF-D006 EFF-D030 EFF-D033 EFF-D034 EFF-D035 EFF-D036 EFF-D037 EFF-D038 EFF-D039 EFF-D040 EFF-D063 EFF-D116 EFF-D123 EFF-D129 EFF-D163
- EFF-O06 KEEP (21): EFF-D005 EFF-D017 EFF-D030 EFF-D041 EFF-D042 EFF-D043 EFF-D044 EFF-D045 EFF-D046 EFF-D047 EFF-D048 EFF-D049 EFF-D050 EFF-D063 EFF-D065 EFF-D123 EFF-D124 EFF-D135 EFF-D136 EFF-D137 EFF-D164
- EFF-O07 KEEP (7): EFF-D048 EFF-D050 EFF-D051 EFF-D052 EFF-D162 EFF-D164 EFF-D165
- EFF-O08 KEEP (30): EFF-D003 EFF-D004 EFF-D028 EFF-D039 EFF-D052 EFF-D053 EFF-D054 EFF-D055 EFF-D056 EFF-D057 EFF-D058 EFF-D059 EFF-D060 EFF-D061 EFF-D062 EFF-D063 EFF-D064 EFF-D065 EFF-D066 EFF-D078 EFF-D109 EFF-D110 EFF-D111 EFF-D112 EFF-D113 EFF-D114 EFF-D132 EFF-D134 EFF-D162 EFF-D163; MAYBE (2): EFF-D075 EFF-D080
- EFF-O09 KEEP (5): EFF-D045 EFF-D046 EFF-D067 EFF-D068 EFF-D069; DROP (3): EFF-D159 EFF-D160 EFF-D161
- EFF-O10 KEEP (6): EFF-D070 EFF-D071 EFF-D073 EFF-D141 EFF-D142 EFF-D162; MAYBE (2): EFF-D072 EFF-D074
- EFF-O11: see §11. EFF-O12: see §11.
- EFF-O13 KEEP (3): EFF-D143 EFF-D144 EFF-D145; MAYBE (2): EFF-D146 EFF-D147
- EFF-O14 KEEP (4): EFF-D148 EFF-D149 EFF-D151 EFF-D153; MAYBE (1): EFF-D152; INSPECT (1): EFF-D150
- EFF-O15 KEEP (3): EFF-D154 EFF-D155 EFF-D157; MAYBE (1): EFF-D156; DROP (1): EFF-D158

Every obligation retains KEEP core; no supervisory lane is wiped. DROP-affected obligations retain material coverage: O02 via 19 KEEP (Dedup/DoReMi data-efficiency lane), O09 via Hinton + reasoning-distillation authorities, O15 via FrugalGPT/RouteLLM/survey/fragility.

## 11. O11 / O12 correction (r1 §9 breakdown was wrong; non-DROP total was right)

- EFF-O11 total 43, all non-DROP. Corrected breakdown: KEEP 32 / MAYBE 9 / INSPECT 2 / DROP 0.
  - KEEP (32): EFF-D004 EFF-D008 EFF-D017 EFF-D027 EFF-D028 EFF-D029 EFF-D030 EFF-D031 EFF-D040 EFF-D049 EFF-D052 EFF-D063 EFF-D069 EFF-D078 EFF-D081 EFF-D083 EFF-D123 EFF-D124 EFF-D125 EFF-D126 EFF-D127 EFF-D128 EFF-D129 EFF-D130 EFF-D131 EFF-D132 EFF-D145 EFF-D153 EFF-D162 EFF-D163 EFF-D164 EFF-D165
  - MAYBE (9): EFF-D075 EFF-D076 EFF-D079 EFF-D080 EFF-D082 EFF-D084 EFF-D085 EFF-D086 EFF-D087
  - INSPECT (2): EFF-D032 EFF-D077
  - r1 §9 claimed `38 KEEP, 5 MAYBE` followed by a 10-ID MAYBE list (D075 D076 D079 D080 D082 D084 D085 D086 D087 D100) that also wrongly included EFF-D100 (a PRIMARY_MODEL_CARD MAYBE bound to EFF-O12, not EFF-O11). All three claims are superseded by the recomputed values above.
- EFF-O12 total 23, all non-DROP. Corrected breakdown: KEEP 14 / MAYBE 7 / INSPECT 2 / DROP 0.
  - KEEP (14): EFF-D088 EFF-D089 EFF-D090 EFF-D091 EFF-D092 EFF-D094 EFF-D095 EFF-D096 EFF-D098 EFF-D118 EFF-D121 EFF-D122 EFF-D127 EFF-D162
  - MAYBE (7): EFF-D079 EFF-D082 EFF-D084 EFF-D097 EFF-D099 EFF-D100 EFF-D120
  - INSPECT (2): EFF-D093 EFF-D119

## 12. X/community and F1–F4 dispositions (unchanged substance, restated on corrected base)

- EFF-D162 (x-community-signal, X_OBSERVATION): KEEP. Reception/deployment/friction signal only; never spec authority. Self-reported measurements remain configuration-bound observations.
- EFF-D163 (RUNTIME_RECIPE, vLLM DeepSeek V4.1 recipe): KEEP.
- EFF-D164 (PACKAGING_DOCS, Unsloth GLM-5.3-Flash): KEEP.
- EFF-D165 (RUNTIME_PR, llama.cpp Qwen implementation PR): KEEP.
- F4 Jev independent writeup: `INDEPENDENT_WRITEUP_NOT_RESOLVED`, no Discovery record.
- Duplicate groups recorded, not merged: `dynamo-v41-recipe-readings` (D004+D063), `hf-v41-card-readings` (D030+D153), `hf-qwen-card-readings` (D029+D100) — same-locator distinct analytical roles; Sol may direct merge or keep.

## 13. Recomputation method and cross-check

Method (executed 2026-09-22, work branch `special/efficient-llm-2026-work`, HEAD `bece7052f8da9a5fb21bb09726f6f0cb7e0075e5`):

1. Loaded all 165 lines of `discovery-v2.jsonl`; keyed by `discovery_id`.
2. Loaded `screening-accepted.json` (`record_count` 165); keyed `decision` by `discovery_id`.
3. Joined on `discovery_id`; tabulated `source.source_type` × `decision` and `provenance.obligation_ids` × `decision`.
4. Result matched the supplied correction tables cell-for-cell (§9: all 12 classes; §10: all 15 obligations), so r2 reports those values as the actual recomputed values — nothing was forced.

## 14. Validator / checkpoint results (unchanged, restated)

- Interactive runner acceptance: `screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json` (SHA `65330476ff975c49fb4510f56d27942ec2b334b8ceed8a66b00639c659ec24fe`), record_count 165, DIRECT basis.
- Stage validation: `execution/x-completion/validation/screening-stage-validation-r1.json` (CORE_STAGE_CONTRACT PASS).
- Stage checkpoint: `orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json` (SHA `3914fd8711c3766615342686735c0516bf5a0469fb5ec455fb08100e144f63e3`), `DISCOVERY_COLLECTED` → `CANDIDATES_NORMALIZED`.
- Production State: SHA `5b5f351762e183ea0aa4830d0f1a2b895d27aed6b71923bad78195f1be4dd7ae`, lifecycle `CANDIDATES_NORMALIZED`, screening passed, evidence/materiality/completeness/selection/architecture pending.

## 15. r1 defect ledger (for the record)

1. r1 §8: `Dropped primary authorities: None` — false. Actual: 5 dropped PRIMARY_PAPER records (§7–§8).
2. r1 §8 sub-claim: DROPs are secondary/bridge records — false. All five DROPs are PRIMARY_PAPER.
3. r1 §9: O11 breakdown `38 KEEP / 5 MAYBE` — false. Actual: 32 / 9 / 2 / 0 (§11). The trailing 10-ID list also mis-includes EFF-D100.
4. r1 §11: `16 records bound; 15 non-DROP` for O13/O14/O15 combined — true as far as it goes, but stated without the per-obligation KEEP/MAYBE/INSPECT/DROP split now given in §10.
5. r1 §12: per-obligation non-DROP tallies (e.g. O02 14/15, O04 24/24, O05 11/11, O06 13/13, O08 22/22) undercount the recomputed totals — superseded by §10.

Substance preserved from r1: disposition totals (135/20/5/5), KEEP/MAYBE/INSPECT/DROP ID lists, X boundary, duplicate-group note, compression-trigger assessment (none), validator/checkpoint references.

## 16. Sol review readiness

- Sol Screening review: `PASS / PROCEED_TO_EVIDENCE` recorded in `execution/reviews/sol-screening-review-pass-20260922.md` (Reviewer: Sol / GPT-5.6). Screening acceptance itself is not regenerated.
- Evidence (`stage:evidence-materiality-completeness`) is authorized. Selection is NOT authorized.
