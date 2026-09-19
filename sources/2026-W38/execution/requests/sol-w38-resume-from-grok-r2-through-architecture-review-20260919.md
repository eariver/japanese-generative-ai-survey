# W38 execution instruction — accepted Grok r2 Raw through fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / W38_RESUME_FROM_ACCEPTED_GROK_R2 / X_RAW_REPOSITORY_LOCAL / BOUNDED_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W38-v2-work`

## 1. Mission

Resume 2026-W38 Weekly production from the current:

`ISSUE_INITIALIZED / GROK_R2_REPOSITORY_LOCAL / DISCOVERY_NOT_STARTED`

state.

The Human-mediated Grok r2 result has already been independently reviewed by Sol, and its exact bytes have been imported repository-locally.

First canonicalize the X Source Intake result/manifest and bind an X-derived Discovery seed without rewriting Raw bytes. Then perform fresh primary/authoritative Discovery and carry-over disposition, and execute the current Core v2 Weekly pipeline through:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED -> materiality/completeness -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED -> fresh Human Architecture Review pending -> STOP`

Do not invent any Human decision.

Muse/OpenCode must not use, request, search for, authenticate to, or install Google Drive access. All required Grok Raw authority is already repository-local.

## 2. Invocation starting guard

The Muse invocation MUST provide the exact current remote HEAD/tree after this execution request commit is pushed.

Before any repository write, read-only verify:

- remote `weekly/2026-W38-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- remote W38 tree == Exact Starting Tree supplied in the invocation;
- Exact Starting SHA parent == `b7ed71b93d9f50955fbe7fd31c85ead659842f0f`;
- parent tree == `a209df54964202b59b7ae16be9736215d3824e6e`;
- remote `main` HEAD == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- remote `main` tree == `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
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
2. `sources/2026-W38/production-profile.json`;
3. `sources/2026-W38/production-state.json`;
4. `sources/2026-W38/external/x/x-source-intake-v2.json`;
5. `sources/2026-W38/external/x/weekly-x-2026-W38/raw/grok-x-result-r2.md`;
6. `sources/2026-W38/execution/reviews/sol-grok-x-r2-review-20260919.md`;
7. `sources/2026-W38/execution/reviews/sol-grok-x-r1-review-20260919.md`;
8. `sources/2026-W38/execution/sessions/w38-pre-discovery-research-prep-20260919-r1.md`;
9. current Weekly operations / carry-over / Discovery / Evidence / Selection / Architecture authority in the repository;
10. current CLI/help for any helper before invoking it;
11. released W37 authority needed for fresh W38 carry-over derivation.

Repository authority takes precedence over remembered procedure.

## 4. Current canonical W38 state

Expected production state before formal Discovery continuation:

- issue: `2026-W38`
- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`
- lifecycle: `ISSUE_INITIALIZED`
- target gate: `ARCHITECTURE_REVIEW`
- next action: `stage:discovery`
- Human Architecture Review: `pending`
- Human Publication Preview: `pending`
- all machine checkpoints: pending

Do not hand-edit production-state JSON.

Use canonical pipeline tooling for state/checkpoint transitions.

The existing execution index still reflects the pre-Grok blocking stop and contains stale Grok task navigation metadata. Update it during canonical result recording so it points to the accepted r2 Raw/Sol review and current manifest state. Do not treat the stale human-readable index as machine lifecycle authority.

## 5. Canonical W38 time window

The ordinary Weekly window is end-exclusive.

America/New_York:

`[2026-09-11T18:00:00-04:00, 2026-09-18T18:00:00-04:00)`

UTC authority:

`[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`

JST reference:

`[2026-09-12T07:00:00+09:00, 2026-09-19T07:00:00+09:00)`

For timestamped X observations, use the Snowflake-derived UTC ledger accepted by Sol.

Late Breaking must not contribute to ordinary-window breadth or ordinary candidate-source classification.

## 6. Accepted Grok r2 Raw authority

Canonical repository Raw:

`sources/2026-W38/external/x/weekly-x-2026-W38/raw/grok-x-result-r2.md`

Exact identity:

- bytes: `16022`
- SHA-256: `dac7e19fefcd2760efe82e4e602c8faa0f819b39866c0cffca6f6f02cc9e2634`
- revision: `r2`

The repository Raw is exact byte-for-byte content from the reviewed Drive result.

Do not normalize, rewrite, repair, reformat, or replace this Raw.

r1 remains historical failed Raw on Drive only and must not be imported as canonical result.

## 7. Sol r2 review corrections are downstream authority

Read:

`sources/2026-W38/execution/reviews/sol-grok-x-r2-review-20260919.md`

The row-level 25-status-ID ledger is accepted.

Independent Sol audit verified:

- total unique status IDs: `25`
- `PRE_WINDOW_CARRY_IN`: `0`
- `ORDINARY_WINDOW`: `23`
- `LATE_BREAKING`: `2`
- `TIME_UNVERIFIED`: `0`
- duplicate status IDs: `0`
- Snowflake timestamp mismatches: `0`
- temporal-class mismatches: `0`

Role-aware ordinary account recount:

- ordinary unique accounts: `15`, not 16
- role-`INDEPENDENT`: `7`
- role-`OFFICIAL`: `3`
- role-`COMMUNITY`: `5`, not 6

Candidate-level correction:

- C1 ordinary URLs: `7`, not 8
- C1 ordinary accounts: 7
- C1 independent accounts: 4
- C1 community accounts: 3
- C1 classification remains `MULTI_ACCOUNT_X`

C2 exact ordinary support:

- URLs: 5
- accounts: 2
- independent: 1
- official: 1
- downstream normalized source-breadth class: `MULTI_ACCOUNT_X`

C3:

- URLs: 6
- accounts: 1
- classification: `OFFICIAL_ONLY_X`

C4:

- URLs: 5
- accounts: 5
- independent: 2
- official: 1
- community: 2
- classification: `MULTI_ACCOUNT_X`

Do not rewrite Grok Raw to fix the derived summaries.

Preserve exact Raw bytes and use the Sol review as the correction layer.

## 8. Timestamp provenance caveat

The r2 Raw front matter self-declares:

`observed_at: 2026-09-19T13:20:00+09:00`

Sol did not accept that value as independently verified wall-clock completion provenance.

Do not rewrite the Raw.

When recording repository import/provenance:

- preserve the Raw field exactly;
- keep the Sol review linked;
- use actual timezone-aware worker/import timestamps for repository state transitions;
- do not propagate the Raw `observed_at` as authoritative machine execution time.

If the canonical X result recorder requires an external `observed_at`, inspect its current contract and record the distinction explicitly rather than silently substituting a guessed timestamp.

## 9. Canonicalize X Source Intake

Current X manifest remains:

`AWAITING_GROK`

because Sol intentionally staged the reviewed Raw before canonical machine result recording.

Use the current canonical X intake helper/controller to record r2 as the successful result.

Required semantics:

- run ID: `weekly-x-2026-W38`
- result status: `SUCCESS`
- drive filename / provenance name: `grok-x-result-r2.md`
- exact Raw path/SHA/bytes from §6
- Sol review path from §7
- discovery disposition: `DISCOVERY_RECORDED` only after the repository-local X Discovery seed is durably created
- manifest final status: `COMPLETE`

Do not manually forge a manifest if canonical tooling exists.

Validate the completed manifest with current canonical tooling.

## 10. Initial X-bound Discovery seed

Create one repository-local Discovery seed binding the accepted r2 Raw and Sol correction record.

Suggested stable semantic identity:

`w38-grok-r2-25-url-ledger`

Use the current Discovery schema and canonical helper behavior rather than copying this literal blindly if the current contract requires a different generated ID shape.

The seed must preserve:

- exact Raw path/SHA;
- Sol review/correction path;
- ordinary/pre/late split;
- X as `SOCIAL_OBSERVATION / Raw Observation / community signal`;
- the fact that technical claims remain unverified;
- candidate/community provenance sufficient for downstream traceability.

Do not encode Grok's `STRONG_CANDIDATE` labels as Survey KEEP/SELECTED decisions.

## 11. X remains Raw Observation, not technical Evidence

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
- transaction/partnership terms
- autonomy or agent behavior claims

X observations may affect Discovery breadth, why-now, community movement, materiality, or verification priorities.

Retrieval success is not semantic consumption.

## 12. Formal W38 Discovery

Perform fresh formal Discovery for W38.

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

Use Grok r2 as one discovery sensor, not as the complete candidate universe.

The pre-Discovery preparation note is non-authoritative breadth input only.

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

## 13. W37 carry-over

Read the released W37 authority fresh and derive W38 carry-over canonically.

W37 item != automatic W38 candidate != automatic W38 Evidence != automatic W38 Selection.

Do not inherit any W37 Human decision.

For every actual carry-over obligation:

- revalidate current relevance;
- identify what changed or remained unresolved in W38;
- bind explicit external parent refs if current Discovery contract requires them;
- dispose stale carry-over explicitly.

If there are no carry-over obligations after canonical derivation, record that explicitly.

## 14. Grok r2 candidate leads requiring primary verification

Treat these as leads only.

### C1 — GPT-6 Astra adoption / specialized use / Law / agents

Verify from OpenAI primary authority as applicable:

- current Astra identity and availability;
- Agents API relationship;
- Astra for Law identity/timing;
- official capability claims;
- computer-use/agent boundaries;
- pricing/context/limits;
- whether any technical claims in the X posts are first-party supported.

The lrogersaz hotel reconciliation post is `LATE_BREAKING` and cannot support ordinary W38 breadth.

### C2 — Gemini 3.8 family / Live

Verify from Google/DeepMind primary authority:

- exact model identity and release timing;
- Live / speech-to-speech capabilities;
- tool-use behavior;
- language coverage;
- model card / safety boundaries;
- pricing/availability where material.

Do not promote @tetumemo's integration observations into official technical facts.

### C3 — Anthropic R&D metrics / biomolecular optimization / LSVP / Accenture evaluation

Verify separately from Anthropic primary authority and linked artifacts:

- exact R&D measurement methodology and scope;
- biomolecular optimization repository/report;
- experimental validation boundaries;
- Life Sciences Verification Program identity/safeguards;
- Accenture evaluation partnership terms and role.

X support is `OFFICIAL_ONLY_X`; do not describe independent ordinary corroboration unless separately discovered.

### C4 — Jev / TypeSafe AI structured decision model

Verify from first-party TypeSafe AI authority as available:

- exact product/model identity;
- release/early-access status;
- architecture or non-generative framing;
- training/RLCD claims;
- latency/performance claims;
- pricing/availability;
- intended routing/triage use.

Do not rely on X community summaries for technical architecture.

### Secondary leads

Also disposition, without automatic promotion:

- local GGUF/MLX tooling;
- Qwen/Chinese omni signals;
- image/video quiet-lane claim;
- memory/RAG quiet-lane claim;
- cipher/math anecdotes;
- other open-world candidates found during primary Discovery.

## 15. Open-world requirement remains active

Formal primary/Web Discovery must not collapse to the four Grok strong candidates or a fixed known-vendor list.

As new terms/projects/papers/repositories are encountered, follow material leads far enough to determine whether they create additional W38 Discovery candidates.

Do not mechanically import all X open-world items.

Use current Discovery relevance and source-quality rules.

## 16. Screening and normalization

After fresh Discovery is complete, execute canonical Screening/Normalization.

For each candidate preserve or explicitly derive:

- temporal relevance
- underlying event date
- W38 why-now
- lane(s)
- duplicate/cluster identity
- primary-source availability
- authority class
- technical significance potential
- carry-over relation
- ordinary / pre-window / Late Breaking relation as applicable
- X-only versus primary-backed status

Advance canonically through `CANDIDATES_NORMALIZED`.

Do not copy Grok's candidate labels into Survey Selection decisions.

## 17. Retrieval and semantic consumption

For all non-DROP candidates, retrieve the necessary primary/authoritative sources and actually read the claim-relevant content.

Maintain the semantic distinction represented by current canonical vocabulary, equivalent to:

- retrieved and semantically consumed
- retrieved but not consumed
- source unavailable
- secondary-only
- X-only

Do not count a URL/search result/snippet as semantic consumption.

Do not produce a mechanical one-retrieval-per-Evidence-row pattern when additional primary authority is required to substantiate a claim.

## 18. Evidence

Generate fresh W38 Evidence from semantically consumed authority.

Each technical claim must retain:

- source identity
- provenance
- claim boundary
- source authority class
- semantic-consumption basis
- temporal relevance
- uncertainty / limitation

Only use `VERIFIED` where the actual source supports that status.

Keep unresolved primary-source gaps explicit as `PARTIAL`, `UNRESOLVED`, or the current canonical equivalent.

X community observations may remain linked as context but must not substitute for technical authority.

## 19. Materiality and completeness

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

## 20. Selection

Perform fresh W38 Survey Selection from current Evidence / Materiality / Completeness.

Grok labels and X attention are not Survey Selection authority.

Use current canonical Selection semantics.

Selection must be supported by the Evidence set and W38 materiality rationale.

## 21. Architecture

Build fresh W38 Architecture only after Selection completes.

Architecture must:

- trace to selected Evidence;
- preserve source/verification boundaries;
- distinguish official claims from independent observations;
- distinguish ordinary W38 facts from pre-window context and Late Breaking;
- avoid cluster-wide generalization from model-specific evidence;
- avoid converting community momentum into unsupported technical fact;
- retain residual limitations important to Draft.

Do not repeat known prior failure modes where:

- a transaction/partnership state is overstated beyond first-party wording;
- a property supported for only one model becomes a cluster-wide thesis;
- internal process terms leak into reader-facing narrative;
- model/version timing is generalized to "same week" without exact support.

Validate Architecture using current canonical validators.

## 22. Fresh Human Architecture Review and STOP

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

## 23. Shared-Core freeze

Do not modify:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`
- `production/survey-core-v2`

Issue #505 remains future generic X-intake hardening and is out of scope.

Issue #508 generic Weekly pagination hardening is out of scope.

Known Freeze/release defects are irrelevant before Architecture Review and must not be repaired here.

If a new shared-Core contradiction blocks Discovery through Architecture:

1. stop at the last safe edition-local checkpoint;
2. record exact command / expected / actual / minimal reproduction;
3. do not invent an edition-local semantic workaround;
4. STOP.

## 24. Commit discipline

Stay on:

`weekly/2026-W38-v2-work`

At meaningful stages:

- use normal commits;
- non-force push;
- remote read-back;
- verify expected prior remote SHA before each write group.

No new branch.

No force/reset/rebase/squash/history rewrite.

## 25. Execution provenance

Maintain W38 edition-local execution provenance covering at least:

- invocation Starting SHA/tree;
- accepted Grok r2 Raw path/SHA/bytes;
- Sol r2 review/correction path;
- canonical X temporal counts;
- corrected X account/candidate counts;
- X Source Intake `COMPLETE`;
- X Discovery seed ID;
- fresh Discovery total and lane coverage;
- W37 carry-over result;
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

## 26. Final validation and report

Before normal stop, read back:

- remote W38 HEAD/tree;
- production-state lifecycle / next action / target gate;
- machine checkpoint states;
- X intake manifest and Raw identity;
- Sol r2 review identity;
- accepted Discovery artifact and counts;
- Screening/Evidence/Selection counts;
- Materiality / Completeness state;
- Architecture path/hash;
- Human Architecture Review path/hash;
- changed paths;
- remote `main` still:
  - HEAD `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`
  - tree `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`
- remote `production/survey-core-v2` still:
  - HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
  - tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- shared-Core changed paths = 0.

Final report must include:

- Starting SHA/tree;
- Grok r2 Raw SHA/bytes;
- canonical corrected X accounting;
- Discovery count/lane coverage;
- W37 carry-over result;
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
