# J-GAS W42 — Muse r30 integrated validation-to-Human-Publication-Preview execution

Date: 2026-10-20 JST
Status: `SOL_EXECUTION_AUTHORITY / HUMAN_R30_INTEGRATED / CONDITIONAL_CANONICAL_ADVANCE / STOP_AT_HUMAN_PUBLICATION_PREVIEW`
Repository: `eariver/japanese-generative-ai-survey`
**Only existing branch:** `weekly/2026-W42-v2-work`
**Sol-authorized parent HEAD / Tree before dispatch:** `060d15af369e4a871837716c999f5bb8cd5d481a` / `ec221c628306a971e5f130b69a5d9fa7f5ba82bf`
**Exact Worker starting HEAD / Tree:** supplied by Sol in final activation message, MUST be the commit containing this instruction and Human authorization. Read Git refs from remote, never guess this dispatch commit.

## 0. Mission and immutable baseline

In ONE Muse session, close narrow r29 review limitations (without extensive research or redoing independent 21-page/110-cell audit), construct truthfully attributable Core v2 formal review/surface/quality authorities and validate them. If all evidence genuinely PASS, use **existing first-party operator bridge** to advance `DRAFT_COMPLETE → VALIDATED_DRAFT`, construct and validate Publication Candidate, then advance `VALIDATED_DRAFT → RELEASE_CANDIDATE`. STOP before any Human Publication Preview decision. No separate Human signoffs for routine substeps inside this precisely approved scope.

At session start, BEFORE ANY WRITE: read-only verify remote exact Worker HEAD AND root Tree, direct one-chain ancestry to `060d15af369e4a871837716c999f5bb8cd5d481a`, remote reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / Tree `801de813319f08777ab1581a5e8875fc1ac5df19`; Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`; State-pinned implementation HEAD `a4f25630270f029656f35771592f9ebda02fa5cc` / Tree `e68560d1542806b61b4c55f03063839fd2ec30c0`; r29 audited PDF commit `9207767cff484b2766bd00b28da120bb58b002d8` / Tree `10a77f0ea934993ca2e2b70c718cfaea8d946f03`.

Protected baseline blobs at dispatch: `sources/2026-W42/production-state.json` SHA1 `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`; approved Architecture r1 SHA1 `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`; Human Gate review-index SHA1 `6682579c135fc72599bfdbb883621da726e09f83`; r18 Reader master SHA1 `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`. Read actual stage State: `DRAFT_COMPLETE`, `publication_preview=pending`, `validation=pending`; if these already changed, do not replay the instruction.

Canonical r29 file authorities:
- TeX `surveys/weekly/2026-W42/main.tex` SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3`, 96790 bytes.
- PDF `surveys/weekly/2026-W42/main.pdf` SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9`, 505102 bytes / 21 pages.
- Reader `sources/2026-W42/publication/v2/reader-manuscript-v2.json` SHA256 `47634ae3ac347dd9529e796e01ed3661defa89e5f31b164dfe9752155b23c76f`; manifest content digest `78d9928ded5ec663c7f25a028135fa05cf5411a2ecc0a0c1bb407eb9f02708e0`.
- Independent review **original verdict PASS_WITH_LIMITATIONS**: archived `sources/2026-W42/execution/reviews/independent-w42-r29-semantic-visual-audit-archived-20261020.md`, original byte SHA256 `3a94cecd0f2a5c453cf9e9e4a98d33e560fc92026f1158425e0fb4fa54cab7cd`; Sol disposition `sources/2026-W42/execution/reviews/sol-w42-r29-independent-semantic-visual-disposition-20261020.md`.
- r29 deterministic evidence and all 21 PNGs: `sources/2026-W42/execution/publication-build-r29/`.

Any mismatch, output collision, workspace dirt, unresolvable authority, unapproved source change or unsafe branch state: `R30_PREFLIGHT_BLOCKED / ZERO_WRITES`. No new/fallback/review/repair branch, force push, rebase, reset (including local `reset --hard`), destructive checkout, speculative overwriting or modifying other users' work. If using a clean isolated worktree/checkout, do not create a branch or affect existing dirty trees.

## 1. Authored evidence closure, not another broad independent audit

Read in order: r30 Human authorization, this contract, Sol r29 disposition, verbatim independent r29 report (archived), r29 manifest and session, Human r27 Route A, r28 Bridge routing disposition, actual Core v2 source/schema (State-pinned or identical reviewed main), approved r1 Architecture and Selection. Avoid loading all 21 PNGs or entire Reader into the conversational context unless a specific discrepancy needs inspection.

Persist bounded, verifiable evidence under new `sources/2026-W42/execution/validation-to-preview-r30/`:
- **L02**: directly verify three high-risk authorities: **B16 Beam License actual full license**, **B54 independent Vals methodology/ranking**, **B57 ASPIRE Oct 16 OSS release-date/provenance**. Compare source versions/dates, cited assertions, limitations; record source URL, capture/access time, relevant verbatim short fact/excerpt, claim/location and confidence. Where inaccessible, state `UNVERIFIED`, never substitute a secondary paraphrase as direct source. Do not reopen other 71 URLs/90 keys or modify published words without a concrete discrepancy/owner direction.
- **L03**: independently render the *existing immutable r29 PDF* with recorded renderer/version/settings (e.g., PyMuPDF or Poppler). Verify 21-page count, page dimensions, and full page mapping against committed `p-01..p-21.png`. Where same pipeline and resolution allow, compare image hashes/pixels. If renderer differs, objectively quantify or describe tolerable antialias differences; independently inspect the visually material mismatches (not every page again). Never mislabel byte differences from different renderers as content regression. Persist commands, exact PDF hash, comparison metrics, evidence and outcome. PDF/PNG must not be altered just to force equality.
- **L04**: create exact 28 selected IDs → P1..P7 → actual Reader/TeX sections crosswalk; spot-check materiality, citations and presence. Any unmapped ID is a blocker, not an invitation to invent mapping.
- **L01** previously accepted whitespace: retain as disclosed Human Preview limitation, do not re-typeset. **L05** optional Japanese tone: no rewrite.

Do not declare evidence closure solely because report is `PASS_WITH_LIMITATIONS`. Where L02 observations cannot be confirmed, assess whether truly required check can be supported without inventing independent confirmation; when material for a required PASS, stop with explicit unresolved issue/evidence. Genuine material discrepancy → `R30_EDITORIAL_OR_AUTHORITY_BLOCKED`, preserve r29 bytes and report before Stage/Gate.

## 2. Formal Core v2 validation authorities — no forged independent PASS

Use the Frozen State-pinned official builders/validators and actual schema, not handcrafted status fields. At least:
- `survey_reader_publication_v2.validate_manuscript_manifest`; verify source/Reader/r1/profile exact binding;
- `survey_quality_v2.build_bundle/validate_bundle` with every applicable **DETERMINISTIC** quality check from actual frozen config, genuine result paths and executors; canonical target `sources/2026-W42/publication/v2/quality-regression-bundle-v2.json`;
- `survey_reader_publication_v2.build_review_record/validate_review_record`: canonical `publication/v2/semantic-editorial-review-v2.json` and `publication/v2/visual-review-v2.json`, bound to exact PDF/TeX/Reader bytes; checks set equals real Core expected family. Core `publication-review-record-v2.schema.json` requires `status=PASSED`, **each check=PASS**, evidence locations and truthful `reviewed_by`. Relevant extra semantic IDs: `PUBLICATION_BOUNDARY`, `ARCHITECTURE_CONTENT_FIDELITY`, `FINAL_SYNTHESIS_QUALITY`, `WEEKLY_COMMUNITY_MOVEMENT`; visual: `EXACT_PDF_VISUAL_REVIEW`. Also include all additional config-driven checks and any required `survey_reader_fidelity_v2.validate_review_depth` block-level evidence. Preserve original `PASS_WITH_LIMITATIONS` report and all L01-L05 in separate provenance/disclosure, never change that historical conclusion to unconditional independent PASS.
- Reader-Surface Gate requires a **different independent semantic-review authority** under `schemas/reader-surface-semantic-review-v2.schema.json` with substantive `READER_PIPELINE_INDEPENDENCE` PASS tied to exact TeX PRIMARY_SOURCE SHA. Its validator rejects fallback to ordinary publication review and synthetic PASS. Produce authentic reviewer-attributed, persisted, byte-bound semantic review and only then call `survey_reader_publication_v2.build_reader_surface_gate` / `survey_reader_surface_gate_v2.validate_reader_surface_gate`. Canonical Gate `publication/v2/reader-surface-gate-v2.json`; independently review any structured surface if used. Document true separate reviewer identity, reviewed bytes, evidence and limitations.

**Separation rule:** Muse is a BUILD/EXECUTION WORKER, not the independent Sol. Independent r29 report may be incorporated as provenance only for factual checks it **actually performed**. Additional L02-L04 evidence performed by Muse is worker evidence, not an independent human/agent verdict. Do not invent an independent reviewer, backdate a review, attribute Muse-authored conclusions to Sol, or create formal PASSED records simply because required schema says PASSED. If a genuinely separate reviewer/evaluation method is accessible within this Muse execution, use it and retain its raw attributable report and exact checks before deriving official records. If it is NOT available or a required semantic check is not supported, stop `R30_INDEPENDENT_REVIEW_AUTHORITY_PENDING / NO_STAGE` with an exact list of missing checks; **do not make up any review to maintain one-run appearance**. No general second full-PDF audit unless evidence specifically requires it.

Core's `DRAFT_COMPLETE` validator requires exactly these **seven names** (six listed in frozen `stage_plan` plus mandatory seventh):
`reader-manuscript`, `validated-source`, `publication-pdf`, `quality-regression-bundle`, `semantic-review`, `visual-review`, `reader-surface-gate`.
Place genuine records at canonical edition-local paths. Dry-run actual `survey_stage_validation_v2.validate_stage` in safe scratch/capture location and fix ordinary deterministic packaging failures inside authorized bounds. Do not modify Core/check definitions, alias handler names, lower thresholds, or bypass missing seventh.

## 3. Execute BOTH first-party Stage transitions, conditional on all requirements

**Only after seven authorities genuinely validate**, build immutable repository-local operator execution request conforming to `schemas/operator-execution-request-v2.schema.json` with exact source root, work branch, reviewed main, current State and byte-bound artifacts. Use existing trusted-reviewed `.github/workflows/survey-production-v2-operator-bridge.yml` → `scripts/survey_core_execution_bridge_v2.py` `ADVANCE_STAGE`; DO NOT call nonexistent default Orchestrator registry `stage:reader-publication-validation`/ `validate:reader-publication` directly, or create aliases/shims.

Transition 1: `DRAFT_COMPLETE → VALIDATED_DRAFT`, via canonical Stage Validator and actual Stage Checkpoint (Core produces it), then check State/checkpoint read-back. If Bridge workflow's trusted `main` dispatch constraints or recorded state prevent valid execution, **stop with actual error**, no direct State edits or alternative route.

Build and independently validate candidate through frozen `survey_publication_v2.build_candidate/validate_candidate`:
`sources/2026-W42/publication/v2/publication-candidate-v2.json` with `READY_FOR_PUBLICATION_PREVIEW`, exact 21-page PDF and reviewed source/Reader/quality/semantic/visual refs. Do not modify PDF or original r29 material during candidate production. Complete required CORE stage checkpoint/contract for this next transition, where applicable.

Transition 2: `VALIDATED_DRAFT → RELEASE_CANDIDATE` via SAME first-party Bridge `ADVANCE_STAGE`, strict expected-from-state and normal non-force branch refs, read back canonical State `RELEASE_CANDIDATE`, Human Preview gate `pending` and candidate/coupled-review hashes. If Core sets `terminal_reason=HUMAN_GATE_REACHED`, preserve it as a legitimate stop, NOT as Human Gate approval. If State remains `VALIDATED_DRAFT`, report blocked, never label preview ready.

Important: ensure workflow semantics, branch SHA, Git-saved artifacts and approved content identity at EACH step. Commit and non-force push complete prerequisite artifacts before dispatching requests that must read remote refs. Confirm no race just before each push and dispatch. Multiple normal FF commits are allowed **on the same existing branch**; never force, rebase, reset, or use fallback branches.

## 4. Allowed writes and prohibited outputs

Allowed (new/append only unless canonical first-party Bridge safely and necessarily updates its own state/checkpoint paths):
- New `sources/2026-W42/execution/validation-to-preview-r30/` for evidence source excerpts (copyright-limited), methods, actual separate reviewer provenance, render metrics, Selection crosswalk, results, run IDs, operator requests and receipts, no overclaim;
- New W42 canonical `publication/v2/` QUALITY bundle, formal Semantic/Visual review, Reader-Surface *semantic-review authority/input as actually needed*, Reader-Surface Gate, Publication Candidate (no overwrite);
- First-party Bridge-generated legitimate W42 Stage validation checkpoint(s), State, transport receipts only for the two authorized transitions, and required canonical execution records;
- New `sources/2026-W42/execution/sessions/muse-w42-r30-20261020.md`, append-only W42 `execution/index.md`.

Forbidden: edit any existing r29 canonical TeX/PDF/Reader or other prior rXX artifacts; protected r1 Architecture, Selection, r18 draft, r26 diagnostic, all historical review/approvals; all shared Core/config/scripts/schemas/workflows or main; retroactively edit Human approvals; create unearned human Gate records; publication preview `APPROVED`, preview export approval, Freeze, Release, merge to main, new branches, reset/rebase/force. The original r29 external audit may only be archived unchanged, never rewritten.

## 5. Terminal conditions and must-report evidence

**SUCCESS only if all actual validators and Bridge operations complete:**
`SOL_W42_R30_PUBLICATION_PREVIEW_READY / RELEASE_CANDIDATE / HUMAN_PUBLICATION_PREVIEW_PENDING / PDF_BYTES_IMMUTABLE / NO_FREEZE_NO_RELEASE`.

A success report MUST show:
- Worker exact initial/final remote HEAD/Tree; ancestry, list of changed paths vs dispatch, non-force read-back confirmation;
- reviewed r29 immutable TeX/PDF/Reader hashes and exact 21pp PDF URL at final fixed commit;
- L02/L03/L04 concise concrete outcomes + L01/L05 disclosed;
- independent r29 report unchanged `PASS_WITH_LIMITATIONS` and links to supplemental attributable independent records; no conflation of provenance;
- seven canonical current authorities, checksum/path, actual validator results and any residual limitations;
- canonical Bridge workflow/run request/receipt and actual Stage Checkpoint(s), final State `RELEASE_CANDIDATE`; Publication Candidate path/hash;
- **explicit statement no Human Preview approval/Freeze/Release has happened**;
- Human Owner-facing link for publication PDF and any visually material limitations to inspect before approval.

**STOP if any authority is missing, evidence insufficient, source mismatch, guard fails, independent semantic reviewer unavailable, validator fails or Bridge cannot legitimately execute.** Use `R30_BLOCKED / LAST_GOOD_STAGE_RECORDED / NO_FABRICATED_PASS` and provide exact blocker plus earliest safely resumable commit; do not falsely claim success or trigger an additional Human decision for deterministic, noneditorial fixes within this approved scope.

This single integrated r30 Muse contract replaces repetitive r30/r31/r32 micro-approval dispatches; authority terminates exactly at the real Human Publication Preview boundary.
