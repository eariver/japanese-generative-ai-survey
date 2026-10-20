# J-GAS W42 — Muse r32 Issue #570 limited Argon unified-token correction to fresh Publication Preview

Date: 2026-10-20 JST
Status: `EXECUTION_AUTHORITY / HUMAN_ISSUE570_LIMITED_REQUEST_CHANGES / ONE_INTEGRATED_MUSE_RUN / STOP_AT_FRESH_PREVIEW`
Repository: `eariver/japanese-generative-ai-survey`
**Only existing branch:** `weekly/2026-W42-v2-work`
**Actual Muse starting exact HEAD/Tree:** supplied by Sol dispatch after committing THIS document; verify against live remote read-only. Parent baseline `734b0d08b00e2bfce8219c598eca3e897675066f` / root Tree `505601acdb9d5d58bef55c9a01d8060876f55008`.

## 0. Mission

In one bounded execution, resolve Human-owned GitHub Issue **#570**, correcting exactly two reader-facing Argon token-limit statements in W42 Section 1/Table T1. Under proper Human `LIMITED REQUEST_CHANGES` authorization use the canonical first-party **Publication Preview REQUEST_CHANGES** to `DRAFT_COMPLETE`, rebuild new PDF/Reader/current formal QA and reviews, perform focused delta semantic/visual inspection on corrected pages, then trusted first-party GitHub Actions Stage transitions `DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE`. Stop at new Human Publication Preview pending and present fixed immutable PDF; NO approval, Freeze or Release. No micro-signoffs for routine deterministic substeps.

## 1. Trust preflight — absolutely zero writes on mismatch

Read in order: (1) `sources/2026-W42/execution/governance/human-w42-r32-issue570-limited-preview-request-changes-authorization-20261020.md`; (2) this contract; (3) Sol Issue #570 disposition `sources/2026-W42/execution/reviews/sol-w42-r32-issue570-source-verified-acceptance-disposition-20261020.md`; (4) live Issue #570 body/comment thread; (5) r31 Gate r1 REQUEST_CHANGES, State, Candidate, source/Reader/PDF SHA, Session and execution index; (6) reviewed main frozen Core validator/operator workflow and matching schemas; (7) exact reviewed Google official documents linked in the Human authorization.

MUST verify:
- live `weekly/2026-W42-v2-work` HEAD and root Tree exact Sol dispatch values; ancestry to r31 fixed `734b0d08b00e2bfce8219c598eca3e897675066f` / `505601acdb9d5d58bef55c9a01d8060876f55008`; clean isolated worktree, no concurrent mutation;
- reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` root Tree `801de813319f08777ab1581a5e8875fc1ac5df19`, frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`, state-pinned implementation `a4f25630270f029656f35771592f9ebda02fa5cc` / Tree `e68560d1542806b61b4c55f03063839fd2ec30c0`;
- Architecture r1 SHA1 `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`, architecture review approved, r18 proposed Reader master unchanged; r31 current TeX exact SHA256 `008b6a279185b14693ebeffe54ef1f4db4397d00946b9ebcd1248f662ca81e4e` (97154 bytes) and PDF `026386115c924b9e7188fb697b8bf1585cf824bcd8affa19a912760167b8fc0c` (505327 bytes, 21pp);
- state `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / publication_preview=pending / architecture_review=approved`; Gate index = ARCHITECTURE r1 APPROVED + PUBLICATION r1 REQUEST_CHANGES, hence expected next PUBLICATION r2 if still unchanged;
- reviewed main unchanged and no concurrent request-only admission in flight.

Anything inconsistent → STOP `W42_R32_PREFLIGHT_BLOCKED / ZERO_WRITES`. No new branch, rebase, reset of any kind, force, shared Core, config/schema/workflow/main edits, or unapproved reader-content expansion.

## 2. Official Gate revision first, with real GitHub Actions trusted admission

Before any current TeX/PDF/Reader overwrite, ensure authenticated first-party workflow route is available. Follow the **same actual tested trusted route from r31**:
- official workflow `.github/workflows/survey-production-v2-operator-bridge.yml` reviewed main;
- create a single NEW `sources/2026-W42/execution/requests/muse-w42-r32-issue570-preview-revision-20261020.json` as the **only changed file** in its own normal FF commit;
- `operation.kind=REQUEST_PUBLICATION_PREVIEW_REVISION`;
- `expected_revision` from actual Gate index (anticipated `2`), `regeneration_boundary=DRAFT_COMPLETE`, `state_path=sources/2026-W42/production-state.json`;
- `requested_changes`: exactly Issue #570 Argon body/Table T1 unified context vs normal single-output vs long decode; never mention r31's already-corrected ASPIRE as needing another fix;
- `reviewed_repository_commit_sha` equals request-only commit **parent** (the fixed r32 dispatch authorizing this limited change);
- `reviewed_by=Human Owner`, `review_reference` names Human authorization file and Issue #570 URL, clearly explains Human message date-only provenance. Use truthful ISO formal-review-recording timestamp for `reviewed_at`, not fabricated owner click seconds;
- all request fields exact `schemas/operator-execution-request-v2.schema.json` schema.

Commit, non-force push, trigger **authenticated Human/owner authorized** issue #448 exact `/survey-core-execute <40 lowercase hex request-only SHA>` or an officially accepted same-repo PR transport **without new branch**, and save actual workflow run URL/ID, trusted reviewed-main runtime, `operator-preflight` and `operator-execute` success and receipt. The request commit must be exact remote HEAD during admission; do not move branch while run is active. No local CLI substitute. No manually authored Gate decision / Stage state.

Read back real Core-generated `sources/2026-W42/gates/reviews/publication-r2.json` with `REQUEST_CHANGES`, updated Gate index keeping r1 historical record, current State `DRAFT_COMPLETE`, architecture r1 still approved; list precisely native invalidated checkpoints/removed paths. Historical r31 file bytes remain retrievable through Git and audit records untouched.

If official workflow cannot run, STOP BEFORE Gate mutation `W42_R32_TRUSTED_OPERATOR_UNAVAILABLE`. No unreviewed alternative route.

## 3. Strictly TWO reader-facing edits, Google-primary sourced

Old original TeX near **L64**:
`出力100万トークンという文脈長の大きさとあわせて、長時間作業を前提にした価格設計と読める。`

Correction must precisely convey:
1. **1,048,576 tokens** is a unified context window shared by **input, thinking, output, and function call history**, NOT 1M unconditional per-response output; each category consumes the same finite budget.
2. Ordinary synchronous calls cap **65,536** tokens per generating hop/response (including thinking as specified by API), whereas direct non-streaming GenerateContent REST caps **32,768** without continuation. Distinguish transports, do not describe all non-streaming APIs as 32,768.
3. Greater-than-65,536 long output/reasoning needs explicit supported **long decode/continuation** and compatible SDK/harness, `max_output_tokens>65,536` where the API requires it; e.g. Interactions `background:true` server continuation, GenerateContent upgraded SDK or client continuation. The maximum is constrained by 1,048,576 minus consumed inputs/thinking/functions; changing only the model ID does not enable long decode.
4. Preserve identical original price terms (intro 2/10 USD per 1M input/output; 11/30 → 4/20), price framing and surrounding paragraphs, evaluation/source caveats.
5. Japanese must be readable rather than unnecessary translated kanji/jargon; prefer `入力・思考・出力で共有する統合枠`, with `long decode（継続生成）` once.

Suggested content direction (NOT compulsory verbatim if source-faithful):
`Argonの料金は導入時が入力2ドル・出力10ドルで、11月30日から4ドル・20ドルに上がる。1,048,576トークンは入力・思考・出力（関数呼出しを含む）で共有する統合枠で、通常の単一生成は最大65,536トークン（直接の非ストリーミングRESTは32,768）に限られる。それを超える生成には対応API・SDKでのlong decode（継続生成）が必要で、入力等が使った分だけ総枠の残りは減る。料金改定は導入期と定常期を分けた設計であり、長時間利用の見積もりに直結する。`
Ensure this does not imply there is a guaranteed visible 65,536-token answer while thinking consumes generation budget.

Old original **Table T1 Argon row near L105**, replace only `出力100万トークン` with a very compact source-faithful phrase:
`統合枠約100万（入力・思考・出力で共有、長文は継続生成条件つき）`.
Keep price/date, Wonder row, Minecraft conditions, captions, current 7-table structure, no other cell edits; long decode API conditions and standard limits are in body rather than overfilling table cell.

Authoritative references (verify access and quote short source facts with date/method in edition-local source evidence only):
- https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- https://ai.google.dev/gemini-api/docs/tokens
- https://ai.google.dev/gemini-api/docs/long-decode (Interactions)
- https://ai.google.dev/gemini-api/docs/generate-content/long-decode
- https://ai.google.dev/gemini-api/docs/latest-model

**Citation scope:** Issue #570 explicitly limits reader-facing changes to the TWO sites. Existing §1 citations and 90 bibliography keys, P1 architecture and Reader baseline stay intact; archive exact primary URLs and captured evidence in `sources/2026-W42/execution/issue570-r32/`. Do not silently add bibliography keys or new reader paragraphs outside the two sites. If edition citation schema demands a new printed source key for this newly precise claim rather than edition-local provenance, report the conflict; do not enlarge authority unilaterally.

## 4. Byte-bound rebuilt PDF and differential QA

After successful native Gate revision, replace current canonical `surveys/weekly/2026-W42/main.tex`, `main.pdf`, updated current `sources/2026-W42/publication/v2/reader-manuscript-v2.json`, and all dependent formal quality, semantic, visual, Reader-Surface review/Gate and Candidate JSON/deterministic QA artifacts as the actual Core validators require. Old r29/r30/r31 commits and their human/independent audit records remain immutable; canonical replacements must be auditable via **old→new hashes, line diffs, page mapping and SHA references**. Do not touch r18 PROPOSED Reader master, Architecture r1, Selection/Evidence or frozen Core; do not reset.

Keep R31 21-page PDF layout and accepted Human Route A whitespace unless content legitimately causes page shift; no 28-page target/padding. Compile with established LuaHBTeX/preview.sty, record engine/version/log/epoch and PDF SHA256. Render new PDF to actual page PNGs and compare against verified r31 PNGs:
- first inspect baseline affected **p03–p04** (Argon body and Table T1) and neighboring **p02 and p05**; expand to any page to which paragraph/table/caption flows;
- verify no header orphan, split/misaligned Table T1, clipped table cell, Japanese glyph dropouts, overlaps, unexpected large blank blocks or page-count change; explicitly record page number mapping, actual changed page hashes/pixel diff and justified reflow;
- verify all 7 tables and 90 bibliography/citation keys unchanged apart from the designated Argon Table T1 cell; P1–P7 package coverage and 28/28 selection unchanged; prior independent 21pp/110-cell audit applies ONLY to unchanged bytes, not new pages.
- focused separate **read-only independent delta reviewer** must inspect both changed prose and table semantics, exact new TeX/PDF hashes, affected page PNGs, adjacent pages, and preservation of full-book unchanged content. Persist its raw attributable report; no fake independent status, no all-book re-audit.

Regenerate seven Core `DRAFT_COMPLETE` authorities `reader-manuscript`, `validated-source`, `publication-pdf`, `quality-regression-bundle`, `semantic-review`, `visual-review`, `reader-surface-gate` with genuine validation and a separate Reader-Surface semantic reviewer; use actual original Core builders/validators, no schema/threshold weakening or reused r31 PASS hashes for new source. Candidate must bind newly exact bytes. Disclosure of prior accepted whitespace remains; no Release.

## 5. Two real trusted Stage transitions; final stop

Only after corrected files and all seven genuine validators PASS:
1. Commit current canonical corrected and review artifacts to existing branch with normal FF. Create a **new request-only** Git commit for `ADVANCE_STAGE` with exactly all seven names, `expected_from_state=DRAFT_COMPLETE`, launch actual authenticated GitHub Actions Bridge, verify preflight/execute, Stage Checkpoint, State `VALIDATED_DRAFT`, run receipt and remote non-force bot commit;
2. after VALIDATED_DRAFT success build/revalidate and commit one new corrected edition-local `publication/v2/publication-candidate-v2.json` `READY_FOR_PUBLICATION_PREVIEW` binding exact Reader/TeX/Quality/Semantic/Visual/PDF bytes;
3. create a separate request-only commit for `ADVANCE_STAGE`, `expected_from_state=VALIDATED_DRAFT`, **only** `publication-candidate`, launch trusted Bridge, read back Stage `RELEASE_CANDIDATE`, `HUMAN_GATE_REACHED`, preview pending, no freeze or release. Preserve actual request commit IDs, workflow run IDs/preflight/results/bot pushes and hashes. No branch movement during in-flight workflow admission.

Do not open new branches, PRs to main except the exact native officially permitted transport (no new branch), or merge/Freeze/Release. No local CLI fallback or manual State edits. If any trusted boundary unavailable, STOP with actual last-good state and exact blocker; do not manufacture PASS.

## 6. Issue #570 workflow and handoff

Store `sources/2026-W42/execution/issue570-r32/`: Google first-party source verification, old/new two-line diff, Core Gate r2 and request-only/admission receipts (links and IDs), new file hashes, build log, p02–p05 + true spillover page comparisons, raw focused independent delta audit, final acceptance matrix against Issue #570 checkboxes, and a bounded session note; append execution/index.md.

GitHub Issue #570 must retain a traceable link to final artifact/checks when possible, and remain **open** until the Human has had an opportunity to review the new PDF; do not mark `APPROVED` or close on worker assumption. If allowed post a concise factual implementation/evidence comment without implying Human approval. Do not generate a second unrelated Issue.

SUCCESS only on `SOL_W42_R32_ISSUE570_CORRECTED_PREVIEW_READY / RELEASE_CANDIDATE / HUMAN_PREVIEW_PENDING / CORE_V2_FROZEN / NO_FREEZE_NO_RELEASE`.
Final report: exact start/end HEAD/Tree, change list, original vs revised two-locus text, Google source claims, old/new Reader/TeX/PDF SHAs/pages, focused page diffs and independent review, formal check results, 3 trusted workflow run URLs and preflight job results, Gate r2 REQUEST_CHANGES, current Candidate sha and PDF fixed GitHub URL, and Issue #570 acceptance matrix. The NEXT user decision is Human Publication Preview; no pre-approval, Release or Freeze.

If blocked, stop `W42_R32_BLOCKED / LAST_GOOD_STAGE_EXACT / NO_UNAUTHORIZED_WORKAROUND` and report real blocker rather than looping unnecessary Human review requests.
