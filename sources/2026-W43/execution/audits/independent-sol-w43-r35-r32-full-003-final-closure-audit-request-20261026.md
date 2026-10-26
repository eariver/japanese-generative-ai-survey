# J-GAS W43 — Independent Sol r3.5 FINAL one-finding P1 closure audit request

Status: `INDEPENDENT_READ_ONLY_AUDIT_REQUEST / FIXED_SUBJECT / R32-FULL-003_ONLY / NO_HUMAN_GATE`
Date: 2026-10-26 JST
Repository: `eariver/japanese-generative-ai-survey`
Independent assessor: **a distinct independent Sol session**, not editorial Sol, Muse Worker, and not the Human Owner.

## 0. Immutable audit subject and boundaries

- Existing branch: `weekly/2026-W43-v2-work`
- **Fixed Muse r3.5 audit HEAD: `bc6b1cdf8af266e0072df75449719bf535c65b18`**
- **Fixed Muse r3.5 root Tree: `dfe0eefeb9921327ce17986914fb3c9c02f68bd1`**
- Exact parent (editorial execution contract): `2ec0202bb9c53dba4d8b64b2edfb1b69f117471a`
- Reviewed main: HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`
- Frozen Core v2: HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

Audit contract commit will be **later than r3.5 fixed subject**. If Work branch has advanced due to contract, do not reset audit target to the tip; read target files at the exact fixed HEAD. First verify subject Git commit object/root Tree, direct parent, 1 normal fast-forward commit (no force history), exact ten changed paths confined to `sources/2026-W43/execution/`, and main/frozen unchanged. On mismatch with fixed subject object/tree, stop `AUDIT_SUBJECT_MISMATCH`. No writes to GitHub, State, Gate, Core or production branch; no branch creation. Do not run Core-native validators or TeX/PDF.

## 1. Binding source report and sole scope

Use the preceding **independent** r3.4 report, not Muse/editorial QA as pass authority:
`https://drive.google.com/file/d/1jRqM0m1aVJBkaga3zi3kHYpUNuQwr4ZU/view?usp=drivesdk`
(2026-10-26, `REQUEST_CHANGES`, P0=0/P1=1).
Only `R32-FULL-003` (remaining original P1) is under new audit. Original comprehensive report `GPT-Sol_Review/20261026022400_SolReview.md` has 10 finding IDs, of which 001/002 P1 FIXED and the P2 004–010 FIXED or QUALIFIED_WITH_LIMITATION in the preceding independent review; **do not reopen** other findings absent a newly introduced regression. The approved Architecture / 31-requirement independent assessment stays 20 SUBSTANTIVE_COMPLETE / 11 PARTIAL; no invented upgrade.

**Blind-first**: inspect actual r3.5 reader, ledger, manifest, expected-claim map, raw source snapshots and Python source **before** using Muse's r3.5 result/QA. Form an independent initial conclusion. Then compare to self-QA and to editorial observations. Distinguish audit based on reading source and independently computed facts from mere static-code inspection. Do not claim Python or negative-case execution if only statically followed.

Fixed assets at subject:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md`
- `.../w43-r3-5-citation-confidence-ledger.json`
- `.../w43-r3-5-physical-row-manifest.json`
- `.../w43-r3-5-strict-semantic-claim-join-check.py`
- `.../w43-r3-5-semantic-join-result.json`
- `.../w43-r3-5-source-crosswalk-delta.md`
- Muse r3.5 handoff, session and QA, to be examined AFTER first independent checks.
- r3.4 fixed predecessor for direct compare: HEAD `1a4cfedb95692ae481c241594e24231680a9a01d`, Tree `a79c26efcbb8c7a2a6555c485b243be6c9746a18`.

## 2. Required closure proof (not just table-count smoke)

**A. Actual reader changes and provenance.** Compare r3.4→r3.5 actual text, ledger, manifest. Expected bounded change: one title-version edit plus exactly two `｜` physical rows — `p7-f1-01` COBOL and `p8-f2-03` TanStack npm. Preserve all other rows and claims/blocks, including original 001/002 and P4 FAQ. Confirm all accepted prior evidence limitations still correctly qualified. Inspect the independently accepted claim provenance; avoid a fabricated original.

**B. COBOL (`p7-f1-01/enterprise-40p`).** Reader physical `p7-f1-01` must actually print the `40%+` lexical equivalent (e.g. `40%超`) plus enterprise share/online-banking context, distinct from COBOL benchmark `10.9→72.1`. Confirm its claim `enterprise share` vs `accuracy` is semantically disambiguated, own-block DATA, and does not make `40.3%` Luna cost an accidental false match. Trace evidence `task-160489… claim-3`; where original page is unavailable, preserve `ARCHIVE_UNAVAILABLE`, accepted-derived only.

**C. npm (`p8-f2-03/npm-clock`).** Reader physical `p8-f2-03` must actually print the 2026-10-22 `15:21:49Z` npm timestamp (millis `.491Z` remains in ledger documented), with clear `GH 15:18:14Z` separation. Ensure `https://registry.npmjs.org/@tanstack%2Fai` is scoped and provenance `RAW_NOT_ARCHIVED`; do not use archived GitHub release as raw proof of npm time. Confirm actual printed timestamp is bound to correct DATA row, not merely ledger `clock` field.

**D. Global invariants.** Independently parse reader fenced 表 blocks, exact 20 expected table headers, 80 physical table rows (78 DATA, two NOTE), 3 separate figure rows, 13 sanctioned aliases, ledger 96 blocks, 29 claim records. Verify all 20 headers ↔ ordered manifest IDs, every physical row text/ordinal/reader line ↔ SHA256 ↔ ledger row ID/type both directions, uniqueness/no orphan/cross-block/NOTE claim. Independently inspect all 29 claim attachments: variant/product, metric, printed actual value, unit/comparator, URL, evidence class. Confirm claims remain stable r3.4→r3.5, except if a documented change was authorized (none expected).

**E. Checker strength.** Inspect `EXPECTED_HEADERS`, `EXPECTED_ALIASES`, hardcoded `EXPECTED_CLAIMS` for ungrounded circular proof. Ensure `validate()` will fail on mislinked physical value even if it exists elsewhere or ledger metadata repeats it. Verify every required positive checker failure actually affects the final PASS gate; inspect whether any baseline has lax variant/value/source matching. Test or trace negative tests: physical reader row delete/duplicate/swap/mutate; header edit; 29→28 claims; wrong value/variant/metric/URL/source qualifier; DATA/NOTE; npm URL scope; units; two original r3.4 semantic counterexamples. Prefer independent ephemeral mutation runs if available. Check each of 24 negative outputs for **specific intended error** and differentiate defects from nonmaterial test-coverage gaps. Inspect exact-byte reader, ledger, manifest SHA256 vs separately named canonical JSON hash. If tools cannot run the checker, say so explicitly.

**F. Source limits.** Archived MemT README vs Patch RENDERED_TEXT not raw HTML, TanStack GH JSON raw, npm HTTP response missing, COBOL enterprise 40% original absent, FLUX FAQ unattributed, Voxtral AA/source not obtained, DeepSeek weights LICENSE/SHA not present. No claim of external independent benchmarking or missing-original verification. Structural/semantic edition-local join PASS never means native Core Stage PASS, official draft complete, or publication approval.

## 3. Independent decision, possible refinements, deliverable

Report **one explicit judgment of `R32-FULL-003`**: `FIXED`, `OPEN`, or `QUALIFIED_WITH_LIMITATION` with exact evidence and whether any material P1 remains. Name any newly discovered regression separately. End with one overall limited closure decision `PASS`, `PASS_WITH_LIMITATIONS`, or `REQUEST_CHANGES` **for permission to start NONCANONICAL Core-free PDF Preview preparation only**, not publication or Freeze/Release. `REQUEST_CHANGES` mandatory if a substantive P0/P1 remains; enumerate minimal bounded fixes/tests.

Save the full independent Markdown audit under Google Drive `GPT-Sol_Review` as `YYYYMMDDHHMMSS_SolReview.md` if connected and verify created file link; if unable, return complete report with explicit upload limitation rather than claiming placement.

Read-only end point: `INDEPENDENT_R35_SINGLE_P1_CLOSURE_REPORTED`. No GitHub changes, no Museum/Muse work delegation, no TeX/PDF, no Stage/Human Gate operations. Editorial Sol adjudicates and either asks Muse for a narrowly bounded repair or, upon genuinely clean independent closure, commissions next **Core-free, UNVALIDATED PDF Preview** with full-page QA for Human approval.
