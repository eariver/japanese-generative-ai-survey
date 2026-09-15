# W35 execution instruction — Architecture Review r2 APPROVED through Publication Preview

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R2_APPROVED / CONTINUE_TO_PUBLICATION_PREVIEW`

Date: `2026-09-15 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W35-v2-work`

## 1. Human decision authority

The Human has explicitly reviewed the W35 Architecture Review r2 and decided:

`APPROVED`

Exact reviewed production authority:

`7692f618488fe27bf298a7a90648a009ae9b0ffb`

Architecture Review r2 presentation shell:

`840fc1ce40e5ef759feee8d4fcb86945318057a2`

The r2 decision is approval of the existing Architecture bytes. Do not reinterpret this approval as permission to modify Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture before drafting.

The prior r1 decision remains historically valid as `REQUEST_CHANGES`, revision 1, boundary `SELECTION_COMPLETE`. This instruction records the new r2 decision as the next Architecture Review revision and does not overwrite r1 provenance.

## 2. Mission

Record the Human Architecture Review r2 decision through the canonical Human Gate protocol, verify the resulting immutable approval authority, then continue W35 production autonomously through drafting, canonical validation, publication rendering/candidate construction, and all required pre-publication reader-surface checks until the next Human Gate:

`PUBLICATION_PREVIEW`

Normal terminal state for this run is the fresh Publication Preview Human Gate pending, with a durable reviewable PDF/candidate and no Publication Preview Human decision recorded.

Do **not** Freeze or Release in this run.

## 3. Starting guard

The Muse invocation will supply the Exact Starting SHA equal to the commit containing this execution request.

Before any repository/GitHub write, read-only verify all of the following:

- remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- Exact Starting SHA parent == `840fc1ce40e5ef759feee8d4fcb86945318057a2`;
- remote `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `main` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- current W35 Production State reports `ARCHITECTURE_ESTABLISHED`, `next_action = ARCHITECTURE_REVIEW`, `terminal_reason = HUMAN_GATE_REACHED`, and Architecture Review pending;
- `sources/2026-W35/execution/reviews/architecture-r2.md` identifies reviewed production authority `7692f618488fe27bf298a7a90648a009ae9b0ffb` and r2 decision still `PENDING` before this approval is recorded;
- `sources/2026-W35/architecture-v2.json` is the reviewed r2 Architecture with corrected thesis/P1 framing;
- candidate Selection remains `17 SELECTED / 2 HOLD` and its accepted authority is unchanged from r2 review.

If any guard differs, perform no repository/GitHub write, report expected versus actual, and STOP.

No force push, reset, rewrite, fallback branch, alternate W35 branch, or unsolicited Core repair branch is authorized.

## 4. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W35/execution/reviews/architecture-r2.md`
2. `sources/2026-W35/execution/reviews/architecture-r2-dossier.md`
3. this execution request
4. `sources/2026-W35/production-state.json`
5. `sources/2026-W35/architecture-v2.json`
6. `sources/2026-W35/architecture-review-summary-v2.json`
7. `sources/2026-W35/candidate-selection-v2.json`
8. current canonical Human Gate implementation/contracts, especially `scripts/survey_human_gate_v2.py`
9. current canonical drafting / validation / publication / reader-surface pipeline contracts and commands from the reviewed Core implementation.

Repository-local current Core behavior is authoritative. Do not use Google Drive.

## 5. Record Architecture Review r2 APPROVED

Use the canonical Human Gate protocol to record the explicit Human decision against the exact reviewed r2 bytes.

Required semantics:

- gate: `ARCHITECTURE_REVIEW`
- next Architecture review revision: `2`
- decision: `APPROVED`
- reviewed repository production commit SHA: `7692f618488fe27bf298a7a90648a009ae9b0ffb`
- reviewed_by: `Human Owner`
- review reference: this execution request plus the r2 Human-facing review surface
- requested changes: none
- regeneration boundary: none

Use the canonical tool's actual execution timestamp for the decision record. Do not invent an earlier exact Human action timestamp.

After recording approval, verify all generated review-index / review-record / immutable approval-snapshot authorities and confirm the lifecycle consequence is the one defined by the current Core contract.

If the canonical Human Gate implementation refuses the approval because reviewed bytes, revision identity, state, or provenance do not match, STOP rather than bypassing the guard.

## 6. Drafting authority

After Architecture r2 approval is validly recorded, draft the W35 edition from the approved Architecture and accepted Evidence only.

Preserve all load-bearing evidence boundaries established in r2, especially:

- P1 must not reintroduce a cluster-wide `sub-5%` claim;
- GLM / Qwen / Hy4 activation ratios are model-specific and PARTIAL where recorded;
- licenses are stated per model and only at the authority level actually verified;
- no cluster-wide offload/memory-mechanism claim;
- Qwen 4 proper must not be presented as released;
- vendor benchmarks and publisher measurements remain clearly attributed/unreproduced where required;
- X/Grok material is community/social observation, not technical authority;
- PARTIAL evidence must not be silently promoted to VERIFIED prose;
- HOLD items remain outside the selected Architecture unless the canonical downstream process has an explicit non-promotional context surface.

Do not perform fresh research merely to improve prose. If drafting exposes a genuine factual contradiction or missing authority that makes approved Architecture unusable, STOP with the exact blocking condition rather than silently changing upstream authority.

## 7. Volume / compression policy for this run

The Human has explicitly stated that ordinary issue length or compression preference is **not** a reason to stop production.

Therefore:

- do not invent a separate compression Human Gate;
- do not stop merely because the draft/PDF is around the expected normal weekly range or somewhat longer;
- do not force a target page count by deleting selected material;
- prioritize coherent synthesis, evidence-bound prose, readability, and the approved five-package Architecture;
- only treat volume as blocking if the output is clearly pathological (for example, severe layout failure, gross duplication, unreadable density, or a canonical quality/reader-surface gate failure).

Any normal editorial compression that the canonical drafting/rendering process performs is allowed, but it must not alter Selection/Architecture authority or erase load-bearing caveats.

## 8. Validation and reader-surface requirements

Run the current canonical downstream pipeline from the approved Architecture through the stages required before Publication Preview.

At minimum ensure that all current Core-required checks execute successfully, including any applicable:

- draft/schema validation;
- evidence/citation/provenance binding checks;
- architecture-to-draft coverage checks;
- publication candidate validation;
- TeX/PDF generation and durable PDF authority recording;
- lexical reader-surface validation;
- persisted semantic reader-surface review gate;
- other current publication-profile validations required before `PUBLICATION_PREVIEW`.

The pre-publication reader-surface semantic review must be genuinely produced/consumed according to the current Core contract. Production code must not manufacture a semantic PASS.

If a generic reusable Core defect is discovered, follow the existing Core-repair / Production-Line policy rather than patching around it edition-locally. If the issue is edition-local content/data, repair only within the W35 branch and within the smallest valid regeneration boundary.

Do not merge W35 to `main`.

## 9. Publication Preview deliverables

Before stopping, make the next Human review practical and auditable. Produce the canonical Publication Preview surface required by the Core, including at least:

- durable publication candidate authority;
- durable PDF authority with exact path, SHA-256, byte count, and page count if available from the canonical tooling;
- current Production State showing the Publication Preview Human Gate pending;
- machine validation summaries required by the profile;
- a Human-facing Publication Preview review dossier/checkpoint summarizing:
  - exact reviewed production commit;
  - Architecture approval provenance;
  - final package/section structure;
  - page count and high-level layout;
  - evidence-boundary carry-through;
  - reader-surface lexical/semantic results;
  - known non-blocking residual limitations;
  - any material deviations from the approved Architecture;
  - exact PDF authority.

Do not record a Publication Preview Human decision.

## 10. Commit / push discipline

Use the existing W35 branch only.

For every repository write sequence:

- preserve normal parentage;
- use normal commits;
- push non-force only;
- read back remote HEAD after push;
- do not rewrite or squash away review/gate provenance;
- retain the r1 REQUEST_CHANGES and r2 APPROVED records as immutable history.

If remote HEAD changes unexpectedly before a write, STOP and report expected versus actual.

## 11. Normal STOP condition

Normal successful terminal condition:

- Architecture Review r2 = canonically `APPROVED`;
- Draft and required downstream publication artifacts generated;
- all required pre-Publication-Preview machine/reader-surface gates passed;
- lifecycle at the current Core-defined Publication Preview stop (normally `RELEASE_CANDIDATE`);
- `PUBLICATION_PREVIEW` Human Gate = `pending`;
- no Publication Preview Human decision generated;
- no Freeze;
- no Release;
- `main` untouched;
- Production Line untouched unless an explicitly authorized and completed generic Core repair process required otherwise;
- fresh Human-facing Publication Preview dossier/checkpoint committed and remote-read-back verified.

Then STOP and report the exact remote HEAD/tree, reviewed publication authority, PDF path/SHA/bytes/pages, validation status, and the Publication Preview review surface for Sol/Human review.
