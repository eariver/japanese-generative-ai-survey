# J-GAS W42 — Muse r31 integrated governed recovery through renewed Human Publication Preview

Date: 2026-10-20 JST
Status: `EXECUTION_AUTHORITY / HUMAN_R31_APPROVED / REAL_TRUSTED_OPERATOR_ADMISSION_REQUIRED / STOP_AT_FRESH_PUBLICATION_PREVIEW`
Repository: `eariver/japanese-generative-ai-survey`
**Work branch (existing only):** `weekly/2026-W42-v2-work`

## 0. Exact dispatcher baseline and authority hierarchy

The Sol r31 dispatch commit containing this contract and the Human authorization is the **only starting HEAD**. Sol's activation message MUST provide its exact HEAD and root Tree. Start by verifying live remote HEAD/Tree before any write; if there is any mismatch, zero writes and report the actual hashes. The audit/disposition parent is `98171b524651fce0b2e9d011fe4e57346da12908` / Tree `9fcc8efe94c820690531402e5dfede80a7e2a0e9`; confirm direct ancestry from that commit to exact dispatcher SHA.

Read in this order:
1. Human authorization `sources/2026-W42/execution/governance/human-w42-r31-request-changes-and-integrated-recovery-authorization-20261020.md`;
2. this executable r31 contract (supersedes the historical `.PROPOSED.md` proposal);
3. Sol r30 audit disposition and the archived read-only r30 independent audit;
4. current State, official Human Gate review index `sources/2026-W42/gates/review-index.json`, approved Architecture r1 and existing Candidate;
5. State-pinned frozen Core v2 `scripts/survey_human_gate_v2.py`, `scripts/survey_core_execution_bridge_v2.py`, `scripts/survey_stage_validation_v2.py`, `scripts/survey_reader_publication_v2.py`, `scripts/survey_reader_surface_gate_v2.py`, the publication & operator request schemas and reviewed `main` GitHub Actions workflow;
6. r29 and r30 deterministic/build/review/selection evidence necessary to the **bounded delta**, not the full 21-page independent audit.

Immutable upstream baselines:
- Reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`;
- Frozen Core HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- State-pinned implementation HEAD `a4f25630270f029656f35771592f9ebda02fa5cc`, Tree `e68560d1542806b61b4c55f03063839fd2ec30c0`;
- Architecture r1 Git blob `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`, Human Architecture approval remains approved;
- r18 approved-to-use Reader proposal blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, do not rewrite;
- r29 canonical reviewed TeX SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3` (96,790 bytes); PDF SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9` (505,102 bytes, 21 pages); Reader SHA256 `47634ae3ac347dd9529e796e01ed3661defa89e5f31b164dfe9752155b23c76f`;
- r30 fixed audit commit `b33098f32027d52a245fbbeb07586d52fa7ae6f0`, Tree `a2ace998c38c94a3260371bbe8f8acd4511e6feb`.

Current, pre-revision State MUST be `RELEASE_CANDIDATE/HUMAN_GATE_REACHED` with `human_gates.publication_preview=pending`, `human_gates.architecture_review=approved`, `next_action=PUBLICATION_PREVIEW`, validation passed. Existing Gate review index has Architecture r1 approved, no Publication Preview decision, so anticipated Publication Preview revision number **r1**; derive it from actual index rather than hardcode if changed. This Human instruction **authorizes** the `REQUEST_CHANGES` Gate record, it does NOT claim the record is already created.

NO new/fallback/review/repair branches; no `reset` of any kind, local `reset --hard`, `rebase`, `force`, rewriting old commits, destructive checkout or other-user workspace mutation. Start in a clean isolated checkout/worktree if needed, retaining current branch identity. No shared Core, config, schema, workflow, reviewed main or Architecture edit. No Release/Freeze/Human approval.

## 1. Before any Gate mutation, establish actionable TRUSTED GitHub Actions transport

The reviewed `.github/workflows/survey-production-v2-operator-bridge.yml` is the required security boundary. Read actual workflow around its `issue_comment` or `pull_request_target` trigger, `operator-preflight`, trusted runtime checkout and `operator-execute` postflight. Prefer owner/collaborator-authorized **issue #448** command transport if available; the exact issue_comment body must be `/survey-core-execute <40-lowercase-hex-request-only-commit-SHA>`. Workflow may also allow same-repo reserved-prefix PR to main when legitimate; **do not create a branch to obtain this route**. An inaccessible authenticated caller or unavailable issue permissions is a genuine blocker — do not submit an inert comment from an untrusted/bot identity and pretend it admitted execution.

The exact request-only git commit must:
- add **one** new JSON file under `sources/2026-W42/execution/requests/`;
- change **no other file** in that commit;
- be remote current HEAD at `operator-preflight`, including after any race;
- contain `reviewed_main_sha=c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, `work_branch=weekly/2026-W42-v2-work`;
- for Human Gate request, contain `reviewed_repository_commit_sha=<request-only commit parent SHA>` (the current reviewed Candidate/State plus these r31 Human documents, not an older original r30 commit);
- validate against `schemas/operator-execution-request-v2.schema.json`; request referenced within preflight must actually be newly added to remote HEAD;
- use a unique request_id and unoccupied bridge-run directory, as Core Bridge refuses an already run request.

**Preflight must pass before the requested mutation.** Record actual Actions workflow run URL/ID, exact request SHA, true request parent, logged preflight success, Core execution receipt, postflight commit and verified new branch HEAD. No self-reported local result counts as trusted admission; no synthetic `PASS`. Do not change the work branch while the run admits and executes. Do not touch State or delete any canonical output before the legitimate revision succeeds.

If workflow transport is unavailable, STOP `W42_R31_TRUSTED_ADMISSION_UNAVAILABLE / BEFORE_GATE_REVISION`. This is preferable to a new unreviewed local CLI permission exception.

## 2. Genuine Human Gate REQUEST_CHANGES, rollback only via first-party Core

Prepare `REQUEST_PUBLICATION_PREVIEW_REVISION` operator request:
- `state_path=sources/2026-W42/production-state.json`;
- `expected_revision` from live `sources/2026-W42/gates/review-index.json` (first Publication Preview r1 if unchanged);
- `regeneration_boundary=DRAFT_COMPLETE`;
- `requested_changes` explicitly identify F-B57 inaccurate repository first-publication and F-OP01 r30 missing trusted workflow admission, plus low-risk B54 snapshot annotation;
- `reviewed_by=Human Owner` and `review_reference` identify the exact r31 Human authorization document and the Sol audit disposition; `reviewed_at` must be an honest ISO date-time for the formal recorded review event, **not a fabricated timestamp for the user's date-only ChatGPT message**. In accompanying provenance record the original owner's decision date (2026-10-20 JST) separately.
- `reviewed_repository_commit_sha` MUST equal request-only commit's parent, per workflow.

Execute via first-party trusted GitHub Actions run only. Core `survey_human_gate_v2.request_publication_preview_revision` is the authorized operation; never use `invalidate_pending_gate` (Publication Preview operator boundaries empty), general direct State edits, manual deletion of checkpoint/Gate authority, or `publication-surface-revalidation` (reason `REVIEWED_CORE_CHANGE` in `VALIDATED_DRAFT` is inapplicable here).

Read back first-party Gate `REQUEST_CHANGES` r1 review record/index, true State `DRAFT_COMPLETE`, draft stage checkpoints/provenance, preserved Architecture r1 approval, removed/superseded paths from trusted receipt, intact old r30 historical evidence in Git. The canonical W42 Reader/TeX/PDF/QA records may exist on disk after the native rollback: those are **stale current singleton bytes**, not authorized for reuse under a corrected source. Account for them using a strict old→new manifest and controlled edition-local replacement only AFTER Gate invalidation, with original byte proof retained in historical commits.

## 3. Focused factual repair — do not expand editorial scope

**F-B57 / mandatory.** GitHub source:
- NVlabs/ASPIRE commit `7ba73d3bcac8f6b6d4a7d67ed4040988f768d282` 2026-08-21 `Public release`: repo already public;
- NVlabs/ASPIRE commit `fa00f0ef2bc1d91d594b9aa502c22133c9f538f7` 2026-10-16 `ASPIRE v1.0 release`: this week's event.

Only in Section 7 reader-facing prose and dependent Table T7 row: replace "10月16日リポジトリ公開" with a precise distinction "8月には公開済みのNVlabs/ASPIREで、10月16日にv1.0が公開された" and June paper/background separation. Adjust old TeX deck near line 715 ("ASPIREのOSS公開"→"ASPIRE v1.0公開"), Table T7 near line 732 (October release→v1.0 on Oct 16), body near line 759, and old line 763 "10月16日のX投稿" only if independently source-proven; otherwise write a date-neutral announcement. Keep licensing ownership/apportionment and empirical numbers intact. Do not assert non-evidenced poster/date. Capture exact limited old/new text diff and protected unchanged-block metrics.

**B54 / small temporal qualification.** Keep 19.17%, 79 entries / seventh, $0.15/test, and `72分`; add only `2026年10月12日時点のVals公表値` to historical rank context near §7 old lines 720 and 742 as necessary for snapshot clarity. Official Vals Harvey's Legal Agent Benchmark v1 `https://www.vals.ai/benchmarks/hlab-v1` lists `1h12m`, so `72分` is verified and must not be silently replaced by unrelated dynamic card latency. Preserve price and evaluator vs publisher graph distinction. If extra bibliographic date/reference citations are truly needed, update edition-local citation maps and exact documentation; avoid unduly increasing the 90-key base count.

Outside these limited Section 7 modifications, keep all r18 prose/table/citation content identical where semantically possible. Core-reviewed Architecture r1 is not a length minimum; Human accepted 21pp Route A and known p03/p11/p13 whitespace. No synthetic page padding, no comprehensive re-research, no optional tone rewrite.

## 4. Byte-bound regeneration, quality proof, focused independent review

After native `REQUEST_CHANGES`, replace only the necessary **current** edition-local canonical `surveys/weekly/2026-W42/main.tex`, `main.pdf`, `preview.sty` only if truly needed, `sources/2026-W42/publication/v2/reader-manuscript-v2.json`, quality/semantic/visual/reader-surface semantic+Gate files, candidate and their deterministic results/manifests as required. Edition-local current canonical path changes MUST be under clearly recorded revision scope and normal FF commits. Preserve old r29/r30 Git commits and archived Sol reports; no deleting provenance records. Do not use `git reset` to go back to r29 and then patch. Record old/new hashes and changed source ranges.

Regenerate exact PDF using reviewed edition toolchain. Validate page count and printing, no LaTeX warnings/overfull/missing glyphs. Compare old/new TeX sections P1–P6, 7 chapter headings, bibliography keys, citation expansion and unaffected table cells; verify only intended §7 reader deltas. If PDF remains 21pp confirm; if pagination changes by genuine few lines, inspect changed pagination and no lost text; do not artificially force page count. Retain 7 tables/27 rows/110 cells baseline except explicitly corrected T7 cell, 28/28 Selection coverage, 90-bib-key baseline with deviations accounted.

Use actual Core builders/validators for current Reader manuscript and the **seven** `DRAFT_COMPLETE` authorities `reader-manuscript`, `validated-source`, `publication-pdf`, `quality-regression-bundle`, `semantic-review`, `visual-review`, `reader-surface-gate`. Regenerate QA artifacts and exact-hash review records rather than reusing prior old-PDF SHA. Real separate read-only independent semantic review of corrected Section 7 facts and Reader-Surface new exact TeX; focused visual review on affected page(s), T7/bibliography, cover/pagination and deterministic unchanged-page check. Preserve raw attributable reviewer output; Muse may not assume it has independent review authority or fabricate PASS. Truthful actual source/date evidence for B54/B57 required.

Use deterministic validators `survey_reader_publication_v2.validate_manuscript_manifest`, `survey_quality_v2.validate_bundle`, `survey_reader_publication_v2.validate_review_record`, `survey_reader_surface_gate_v2.validate_reader_surface_gate`, `survey_stage_validation_v2.validate_stage`. Respect original Core schema's review check family; never reduce thresholds or invent result paths.

## 5. Two real trusted ADVANCE_STAGE operations

Only if corrected bytes have full valid documented evidence and real independent surface authority:
1. Commit all seven current authorities to existing W42 branch with normal FF. Then create **a separate request-only commit** for `ADVANCE_STAGE`, `expected_from_state=DRAFT_COMPLETE`, all seven artifacts (including mandatory reader-surface-gate, even though stage_plan text lists six); launch and verify exact trusted workflow run, new Stage Checkpoint and State `VALIDATED_DRAFT`.
2. Create a **new** canonical `publication/v2/publication-candidate-v2.json` by official builder, bound to corrected current TeX/Reader/PDF/reviews/bundle. Verify `READY_FOR_PUBLICATION_PREVIEW` by official validator and commit as a normal FF change.
3. Create the **second separate request-only commit** for `ADVANCE_STAGE`, `expected_from_state=VALIDATED_DRAFT` with **only** `publication-candidate` artifact; launch trusted workflow, verify returned Stage Checkpoint, State `RELEASE_CANDIDATE`, `terminal_reason=HUMAN_GATE_REACHED`, `human_gates.publication_preview=pending`. Store real run URLs, reviewed Main runtime, receipts and sha-bound State. Ensure old r30 local CLI deviation remains documented, not retroactively accepted as trusted.

For every transition: one authorized workflow event, exact remote request HEAD, actual `operator-preflight` success, trusted runtime provenance, and remote read-back after first-party normal non-force push. If any request was made stale by a concurrent commit, STOP and report; no clandestine retry with rewritten histories.

## 6. Writes/stop/report

Allowed: official first-party native Gate revision (which may invalidate relevant historical *current checkpoint files* as designed), controlled replacement of edition-local canonical publication surface only after revision, edition-local provenance/quality/review/Candidate regeneration, new r31 evidence/session/append-only execution index, and official workflow-generated receipts/State/checkpoints. Historical earlier commits and audits immutable.

Forbidden: change `.github/workflows`, `config`, `schemas`, `scripts`, `main`, Frozen Core, approved Architecture r1, selection/evidence/screening/history except through official native Gate State regeneration, any new/fallback/review branch, manual State crafting, force/rebase/reset, direct local Bridge substitution, other-user dirty workspace disruption. No publication approval, no Freeze, no Release.

**SUCCESS ONLY** at `SOL_W42_R31_CORRECTED_PREVIEW_READY / RELEASE_CANDIDATE / HUMAN_PUBLICATION_PREVIEW_PENDING / FROZEN_CORE_PRESERVED / NO_FREEZE_NO_RELEASE`.

Final report must include:
- starting/final exact remote HEAD/Tree and linear ancestry, allowlisted paths, no force, read-back;
- Human Gate `REQUEST_CHANGES` official r1 record and actual trusted run/preflight URL;
- original ASPIRE August/October proof and exact before/after §7/T7 text; Vals 79-snapshot and 72min proof;
- corrected PDF URL at final commit, SHA256, actual pages, Reader/TeX hashes;
- focused independent delta content/visual/Reader-Surface review authority and 7 formal current artifacts with validators;
- true two trusted Stage request-only commits, Actions run IDs, receipts, checkpoints and final State;
- residual disclosed Human Route A whitespace and any other source limits; stop on any NEW substantive issue;
- explicit `NO_HUMAN_PUBLICATION_PREVIEW_APPROVAL / NO_FREEZE / NO_RELEASE`.

If unable to gain authorized trusted issue comment/PR workflow admission, missing separate semantic reviewer, or any authoritative mismatch, STOP at actual last-good commit/State, classify blocker `W42_R31_TRUSTED_TRANSPORT_OR_REVIEW_BLOCKED`; do not claim final Candidate is ready.

This single integrated authorization replaces further per-substep approval requests; normal permitted deterministic failures should be corrected within it if safe. The sole next Human stop after success is fresh Publication Preview.
