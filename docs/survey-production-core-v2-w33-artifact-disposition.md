# Survey Production Core v2 — W33 Legacy Artifact Reference Policy

Status: `PHASE 3 SUPPORTING POLICY / optional legacy fixture`  
Established: 2026-08-22 JST  
Revised after second audit: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Legacy fixture branch: `weekly/2026-W33-work`

## 1. Purpose

W33 already has a substantial legacy-pipeline Release Candidate. Its existence is useful, but it must not redefine the purpose of the first Weekly v2 Pilot.

The primary W33 Pilot objective is:

> **Weekly Profile First Production Validation**

The legacy W33 RC is therefore an **optional benchmark/provenance fixture**.

It may be used to:
- compare research breadth and editorial decisions;
- reuse immutable factual inputs when independently safe;
- provide regression examples;
- explain differences between legacy and v2 output.

It is **not** required to prove:
- automatic v1 → v2 state migration;
- seamless resume from legacy intermediate state;
- artifact-by-artifact compatibility;
- preservation of legacy editorial decisions;
- reuse of any legacy artifact at all.

If clean regeneration under v2 is simpler or produces clearer provenance, regeneration is preferred.

## 2. Legacy fixture facts

The legacy branch records:
- `lifecycle_state = RELEASE_CANDIDATE`;
- Raw, candidate inventory, Evidence, Selection, Architecture, Draft, validation, PDF build and Visual Review passed;
- Freeze pending;
- legacy candidate PDF page count: 14;
- legacy candidate PDF SHA-256:

```text
066cb28f2dd3401bdc79849a6e2fd2b05ce0137b939d24826481f740966f9017
```

The branch also contains content-addressed collector Raw data and `raw-index.json`.

These facts make the branch valuable historical evidence. They do not create a v2 compatibility requirement.

## 3. Decision vocabulary when reuse is considered

The following vocabulary applies **only when a Pilot or implementation explicitly considers reusing a legacy artifact**.

### REUSE

Exact bytes are contract-neutral and may enter v2 after identity/hash verification.

### REVALIDATE

Potentially useful factual/provenance content must pass v2 validation before use.

### REGENERATE

Underlying facts/provenance may inform the run, but the legacy artifact itself encodes obsolete semantics and is rebuilt under v2.

### REJECT

Artifact must not become authoritative v2 input; it may remain a comparison fixture.

These are safe-disposition choices, not mandatory steps in every W33 run.

## 4. Optional safe-reuse table

| Artifact class | If reuse is attempted | Reason / boundary |
|---|---|---|
| Accepted collector Raw bytes | `REVALIDATE` | factual/provenance input; verify path/SHA/bytes/window/source provenance |
| `raw-index.json` | `REVALIDATE` | useful content-addressed inventory but produced under legacy acceptance/state |
| Collector run metadata | `REVALIDATE` | retain legacy contract identity as provenance; do not pretend v2 generated it |
| Weekly carry-over artifacts | `REVALIDATE` | carry-over remains Weekly semantics but v2 completeness/materiality must re-evaluate obligations |
| Grok/X trend Raw inputs | `REVALIDATE` | timing/currentness must be re-derived from v2 Weekly Profile |
| Legacy Screening | `REGENERATE` | contains `why_now` and fixed Weekly lanes; no v2 Materiality basis |
| Legacy Evidence factual fields | `REVALIDATE` | source/claim/metric/limitation facts may be reusable if v2 correctness checks pass |
| Legacy Evidence `why_now`/editorial fields | `REJECT` as v2 authority | edition significance belongs to fresh Weekly Edition Evidence View |
| Legacy Candidate Matrix / Selection | `REGENERATE` | legacy timing/role/Human Gate semantics differ |
| Legacy Architecture | `REGENERATE` | not bound to v2 Materiality/Completeness/Architecture contract |
| Legacy Architecture approval | `REJECT` as v2 approval | v2 Human Gate 1 must bind exact v2 basis |
| Legacy Draft / Synthesis / final claim review | `REGENERATE` as canonical semantic artifacts | upstream semantic basis changes |
| Legacy TeX/PDF/Visual Review | `REJECT` as v2 release authority; retain fixture | exact bytes authorize only the legacy semantic path |
| Legacy `pipeline-state.json` | `REJECT` as v2 authority | state/gate contract differs |

## 5. Stage ownership if optional reuse is implemented

Reuse support must follow the production stage it belongs to. Do not concentrate all compatibility behavior in Selection/Architecture tooling.

```text
WU-006 / discovery + Screening
  - Raw/provenance import or revalidation, if used
  - carry-over/current-context revalidation, if used

WU-007 / Evidence + Materiality
  - factual Evidence revalidation, if used
  - fresh Edition Evidence View regardless

WU-008 / Matrix + Selection + Architecture
  - semantic comparison report
  - fresh v2 Matrix/Selection/Architecture
```

A work unit may implement **zero** W33-specific reuse code if the general v2 path can simply consume/recollect the required factual inputs more safely.

## 6. W33 acceptance criteria do not include reuse

W33 is accepted as the first Weekly Profile Pilot based on whether v2 can correctly produce the issue under the new contract.

Required concerns include:
- correct W33 editorial window and carry-over handling;
- broad/current Source Intake with explicit completeness status;
- one explicit disposition for material information;
- correct factual Evidence and attribution;
- internal Candidate Selection;
- Architecture Review with visible research compression and limitations;
- valid post-Architecture semantic/publication path;
- normal two-Human-Gate mechanics.

None of the following is a pass/fail criterion:
- number of legacy artifacts reused;
- successful legacy state translation;
- identical Selection to legacy W33;
- identical Architecture/PDF to legacy W33.

## 7. Comparison remains useful

After W33 v2 production, compare against the legacy fixture when useful:
- source surfaces;
- Screening differences;
- factual Evidence differences;
- material candidates gained/lost;
- Selection/Architecture differences;
- completeness limitations;
- article hierarchy/thesis;
- claim boundaries/references/layout;
- final PDF structure.

A difference is evidence, not automatically a defect.

## 8. Safety rule

Do not overwrite or repurpose `weekly/2026-W33-work` as the v2 work branch.

Any legacy bytes used by v2 must be hash-verified and referenced/imported without mutating the fixture.

## 9. Authority

This revised policy supersedes the earlier interpretation of W33 as a required compatibility-boundary Pilot.

The authoritative rule is:

```text
W33 = Weekly Profile First Production Validation
legacy W33 RC = optional benchmark/provenance fixture
legacy reuse = permitted optimization, never acceptance criterion
```
