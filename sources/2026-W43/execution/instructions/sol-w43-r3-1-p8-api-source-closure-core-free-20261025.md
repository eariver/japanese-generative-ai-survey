# W43 Muse Core-free Draft r3.1 — P8 example and provenance closure

Status: `SOLE_MUSE_R3_1_EXECUTION_CONTRACT / BOUNDED_EDITORIAL_FIX / NO_CORE_REPAIR / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST.
Repository `eariver/japanese-generative-ai-survey`, existing branch ONLY `weekly/2026-W43-v2-work`.
The exact start work HEAD/Tree is provided by Sol dispatch AFTER this contract is added. Main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Root Tree `a134dc36a407d08ab1de416324229b3955e0325a`; Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## Mandatory guards

Before ANY write remote work/main/frozen six-way read-only exact HEAD+Tree vs Sol dispatch. Mismatch `STOP_ZERO_WRITES`. Local checkout if clean and FF-behind remote only: fetch + `git merge --ff-only` following guard; else STOP. No new/fallback/review branches, history rewrite, merge commit, force, reset, rebase, shared Core/State/Architecture/Selection/Evidence/Human gates edits. Do not run frozen-native broken Draft runner or fake QA/stage.

## Mandatory documents

1. Binding editorial Sol r3 verdict `sources/2026-W43/execution/reviews/sol-w43-r3-post-independent-audit-editorial-verdict-20261025.md` (R3-SOL-01 through R3-SOL-04), and original independent r2 receipt + adjudication 11 findings.
2. Fixed Muse r3 `696f0d83cd5b506f58085f8537c7b91ee7741c9e` / Tree `390e60e9f676a3bb47f10e414d100921b7926657` artifacts: reader preview, 96-row ledger, QA, crosswalk, handoff; preserve them unchanged as history.
3. Actual publicly available **first-party** OpenAI Decisions official developer docs: `https://developers.openai.com/api/docs/guides/decisions` (contains an Oct25-observed `POST /v1/decisions` + `gpt-6-luna` JSON request example and illustrative response snippets), `https://developers.openai.com/api/reference/resources/decisions/methods/create`, `https://developers.openai.com/api/reference/typescript/resources/decisions/methods/create`. This Sol directly found the guide; Muse MUST itself fetch/read the actual source, record date, excerpt/hash/snapshot if legally allowed. If inaccessible, STOP `SOL_W43_R3_1_DECISIONS_SOURCE_BLOCKED`; don't invent schema/response.
4. Accepted 2026-W43 Decisions Evidence and original Oct22 GA article `https://openai.com/index/decisions-api/`. October 25 live documentation is a secondary observation time **after W43 issue cutoff**. Do not infer it was published unchanged by Oct22 or promote new postcutoff features as W43 event.

## Bounded patch (NEW edition-local r3.1 assets, never overwrite r3)

**R3-SOL-01 P1 / P8 actual JSON:** create actual copyable and parsable JSON **request** in reader-facing §8.1 with the official schema (`POST /v1/decisions`, `model`, `input`, `questions`, `predicate` `name`/`instructions`). Also show an **official illustrative response excerpt** with `answers[]`, `name`, `type`, `probability`; response's scenario may differ from the shown request if the official published examples do not pair, but **explicitly label that**; never fabricate probability, cost, TTL, response data or assert real API execution. `NOT_RUN` and `ILLUSTRATIVE` labels stay. Clearly distinguish publisher's Oct22 GA description from Oct25 guide read. Replace `p8-f1` checklist in new reader with JSON + short usage explanation, preserve old checklist information in P8 prose or QA as supported.
- Syntax-validate JSON snippets (parsing only) and verify required fields against documentation; not live API call. Check character encodings and code fences and product/SDK status. If source lacks matching example, use exact official guide request body plus separately identifiable official response excerpt from another scenario; don't mismatch names claiming a paired run.
- Update per-claim `ledger` P8-f1 with exact doc URL, verified source tier/time, saved excerpt/snapshot path and `SOURCE_REPORTED` not independent `VERIFIED_DIRECT`, extra sample provenance metadata distinguishing instruction/actual outputs. If new documentation constitutes a materially novel outside-W43 claim rather than documentation of selected topic, STOP and consult Sol.

**R3-SOL-02 P2 / quantified depth QA:** recompute char counts for fixed r2/r3/r3.1 directly with one documented consistent counting method. Previous r2 full Markdown JavaScript string length 26,678 / r3 32,065 = +5,387 code units, **including headers/tables**; these are Sol direct GitHub text observations and are not automatically narrative prose chars. Report prose-only measures separately if useful, with exact reproduction command and path/hash. Correct unsupported "+9,900 substantive characters" and the associated r3 session/handoff historical fact via a new correction note, NOT by rewriting r3 history.

**R3-SOL-03 P2 / reader-only cleanup:** remove from the end of new reader preview `（了。運用メモ・編集注記は \`w43-r3-editorial-qa.md\` に移管した。）`. Keep all five final `今週の総括` paragraphs intact after P8 and before references, no editor-only comments in reader view. QA separately records this change.

**R3-SOL-04 P2 / source crosswalk anchor:** provide fully-qualified correct repository-relative archive paths for critical multi-product table/figure sources, avoiding `collectors/.../` shorthand. No fabricated archive paths; verify existing files on fixed commit. Each `table_rows[]` external primary URL/claim pointer should map to exact source or explicitly `ARCHIVE_UNAVAILABLE`. Retain 96 unique ledger IDs, 19 selected, 8 packages/31 must covers and all 5 LIMITED plus 68 Attention; r3 28/3 truth states may update only with shown evidence. Twenty tables still `DRAFT_TEXT`, not TeX QA.

## Deliverables

On same existing work branch, write NEW:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-1-reader-preview-UNVALIDATED-20261025.md`
- `sources/2026-W43/execution/editorial-bypass/w43-r3-1-citation-confidence-ledger.json`
- `sources/2026-W43/execution/editorial-bypass/w43-r3-1-source-crosswalk.md`
- `sources/2026-W43/execution/editorial-bypass/w43-r3-1-editorial-qa.md`
- `sources/2026-W43/execution/SOL_W43_CORE_FREE_EDITORIAL_R3_1_POST_R3_SOL_HANDOFF.md`
- edition-local session log and navigation updates.
Current `r3`, r2, r1 and original unvalidated source remain unchanged. Snapshot collected official guide/document lines with provenance if license/rights permit, no silent new W43 fact. No claim of endpoint successful run or Core QA PASS.

Stop upon normal commit, nonforce push and remote HEAD+Root Tree readback:
`SOL_W43_CORE_FREE_EDITORIAL_R3_1_READY_FOR_SOL_SPOTCHECK`.
If P8 source unavailable, stop `SOL_W43_R3_1_DECISIONS_SOURCE_BLOCKED`. If source schema contradicts legacy Evidence, stop `SOL_W43_R3_1_SOURCE_CONFLICT`. Do not advance Stage, TeX/PDF, Publication Preview, Freeze or Release; all are separately governed later. Sol then performs targeted spotcheck and independent full r3.1 differential review with fixed exact SHA.
