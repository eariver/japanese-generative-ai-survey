# Survey Production Core v2 — W33 Legacy Artifact Disposition

Status: `PHASE 3 CORRECTION / Pilot compatibility boundary`  
Established: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Legacy fixture branch: `weekly/2026-W33-work`

## 1. Purpose

W33 already exists as a substantial legacy-pipeline production candidate. Its recorded state is `RELEASE_CANDIDATE`: Raw, candidate inventory, Evidence, Selection, Architecture, drafting, claim/chronology validation, LaTeX build and Visual Review are passed; Freeze remains pending. The legacy candidate PDF is 14 pages with SHA-256:

```text
066cb28f2dd3401bdc79849a6e2fd2b05ce0137b939d24826481f740966f9017
```

This makes W33 too valuable to discard as if no production work existed, but it does **not** justify making perfect automatic v1-state migration a generic Core v2 requirement.

The Pilot policy is therefore artifact-level compatibility:

```text
legacy W33 artifact
  -> inspect exact provenance + semantic contract
  -> REUSE | REVALIDATE | REGENERATE | REJECT
  -> enter v2 only through an explicit recorded disposition
```

## 2. Disposition vocabulary

### REUSE

The exact bytes are contract-neutral enough to enter v2 directly after identity/hash verification. No semantic reinterpretation is required.

### REVALIDATE

The artifact contains potentially reusable information, but it must pass v2 provenance and semantic validation before becoming an input to v2. If validation fails, regenerate or reject the affected unit.

### REGENERATE

The underlying source facts/provenance may inform the new run, but the artifact itself encodes legacy semantics and must be reconstructed under the v2 contract.

### REJECT

The artifact cannot be an authoritative v2 input. It may remain an immutable comparison/regression fixture.

## 3. W33 fixture facts

The legacy branch contains, among other surfaces:

- immutable collector Raw trees and `raw-index.json`;
- carry-over artifacts;
- Screening results;
- Evidence runs/cards;
- candidate matrices;
- Candidate Selection;
- Architecture artifacts;
- Draft/validation outputs;
- final claim review;
- final source/PDF build provenance;
- Visual Review record;
- legacy `pipeline-state.json`.

The Raw index itself is content-addressed and records SHA-256/byte size for accepted collector files. This is a strong candidate for reuse after v2 provenance/window validation.

## 4. Artifact disposition table

| Artifact class | Default v2 disposition | Reason | Required v2 action |
|---|---|---|---|
| Accepted collector Raw bytes | `REVALIDATE` | Raw bytes are factual/provenance inputs and should not depend on Weekly editorial semantics | verify every recorded path/SHA/byte count; verify collector acceptance and W33 window/source provenance; if valid, reference exact bytes from v2 provenance |
| `raw-index.json` | `REVALIDATE` | good content-addressed inventory, but generated under legacy state/collector acceptance | regenerate or import a v2 provenance index that binds the exact verified legacy Raw bytes and source commit |
| Collector run metadata/acceptance | `REVALIDATE` | operational provenance may be reusable if exact collector contract and window are acceptable | validate exact run metadata; record legacy contract identity as source provenance rather than pretending it was v2-generated |
| Weekly carry-over source artifacts | `REVALIDATE` | carry-over is still a Weekly Profile obligation but v2 completeness/materiality rules differ | verify origin issue/state, re-evaluate each carry-over obligation under current W33 Weekly Profile, bind into v2 completeness/materiality |
| Grok/X trend Raw inputs | `REVALIDATE` | potentially valid Raw current-context evidence, but timing/relevance semantics are Weekly Profile data | verify collection time/window/source; re-derive v2 Weekly relevance annotations |
| Legacy Screening results | `REGENERATE` | v1 Screening mixes generic triage with `why_now` and fixed A–L lanes and has no v2 Materiality trace | run profile-neutral Screening v2 from verified discovery inputs; keep legacy Screening only for comparison |
| Legacy verification queue | `REGENERATE` | derived from v1 Screening dispositions and prompt contract | build from accepted v2 Screening |
| Legacy Evidence Cards | `REVALIDATE` factual subset | source/claim/metric/limitation facts may be reusable; Weekly relevance fields are not authoritative | validate source refs, exact task/input hashes where possible, identifier/entity binding and factual readiness; create fresh v2 Edition Evidence View; regenerate any card that fails new correctness checks |
| Legacy Evidence editorial recommendation / `why_now` fields | `REJECT` as v2 authority | edition-specific meaning belongs to v2 Weekly Profile/Edition View | derive fresh Weekly relevance/materiality annotations |
| Legacy Candidate Records/Matrix | `REGENERATE` | current matrix depends on legacy rolling-window/timing semantics and lacks v2 Materiality/Completeness basis | rebuild v2 candidate matrix from accepted v2 Evidence Views + ledger |
| Legacy Candidate Selection | `REGENERATE` | old role vocabulary and standalone Human approval semantics conflict with v2 internal Selection contract | run internal v2 Selection and expose it inside Architecture Review Summary |
| Legacy Architecture Input/Plan | `REGENERATE` | v1 Architecture contract contains Weekly-only publication fields and is not bound to v2 Completeness/Materiality summary | construct v2 Architecture from new matrix/Selection; legacy plan becomes comparison evidence only |
| Legacy Architecture Human approval | `REJECT` as v2 approval | v2 Architecture Review must bind exact v2 Selection/Materiality/Completeness/Architecture hashes | request the normal v2 Architecture Review once the new proposal is ready; do not infer approval from legacy Selection/Architecture flags |
| Legacy Draft Packages | `REGENERATE` | basis Architecture SHA changes and v1 packages contain Weekly-only `late_breaking`/`this_week` semantics | materialize v2 generic Draft Packages from approved v2 Architecture |
| Legacy Article Draft Results | `REGENERATE` as canonical input | accepted text may be useful comparison, but v2 package/evidence/profile basis differs | use only as editorial comparison; redraft under v2 package/prompt or explicitly import text through a v2 reviewed-revision mechanism if such a mechanism is implemented and validates evidence use |
| Legacy Issue Synthesis | `REGENERATE` | v1 synthesis is `this_week_signals` shaped and not bound to v2 synthesis/profile contract | generate Weekly Profile synthesis under v2 after approved drafts |
| Legacy final claim review | `REGENERATE` | old review basis is legacy drafts/architecture | rerun v2 claim/attribution/materiality-use validation |
| Legacy TeX/source tree | `REJECT` as v2 canonical source; retain fixture | derived from legacy Architecture/Draft/Synthesis and publication contract | keep for regression/comparison; build new v2 publication source from v2 semantic artifacts |
| Legacy PDF + Visual Review | `REJECT` as v2 release candidate; retain fixture | exact bytes prove legacy result only and cannot authorize a semantically different v2 production path | use for visual/content comparison and regression only; v2 Publication Preview must bind the new exact PDF |
| Legacy `pipeline-state.json` | `REJECT` as v2 authority | legacy Human Gate semantics and state contract differ | preserve immutable fixture; initialize independent v2 `production-state.json`; never infer v2 approval from legacy state |

## 5. Why this is not a generic migration feature

The table above is a **Pilot-specific compatibility audit** for a real issue that happens to have extensive legacy work. It does not create a requirement that Core v2 automatically translate every historical state or every old intermediate artifact.

Core requirements remain narrower:

- frozen artifacts stay immutable/readable;
- source provenance can be inspected;
- reusable facts can be independently revalidated;
- future editions start cleanly under v2;
- no compatibility adapter may silently downgrade v2 correctness.

A generic automatic migrator should be added only if later production evidence shows repeated operational value.

## 6. W33 validation value

This disposition gives W33 a distinct role from W34.

### W33

Tests compatibility boundaries:
- can v2 reuse old immutable factual inputs without inheriting old editorial semantics?
- can legacy Evidence facts be independently revalidated?
- does v2 deliberately regenerate semantic artifacts whose contract changed?
- does the new Materiality/Completeness/Architecture path discover differences from the legacy candidate?

### W34

Tests clean current Weekly production after W33 findings are repaired:
- fresh window;
- fresh collection/currentness;
- no legacy artifact dependency;
- fixes generalize.

Thus W33 and W34 are complementary rather than duplicate tests.

## 7. Required comparison report after W33 Pilot

W33 Pilot should preserve a structured comparison between legacy and v2 results, at minimum:

- Raw/source surfaces reused or newly collected;
- Screening disposition differences;
- Evidence facts reused/regenerated/rejected;
- material candidates gained/lost;
- Selection role differences;
- Architecture differences;
- materiality/completeness limitations newly exposed;
- article hierarchy/thesis differences;
- final PDF length/structure differences;
- regressions or improvements in claim boundaries, references and layout.

Differences are evidence, not automatically defects. The control session classifies whether each difference is expected profile evolution, a Core defect, a Weekly Profile defect, or an edition-local editorial choice.

## 8. Safety rule

The legacy `weekly/2026-W33-work` branch must not be overwritten or repurposed as the v2 work branch.

The Pilot implementation should use an explicitly separate v2 work branch/path strategy until stabilization. Any legacy bytes reused by v2 are referenced/imported through hash-verified provenance rather than mutated in place.

## 9. Exit decision

W33 compatibility policy is now explicit enough for WU-004:

- no clean-slate discard of the existing RC by default;
- no requirement for automatic full-state migration;
- artifact classes have deterministic default dispositions;
- factual/provenance reuse is separated from semantic regeneration;
- the legacy PDF/state remains a valuable immutable comparison fixture.
