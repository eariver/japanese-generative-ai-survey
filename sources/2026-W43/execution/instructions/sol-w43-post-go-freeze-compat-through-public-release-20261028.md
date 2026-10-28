# J-GAS W43 — Human GO recorded; finish Freeze → main → public Release via W43-only W42-precedent runtime compat

Date: 2026-10-28 JST.
Status: EXECUTION_CONTRACT / HUMAN_FINAL_PDF_GO_ALREADY_RECORDED / W43_ONLY_FREEZE_ADMISSION_COMPAT / RELEASE_AUTHORIZED
Worker: Muse/OpenCode; editor: Sol. No ChatGPT Work requirement.

## 0. Exact starting state, read-only guard, and allowed writes

Repository: eariver/japanese-generative-ai-survey
EXISTING branch: weekly/2026-W43-v2-work
Pre-contract HEAD: f03ba496f4d3c40038ea5d24d7ec856d9d549ce6
Pre-contract Root Tree: c38b518136c6d51650d2017fddcd6fa575b6c24e
The final Sol instruction commit SHA/Tree will be supplied at dispatch. Verify branch remote HEAD and Tree exactly equal those supplied, and its single parent is the pre-contract HEAD. Verify main HEAD/Tree 041a08dfef3112643cbf85b4a86a7b6f9128aed6 / a134dc36a407d08ab1de416324229b3955e0325a, and production/survey-core-v2 HEAD/Tree 774dd39a951c9ac3818e83dfffd4c7666efb0a20 / cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481. Any mismatch: STOP, no write.

READ-ONLY for guards/protected Core and approved PDF; WRITE ENABLED for W43 edition-local Freeze recovery, real checkpoint/State outputs, release records, PR/Release workflows and bounded execution logs. git fetch + fast-forward-only local sync authorized. Normal commits and non-force push on existing W43 branch are REQUIRED; no reset, rebase, force push or fallback branch in W43.
Main changes only through history-preserving PR merge. Workflow-created release-record branch/PR is permitted as official post-release provenance transport.

## 1. Human GO is ALREADY accepted and a first-party Gate is ALREADY PASS

Human Owner's verbatim final reply after Sol presented exact candidate PDF and the release procedure: 「承認します。」
Durable Human scope record:
sources/2026-W43/execution/governance/human-w43-final-publication-preview-go-20261028.md
Human authority record commit: e5a93087ae50e744db8035eeeff8dc59a5020989
Exact request-only commit: 9c85041f671360dab913f6e896882868a911c512
Official operator run #40608435059: SUCCESS
Official Gate bot commit: bfc777116885c7235d8cf422c3cb3841cc8640a1
Official approval: sources/2026-W43/gates/publication-preview-approval.json,
approval_id publication-preview:2026-W43:f9abcae4b07d254c79a6,
whole-file SHA256 af676842dce8f9ed922cfcc182c125af99744ede08ea4c155d8f448db41cb931.
Human \`PUBLICATION_PREVIEW\` decision APPROVED; current production-state.json \`RELEASE_CANDIDATE\`, \`publication_preview=approved\`, \`next_action=stage:freeze\`.
Do NOT ask Human for GO again, do NOT repeat General/GPT full PDF audit, do NOT modify approved PDF. The explicit final GO authorizes deterministic Freeze, normal main merge, public Release and provenance closure on identical bytes.

Pinned exact published asset target:
surveys/weekly/2026-W43/main.pdf
SHA256 b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165
486967 bytes, 22 A4 pages.
TeX SHA256 3fa6ca3b4c610cd12fecd3e6ce449e0d9cffd9e7edc67efb1b85f5bd0e758784.
Publication candidate whole-file SHA256 f85a17c1d2a5e0099ee9b4dfab03e410f69d50242494df1ba854716daf10b074.
Reader/Candidate/quality/General regression were already validated before Human GO. The original r8 proof is NOT the release asset.
General verdict: GENERAL_W43_EQUIVALENCE_PASS, no P0/P1, six nonblocking P2; Sol independently noted the General report's malformed old-r8 hash text; do not rewrite history.

## 2. Actual Freeze attempt — known frozen validator defect; NO Stage advancement

Staged W43 files already in existing branch:
- sources/2026-W43/publication/v2/freeze-record-v2.json
- sources/2026-W43/publication/v2/release-manifest-v2.json
They were composed from actual frozen-low-level schema fields by editorial Sol and committed, NOT an assertion that Core's build_freeze already executed. Expected staged file SHA256:
freeze-record f73698454a5f1b4fd681360331ba57d7da1350a389ec3da9947c5b602e2ba7bb
release-manifest bc1a1fdd328a7fa413155c423afae723d73b5007d2cf581cdac446c8a5b1655f.
Check actual byte SHA before using, and verify values with native frozen validators/low-level \`survey_publication_v2.build_freeze\` as appropriate; if a canonical builder would emit different bytes or require a correction, investigate before any checkpoint, preserving approved PDF/Candidate/Gate. Do not silently overwrite immutable committed manifests.

Attempted first-party \`ADVANCE_STAGE RELEASE_CANDIDATE→FROZEN\`:
- request-only commit f03ba496f4d3c40038ea5d24d7ec856d9d549ce6
- request path sources/2026-W43/execution/requests/sol-w43-final-freeze-20261028.json
- GitHub Actions run #40608878000: FAILURE at execute canonical deterministic Core operation, after operator-preflight SUCCESS.
- exact error in trusted job log: \`prior Stage Checkpoint fails .../schemas/stage-checkpoint-v2.schema.json: $: 'artifacts' is a required property\`.
- No bot Stage commit, no State change, no Freeze complete, no main PR/merge, no tag/public Release. Do not retry the same unmodified request: deterministic failure.
This is the already documented generic Frozen Core defect CV2-DM-002, which treats approved Human Publication Preview authority as a Stage Checkpoint. Companion CV2-DM-001 visual review schema and CV2-DM-003 unreferenced VALIDATED_DRAFT checkpoint may recur after this earlier failure is resolved. The actual approved PDF/Candidate and Gate were NOT rejected.

## 3. W43-only minimal recovery from proven W42 late-stage precedent

Human Owner previously authorized W43-only workarounds over broad shared-Core repair, and the final exact-PDF GO explicitly authorizes completing Freeze→Release. This same late-stage Human-approval-vs-checkpoint bug has a direct, repeatedly successful W41/W42 W43-relevant precedent. No shared Core modification permitted.

Mandatory source inputs:
- sources/2026-W42/execution/compat/w42-freeze-compat-driver.py
- sources/2026-W42/execution/compat/w42-freeze-advance.py
- sources/2026-W41/execution/compat/w41-freeze-compat-driver.py
- sources/2026-W42/execution/governance/human-w42-r34-edition-local-compat-freeze-release-authorization-20261021.md
- docs/core-v2-deferred-maintenance-summary.md CV2-DM-001/002/003
- actual W43 first-party failed job log #40608878000
- W43 frozen Core/current scripts at protected main, especially survey_stage_validation_v2 and survey_agent_control_v2.
- W43 actual approved Gate/State, VALIDATED_DRAFT checkpoint, Candidate, Visual record, prepared freeze/manifest.

Adapt the already proven W42 edition-local script to W43 ONLY:
A. \`survey_stage_validation_v2._prior_artifacts\`: separately validate Human Approval (exact state-bound file SHA, \`APPROVED\`, exact candidate/PDF) and exclude it from the Stage Checkpoint schema loop. All genuine historical checkpoints still verified against exact original schema and bound artifact SHAs. Do NOT disable other integrity checks.
B. \`_current_artifacts\`: allow W42-proven strictly necessary \`visual-review-record\` and \`publication-candidate\` in RELEASE_CANDIDATE; validate real modern VISUAL record and bind Candidate exact byte hash to the true VALIDATED_DRAFT checkpoint. No extra or invented artifact.
C. Run actual frozen \`validate_stage\`, produce actual deterministic \`CORE_STAGE_CONTRACT\` report, then actual frozen \`agent.build_stage_checkpoint\` and \`agent.advance_with_checkpoint\` with unchanged core modules; re-run \`agent.validate_agent_state\`. Log scope \`EDITION_LOCAL_RUNTIME_COMPAT\`, not \`DEFAULT_FROZEN_CORE_VALIDATION_PASS\`.
D. The adapter resides ONLY under sources/2026-W43/execution/compat or runtime-compat; no tracked shared scripts/config/schema/tests/CI change. If further unrelated error occurs, stop with exact error; no blanket bypass. Do not change source, PDF, Candidate, Gate or approved upstream.

Minimal honest verification, not another extensive research/QA campaign: all file SHAs, current exact Gate and Candidate, stage validator PASS under disclosed W43 runtime-only compatibility, checkpoint and resulting real \`FROZEN\` State PASS. One normal commit/non-force push containing actual runtime compat driver, validation report, real Checkpoint, real State, session/handoff; read back remote HEAD/Tree and protected refs.

## 4. Continue through public Release without another Human stop

Once State is really \`FROZEN\`, release_manifest status AUTHORIZED and PDF exact bytes unchanged:
1. Create an ordinary PR from existing weekly/2026-W43-v2-work into main (history-preserving normal merge, no squash/rebase/force). Review protected paths and confirmed main HEAD/Tree. DO NOT merge if unrelated changes or PDF SHA mismatch.
2. Merge and verify on merged main: FROZEN W43 State exact file SHA, Release Manifest SHA, Candidate approval/source/PDF byte chain and unchanged Core. If main advanced independently, reconcile only through lawfully safe, normal history-preserving merge without losing reviewed authority, else STOP.
3. Dispatch the existing \`.github/workflows/survey-production-v2-release.yml\` ON MAIN using exact \`issue_id=2026-W43\`, \`production_state_sha256=<actual merged main SHA256 of sources/2026-W43/production-state.json>\`, \`release_manifest_sha256=<actual merged main SHA256 of sources/2026-W43/publication/v2/release-manifest-v2.json>\`, \`confirmation=release:2026-W43\`.
4. Verify workflow run success and actual public release URL/tag \`weekly/2026-W43\`. Download asset (not just release listing) and confirm SHA256 \`b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165\` and 486967 bytes.
5. Release workflow creates the normal post-release provenance PR; merge it after checking its exact released bytes and legitimate RELEASED Stage State/record. Confirm main final W43 \`RELEASED / COMPLETE\` and unchanged approved PDF.
6. STOP if any genuine blocker, with committed real evidence. NO additional Human approval is necessary for the exact unchanged PDF under the prior GO; if PDF SHA must change or a new Owner-level scope exception is actually required, return to Human explicitly.

## 5. Deliverables, terminal, reporting

Write and push (existing W43 branch, unless first-party workflow creates its own narrowly governed provenance PR):
- W43-only transient freeze compat code and actual run records,
- existing Freeze Record/Manifest validated at exact byte SHAs,
- genuine \`orchestration/v2/checkpoints/RELEASE_CANDIDATE.json\`, \`production-state.json\` FROZEN, stage evidence,
- PR/merge record, workflow Run ID and published Release URL,
- downloaded Release asset SHA verification and release-provenance PR closure,
- \`sources/2026-W43/execution/SOL_W43_EXACT_RELEASE_CLOSURE_HANDOFF.md\` with final HEAD/Tree, main/Frozen Core, PDF SHA, workflow/PR and real Stage receipt.

Successful terminal only if public Release asset is verified and main closure legitimately recorded:
\`MUSE_W43_PUBLIC_RELEASE_EXACT_BYTES_VERIFIED_COMPLETE\`.
If blocked before publish: \`MUSE_W43_RELEASE_BLOCKED_AFTER_HUMAN_APPROVAL\`; report last successful stage and exact blocker, no false RELEASED.
Remember: **Human GO already exists, General QA already PASS, and first-party Preview Gate already APPROVED. The missing work is Freeze-admission compatibility → frozen stage → merge → Release → provenance closure, not new editorial work.**
