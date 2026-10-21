# J-GAS W42 Muse r19 — read-only reader master, TeX/bibliography-only layout repair and page-plan reconciliation

Date: 2026-10-18 JST
Authority: `SOL_EXECUTION_AUTHORITY / R18_EXTERNAL_REQUEST_CHANGES_ADOPTED / R19_NONCANONICAL_PRINT_ONLY`
Repository `eariver/japanese-generative-ai-survey`
Branch `weekly/2026-W42-v2-work` (already exists; ONLY permitted branch).

## 0. Fail-closed exact repository guard

Sol dispatch gives `Exact Starting Remote HEAD` and `Expected Starting Git Tree` for THIS dispatch commit. Before writes read **remote branch ref, commit object and root Git tree** and require exact equals; verify main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / `801de813319f08777ab1581a5e8875fc1ac5df19`; frozen Core v2 `production/survey-core-v2` HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Independent r18 baseline HEAD/Tree `f3840b4240791b7679c08be33b0db53055d9f878`/`373a68c7945510f0746e79505744db3120e07f58`. If *any* identity missing/mismatch, report exact expected/actual and **ZERO WRITES, STOP**. Repeat remote lease before push.

Never create alternate/fallback/new branches; no force-push/rebase/reset/history rewrite. Normal fast-forward commit / non-force push to existing W42 branch only. After push verify remote HEAD/Tree, new blob read-back, exact changes and protected unchanged.

**Immutable all along:** main, Frozen Core v2, shared roots, W42 canonical Discovery/Evidence/Selection/Architecture, Human r1 architecture approval, canonical Draft v10.0/Synthesis, Production State, Gates, checkpoints, and ALL r11–r18 historical execution files. Write ONLY NEW `sources/2026-W42/execution/typeset-repair-r19/`, `execution/diagnostic-r19/`, `execution/sessions/`, and append-only `execution/index.md`. NO formally approved Reader/Publication Preview or authority change.

## 1. Read authority and hard source boundary

1. Sol ruling `sources/2026-W42/execution/reviews/sol-w42-r18-independent-reader-layout-audit-disposition-20261018.md`, r19 contract, r18 Muse session/closure/validation, r16/r17 independent dispositions, r18 Human page-plan proposed brief.
2. **Source of truth for reader bytes:** EXACT `sources/2026-W42/execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` + seven r18 proposed Draft results, r18 bibliography map, duplicate matrix, and citation ledger. Confirm 7 chapters, 136 PARAGRAPH / 25,015 paragraph chars, 7 TABLE, 7 NOTE, 7 HEADING, 157 reader blocks, 90 bibliography keys/19 aliases/177 ledger rows. Compute and record SHA256/source Git blobs. **Do NOT edit/copy/rewrite r18 Reader or seven paragraph proposal texts in r19.** The technical content and claims are settled for this print-only unit.
3. r18 diagnostic TeX/style/log/manifest/PDF, all 21 individually rendered PNGs (esp. p1,p16–21), split contact sheets as source of prior rendering failure. Audit `reader-preview-r18.PROPOSED.md` as a wrapper to **exclude** editor-only `CLAIM_BOUNDARY/PROPOSED` header from print.
4. Approved `sources/2026-W42/architecture-v2.json`, Human Architecture r1 basis and gate records read-only: 7 packages/28 selected, approved body26.5, issue target28/max30, `DRAFT_COMPLETE`, Human Architecture approved and Publication pending.
5. External r18 original `20261018180741_SolReview.md` was supplied to Sol outside repository; only Sol's disposition is in repo, never claim external raw file was present or separately checked by Muse.

## 2. Unit A — fully fix sentence-break Table 7 layout (HIGH)

r18 **actual** p16 right-column tail: `ElorianのGlimpseは、視覚的作業空間（高密度`; p17 top `table*[htbp]` Table 7; p17 under table continuing same sentence `の再走査・ズーム・追跡...`. The previous claim "t7-04 paragraph complete" missed the *other* Glimpse paragraph. This is a visual FAIL although table is no longer alone.

Implement a body-byte-preserving placement that keeps all P7 paragraph(s) **continuous across reader flow without unrelated Table 7 inserted inside a sentence**. Source JSON order stays unchanged. Evaluate at least 2 genuinely rendered print-only alternatives if necessary: place comparison after a complete relevant introduction before the Glimpse paragraph, or use safe two-column full-width placement / barriers or fixed nonfloat insert at a completed boundary. Do not insert or delete sentences to hide the issue. Page transitions between paragraphs are allowed; inserting Table 7 between two halves of **one paragraph** is not. Preserve all 7 tables/captions/cites, relevance to P7, and no table-only page/no cross-chapter float. Compare p15→p17 render and **read actual p16 end and next page first paragraphs** before marking PASS.

## 3. Unit B — bibliography print-only renderer, preserve all source identities (HIGH)

Preserve r18 **90 canonical/alias Bxx keys**, 19 `alias_of` pairs, URL syntax, 177 ledger rows and source certainty. No changes to source evidence/rights/data and no invented titles/author metadata. Author `typeset-repair-r19/bibliography-display-map-r19.json` and `bibliography-display-policy-r19.md` from immutable r18 map; trace each Bxx logical key to displayed reference and original URL, including direct/alias and primary/vendor/secondary/independent class.

**B28 p18→p19**: `https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein` ended `...-k` on p18 and left `lein` alone atop p19. Format entry as robust readable unit, using appropriate `\needspace`, no-break of short tail, keep-together or local group with caution. Preserve all citations. Check B57 `https://github.com/NVlabs/ASPIRE` old orphan `RE` stays fixed and check **all 90 entries** for page-top stray URL fragments, empty link lines and orphan abbreviations after reflow. No font shrink or excessive forced whitespace.

**Machine editorial provenance must NOT appear in Reader bibliography**: remove from *print only* texts like `alias-of`, `www/trailing-slash normalization`, `identical source snapshot`, prior r17 reclassification, `see ledger` and raw trial notes. For genuine duplicate Bxx, print simply `[B72] → [B20]（同一資料）` (with accurate original publisher kind as needed), while mapping stays intact. Keep source-significance where relevant: B88 OpenRouter is aggregator, **not independent repeat**; concise Japanese note appropriate. Ensure display distinguishes source kind clearly, does not require reader to parse developer metadata, does not duplicate 19 full URLs or discard Bxx lookup targets. 90 entries may render shorter, affecting bibliography length: **recalculate actual pagination**. Include compile/static scan over TeX **bibliography printing strings AND extracted PDF text**, excluding provenance only in JSON sidecar, ensure 0 unwanted machine phrases.

## 4. Unit C — diagnostic stamp full-width/single-flow, not broken (HIGH)

Prior p21 diagnostic footer flows as post-bibliography ordinary two-column text: left bottom `NOT FOR HUMAN`, right top `APPROVAL —`. p1 cover also wraps `AP-/PROVAL`. Keep visible **NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL** in diagnostic PDF, but render as unbreakable appropriate cover block/footer/page decoration or separate full-width element outside body flow. Do not merely remove authority warning or suppress it; do not put any diagnostic stamp into canonical Reader or Reader text. All banner words **visually contiguous**; inspect p1, last page, and remaining pages after build. Prefer compact Japanese additional description if it reduces possible English word wrapping while preserving precise prohibition; no styling tricks to reach page count.

## 5. Unit D — robust full PDF visual QA from r18 unchanged Reader

Build genuinely new `execution/diagnostic-r19/` in temp from r18 Reader content **byte-identical on every HEADING/PARAGRAPH/TABLE/NOTE**, with r19 print-only display transformations and bibliographic formatting. Source/readout hashes and textual equivalence checks mandatory. Source of truth is r18 JSON, never stale r17/r18 TeX pretending to be r19 content.

Archive diagnostic proof: `main.tex`, `preview.sty`, `main.pdf`, full `main.log`, manifest exact PDF SHA256/bytes/pages, TeX SHA256, command/fonts/packages/version, missing CJK/overfull/underfull/errors/warnings, **all individual PNGs**, split 2–3 small contact sheets, page index. Actually open **every page** rather than "same page text" substituting for visual inspection: reflow can move objects even when text byte-identical. Validate all 7 tables and 7 notes in correct chapters, no float sentence interruptions, no large blank pages, no orphan URL fragments, chapter starts and close, no split warning stamp, links and book references legible. If one of F-01–04 persists, report explicit `R19_PRINT_SURFACE_BLOCKED` — do NOT self-approve.

No formal Reader/Publication pipeline or Human candidate. Diagnostic stamp visible and noted. **No white-space fillers, forced 28 pages, unrelated matter, layout shrinking, fake citations**.

## 6. Unit E — measured page-plan decision brief correction (MEDIUM)

Only AFTER successful r19 diagnostic measured page split, create `typeset-repair-r19/human-architecture-pageplan-decision-brief-r19.PROPOSED.md`, in independent auditable terms:
- APPROVED architecture remains 7 chapter/28 selected, body-plan **26.5**, target **28**, maximum **30**, Human r1 `approved`; never edit it.
- MEASURED r18 historical **21 total = cover1 + body physical16 + bibliography4**, and actual NEW r19 total/physical body/cover/bibliography (may change after alias display clean-up).
- EFFECTIVE PAGE AREA: use only a defined measured equivalent `occupied article area / actual usable page area` bounded `0..N physical body pages`, with table+notes+heading allocation and no double counting, exact computation and uncertainties. If no credible independent area measurement method available, write `UNMEASURED; <= N PHYSICAL BODY PAGES`; **withdraw** r16/r17/r18 undefined `15.5–17`. Never present 17 as observed physical 16.
- Re-locate P1..P7 headings by real r19 pages **AND columns** after reflow (r18 P4 p9-right→p11-left, P5 p11-right start, P6 p13-right start, etc. are historical checks only). Since two chapters share same page, overlapping page intervals are NOT additive.
- CONDITIONAL HYPOTHETICAL of retaining 26.5 body-plan with measured r19 nonbody pages: `26.5 + actual_cover + actual_bib` versus approved target28/max30; label this as not actually rendered. The r18 cover1+bib4 historical gives31.5; do not hardcode it to r19.
- PROPOSAL Option B only: 7 chapters P1 2.5/P2 2.5/P3 3/P4 2.5/P5 2/P6 2.5/P7 2 = **17.0 planned**; don't equate with actual article body consumed. Compare Option A retain/needs new evidence, B provisional source-grounded reallocation, C structural redesign only if warranted. Preserve all 28/7 and technical qualifications; no padding or extraneous magazine filler.
- GATE PROCEDURE: Current lifecycle `DRAFT_COMPLETE`, Architecture Human approved and Publication pending. Frozen Core human-gate CLI requires suitable pending gate/review lifecycle. Do not assert that `record_architecture_approval r2` or `request_architecture_revision` can run now. Clearly split **Human editorial preference consultation** (could occur now without changing repository) from **future actual authorized workflow** (separate read-only investigation, explicit scope, Core compliant state transition, Human authority). No writes to gates/review index/state.
- Data/table arithmetic independently verify. Brief is `PROPOSED / NO_HUMAN_VOTE`; Sol vetting + external focused audit needed before publication/approval.

## 7. Exact terminal conditions

Deliver new `typeset-repair-r19/finding-closure-matrix-r19.md` for F-01…F-07 with old/new physical observations and clear PASS/FAIL/UNVERIFIED. `bibliography-display-map-r19.json`, display-policy, evidence master/hash receipt, page-plan brief, layout alternatives and QA notes; `diagnostic-r19/` full PDF/log/PNGs/index; `execution/sessions/muse-w42-r19-20261018.md`, append-only index.

Verify all r18 **content** remains byte-exact and all 90/19/177 source structures untouched, preserve negative results, license scope, cutoff, 7 reader chapter roles. Production State/Gates/canonical/Architecture/Core/main unchanged and all r11–r18 bytes untouched. Re-run frozen Draft/Synthesis validators on **r18 proposal bytes only if practical as read-only verification**; do not modify the master or claim new r19 content validator acceptance from print changes. Run custom PDF text/print leakage QA separately.

No blanket self-attestation. Stop `SOL_W42_R19_PRINT_AND_PAGEPLAN_AUDIT_READY / NONCANONICAL` **only if F-01–F-05 all resolved or strictly measured residual uncertainties documented for page area**, otherwise `R19_PRINT_SURFACE_BLOCKED` and why. Do not seek/perform Human approval, formal Reader/Publication/Freeze/Release. Human Architecture preference consult only after Sol editorial evaluation and focused independent audit.