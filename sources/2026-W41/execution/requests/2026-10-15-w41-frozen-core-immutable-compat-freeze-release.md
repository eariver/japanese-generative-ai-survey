# J-GAS W41 — Frozen Core immutable / bounded Freeze compatibility through public Release

Status: `HUMAN_APPROVED_EDITION_LOCAL_COMPAT / NO_CORE_PATCH / PUBLISH_EXACT_BYTES`
Date: 2026-10-15 JST
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W41-v2-work`
Source stop: `1001ce055aa5240bb9848026331b4152d94f7306` (Tree `711b7111373bcf1929d8199433e4d4a5dc0463a0`)
Inventory-update ancestor: `fcbbe0f27f9b5dac3c881e5675d94978b5646b38` (Tree `9a681badd37f9f8223bb483139bea36d4a255e38`)
Exact invocation HEAD/Tree: supplied separately by Sol after committing this request. Stop on mismatch.

## 1. Human authority and terminal goal

Human Owner explicitly approved W41 r18 exact 17-page PDF and authorized Freeze and public Release. Following a shared-Core Freeze failure, Human Owner explicitly **rejected even a minimal Core fix** and instructed: `Core不具合を回避して編纂を完了させ、Core v2 Freeze後不具合リストへの追記とIssue起票を行ってください。`

Complete normal W41 publication without changing shared Core implementation. The inventory has already been updated under CV2-DM-002, and [W41 recurrence Issue #565](https://github.com/eariver/japanese-generative-ai-survey/issues/565) is open; do not create a duplicate issue.

## 2. Immutable identities

- Exact Human-approved PDF: `surveys/weekly/2026-W41/main.pdf`
- SHA-256: `4fd1958ce7dea3b2c257c5abe1de96e14c7e66cfe0d9c35e884ae596819750ce`; 446781 bytes; 17 pages.
- TeX SHA-256: `c159a8a63af46daefa57ce9f3e96ba95af4db4491226f68a5e2bd66f2b09cfc6`.
- Human approval: `sources/2026-W41/gates/publication-preview-approval.json`, SHA-256 `aa51e5df0b4165f65675f7df28f1f23a3c644a9f6f1326b0f16881f14ba6eb9c`.
- Reader-Surface Gate: `PASSED`, digest `8ff23098a699c711de20559497e80576a67414bd7be4ea25f364eae9e3f202c1`.
- Independent Semantic Review digest: `0a5da664e313b30ff918f9fb7d43491e615b712edac0d35149a7e7adbdff1471`.
- Publication Candidate: `READY_FOR_PUBLICATION_PREVIEW`, already approved by the Human; do not regenerate.
- Stopped lifecycle: `RELEASE_CANDIDATE`, `human_gates.publication_preview=approved`, next_action `stage:freeze`.
- Reviewed main: `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`.
- Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Release identity: `weekly/2026-W41`.

## 3. Guard and mandatory reading

Read-only confirm exact current remote W41 HEAD/Tree as supplied by Sol, `main`/frozen-Core HEAD/Tree, working tree, all exact authorities above, absence of public W41 release/tag and competing changes. If mismatch, STOP WITHOUT WRITES.

Read mandatory precedents:

- `sources/2026-W41/execution/defects/w41-release-core-defect-20261015.md`.
- `sources/2026-W35/execution/defects/w35-freeze-prior-checkpoint-provenance-core-defect-20260915.md`.
- `sources/2026-W36/execution/defects/w36-freeze-core-defects-20260918.md`.
- `sources/2026-W39/execution/defects/w39-freeze-compat-note-20260929.md`.
- `sources/2026-W35/execution/requests/sol-w35-temporary-compat-freeze-release-after-core-defect-20260915.md`.
- `docs/core-v2-deferred-maintenance-summary.md` (CV2-DM-001/002/003/004, W41 r1.0).
- `sources/2026-W40/execution/requests/sol-w40-publication-r4-approved-freeze-release-20261011.md`.
- `docs/freeze-release-policy.md`, `docs/weekly-release-process.md`, `.github/workflows/survey-production-v2-release.yml`.

## 4. Freeze compatibility — runtime only, use prior W34–W39 proof

**Do not modify frozen Core**, even minimally. No edits or commits to `scripts/`, `schemas/`, `config/`, `.github/`, `tests/`, frozen production branch or Core contract. No counterfeit approval, false PASS, synthetic review, weakened evidence check, PDF/TeX/Bib/Architecture/Evidence/manifest/content change.

Freeze/Release Manifest already exist, but Freeze was NOT completed and neither record is effective until formal stage validation/advance succeeds. Independently validate these records with the frozen Core canonical validators. Check their timestamps: `freeze-record-v2.json` currently advertises `frozen_at=2026-10-15T01:05:00Z`; do not preserve or claim a not-yet-occurred or false Freeze instant. If not an authentic completed Freeze instant, regenerate unapproved Freeze/Manifest through the existing `survey_publication_v2.build_freeze()` with the actual execution timestamp. All Candidate/approval/PDF bytes must remain immutable.

Run a **one-edition, transient in-memory/Python-driver admission shim** matching the W34–W39 precedent. It may temporarily adapt only the semantic *typing/admission* boundary of the frozen validator in the current process; this does NOT authorize a persisted code patch or edit of the Core package:

1. Preserve and validate every genuine prior Stage Checkpoint and all bound artifact/review SHA bytes.
2. Treat `checkpoint_provenance.publication_preview` as Human Approval, not as a Stage Checkpoint; validate it separately with the existing `publication.validate_preview_approval`, `agent.validate_agent_state`, current Candidate and state-bound SHA.
3. Admit the genuine `VALIDATED_DRAFT` checkpoint if required, with exact SHA and true checkpoint schema; no invented substitute.
4. Permit `visual-review-record` as the one additional current `RELEASE_CANDIDATE` freeze artifact if the canonical Freeze checkpoint/validator schema requires this role, reusing existing candidate-bound modern VISUAL record unchanged.
5. Run the **actual frozen-Core** `survey_stage_validation_v2.validate_stage()` semantic/contract checks with the bounded shim, not a hand-created PASS report. Retain original fail output and transient driver source, real command, patched admission scope, outputs, SHA checks and justification as W41 edition-local execution evidence. Identify the result as `EDITION_LOCAL_RUNTIME_COMPAT`, NOT `unmodified default validator PASS`.
6. Using only the real validated result, create authentic Stage Checkpoint with Core APIs and advance via `survey_agent_control_v2.advance_with_checkpoint()` (or standard CLI with identical guarantees); validate new State `FROZEN` via frozen Core. No provenance pointers may be removed from persisted State and no Human decision may be rewritten.

Keep only edition-local runtime driver and evidence under `sources/2026-W41/execution/compat/` and validation records under `execution/validation/`; do not commit temporary Python artifacts to shared Core folders. Stop if remaining checks fail or non-admission Core errors arise; no broader bypass allowed.

## 5. Normal integration and public release

Commit genuine `FROZEN` State, checkpoint, Freeze/Manifest and bounded compatibility evidence on existing W41 branch with normal non-force push; remote read-back. Check `main` unchanged from reviewed identity before any integration; if moved, stop and report; no silent rebase.

Use ordinary history-preserving PR from W41 existing branch to main; no squash/rebase/force. Verify merged main has exact approved PDF byte digest, freeze authority and immutable shared-Core files. Run canonical release mechanism `.github/workflows/survey-production-v2-release.yml` on main with true State/Manifest SHA inputs, release identity `weekly/2026-W41`. Do not invent asset/link or replace PDF.

Verify public Release is non-draft and tag correct. Download the GitHub Release PDF asset and independently recompute SHA-256 = `4fd1958ce7dea3b2c257c5abe1de96e14c7e66cfe0d9c35e884ae596819750ce` and size 446781. Verify provenance tag anchor differs appropriately from frozen source commit when workflow contract requires.

Known CV2-DM-004 workflow defect (nonexistent `survey_agent_control_v2.py validate-state`) may occur **after** exact public Release creation. Only then apply the already documented W38–W40 narrow post-publish release-record recovery (without asset recreation), preserving the genuinely published release. Never report failure as no release without checking public state.

Complete Core lifecycle `RELEASED`, terminal_reason `COMPLETE`, passed publication_preview/freeze/release checkpoints and committed Merge Verification/Release Record. If official Stage or release validation cannot be satisfied with documented narrow compatibility, STOP, preserve evidence, report actual public/private status and do not fabricate `RELEASED`.

## 6. Core debt and W42 findings

CV2-DM-002 remains `OPEN_CORE / EDITION_WORKAROUND` even after successful publication. W41 incident Issue #565 may be closed only after the exact public PDF and RELEASED state are verified; generic Issue #497 and inventory tracker #515 stay OPEN. Update `docs/core-v2-deferred-maintenance-summary.md` with a **release closure** row/revision when completed, without changing Core. Preserve W41 user nonblocking notes (p.14 whitespace; repetitive 'unfetched/unverified' disclaimers; weak independent Community evidence) for W42 editorial planning only.

## 7. Final report

Report exact start/final W41 HEAD+Tree, frozen Core/main identity, runtime-only shim diff/verification, real Freeze Stage validation and checkpoint hashes, Candidate and Human approval binding, frozen source SHA, normal PR/merge SHA, workflow run, release tag, public Release URL and asset URL with downloaded exact SHA+size, Release/merge records and final `RELEASED/COMPLETE` state, Issue #565 status, inventory revision. Stop after W41; no W42 compilation.
