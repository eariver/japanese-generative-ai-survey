# W37 execution instruction — accepted Grok r3 Raw through fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / W37_RESUME_FROM_ACCEPTED_GROK_R3 / X_RAW_ALREADY_IMPORTED / BOUNDED_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-09-18 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Mission

Resume 2026-W37 Weekly production from the current:

`ISSUE_INITIALIZED / X_SOURCE_INTAKE_COMPLETE / DISCOVERY_SEEDED`

state.

The Human/Sol-reviewed Grok r3 Raw has already been imported into the repository and the canonical X Source Intake manifest has already been recorded as `COMPLETE`.

Continue from the existing X-bound Discovery seed, perform fresh primary/authoritative Discovery and carry-over disposition, then execute the current Core v2 Weekly pipeline through:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED -> materiality/completeness -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED -> fresh Human Architecture Review pending -> STOP`

Do not invent any Human decision.

Muse/OpenCode must not use, request, search for, authenticate to, or install Google Drive access. All required Grok Raw authority is already repository-local.

## 2. Invocation starting guard

The Muse invocation MUST provide the exact current remote HEAD and tree after this request commit is pushed.

Before any repository write, read-only verify:

- remote `weekly/2026-W37-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- remote W37 tree == Exact Starting Tree supplied in the invocation;
- Exact Starting SHA parent == `d574b20be2398d02120ebd5ae113a1d5274bb0ad`;
- parent tree == `065d146684daf4234e1548f790f9e94220990738`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote `main` tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

If any guard differs, perform no repository/GitHub write. Report expected versus actual and STOP.

Do not create any alternate, fallback, repair, review, temporary, or iteration branch.

Forbidden:

- force push
- reset
- rebase
- squash
- history rewrite
- destructive cleanup

## 3. Mandatory read order

Before production work, read at minimum:

1. this execution request;
2. `sources/2026-W37/production-profile.json`;
3. `sources/2026-W37/production-state.json`;
4. `sources/2026-W37/external/x/x-source-intake-v2.json`;
5. `sources/2026-W37/external/x/weekly-x-2026-W37/raw/grok-x-result-r3.md`;
6. `sources/2026-W37/execution/reviews/sol-grok-x-r3-review-20260918.md`;
7. `sources/2026-W37/discovery/discovery-v2.jsonl`;
8. current Weekly operations / carry-over / Discovery / Evidence / Selection / Architecture authority in the repository;
9. current CLI/help for any helper before invoking it;
10. released W36 authority needed for fresh carry-over derivation.

Repository authority takes precedence over remembered procedure.

## 4. Current canonical W37 state

Expected production state before formal Discovery continuation:

- issue: `2026-W37`
- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`
- lifecycle: `ISSUE_INITIALIZED`
- target gate: `ARCHITECTURE_REVIEW`
- next action: `stage:discovery`
- Human Architecture Review: `pending`
- Human Publication Preview: `pending`
- all machine checkpoints: still pending

Do not hand-edit production-state JSON.

Use canonical pipeline tooling for state/checkpoint transitions.

## 5. Canonical W37 time window

The ordinary Weekly window is end-exclusive.

America/New_York:

`[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)`

UTC authority:

`[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`

JST reference:

`[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`

Do not use calendar-date-only classification.

For any timestamped observation:

- before UTC start -> pre-window / carry-in as applicable;
- start <= timestamp < end -> ordinary W37;
- timestamp >= end -> Late Breaking.

Late Breaking must not contribute to ordinary-window breadth or ordinary candidate-source classification.

## 6. Accepted Grok r3 Raw authority

Canonical repository Raw:

`sources/2026-W37/external/x/weekly-x-2026-W37/raw/grok-x-result-r3.md`

Exact identity:

- bytes: `14803`
- SHA-256: `318ed342b3cbfeb41ea6c36838d9b3ae1b1b35c01504e0c78fca32c3768b03f5`
- observed_at: `2026-09-18T13:55:00Z`
- revision: `r3`

The repository Raw is exact byte-for-byte content from the reviewed Drive result.

Do not normalize, rewrite, repair, reformat, or replace this Raw.

The canonical X Source Intake manifest is expected to be:

`sources/2026-W37/external/x/x-source-intake-v2.json`

with:

- status: `COMPLETE`
- result status: `SUCCESS`
- drive filename: `grok-x-result-r3.md`
- discovery disposition: `DISCOVERY_RECORDED`
- discovery ID: `w37-grok-r3-45-url-ledger`
- exact Raw SHA/bytes above.

Validate using current canonical tooling when appropriate.

## 7. Sol review corrections are authority for downstream normalization

The Grok r3 Raw itself is immutable, but several derived counts in its prose are nonblocking arithmetic/role-count errors.

Read:

`sources/2026-W37/execution/reviews/sol-grok-x-r3-review-20260918.md`

The row-level direct URL ledger is accepted.

Independent Sol audit reconstructed every X/Twitter Snowflake timestamp from the 45 status IDs and verified:

- total unique direct X URLs: `45`
- `PRE_WINDOW_CARRY_IN`: `1`
- `ORDINARY_WINDOW`: `24`
- `LATE_BREAKING`: `20`

Role-aware ordinary account recount:

- ordinary unique accounts: `19`
- ordinary role-`INDEPENDENT` accounts: `12`
- ordinary role-`OFFICIAL` accounts: `4`
- ordinary role-`COMMUNITY` accounts: `3`

Additional corrections:

- total unique accounts across all 45 rows = `35`, not 32;
- C1 ordinary support = `2 INDEPENDENT + 1 COMMUNITY + 1 OFFICIAL`; do not call all three non-official accounts “independent”;
- C6 ordinary support consists of two `COMMUNITY` accounts, not two role-`INDEPENDENT` accounts.

Do not rewrite Grok Raw to fix these. Preserve exact Raw bytes and use the Sol review as the correction layer.

These corrections do not change the accepted W37 conclusion that the mandatory expansion was completed and the ordinary independent-account diagnostic floor was cleared.

## 8. Existing Discovery seed

The repository already contains:

`sources/2026-W37/discovery/discovery-v2.jsonl`

with one initial X-bound Discovery record:

`w37-grok-r3-45-url-ledger`

This record binds the exact Raw bytes above.

Do not delete, replace, or silently rewrite this seed.

Append fresh Discovery records according to the current canonical Discovery contract.

The Discovery acceptance artifact has intentionally **not** been created yet. Build it only after the complete formal W37 Discovery set is ready.

## 9. X remains Raw Observation, not technical Evidence

Never promote an X-only statement directly to a verified technical fact.

Primary/authoritative verification is required for, among other things:

- release identity and date
- model/API availability
- parameter counts / active parameters
- architecture
- context limits
- benchmark scores and methodology
- pricing
- license terms
- hardware requirements
- serving/local-inference compatibility
- retirement/deprecation schedules
- security/capability claims
- cost or latency claims
- transaction status
- autonomy or agent behavior claims

X observations may affect Discovery breadth, “why now”, community movement, materiality, or verification priorities.

Retrieval success is not semantic consumption.

## 10. Formal W37 Discovery

Perform fresh formal Discovery for W37.

Do not restrict Discovery to Grok candidates.

Inspect all required Weekly lanes:

A. Foundation Models / Reasoning  
B. Agents / Coding / Harness / Computer Use  
C. Multimodal Foundation Models  
D. Image Generation / Editing  
E. Video Generation / Editing  
F. Speech / Audio / Music Generation  
G. Open Weight / Local AI / Quantization  
H. Inference / Serving / Systems  
I. Memory / Multi-Agent / Retrieval  
J. Evaluation / Benchmarks  
K. Safety / Security  
L. Other Emerging Generative AI Technology

Use Grok r3 as one discovery sensor, not as the complete candidate universe.

Search primary/authoritative surfaces such as:

- official announcements
- official docs / API references
- release notes / changelogs
- model/system cards
- repositories
- papers
- model cards
- first-party engineering posts
- authoritative vendor documentation

Quiet lanes may legitimately remain quiet after being examined.

Do not fabricate candidates to meet a category or count quota.

## 11. W36 carry-over

Read the released W36 authority fresh and derive W37 carry-over canonically.

W36 item != automatic W37 candidate != automatic W37 Evidence != automatic W37 Selection.

Do not inherit any W36 Human decision.

For every actual carry-over obligation:

- revalidate current relevance;
- identify what changed or remained unresolved in W37;
- bind explicit external parent refs if current Discovery contract requires them;
- dispose stale carry-over explicitly.

If there are no carry-over obligations after canonical derivation, record that explicitly.

## 12. Grok candidate leads requiring primary verification

The accepted r3 Raw contains a ten-candidate pool. Treat these as leads only.

High-priority ordinary-window leads include:

### C1 — GPT-6 Astra rollout / vertical packaging
Verify from OpenAI primary authority as applicable:

- exact rollout chronology inside W37;
- API/model naming;
- ChatGPT Work / Codex availability;
- Financial Services packaging;
- pricing/context/capability claims;
- any relevant usage-limit or operational boundary from authoritative surfaces.

### C2 — DeepSeek V4.1 Flash
Verify from DeepSeek / repository / model card / paper / API authority as available:

- exact model identity;
- release date;
- multimodal claims;
- weights / open-source status;
- API model ID;
- architecture / parameter claims;
- retirement/deprecation statements;
- benchmark and integration claims.

### C3 — SWE-2 / Cognition / Fusion / Devin
Verify from Cognition and authoritative evaluation surfaces:

- SWE-2 identity and availability;
- Fusion CLI behavior / pricing / cost claims;
- Devin Voice relationship if relevant;
- benchmark methodology and source identity;
- distinguish official vendor claims from independent evaluation.

### C4 — MiniCPM5-2B
Verify from OpenBMB / model card / repository:

- exact model identity and release timing;
- weights/license;
- parameter scale;
- local inference / serving support;
- architecture/training claims;
- benchmark/evaluation boundaries.

Secondary Grok leads include:

- C5 GPT-Live-1
- C6 North Small Translate
- C7 Ling 3.0 Flash VL
- C8 hybrid/efficient architecture/runtime signals
- C9 safety-researcher resignation context
- C10 GLM-5.5 rumor

Do not elevate these merely because Grok listed them.

C5/C7/C8/C9/C10 had zero ordinary direct X URLs after canonical window correction; several were Late Breaking only. Preserve this timing boundary.

Rumor-only C10 must remain unverified unless primary authority independently establishes a material W37 fact.

## 13. Open-world requirement remains active

Grok r3 materially demonstrated the value of open-world X discovery.

Formal Web/primary Discovery must likewise not collapse to a fixed known-vendor list.

As new terms/projects/papers/repositories are encountered, follow material leads far enough to determine whether they create an additional W37 Discovery candidate.

Do not mechanically import all X open-world items. Use current Discovery relevance and source-quality rules.

## 14. Screening and normalization

After fresh Discovery is complete, execute canonical Screening/Normalization.

For each candidate preserve or explicitly derive:

- temporal relevance
- underlying event date
- W37 “why now”
- lane(s)
- duplicate/cluster identity
- primary-source availability
- authority class
- technical significance potential
- carry-over relation
- ordinary / pre-window / Late Breaking relation as applicable
- X-only versus primary-backed status

Advance canonically through `CANDIDATES_NORMALIZED`.

Do not copy Grok’s `STRONG_CANDIDATE` / `CANDIDATE_NOT_SELECTED` labels into Survey Selection decisions.

## 15. Retrieval and semantic consumption

For all non-DROP candidates, retrieve the necessary primary/authoritative sources and actually read the claim-relevant content.

Maintain the semantic distinction represented by current canonical vocabulary, equivalent to:

- retrieved and semantically consumed
- retrieved but not consumed
- source unavailable
- secondary-only
- X-only

Do not count a URL/search result/snippet as semantic consumption.

Do not produce a 1:1 mechanical “one retrieval per Evidence row” pattern if additional primary authority is required to substantiate a claim.

## 16. Evidence

Generate fresh W37 Evidence from semantically consumed authority.

Each technical claim must retain:

- source identity
- provenance
- claim boundary
- source authority class
- semantic-consumption basis
- temporal relevance
- uncertainty / limitation

Only use `VERIFIED` where the actual source supports that status.

Keep unresolved primary-source gaps explicit as `PARTIAL`, `UNRESOLVED`, or current canonical equivalent.

X community observations may remain linked as context but must not substitute for technical authority.

## 17. Materiality and completeness

Execute canonical Materiality and Completeness evaluation.

Completeness means the required space was actually examined and material gaps are explicit; it does not mean every lane must contain a selected item.

Confirm, among other things:

- all required Weekly lanes were examined;
- carry-over was disposed;
- material Grok/open-world leads were dispositioned;
- primary-source gaps remain visible;
- Late Breaking did not contaminate ordinary-window evidence;
- X-only claims were not promoted;
- discovered technically material alternatives were not silently dropped.

If a genuine Exception Gate is required, use the canonical stop contract instead of forcing progression.

## 18. Selection

Perform fresh W37 Survey Selection from current Evidence / Materiality / Completeness.

Grok labels and X attention are not Survey Selection authority.

Use current canonical Selection semantics.

Selection must be supported by the Evidence set and W37 materiality rationale.

## 19. Architecture

Build fresh W37 Architecture only after Selection completes.

Architecture must:

- trace to selected Evidence;
- preserve source/verification boundaries;
- distinguish official claims from independent observations;
- distinguish ordinary W37 facts from pre-window context and Late Breaking;
- avoid cluster-wide generalization from model-specific evidence;
- avoid converting community momentum into unsupported technical fact;
- retain residual limitations important to Draft.

In particular, do not repeat known prior failure modes where:

- a transaction state is overstated beyond first-party wording;
- a property supported for only one model becomes a cluster-wide thesis;
- internal process terms leak into reader-facing narrative;
- model/version timing is generalized to “same week” without exact support.

Validate Architecture using current canonical validators.

## 20. Fresh Human Architecture Review and STOP

After Architecture generation and validation, generate the fresh Human Architecture Review surface and STOP.

Normal endpoint:

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review pending`

Do not invent:

- `APPROVED`
- `REQUEST_CHANGES`
- any Sol/Human decision

Do not begin:

- Draft
- reader-surface gate
- Publication Preview
- Freeze
- Release

## 21. Shared-Core freeze

Do not modify:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`
- `production/survey-core-v2`

Issue #505 is a future generic X-intake hardening proposal and is out of scope for this execution.

Issue #497 and the known nonexistent `survey_agent_control_v2.py validate-state` workflow defect are also out of scope.

Do not implement shared-Core fixes during W37 production.

If a new shared-Core contradiction blocks Discovery through Architecture:

1. stop at the last safe edition-local checkpoint;
2. record exact command / expected / actual / minimal reproduction;
3. do not invent an edition-local semantic workaround;
4. STOP.

## 22. Commit discipline

Stay on:

`weekly/2026-W37-v2-work`

At meaningful stages:

- use normal commits;
- non-force push;
- remote read-back;
- verify expected prior remote SHA before each write group.

No new branch.

No force/reset/rebase/squash/history rewrite.

## 23. Execution provenance

Maintain W37 edition-local execution provenance covering at least:

- invocation Starting SHA/tree;
- accepted Grok r3 Raw path/SHA/bytes;
- Sol r3 review/correction path;
- canonical X temporal counts;
- X Source Intake `COMPLETE`;
- initial X Discovery seed ID;
- fresh Discovery total and lane coverage;
- W36 carry-over result;
- Screening distribution;
- retrieval counts;
- semantic-consumption counts;
- Evidence counts by status;
- Materiality result;
- Completeness result;
- Selection distribution;
- Architecture path/hash;
- validation results;
- ending HEAD/tree;
- Human Architecture Review path/hash;
- Human Architecture Review pending;
- shared-Core changed paths = 0;
- main unchanged;
- Production Line unchanged.

## 24. Final validation and report

Before normal stop, read back:

- remote W37 HEAD/tree;
- production-state lifecycle / next action / target gate;
- machine checkpoint states;
- X intake manifest and Raw identity;
- accepted Discovery artifact and counts;
- Screening/Evidence/Selection counts;
- Materiality / Completeness state;
- Architecture path/hash;
- Human Architecture Review path/hash;
- changed paths;
- remote `main` still:
  - HEAD `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`
  - tree `62cf5dfb30cc692cd19c11289fa80c837fd17b66`
- remote `production/survey-core-v2` still:
  - HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
  - tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- shared-Core changed paths = 0.

Final report must include:

- Starting SHA/tree;
- Grok r3 Raw SHA/bytes;
- canonical X accounting;
- Discovery count/lane coverage;
- W36 carry-over result;
- Screening distribution;
- retrieval and semantic-consumption status;
- Evidence status counts;
- Materiality;
- Completeness;
- Selection distribution;
- Architecture summary/validation;
- Human Architecture Review path;
- Ending SHA/tree;
- main/Production Line unchanged confirmation;
- Core changes = 0;
- exact stop reason.

Human decision must not be included or inferred.
