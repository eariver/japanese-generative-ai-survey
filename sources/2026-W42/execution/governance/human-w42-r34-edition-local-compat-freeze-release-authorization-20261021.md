# J-GAS W42 — Human r34 authorization: edition-local immutable-Core Freeze compatibility

Date: 2026-10-21 JST
Authority: `HUMAN_OWNER_APPROVED_W42_R34_BOUNDED_RUNTIME_COMPAT / EXACT_PDF_FREEZE_RELEASE / SHARED_CORE_IMMUTABLE`
Repository: `eariver/japanese-generative-ai-survey`
Existing production branch: `weekly/2026-W42-v2-work`
Human-reviewed failure baseline HEAD: `2f8058f04f8b623654a5f60da3a462e12add7720`, Tree `01dd94d24b57951d1726d320b37eee3b11ace1d6`.
Reviewed main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`.

## Exact Human approval and limits

Sol presented the independent finding that W42 trusted Freeze run `39455215003` failed on frozen Core's classification of `checkpoint_provenance.publication_preview` as a Stage Checkpoint, noted verified W41 Human-authorized edition-only compatibility precedent, and asked:

> W41と同様に、Frozen Core v2を変更しないW42専用の限定互換処理を承認しますか？
>
> 承認いただければ、今回の障害記録とW41の実績を基に、MuseがReleaseまで一括実行する正式指示を作成します。

Human Owner replied, verbatim:

> はい、承認します

This expressly authorizes **W42-only edition-local, in-process runtime compatibility matching the previously authorized W41 approach**, to complete the already-approved W42 exact-PDF Freeze and public Release. No further ordinary-stage Human approvals are required.

This approval modifies r33's prohibition on runtime compatibility ONLY for the two identified freeze-admission typing/shape conflicts. It does not waive freeze semantics, permit synthetic PASS/Stage State, patch protected Core, broaden editorial work, or retroactively change failed trusted Action into success.

## Immutable approval basis

- Human Publication Preview revision r3 already formally `APPROVED` by trusted first-party operator Actions run `39453500739`; no replay.
- Approved W42 PDF `surveys/weekly/2026-W42/main.pdf`: SHA256 `827a93d8a7ec786a1e052b4832ab160eff5131402888e5792d82682febf79a34`, 505694 bytes, 21 pages. Must remain byte-identical throughout Release.
- TeX SHA256 `e6d53d5ae962332c85df8b60c52ac614d259da3c7301cdffc4b0112372552697`, Publication Candidate SHA256 `2bcb42a6acb611ee970b3fa96c189d14b06ce740aa5c1059fffaeb9fe1f32649`, active Human Approval SHA256 `90be771e7ce11ad84b809ca45a9259add0fb74aa1524b2f2f4a714112a7aec8c`.
- W42 r33 first-party Freeze Record and Release Manifest exist but do not imply a successful FROZEN Stage; current State is `RELEASE_CANDIDATE`, next `stage:freeze`, freeze and release pending.
- r33 trusted Freeze request-only commit `a36541cb385919ad6bef8fada2027876a6b8fd99`, workflow run `39455215003`: preflight PASS, executor FAIL; preserve historical failure.
- W41 Human-approved precedent commit `813b5eea511c7cd769308aad8214bfa824ba0b6b`, `sources/2026-W41/execution/compat/w41-freeze-compat-driver.py`, Human contract `sources/2026-W41/execution/requests/2026-10-15-w41-frozen-core-immutable-compat-freeze-release.md`.
- Known generic debt `CV2-DM-002` (related DM-001 and DM-003); use original existing debt; no new generic defect ID.
- Shared frozen Core SHA `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`; no changes in `scripts`, `schemas`, `config`, `.github`, Architecture r1 or reader artifacts.

## Authorized narrow recovery

Allow W42-only in-memory compatibility to `survey_stage_validation_v2._prior_artifacts` (Human Preview Approval provenance is approval, not Stage Checkpoint; separately verify SHA + canonical approval validation) and `_current_artifacts` (admit exact modern `visual-review-record` and genuine `VALIDATED_DRAFT`-pinned `publication-candidate` required by existing Freeze contracts). Preserve and validate all real Stage Checkpoints, stage semantics and hashes.

Run **unchanged frozen Core functions** `validate_stage`, `build_stage_checkpoint`, `advance_with_checkpoint` after admission compatibility; label evidence `EDITION_LOCAL_RUNTIME_COMPAT`. No manual State/checkpoint/result fabrication, no arbitrary bypass. If genuine additional Core failures arise, stop for separate decision.

After real FROZEN state, normal W42 → main PR merge and main-only GitHub Actions Release workflow; verify public asset bytes. If known post-publish `CV2-DM-004` causes the workflow to fail *after* correct Release asset creation, use only the previously proven edition-local canonical provenance recovery without republishing, with honest failure reporting and normal PR. Never claim Released until verified.

Issue #570 remains entirely user-managed; no comment, label, close/reopen or status action.

Authoritative executable contract: `sources/2026-W42/execution/instructions/2026-10-21_muse-w42-r34-edition-local-compat-freeze-to-release.md`.
Target status: `SOL_W42_R34_RELEASED / PREVIEW_R3_APPROVED / EDITION_LOCAL_COMPAT_DISCLOSED / EXACT_RELEASE_ASSET_VERIFIED / CORE_V2_UNCHANGED / ISSUE570_UNTOUCHED`.
