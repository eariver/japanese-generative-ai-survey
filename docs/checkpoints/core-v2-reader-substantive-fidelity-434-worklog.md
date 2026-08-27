# Core v2 reader substantive fidelity maintenance — Issue #434

Date: 2026-08-27
Branch: `fix/core-v2-reader-substantive-fidelity-434`
Base reviewed `main`: `079dac9605e4cf55a239de6f03e37a93f756a918`
Maintenance PR: `#473` — `Core v2: enforce reader substantive Architecture fidelity`

## Trigger

SP001 Publication Preview candidate `aa5b0665cf96546c88601883eac82819f1e428f1` was Human-reviewed under Issue #400 and remains revision-required. The cold-start candidate improved Publication Boundary leakage and restored mixed layout, but compressed the approved six-package `LONGFORM_SPECIAL` Architecture into a seven-page candidate while `LONGFORM_TECHNICAL_DEPTH` still passed. Issue #434 records this as a shared Architecture -> Publication substantive-fidelity defect.

## Maintenance scope

This branch changes shared Core only. It does not edit SP001 generated publication bytes.

## Responsibility split

The implementation follows the Reader Manifest authority: deterministic helpers protect exact identity and traceability; substantive/editorial adequacy remains ChatGPT-owned semantic review.

Accordingly, this repair does **not** make page targets into quotas and does not infer quality from fixed character counts, citation counts, source diversity, package-to-section ratios, or one-block-per-requirement rules.

### Deterministic Reader Manuscript traceability

`scripts/survey_reader_fidelity_v2.py` requires LONGFORM coverage claims to resolve to real, non-empty numbered TeX content blocks using exact locations such as:

- `Section N — title`
- `Subsection N.M — title`

The same applies to `FINAL_SYNTHESIS`. Abstract locations such as `main.tex :: Sections 1–6` are not sufficient authority for a new LONGFORM Reader Manifest.

The deterministic layer only proves that the author-accountability map points at exact reader-facing bytes already bound by the Reader Manifest. It does not declare those bytes editorially sufficient.

The parser is deliberately bounded to the repository's numbered `section` / `subsection` LONGFORM authoring surface. During pre-freeze review it was hardened so that:

- `section*` / `subsection*` do not consume numbered reader-location identities;
- starred headings still terminate a preceding numbered block, so unnumbered notes/references cannot be attributed to it;
- headings inside ordinary TeX comments are ignored while source offsets are preserved;
- escaped `\%` remains ordinary reader-visible content rather than starting a comment;
- heading text and structural `\label{...}` metadata alone cannot make a block appear to contain reader prose.

`schemas/reader-manuscript-v2.schema.json` description authority is synchronized with this responsibility: LONGFORM deterministic validation proves exact extant non-empty numbered block traceability, while substantive fulfillment remains semantic/editorial judgment.

### Semantic/editorial substantive fidelity

For LONGFORM `SEMANTIC_EDITORIAL` review:

- `ARCHITECTURE_CONTENT_FIDELITY` must explicitly bind every approved `package:<id>` and every exact Reader Manifest coverage block;
- `LONGFORM_TECHNICAL_DEPTH` must explicitly bind every approved package and every exact coverage block, preventing generic topic-presence review from standing in for package/content review;
- `FINAL_SYNTHESIS_QUALITY` must bind the final Architecture package, the exact `FINAL_SYNTHESIS` reader location, and `reader-role:final-synthesis`;
- the final package is the unique package with maximum canonical `drafting_order`, not the last JSON array element;
- when actual pages are below the soft Architecture `target_pages`, `LONGFORM_TECHNICAL_DEPTH` must additionally record the exact `page-plan:<actual>/<target>` observation and the explicit semantic disposition `density-review:below-target-substantive`.

This makes a below-target result reviewable rather than automatically invalid: ChatGPT may still judge a compact result substantive, but must do so consciously and against exact package/block evidence.

### Exact PDF page authority

Publication Review does not trust mutually consistent caller metadata for the actual page count. `scripts/survey_reader_publication_v2.py` derives page count from the exact repository-resident PDF bytes with pinned `pypdf==6.16.2`, rejects encrypted/unreadable/zero-page PDFs, rejects asserted or recorded page-count mismatch, and passes only the derived count into the LONGFORM density review.

The parser choice is covered by a static two-page LuaLaTeX fixture whose Page dictionaries are stored in an `/ObjStm`; the fixture intentionally has zero raw `/Type /Page` tokens. This proves the exact-page authority against the production PDF encoding that defeated the earlier raw-byte scanner.

### Integration and regression coverage

- `scripts/survey_reader_publication_v2.py` validates exact LONGFORM traceability when Reader Manuscript authority is built/revalidated, then validates package/block-bound semantic review when publication review records are built/revalidated.
- `tests/test_survey_reader_fidelity_v2.py` covers exact traceability, abstract/nonexistent/empty location rejection, non-overfit layout freedom, package/block semantic evidence, canonical final-synthesis ordering, JSON-number page targets, below-target density disposition, and WEEKLY non-applicability.
- `tests/test_survey_reader_fidelity_parser_v2.py` covers starred heading numbering/boundaries, commented headings, escaped percent, heading-only blocks, and label-only blocks.
- `tests/test_survey_pdf_page_inspection_v2.py` carries the real LuaLaTeX object-stream PDF fixture and proves exact page inspection works while malformed PDF fails closed.
- `tests/test_survey_publication_v2.py` and `tests/test_survey_human_gate_v2.py` exercise integrated Publication Candidate and Human Gate round-trip paths using valid PDFs, exact reader blocks, and package-bound semantic-review evidence.

## Human review of the first frozen candidate

The first frozen maintenance candidate was:

`b42c1f38e16a812bdd0925270de484a139d6d7cf`

It had exact-head green CI and a fresh 7/7 audit recorded outside the tree. PR review `5036108178` then identified three accepted-input counterexamples. That review **invalidated the freeze and superseded the old 7/7 result**; it must not be reused as approval evidence.

The three findings and repairs are:

1. **JSON-number `target_pages`** — canonical Architecture permits numeric values such as `18.0`, while the first implementation only applied the below-target review rule to Python `int`. The repaired fidelity validator accepts finite positive `int`/`float` values (excluding booleans), normalizes integral floats such as `18.0` to the canonical review marker `18`, and regression-tests `target_pages: 18.0` with a seven-page result.
2. **Exact PDF page-count authority** — the first implementation trusted caller-supplied `page_count`, so mutually consistent metadata could claim an 18-page result for a seven-page exact PDF. Publication review now derives page count from the exact repository PDF bytes, rejects asserted/recorded mismatch at both build and revalidation time, and passes only the derived count into longform density review.
3. **Canonical final-package ordering** — the first implementation used `packages[-1]`, even though Architecture finality is defined by maximum `drafting_order`. The repaired validator derives the unique final package from maximum canonical `drafting_order`, independent of JSON array position, and regression-tests reversed array order.

These are narrow contract repairs. They do not introduce a page quota, a new Human Gate, or an editorial-quality heuristic.

## Fresh-audit finding after the review repair

Post-review head `59e9e8e13565acca309b476ff97fb117ec1eb783` reached green exact-head CI and passed the pre-freeze scope check, but the fresh seven-point audit deliberately tested the new PDF authority against the repository's actual Special build method. `build-special-pdf.yml` compiles with LuaLaTeX, whose valid PDFs may place `/Page` dictionaries inside compressed object streams. The interim raw-byte `/Type /Page` scanner therefore reported zero pages on a real two-page LuaLaTeX output even though its synthetic Page-tree fixtures passed.

That is a generalization/control-proportionality defect. Consequently `59e9e8e1...` is **not** a valid frozen 7/7 candidate and no audit PASS may be recorded for it.

The repair replaces ad-hoc raw PDF parsing with pinned `pypdf`, installed through the existing Core requirements path. The default-branch operator workflow already installs `config/survey-production-v2-requirements.txt` after protected-authority preflight, so the dependency follows the same trusted runtime path as the rest of Core after integration.

## Pre-freeze parser/authority hardening

After the PDF repair, static full-PR review deliberately tested the exact-block parser against supported TeX authoring shapes rather than stopping at green fixtures. It found and repaired four generic traceability edge classes before freeze:

1. starred subsections could affect numbering or leak unnumbered prose into a numbered block;
2. a starred section such as References could be included in the preceding numbered section body;
3. commented-out headings could be mistaken for live reader locations;
4. heading labels or `\label{...}` metadata could make an otherwise empty block appear non-empty.

Negative regressions were added for all four classes, including escaped-percent handling. These repairs remain deterministic traceability only; they do not score prose depth or quality.

The Reader Manifest schema descriptions were also synchronized so repository authority no longer describes LONGFORM deterministic validation as manifest identity-only while the implementation enforces exact reader-block traceability.

## SP001 expected effect

The current SP001 Reader Manifest at `aa5b0665...` already uses exact Section-level coverage locations, so deterministic traceability alone does not reject it. That is intentional: exact Section bytes exist.

Its current semantic review does **not** satisfy the repaired contract: the Architecture/depth checks use generic `reader-manuscript-v2.json :: architecture_coverage` / `main.tex :: Sections ...` evidence rather than explicit package-plus-exact-block review, and the 7-page result is below the approved soft 18-page target without an exact `page-plan:7/18` density disposition. The exact PDF-derived page-count rule additionally prevents that below-target condition from being bypassed through review metadata. Therefore the old candidate cannot be revalidated as a new acceptable LONGFORM candidate without regeneration/re-review.

A regenerated SP001 candidate must supply an exact accountability map and a fresh semantic review that actually assesses each package/block, final synthesis role, and any below-target density before Publication Candidate authority can pass.

## Diagnostic history

- Initial diagnostic Core CI on old head `1ac49d00...` exposed nine failures sharing one cause: the Human Gate fixture still generated LONGFORM reader source with no numbered sections / abstract locations. The production gate implementation itself compiled, and the new direct fidelity tests passed on that head.
- The Human Gate and Publication fixtures were migrated to exact reader locations, valid PDFs, and semantic package/block evidence.
- Frozen head `b42c1f38...` reached exact-head green CI and 7/7 audit, but PR review `5036108178` found the three accepted-input gaps above. Its audit is superseded.
- Post-review repairs added direct regressions for float page targets, exact-PDF page-count mismatch, and array-order-vs-drafting-order final synthesis.
- Head `59e9e8e1...` reached green CI but fresh audit found its raw PDF page scanner incompatible with real LuaLaTeX object-stream output. That candidate is invalidated before any reusable 7/7 result.
- PDF inspection was moved to pinned `pypdf` with a real LuaLaTeX object-stream regression fixture.
- Diagnostic head `f15f9d20391c8f2e1cd0733c6cea2ca8ac298b1c` completed both exact-head workflows successfully: `Survey Production Core v2 CI` #1209 (`33084238758`) and `Pipeline contract tests` #3466 (`33084239916`). Those runs prove the PDF/Human-Gate fixture repair but are not final-audit authority because later parser/schema hardening changed the tree.
- Pre-worklog-sync head `f8a5969545f5a0728cfae92d6d0f8aa44c58ef21` completed `Pipeline contract tests` #3478 (`33086055027`) successfully with the starred/comment/label parser regressions. Its Core run was queued when the final worklog synchronization began, so the final docs-only candidate must obtain fresh exact-head evidence from both workflows.
- Several intermediate heads are diagnostic only; none is final-audit authority.
- No Core merge has been performed.

## Pre-freeze scope observations

Before final worklog synchronization:

- reviewed `main` remained `079dac9605e4cf55a239de6f03e37a93f756a918`;
- the maintenance branch was ahead of that base and not behind it;
- changes were limited to Core requirements, Reader Manifest schema description authority, reader fidelity/publication code, regressions, and this worklog;
- no `sources/`, `surveys/`, generated SP001 bytes, or workflow files were modified;
- PR #473 remained open, Draft, unmerged, and mergeable;
- the only prior blocking PR review was the three-item review on `b42c1f38...`, and those three items now have direct regressions;
- operator dependency installation remains behind reviewed-main/protected-Core trust checks and uses the same pinned Core requirements file.

These observations are diagnostic. They must be repeated against the final post-worklog head before that SHA is frozen.

## Remaining steps

1. Treat the commit containing this synchronized worklog as the new final-candidate **candidate**, not yet as a frozen audit authority.
2. Reconfirm current `main`, PR head/state, changed-file scope, stale review surface, and absence of edition-local artifact contamination on that exact head.
3. Obtain exact-head SUCCESS from both `Survey Production Core v2 CI` and `Pipeline contract tests` after this final tree mutation; any further mutation invalidates those results.
4. Freeze that unchanged SHA and execute all seven points in `docs/survey-production-core-v2-final-audit-rule.md` from Point 1. Neither `b42c1f38...`, `59e9e8e1...`, `f15f9d20...`, nor `f8a59695...` is reusable final-audit authority.
5. Record any fresh 7/7 result outside the audited tree and present the candidate for Human Core-maintenance review; do not merge without explicit Human approval.
6. After approved Core repair is merged to `main`, resume SP001 through the canonical revision path, regenerate Publication Candidate, perform fresh exact-byte semantic/visual review, and return to Publication Preview Human Gate.
7. Do not Freeze/Release SP001 before explicit Human Publication Preview approval.
