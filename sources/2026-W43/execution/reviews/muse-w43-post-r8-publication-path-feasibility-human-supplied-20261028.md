# J-GAS W43 post-r8 Human proof approval — lawful publication path feasibility

Date: 2026-10-28 JST
Status: WORKER_FEASIBILITY_REPORT / HUMAN_SUPPLIED_IN_CHAT / NO_RELEASE_AUTHORITY
Terminal supplied by Muse: \`READ_ONLY_SHARED_CORE_REVIEWED_REPAIR_REQUIRED\`
Provenance: The Human Owner pasted the Muse findings into the editorial Sol conversation following an over-restrictive in-chat-only execution contract. This is a durable, edited transcription of the worker-supplied report, **not a new independent Sol execution**. No detached worker result file has been independently SHA-verified. This report is documentary evidence, not a Stage Checkpoint or Human Gate receipt.

## 0. Git guards, reported and editorial Sol checked

| Subject | HEAD | Root Tree |
|---|---|---|
| Existing W43 work branch at inspection | \`88e791258cc34fc18269553a3a4fb38260f4c905\` | \`342805330fe7336ad4cd8f48891d6ed9288feaec\` |
| Parent, pre-contract | \`589019fa183e73035a24699b54b5aa38fc03ddb4\` | \`b42a1e1b4d6949f84c55588f16c15cc6dbccede1\` |
| Reviewed main | \`041a08dfef3112643cbf85b4a86a7b6f9128aed6\` | \`a134dc36a407d08ab1de416324229b3955e0325a\` |
| Frozen production/survey-core-v2 | \`774dd39a951c9ac3818e83dfffd4c7666efb0a20\` | \`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481\` |
| Fixed r8 PDF implementation | \`953a9d331972fdae237da4bd0f1019b17168a118\` | \`dfafff50c946e3d0abc051eb419797de283b192a\` |

- W43 work HEAD parent exactly matches the pre-contract commit.
- Fixed P2 sidecar exists at \`de5e41c253de37015fdb828503040f818698c6bc\`.
- Muse reported a clean working tree following authorized local fetch and fast-forward sync; the editorial Sol checked remote refs separately. Do not treat local Git fetch/fast-forward as repository/GitHub publication write.

## 1. Approved and unapproved authority

Human statement (verbatim): 「確認の結果OKです、承認します。」
The accepted document:
\`sources/2026-W43/execution/governance/human-w43-r8-corefree-proof-content-layout-approved-20261028.md\`

This accepts exact 22-page \`NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF\` for Human **editorial content/layout pre-review** after independent audit terminal \`INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS\` (P0=0/P1=0/P2=4 nonblocking).
Fixed PDF SHA-256: \`abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72\`; TeX SHA-256: \`4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d\`; PDF size 487351 bytes and 22 A4 pages.
It is NOT the canonical exact-byte \`PUBLICATION_PREVIEW\` Human Gate, NOT Freeze/Release/PR/merge approval, and NOT a consent to Core modification, compatibility shim, state mutation, exception_gate activation or proof-as-release.

Actual \`sources/2026-W43/production-state.json\`: \`ARCHITECTURE_ESTABLISHED\`, architecture_review \`approved\`, publication_preview \`pending\`, exception_gate \`inactive\`, next_action \`stage:drafting-synthesis\`, Draft/Validation/Preview/Freeze/Release checkpoints \`pending\`.
Preserve 36 bibliography keys / 15 \`CURATED_REVIEW_REQUIRED\`, approved Architecture, Evidence, Selection, r8 byte identity.

## 2. Blocking defect and authority mismatch — worker's source-level findings

Canonical Draft runner:
\`scripts/run_drafting_synthesis_v2_interactive.py --repo-root . --state sources/2026-W43/production-state.json\`
failed \`ValueError: Screening package basis drift: state_sha256\`.
Evidence: \`sources/2026-W43/execution/defects/w43-drafting-screening-basis-drift-20261025.md\`.

Call chain reported:
- \`survey_drafting_v2.derive_draft_package\` → \`survey_drafting_v2_base._load_drafting_basis\` → \`_resolve_effective_screening_discovery\` (\`survey_drafting_v2_base.py:137–188\`, specifically :170);
- \`survey_screening_v2.validate_package_basis\` (\`survey_screening_v2.py:629–650\`);
- lines 637–639 require equality between \`basis["state_sha256"]\` and current State bytes.

Observed historical screening r1/r2 basis \`state_sha256\`: \`885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596\`.
Current State SHA-256: \`b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6\`.
Screening profile SHA and Discovery SHA both MATCH. State drift follows trusted \`EVIDENCE_REVIEWED→SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED\` bridge transitions and Human Architecture approval. Static screening-time State byte equality cannot hold after valid Stage advancement.

Related general validator/bridge mismatch, evidence:
\`sources/2026-W43/execution/defects/w43-screening-prepare-state-basis-20261025.md\`.
- \`survey_production_v2.verify_state_basis\` (:896–932) invokes \`validate_state_semantics\` (:658 onward).
- Lines :712–713 reportedly require every State history row's \`repository_commit_sha\` to equal init \`7a969fd9…\`, but W43 history rows correctly track distinct executing commits \`e67099d5/0e6ecaa5/9b9f388b/0005db67/aaaf45b1\`.
- \`_checkpoint_attestation_path\` (:518–520) expects \`orchestration/v2/attestations/<checkpoint>.json\` through current State authority config; agent-first bridge actually records FROM-state checkpoint paths \`orchestration/v2/checkpoints/ISSUE_INITIALIZED.json\` and successive FROM-state names. \`_validate_authority_ref\` (:530–544) rejects paths.
- Similar structural mismatch was reported for W42 RELEASED. No evidence here that W43 research bytes or valid Human Architecture consent are damaged. The defect is in shared validation conventions versus agent-first bridge authority.

## 3. Three possible paths — feasibility matrix

### Path A: existing frozen native Core

Result: \`IMPOSSIBLE_ON_FROZEN_CORE_V2\` on current evidence.
No accepted frozen-Core native primitive resolves historical Screening State basis while preserving active State, Human Gate, accepted Screening, Evidence/Selection/Architecture and immutable Core. \`derive_draft_package(...implementation_sha)\` fails via \`validate_package_basis\`. Rewriting State or Screening inputs, bypassing checks, \`--implementation-sha\`-only override, hand-built Draft or detached old State would be authority forgery or violate stage preconditions. \`ADVANCE_STAGE\` cannot cure an unsuccessful Draft. The release workflow requires \`FROZEN\` exact State/manifest; W43 remains \`ARCHITECTURE_ESTABLISHED\`.

A reviewed generic Core maintenance candidate on a separately authorized maintenance track, plus formal seven-point acceptance audit, new baseline decision and clean W43 rerun, is the supported long-term correction. Production W43 cannot edit Frozen Core v2 in place.

### Path B: edition-local transient runtime compatibility

Result: \`THEORETICALLY_CONCEIVABLE_BUT_NOT_LAWFULLY_AUTHORIZED_OR_PROVEN\`.
W41/W42 approved edition-local compatibility concerned late-stage Freeze/Pub Gate provenance typing and schema (\`CV2-DM-001/002/003\`), AFTER canonical Publication Preview approval; no authority transfers to early-stage W43 \`Screening→Draft\` root-of-trust changes.
- W41/W42: \`RELEASE_CANDIDATE→FROZEN\`, prior \`_prior_artifacts\` incorrectly classified Human approval as Stage Checkpoint or lacked proper VISUAL schema; this was limited, separately authorized, runtime-only.
- W43: \`ARCHITECTURE_ESTABLISHED→DRAFT_COMPLETE\` provenance/basis \`validate_package_basis: state_sha256\` plus \`verify_state_basis\` history/path mismatches; different functions, stages and possible impacts.
- \`docs/core-v2-deferred-maintenance-summary.md\` restricts compatibility to separately authorized and precedent-justified cases. There is no Human consent for W43, and no bounded proof that a narrow transient shim can preserve all stage/checkpoint/cross-stage integrity.

First missing conditions: detailed bounded in-memory behavior proposal, input hashes and affected exact functions, positive/negative tests and independent audit; explicit **separate** Human Owner consent in an authorized exception channel. No such approval currently exists, so DO NOT implement or record a canonical clean PASS based on an imagined shim.

If an exception proposal is later requested, cover:
\`validate_package_basis\`, \`verify_state_basis\`, \`validate_state_semantics\`, \`_resolve_effective_screening_discovery\`, \`derive_draft_package\`;
historical screening state basis \`885927bd…\`, current State \`b0450d25…\`, profile \`4447d25e…\`, Discovery \`f62d8459…\`;
allowlisted transient changes, causal provenance checks, negative testing, audit requirements, immutable canonical artifacts, fail-closed boundaries.
An exception must not manufacture a Stage PASS.

### Path C: publish noncanonical proof as canonical issue

Result: \`NOT_AUTHORIZED\`.
\`docs/freeze-release-policy.md\`, \`docs/weekly-release-policy.md\` and \`docs/weekly-release-process.md\` require canonical exact-byte Publication Preview approval, Freeze source/PDF binding, immutable release manifest and controlled release identity. The operator bridge has 8 allowlisted operations and no proof-as-release or bypass operation.
The known TS-003 one-off exception was scoped to a later, post-\`VALIDATED_DRAFT\` publication situation. It is not blanket precedent for W43's blocked Draft. Human approval of a clearly labelled core-free proof does not imply an exception or authority for public Release.

## 4. Recommendation and stop

Worker terminal: \`READ_ONLY_SHARED_CORE_REVIEWED_REPAIR_REQUIRED\`.

Rank 1: preserve Frozen Core v2 and accepted W43 research; resolve shared Core validation/bridge convention mismatch in a separately reviewed maintenance candidate, exact-head tests, seven-point fresh independent audit, Human full-candidate review, formal integration/new baseline decision, then W43 clean rerun. No production-side shared Core edit.

Rank 2: only if urgent W43 release merits a separately justified owner-level exception, investigate W43 transient compatibility via written scope+hashes+tests and **explicit prior consent**. No safe transfer of W41/W42 precedent on supplied evidence.

Rank 3: do not offer proof-as-release path C as ordinary publication; absent a separate lawfully governed scope change, halt release.

No publication Stage or Human Gate was advanced by this investigation. This durable report recording is a documentation-only commit on W43 branch, independent of the source material's report-run actions. GitHub/Core/PDF freeze/release remains unchanged.
