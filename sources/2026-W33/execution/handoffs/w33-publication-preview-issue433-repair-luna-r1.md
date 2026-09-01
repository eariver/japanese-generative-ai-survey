# W33 Publication Preview Issue #433 Repair — Luna Handoff r1

## Purpose

Execute the Owner's explicit Publication Preview `REQUEST_CHANGES` decision, roll the canonical lifecycle back to `DRAFT_COMPLETE`, and rebuild only the W33 reader/publication transformation so that the replacement publication actually satisfies Issue #433.

This is a bounded publication repair. It is **not** a new research pass, Architecture revision, Selection revision, or Draft semantic re-authoring pass.

## Repository authority

- Repo: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Use the Exact Starting SHA supplied with the external invocation as the only allowed starting remote HEAD.
- Before the first write, verify the remote branch HEAD exactly equals that SHA. If it differs, perform no GitHub write and stop with the actual remote HEAD.

## Mandatory reads

Read these before editing or creating an operator request:

1. `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r1.md`
2. `sources/2026-W33/execution/reviews/w33-publication-preview-issue433-sol-review-20260901-r1.md`
3. GitHub Issue `#433` and its acceptance criteria
4. `sources/2026-W33/production-state.json`
5. `sources/2026-W33/publication/v2/publication-candidate-v2.json`
6. all seven frozen Draft Results under `sources/2026-W33/drafting/v2/luna-r1/results/`
7. the corresponding frozen Draft Packages under `sources/2026-W33/drafting/v2/luna-r1/packages/` when attribution/source identity is needed
8. current reader source under `surveys/weekly/2026-W33/`
9. reviewed-main Core contracts necessary to execute `REQUEST_PUBLICATION_PREVIEW_REVISION` and later validate `DRAFT_COMPLETE`.

## Phase 1 — Canonical Human Gate revision materialization

The Owner decision is already made. Do not re-evaluate it.

Materialize Publication Preview revision 1 through the canonical operator bridge using operation:

`REQUEST_PUBLICATION_PREVIEW_REVISION`

Required semantic fields:

- `state_path`: `sources/2026-W33/production-state.json`
- `expected_revision`: `1`
- `reviewed_repository_commit_sha`: **the exact parent SHA of the request-only commit**. Because the request-only commit must be the first new commit after the externally supplied Exact Starting SHA, this value must equal that Exact Starting SHA.
- `regeneration_boundary`: `DRAFT_COMPLETE`
- `requested_changes`: faithfully summarize the Owner decision and Sol Issue #433 review; do not add a different decision or a broader rollback boundary.
- `reviewed_by`: `Owner`
- `review_reference`: `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r1.md`
- `reviewed_at`: use an offset-aware timestamp consistent with the explicit Owner decision on 2026-09-01 JST.

The request-only commit must contain exactly one newly added request JSON and no other path changes. Use the canonical operator transport and verify preflight/execute PASS.

After bridge completion, verify the canonical lifecycle is exactly `DRAFT_COMPLETE`, the Publication Preview review record is `REQUEST_CHANGES`, revision 1 is recorded, and downstream validation/publication-candidate authority has been invalidated/removed exactly as Core specifies.

If canonical rollback fails, stop. Do not edit reader source on top of an invalid state.

## Frozen semantic authority

Do not change or regenerate:

- Production Profile;
- Discovery / Screening / Evidence / Materiality / Completeness / Selection;
- Architecture / Architecture Review / Architecture approval;
- all seven Draft Packages;
- all seven Draft Results;
- Weekly Profile Synthesis Input/Result;
- shared Core, config, schemas, workflow, or `templates/survey/jgaisurvey.sty`.

The seven accepted Draft Results remain the principal substantive content authority.

For the specific `Weekly Community Movement` repair, you may inspect **only the already-selected/bound community Evidence explicitly referenced by the frozen Draft Package/Result** to convert the accepted context observation into reader-facing prose. This exception is context-only: it may not introduce a new technical fact, performance result, benchmark, product capability, interoperability claim, source family, candidate, or chronology. No fresh Web/X/Drive/raw-source research is allowed.

## Phase 2 — Rebuild the reader/publication transformation

Re-author the reader-facing W33 publication from the frozen semantic authority, preserving technical accuracy while enforcing Issue #433's three-layer separation:

1. public reader prose;
2. reader-facing source/claim limitations;
3. repository-only production provenance.

Layer 3 must not leak into the PDF.

### Principal repair surface

The main repair targets are:

- `surveys/weekly/2026-W33/sections/00-frontmatter.tex`
- `surveys/weekly/2026-W33/sections/10-frontier-models-access.tex`
- `surveys/weekly/2026-W33/sections/20-cyber-access-governance.tex`
- `surveys/weekly/2026-W33/sections/70-week-in-review.tex`
- `surveys/weekly/2026-W33/sections/99-source-notes.tex`
- `surveys/weekly/2026-W33/references.bib`
- `surveys/weekly/2026-W33/main.tex` only if needed for reader-facing structure/layout after the prose changes.

Sections 30/40/50/60 are already technically strong. Preserve their substantive content. Modify them only if a local sentence contains Issue #433-style production leakage or if small layout consistency adjustments are necessary after the publication rewrite.

### Internal vocabulary to remove from reader-facing output

Remove or naturally transform production/editorial uses of terms such as:

- `candidate`
- `HOLD`, `REJECT`, `DROP`, `HOLD_OUT`
- `Profile Completeness` or production-state `Completeness`
- `Evidence identity`, `Evidence Card`
- `Issue Synthesis`
- `materiality`
- pipeline-stage `Discovery`, `Screening`
- `must-cover`
- package placement / already-placed material
- `Core v2`, checkpoint, bridge, operator
- raw intake IDs/paths
- phrases equivalent to "記事では", "確認資料", "承認済みArchitecture", or "technical authority" when the sentence only explains production mechanics
- `dedicated event / chronology/index / context signal` as repository object taxonomy.

Do **not** mechanically ban ordinary words. For example, `source`/`資料` are valid when used naturally as `一次資料`, `公開資料`, `release notes`, or bibliographic sources. What is prohibited is describing repository source objects, adding/removing sources, internal source identities, or workflow classification.

### Reader-facing limitation language

Preserve uncertainty and claim strength, but express it directly. Appropriate formulations include, where supported:

- `公開一次資料で確認できる範囲では…`
- `提供対象・提供経路は限定されている`
- `速度値は提供元の報告であり、独立測定ではない`
- `論文著者が報告した評価であり、独立再現は確認していない`
- `測定条件が異なるため単純比較できない`
- `X上で関心が見られたが、技術的事実の裏付けには用いない`.

Do not replace one internal token with another internal token.

### Weekly Community Movement

The replacement block must answer **what was actually observed**, not merely explain the policy for community evidence.

Use only the already-bound W33 community observation. Summarize the accepted observation in natural reader language, for example at the level actually supported by the frozen material: concurrent interest in the dense release wave, model/access discussion, local/open-weight or agent/coding/runtime/workflow topics, hands-on testing/correction signals, etc., only where the accepted observation actually supports them.

Every sentence must remain clearly a statement about community discussion/attention, not proof of model performance or technical capability.

If the frozen authority supports only broad movement, keep the prose broad. Do not fill gaps by browsing or inference.

### Week in Review

Keep `w33-week-in-review` as an independent synthesis with the existing reader purpose:

- what changed;
- why the changes matter together;
- what to watch next.

Do not discuss candidate/source addition, HOLD/REJECT disposition, Profile Completeness, package placement, or the fact that prior chapters were used as synthesis inputs.

Convert the valid underlying limitations into reader-facing watchpoints instead.

### Sources & limitations / References

Turn Source Notes into concise reader-facing `Sources & limitations` material. Explain source classes only when useful to the reader: vendor/project primary release information, paper-author reported results, and context-only community observation.

Do not describe repository Evidence identity, Issue Synthesis, Selection state, or Core provenance.

References should expose normal reader-facing bibliographic identity: title, organization/authors, date, and already-known public URL when available.

The raw internal `Grok_X_SourseIntake/.../grok-x-result.md` URL must not appear in the publication. If the accepted community observation has no reader-safe public URL already present in frozen authority, omit the URL rather than inventing one. Repository provenance may remain in non-reader publication/execution metadata.

## Content depth and page plan

Do not revert to the six-page compressed failure described by Issue #433.

The current stronger technical substance in Serving, inference systems, Agent Reliability, and Multimodal must survive. The early chapters and final synthesis should be sufficiently explanatory that their must-cover substance appears as actual technical narrative rather than descriptions of what Architecture/Evidence required.

Architecture page plan remains:

- soft target: 18 pages
- hard maximum: 24 pages.

The soft target is not a padding quota. Eleven pages is not itself a defect. Natural page growth from better reader prose is acceptable. Never add filler solely to approach 18 pages.

## Phase 3 — Canonical CI and exact-byte validation candidate

After the reader rewrite:

1. commit/push W33 reader source normally and non-force;
2. use existing `.github/workflows/build-weekly-survey.yml` as the canonical build environment;
3. require build success and final TeX publication-warning gate PASS;
4. retrieve the exact CI artifact and independently verify `main.pdf.sha256` against the artifact PDF;
5. pin the exact PDF bytes to `surveys/weekly/2026-W33/main.pdf` without mutation;
6. visually inspect every page of the exact pinned PDF;
7. regenerate current Reader Manuscript Manifest, deterministic authority records, Quality Regression Bundle, Semantic/Editorial Review, and Exact-PDF Visual Review;
8. run canonical current-Core `DRAFT_COMPLETE` stage-contract validation and require PASS.

### Mandatory Issue #433 self-review

Canonical validation is necessary but not sufficient.

Before completion, perform a fail-closed semantic search/review over all reader-facing `.tex` and bibliography output for Issue #433 leakage. Explicitly record the result in the session and Semantic/Editorial Review. Add an edition-local semantic review check such as `ISSUE_433_PUBLICATION_TRANSFORMATION` if the review schema permits it.

At minimum verify that publication output contains no inappropriate pipeline/provenance use of:

- candidate;
- HOLD / REJECT / DROP / HOLD_OUT;
- Profile Completeness / production-state Completeness;
- Evidence identity / Evidence Card;
- Issue Synthesis;
- materiality;
- Discovery / Screening as pipeline stages;
- must-cover / package placement;
- Core v2 / checkpoint / bridge;
- `Grok_X_SourseIntake` raw path;
- internal production rationale in place of technical narrative.

A literal token may appear only if it is part of a legitimate external source/title and not functioning as production metadata; document any such exception explicitly.

Also manually re-read the final Week in Review, Community Movement, and Sources & limitations sections for semantic leakage even if a string scan passes.

## Allowed write surface after rollback

Edition-local writes needed for the repair may include:

- `surveys/weekly/2026-W33/**`
- `sources/2026-W33/publication/v2/**`
- canonical Human Gate review/index/state artifacts generated by `REQUEST_PUBLICATION_PREVIEW_REVISION`
- the immutable operator request and bridge-run outputs for that revision operation
- one new repair session record under `sources/2026-W33/execution/sessions/`.

Do not write shared Core/config/schema/workflow/style paths or upstream research/selection/architecture/drafting authorities.

## Stop boundary

**Stop at `DRAFT_COMPLETE`.**

Do not execute:

- `DRAFT_COMPLETE -> VALIDATED_DRAFT`
- a replacement Validation checkpoint
- a replacement Publication Candidate
- `VALIDATED_DRAFT -> RELEASE_CANDIDATE`
- Publication Preview approval
- freeze
- release
- merge.

The final Production State must be `DRAFT_COMPLETE` with draft checkpoint still passed and validation/publication-preview downstream state pending as canonically derived after the revision rollback.

Normal successful stop status:

`ISSUE_433_READER_TRANSFORMATION_REPAIR_READY_FOR_SOL_REVIEW`
