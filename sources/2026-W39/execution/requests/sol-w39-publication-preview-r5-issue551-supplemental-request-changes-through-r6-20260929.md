# W39 Publication Preview r5 — Issue #551 supplemental REQUEST_CHANGES through fresh r6

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R5_REQUEST_CHANGES / DRAFT_COMPLETE / ISSUE_551_SUPPLEMENTAL / BOUNDED_TO_R6_PENDING`

Date: `2026-09-29 JST`

## 1. Mission

Continue `eariver/japanese-generative-ai-survey` W39 publication work on the existing branch only.

This execution implements the Human Owner's explicit instruction to address the additional findings appended to GitHub Issue #551 after fresh r5 review.

The r5 candidate is otherwise accepted as the factual/layout baseline. This run is limited to the two residual reader-facing source-note/provenance inconsistencies identified in Issue #551 and must end at a fresh Human Publication Preview r6 with decision `PENDING`.

Do not broaden the work.

## 2. Exact starting guard

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W39-v2-work`

Expected remote branch HEAD before this request commit: `f9a1a35a468ee3c9ce9dec92a9940a6a4d215552`

Expected remote branch tree before this request commit: `3fafea0f26f8da292bfca9e64217f94245f52b19`

Reviewed main SHA: `519aed90607f6e787bb3a7c00b651777835fd657`

Frozen Production Core SHA: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

At execution time, the worker MUST use the exact HEAD/tree supplied by Sol in the handoff prompt after this request file is committed. Before any write, verify read-only:

- remote `weekly/2026-W39-v2-work` HEAD == supplied Exact Starting SHA;
- remote work tree == supplied Expected Starting Tree;
- remote `main` HEAD == `519aed90607f6e787bb3a7c00b651777835fd657`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`.

If any guard mismatches, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, force push, history rewrite, or cherry-pick.

## 3. Human gate authority

Human Publication Preview r5 decision is explicitly:

`REQUEST_CHANGES`

Allowed regeneration boundary:

`DRAFT_COMPLETE`

Reviewed r5 authority:

- reviewed repository commit: `342adad3400bd6dee07fb920441f8e259f18eb15`
- r5 publication candidate SHA-256: `18b9ab48868136eb6e5c47320a03a6cbc46769928d2fc3810f773b3ffe8926e1`
- r5 PDF SHA-256: `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`
- r5 PDF bytes: `335104`
- r5 PDF pages: `12`

Use current reviewed Core canonical Human Gate tooling to record this r5 `REQUEST_CHANGES @ DRAFT_COMPLETE` against the exact reviewed authority above.

Do not infer approval. Do not modify Architecture approval.

## 4. Required Issue #551 read-back

Before editing, read the complete Issue #551 body and all comments, including at minimum:

- original Issue #551 requirements;
- r5 execution report;
- Sol fresh-r5 residual citation-boundary finding;
- supplemental independent audit comment identifying the Claude Code date inconsistency.

Treat the latest Issue #551 thread as the requested repair basis.

The following r5 repairs are already PASS and MUST NOT be regressed:

- ART system-level novelty / known RT correction;
- Cursor proxy claim-strength correction;
- Opus 5.5 typical-workload cost framing;
- Opus 5.5 `最大2.5倍` fast-mode wording;
- DolphinBench v1 Sep 21 / v2 Sep 22 wording;
- Claude Code behavior claim cited to official `@ClaudeDevs` post, with plan-tier conditions separately attributed to the post-window secondary source;
- PDF layout and existing Issue #501 terminology repairs.

## 5. Residual blocker A — official-X provenance boundary contradiction

Current r5 reader-facing state is internally inconsistent:

- `surveys/weekly/2026-W39/sections/20-frontier-challenger.tex` explicitly uses `w39x-c2-claudedevs` as first-party evidence for the Sep. 25 Claude Code graceful-stop behavior change;
- `surveys/weekly/2026-W39/sections/99-source-notes.tex` categorically says the 26-post public ledger is only background and does not establish publication facts/specifications;
- `surveys/weekly/2026-W39/community-observation-ledger.md` likewise categorically frames all 26 posts as context-only.

Repair the reader-visible provenance rule without weakening the general community-observation boundary.

Required semantic rule:

- independent/community public posts remain context/background only and MUST NOT establish specification, performance, price, license, availability, safety, architecture, or release facts;
- an OFFICIAL first-party post MAY serve as primary announcement evidence **only when it is separately and explicitly cited/bound in the article for the exact announcement fact it supports**;
- being present in the public ledger alone does not elevate any row to technical evidence;
- the exception is source-role/binding-specific, not a blanket permission for all official posts or all claims within them.

Update all reader-facing/public-facing statements that conflict with this rule. At minimum inspect and, if necessary, repair:

- `surveys/weekly/2026-W39/sections/99-source-notes.tex`
- `surveys/weekly/2026-W39/community-observation-ledger.md`
- `surveys/weekly/2026-W39/sections/20-frontier-challenger.tex`
- `surveys/weekly/2026-W39/references.bib`

Do not alter raw row counts, URLs, Snowflake timestamps, temporal classes, account roles, or accepted Evidence bytes.

## 6. Residual blocker B — Claude Code date inconsistency

Current r5 has a second reader-facing inconsistency:

- `99-source-notes.tex` `Primary sources consulted` says `9月23日のClaude Codeの動作変更`;
- the repaired body says the Claude Code behavior change occurred on Sep. 25;
- `w39x-c2-claudedevs` bibliography entry and accepted public ledger bind the official announcement to Sep. 25 19:04 UTC.

Correct the source-notes date to Sep. 25 and ensure all reader-facing references to this Claude Code behavior-change event use a mutually consistent date.

Search final reader-facing sources for at least:

- `Claude Code`
- `graceful stop`
- `9月23日`
- `9月25日`
- `w39x-c2-claudedevs`
- `claudecodegraceful`

Do not change the plan-tier secondary-source temporal caveat: the plan-specific detail remains post-window secondary material as already documented.

## 7. Source/evidence boundary

This is a publication-local repair. Do NOT mutate:

- Discovery;
- Screening;
- accepted Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Architecture approval;
- Shared Core;
- `main`;
- `production/survey-core-v2`.

Accepted Evidence already records the official `@ClaudeDevs` ordinary-window row as corroborating the graceful-stop update. No evidence escalation is authorized or needed for the requested fixes.

If execution discovers a new material factual contradiction that cannot be corrected within the existing accepted authority, STOP and report it instead of broadening the boundary.

## 8. Regression requirements

Preserve all successful Issue #551 r4→r5 corrections and all prior Issue #501 terminology corrections.

Run the existing terminology corpus as a read-only regression guard; do not create broad lexical churn.

No facts, numbers, dates, claim strength, attribution, citations, selected/HOLD disposition, or temporal inclusion rules may change except the two explicitly authorized source-note/provenance corrections above and mechanically required regenerated hashes/metadata.

## 9. Regeneration

After recording Human r5 `REQUEST_CHANGES @ DRAFT_COMPLETE` and applying the bounded repairs, regenerate from the current Core-defined `DRAFT_COMPLETE` boundary through a fresh r6 publication candidate.

Rebuild and validate at least:

- reader manuscript;
- reader-surface input/gate;
- source/citation binding;
- identifier preservation;
- deterministic checks;
- semantic-editorial review;
- visual review;
- quality regression bundle;
- TeX/Bib;
- CI PDF;
- PDF preflight;
- publication candidate;
- reader-publication stage validation;
- publication-candidate stage validation;
- agent-state validation.

Do not reuse r5 PASS artifacts as r6 PASS evidence.

## 10. PDF exact-byte requirements

For fresh r6, independently compute from actual files:

`SHA256(repository main.pdf)`
`== repository main.pdf.sha256`
`== SHA256(Actions artifact main.pdf)`
`== artifact main.pdf.sha256`

Byte counts must match on all surfaces. Page count must be reported.

Perform a fresh full-page visual review; do not rely solely on previous r5 visual PASS.

## 11. Acceptance criteria

All of the following must PASS:

1. Human r5 `REQUEST_CHANGES @ DRAFT_COMPLETE` is canonically recorded against exact r5 authority `342adad3400bd6dee07fb920441f8e259f18eb15`.
2. `99-source-notes.tex` no longer contradicts the explicit use of an official first-party X post as announcement evidence.
3. `community-observation-ledger.md` no longer categorically forbids the narrowly bound official-first-party exception, while independent/community rows remain context-only.
4. Presence in the ledger alone is explicitly insufficient for evidence elevation.
5. Claude Code graceful-stop event date is consistently Sep. 25 across final reader-facing surfaces.
6. Plan-tier details remain separately and transparently secondary/post-window sourced.
7. ART, Cursor, Opus, DolphinBench and prior terminology repairs do not regress.
8. No accepted Evidence/Architecture/Core mutation occurs.
9. Fresh r6 validations PASS.
10. Fresh r6 exact PDF four-surface identity PASSes.
11. Fresh Publication Preview r6 is produced with Human decision `PENDING`.
12. No Freeze / Release occurs.

## 12. Terminal state

Success terminal state:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R6_PENDING`

Human r6 decision must remain `PENDING`.

Do not Freeze or Release.

## 13. Issue #551 reporting

Before stopping, add an Issue #551 execution comment containing:

- canonical r5 gate record identity;
- exact source-boundary wording repair locations;
- exact Claude Code date correction locations;
- confirmation that official-X exception is narrowly binding-specific;
- confirmation that independent/community posts remain context-only;
- confirmation that accepted Evidence/Architecture/Core were unchanged;
- repair commit(s);
- r6 reviewed authority;
- r6 candidate SHA-256;
- r6 PDF SHA-256 / bytes / pages;
- Actions run/artifact IDs;
- four-surface identity result;
- final validation result;
- statement that r6 Human decision remains PENDING.

Keep Issue #551 open until fresh Sol/Human r6 review.

## 14. Required final report

Report:

- starting guard expected/actual;
- Human r5 gate record result;
- changed reader/public files;
- source-boundary repair summary;
- Claude Code date repair summary;
- regression checks;
- validation outputs;
- exact r6 commit/tree;
- candidate SHA;
- PDF SHA / bytes / pages;
- Actions run/artifact;
- four-surface identity;
- Issue #551 comment ID;
- final terminal state.
