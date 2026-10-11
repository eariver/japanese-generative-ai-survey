# Sol W40 Evidence Authority-Consumption Review r1 — REVISION_REQUIRED

Status: `SOL_EVIDENCE_AUTHORITY_REVISION_REQUIRED / CORE_ACCEPTANCE_BLOCKED`  
Date: `2026-10-10 JST`  
Repository: `eariver/japanese-generative-ai-survey`  
Existing branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r4 HEAD: `e81ab6e461ff0e58bd62c590a532a78ca80a7057`  
Reviewed Muse r4 Tree: `db7423d2b17947fd56a0af9455153f27ac33eb13`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Edition: `2026-W40`; ordinary UTC window `[2026-09-25T22:00:00Z,2026-10-02T22:00:00Z)`

## 1. Git and Core state admission — PASS

- Exact prior Starting HEAD `dcd5df29057d6097ea5c9a7aefd7e551c49d8d4b`; Muse final HEAD above is direct first-child commit; no diverged history or force push.
- 103 changed files, all `sources/2026-W40/**`; reviewed `main` unchanged, no shared scripts/config/schemas/Human Gate modifications.
- Discovery Acceptance 37; official Core checkpoint `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` passed; Screening Acceptance 37 (31 KEEP / 3 INSPECT / 1 MAYBE / 2 DROP); official Core checkpoint `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` passed.
- Canonical Production State: `CANDIDATES_NORMALIZED`, next `stage:evidence-materiality-completeness`; discovery/screening passed, evidence/materiality/completeness pending, both Human Gates pending.
- Muse produced 35 task files, 35 **reviewer-input** `interactive-evidence.json` records (28 VERIFIED / 7 PARTIAL), 35 draft Edition Views; importantly these are **not** formal Evidence Cards/Acceptance nor actual Stage `EVIDENCE_REVIEWED`. The reported runner check used `task_source_ids=None` and bypassed failing source-class binding, so do NOT call 35/35 a full Core Evidence authority PASS.
- Muse correctly stopped at `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` without Selection/Architecture/Human action.

## 2. Blocking findings

### SC-E01 — Evidence source taxonomy fails after accepted Discovery/Screening [CORE BLOCKER: recurrence CV2-DM-016]

Independent read of reviewed `scripts/survey_evidence_v2.py` confirms `SOURCE_CLASS_MAP` does not contain **`PRIMARY_RESEARCH_ABSTRACT`** and **`EVALUATOR_PUBLISHER`**. `task_authority_sources()` calls `_source_class()` and fail-closes:

- `w40-primary-contextlms-20260929` and `w40-prewindow-lift-20260925`: `PRIMARY_RESEARCH_ABSTRACT` -> unsupported;
- `w40-primary-aa-agentperf-20260929`: `EVALUATOR_PUBLISHER` -> unsupported.

The reviewed `schemas/survey-discovery-record.schema.json` requires a nonempty `source_type` string but has no Evidence taxonomy enum; valid Discovery/Screening can therefore admit types Evidence later rejects. This is **a concrete W40 recurrence** of existing generic `CV2-DM-016` (`docs/core-v2-deferred-maintenance-summary.md`), not a new defect needing a duplicate maintenance ID.

The prepared 35-record reviewer input does not satisfy canonical task-source binding. Evidence Acceptance and downstream stages are BLOCKED. **Shared Core is frozen: do not patch it in W40.** The existing DM-016 catalog describes a narrow edition-local task-source type projection as a possible remedy; before applying it to new W40 types, validate exact semantic mappings and preserve source-class and SHA lineage, with prior Sol review. Under r5 this is *compatibility PROPOSAL and deterministic preflight only*, not authority to proclaim Evidence Accepted.

### SC-E02 — ELYZA available primary benchmark and training body left unconsumed [CONTENT BLOCKER]

Current r4 reviewer evidence for `w40-weak-elyza-20261002` says `NO eval/benchmark content consumed`, status PARTIAL + HOLD solely for missing evaluation/merit, even though primary initial-release Hugging Face model cards **contain `Average performance` and `Benchmark Results` sections**, plus 3-phase mid-training/SFT/RLVR methodology and Japanese-specific task/data construction.

Primary launch-revision references:

- Dense 33B initial model repo commit: `https://huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-33b/commit/6ca556b2ddc4642580752b3a1ae2d7e7681106fc` (README includes `Benchmark Results`);
- MoE 32B-A3B model: `https://huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-32b-a3b` (initial SHA `5260ecc249f32ef5005ef940c78f41f130d9c468`, cited in r4 delegation log).

This matters for a **Japanese Generative AI Survey**: both models are eligible Oct-2 in-window, Japanese reasoning/knowledge and tool calls are material technical claims; do not exclude merely because Muse did not open a clearly available table. Retrieval of pinned original model cards and evaluation table is required. Separately assess claimed improvements/baselines/conditions; no independent reproduction is implied. The screening MAYBE can remain historically immutable while draft Evidence materiality HOLD must be reconsidered after consumption, with a true reason if still not selected.

### SC-E03 — Context Language Models PDF verification target mislabeled [PROVENANCE BLOCKER]

`w40-primary-contextlms-20260929` in `interactive-evidence.json` contains `verification=[VERIFIED:arxiv-2609-37725-pdf]` but also explicitly says **only the abstract has been consumed** and full PDF code/configs not read. The arXiv submission date and abstract are valid sources for a *bounded abstract-backed author claim*, but that is **not PDF consumption**. For MATERIAL research subject, read the actual original paper/PDF (when available) and extract methods, experimental baselines, cache-reuse conditions, limitations, otherwise change verification target to `arxiv-abs-only` and keep full-paper inference unresolved with defensible materiality limits. Do not leave `pdf VERIFIED` while PDF unread.

## 3. Additional semantic corrections

### SC-E04 — Gemini 4 Argon 1M output-token claim source precision [TARGETED CORRECTION]

Google's original Sep-30 announcement `https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/` explicitly states **expanding the model's OUTPUT token limit to 1M from 64K**. W40 r4 record repeats the broad `1 million token limit` and then says source is too ambiguous to state the output limit without separate model docs. This is overly conservative and inaccurately describes the publisher's actual specific claim. Correct to `GOOGLE-ANNOUNCED 1M OUTPUT TOKEN LIMIT` with explicit publisher attribution and model/version/rollout qualifiers. Leave separate API availability/context constraints unresolved until docs examined.

### SC-E05 — High-signal original reports/cards not substantively consumed [REVIEW DEPTH]

Muse transparently lists code/reports/systems cards as `AUTHORITY_CAPTURED_BUT_UNCONSUMED`. This taxonomy is good; however source-rich *material* candidates such as Olmo-core 3 (direct linked technical report and repository), ProvenanceGuard (original arXiv paper 2606.18037), and potentially Open TTS Leaderboard (evaluation scripts) require a bounded second original-authority pass before claiming deep technical method/evaluation sufficiency. Prioritize **Olmo-core 3 technical report** and **ProvenanceGuard original paper** because important specific vendor/paper numbers are already included. Record exact methods, ablations, limitations and attribution. TTS evaluation code reproduction can remain a disclosed limitation unless a specific claim depends on it. Avoid unlimited research demand; focus the high-impact gaps.

### SC-E06 — Unsupported formal PASS inference [NONBLOCKING if corrected]

The 35 reviewer-input objects are not canonical Core Evidence Cards. Task/source map failed; validation occurred with task-source binding disabled. A report saying simply `Evidence 35/35 PASS` would be misleading. Mark `STRUCTURAL_REVIEW_INPUT_PASS / FORMAL_CORE_EVIDENCE_BLOCKED`. Preserve draft status and source provenance. No direct Story Selection/Architecture authority follows from 28 `MATERIAL` annotations. Note independently confirmed AMD original newsroom **does** explicitly state all-stock ~$8.2B; r4 correctly attributes it to AMD but does not independently validate transaction close; do not remove this properly attributed vendor figure.

## 4. What passed vs what remains

**PASS**: Source Intake / Sol Discovery Completeness (prior r3), 37 Discovery canonical, 37 Screening canonical, 35 draft evidence-record coverage, honest vendor-only benchmark attribution overall, W39 rumor HOLD, pre-window LIFT, X/Grok cohort separation, no Core/Gate edits. Some delegated-source verification still requires Sol/issuer pin readback and cannot be upgraded to independently reproduced methods.

**BLOCKING**: source-type taxonomy + unsafe full Card acceptance path (E01); accessible ELYZA benchmark/body omitted (E02); context-paper PDF verification mislabel (E03). **CORRECTIVE**: Gemini output-specific wording (E04), two targeted paper/report consumption tasks (E05).

**Decision**: `SOL_EVIDENCE_AUTHORITY_REVISION_REQUIRED`, `CORE_ACCEPTANCE_BLOCKED`; **NO** `EVIDENCE_REVIEWED`, Materiality/Completeness checkpoint, Selection/Architecture/Human gate. Request Muse r5 bounded repair/review; shared Core DM-016 stays OPEN and the W40 reproduction must be appended to the deferred inventory **at W40 edition closure** according to `docs/core-v2-deferred-maintenance-summary.md` section 2, and can be noted in tracking Issue #515 now.
