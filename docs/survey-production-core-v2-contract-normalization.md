# Survey Production Core v2 — Contract Normalization

Status: `PHASE 1 OUTPUT / candidate canonical contract map`  
Established: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Inspected `main`: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Purpose

This document resolves the major contract drifts identified by Phase 0 before implementation refactoring begins.

It is intentionally a **candidate v2 contract on the improvement branch**, not yet the operational production authority. Until coherent v2 changes are reviewed and merged, current `main` remains the production source of truth.

The objectives are:

1. assign one owner to each major production rule;
2. distinguish shared Core rules from research/editorial Profile rules and Publication rules;
3. distinguish current canonical intent from legacy compatibility;
4. define a target Human Gate / state / release / temporal-scope model suitable for Weekly, Retrospective Period, and Thematic production;
5. provide Phase 2/3 with stable decisions so implementation does not accidentally generalize stale behavior.

---

## 2. Authority model

### 2.1 During this improvement branch

Production authority remains current `main`.

The improvement documents define the target design only on:

```text
refactor/survey-production-core-v2
```

W33 and SP001 must not treat an unmerged feature branch as canonical production policy.

### 2.2 Target authority hierarchy after v2 merge

The target hierarchy is:

```text
AGENTS.md / session bootstrap
  -> Survey Production Core Contract
      -> Research / Editorial Profile Contract
          -> Weekly Profile
          -> Retrospective Period Profile
          -> Thematic Profile
      -> Publication Profile Contract
      -> optional Series Research Contract
  -> machine-readable config / schema implementing those contracts
  -> workflows / scripts implementing config and schema
  -> edition state / artifacts recording execution under one exact contract identity
```

Rules lower in the hierarchy may specialize higher-level extension points but must not silently contradict them.

### 2.3 Contract source categories

After v2 stabilization, documents should explicitly identify themselves as one of:

- `CANONICAL_CONTRACT`
- `PROFILE_CONTRACT`
- `OPERATIONS_GUIDE`
- `IMPLEMENTATION_STATUS`
- `HISTORICAL_DESIGN`
- `LEGACY_REPLAY_GUIDE`
- `EDITORIAL_BACKLOG / PLANNING`

This avoids the present situation where an old implementation baseline and a later canonical policy both look operational.

---

## 3. Normalized invariant set

The following invariants are accepted as target v2 rules.

### C-01 — Current `main` is the production source of truth

Owner: `CORE / operations`

A production session reads current repository policy and repository state. Chat history is not authoritative state.

Cross-edition pipeline/schema/workflow changes enter production through normal review/merge to `main`.

### C-02 — Correctness priority remains unchanged

Owner: `CORE`

```text
Correctness > Traceability > Coverage > Speed
```

Automation exists to improve repeatability and liveness, not to bypass editorial correctness.

### C-03 — Raw accepted provenance is immutable

Owner: `CORE`

Raw collector output accepted into canonical provenance is append-only/immutable. Derived normalization may change through new versioned artifacts, not mutation of accepted Raw bytes.

### C-04 — Machine checkpoints and Human Gates are different concepts

Owner: `CORE`

A production pipeline may contain many mandatory machine validation checkpoints without creating an equal number of user interaction stops.

This distinction becomes explicit in v2 state and schemas.

### C-05 — Normal production has two Human Gates

Owner: `CORE`

1. **Architecture Review**
2. **Publication Preview**

This target adopts the mature current Special interaction model for all normal Survey production, including Weekly.

No concrete Weekly requirement discovered in Phase 0 justifies retaining Candidate Selection and Freeze as separate routine user stops.

### C-06 — Candidate Selection is an auditable internal checkpoint

Owner: `CORE` mechanics + Profile editorial semantics

Candidate Selection remains explicit, SHA-bound, complete, and reviewable.

It is not a standalone Human Gate.

The Architecture Review surface must make the Selection basis and important exclusions/holds visible so the user approves Selection and Architecture as one editorial decision.

### C-07 — Architecture Review authorizes downstream semantic production

Owner: `CORE`

Architecture approval authorizes deterministic and model-assisted work necessary to produce a publication-ready candidate, as long as work stays within the approved Architecture and Evidence boundaries.

A material change to the approved Architecture requires an Exception Gate or renewed Architecture Review, depending on the eventual implementation shape.

### C-08 — Publication Preview approval is exact-byte authority

Owner: `CORE` gate semantics + `PUBLICATION_PROFILE` artifact realization

Publication Preview occurs only after required machine preflight passes and the exact candidate PDF exists.

Approval is bound to:

- PDF SHA-256;
- approval reference;
- the relevant approved source/provenance basis.

For identical approved bytes, Publication Preview authorizes:

- Visual Review checkpoint record;
- Freeze record;
- work PR merge;
- exact artifact verification;
- public Release.

### C-09 — Visual Review and Freeze are machine/provenance checkpoints, not normal Human Gates

Owner: `CORE` + `PUBLICATION_PROFILE`

The terms remain useful state/provenance concepts. They do not imply a separate user approval after Publication Preview.

### C-10 — Exception Gate is on demand

Owner: `CORE`

Raise an Exception Gate only when a new editorial/publication decision is genuinely needed, including materially insufficient/conflicting Evidence, material approved-Architecture change, semantic change after Publication Preview, provenance loss, or required publication-policy deviation.

Retryable deterministic failure is not a Human Gate.

### C-11 — Start/resume request authorizes deterministic initialization

Owner: `CORE / bootstrap`

A user request to compile a configured/valid edition to a named Human Gate authorizes deterministic initialization and autonomous progression through non-Human stages.

Initialization is not a Human Gate.

### C-12 — A requested Human Gate is a liveness target

Owner: `CORE / orchestration`

Once production begins with a target Human Gate, intermediate deterministic stages must not become accidental conversational stopping points.

The controller should stop only for:

```text
HUMAN_GATE_REACHED
EXCEPTION_GATE_REQUIRED
COMPLETE
```

A technical failure may pause execution internally, but if recoverable under existing authority it should be retried/repaired without requesting editorial approval.

---

## 4. Human Gate drift resolution

### 4.1 Current conflict

Legacy/current Weekly configuration still declares:

```text
human_gate_required_for_selection = true
human_gate_required_for_freeze = true
```

and the W32-derived Weekly design describes Candidate Selection and Freeze as Human Gates.

Current Special configuration and canonical Special policy declare:

```text
Candidate Selection -> internal checkpoint
Architecture Review -> Human Gate 1
Publication Preview -> Human Gate 2
Visual Review -> machine checkpoint
Freeze -> deterministic/provenance transition
Release -> deterministic transition under approved bytes
Exception Gate -> on demand
```

### 4.2 Target decision

**Adopt the Special two-Human-Gate interaction model as the Core v2 default for Weekly, Period, and Thematic production.**

Reasoning:

- Architecture Review is the natural point at which Selection can be judged in context rather than as isolated rankings;
- Publication Preview is stronger than an abstract Freeze approval because it binds the exact reader-visible PDF bytes;
- machine checkpoints remain strict, so reducing conversational gates does not reduce validation;
- the model directly supports the user's desired autonomous-to-gate workflow.

### 4.3 Compatibility handling

Existing frozen Weekly state with old Human flags remains historical provenance.

Do not rewrite W32 or old W33 branch state merely to match v2.

Future v2 state must not infer user approval from legacy flags without an explicit compatibility rule.

---

## 5. State and lifecycle normalization

### 5.1 Lifecycle

Retain the existing coarse lifecycle for the v2 candidate unless implementation reveals a concrete semantic deficiency:

```text
ISSUE_INITIALIZED
DISCOVERY_COLLECTED
CANDIDATES_NORMALIZED
EVIDENCE_REVIEWED
SELECTION_COMPLETE
ARCHITECTURE_ESTABLISHED
DRAFT_COMPLETE
VALIDATED_DRAFT
RELEASE_CANDIDATE
FROZEN
```

Reason:

- both Weekly and Special already use it;
- historical state remains understandable;
- the main defect is ownership/meaning, not necessarily state-name granularity.

Do not rename states for cosmetic v2 branding.

### 5.2 Shared Core state

Core state should own:

- issue identity;
- profile identity;
- lifecycle state;
- machine checkpoint status;
- target Human Gate;
- Human Gate approval references;
- Exception Gate state;
- next action / terminal reason;
- provenance references;
- contract identity.

### 5.3 Profile state

Profile-specific state should own temporal/editorial fields.

Weekly example:

- editorial cutoff;
- rolling window;
- intake split;
- carry-over linkage.

Period example:

- coverage start/end;
- retrospective-as-of;
- period granularity / synthesis obligations.

Thematic example:

- research question/scope identity;
- temporal policy (`OPEN_HISTORY_AS_OF`, `CURRENT_STATE_AS_OF`, or explicitly bounded thematic scope);
- lineage/completeness audit state.

### 5.4 Publication state

Publication Profile should own/reference:

- publication format/template identity;
- final source manifest;
- build/run/artifact identity;
- PDF SHA/page count/preflight;
- Publication Preview approval;
- Visual Review record;
- Freeze record;
- Release manifest/asset verification.

The state need not physically be split into separate files in the first candidate. Ownership must be logically explicit even if one JSON document initially contains namespaced sections.

---

## 6. Research scope and temporal policy normalization

### 6.1 Current conflict

Weekly correctly derives a rolling cutoff-to-cutoff editorial window.

Retrospective Period correctly uses explicit bounded coverage plus a later `retrospective_as_of`.

Current Special manifest validation also requires Thematic editions to provide bounded `coverage.start/end`, which is not a valid general model for historical lineage or broad current-state themes.

### 6.2 Target contract

Every edition has a `research_scope` with at least:

```text
question
inclusion
exclusion
scope_dimensions
temporal_policy
```

Temporal policy is one of the following initial modes:

```text
ROLLING_WINDOW
BOUNDED_PERIOD
OPEN_HISTORY_AS_OF
CURRENT_STATE_AS_OF
```

Additional modes require an explicit later contract change rather than ad hoc date-field interpretation.

### 6.3 Profile mapping

Weekly:

```text
ROLLING_WINDOW
```

Retrospective Period:

```text
BOUNDED_PERIOD
```

Historical Thematic:

```text
OPEN_HISTORY_AS_OF
```

Current-state Thematic:

```text
CURRENT_STATE_AS_OF
```

A Thematic Special may explicitly choose a bounded period if its research question truly calls for one, but bounded coverage is not implied by `THEMATIC` itself.

### 6.4 `retrospective_as_of`

The concept remains valid for retrospective interpretation, but it should become an appropriate `as_of` field under temporal policy rather than a mandatory semantic for every Thematic edition.

---

## 7. Completeness and Materiality normalization

### 7.1 Core rule

Collector success does not imply research completeness.

A stage is not complete merely because it produced many records.

### 7.2 Core owns traceability mechanism

The Core must ensure that material discoveries have explicit downstream disposition.

Target trace:

```text
Discovery / Source Intake
  -> Screening disposition
  -> Evidence / duplicate link / HOLD / explicit exclusion
  -> Candidate Selection disposition
  -> Architecture placement / explicit exclusion
  -> reader-facing narrative / chronology / synthesis / explicit omission rationale
```

This becomes the Materiality Ledger contract.

### 7.3 Profiles own completeness semantics

Weekly completeness asks whether the editorial window plus carry-over obligations have been adequately covered.

Period completeness asks whether material time/actor/technical-layer/source gaps across the bounded period are resolved or explicitly retained as limitations.

Thematic completeness asks whether the major branches, transitions, competing approaches, counterexamples, and primary-source gaps required by the research question are covered.

Series completeness asks whether the volume responsibly fits the shared lineage/dependency graph and whether unresolved cross-volume questions remain visible.

### 7.4 Architecture Review surface

Human Gate 1 must expose at least:

- base/supplemental discovery counts where meaningful;
- Screening disposition counts;
- Evidence counts;
- material holds/exclusions;
- Selection role counts;
- major coverage/completeness obligations and where they landed;
- residual limitations;
- proposed issue thesis and package architecture.

The exact fields may vary by Profile, but the user must be able to audit how broad research was compressed into the proposed issue.

---

## 8. Candidate Selection and editorial-role normalization

### 8.1 Core responsibility

Core owns:

- exact matrix/basis hash binding;
- every row receives a downstream disposition;
- upstream HOLD/REJECT boundaries cannot be silently promoted;
- no selected material silently disappears;
- Selection state remains auditable.

### 8.2 Profile responsibility

Profile owns editorial-role vocabulary and special temporal constraints.

The current shared role set contains:

```text
FEATURE_CORE
SECTION_CORE
PAPER_WATCH
SUPPORTING_EVIDENCE
LATE_BREAKING
CHRONOLOGY
WATCHLIST
HOLD_OUT
EXCLUDE
```

Not every role is universal.

Target classification:

- `HOLD_OUT` / `EXCLUDE`: common disposition candidates;
- `SUPPORTING_EVIDENCE`: broadly reusable;
- `FEATURE_CORE` / `SECTION_CORE` / `PAPER_WATCH`: publication/editorial Profile vocabulary, reusable where desired but not Core ontology;
- `LATE_BREAKING` / `WATCHLIST`: primarily Weekly Profile;
- `CHRONOLOGY`: Period/Weekly may use it; Thematic may instead need lineage/context placement.

Core selection APIs should therefore validate against a Profile-provided allowed role set rather than hard-code current Weekly vocabulary forever.

### 8.3 Foundations `Core / Bridge / Context`

The Foundations planning classification is not automatically the same object as Candidate Selection roles.

It describes **lineage/materiality role in a research series**, so its natural owner is Thematic/Series research state or edition-specific Evidence View.

Do not overload one `role` field to mean both publication placement and historical lineage significance.

---

## 9. Architecture normalization

### 9.1 Core responsibility

Core owns:

- selected Evidence → Architecture Input binding;
- exact Selection/Matrix SHA basis;
- primary/supporting assignment consistency;
- evidence boundary propagation;
- each required primary Evidence placement;
- approved/proposed status and approval reference;
- generic package identity/order.

### 9.2 Profile responsibility

Profile owns:

- required architecture questions;
- admissible package/editorial roles;
- completeness summary requirements;
- synthesis obligations;
- temporal/lineage constraints.

Examples:

Weekly:
- weekly thesis;
- Late Breaking handling;
- why-this-week;
- carry-over disposition.

Period:
- period-wide trajectory;
- chronology;
- cross-month/annual reclassification;
- final retrospective synthesis.

Thematic:
- lineage/branch structure;
- inheritance vs abandonment;
- parallel/competing approaches;
- explicit historical attribution boundaries.

### 9.3 Publication responsibility

Publication Profile owns page budget/layout constraints, not the research Core.

Architecture may consume those constraints as inputs, but the Core should not assume all profiles have the same target page count or section style.

---

## 10. Drafting and synthesis normalization

### 10.1 Structured drafting remains canonical

Owner: `CORE`

Models consume bounded Draft Packages and return structured Article Draft Results rather than uncontrolled final LaTeX.

Evidence references, attribution mode, limitations, must-cover requirements, and source boundaries remain machine-validatable.

### 10.2 Reader-facing prose boundary

Owner: `CORE` editorial correctness + `PUBLICATION_PROFILE`

Published prose must not expose internal production vocabulary when it is not reader-relevant.

Claim-strength/boundary information remains reader-visible where it helps interpretation; internal Candidate/runner/state terminology remains provenance-side.

### 10.3 Synthesis

Core owns:

- synthesis input based only on validated article bytes/Evidence;
- no introduction of unsupported new external facts;
- exact input/prompt/result provenance.

Profiles own the required kind of synthesis.

Weekly may require issue signals/frontmatter.

Period requires cross-article retrospective synthesis unless Architecture explicitly and validly changes that policy.

Thematic requires research-question/lineage synthesis rather than a period summary.

Publication Profile determines where/how synthesis is rendered.

---

## 11. Subject/entity attribution contract

Owner: `CORE`

Issue #191 is promoted from a Special repair finding into a generic evidence/claim invariant.

A technical attribute extracted from a source must be bound to its subject/entity.

Comparator, related-product, table-neighbor, historical-reference, navigation, or category values cannot be treated as target-entity attributes solely by proximity.

If comparator values are retained, comparator identity must be explicit.

This contract applies to Evidence extraction and to later Technical Notes/reader-facing rendering.

Historical Mistral/Jamba/Ministral cases become regression candidates during Phase 2.

---

## 12. Publication Profile normalization

### 12.1 Research/editorial Profile is separate from Publication Profile

An edition's research scope must not be coupled to one document layout.

Examples:

```text
Weekly research profile + magazine publication profile
Period research profile + long-form Special publication profile
Thematic research profile + long-form Special publication profile
```

Future publication styles may be added without creating new research pipelines.

### 12.2 Shared publication invariants

Publication Profile must preserve:

- deterministic source assembly;
- source/file hash manifests;
- bibliography/reference integrity;
- LuaLaTeX/Biber success;
- unresolved citation/reference failure;
- configured layout/log warning policy;
- render-first Visual QA;
- exact PDF SHA binding;
- reproducibility or exact-artifact provenance;
- Freeze/source/PDF integrity;
- release asset digest verification.

### 12.3 Layout policy

Weekly/long-form templates, columns, page budgets, reference pagination, Technical Notes layout, and visual compaction policy are Publication Profile configuration/implementation concerns.

Historical layout-repair ancestry must not become Core research semantics.

---

## 13. Release identity normalization

### 13.1 Current authority

`docs/release-identity-policy.md` is treated as the target current public identity rule because it explicitly supersedes routine revisioned public releases after the named legacy issues.

### 13.2 Target rule

A normal published issue has issue-only identity.

Weekly:

```text
weekly/<issue>
```

Special:

```text
special/<slug>
```

Internal source revisions remain provenance and do not form public release identity.

### 13.3 Preserve source commit vs release anchor distinction

The useful integrity distinction in `docs/weekly-release-process.md` remains valid even though its revision terminology is stale:

```text
release tag / anchor commit
!=
frozen source commit
```

The release metadata must separately record:

- release anchor identity;
- frozen source commit;
- exact PDF SHA-256.

Do not discard this mechanism while normalizing public tag names.

### 13.4 Corrections

Post-publication correction is exceptional.

Normal editing must not be implemented as `v0.x` public releases.

A material post-release defect requires explicit correction/erratum policy and Human approval while preserving original provenance.

### 13.5 Legacy

Existing legacy public tags/manifests remain untouched.

Old revisioned release workflows may remain as `LEGACY_REPLAY` until callers/recovery requirements are audited, but future canonical production does not use them.

---

## 14. Visual Review / Freeze / Release authorization normalization

Target authority chain:

```text
machine preflight passed
  -> exact Publication Preview PDF exists
  -> HUMAN: Publication Preview approval
  -> machine Visual Review record for identical bytes
  -> Freeze record / release manifest
  -> merge approved work
  -> exact artifact re-fetch / digest verification
  -> public Release
```

Rules:

- no semantic modification after Publication Preview approval without a new editorial decision;
- layout-only repair occurs before Publication Preview approval;
- deterministic release retry using identical frozen bytes does not require a new Human Gate;
- recovery primitives may remain available but cannot accept new independent Human authority that bypasses the Publication Preview record.

This is a Core gate contract implemented through Publication Profile workflows.

---

## 15. Bootstrap and cross-session normalization

### 15.1 Existing Special rule to generalize

Current Special bootstrap already establishes the desired behavior:

- target edition + requested Human Gate is sufficient;
- absent edition may be initialized deterministically;
- existing edition resumes from repository state;
- initialization is not a Human Gate;
- production advances autonomously to requested Human Gate;
- repository state must support another session without chat history.

### 15.2 Target generic bootstrap

The v2 bootstrap should resolve:

```text
edition ID / slug
  -> research profile
  -> temporal policy
  -> publication profile
  -> canonical source/survey/work paths
  -> current state or initialization plan
  -> requested target Human Gate
```

Weekly and Special naming/branch conventions may remain different if operationally useful; the resolver exposes them as profile/edition descriptors rather than requiring separate state engines.

### 15.3 W33 rule

The existence of a legacy W33 work branch does not require a v2 migration bootstrap.

W33 v2 production may compare or selectively reuse artifacts only when they independently satisfy v2 provenance/contract requirements.

---

## 16. Orchestration contract

### 16.1 Core controller

Add a generic orchestration controller, provisionally `advance-to-gate`.

It should not contain all production logic. It resolves state and dispatches existing/normalized deterministic primitives.

Required concepts:

- `target_gate`;
- `current_stage`;
- `next_action`;
- `terminal_reason`;
- `exception_gate_state`;
- exact artifact/provenance inputs for next action.

### 16.2 Workflows

GitHub Actions workflows should increasingly become thin execution/control surfaces around canonical Python contracts.

Avoid a monolithic workflow with dozens of edition conditionals.

### 16.3 Safe control

Existing allowlisted assistant-control mechanisms remain an operational safety layer.

Canonical workflow names/inputs should be stabilized before allowlists are substantially rewritten.

---

## 17. Contract provenance

### 17.1 Problem

Current artifacts record many prompt/task/source hashes but do not bind the complete production semantics to one explicit pipeline/quality contract identity.

This makes it harder to tell whether two otherwise similar runs were produced under different Human Gate, completeness, or temporal policies.

### 17.2 Target fields

Every initialized v2 edition state should record at least:

```yaml
contract:
  pipeline_contract_version: "2.0-rc1"
  pipeline_contract_sha256: "..."
  quality_contract_version: "2.0-rc1"
  quality_contract_sha256: "..."
  research_profile: "WEEKLY | RETROSPECTIVE_PERIOD | THEMATIC"
  research_profile_version: "..."
  research_profile_sha256: "..."
  publication_profile: "..."
  publication_profile_version: "..."
  publication_profile_sha256: "..."
```

The exact file layout is Phase 3 work. The invariant is that the semantic contract is hash-identifiable and immutable for a given accepted artifact/run.

### 17.3 Contract updates during an edition

A material contract change during active production cannot silently rewrite the basis of already accepted upstream artifacts.

Possible strategies include:

- continue current edition under its initialized contract;
- explicitly migrate/revalidate affected artifacts under a new contract;
- raise an Exception Gate if the change alters an already approved editorial/publication decision.

The first v2 candidate should prefer simple explicit revalidation over complex transparent migration.

---

## 18. Series Research Layer contract

Series state is outside the normal per-edition lifecycle.

It owns:

- series research question/thesis;
- shared lineage graph;
- volume dependencies;
- source/reusable-Evidence references;
- unresolved lineage questions/research debt;
- merge/split/insert/resequence decisions;
- cross-volume Evidence usage;
- dated frontier snapshots where required.

Per-edition production remains governed by Core + a research Profile + Publication Profile.

A volume may use the shared corpus, but its materiality/lineage interpretation remains edition-specific.

No routine third Human Gate is introduced merely because an edition belongs to a series. A distinct Series Architecture Review may be raised when a genuinely series-level decision is required.

---

## 19. Reusable Evidence contract

Target model:

```text
Canonical Source
      ↓
Reusable Evidence
      ↓
Edition-specific Evidence View
      ↓
Edition-specific editorial interpretation
```

Reusable Evidence may contain:

- stable source identity/hash;
- bibliographic metadata;
- author/date;
- directly verified method facts;
- directly verified experimental facts;
- directly supported limitations.

Edition-specific Evidence View contains:

- relevance to current research question;
- materiality disposition;
- lineage role;
- Core/Bridge/Context where applicable;
- inheritance/abandonment interpretation;
- competing-branch relation;
- reader-facing synthesis intent.

Invariant:

> Facts may be reused; historical significance and lineage interpretation must be re-evaluated for the edition's question.

---

## 20. Legacy compatibility contract

### 20.1 Frozen artifacts

Never mutate frozen source/PDF/release provenance merely to conform to v2 schemas or names.

### 20.2 Intermediate legacy state

Exact compatibility with every old intermediate state is not a v2 requirement.

Adapters are justified only when a real audit/replay/active-production need exceeds their complexity cost.

### 20.3 Repair chains

Historical versioned repair chains may be retired from future hot path only after:

- callers/workflows are known;
- generic/profile/publication invariants are extracted;
- regression tests are moved to canonical implementations;
- any required exact-replay capability is isolated.

### 20.4 Historical documents

Superseded design documents remain in Git history and may remain in-repository when useful, but must be labeled historical/superseded so future sessions cannot mistake them for current authority.

---

## 21. Drift resolution table

| Topic | Current conflicting surfaces | v2 owner | Target decision | Legacy handling |
|---|---|---|---|---|
| Human Gates | Weekly Selection/Freeze vs Special Architecture/Preview | `CORE` | 2 gates: Architecture Review + Publication Preview | old state preserved |
| Candidate Selection | Weekly Human approval vs Special internal checkpoint | `CORE` + Profile | internal auditable checkpoint reviewed at Architecture | legacy approval metadata readable |
| Visual Review | historical Human review workflows vs current Special machine checkpoint | `CORE`/Publication | machine/provenance checkpoint under exact Preview approval | historical workflows replay-only |
| Freeze | Weekly Human gate vs Special deterministic authorized transition | `CORE`/Publication | not separate normal Human Gate | frozen historical records unchanged |
| Release identity | revisioned tags vs issue-only policy | Publication | issue-only after named legacy releases | legacy tags untouched |
| Lifecycle | duplicate Weekly/Special schemas | `CORE` | preserve shared coarse lifecycle, merge state semantics | old schemas readable |
| Calendar/scope | Weekly rolling vs Special bounded coverage | Profiles | explicit temporal policy | historical fields preserved |
| Thematic scope | bounded coverage forced by Special validator | `THEMATIC_PROFILE` | open/current-as-of allowed | old thematic manifests remain valid legacy inputs |
| Completeness | collector success/local checks vs coverage requirement | Profiles + Core ledger | profile completeness + material traceability | historical gaps documented, not rewritten |
| Materiality | dispersed dispositions | `CORE` | Materiality Ledger | backfill only when useful for tests/audit |
| Architecture roles | one hard-coded role set | Profiles + Core mechanics | Profile supplies editorial role vocabulary | current roles supported initially |
| Drafting | shared structured contracts | `CORE` | retain | none needed |
| Synthesis | Weekly/Period behavior mixed in finalizers | Core + Profiles | shared evidence-bounded synthesis, profile-specific requirement | historical output unchanged |
| Publication assembly | separate finalizers/checks | Publication + Profile hooks | shared primitives, distinct publication configuration | old builders replay-only eventually |
| Bootstrap | Special mature, Weekly separate | `CORE` | generic edition/profile bootstrap | old entrypoints can wrap new resolver |
| Orchestration | stage workflows / conversational continuation | `CORE` | `advance-to-gate` | workflows remain recovery primitives |
| Contract identity | absent | `CORE` | SHA/version-bound contract identity | legacy marked as pre-v2 |
| Series state | planning memo only | `SERIES_LAYER` | explicit cross-volume state | no impact on standalone issues |

---

## 22. Candidate canonical document set

Phase 3 should avoid proliferating many overlapping policy documents. A minimal target documentation set is:

```text
docs/survey-production-core.md
  canonical shared lifecycle, gates, provenance, orchestration, materiality

docs/profiles/weekly.md
  Weekly research/editorial profile

docs/profiles/retrospective-period.md
  bounded Period profile

docs/profiles/thematic.md
  thematic/lineage profile

docs/publication-profiles/<profile>.md
  Weekly magazine / long-form publication behavior

docs/series-research.md
  generic series layer contract
```

Existing rich guides such as annual/half-year and Foundations remain valuable domain-specific extensions; they should point to rather than duplicate the Core contract.

Exact paths/names are implementation choices. The important point is one clear authority chain.

---

## 23. Phase 1 decisions that are intentionally not implementation-complete

This document fixes ownership and semantics but does not yet choose every JSON field or Python class.

Still open for Phase 2/3 design:

- exact common pipeline-state schema shape;
- whether profile metadata is embedded or referenced by hash;
- precise Materiality Ledger schema;
- exact shared Evidence corpus storage path;
- exact Thematic completeness representation;
- exact Review Finding / Repair Set schema;
- exact generic workflow consolidation boundary;
- exact migration strategy for active pre-v2 branches beyond the W33 non-requirement;
- whether `FROZEN` remains final lifecycle state while Release is tracked separately or whether a later `RELEASED` state is worth adding after compatibility analysis.

These must not be resolved by accidental implementation convenience.

---

## 24. Phase 1 conclusion

The principal normalization is:

```text
shared semantic mechanisms already exist
        ↓
make Core ownership explicit
        ↓
separate research Profiles from Publication Profiles
        ↓
normalize all normal user interaction to
Architecture Review + Publication Preview
        ↓
add materiality/completeness/orchestration/contract identity
        ↓
isolate legacy repair/release compatibility
```

This resolves the current conceptual conflict without requiring a greenfield rewrite.

The next phase should mine the fifteen completed Special editions and major Weekly/Special Human Review Issues to convert accumulated repair history into:

- explicit invariants;
- regression fixtures;
- Core/Profile/Publication ownership;
- legacy-only variance.

Only after that distillation should the Phase 3 implementation vertical slice be fixed, so the new Core does not accidentally omit lessons presently trapped inside repair scripts and edition-specific tests.

## 25. WU-002 exit decision

WU-002 exit condition is satisfied when this document is committed and checked against current `main` because:

- each major known drift has a target owner and decision;
- current canonical intent is distinguishable from legacy compatibility;
- Human Gate semantics are normalized;
- public Release identity is normalized while retaining source-commit/anchor integrity;
- research scope is separated from temporal policy;
- completeness mechanism vs profile semantics are separated;
- bootstrap/orchestration authority is explicit;
- contract provenance is defined as a required future invariant;
- unresolved implementation details are explicitly deferred rather than silently guessed.

The next work unit is **Phase 2 — Historical Knowledge Distillation**.
