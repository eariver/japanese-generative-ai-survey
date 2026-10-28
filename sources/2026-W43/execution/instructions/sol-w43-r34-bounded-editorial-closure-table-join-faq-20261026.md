# W43 editorial Sol r3.3 inspection / r3.4 bounded closure execution contract

Date: 2026-10-26 JST
Authority: EDITORIAL_SOL_REVIEW_AND_EXECUTION_CONTRACT; not independent audit, not Human approval.
Target: existing `weekly/2026-W43-v2-work` only.
Status: `EDITORIAL_CHANGES_REQUIRED / R32-FULL-003_P1_OPEN / R32-FULL-006_P2_OPEN / PREVIEW_STOP`.

## 0. Execution precondition — ZERO WRITES on any mismatch

Read **remote** six-way exactly, before fetch/rework and before any write:

| Ref | Exact HEAD | Exact root Tree |
|---|---|---|
| `weekly/2026-W43-v2-work` | `4f89fba23bdbf8ff88f4dddabd3e0a2352007de3` | `aed10c3388e3852b34fd32bbaa68ad4c915179fb` |
| `main` | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| `production/survey-core-v2` | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

**Important:** the above W43 SHA is the r3.3 subject before this Sol contract commit. At execution start the remote W43 HEAD will ordinarily be advanced by one editorial-contract-only commit. **Do not use this stale W43 value as an authorization after placement.** Editorial Sol will provide the actual contract-commit HEAD and Tree in the dispatch message. The three pairs in that dispatch are the authoritative start guard; if they differ from the remote, stop ZERO WRITES. Confirm this contract's parent exactly equals `4f89...` and diff is this new contract file only.

No new/fallback/review/repair branch, no reset/rebase/force, no direct main/Core edits. A clean local behind may fetch+ff-only. Edition-local changes only; no formal Stage, no Gate mutation, no TeX/PDF or release. Normal commits, non-force push, readback after completion.

## 1. Basis and Sol adjudication

Fixed inspected r3.3 subject: `4f89fba23bdbf8ff88f4dddabd3e0a2352007de3` / Tree `aed10c3388e3852b34fd32bbaa68ad4c915179fb`.
Parent `1dc4e1e8cc9d3d91d066c4b3f5837e0ff9211f45`; GitHub compare ahead 1, behind 0; changed paths 9 and all under `sources/2026-W43/execution/`.
The historical r3.2 independent comprehensive audit original is `20261026022400_SolReview.md` in Drive `GPT-Sol_Review`, SHA256 `78a61517d59c8140f1c32eff21376657374ab2d7d37af7a4939e63f7bfb1846f`, REQUEST_CHANGES P0=0/P1=3/P2=7. Its adjudication/contract and Muse r3.3 handoff are in this edition.
Sol checked actual W43 reader, 96-block ledger, join-check code/result, MemT archived README line 24/55/208-219, Patch RENDERED_TEXT lines 15-25, plus corrected P3/P4/P5/P7 excerpts. R32-FULL-001 and -002 are editorially provisionally repaired; this is not an independent PASS. R32-FULL-004/-005/-007 appear corrected. R32-FULL-008/-009 have bounded evidence limitations; -010 is partially addressed and subject to eventual independent closure.

Two closure defects require an **exclusive, bounded r3.4 repair** before any independent closure or PDF.

### R32-FULL-003 — P1 still open: checker does not prove physical row joins

- The reader contains **20 fenced tables with 80 physical table rows**, and ledger has 20 TABLE blocks with 80 table_rows (of which 2 typed NOTE), plus 3 figure rows. Count coincidence is not a row join. 29 claims have row_id; no currently dangling cross-block references were observed, but this is not proof of semantic source binding.
- In the actual reader vs ledger, **13 physical-row labels are not exact** even though row order and counts match: p1-t2 Kimi/Flint/Nemotron, p1-t4 three variants, p2-t2 11bench/1.86x/66x, p2-f2 software/third-party, p4-t1 22x, p5-t1 TTS Speech 3. Aliases can be correct but need explicitly governed 1:1 mapping.
- `w43-r3-3-table-join-check.py` S8 accepts a table when **any** ledger DATA label's first six characters appear **anywhere in the entire reader**; it never parses and exhaustively matches each physical row. S3's `noted` list is computed but `check("S3-claims-linked", not orphan, ...)` ignores it, so a NOTE-reference could wrongly PASS. Claim `row_id` owning-block, variant, unit, comparator, URL scope, and exact row contents are not fully validated. `STRUCT_PASS 33/33` is therefore a **limited smoke test**, not the P1 acceptance test. Do not silently promote it.
- Original independent audit's acceptance: **20/20 tables all physical data rows ↔ canonical row IDs ↔ ledger ↔ corresponding claim/source, bidirectional**, NOTE excluded, no orphan, no false source upgrade, and test verifies actual contents not only counts.

Required r3.4 solution:
1. Preserve the r3.3 immutable reader/ledger/QA artifacts. Produce a new r3.4 reader, ledger, edition-local physical-row manifest (or equivalent unambiguous inline identity with rendering-safe strategy), strict checker, machine-result JSON, crosswalk delta, editorial QA and handoff. Reader-friendly row labels should not be cluttered with operator IDs in final printed text.
2. Give every **one of 80 physical rows** an exact immutable `row_id` by mapping stable table identity + within-table physical row ordinal + **full exact physical row text/hash**, captured in a machine-readable manifest. Make table IDs explicit and unambiguous; do not rely on positional ordering alone without unique header/table identity, and avoid global substring lookups. Ledger row_id must join 1:1; explicitly record sanctioned aliases for those 13 labels without asserting literal equality. Classify the 2 NOTE rows separately and preserve 3 figure rows as distinct scope.
3. Parse all 20 reader fenced tables. Assert exact 20 matches and **both-way total bijection 80 physical ↔ 80 ledger**, with no missing, duplicate, extra, or swapped row. Assert 29 claims are on a DATA row in their **own** block, reference correct variant/model, metric/unit/comparator, and expected source link/class or an honest `ARCHIVE_UNAVAILABLE` qualifier. Assert no NOTE claims; make `noted` trigger FAIL. Npm `@tanstack/ai` scope/clock, Voxtral product/unit, p3-t2 classifier, p5-t1 TTS Speech 3, p5-t2 Controlled Voice, MemT storage meaning need specific assertions. Row-level provenance counts by raw-primary/accepted-derived/unavailable with definition and no false verified promotion.
4. Validate the negative case: remove/duplicate/swap one physical row; mutate a row's text; point claim to NOTE or to wrong table/model; change scoped npm URL to unscoped; change a unit. Test runner must FAIL, not just return PASS on original.
5. Report explicit row-id→reader-line/span + exact reader/ledger SHA256, and scoped validation `EDITION_LOCAL_ROW_JOIN_PASS` **only if genuinely proven**. This never means source originality or native Stage PASS. If proof cannot be constructed, mark P1 OPEN, stop and report; do not invent a checker PASS.

### R32-FULL-006 — P2 residual: unresolved FAQ wrongly called confirmed conflict

- In r3.3 reader at P4 introductory line and in §4.1 / later subsection, phrases such as `資料間で矛盾する`, `keyframes の扱いは資料間で矛盾する`, `keyframes の矛盾` remain despite `UNRESOLVED_FAQ_ATTRIBUTION` and an **unretrieved FAQ source**. Original independent audit explicitly prohibits confirming official-to-official contradiction without FAQ date/URL/original text.
- Correct reader-facing Japanese: 10/19 PR makes an availability claim, whereas an unattributed `Two at launch` phrase is not yet verified. As of W43 cutoff no definite source conflict can be proven; keyframes live/schema/GA UNKNOWN. Preserve benchmark arithmetic and all evidence limitations. Check *every* P4 mention, including heading and closing recap where relevant. Reader prose should not call it a confirmed contradiction. This fix must not rewrite accepted Architecture.

## 2. Stability and scope

R32-FULL-001/002 correct P1 meanings must be preserved (MemT 128K full-context KV **storage** ~1/66, vendor benchmark parametric scope; 1.86x SOURCE_UNVERIFIED; Patch stage4 product-update preparation, stage5 guidance/deployment after patch availability; Daybreak/checker outside; CVE not found != none). R32-FULL-004 npm scoped package, -005 clean header, -007 path split, -008/-009 bounded limitations, -010 pseudocode labels must be maintained. No gratuitous rewrite or new research/Architecture changes. Keep 8 packages, 31-requirement independent baseline 20 COMPLETE/11 PARTIAL, five-paragraph recap, r3.3 historical bytes, 96 block IDs, 29 numerical claims unless justified with explicit change; 19 SELECTED etc untouched.
All W43 `production-state.json`, Human gates/reviews, accepted Evidence, Selection, Architecture, main, Frozen Core, shared Core path roots and earlier artifacts are protected. Exact remote full diff and SHA/tree proof in Muse final report.

## 3. Stop boundary and next step

Stop at `MUSE_W43_R34_BOUNDED_ROW_JOIN_FAQ_REPAIR_READY_FOR_SOL_EDITORIAL_RECHECK`. No PDF, no Human Gate action, no Freeze/Release. After Sol validates the strict checker and reader correction, commission **one** separate independent Sol **10-item r3.2→r3.4 limited closure audit** at a fixed HEAD/Tree, blind-first/read-only. Only on independent PASS/PASS_WITH_LIMITATIONS with no P0/P1 may Sol direct Muse's Core-free NONCANONICAL PDF Preview. The user alone approves the actual PDF and separately authorizes any exceptional official publication route.
