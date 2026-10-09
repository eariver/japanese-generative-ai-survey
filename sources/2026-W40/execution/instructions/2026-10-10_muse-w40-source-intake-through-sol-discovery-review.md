# W40 Muse Execution Contract — Source Intake Completion through Sol Discovery Completeness Review

Status: `SOL_EXECUTION_AUTHORITY / BOUNDED_AT_SOL_DISCOVERY_COMPLETENESS_REVIEW`  
Edition: `2026-W40`  
Prepared: 2026-10-10 JST  
Owner: Sol editorial/supervisory coordinator  
Executor: Muse (bulk collection, edition-local pipeline execution only)

## 0. Execution guard — mandatory, fail closed

Repository: `eariver/japanese-generative-ai-survey`  
**Existing and only allowed work branch:** `weekly/2026-W40-v2-work`  
Reviewed `main` HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Pre-instruction authority HEAD: `852a02463bde4100982774211621aaedce6e52be`  
Pre-instruction Tree: `0dbe719b7447a92f7d7f3cd77152c64c46c67e67`

The **exact Muse starting work-branch HEAD and Tree** must be specified in the outer invocation that links to this contract; use the *commit that adds this contract*, not the pre-instruction HEAD above. The outer invocation is authoritative for the execution starting SHA/Tree.

**Before any repository write**, verify independently, read-only:

1. remote `weekly/2026-W40-v2-work` HEAD exactly equals invocation's Starting SHA;
2. corresponding commit tree exactly equals invocation's Starting Tree;
3. remote `main` HEAD exactly equals the reviewed main SHA above;
4. invocation's starting commit is descendant of the pre-instruction authority commit, not a replaced or parallel history;
5. `sources/2026-W40/production-state.json` remains `ISSUE_INITIALIZED`, next action `stage:discovery`, Architecture and Publication Preview Human Gates pending.

**If any check fails: STOP with expected/actual values; ZERO WRITES.** Do not recover by rebasing, cherry-picking, resetting, force-pushing, creating a new branch or replacing a baseline. Once verified, use exclusively the existing W40 branch for edition-local writes and normal commits / non-force fast-forward push.

No Shared Core v2 scripts, schemas, config, CI/workflow, `main`, other editions, W39 acceptance history, existing Human Gates, or global documentation changes are authorized. Do not create or modify a normal Core stage checkpoint without the Sol permission required below.

## 1. Mission and exact stop boundary

Complete retrospective **Source Intake and Core-schema-valid Discovery preparation for W40**, using preserved Grok Raw and Daily X observations, including independent newness/time-scope and negative-space research. Deliver an inspectable, SHA-qualified bundle for **Sol Discovery Completeness Review**.

**Stop at `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY` or an explicit `SOL_DISCOVERY_COMPLETENESS_REVIEW_BLOCKED`.**

This unit does **not** authorize:

- silently declaring Sol coverage PASS or creating a fabricated `reviewed_by: Sol`;
- advancing Production State to `DISCOVERY_COLLECTED` or beyond;
- starting Screening, Evidence, Materiality, Selection, Architecture, Draft, Publication Candidate or Human Gate;
- accepting a sparse set of model launch headlines as full research coverage.

Normal Core deterministic preflight/schema validation of *prepared* Discovery artifacts is allowed. If it depends on actual Sol approval, record `REVIEW_PENDING` rather than forging a favorable review. A canonical accepted/advanced Stage checkpoint is **not** generated before Sol reviews the coverage.

After stopping, Sol independently reviews breadth/negative-space and either authorizes transition into Screening or issues a bounded gap-fill request.

## 2. Immutable editorial window

Profile `WEEKLY` / Publication Profile `WEEKLY_MAGAZINE`.

- `[2026-09-25T18:00:00-04:00, 2026-10-02T18:00:00-04:00)` America/New_York (end exclusive).
- `[2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)` UTC.
- `[2026-09-26 07:00, 2026-10-03 07:00)` JST.

Classify each source and claim by **event/release date**, **primary source publication date**, **observed X post date**, **retrieval date**, and **version/tag**. They are not interchangeable. Event announcements may be in the ordinary window while the actual general rollout occurs later. Content observed after the cutoff belongs to `LATE_BREAKING` or subsequent edition, unless it is specifically a retrospective source verification of an in-window event. Historical rechecks of pre-window research are `CONTEXT`, not new W40 paper releases.

## 3. Mandatory input reading order

1. `docs/survey-production-core-v2-session-bootstrap.md`
2. `docs/survey-production-core-v2-sol-luna-review-governance.md`
3. `docs/survey-production-core-v2-x-source-intake.md` and any currently authoritative Core v2 contracts/configuration
4. W40 `production-profile.json`, `production-state.json`, `execution/index.md`, `execution/sessions/sol-w40-initial-20261010.md`
5. W40 `external/x/x-source-intake-v2.json` and `external/x/weekly-x-2026-W40/raw/grok-x-result.md`
6. `execution/source-intake/w40-grok-dailyx-review-r0.md` and `w40-grok-dailyx-reconciliation-r0.json`
7. `execution/source-intake/w40-dailyx-xstatus-ledger-r1.json` and `w40-dailyx-xstatus-audit-r1.md`
8. `execution/source-intake/w40-sol-source-intake-register-r1.json` and `w40-sol-source-intake-review-r1.md`
9. `execution/source-intake/w40-targeted-lane-expansion-r2.json` and `w40-targeted-lane-expansion-r2.md`
10. W39 `candidate-selection-v2.json`, W39 Discovery/Screening carries, and W39 accepted X manifest **for format/reference only**; do not copy W39 outcome or source authority as W40 verification.
11. Applicable schemas: `schemas/survey-discovery-record.schema.json`, `schemas/discovery-acceptance-v2.schema.json`, `schemas/x-source-intake-v2.schema.json`, `schemas/collector-run.schema.json`, `schemas/raw-source-index.schema.json` and the stage validator.

**Prior Sol lists are investigative leads, not a verified closed universe or mandatory article selections.**

## 4. Existing sources — integrity and known findings

### Grok

Exact preserved Raw path:  
`sources/2026-W40/external/x/weekly-x-2026-W40/raw/grok-x-result.md`

Expected Raw SHA-256:  
`10b3d7735befa1ec435462aa5254cb45b76b3d59d6f4fca0e15fc54db0dca79f`  
Expected bytes: `20477`.

Grok supplied a 10-row candidate pool but wrote **4 auditable direct X status URLs**, despite asserting more than 25 posts and more than 15 independent accounts. Preserve raw bytes. **Do not simply certify Grok self-reported coverage as independently checked.** If a new bounded Grok addendum is genuinely needed, keep it separate and ask Sol to commission it; never manufacture X URLs or turn a statistical absence into positive evidence.

### Daily X

A separate independent Daily X audit recorded **64 unique X status IDs / 55 distinct account handles**, all whose ID-derived UTC timestamps fall in the W40 window. It is an independent observation set, **not proof of the unseen Grok posts**, not proof that 55 accounts are independent organizations, and not first-party evidence for model capabilities.

Daily X available reports: `2026-09-27`, `09-28`, `09-29`, `09-30`, `10-02` PDF. Exact Drive file IDs, PDF hashes, post URLs and UTC times are in `w40-dailyx-xstatus-ledger-r1.json`. Daily reports ending October 1 and October 3 at 07:00 JST are absent; these daily archive gaps do not imply no releases on those dates.

### Sol primary-source leads

Sol's first-pass register: **21 entries** — `17 ordinary`, `1 pre-window`, `1 official-X-only / product-release-unverified`, `2 W39 carryovers on HOLD`. Second targeted gap fill: **5 entries** — `4 ordinary` and `1 publication-time unresolved`. The 26 entries **are not an accepted Discovery inventory** and include related release announcements that may need splitting/merging by primary authority.

Important version/claim boundaries to preserve:

- Sonnet 5.5 Sep 28 vs Opus 5.5 pre-window Sep 22;
- GPT-6.1 Sol, dots, Agents API computer use, Decisions API, Ultrafast and other DevDay announcements — distinguish individual rollout/price/security conditions;
- Ollama `/v1/systemone` Sep 29 vs Oct 1 Cloudflare Clef/Clef-flash and Strands Decider 2B; vendor benchmarks are not comparable by default;
- Gemini 4 Argon Sep 30 limited-access announcement: do **not** transmute a `1M token limit` into `1M output token limit` unless official model specs prove it;
- SynthID Bio first official announcement Sep 30 vs Oct 1 X momentum;
- FLUX 3 Image official Oct 1 X lead vs July 23 original FLUX 3 foundation introduction; independently resolve Image SKU/model card/weights and availability date;
- LIFT arXiv submission Sep 25 **before** the W40 22:00Z cutoff; Context Language Models arXiv Sep 29 within it;
- Sep 28 AMD–World Labs **acquisition agreement**, not a completed acquisition; secondary financial valuation not accepted;
- Sep 29 NVIDIA VSS Blueprint 3.3 vendor visual token savings and concurrency rates; Sep 30 NVIDIA Nemotron ASR adaptation, NeMo Relay tracing, AMD Ross;
- Oct 2 NVIDIA DGX Spark 64GB item: explicit publication-time uncertainty around 22:00Z cutoff; Oct 23 planned availability is not a W40 shipping event;
- W39 Pixel Canary/Codex identity and TBC/AWS bio-video acceleration multipliers remain unsupported and on HOLD.

## 5. Muse authorized execution — end to end within this boundary

### A. Independent source sweep / negative-space

Conduct independent discovery **not restricted to the 26 provided leads**. Include official vendor release notes, model and API docs, paper pages, paper versions, model/repository release/tag histories, primary evaluator methods, and credible independent technical reproductions.

Cover lanes A–L: proprietary models; open weights and licenses; coding/browser/agent harness; multimodal/image/OCR; video and temporal; audio/speech; serving/quantization/local AI; hardware; evaluations and reproduction; safety and cybersecurity; retrieval/memory/enterprise; new open-world topics.

Directly search the two Daily X archive gaps and weak lanes (open-weight LLM, video, audio, long-context/retrieval, inference system internals). Repeat targeted search using alternate project/technical vocabulary. Log search expressions, sources, negative results and date limitations. Coverage counts alone do not prove material completeness.

Freshly verify any major official announcements and meaningful sources absent from Sol's list. Separate `NO_SOURCE_FOUND`, `NOT_NEW_IN_WINDOW`, `LOW_MATERIALITY`, and `SOURCE_INACCESSIBLE`.

### B. Primary Raw capture and provenance

For each unique material or plausibly material source, fetch original article/documentation/release/model card/paper repository content and preserve **actual captured bytes where licensed and practical** with SHA-256, byte count, source URL, retrieval time, publication time evidence, access mode and if applicable source revision/commit. Preserve original snippets/body relevant to bounded technical claims. Do not falsely label re-authored summaries as byte-identical remote Raw; keep derivative summaries separate and link exact source content. Where copyright or source access restricts redistribution, retain lawful excerpts, locator, retrieval proof and explicit `CONTENT_ACCESS_LIMITED` status. **No invented full source captures or unverifiable primary facts.**

Write under W40 edition-local `collectors/primary/runs/<new-run-id>/`, with compliant collector-run and raw-source index records. Never rewrite existing Grok bytes, prior Daily X ledger or Sol input registers.

For relevant sources, consume substance (model architecture/method, data/evaluation conditions, version, availability/license, limitations, attribution) rather than stopping at headline or URL. Run iterative gap-fill if the first source is incomplete.

### C. Grok/X result authority

Independently validate the existing Raw SHA and available direct URLs. Reconcile the two *separate* source classes (Grok 4 direct URLs and Daily X 64 URLs) without asserting that they overlap or prove Grok's unlisted claims.

Use actual `schemas/x-source-intake-v2.schema.json` accepted enumerations. Because the Grok result is received but evidence coverage is partial, consider `PARTIAL` with accurate `discovery_disposition` and concrete Discovery IDs if/when created. Set `observed_at` / `imported_at` from traceable execution/Drive facts; do not fabricate timestamps from report approximations. If the schema/lifecycle cannot truthfully represent the current state, record a bounded block and stop rather than using a false `SUCCESS`.

**Status `COMPLETE` on the manifest means the required result/disposition has been recorded, not that Grok's self-reported >25 URLs passed independent auditing.** Capture that limitation explicitly.

### D. Discovery candidate materialization

Deduplicate by **specific event and primary authority**, not just brand. Include independently discovered omissions, rejected/weak leads, attribution boundaries, and W39 rechecks. Generate schema-compliant `sources/2026-W40/discovery/discovery-v2.jsonl` and supporting collector Raw references.

Every record must satisfy `schemas/survey-discovery-record.schema.json`: origin, research pass, parent refs, obligation IDs, collector/run IDs, source locator, timestamps, raw paths, metadata. Supply an independently checkable mapping of raw file to discovery ID and the published/observed timing basis; do not use X post date for original issuer publication unless it is itself the direct event.

Prepare the SHA-qualified `discovery-accepted-v2` **candidate** and its source-graph proof for Sol inspection. Do not finalize an artifact named `discovery-accepted-v2.json` as a genuine *Sol-reviewed acceptance* before Sol has reviewed it; if the formal validation needs a complete file for structural preflight, keep it in an isolated proposal/validation directory clearly marked `PROPOSED_NOT_ACCEPTED`, and do not update current Production State/checkpoints.

The execution agent's own positive conclusion is not Sol's independent completeness finding.

### E. Deterministic validation / report

Run the repository's reviewed Core v2 preflight/schema checks for this stage on the prospective file set, with logged commands, input hashes, stdout/stderr, exit code, and exact mismatch reports. Prefer meaningful Core checks to hand-authored optimistic PASS flags; record any validator whose acceptance stage cannot be run until Sol review. Never alter Core implementations or introduce a new override.

Update:

- `sources/2026-W40/execution/index.md`;
- current `sources/2026-W40/execution/sessions/sol-w40-initial-20261010.md` only for accurate operations **or** append a distinctly named Muse execution session record;
- a complete inventory of generated Raw and their hashes;
- a detailed, reader-inspectable `SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF.md` under the W40 execution subtree.

## 6. Sol-facing dossier required at terminal

Provide all of:

1. exact Starting HEAD/Tree, reviewed `main`, Final HEAD/Tree, direct ancestry and non-force push evidence;
2. changed-file allowlist and exact final Production State / Human Gate state (expected still `ISSUE_INITIALIZED`);
3. source surfaces actually searched; per-lane A–L coverage matrix and independent open-world findings; queries/date limitations;
4. per-event/primary-date provenance, within/pre/late/unknown buckets and follow-up statuses; no retrospective conflation;
5. complete deduplicated source/candidate count, how many first-party bodies actually consumed, inaccessible sources, weak and unselected leads, cross-vendor/version ambiguity;
6. X raw proof, Daily X 64 ledger proof, separate status ID cohorts and count discrepancy; no false 25-status acceptance;
7. W39 Pixel Canary, TBC rechecks with official source evidence or explicit HOLD;
8. exact Discovery records and each bound Raw SHA, any source-graph/acceptance proposal and schema checks;
9. exclusions and counterfactual omissions: what the original 10-row Grok list and 26 lead list both missed;
10. unclosed findings ranked `BLOCKER`, `NONBLOCKING`, or `SOURCE_INACCESSIBLE`, with targeted next steps;
11. an explicit terminal outcome, either:
   - `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY` **only if** complete raw/provenance and an independently auditable coverage dossier exist, or
   - `SOL_DISCOVERY_COMPLETENESS_REVIEW_BLOCKED` if evidence/validation gaps remain.

Do not claim Human Architecture approval, Accepted Evidence, Selection complete, or publication readiness.

## 7. Allowed edits and prohibited substitutions

Allowed: W40 collector runs/raw indexes, W40 edition-local external/X manifest (preserve original Raw), W40 Discovery *draft/pre-acceptance* records, W40 execution/QA logs, and W40 execution navigation/sessions. Existing W40 Sol input registers are immutable references; add revisions rather than rewriting those findings.

Prohibited: branch creation, forced history rewriting, Core/schema/config/CI patches, W39 or other edition writes, special-edition edits, editing `main`, changing Architecture/Publication Human Gates, or moving `production-state.json` beyond `ISSUE_INITIALIZED` in this bounded unit.

Use normal commits and non-force push only on the existing work branch; verify final remote read-back. If page/retrieval limits obstruct completion, honestly stop `BLOCKED` with work already persisted; never shrink criteria to manufacture a PASS.

## 8. Final report shape

```text
W40_MUSE_SOURCE_INTAKE_DISCOVERY_HANDOFF
Starting HEAD:
Starting Tree:
Reviewed main HEAD:
Final HEAD:
Final Tree:
Changed-file paths:
UTC research window:
Raw/source file counts & bytes:
Ordinary/pre/late/unknown event and source counts:
Grok X: preserved Raw SHA; exact disposition:
Daily X: 64 direct post identities; independent source limitation:
Discovery records and schema checks:
Sol completeness findings: REVIEW_PENDING (Muse MUST NOT fill PASS)
Production State: ISSUE_INITIALIZED
Human Gates: PENDING / PENDING
Core v2 changed: NO
Terminal: SOL_DISCOVERY_COMPLETENESS_REVIEW_READY | SOL_DISCOVERY_COMPLETENESS_REVIEW_BLOCKED
```

STOP. Return findings to Sol for independent research coverage/quality judgment; **no Screening or downstream execution without new Sol authorization**.
