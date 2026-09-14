# W35 execution instruction — resume from accepted Grok r3 through fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / W35_RESUME / GITHUB_ONLY_GROK_HANDOFF / THROUGH_FRESH_ARCHITECTURE_REVIEW`

Date: `2026-09-15 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W35-v2-work`

## 1. Mission

Resume W35 from the contract-compliant `AWAITING_GROK` stop, consume the Sol-reviewed Grok/X result that has already been imported into this repository, complete the canonical W35 production flow through a **fresh Human Architecture Review**, and STOP there without inventing the Human decision.

Muse/OpenCode has **no Google Drive authority** for this task. All handoff material required for execution is in GitHub.

Do not request, install, search for, or use a Google Drive connector. Do not ask the Human to copy Grok material from Drive. The exact accepted result bytes have already been transferred by Sol into edition-local repository Raw storage.

## 2. Starting guard

The Muse invocation will provide an **Exact Starting SHA** equal to the Sol handoff commit that contains:

1. this execution request; and
2. the accepted Grok r3 Raw artifact.

Before any repository write, read-only verify all of the following:

- remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- the Exact Starting SHA has parent `799ac17f2b86c9a9cba8abc68e3436502f22f0e5`;
- remote `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `main` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- accepted Grok Raw exists at the path below and matches the exact SHA-256 and byte count below.

If any guard differs, perform **no repository/GitHub write**, report expected versus actual values, and STOP.

No force push, reset, history rewrite, fallback branch, repair branch, or alternate W35 branch is allowed unless the Core-defect protocol in this instruction is explicitly triggered.

## 3. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W35/execution/requests/sol-w35-initialize-through-architecture-review-20260915-r1.md`
2. this request
3. `sources/2026-W35/execution/sessions/w35-sol-initialize-through-architecture-review-20260915-r1.md`
4. `sources/2026-W35/execution/sessions/w35-pre-discovery-research-prep-20260915-r1.md`
5. `sources/2026-W35/production-profile.json`
6. `sources/2026-W35/production-state.json`
7. `sources/2026-W35/external/x/x-source-intake-v2.json`
8. `sources/2026-W35/external/x/weekly-x-2026-W35/grok-task.md`
9. accepted Grok Raw below
10. current generic Core/config/schema/script authority required by the canonical stage tooling.

The earlier pre-Discovery preparation remains **non-authoritative preparation only**. It is not accepted technical Evidence by itself.

## 4. Accepted Grok/X authority imported by Sol

Accepted external result:

`grok-x-result-r3.md`

Repository Raw path:

`sources/2026-W35/external/x/weekly-x-2026-W35/raw/grok-x-result-r3.md`

Exact SHA-256:

`43b16b9aca2912ad191b95e7ba02a70fb06c1e24e7bba317e281cbd24ff80208`

Exact byte count:

`21590`

Observed-at authority from the result front matter:

`2026-09-15T03:06:00+09:00`
= `2026-09-14T18:06:00Z`

Sol review decision:

`PASS_FOR_W35_X_SOURCE_INTAKE`

Canonical post-level accounting from the accepted ledger:

- total unique X URLs: `35`
- `ORDINARY_WINDOW`: `25`
- `BACKGROUND_ONLY`: `0`
- `LATE_BREAKING`: `10`
- ordinary official-account URLs: `9`
- ordinary independent/non-official URLs: `16`

The original approximate `~40+ ordinary-window` claim was **not reproduced**. This is accepted and is not a blocker. Do not inflate or recreate the old approximation.

### Important authority rule inside r3

Treat the **post-level ledger rows, their exact X URLs/timestamps/window classes, and the global 35/25/0/10 accounting** as the canonical observation authority.

Some cluster-level composition counts in the human-readable r3 summary are derivative editorial summaries and are not canonical counters. If any downstream step needs a per-cluster count, recompute it from the post-level ledger. Do not modify the immutable Raw file merely to cosmetically repair a derivative summary.

X remains Raw Observation/community signal, not final technical Evidence.

## 5. Record the X result canonically

Use the repository-local Raw file above. Do not touch Drive.

Complete `sources/2026-W35/external/x/x-source-intake-v2.json` through the canonical `scripts/survey_x_intake_v2.py record-result` mechanism.

Use:

- run id: `weekly-x-2026-W35`
- raw path: `sources/2026-W35/external/x/weekly-x-2026-W35/raw/grok-x-result-r3.md`
- drive file name recorded for provenance: `grok-x-result-r3.md`
- observed at: `2026-09-15T03:06:00+09:00`
- result status: `SUCCESS`
- discovery disposition: `DISCOVERY_RECORDED`

For `imported_at`, use the timestamp of the Sol handoff commit that first imported the exact Raw bytes into GitHub, normalized as required by the tool.

Create the required edition-local Discovery record(s) through the canonical W35 Discovery machinery, and pass the actual resulting Discovery ID(s) to `record-result`. Do not fabricate IDs solely to satisfy the manifest.

The result rationale must make clear that:

- r3 is the Sol-reviewed correction/materialization result;
- 35 exact X URLs are persisted;
- 25 are ordinary-window;
- X claims remain leads/community observations pending primary-source verification;
- the prior `~40+` approximation was not reproduced and is not used as authority.

After recording, validate the X manifest against the Discovery acceptance surface. The expected X manifest terminal status is `COMPLETE`.

## 6. Resume Discovery from the actual W35 evidence base

After X intake is COMPLETE, resume the canonical W35 flow.

Do not treat the Grok ledger as a substitute for fresh primary-source research.

For every technically material candidate:

- retrieve authoritative/first-party sources where available;
- semantically consume the source content, not merely retrieve a URL;
- distinguish official claims, independent X observations, and downstream verified technical facts;
- preserve unresolved or unavailable authority as unresolved rather than inferring from snippets;
- record chronology against the canonical W35 window;
- separate ordinary-window material, background context, and late-breaking material according to current Core rules.

Coverage must remain broad enough to test the Weekly lanes rather than merely confirming the three dominant X clusters.

A lane may legitimately end with no material candidate. Do not manufacture category balance.

## 7. Semantic-consumption requirement

Do not repeat the W34 failure mode where retrieval count was close to Evidence count without adequate source consumption.

A successful fetch/download is not semantic verification.

For each retained technical claim, the Evidence construction must identify what the authoritative source actually establishes and what remains unsupported.

Where multiple claims are supported by one source, consume the relevant portions once and map them appropriately rather than mechanically creating one retrieval per claim.

Where an X observation gives a lead but no authoritative source can substantiate it, retain the observation as community signal or unresolved material; do not promote it to VERIFIED technical Evidence.

## 8. Carry-over

Use the current canonical carry-over mechanism only.

Do not copy W34 Selection, Evidence, Architecture, Draft, or prior Human judgments as W35 conclusions.

Any carry-over candidate must be freshly revalidated against W35 authority and current Core rules.

The previously noted W34 MiniMax `RECHECKED_UNRESOLVED` obligation may be evaluated only through the formal current mechanism; no automatic promotion.

## 9. Required production progression

Proceed through the canonical stages required to reach a fresh Human Architecture Review:

```text
ISSUE_INITIALIZED
→ completed X Source Intake
→ DISCOVERY_COLLECTED
→ CANDIDATES_NORMALIZED
→ EVIDENCE_REVIEWED
→ SELECTION_COMPLETE
→ ARCHITECTURE_ESTABLISHED
→ fresh Human Architecture Review pending
→ STOP
```

Use the repository's current canonical stage commands, validators, schemas, checkpoints, and execution-record requirements.

Do not skip a required gate merely because the likely W35 themes appear obvious from Grok.

Do not advance a stage unless its current contract passes.

## 10. Selection and Architecture requirements

Selection must be evidence-driven.

Do not promote a topic solely because it is popular on X.

Keep internal selection rationale, package identifiers, review terminology, lifecycle names, file paths, and operator metadata out of any future reader-facing prose.

Architecture must be W35-specific and derived from the accepted W35 Selection.

Do not copy the W34 package structure merely for convenience.

At the Architecture stage, materialize the canonical fresh Human Architecture Review surface and STOP before any Human approval is invented.

No Draft generation is authorized in this execution.

## 11. Reader-Surface Gate awareness

This run stops at Architecture Review, so the post-Architecture reader-surface gate is not expected to execute yet.

However, do not introduce new architecture/publication structures that bypass the current #434/#496 contract.

Future publication order remains:

```text
publication_payload
→ canonical structured reader surface
→ lexical pre-publication gate
→ persisted SEMANTIC_EDITORIAL review
→ READER_PIPELINE_INDEPENDENCE PASS
→ exact-byte/digest revalidation
→ TeX
→ downstream defense-in-depth
→ PDF
```

Core production code must not manufacture semantic editorial PASS.

## 12. Core-defect protocol / Production Line separation

If a **generic Core defect** is discovered during W35:

1. stop W35 at a safe checkpoint;
2. distinguish the generic Core defect from W35 issue-local content/data problems;
3. create only the bounded repair branch required by the established policy:
   `fix/core-v2-<bounded-slug>-<YYYYMMDD>`;
4. base the repair on the current exact `main`;
5. open a PR with `base = main`;
6. run the required regression/CI and obtain review;
7. **do not merge the Core repair PR to main**;
8. after Sol/Human review PASS, integrate the reviewed repair by normal merge into
   `production/survey-core-v2`;
9. read back the exact Production Line SHA;
10. normal-merge the current Production Line into `weekly/2026-W35-v2-work`;
11. resume W35 from the resulting exact branch state.

Do not silently patch generic Core only on the W35 branch.

Do not merge a Core repair to main.

Do not force-sync Production Line or W35 to main.

If no generic Core defect is found, do not modify `production/survey-core-v2`.

## 13. Repository write scope

Normal production writes are limited to the existing:

`weekly/2026-W35-v2-work`

branch and the W35 edition-local artifacts/checkpoints required by the current Core.

The accepted Grok Raw path supplied by Sol is immutable input. Do not rewrite it.

Do not create another W35 branch.

Do not modify W34.

Do not merge W35 to main in this execution.

All pushes must be normal/non-force.

## 14. Checkpoint at Human Architecture Review

Create/update the canonical W35 checkpoint required by the current repository. If an explicit path is needed and no newer canonical convention overrides it, use:

`docs/checkpoints/2026-W35-architecture-review-pending-20260915.md`

Record at minimum:

- starting W35 SHA/tree;
- reviewed main SHA/tree;
- Production Line starting/current SHA;
- accepted Grok Raw path/SHA-256/byte count;
- X accounting `35 total / 25 ordinary / 0 background / 10 late`;
- X manifest completion/result status;
- Discovery aggregate;
- normalized candidate aggregate;
- Evidence verification aggregate;
- Selection aggregate;
- Architecture package aggregate;
- unresolved and carry-over items;
- any Core defects/repair PRs and Production Line integration SHAs;
- current lifecycle stage;
- exact Human gate;
- exact terminal stop reason.

## 15. Final remote validation

Before reporting completion, read back the remote refs and exact artifacts.

Confirm:

- remote W35 branch HEAD == reported ending SHA;
- ending tree == reported ending tree;
- remote `main` HEAD remains the guarded main SHA unless the Human separately changed policy outside this task;
- remote `production/survey-core-v2` HEAD remains the guarded Production Line SHA if no Core repair occurred;
- if a Core repair occurred, main remains unmodified by that repair and the Production Line SHA reflects the reviewed integration;
- accepted Grok Raw still matches SHA-256 and byte count;
- X manifest validates COMPLETE;
- the fresh Human Architecture Review surface exists;
- no Draft was generated;
- no force push/history rewrite occurred.

## 16. Required final report

Report:

```text
Reviewed main:
Production Line:
Starting W35 SHA:
Ending W35 SHA:
Ending W35 tree:

Accepted Grok Raw:
Grok Raw SHA-256:
Grok Raw bytes:
X accounting:
X manifest status:

Current lifecycle stage:
Discovery aggregate:
Normalized candidate aggregate:
Evidence aggregate:
Selection aggregate:
Architecture package aggregate:

Human gate:
Architecture Review artifact:

Core defects discovered:
Core repair PRs:
Core repairs integrated into Production Line:
Core repairs merged to main: NONE

Main unchanged by Core repair: PASS/FAIL/N/A
Force push used: NO
Stop reason:
```

Normal successful stop reason:

`FRESH_HUMAN_ARCHITECTURE_REVIEW_REQUIRED`

STOP there.
