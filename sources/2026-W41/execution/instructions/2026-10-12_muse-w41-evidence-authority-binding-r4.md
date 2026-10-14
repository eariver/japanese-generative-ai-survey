# J-GAS W41 Muse r4 — Evidence Authority Binding and Frozen-Core Compatibility

Status: `EXECUTION_AUTHORITY / SOL_EVIDENCE_R1_PARTIAL_PASS / EDITION_LOCAL_PREACCEPTANCE_ONLY / NO_CORE_CHANGES`
Date: 2026-10-12 JST
Repository: `eariver/japanese-generative-ai-survey`
Only existing branch: `weekly/2026-W41-v2-work`

## 0. Exact starting gate

Invoker supplies exact remote HEAD and Tree of this instruction commit. Before any write, read-only assert:
- remote W41 branch SHA/Tree match invoker values; this instruction commit's parent == `a43a497c7399488fdd3b71fc14f4b739ad30c4d8` (Sol Evidence r1 Review);
- reviewed Muse r3 HEAD `fa7f7a5b091e5edea539b1ea91728b53f4656279` and Tree `1395dfae6277416d000920f646530aebc5e22266` are ancestors of invocation;
- remote main HEAD `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`;
- `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- W41 State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`, discovery and screening PASSED, evidence/materiality/completeness PENDING; both Human Gates PENDING;
- existing accepted Discovery=37 and Screening=37, r1 Evidence=36 PROVISIONAL/NOT_ACCEPTED; no conflicting worker commits or unowned dirty modifications.

Any mismatch: report exact expected/actual, **ZERO WRITES**. No branch creation, force/reset/rebase/rewrite, shared Core/scripts/config/schema/CI change, W40/main mutation, or Human gate operation.

## 1. Governing Sol authority

Read FULL `sources/2026-W41/execution/reviews/sol-w41-evidence-authority-consumption-r1-20261012.md` (SC-E41-01 through -04). Read W41 r3 handoff, Core `scripts/survey_evidence_v2.py`, `schemas/evidence-authority-supplement-v2.schema.json`, Evidence Card/Task/package validators, r1 collector bundles and complete 36 results.

W40 reviewed **precedent only**:
- `sources/2026-W40/execution/defects/w40-core-evidence-sourcemap-20261010.md`;
- `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-evidence-supplement-card-binding-r6.md`;
- `sources/2026-W40/execution/reviews/sol-w40-evidence-authority-consumption-r4-20261010.md` (derived tasks and original-source supplements, no shared Core change).

## 2. Source-class compatibility proof BEFORE large-scale card work

A. Reproduce unmodified frozen Core `survey_evidence_v2.task_authority_sources` failures on the nine r1 `SECONDARY_OBSERVATION` tasks and list exact task IDs/error strings. Inspect actual package validator for semantic provenance, not just JSON Schema.
B. Propose a narrow W41-only derived Evidence Task `source_records[0].source_type: SECONDARY_OBSERVATION -> SECONDARY` for **exactly nine** known r1 entries while preserving discovery ID, locator, published/observed timestamps, raw_paths, summary, verification targets and existing screening basis. This is an Evidence task **authority-class projection** with identical secondary strength, NOT a modification of original Discovery records or a new first-party upgrade. Record old/new SHA, all fields changed, reasoning, unknown-type rejection, original r1 immutable hash and acceptance chain in an edition-local projection ledger.
C. Demonstrate deterministic double-build and run unmodified Core `validate_evidence_package_basis`, `task_authority_sources` (all 36) and negative tests. If any Core function requires changing canonical Discovery/Screening or this would violate approved provenance rules, STOP with `CORE_COMPATIBILITY_BLOCKED`—no unreviewed workaround. Use a fresh `evidence/v2/packages/r2` path; never overwrite r1.

Do not modify shared Core or monkeypatch/override its source mapping in the r2 validation runtime. Any such override invalidates the claimed PASS.

## 3. Source-bound Evidence Authority Supplement

For material candidates where r1 consumed new first-party sources that were NOT bound in canonical Discovery (e.g., Google DeepMind Nano Banana 2.1 model card, Google SynthID blog, Nace Drex product docs), create faithful bounded primary excerpts with original URL/version/access date, content class, exact SHA/byte_count, and provenance. Prefer actual issuer original model/release/system card or paper where accessible; extract relevant technical mechanisms/method/limits, not just headline marketing. For original PDFs like textGrain technical report, read with appropriate PDF tools if obtainable; if unreadable, leave method-specific claims unverified.

Use frozen `build_evidence_authority_supplement` and `validate_evidence_authority_supplement` to bind exact material to **correct** Evidence Task IDs and source classes. In all 36 Cards, `source_ids` for facts about Google/Nace/vendor technical pages must point to actually bound first-party supplements, not merely old Grok/X/secondary `src-1` authorities. Unsupported source authorities remain `UNRESOLVED` or vendor-claimed.

Prioritize original-source consumption for GPT-6/Haiku, Mistral 49B/52B version pins and weight availability, Liquid d1, Kolibri, Nova Sonic, Nano Banana, OpenAI textGrain, EmbeddingGemma 2, Perplexity decider/embed, Clef-omni, Reflection Beam, agent/decision API. Preserve exact W41 date-clock boundaries and 4 W40 HOLDs.

## 4. Rebuild versioned 36-card reviewer package under real frozen Core

- Under immutable accepted 37 Discovery and Screening artifacts, construct derived r2 Evidence package, new task copies, task-bound supplement and *new* 36 candidate Evidence Cards/Views as necessary. Do not mutate r1 assets, and never claim provisional Views are acceptance outputs.
- Fix overstrong verification targets/status: `weight-repo-status=VERIFIED` is not proof of downloaded weights; `publisher claims downloadable` distinct from actual downloaded/license-verified. Decisions API `VERIFIED` applies to changelog feature announcement, not unresolved price.
- Distinguish Direct Read / Delegated Read / Original Raw or bounded excerpt / Locator Only / Failed Retrieval for every material claim with sufficient source linkage. Prevent `PRIMARY_FACT` from citing an unverified old `SOCIAL` or `SECONDARY` locator as sole authority for newly read primary paper/model-card content. Vendor measurements stay vendor metrics; license, downloadability and published clock must be separately tested.
- Preserve weak-source `HOLD`/`CONTEXT`; never force 36 VERIFIED cards. W40 carried HOLD entries, Nace pre-window original GA, Microsoft day-only cutoff and Tencent month-only remain correctly labelled.
- Real immutable Core validations: `validate_evidence_package_basis`, `task_authority_sources` 36/36, `validate_evidence_card` 36/36 with actual `repo_root`/package binding, Source Supplement validation, SHA/byte-count checks, legitimate source-owner checks, unknown-type negative injection and at least two deterministic builds for projection+task identities. Report exact exit/status. No "schema PASS" substitute for source-authority semantic validation.

## 5. Stop boundary

**DO NOT** call `accept_evidence_results` or accept Edition Views yet. No `EVIDENCE_REVIEWED` transition, Materiality/Completeness acceptance, Selection, Architecture, Draft, PDF or Human Gate. Return to Sol for **new Evidence Binding/Semantic Review r2** with:
- exact final HEAD+Tree and all changed paths;
- 9-item compatibility projection ledger with complete old/new source-type hashes + frozen-Core full PASS/failure evidence;
- indexed original-source supplement URI, source file SHA/byte count, task/claim citation graph;
- full 36 new candidate Cards with source class, VERIFIED/PARTIAL/NEEDS_MORE/MATERIAL/HOLD/CONTEXT and unresolved boundaries;
- source-coverage matrix for all material claims (direct/delegated/failed, issuer/independent);
- explicit self-consistency checks and blocker list;
- canonical State still `CANDIDATES_NORMALIZED`, no false Human approval.

If frozen Core cannot legally perform derived-task projection or supplement binding, **stop** and document defect; Core repair is separate/deferred, not an authorization in this edition.
