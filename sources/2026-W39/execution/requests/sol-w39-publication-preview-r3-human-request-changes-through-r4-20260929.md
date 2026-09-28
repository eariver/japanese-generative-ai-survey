# W39 Publication Preview r3 — Human REQUEST_CHANGES through fresh Publication Preview r4

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R3_REQUEST_CHANGES / BOUNDED_AT_FRESH_R4_PUBLICATION_PREVIEW`

Date: `2026-09-29 JST`

## 1. Human decision authority

The Human Owner explicitly requests continued repair after Sol's independent review of Publication Preview r3.

Canonical Human decision to record:

- Gate: `PUBLICATION_PREVIEW`
- Revision: `r3`
- Decision: `REQUEST_CHANGES`
- Regeneration boundary: `DRAFT_COMPLETE`
- Reviewed repository commit: `4463e80e1e01476adf12586a705006e7bbcda8a6`
- Reviewed tree: `60c4cfaccaf2a21f4293a10ad9d79f74421d74dc`
- Reviewed candidate SHA-256: `7def181d8811b52ee20b17b7b5bca04eb6875c373d4e3203b944b651e0fc26c3`
- Reviewed PDF SHA-256: `7fac4b5c76695edb9821dc3c2463bc281014407cd01ec5a9c4c1784d711d8cdb`
- Reviewed PDF byte count: `329744`
- Reviewed PDF page count: `12`

This decision authorizes only publication-local regeneration from `DRAFT_COMPLETE`. It does not reopen Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture. Human Architecture Review r1 remains `APPROVED` and immutable.

## 2. Mission

Record the Human r3 `REQUEST_CHANGES` canonically using the current reviewed Core Human Gate tooling, return the edition to the allowed `DRAFT_COMPLETE` boundary, repair the remaining reader-facing Japanese language defects identified by Sol's exact-final-byte review, regenerate the publication surface canonically, prove PDF byte identity, and stop at a fresh Human Publication Preview r4 with Human decision `PENDING`.

Do not Freeze. Do not Release. Do not create or infer a Human r4 decision.

## 3. Starting guards

Work only on existing branch:

`weekly/2026-W39-v2-work`

The execution prompt supplies the exact remote starting HEAD/tree. Before any write, verify read-only:

1. remote W39 branch HEAD/tree exactly match the supplied expected values;
2. remote `main` remains `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`;
3. frozen `production/survey-core-v2` remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
4. reviewed r3 authority `4463e80e1e01476adf12586a705006e7bbcda8a6` is an ancestor of the current W39 branch;
5. `sources/2026-W39/execution/reviews/publication-preview-r3.md` still binds the r3 authority/candidate/PDF above with Human decision `PENDING` before recording the new decision.

If any guard fails, perform zero writes and report expected vs actual values.

## 4. Forbidden actions

- No new branch, fallback branch, repair branch, or review branch.
- No force push, reset, rebase, history rewrite, or branch replacement.
- No Shared Core edit.
- No `main` edit.
- No `production/survey-core-v2` edit.
- No reopening/recomputing Discovery through Architecture.
- No unsupported factual/content expansion.
- No blind lexical replacement.
- No direct/manual PDF byte editing.
- No manual checkpoint/state surgery that bypasses canonical Core tooling.

Use normal commits and non-force push only. Perform remote read-back after each write group.

## 5. Canonical Human r3 decision recording

Use the current reviewed Core canonical Human Gate/revision tooling to record exactly:

`PUBLICATION_PREVIEW r3 = REQUEST_CHANGES @ DRAFT_COMPLETE`

Bind the record to the exact reviewed r3 repository authority, candidate SHA, and PDF SHA from §1.

Do not hand-author a fake gate record if canonical tooling exists. Validate the resulting Human Gate state before proceeding.

## 6. Terminology QA authority — four-file union

Treat the following four files as one combined read-only terminology QA corpus:

1. `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
2. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
3. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`
4. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r3-residual-additions.md`

The corpus is not a replacement dictionary. Enumerate every observed/search form from all four files and search every exact reader-facing source that feeds the final PDF.

For every search form/hit, record one of:

- `REPLACE`
- `RETAIN_WITH_CONTEXT_REASON`
- `ZERO_HIT_CHECKED`

Every retain requires a context-specific reason. A phrase may be retained only when it is conventional, precise, source-faithful, and does not force a technical reader to reconstruct the English source phrase.

## 7. Mandatory r3 residual adjudication

At minimum, independently find and adjudicate every r3 residual recorded in the fourth supplement, including:

- `今号の物語に入れない`
- `遺伝子操作への用立て`
- `スコア比較は本号では真としない`
- `ベンチマークのスコア比較は真としない`
- `高速モードは2.5倍の速さで倍の値`
- `トークン代を7%ほど軽くした`
- `ベンチマークの深追いは本号ではしない`
- `測られた数値の出所`
- `値札`
- `目配り`
- `手ほどき`
- `素性`
- `脇を固めた`
- `動向をうたう言い回し`

These are a minimum set, not an upper bound.

Preferred repair direction is documented in the r3 supplement. Preserve source meaning, uncertainty, attribution, dates, numbers, citations, package boundaries, and temporal boundaries exactly. Where the source context requires a different conventional expression than the supplement's example, use the source-faithful expression and record why.

## 8. Exact reader-surface scope

Search and review all canonical final-PDF inputs, including at least:

- `surveys/weekly/2026-W39/main.tex`
- all `surveys/weekly/2026-W39/sections/*.tex`
- reader-visible bibliography text where wording is edition-authored rather than quoted source metadata
- publication reader manuscript / reader-surface structures regenerated from those sources

Do not treat frozen internal Draft/Architecture artifacts as reader-surface defects unless they are rendered into the PDF. Preserve frozen upstream authority.

## 9. Seed-external final-byte review

After all corpus-based edits and after the exact final TeX bytes are fixed, perform a fresh full semantic/editorial reread of the exact final reader bytes.

This reread must actively detect:

- coined/nonstandard Japanese replacing standard technical terminology;
- literary metaphor inside technical/evidence-boundary statements;
- archaic or colloquial wording that obscures a technical concept;
- Chinese-like literalization;
- identity-destroying translations of model/benchmark/metric/method/tool/product names;
- vague substitutes for price, benchmark validity, model identity, deployment status, provenance, temporal inclusion/exclusion, or availability;
- grammatical errors and typos;
- contradictions between the QA report and final reader bytes.

Do not reuse an intermediate scan as the final scan.

If a new generic defect is found, add it to an explicit successor terminology supplement before completing r4. Do not modify the existing four seed files destructively.

## 10. Content invariants

Language repair must not alter substantive authority. Confirm that r4 preserves:

- seven approved packages, order, purposes, must-cover items, and boundaries;
- all selected/HOLD dispositions;
- all cited source identities and citation keys unless a purely mechanical citation repair is necessary;
- vendor-claim attribution and caveats;
- X/community context-only status;
- W39 temporal boundaries and late-only isolation;
- all material numeric values and dates;
- DeepSeek carry-over limitations;
- Grok harness/evaluation limitations;
- Opus eval-awareness limitation;
- MentalHealthBench grader-circularity limitation;
- DolphinBench PDF-unconsumed limitation;
- Private AI Compute availability/audit limitations;
- TBC and Pixel Canary quarantine/HOLD treatment.

Any non-language substantive change is outside this execution authority and must BLOCK instead of being silently introduced.

## 11. Canonical regeneration

After Human r3 `REQUEST_CHANGES` is recorded and reader-language repairs are complete, run the current frozen Core publication pipeline from the canonical allowed boundary.

Regenerate/revalidate as required by Core, including:

- DRAFT_COMPLETE checkpoint authority for the repaired reader surface;
- reader manuscript;
- deterministic validation;
- architecture-to-draft / identifier-preservation checks;
- citation/source binding;
- lexical/reader-surface gate;
- semantic-editorial Worker review;
- visual Worker review;
- quality regression bundle;
- TeX/Bib publication surface;
- CI PDF build;
- PDF preflight;
- publication candidate;
- stage validation;
- agent-state validation.

Do not claim PASS from stale r3 validation artifacts. All r4 validation evidence must bind the exact repaired r4 bytes.

## 12. PDF four-surface byte identity

For the fresh r4 PDF, independently calculate from real bytes and require:

`SHA256(repository main.pdf)`
`== repository main.pdf.sha256`
`== SHA256(Actions artifact main.pdf)`
`== artifact main.pdf.sha256`

Also require identical byte count and page count where applicable.

A successful workflow, matching filenames, matching byte count alone, or matching sidecar text without hashing the actual PDF is insufficient.

If exact-byte identity cannot be achieved without Shared Core modification, BLOCK and stop rather than modifying Core.

## 13. Fresh Human Publication Preview r4 stop

Only after all language QA, validation, PDF identity, and state validation pass, create a fresh Human Publication Preview r4 shell/dossier bound to the exact r4 reviewed repository commit, candidate, and PDF.

Final state must be:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R4_PENDING`

Human r4 decision must remain `PENDING`.

Do not Freeze or Release.

## 14. Required final report

Report at minimum:

1. starting remote HEAD/tree and guard verdicts;
2. canonical r3 Human `REQUEST_CHANGES` record path/id/reviewed authority;
3. exact DRAFT_COMPLETE regeneration boundary reached;
4. four-file union corpus counts by file and total search forms;
5. total hit counts and `REPLACE` / `RETAIN_WITH_CONTEXT_REASON` / `ZERO_HIT_CHECKED` counts;
6. disposition of every §7 r3 residual;
7. seed-external exact-final-byte scan result and any newly added successor supplement;
8. confirmation that factual/numeric/temporal/evidence/citation invariants were preserved;
9. r4 CI run ID and artifact ID;
10. repository PDF SHA/bytes/pages;
11. repository sidecar SHA;
12. artifact PDF SHA/bytes/pages;
13. artifact sidecar SHA;
14. explicit four-surface identity verdict;
15. semantic-editorial, visual, lexical, deterministic, stage, and agent-state validation verdicts;
16. exact r4 reviewed production authority commit/tree;
17. final branch HEAD/tree;
18. explicit statement that Human r4 decision remains `PENDING`, and Freeze/Release were not performed.

Any blocker must be reported precisely and the run must stop without unauthorized workaround.