# TS-003 Muse execution — Evidence immutability/provenance repair after Sol r4

Status:

`EXECUTION_AUTHORITY / EVIDENCE_R4_REQUEST_CHANGES / IMMUTABILITY_REPAIR_ONLY / STOP_FOR_SOL_R5`

Date: `2026-09-30 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Guard authority

Do not hardcode the work-branch SHA/tree in this file.

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole work-branch start guard.

Before any write, read-only verify:

- remote work branch HEAD/tree against the launch message;
- remote main HEAD/tree;
- remote `production/survey-core-v2` HEAD/tree;
- issue = `SP-vision-multimodal-2026`;
- lifecycle = `CANDIDATES_NORMALIZED`;
- discovery checkpoint = `passed`;
- screening checkpoint = `passed`;
- evidence checkpoint = `pending`;
- materiality/completeness/selection/architecture = `pending`;
- Human Architecture Review and Publication Preview = `pending`.

If any guard differs, perform zero writes and report expected vs actual.

No new/fallback/repair/review/iteration branch. No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authorities

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r4.md`
2. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r3.md`
3. `sources/SP-vision-multimodal-2026/execution/evidence-semantic-repair-r3-20260930/repair-report-r3-to-r4.md`
4. r3 accepted Evidence: `sources/SP-vision-multimodal-2026/evidence/v2/accepted/c6763f1c5d3f69cc96c78bab5eccde83c9956fb8c20a71e58b1b57fb3d33c8d7/`
5. r3 accepted Views: `sources/SP-vision-multimodal-2026/evidence/v2/views/accepted/fc8556a310b8bf8d33809e2e40bb08f4867690a38eb4d8b561ab7d999ea499c7/`
6. r4 accepted Evidence/Views only as the source of the four accepted wording deltas, not as the baseline for unaffected timestamps/provenance.
7. current `production-state.json`.
8. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-020.

Sol r4 review is authoritative over worker reports.

## 2. Mission

Repair only the r4 immutability/provenance defect.

The semantic corrections in r4 for D074/D075/D077 are accepted. The same-class D111 semantic correction is now explicitly authorized. Do not research anything new and do not alter any other Evidence meaning.

Construct a new append-only r5 acceptance from the **r3 accepted set as baseline**.

Authorized changed Cards are exactly:

- `VM-D074`
- `VM-D075`
- `VM-D077`
- `VM-D111`

For those four, preserve the r4 wording cleanup while retaining r3 provenance timestamps unless an already-existing canonical authority requires otherwise.

For all other 107 records, copy the r3 Card bytes exactly. Do not regenerate their `observed_at`, `accessed_at`, contexts, formatting, ordering or any other field.

VM-D101 is explicitly protected and must be byte-for-byte identical to r3.

## 3. Views contract

Use r3 Views as the baseline.

For the 107 unaffected records, copy View files byte-for-byte from r3.

For D074/D075/D077/D111, change only fields that must change because the corresponding Evidence Card content/hash changed. Preserve every unrelated annotation, transition, branch, materiality and lineage field.

Do not globally regenerate View payloads with timestamps or unrelated formatting changes.

## 4. Tooling rule

If the ordinary Evidence build command necessarily regenerates timestamps/content for all Cards, do not use it as proof of byte identity.

Use the lowest-level existing canonical tooling needed to create a schema-valid append-only acceptance and manifests while preserving copied Card/View bytes.

Do not edit Shared Core.

If the current edition tooling cannot produce a valid mixed acceptance with byte-preserved unaffected records, fail closed and report the tooling limitation instead of rewriting unrelated Evidence.

## 5. Required outputs

Create additive execution artifacts for r4→r5 containing at minimum:

- exact r3 baseline identity;
- exact r4 wording-delta identity;
- r5 accepted Evidence identity;
- r5 accepted Views identity;
- per-record byte comparison r3→r5;
- explicit changed-record list;
- validator receipts;
- repair report;
- coverage/validation summary.

The report must not use `byte-identical` unless actual bytes/blob hashes match.

## 6. Fail-closed r5 checks

All must pass:

1. 111/111 tasks represented.
2. r1/r2/r3/r4 accepted directories remain unchanged.
3. Exactly four Evidence Card payloads differ from r3: D074/D075/D077/D111.
4. Exactly 107 Evidence Card payloads are byte-for-byte identical to r3.
5. D101 is byte-for-byte identical to r3.
6. The four changed Cards preserve r4 semantic cleanup and contain no unbound `HF`/`Hugging Face`/`release API`/`release tag` provenance naming.
7. Exactly the required four View payloads differ from r3; 107 unaffected Views are byte-for-byte identical, unless a schema-mandated manifest-only container change is required. Any exception must be explicit and justified before acceptance.
8. `PRIMARY_FACT` remains absent.
9. G01–G06 remain preserved.
10. VERIFIED/PARTIAL remains evidence-driven; expected count remains 106/5 unless a canonical validator forces a different honest status.
11. lifecycle remains `CANDIDATES_NORMALIZED`.
12. No Materiality/Completeness/Selection/Architecture/Human Gate artifacts are created.
13. main and frozen Production Core remain unchanged.

## 7. Prohibited

Do not:

- rerun Discovery;
- rerun or change Screening;
- perform new research;
- change the 111-task set;
- alter any non-target Card/View semantics;
- build Materiality Ledger or Profile Completeness;
- run Selection or Architecture;
- make Human Gate decisions;
- modify main or Production Core.

Normal commit + non-force push only.

## 8. Stop

Normal completion:

`TS-003 EVIDENCE_IMMUTABILITY_REPAIR_R4_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R5`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`

Stop there.
