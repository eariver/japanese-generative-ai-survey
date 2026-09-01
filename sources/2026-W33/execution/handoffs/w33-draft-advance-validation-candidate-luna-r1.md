# 2026-W33 Draft checkpoint + Validated Draft candidate — Luna handoff r1

## Purpose

Take the Sol-accepted complete W33 Draft candidate set through the **deterministic Draft checkpoint**, then in the same bounded Luna work unit author, compile, inspect, validate, and internally repair the complete reader-facing W33 publication candidate surface required for the next `DRAFT_COMPLETE -> VALIDATED_DRAFT` transition.

Do **not** perform that second transition.

This unit intentionally combines:

1. cheap deterministic acceptance of the already-reviewed Draft set; and
2. expensive reader-manuscript / LaTeX / exact-PDF / quality / semantic / visual candidate generation and local repair.

The Sol review boundary remains before `VALIDATED_DRAFT`, so a publication-layout/editorial defect can still be repaired without rolling back the validated-draft checkpoint.

Normal completion status:

`VALIDATED_DRAFT_CANDIDATE_READY_FOR_SOL_REVIEW`

## Repository authority

Repository:

`eariver/japanese-generative-ai-survey`

Branch:

`weekly/2026-W33-v2-work`

The caller will provide an **Exact Starting SHA**. Before any GitHub write, verify that the remote branch HEAD exactly equals that caller-supplied SHA.

If it does not match:

- perform no GitHub write;
- report the actual remote HEAD;
- stop.

Reviewed-main Core authority:

`6267de3f6876f491950139757bfdf1085fc07bdc`

Shared Core/config/schema/workflow authority is read-only.

Do not modify reviewed-main Core or backport/reinterpret its contracts.

## Mandatory starting State

Read:

`sources/2026-W33/production-state.json`

Required starting values:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- Architecture Human Gate: `approved`
- Architecture checkpoint: `passed`
- Draft checkpoint: `pending`
- `next_action = stage:drafting-synthesis`
- `terminal_reason = null`
- Publication Preview: `pending`
- Exception Gate: `inactive`

Required starting Production State SHA-256:

`2112dddfa5c6f8f55ec3d497ee4a633e16d2d1899436270d76f6423ec30f0d08`

If State does not match, stop `NEEDS_SOL_REVIEW` without writes.

## Mandatory read order

Read and use authority in this order.

### A. Current control / review authority

1. `sources/2026-W33/production-state.json`
2. `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/reviews/w33-draft-candidate-set-sol-review-20260831-r1.md`
4. `sources/2026-W33/execution/sessions/w33-luna-draft-candidate-set-20260831-r1.md`
5. `sources/2026-W33/gates/architecture-approval.json`
6. `sources/2026-W33/architecture-v2.json`
7. `sources/2026-W33/architecture-review-summary-v2.json`
8. `sources/2026-W33/production-profile.json`

### B. Exact accepted Draft candidate authority

Read all 16 candidate artifacts:

Draft Packages:

1. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-frontier-models-access.json`
2. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-cyber-access-governance.json`
3. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-serving-runtime.json`
4. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-memory-decoding-systems.json`
5. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-agent-evaluation-reliability.json`
6. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-multimodal-media.json`
7. `sources/2026-W33/drafting/v2/luna-r1/packages/w33-week-in-review.json`

Draft Results:

8. `sources/2026-W33/drafting/v2/luna-r1/results/w33-frontier-models-access.json`
9. `sources/2026-W33/drafting/v2/luna-r1/results/w33-cyber-access-governance.json`
10. `sources/2026-W33/drafting/v2/luna-r1/results/w33-serving-runtime.json`
11. `sources/2026-W33/drafting/v2/luna-r1/results/w33-memory-decoding-systems.json`
12. `sources/2026-W33/drafting/v2/luna-r1/results/w33-agent-evaluation-reliability.json`
13. `sources/2026-W33/drafting/v2/luna-r1/results/w33-multimodal-media.json`
14. `sources/2026-W33/drafting/v2/luna-r1/results/w33-week-in-review.json`

Synthesis:

15. `sources/2026-W33/drafting/v2/luna-r1/synthesis-input.json`
16. `sources/2026-W33/drafting/v2/luna-r1/synthesis-result.json`

The candidate hashes recorded in the Luna session are frozen input authority. Do not revise these 16 files in this task.

### C. Reviewed-main Draft acceptance / reader-publication authority

Read from exact reviewed-main SHA `6267de3f6876f491950139757bfdf1085fc07bdc`:

1. `config/survey-production-v2.json`
2. `scripts/survey_stage_validation_v2.py`
3. `scripts/survey_agent_control_v2.py`
4. `scripts/survey_agent_tool_v2.py`
5. `scripts/survey_drafting_v2.py`
6. `scripts/survey_reader_publication_v2.py`
7. `scripts/survey_reader_fidelity_v2.py`
8. `scripts/survey_quality_v2.py`
9. `scripts/survey_publication_v2.py`
10. `config/publication-review-v2.json`
11. all schemas referenced by those modules for Reader Manuscript, quality bundle, semantic review, visual review, and publication-stage artifacts
12. publication / quality contract files referenced by current Production Profile

Do not guess a schema field, review check, artifact name, transition, or output contract when Core can derive it.

### D. Layout reference only

You may inspect:

`surveys/weekly/2026-W32/**`

only as a **non-factual layout / LaTeX convention reference**, including:

- `jlreq`
- `jgaisurvey`
- `.latexmkrc`
- `main.tex` composition pattern
- section-file organization
- bibliography mechanics

W32 prose, facts, editorial selection, citations, and content are **not authority for W33** and must not be copied as W33 factual content.

## Phase 1 — deterministically accept the reviewed Draft set

This phase must be mechanically narrow.

### 1. Revalidate frozen Draft authority

Before creating any request, rerun the canonical reviewed-main validators over the exact current 7 Draft Package / 7 Draft Result / Synthesis Input / Synthesis Result set.

Required:

- all 7 Draft Packages validate;
- all 7 Draft Results validate;
- Profile/Publication extension propagation validates;
- canonical Synthesis Input derivation equals the committed input exactly;
- Synthesis Result validates;
- Architecture approval remains valid;
- no accepted upstream authority drift is detected.

If any validation fails, stop `NEEDS_SOL_REVIEW`. Do not repair the frozen Draft files in this task.

### 2. Materialize exactly one Draft stage transition

Use the repository's canonical trusted operator bridge and normal non-force branch updates.

Operation:

`ADVANCE_STAGE`

Expected source lifecycle:

`ARCHITECTURE_ESTABLISHED`

Current-stage artifact set must contain exactly:

- `synthesis-input`
- `synthesis-result`
- `draft-package:w33-frontier-models-access`
- `draft-result:w33-frontier-models-access`
- `draft-package:w33-cyber-access-governance`
- `draft-result:w33-cyber-access-governance`
- `draft-package:w33-serving-runtime`
- `draft-result:w33-serving-runtime`
- `draft-package:w33-memory-decoding-systems`
- `draft-result:w33-memory-decoding-systems`
- `draft-package:w33-agent-evaluation-reliability`
- `draft-result:w33-agent-evaluation-reliability`
- `draft-package:w33-multimodal-media`
- `draft-result:w33-multimodal-media`
- `draft-package:w33-week-in-review`
- `draft-result:w33-week-in-review`

Use the exact repository paths above.

The semantic review authority for the request is:

`sources/2026-W33/execution/reviews/w33-draft-candidate-set-sol-review-20260831-r1.md`

Decision:

`ACCEPT / DRAFT_CANDIDATE_SET_SEMANTICS_VERIFIED / READY_FOR_DRAFT_CHECKPOINT_AND_VALIDATED_DRAFT_CANDIDATE`

Use a clear agent-review check identifier such as:

`SOL_DRAFT_CANDIDATE_SET_SEMANTIC_REVIEW`

subject to the exact reviewed-main request/check contract. If Core requires a different machine representation, follow Core rather than inventing a new field.

### 3. Bridge discipline

Required:

- immutable request JSON;
- request-only commit;
- `reviewed_repository_commit_sha` bound exactly according to current trusted operator contract;
- canonical operator transport;
- Preflight PASS;
- Execute PASS;
- exactly one `ADVANCE_STAGE` operation;
- no force push;
- bridge result must be a normal descendant of request-only commit;
- read back receipt, checkpoint, and Production State after execution.

If the branch moves unexpectedly before request/ref update, stop rather than force or rebase around an unknown writer.

### 4. Expected Phase-1 result

The resulting lifecycle must be the Core-derived Draft-complete lifecycle, expected as:

`DRAFT_COMPLETE`

The Draft checkpoint must be `passed` with non-null provenance.

Architecture and all previous checkpoint/Human-Gate authority must remain unchanged.

Do not proceed to Phase 2 unless Phase 1 is fully valid.

## Phase 2 — author the complete reader-facing W33 source

Create a new canonical survey root:

`surveys/weekly/2026-W33/`

It does not exist at task start.

### Reader-facing source authority

The factual/content authority for the reader manuscript is the **seven Sol-accepted Draft Results**.

You may use the seven Draft Packages only for:

- Evidence identity mapping;
- source title / URL / author / date / attribution metadata already embedded in accepted Evidence Cards;
- building accurate bibliography/source-note metadata;
- preserving Evidence limitations and subject roles.

Do not use Draft Package Evidence Cards to add a new substantive factual claim that does not appear in the accepted Draft Result semantic content.

No Web, Google Drive, Raw capture, external browsing, new source collection, or fresh Evidence research is permitted.

### Required chapter structure

The reader manuscript must visibly preserve the seven approved Architecture packages as the substantive structure:

1. Frontier Models & Access
2. Cyber Access & Governance
3. Serving & Runtime
4. Inference Systems Deep Dive — memory / prefetch / decoding
5. Agent Reliability
6. Multimodal Media
7. Week in Review

The final `Week in Review` chapter is mandatory and independent. It must visibly answer:

- what changed this week;
- why the changes matter together;
- what to watch next.

It must not collapse into frontmatter, a contents page, source notes, references, or a one-paragraph afterword.

### Weekly community movement

The active Weekly reader contract requires `WEEKLY_COMMUNITY_MOVEMENT`.

Satisfy it with an explicit reader-facing block that uses **only the already accepted X/community contextual Evidence present in the accepted Draft authority**.

It must state the epistemic boundary clearly:

- community/X material is contextual signal;
- it is not technical authority;
- it must not establish benchmark, performance, launch, or capability facts.

Do not perform new X research.

### Editorial transformation allowed

You may transform the Draft Results into magazine-quality Japanese prose by:

- expanding transitions;
- splitting/merging paragraphs;
- converting structured Draft TABLE blocks into reader tables;
- adding headings/subheadings;
- shortening repetitive language;
- adding editorial signposting;
- arranging page hierarchy;
- turning explicit boundaries into callouts/source notes;
- improving Japanese fluency and rhythm.

You may **not**:

- introduce a new factual claim;
- change a numerical value;
- remove a material limitation;
- convert vendor/project/paper-reported claims into unqualified fact;
- imply interoperability that accepted Drafts explicitly deny;
- backdate chronology/context records;
- reintroduce rejected/HOLD candidates as W33 substantive developments;
- create a new candidate or Architecture destination.

### Page plan

Approved Architecture:

- target: 18 pages
- hard maximum: 24 pages

Treat 18 as an editorial target, not a license to pad with unsupported content.

Hard requirement:

- final exact PDF page count must not exceed 24.

Prefer a compact magazine-quality issue over invented filler.

## Phase 3 — bibliography / source notes

Create accurate W33 bibliography/source-note support under the canonical survey root.

References must be traceable to accepted Draft/Evidence authority.

Use embedded accepted Evidence metadata when the Draft Result needs a citation target.

Do not fetch bibliographic metadata from the live Web.

Maintain clear attribution for:

- first-party release/changelog claims;
- project-reported performance/timing;
- paper-author-reported results;
- X/community contextual observations;
- limitations / unresolved verification boundaries.

## Phase 4 — build and internally repair exact PDF

Use the repository's canonical LuaLaTeX / `jgaisurvey` publication path under `surveys/weekly/2026-W33`.

Create an exact repository-resident PDF, preferably:

`surveys/weekly/2026-W33/2026-W33.pdf`

If current Core/profile tooling requires a different canonical filename, follow that authority and record it explicitly in the session.

The PDF used for quality and visual review must be the **same exact bytes** committed to the repository and referenced by the validation artifacts.

### Required visual inspection

Do not treat successful compilation as visual review.

Render/inspect every page of the exact final PDF and check at minimum:

- no clipped or overlapping text;
- no unreadable table columns;
- no missing Japanese glyphs;
- no broken bibliography/citation rendering;
- no stranded headings or severe orphan/widow artifacts where avoidable;
- no accidental blank pages;
- no broken cover/frontmatter hierarchy;
- no sections rendered outside intended column/page structure;
- Week in Review is visibly an independent final substantive chapter;
- source notes/references are legible;
- visual density is magazine-appropriate rather than debug/log-like.

If a visual defect is found, repair source, rebuild, and restart exact-PDF binding/review against the new bytes.

If the environment cannot actually render and inspect the PDF, stop `NEEDS_SOL_REVIEW`; do not create a fake PASS visual review.

## Phase 5 — create current Core validation candidate artifacts

Using reviewed-main current Core, create a complete candidate set for the `DRAFT_COMPLETE` stage contract.

Recommended candidate root:

`sources/2026-W33/validation/v2/luna-r1/`

Required stage artifacts are exactly the current Core-required set:

- `reader-manuscript`
- `validated-source`
- `publication-pdf`
- `quality-regression-bundle`
- `semantic-review`
- `visual-review`

The authoritative `validated-source` must be canonical:

`surveys/weekly/2026-W33/main.tex`

unless reviewed-main Core/profile explicitly requires another canonical primary source, in which case stop if that conflicts with the active Profile rather than silently changing Profile authority.

### Reader Manuscript Manifest

Build with canonical reviewed-main helper/validator.

It must:

- bind exact Production Profile;
- bind exact approved Architecture;
- bind exact Architecture Approval;
- bind exact `main.tex` bytes;
- bind all supporting `.tex`/`.bib`/publication-support files needed to reproduce the manuscript;
- cover **every** Architecture `must_cover_requirement` exactly through reader-facing locations;
- include exactly the Profile-required reader requirements;
- include `FINAL_SYNTHESIS` coverage;
- include `WEEKLY_COMMUNITY_MOVEMENT` coverage;
- pass reader-fidelity resolution to exact non-empty TeX blocks.

Do not mark a requirement `FULFILLED` merely because a field exists; the reader-facing location must contain substantive content.

### Quality Regression Bundle

Build/validate with reviewed-main `survey_quality_v2.py` and the active Profile contracts.

It must bind the exact final source and exact final PDF bytes.

All deterministic required checks must PASS.

### Semantic/editorial review

Create the canonical review record against the exact final source/PDF/manuscript authority.

The active review contract requires at least the exact current set derived from:

Core semantic:

- `PUBLICATION_BOUNDARY`
- `ARCHITECTURE_CONTENT_FIDELITY`
- `FINAL_SYNTHESIS_QUALITY`

Weekly semantic:

- `WEEKLY_COMMUNITY_MOVEMENT`

Use the exact Core-derived full check set; do not omit any additional quality/Profile checks that current helpers require.

The semantic review must verify, not merely assert:

- every Architecture package remains represented;
- every must-cover requirement is substantively present;
- limitations/attribution survive the reader transformation;
- final synthesis is genuinely cross-package;
- X/community movement remains context-only;
- no rejected/HOLD material reappears as unsupported W33 fact;
- no Draft-to-reader semantic overclaim is introduced.

### Visual review

Create the canonical visual review record against the exact final PDF bytes.

At minimum the active publication-review contract includes:

- `EXACT_PDF_VISUAL_REVIEW`

Use the complete current Core-derived visual check set.

A PASS requires actual page inspection of the exact final PDF.

## Phase 6 — local repair loop

Within this same Luna task, you are authorized to repair **only the reader-facing / validation candidate surface** when checks fail.

You may revise:

- `surveys/weekly/2026-W33/**`
- candidate validation artifacts under `sources/2026-W33/validation/v2/luna-r1/**`

Then rebuild/revalidate/re-review until all checks pass.

You may not repair by changing:

- any of the 7 accepted Draft Packages;
- any of the 7 accepted Draft Results;
- Synthesis Input/Result;
- Evidence;
- Selection;
- Architecture;
- Human Gate records;
- reviewed Core/config/schema.

If a reader-facing defect cannot be corrected without changing accepted Draft semantics, stop `NEEDS_SOL_REVIEW` and report the exact conflict.

## Phase 7 — stop before Validated Draft advancement

This is mandatory.

Do **not** execute the next `ADVANCE_STAGE` from `DRAFT_COMPLETE`.

Do not create the next Stage Checkpoint.

Do not create a Publication Candidate.

Do not record Publication Preview approval/request-changes.

Do not enter `VALIDATED_DRAFT`, `RELEASE_CANDIDATE`, freeze, or release stages.

Expected final Production State:

- lifecycle: `DRAFT_COMPLETE`
- Draft checkpoint: `passed`
- validation checkpoint: `pending`
- Publication Preview: `pending`
- Exception Gate: `inactive`

The exact `next_action` must be whatever current Core sets for this lifecycle; record it rather than inventing it.

## Git / write boundary

Allowed write surfaces for this task are limited to:

### Phase-1 deterministic transition

- one immutable Draft-advance request under `sources/2026-W33/execution/requests/`
- one corresponding bridge-run directory under `sources/2026-W33/execution/bridge-runs/`
- the canonical Draft Stage Checkpoint created by Core
- `sources/2026-W33/production-state.json`

### Reader/publication candidate

- `surveys/weekly/2026-W33/**`
- `sources/2026-W33/validation/v2/luna-r1/**`

### Bookkeeping

- exactly one Luna session record:
  `sources/2026-W33/execution/sessions/w33-luna-draft-advance-validation-candidate-20260831-r1.md`

Do not modify `sources/2026-W33/execution/index.md`; Sol owns recovery-index update after review.

No new branch, review branch, alternative branch, force push, or history rewrite.

## Required final session record

Record at minimum:

- caller Exact Starting SHA;
- actual remote HEAD at start;
- pre-write remote recheck;
- reviewed-main SHA;
- Phase-1 request path/hash/commit;
- transport / workflow run identity;
- Preflight and Execute result;
- bridge result commit;
- exact Stage Checkpoint path/hash;
- State before/after hashes and lifecycle;
- proof Draft candidate files remained byte-unchanged;
- canonical survey-root file inventory and SHA-256 values;
- exact PDF path/hash/byte count/page count;
- Reader Manuscript path/hash;
- Quality Bundle path/hash;
- Semantic Review path/hash and complete check outcomes;
- Visual Review path/hash and complete check outcomes;
- evidence that every PDF page was actually visually inspected;
- architecture coverage count and reader requirement disposition;
- exact list of local reader/layout repairs performed;
- exact changed-path inventory;
- explicit confirmation of no fresh research;
- explicit confirmation that no `DRAFT_COMPLETE -> VALIDATED_DRAFT` advancement occurred;
- final remote HEAD.

Normal final status:

`VALIDATED_DRAFT_CANDIDATE_READY_FOR_SOL_REVIEW`

## Stop conditions

Stop `NEEDS_SOL_REVIEW` without broadening scope if any of the following occurs:

- starting remote HEAD mismatch;
- starting State mismatch;
- frozen Draft candidate authority drift;
- Draft revalidation failure;
- Core stage-contract failure;
- operator bridge Preflight/Execute failure;
- unexpected branch writer/drift;
- Draft transition does not yield the Core-expected Draft-complete lifecycle;
- reader manuscript cannot cover an Architecture must-cover requirement without changing accepted Draft semantics;
- required bibliography/source metadata is absent from accepted authority and would require fresh research;
- quality validator cannot pass without changing protected authority;
- exact PDF cannot be compiled;
- exact PDF cannot actually be rendered/visually inspected;
- PDF exceeds the 24-page hard maximum;
- semantic review finds an unrepairable factual/attribution/Architecture fidelity defect;
- visual review finds an unrepairable publication defect;
- a second lifecycle advancement would be required to continue.

Do not weaken a check, invent evidence, omit a requirement, or cross the stop boundary to make the task appear complete.
