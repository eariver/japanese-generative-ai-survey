# Automotive E/E experiment: generalization findings

Status: **EXPERIMENTAL / Architecture Review gate reached / production AI pipeline unchanged**

This note records what the Automotive E/E architecture experiment has demonstrated about the existing survey pipeline. It is deliberately **not** a migration plan for the production generative-AI survey. The AI survey remains the repository's primary product and its existing contracts remain authoritative.

## 1. Experiment boundary

- Branch: `experiment/automotive-ee-architecture-special`
- Issue: `SP-automotive-ee-architecture-2023-2026`
- Edition: `THEMATIC`, 2023-08-18 through 2026-08-18
- Target/max pages: 48 / 64
- Production AI collector config, prompts, schemas, deterministic stage implementations and pipeline controller: **unchanged**
- Production lifecycle state for this experiment: **not advanced by the probes**

The experiment asks one question:

> Which parts of the current Special pipeline are genuinely technical-survey machinery, and which parts are generative-AI or weekly-edition context that should remain profile-owned?

The safe direction demonstrated so far is **profile extraction around an AI-first stable core**, not conversion of the repository into a generic framework.

## 2. Source Intake — shared mechanics, profiled source semantics

The production `scripts/source_intake.py` was reused unchanged through an experiment adapter/profile.

Stable intake shape:

- arXiv: 50 unique papers from 6 successful queries
- GitHub Releases: 53 releases from 4 repositories
- official pages: 9 successful snapshots
- acquisition gaps: 4
  - AUTOSAR: 3 TLS chain-validation failures on the hosted runner
  - ISO: 1 HTTP 403
- combined Screening records: 112

No TLS verification was disabled and no access restriction was bypassed. Retrieval failures remain explicit coverage gaps.

### Finding S1

Collector mechanics are broadly reusable. Domain-owned inputs are:

- query/watch lists
- repository lists
- official-page lists
- collection-window semantics
- coverage policy
- transport policy
- provenance labels

The first hard-coded AI/weekly seam was provenance text referring to the production Source Intake config/weekly plan.

## 3. Screening normalization — `page_role` is source semantics

The production `scripts/build_screening_index.py` normalized all 112 Automotive records unchanged.

Canonical behavior classified ordinary HTML pages as `official-index-snapshot`. That matches many AI newsroom/watchlist sources but is wrong for a standard/specification page that is already the evidence item.

The experiment introduced profile metadata:

- `page_role = INDEX`
- `page_role = ITEM`

With identical Raw input:

- canonical: 112 records, 9 `official-index-snapshot`, 5 batches
- profiled: 112 records, 9 `official-page-snapshot`, 6 batches

### Finding S2

`INDEX | ITEM` belongs in source/profile semantics. The production AI default can remain `INDEX`; no domain fork of the normalizer is required conceptually.

## 4. Screening decisions — shared result schema, domain editorial context

The existing Screening result structure was reusable unchanged:

- `KEEP | MAYBE | DROP | INSPECT`
- confidence/reason
- duplicate grouping
- verification targets
- topic-lane identifiers

The production Screening prompt is not domain-neutral because it embeds generative-AI relevance, weekly `why_now`, and the production A–L lane meanings.

Automotive profile lanes:

- A — physical/zonal topology and wiring/I/O boundaries
- B — central/HPC compute and mixed criticality
- C — in-vehicle networking
- D — runtime/middleware/service/data contracts
- E — development/integration/validation lifecycle
- F — safety/security/isolation
- G–L — reserved

Pinned Screening result:

- KEEP: 41
- MAYBE: 19
- DROP: 52
- retained for Evidence: 60

Retained source mix:

- papers: 33
- GitHub releases: 18
- official item pages: 9

### Finding S3

Screening structure is shared machinery. Editorial relevance, `why_now` semantics and lane meanings are profile context.

## 5. Evidence Task construction — shared unchanged

The experiment converted the 60 retained Screening records into a verification queue and invoked production `scripts/build_evidence_tasks.py` unchanged.

Result:

- Evidence Tasks: 45
- `VERIFY_ITEM`: 42
- `VERIFY_SERIES`: 3
- `INSPECT_INDEX`: 0
- missing Screening coverage: 0
- duplicate Screening coverage: 0

The 60→45 reduction comes from three coherent release series (VSS, vSomeIP, S-CORE), not a target-count quota.

### Finding E1

Evidence Task construction is genuinely shared deterministic machinery once Source/Screening item-vs-index semantics are correct.

## 6. Evidence contract — shared provenance model, profiled artifact ontology

The following production Evidence concepts worked unchanged across automotive standards, specifications, OSS platforms, middleware and research papers:

- runner provenance
- source classes
- evidence classes
- temporal Events
- claims, metrics and limitations with source references
- verification-target resolution
- editorial recommendation state

The first schema-level AI assumption was the closed `artifact.artifact_type` enum.

The experiment generated a strict Automotive Evidence schema from the production schema shape with this ontology:

- `STANDARD`
- `SPECIFICATION`
- `PLATFORM`
- `MIDDLEWARE`
- `REFERENCE_IMPLEMENTATION`
- `PROTOCOL`
- `ARCHITECTURE_PATTERN`
- `CONSORTIUM_INITIATIVE`
- `PAPER`
- `FRAMEWORK`
- `PRODUCT`
- `OTHER`

The production schema itself was not widened or modified.

### Finding E2

Keep a strict artifact ontology, but generate/select it from the domain profile at execution-package build time. Do **not** globally replace the production AI enum with an unconstrained string.

## 7. Complete Evidence workload — 45/45 validated

All 45 Evidence Tasks now have exactly one result card.

Every result was revalidated against:

1. exact pinned Evidence Task bytes/SHA-256;
2. exact pinned Automotive Evidence prompt bytes/SHA-256;
3. unchanged production `scripts/validate_evidence_run.py` invariants;
4. generated strict Automotive Evidence Run/Card schemas.

Complete set:

- VERIFIED: 30
- PARTIAL: 15
- CANDIDATE recommendation: 29
- HOLD: 8
- INSPECT_MORE: 8

Artifact types:

- PAPER: 33
- MIDDLEWARE: 3
- SPECIFICATION: 3
- CONSORTIUM_INITIATIVE: 2
- PLATFORM: 2
- PROTOCOL: 1
- STANDARD: 1

Source classes:

- PRIMARY_PAPER: 34
- PRIMARY_REPOSITORY: 19
- PRIMARY_OFFICIAL: 10

The PARTIAL cards are intentional evidence boundaries, not pipeline failures. Abstract-only or incomplete technical evidence was not promoted to VERIFIED merely to complete the set.

### Finding E3

The Evidence provenance/verification model survived a complete non-AI workload. Domain specificity is concentrated in the verification prompt and artifact ontology, not in the core evidence graph.

## 8. Candidate Matrix — shared unchanged on all 45 rows

The complete reviewed Evidence set was passed to production `scripts/build_candidate_matrix.py` unchanged.

Result:

- rows: 45
- READY_WITH_CAVEAT: 29
- HOLD: 16
- MAIN_EVENT: 40
- TIMING_UNRESOLVED: 5

One weekly wording leak remains: when `why_now_confirmed=false`, the production builder may emit `Weekly why-now relevance is not confirmed.`

### Finding C1

Candidate comparison mechanics are shared. `why_now` wording/meaning should eventually be supplied by edition context.

## 9. Candidate Selection — role safety shared, themes need an overlay

A full Selection proposal was built for all 45 matrix rows and validated by production `scripts/candidate_selection_gate.py` unchanged.

Selection proposal:

- status: `PENDING_APPROVAL` in the experiment artifact
- UNASSIGNED: 0
- FEATURE_CORE: 2
- SECTION_CORE: 7
- SUPPORTING_EVIDENCE: 16
- CHRONOLOGY: 3
- EXCLUDE: 1
- HOLD_OUT: 16
- positive Architecture inputs: 28

The only CANDIDATE explicitly excluded was the power-packet/sensorless `Modular Drive` paper because it is credible but peripheral to the survey's E/E responsibility-boundary thesis.

The existing role safety rules are useful across domains, but the Selection structure does not preserve the Automotive A–F topic axes into Architecture Input. The experiment therefore keeps thematic assignments in a separate SHA-bound overlay rather than adding unvalidated fields to the shared Selection object.

Theme participation among the 29 Candidate rows:

- A: 4
- B: 15
- C: 9
- D: 17
- E: 11
- F: 10

### Finding C2

The shared role model is reusable. Domain theme taxonomy and theme-to-candidate assignments are profile/overlay context. A future abstraction should preserve this context explicitly into Architecture generation rather than expanding the generic role enum.

## 10. Architecture Input — shared mechanics, edition constraints outside the core

A synthetic approval exists **only inside the dry-run artifact** to exercise production `scripts/build_architecture_input.py`; no human approval or production lifecycle advancement was recorded.

The shared builder accepted the complete Selection unchanged and produced:

- selected for Architecture: 28
- excluded/not selected: 17

Two edition-specific seams are visible:

- default page target/max is fixed to 16/24
- `this_week_summary_written_last` is weekly-named and later required by the Architecture validator

For the Automotive experiment these are overlaid as:

- page target/max: 48/64
- summary semantics: retrospective Executive Synthesis finalized after package drafts stabilize

## 11. Full-Evidence Architecture Proposal v0.2 — Human Gate reached

The early PoC architecture is superseded for review purposes by the full-Evidence v0.2 profile/proposal.

The v0.2 proposal uses 9 packages and exactly 48 planned pages:

1. **Front Matter / 読み方とEvidence境界** — 2p
2. **Lead — 『中央集約』ではなく責務境界の再設計** — 5p
3. **Compute — HPC統合とmixed-criticalityの現実** — 7p
4. **Network Fabric — TSN EthernetとCAN XLの役割分担** — 7p
5. **Service & Data — ECU境界から契約境界へ** — 7p
6. **Open Platform — S-COREが示す共通実装への移行** — 6p
7. **Lifecycle — SDVではintegration/diagnostics/validationもArchitectureになる** — 7p
8. **Cross-cutting Deep Dive — Safety / Security / Trust Boundary** — 4p
9. **References / Evidence Map / 未解決事項** — 3p

The plan was validated by production `scripts/validate_issue_architecture.py` unchanged:

- plan status: `PROPOSED`
- packages: 9
- planned pages: 48
- primary-required items: 12
- primary-covered items: 12
- missing primary items: 0
- duplicate primary items: 0

The validator-required legacy field `this_week_summary_written_last=true` is retained only for compatibility; the experiment semantics overlay explicitly defines it as retrospective Executive Synthesis behavior.

### Finding A1

Architecture package coverage, Evidence-boundary propagation, primary/support separation and page accounting are reusable. Page budget, domain theme taxonomy and summary semantics are edition/profile context.

## 12. Proven abstraction boundary

```text
shared deterministic machinery — empirically reusable
  ├─ HTTP / arXiv / GitHub collection mechanics
  ├─ Raw provenance and hashing
  ├─ Screening record/batch mechanics
  ├─ Screening result schema
  ├─ Evidence Task construction
  ├─ Evidence invariant validation
  ├─ Evidence source/evidence-class model
  ├─ Candidate comparison mechanics
  ├─ Candidate Selection safety validation
  ├─ Architecture Input mechanics
  └─ Architecture coverage/boundary/page validation

survey/domain profile — empirically domain-owned
  ├─ issue/time-window semantics
  ├─ source queries/watchlists
  ├─ source page role: INDEX | ITEM
  ├─ transport/coverage policy
  ├─ Screening editorial relevance
  ├─ topic/theme taxonomy
  ├─ Evidence verification prompt/context
  ├─ Evidence artifact-type ontology
  ├─ active Selection role subset
  ├─ theme continuity into Architecture
  ├─ page budget
  └─ summary/section naming semantics

production/lifecycle binding — intentionally not generalized yet
  ├─ accepted Source Intake persistence
  ├─ accepted Screening persistence
  ├─ complete Evidence acceptance into canonical lifecycle
  ├─ Selection approval persistence
  ├─ state transitions
  ├─ Architecture approval persistence
  └─ drafting/publication gates

production AI profile
  └─ remains authoritative and must preserve current behavior by default
```

## 13. Guardrails before any production refactor

Do not change the production pipeline merely because the Automotive experiment passes.

Any future abstraction should require:

1. Existing AI weekly/monthly/half-year/annual tests remain byte/behavior compatible where intended.
2. AI remains the default/authoritative repository product; generic context is opt-in.
3. Missing profile fields fail closed or preserve the exact existing AI default.
4. Strict AI ontologies are not weakened for cross-domain convenience.
5. Prompt/schema/profile inputs remain SHA-bound in execution packages.
6. Retrieval failures remain visible; no insecure transport fallback is introduced.
7. Theme/context transport is added without mixing domain-specific semantics into deterministic validators.
8. Lifecycle/acceptance code is generalized only after a separate experiment proves identical state-transition semantics.

## 14. Current gate

The experiment has reached the configured **Architecture Review human gate**.

- Architecture Proposal: `v0.2`
- status: `PROPOSED`
- validator: passed
- production lifecycle advanced: no
- Architecture approval recorded: no
- drafting started: no

The next action after explicit Architecture approval would be to test drafting/claim-validation/rendering behavior, again in experiment-only form before considering any production abstraction.
