# TS-002 Muse execution — Architecture provenance sanitation r2

Status: `EXECUTION_AUTHORITY / BOUNDED_ACTIVE_PROVENANCE_SANITATION / STOP_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-09-25 JST`

Repository: `eariver/japanese-generative-ai-survey`
Branch: existing `special/beyond-text-2026-work` only.

## 1. Mission

Perform a **bounded active-provenance sanitation** after Sol Architecture Review r1.

The substantive TS-002 architecture has passed Sol review. Do not redesign it and do not redo research.

The defect is that active downstream artifacts still contain stale pre-rebind language such as:

`Future Discovery repair should correct the locator.`

That repair is already complete. The active artifacts must reflect the current canonical provenance state before Human Architecture approval.

Also correct the Human Architecture dossier's stale PARTIAL enumeration, where BT-D062 is still mentioned although it is now VERIFIED from the Seamless v2 body.

Authoritative Sol review:

`sources/SP-beyond-text-2026/execution/sol-architecture-review-r1-20260925.md`

Authoritative provenance repair history:

`sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/provenance-repair-manifest.json`

Use the launch SHA/tree supplied by the operator message as the execution guard. Do not substitute older guard values embedded in prior prompts or reports.

## 2. Hard guard

Before any write, verify read-only:

- remote work branch HEAD == operator-supplied Exact Starting SHA
- remote work branch tree == operator-supplied Expected Starting Tree
- remote main HEAD == `0bbb02b3c5963403860897daec2feaf61e82589a`
- remote main tree == `e4ddde5ed5059d303b818f54e27204369b256bcb`

If any mismatch occurs: zero writes, report expected vs actual, stop.

No new branch, fallback branch, repair branch, or review branch.
No force push, reset, rebase, or history rewrite.
Shared Core is frozen and must remain unchanged.

## 3. Do not redo research

Do NOT rerun:

- Discovery research;
- X/community collection;
- broad Screening research;
- semantic Evidence body-consumption campaign;
- external gap-fill research.

Do NOT change substantive claims, metrics, historical interpretations, materiality reasoning, selection semantics, chapter design, transition interpretation, or page allocation unless necessary solely to remove stale provenance-state wording.

Draft and all later publication stages remain prohibited.

## 4. Preserve historical audit surfaces

Historical/audit surfaces must remain immutable where possible, including:

- prior accepted Evidence result-sets;
- prior Edition Views;
- `source-body-access-ledger.json`;
- `provenance-repair-manifest.json`;
- prior execution session reports;
- prior Sol review files;
- raw Discovery/X archives.

Old locators may remain in these historical surfaces when clearly recorded as historical defects.

Do not erase audit history merely to make a text search clean.

## 5. Sanitize the active Evidence provenance language

Start from the current active rebound Evidence authority produced by the provenance-rebind run.

Scan all active Evidence cards associated with rows in `provenance-repair-manifest.json` and any other active cards containing stale provenance-state language.

Required rules:

1. `sources[].url`, artifact canonical URLs, and active canonical locators must point to the corrected canonical source.
2. Remove or rewrite any sentence that says or implies a completed Discovery repair is still pending.
3. In particular, no active Evidence limitation may contain the literal future-state instruction:
   `Future Discovery repair should correct the locator.`
4. If historical provenance is editorially useful, use accurate past-tense wording, for example:
   `Prior recorded locator X was a transcription defect; canonical Discovery provenance was rebound to Y during the 2026-09-24 provenance repair.`
5. Do not treat a prior locator defect as a present technical limitation once corrected.
6. Preserve genuine source-access / body-consumption limitations separately.

Special cases:

### BT-D024

Keep `NEEDS_MORE` unless the already-authorized evidence state provides a basis otherwise. The current unresolved issue is body/version binding for `CompVis/stable-diffusion`, not the old Stability-AI locator itself.

Do not silently promote it.

### BT-D089

Keep `PARTIAL`. The canonical IEEE identity is corrected, but full body/protocol consumption remains unresolved.

### BT-D062

Keep `VERIFIED`. It was rebuilt from the v2 source `2312.05187`; do not reintroduce v1/v2 uncertainty as a current PARTIAL condition.

## 6. Content-addressed Evidence regeneration

Do not mutate an existing accepted content-addressed Evidence directory in place.

If the active Evidence payload changes, create a new canonical Evidence result-set through the current edition-local/Core-supported builder/acceptor path.

Preserve all previous result-sets unchanged.

The new active Evidence semantics must remain:

- total 139
- VERIFIED 126
- PARTIAL 8
- NEEDS_MORE 5

Substantive claims/metrics must remain semantically identical except provenance-state wording sanitation.

Rebuild/re-accept Edition Views as required by the changed Evidence hashes.

## 7. Refresh transition ledger and downstream derived artifacts

Refresh active edition-local derived artifacts that consume Evidence limitations/provenance.

At minimum inspect/regenerate as required:

- transition ledger JSON/Markdown;
- materiality ledger;
- profile completeness;
- candidate matrix;
- candidate selection;
- architecture-v2;
- architecture-review-summary-v2;
- architecture-review-attention-v2;
- Human Architecture Review dossier;
- production state/checkpoints.

This is a deterministic replay, not a new editorial decision pass.

Expected invariant semantics:

- Discovery: 139
- Screening: KEEP 134 / MAYBE 3 / INSPECT 2 / DROP 0
- Materiality: MATERIAL 109 / CONTEXT 25 / HOLD 5
- Completeness: overall LIMITED; 4 SATISFIED / 8 LIMITATION
- Selection: SELECTED 134 / HOLD 5
- Transition ledger: 43 entries
- Architecture: 14 packages
- Page plan: target 80 / guidance max 96
- Human Architecture gate: pending

If any of these semantics would change for a reason other than hash/provenance sanitation, stop and report instead of silently changing the architecture.

## 8. Human dossier correction

Regenerate/correct `execution/architecture-review-dossier-r1.md` into a fresh r2 dossier or canonical equivalent; do not overwrite audit history if edition convention preserves prior dossiers.

The current non-VERIFIED Evidence set is exactly:

PARTIAL (8):

- BT-D022
- BT-D059
- BT-D076
- BT-D083
- BT-D089
- BT-D098
- BT-D106
- BT-D134

NEEDS_MORE / HOLD (5):

- BT-D024
- BT-D072
- BT-D091
- BT-D120
- BT-D125

BT-D062 must not appear in the PARTIAL list.

The fresh dossier must preserve the existing 14-package architecture, page budget, modality balance, transition coverage, anti-thinness rationale, and unresolved/LOW_SIGNAL boundaries.

## 9. Required validators

Create an edition-local validation receipt covering at least:

- `DISCOVERY_COUNT_UNCHANGED`
- `SCREENING_DECISIONS_UNCHANGED`
- `EVIDENCE_COUNT_AND_STATUS_UNCHANGED`
- `MATERIALITY_COUNTS_UNCHANGED`
- `COMPLETENESS_SEMANTICS_UNCHANGED`
- `SELECTION_COUNTS_UNCHANGED`
- `TRANSITION_LEDGER_COUNT_UNCHANGED`
- `ARCHITECTURE_PACKAGE_COUNT_UNCHANGED`
- `PAGE_PLAN_UNCHANGED`
- `CANONICAL_LOCATORS_MATCH_REPAIR_MANIFEST`
- `NO_ACTIVE_FUTURE_DISCOVERY_REPAIR_INSTRUCTION`
- `HISTORICAL_AUDIT_PROVENANCE_PRESERVED`
- `BT_D062_VERIFIED_NOT_PARTIAL`
- `PARTIAL_SET_EXACT_8`
- `NEEDS_MORE_SET_EXACT_5`
- `NO_FALSE_STATUS_PROMOTION`
- `SHARED_CORE_UNCHANGED`
- `DRAFT_NOT_ENTERED`
- `HUMAN_ARCHITECTURE_GATE_PENDING`

For `NO_ACTIVE_FUTURE_DISCOVERY_REPAIR_INSTRUCTION`, scan current active semantic/derived artifacts only. Exclude immutable historical reports/manifests from this check and document the scope.

## 10. Session report

Create a session report documenting:

- start guards;
- stale-language count before sanitation by active artifact;
- Evidence cards changed by ID;
- exact provenance wording policy;
- old active Evidence hash and new active Evidence hash;
- new Views hash;
- transition/materiality/completeness/selection/architecture hashes;
- dossier r2 path;
- invariant count checks;
- remaining PARTIAL/NEEDS_MORE IDs;
- validator receipt;
- final HEAD/tree;
- no Draft/later stages.

## 11. Stop condition

Normal terminal state:

`ARCHITECTURE_REVIEW / AWAITING_HUMAN_ARCHITECTURE_DECISION_R2`

Human gate remains pending. Do not fabricate, infer, or record Human approval.

No Draft, Validation, Publication Preview, Freeze, or Release work.
