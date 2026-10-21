# W42 Sol r34 — shared-Core Freeze failure disposition

Date: 2026-10-21 JST
Status: `CV2_DM002_CONFIRMED / HUMAN_APPROVED_W42_BOUNDED_COMPAT / NOT_A_CORE_FIX`
Reviewed W42 stop commit `2f8058f04f8b623654a5f60da3a462e12add7720`; root tree `01dd94d24b57951d1726d320b37eee3b11ace1d6`.
Human approval: `sources/2026-W42/execution/governance/human-w42-r34-edition-local-compat-freeze-release-authorization-20261021.md`.

## Evidence and classification

Trusted GitHub Actions Freeze run `39455215003` was real: `operator-preflight=success`, `operator-execute=failure` during canonical `ADVANCE_STAGE RELEASE_CANDIDATE→FROZEN`. Error: `prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json: $: 'artifacts' is a required property`. The frozen `_prior_artifacts` treats the Human Publication Preview Approval object (written into `checkpoint_provenance.publication_preview` by `approve_publication_preview`) as a Stage Checkpoint. It is an approval, not a checkpoint. Also the freeze checkpoint schema requires `visual-review-record` though frozen `_current_artifacts` excludes it as an extra, and the Candidate's legitimate `VALIDATED_DRAFT` checkpoint must be independently admitted.

This is a **shared frozen-Core internal incompatibility**, not a W42 draft error. Previously identified as `CV2-DM-002` and reproduced for W41. W41 Human owner authorized narrowly scoped runtime-only admission shim, using real frozen Core validators and State APIs, leading to actual `FROZEN`, public `weekly/2026-W41` exact-byte Release and `RELEASED/COMPLETE` without editing shared Core (commit `813b5eea511c7cd769308aad8214bfa824ba0b6b`). Follow W41 evidence but do not copy its results or claim default Actions Freeze succeeded.

## Sol adjudication

Adopt W41 W34–W39 precedents **only with W42 user's explicit r34 approval**. Preserve all checkpoints and Human approval hashes; driver may change in-memory admission typing but must not change any substantive validator. Run authentic Core Freeze validation, stage checkpoint and advance, report truthful compat usage. r33 failed Action persists as `FAIL`. Freeze Record/Manifest are currently only prepared, not effective. Any misleading Freeze timestamp must be regenerated using canonical builder with truthful time; old bytes retained by immutable Git commits. Approved PDF SHA256 `827a93d8a7ec786a1e052b4832ab160eff5131402888e5792d82682febf79a34` immutable. On success W42 issue merges normally to main, then Release Workflow; known `CV2-DM-004` may need documented post-publish **provenance-only** recovery if and only if genuine public asset verified. No Core change; no Issue #570 action.

Implementation: `sources/2026-W42/execution/instructions/2026-10-21_muse-w42-r34-edition-local-compat-freeze-to-release.md`.
