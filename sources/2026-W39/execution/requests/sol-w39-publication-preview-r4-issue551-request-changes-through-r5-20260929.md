# W39 Publication Preview r4 — Issue #551 REQUEST_CHANGES through fresh r5

Status: `EXECUTION_AUTHORITY / HUMAN_REQUEST_CHANGES_R4 / ISSUE_551_SOURCE_FIDELITY_REPAIR / BOUNDED_AT_FRESH_PUBLICATION_PREVIEW_R5`

Date: `2026-09-29 JST`

## 1. Human authority and reviewed identity

Human Owner instruction in chat: `Issue 551を参照して対応してください`.

This instruction adopts Issue #551 as the required Publication Preview r4 change set.

Canonical Human decision to record with the current reviewed Core tooling:

- Gate: `PUBLICATION_PREVIEW`
- Revision: `r4`
- Decision: `REQUEST_CHANGES`
- Regeneration boundary: `DRAFT_COMPLETE`
- Reviewed repository commit: `eb3bb84fa72af02f30d8dfe888304c5988479013`
- Reviewed r4 publication candidate SHA-256: `d399c25cfabbef368dc9e15156cae2fea56f43faf3ae1f32ab18633a0296048e`
- Reviewed r4 PDF SHA-256: `19767148dfcd6b449b32920d0250b097feab441c28fba32b31c316a951d2d5b8`
- Reviewed PDF: `12 pages / 331169 bytes`

Issue authority:

- `https://github.com/eariver/japanese-generative-ai-survey/issues/551`
- Title: `[Publication][W39] Publication Preview REQUEST_CHANGES — ART semantic correction + source-fidelity/citation repair`

The issue body is authoritative for the requested defects and acceptance criteria. Do not broaden beyond it except for source-read-back findings that make the bounded repair impossible; in that case stop and report.

## 2. Starting guards

Work only on existing branch:

`weekly/2026-W39-v2-work`

Expected starting remote HEAD before this request was added:

`5c48c8dc08092985b192f8cc2418f21d11fe34b5`

Expected starting tree before this request was added:

`8bedd759a51170edd4b72793868f801e71f19df0`

Reviewed main must remain:

`519aed90607f6e787bb3a7c00b651777835fd657`

Frozen Production Core must remain:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

At execution time, use the commit containing this request as the exact branch starting authority supplied by Sol. Before any write, verify remote branch HEAD/tree and main/Core guards exactly. On any mismatch, perform zero repository writes and stop with expected vs actual values.

No new branch, fallback branch, repair branch, review branch, reset, rebase, force push, or history rewrite.

## 3. Frozen upstream authority

Preserve without modification:

- Discovery
- Screening
- Evidence
- Materiality
- Completeness
- Selection
- Architecture
- Human Architecture r1 APPROVED authority

Do not rerun or rewrite those stages merely to repair reader wording or citation binding.

Exception: if the mandatory source read-back in §4 shows that a required Issue #551 correction cannot be supported by the already accepted Evidence authority, do **not** silently add a new source or mutate Evidence. Stop and report the exact missing authority and the minimum boundary escalation required.

## 4. Mandatory source-fidelity read-back before editing

Before editing reader prose, read back the accepted evidence/source authority actually used for each affected claim. Do not repair from Issue #551 wording alone.

### 4.1 ART / enzyme discovery

Read the accepted primary source bound to `enzymeart` and the accepted Evidence record/package.

Confirm exactly:

- whether the reverse transcriptase was already known from prior work;
- what element/system was newly identified;
- ART component structure;
- relationship among RT gene/protein, partner/accessory gene/protein, and the long repeat array;
- what was experimentally validated vs inferred;
- what remains unknown.

Required semantic invariant after repair:

- the RT itself must not be presented as the newly discovered element if the primary source says it was already known;
- system-level novelty must be explicit;
- ART components must be source-faithful;
- no new unsupported mechanism/function claim may be introduced.

If accepted primary evidence does not support Issue #551's requested interpretation, stop and report the discrepancy instead of choosing either side by assumption.

### 4.2 Cursor eval/proxy claim

Read the accepted Cursor source bound to `cursoreff`.

Preserve source strength. The reader wording must reflect that evals can be fast/useful proxies while potentially overrepresenting hard problems and not matching the real user-request distribution. Do not retain a stronger conclusion such as `当てにならず` unless the source directly supports it.

### 4.3 Claude Code graceful-stop citation binding

Inspect the accepted Evidence authority and bibliography/source records for the Sep. 25 Claude Code graceful-stop behavior.

Separate claim/source roles:

1. behavior-change existence / official announcement -> first-party ClaudeDevs / Anthropic source;
2. plan-specific conditions (e.g. Pro weekly once, Max/Team Premium every time) -> secondary source only to the extent that accepted evidence actually supports those details.

If an appropriate first-party source is already present in accepted Evidence but not bound in reader bibliography/citation, rebind the publication surface accordingly.

If the required first-party source is **not** present in accepted Evidence authority, do not add it ad hoc at publication stage. Stop before completing r5 and report:

- missing first-party source identity/URL if known;
- current accepted secondary source;
- why publication-local rebinding is insufficient;
- minimum required pipeline boundary to admit that authority.

### 4.4 Opus 5.5 source-fidelity details

Read the accepted `opus55` source and verify:

- the ~40% cost statement is a typical-workload estimate / Anthropic calculation, not a blanket list-price 40% reduction;
- fast mode wording is `up to 2.5x faster` or equivalent.

Reader wording must make both qualifications explicit wherever those claims recur.

### 4.5 DolphinBench dates

Read the accepted `dolphin` source/record and distinguish arXiv v1 Sep. 21 from v2 Sep. 22. Replace ambiguous `9月21日（改め22日）` wording with an explicit source-faithful v1/v2 statement wherever relevant.

## 5. Required reader/publication repairs

After §4 confirms support, repair all affected reader-facing occurrences, not only the specific quoted sentence.

At minimum inspect and update as necessary:

- `surveys/weekly/2026-W39/sections/00-frontmatter.tex`
- `surveys/weekly/2026-W39/sections/20-frontier-challenger.tex`
- `surveys/weekly/2026-W39/sections/30-agent-operations.tex`
- `surveys/weekly/2026-W39/sections/60-science-eval.tex`
- `surveys/weekly/2026-W39/sections/80-week-in-review.tex`
- `surveys/weekly/2026-W39/sections/99-source-notes.tex`
- `surveys/weekly/2026-W39/references.bib` only where accepted-evidence citation rebinding requires it
- every generated reader-manuscript/publication surface derived from those canonical inputs

Search the entire final reader surface for duplicated/rephrased instances of the same claims so that frontmatter, section text, synthesis, source notes, and claim-boundary boxes remain mutually consistent.

Do not hand-edit final PDF bytes.

## 6. Issue #551 acceptance requirements

All of the following must be satisfied before r5 can be presented:

1. ART novelty/component description corrected against accepted primary source.
2. Cursor proxy wording reduced to source-supported strength.
3. Claude Code behavior-change claim bound to first-party authority and plan conditions bound separately as appropriate; or execution stops under §4.3 if accepted Evidence lacks the authority.
4. Opus 5.5 ~40% statement clearly framed as Anthropic's typical-workload estimate/calculation.
5. Fast mode says `最大2.5倍` / `up to 2.5x`, not unconditional `2.5倍`.
6. DolphinBench v1/v2 date wording explicit.
7. Facts, numbers, temporal boundaries, attribution, caveats, citations, HOLD/late-only treatment preserved except where Issue #551 specifically corrects fidelity/binding.
8. No Discovery/Evidence/Selection/Architecture rewrite unless execution stops and asks for an explicit escalation.
9. Exact PDF rebuilt and fully revalidated.
10. Publication Preview r5 remains Human `PENDING`; no Freeze/Release.

## 7. Terminology regression guard

Issue #551 is not a request to redo the prior terminology repair, but r5 must not regress it.

Use the existing combined terminology authority as a read-only regression check:

- `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r3-residual-additions.md`

Do not create a new supplement unless the Issue #551 repair itself introduces or reveals a new generic defect.

## 8. Regeneration and validation

Once the source-fidelity edits are complete, use the current frozen Core pipeline from the legal `DRAFT_COMPLETE` regeneration boundary to regenerate fresh r5 artifacts, including as applicable:

- reader manuscript
- reader-surface input/gate
- source/citation binding checks
- deterministic checks
- identifier preservation
- semantic-editorial review
- visual review
- quality regression bundle
- TeX/Bib
- CI PDF
- PDF preflight
- publication candidate
- stage validation
- agent-state validation

Do not reuse r4 PASS reports as r5 PASS reports.

## 9. PDF exact-byte authority

For the r5 candidate independently calculate from actual files:

`SHA256(repository main.pdf)`
`== repository main.pdf.sha256`
`== SHA256(Actions artifact main.pdf)`
`== artifact main.pdf.sha256`

Also confirm identical byte count and page count across repository/candidate/artifact surfaces.

Any mismatch is blocking.

## 10. Fresh r5 Publication Preview stop point

Only after all Issue #551 acceptance criteria and validations pass, create fresh:

`PUBLICATION_PREVIEW_R5 / PENDING`

Expected terminal state:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R5_PENDING`

No Human r5 decision may be generated or inferred.

Do not Freeze, Release, merge to main, modify Production Line, or modify Shared Core.

## 11. Issue #551 traceability

Update Issue #551 with an execution comment that identifies:

- this request path;
- exact r4 reviewed authority;
- source-read-back result for each of the five correction groups;
- whether accepted Evidence was sufficient for Claude Code first-party binding;
- exact repair commit(s);
- final r5 reviewed authority and PDF SHA/bytes/pages if successful;
- any blocker/boundary escalation if not successful.

Do not close Issue #551 until fresh Sol/Human review confirms the acceptance criteria.

## 12. Required final report

Report at completion or stop:

- starting guard results (branch HEAD/tree, main, Core);
- canonical Human r4 decision record path/SHA;
- source-read-back results for ART, Cursor, Claude Code, Opus, DolphinBench;
- exact files changed;
- whether any Evidence escalation was required;
- citation keys before/after for Claude Code;
- validation/checkpoint results;
- r5 candidate SHA-256;
- r5 PDF SHA-256 / byte count / page count;
- four-surface byte-identity result;
- fresh r5 review shell/dossier paths;
- final remote HEAD/tree;
- confirmation `Freeze/Release not executed`.
