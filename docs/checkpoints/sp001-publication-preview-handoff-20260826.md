# SP001 Core v2 Publication Preview 引継ぎ — 2026-08-26

## 目的

この文書は、ChatGPTセッション長上限のため、`eariver/japanese-generative-ai-survey` における SP001 Core v2 production を次セッションへ安全に引き継ぐための checkpoint である。

**次セッションは、この文書だけを信用せず、必ず GitHub 上の current `main`、`special/SP001-v2-work`、Production State、Publication Candidate、Human Gate review index を再読してから続行すること。**

本checkpoint作成時点では、SP001は通常の **Publication Preview Human Gate** に到達済みであり、Humanの明示判断なしにFreeze / Releaseへ進めてはならない。

---

## 1. Source of truth / current refs

Repository:

- `eariver/japanese-generative-ai-survey`

Current default branch at checkpoint creation:

- `main`
- HEAD: `079dac9605e4cf55a239de6f03e37a93f756a918`
- commit: `Revert accidental temporary file`

The Human-approved Core maintenance merge relevant to this SP001 production is:

- PR #470 `Core v2: fix interactive cross-package Draft reference resolution`
- merged Core commit: `94168050ae1161f92b594e13706c692c533c4139`

`main` moved after that merge only through non-protected-content cleanup associated with an accidental temporary file. At the end of this session there was no known protected Core drift after `94168050...`, but **next session must recheck current `main` before issuing a Human Gate operator request**.

Canonical SP001 work branch:

- `special/SP001-v2-work`
- HEAD: **`aa5b0665cf96546c88601883eac82819f1e428f1`**
- commit: `Execute Core operator request SP001-advance-publication-candidate-r1`

**Do not move this branch before the Human reviews the exact current Publication Preview.**

Current open transport PR:

- PR #472 `Survey Core operator transport: SP001 Draft r1`
- state: open
- merged: false
- mergeable: true
- head: `special/SP001-v2-work`
- current head SHA: `aa5b0665cf96546c88601883eac82819f1e428f1`
- base recorded by PR: `main@94168050ae1161f92b594e13706c692c533c4139`
- **transport PR only; never merge it**

The PR title/body are historically Draft-oriented because the same immutable transport PR has been reused as the work-branch trigger surface. Its current head is nevertheless the current Publication Preview candidate state. Treat the canonical work branch and Core authorities—not the stale PR prose—as source of truth.

---

## 2. Current Production State — Human Gate reached

Canonical authority:

- `sources/SP001/production-state.json`
- reviewed at commit: `aa5b0665cf96546c88601883eac82819f1e428f1`

Current state:

- `research_profile`: `THEMATIC`
- `publication_profile`: `LONGFORM_SPECIAL`
- `lifecycle_state`: **`RELEASE_CANDIDATE`**
- `human_gates.architecture_review`: `approved`
- `human_gates.publication_preview`: **`pending`**
- `next_action`: **`PUBLICATION_PREVIEW`**
- `terminal_reason`: **`HUMAN_GATE_REACHED`**
- Exception Gate: inactive

Machine checkpoints:

- discovery: passed
- screening: passed
- evidence: passed
- materiality: passed
- completeness: passed
- selection: passed
- architecture: passed
- draft: passed
- validation: passed
- publication_preview: pending
- freeze: pending
- release: pending

Lifecycle history now includes:

- `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` at `2026-08-26T12:22:00Z`
- `DRAFT_COMPLETE -> VALIDATED_DRAFT` at `2026-08-26T14:17:00Z`
- `VALIDATED_DRAFT -> RELEASE_CANDIDATE` at `2026-08-26T14:26:00Z`

The final operator bridge run for the candidate advance:

- workflow run: `32980263072`
- preflight: SUCCESS
- operator-execute: SUCCESS

Therefore there is no pending machine-stage execution. The next required action is Human review only.

---

## 3. Exact Publication Preview review surface

The Human must review the exact bytes retained at canonical commit:

- reviewed repository commit: **`aa5b0665cf96546c88601883eac82819f1e428f1`**

Publication Candidate:

- path: `sources/SP001/publication/v2/publication-candidate-v2.json`
- status: `READY_FOR_PUBLICATION_PREVIEW`
- raw file SHA-256 observed during builder run: **`bc4521166d381437a05bf0645c644ecf66c55c449094b4e95441f894bcce710c`**
- internal `candidate_sha256`: **`939759f9406007a848d1edcdaf81475851a7986be1902835dc32a4d6b201dd72`**

Exact PDF:

- path: `surveys/special/SP001/main.pdf`
- storage: `REPOSITORY_FILE`
- SHA-256: **`6b95ab34a2ba56cee399f989470d439bea62df2cb36113ee96a211abc030d0d3`**
- byte count: **241,198**
- page count: **7**

Validated reader source:

- path: `surveys/special/SP001/main.tex`
- SHA-256: `64973b3d53edd56d5b6b5d82d6463042189b79224e2136548ebbfd46d3faeece`
- byte count: 21,723

Reader Manuscript Manifest:

- path: `sources/SP001/publication/v2/reader-manuscript-v2.json`
- SHA-256: `97aa714d3be206c2db4f21725d2aff9e509f0820f9a186b95346eb70e6c938b8`
- byte count: 20,673

Quality Regression Bundle:

- path: `sources/SP001/publication/v2/quality-regression-bundle-v2.json`
- SHA-256: `7e637b0bb7e513800d213cee7796f3ef7fde97b8409960510e9f099d84aa49d1`
- byte count: 3,051

Semantic / Editorial Review:

- path: `sources/SP001/publication/v2/semantic-editorial-review-v2.json`
- SHA-256: `16194334e145662151401f0eff6fcda29f5679583ff8e46f5f6d19104f3e68bd`
- byte count: 5,248

Visual Review:

- path: `sources/SP001/publication/v2/visual-review-v2.json`
- SHA-256: `b0ff50c27b9849f4de414a0bfaef2fc4296e0d659e5180b34326e7b00e18bc07`
- byte count: 2,531

Useful GitHub review URLs:

- PDF: `https://github.com/eariver/japanese-generative-ai-survey/blob/aa5b0665cf96546c88601883eac82819f1e428f1/surveys/special/SP001/main.pdf`
- Candidate: `https://github.com/eariver/japanese-generative-ai-survey/blob/aa5b0665cf96546c88601883eac82819f1e428f1/sources/SP001/publication/v2/publication-candidate-v2.json`
- reviewed commit: `https://github.com/eariver/japanese-generative-ai-survey/commit/aa5b0665cf96546c88601883eac82819f1e428f1`

---

## 4. Reader Publication Validation work completed in this session

### 4.1 Clean reader publication source

The reader-facing Longform publication was generated from the approved six-package Draft / Profile Synthesis. Old five-section publication material was not used as authority.

Final structure follows the approved six packages:

1. plural foundations
2. DeepSeek
3. Qwen
4. GLM
5. Kimi
6. frontier synthesis

Technical Notes and primary-source References follow the body.

The publication preserves the approved boundaries, including:

- chronology does not imply direct influence or institutional ancestry
- architecture convergence does not imply organizational lineage
- open weight is not generalized into a single open-source category
- repository license is not silently treated as checkpoint/model-weight license
- benchmark conditions remain source-local
- FLOP / cost / parameter accounting is not normalized into an unsupported cross-family league table
- current-state claims are bounded as of 2026-08-24

References are limited to the accepted primary-source set used by the Evidence authorities.

### 4.2 PDF visual repair

The first clean PDF build produced 8 pages, but visual inspection found a real defect:

- page 3 contained only the final few Table-of-Contents entries and was otherwise almost empty.

This was not accepted as PASS.

The source was repaired only at the TOC hierarchy/layout level. No factual prose, evidence, Architecture placement, citation semantics, or final synthesis content was changed.

The corrected build converged to the current 7-page PDF.

All 7 pages of the exact final PDF SHA `6b95ab34...0d0d3` were rendered and visually inspected. The final Visual Review records no remaining blocking defect such as clipping, overlap, broken glyphs, black blocks, orphan pages, or grotesque whitespace.

### 4.3 QA authority generation

The corrected exact source/PDF pair was rebound through the current Core reader/publication validation path.

The resulting authority set includes:

- deterministic quality checks
- semantic/editorial checks
- thematic research closure checks
- Longform technical depth
- TOC hierarchy visual check
- Technical Notes tail check
- Longform page balance
- exact-PDF visual review

The `DRAFT_COMPLETE -> VALIDATED_DRAFT` Core stage contract passed before the canonical advance was executed.

### 4.4 Publication Candidate

`survey_publication_v2.build_candidate()` and `validate_candidate()` were run against the exact canonical Reader/QA/PDF authorities.

The candidate stage validator also passed before the candidate file was adopted into canonical SP001.

---

## 5. Architecture / Evidence context still in force

Architecture remains Human-approved revision 2.

Canonical Architecture:

- `sources/SP001/architecture-v2.json`
- raw SHA-256: `34a5e76e1cf992967b8b5200ad1eddbf4fae9ff8dbfeb9da05360cc5985c3972`

Architecture approval:

- `sources/SP001/gates/architecture-approval.json`
- SHA-256: `311ee3a97829b4f7885286fe648e5a41877ba99946ae0e44a2f10fcf489d85d2`

Approved six-package structure:

- `PKG-1-PLURAL-FOUNDATIONS`
- `PKG-2-DEEPSEEK`
- `PKG-3-QWEN`
- `PKG-4-GLM`
- `PKG-5-KIMI`
- `PKG-6-FRONTIER-SYNTHESIS`

The sixth package was added after Architecture Review r1 requested a final synthesis package while retaining the first five. Architecture Review r2 then approved the revised six-package design.

Do not rewrite Architecture or Evidence unless Publication Preview Human feedback explicitly requires a regeneration boundary that reaches those upstream stages.

---

## 6. Human Gate review history and next revision

Current review index:

- `sources/SP001/gates/review-index.json`

Existing immutable reviews:

- Architecture r1: `REQUEST_CHANGES`
- Architecture r2: `APPROVED`

There is currently **no Publication Preview review record**.

Therefore the next Publication Preview decision is:

- **`expected_revision = 1`**

Core Human Gate semantics were rechecked against current `scripts/survey_human_gate_v2.py`.

For Publication Preview, the Human Gate protocol requires:

- pending `RELEASE_CANDIDATE` state
- exact reviewed Production State bytes
- exact Publication Candidate bytes
- exact Candidate-bound PDF bytes
- a real Git commit containing those exact bytes
- that commit must remain reachable from the canonical work branch

The current intended reviewed commit is:

- **`aa5b0665cf96546c88601883eac82819f1e428f1`**

If `special/SP001-v2-work` moves before the Human decision is recorded, do **not** silently treat the new head as reviewed. The Human review must remain tied to exact reviewed bytes.

---

## 7. What the next ChatGPT session must do first

On session start, do not immediately mutate anything.

First re-read:

1. current `main` HEAD
2. current `special/SP001-v2-work` HEAD
3. `sources/SP001/production-state.json`
4. `sources/SP001/publication/v2/publication-candidate-v2.json`
5. `sources/SP001/gates/review-index.json`
6. PR #472 state/head

Expected safe state if nothing changed:

- SP001 branch HEAD = `aa5b0665cf96546c88601883eac82819f1e428f1`
- lifecycle = `RELEASE_CANDIDATE`
- Publication Preview = pending
- next action = `PUBLICATION_PREVIEW`
- Publication Candidate = `READY_FOR_PUBLICATION_PREVIEW`
- candidate PDF SHA = `6b95ab34a2ba56cee399f989470d439bea62df2cb36113ee96a211abc030d0d3`
- next Publication Preview revision = 1

If those differ, stop and re-evaluate before applying any Human decision.

---

## 8. If the Human says APPROVED

Do **not** interpret silence or a generic continuation request as approval. Require an explicit approval statement for the Publication Preview.

Once explicit approval is present:

1. Reconfirm the reviewed surface is still the exact commit `aa5b0665...` and exact Candidate/PDF bytes above.
2. Reconfirm current `main` and trusted Core authority before forming the operator request.
3. Create a new immutable request-only child commit on `special/SP001-v2-work` for:
   - operation: `RECORD_PUBLICATION_PREVIEW_APPROVAL`
   - `expected_revision`: `1`
   - `reviewed_repository_commit_sha`: **`aa5b0665cf96546c88601883eac82819f1e428f1`**
   - canonical state path: `sources/SP001/production-state.json`
   - Human identity/reference/timestamp from the explicit review turn
4. The request-only commit must not contain unrelated artifacts.
5. The connector/trusted workflow preflight used in this project additionally requires the reviewed repository commit to be the request-only commit parent for Human Gate execution. Therefore, if the canonical branch has moved after Human review, do not manufacture a different reviewed commit; reassess the review surface.
6. Let the trusted default-branch operator bridge record:
   - canonical Publication Preview approval
   - immutable approval snapshot
   - `publication-r1.json` review record
   - updated `review-index.json`
   - Production State transition/control updates
7. Only after that explicit Human approval has been durably recorded should Freeze / Release processing continue under the current reviewed Core.
8. Never merge PR #472; it is transport only.

Do not approve on behalf of the Human.

---

## 9. If the Human says REQUEST_CHANGES

The next Publication Preview review is still revision 1.

Use:

- operation: `REQUEST_PUBLICATION_PREVIEW_REVISION`
- `expected_revision`: `1`
- reviewed commit: exact commit actually reviewed by the Human
- non-empty `requested_changes`
- Human-selected regeneration boundary

Allowed Publication Preview regeneration boundaries in the current schema are:

- `ISSUE_INITIALIZED`
- `DISCOVERY_COLLECTED`
- `CANDIDATES_NORMALIZED`
- `EVIDENCE_REVIEWED`
- `SELECTION_COMPLETE`
- `ARCHITECTURE_ESTABLISHED`
- `DRAFT_COMPLETE`
- `VALIDATED_DRAFT`

Do not turn ordinary review feedback into Owner Exception.

If feedback reaches upstream of `ARCHITECTURE_ESTABLISHED`, the Human Gate protocol can reopen the previously approved Architecture as a normal cross-gate revision. Preserve the immutable prior approval snapshot/history.

The Human Gate module will selectively invalidate superseded downstream checkpoint authority and return Production State to the requested regeneration boundary. Do not hand-edit that lifecycle consequence.

---

## 10. Publication Preview export workflow note

Workflow:

- `.github/workflows/survey-production-v2-export-publication-preview.yml`

The run triggered by the final bot-generated canonical head:

- run `32981328675`
- conclusion: `action_required`
- jobs list was empty

This is **not** the Core candidate advance result and does not invalidate the canonical Human Gate authority.

The workflow is only an exact-byte export convenience. The canonical Publication Preview authority is already durable in the repository commit through:

- Production State
- Publication Candidate
- repository-resident exact PDF

If the next session needs an Actions artifact export, investigate/re-run the export separately. Do not change Candidate/PDF bytes merely to make the export UI green.

---

## 11. Core maintenance encountered during this production

During SP001 Drafting, a genuine generic Core defect was found in the interactive cross-package synthesis reference resolver.

Issue:

- final synthesis package had no direct Architecture candidate placements by design
- old interactive runner incorrectly restricted reference resolution to direct placements
- package 6 therefore could not legally reference accepted cross-package Evidence despite the Draft Package already containing validated `evidence_inputs`

Fix:

- use validated Draft Package `evidence_inputs` as the allowed Evidence reference set
- preserve fail-closed behavior for unauthorized Matrix rows, ambiguous IDs, and duplicate candidate IDs

PR:

- #470 `Core v2: fix interactive cross-package Draft reference resolution`
- frozen audited head: `7fa8dd62e16e0f90359d8fe9999c3b92cb039811`
- Human approved in this chat
- merged commit: `94168050ae1161f92b594e13706c692c533c4139`

Validation before merge:

- Core v2 full regression suite: 245 tests OK, 6 skipped
- Pipeline contract tests: 698 tests OK, 6 skipped
- real SP001 six-package diagnostic: PASS
- fresh fixed-head audit: 7/7 PASS

No further generic Core defect is known at this checkpoint.

---

## 12. Reader Validation execution history worth preserving

Reader Validation initially encountered two fail-closed request issues that were resolved without weakening Core:

1. `reviewed_main_sha` was initially pinned too old, so trusted preflight correctly rejected protected Core drift after PR #470.
2. semantic review authority was initially stored as `semantic-review-v2.json`, while current Core canonical path is `semantic-editorial-review-v2.json`.

Resolution:

- old requests remain immutable history
- semantic review bytes were not changed; only the canonical filename was corrected
- r3 request passed trusted preflight and Core execution
- canonical state advanced to `VALIDATED_DRAFT`

This is useful diagnostic history if old request records are encountered in the branch.

---

## 13. Temporary / transport objects and cleanup debt

Many temporary branches exist from production and diagnostics. They are not current authority.

Notable examples seen during this session include:

- `transport/SP001-drafting-materialization-r1`
- `transport/SP001-drafting-materialization-r2`
- `transport/sp001-reader-publication-r1`
- `transport/sp001-reader-build-r1`
- `transport/sp001-reader-fix-toc-r1`
- `transport/sp001-reader-visual-r1`
- `transport/sp001-reader-visual-r2`
- `transport/sp001-reader-authority-r1`
- `transport/sp001-publication-candidate-r1`
- `tmp-noop-do-not-use`
- `maintenance/core-v2-interactive-cross-package-refs-test-noop`

Also:

- diagnostic PR #469 was closed unmerged
- Core maintenance PR #470 was merged after Human approval
- clean Draft materialization PR #471 was transport-only
- PR #472 remains the active transport trigger surface and must not be merged

Do not resume production from any temporary/diagnostic branch. Use `special/SP001-v2-work` only.

Cleanup can be performed after release or in a dedicated maintenance task; cleanup must not alter the pending Human review surface.

---

## 14. Accidental main temporary file incident

While probing GitHub file-write behavior during Reader Publication work, an accidental temporary `dummy` file was briefly created on `main` because a branch argument was omitted.

It was immediately and explicitly reverted.

Current `main` checkpoint HEAD is:

- `079dac9605e4cf55a239de6f03e37a93f756a918`
- commit message: `Revert accidental temporary file`

No SP001 publication authority was derived from the accidental file. The incident should not be repeated; all future repository writes must name the intended branch explicitly.

---

## 15. Current Human Review prompt

The next session should present or preserve the following decision boundary:

**SP001 Publication Preview Human Gate**

Human should review the exact 7-page PDF at commit `aa5b0665...` and respond with one of:

- `APPROVED`
- `REQUEST_CHANGES` plus requested changes (and, for protocol execution, the intended regeneration boundary)

No Freeze, Release, tag, final merge, or Publication Preview approval may be performed until the Human explicitly decides.

---

## 16. Recommended next-session bootstrap prompt

A short user message sufficient to resume is:

> `docs/checkpoints/sp001-publication-preview-handoff-20260826.md` を参照し、GitHub上の現状と照合してSP001のPublication Preview Human Gateから再開してください。

If the Human has already reviewed the PDF, they can append their explicit decision in the same turn, e.g.:

> 上記checkpointを確認して再開してください。Publication PreviewはAPPROVEDです。

or:

> 上記checkpointを確認して再開してください。Publication PreviewはREQUEST_CHANGESです。…

---

## 17. Final checkpoint summary

At checkpoint creation:

- Core maintenance #470: Human-approved and merged
- SP001 Architecture Review: approved r2
- six-package Drafting: complete
- Reader Publication Validation: complete
- exact final PDF: 7 pages, visual-reviewed
- Publication Candidate: complete and validated
- lifecycle: **RELEASE_CANDIDATE**
- terminal reason: **HUMAN_GATE_REACHED**
- Publication Preview: **pending**
- next Human review revision: **1**
- canonical reviewed commit: **`aa5b0665cf96546c88601883eac82819f1e428f1`**
- canonical PDF SHA-256: **`6b95ab34a2ba56cee399f989470d439bea62df2cb36113ee96a211abc030d0d3`**
- no Human Publication Preview decision has been recorded yet

**Safe stop point: Publication Preview Human Gate.**
