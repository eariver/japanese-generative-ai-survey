# J-GAS W43 — Sol editorial adjudication: independent Architecture r4 post-fix audit

Status: `ARCHITECTURE_REQUEST_CHANGES / R5_BOUNDED_INTEGRATED_REPAIR_REQUIRED / TRUSTED_BRIDGES_HOLD`
Date: 2026-10-25 JST. Editorial authority: Sol (distinct from read-only independent Sol).
Repository: `eariver/japanese-generative-ai-survey`, existing branch `weekly/2026-W43-v2-work`.
Independent fixed subject: `ee206400c9740dd2288b894f31f79a119b7758bc`, Root Tree `49f55eef6e8fc5beacc1645b62ba0d25e42ccb1d`.
Independent report originally named `20261025180802_SolReview.md`: received attachment 19,491 raw bytes, SHA-256 `2a4b54078e6da63d5b03d25f7c2e67d5ae2f5880c82b40d6f17d219b061c21f2`; UTF-8 BOM + CRLF. Repository copy `sources/2026-W43/execution/audits/independent-sol-w43-architecture-r4-postfix-review-result-20261025.md` is text-normalized and **NOT byte-identical**; preserve separate provenance.
Independent reviewer itself marked target Tree NOT_VERIFIED; editorial Sol independently fetched GitHub Git commit API and verified exact fixed target root Tree `49f55eef6e8fc5beacc1645b62ba0d25e42ccb1d`, current work `92396ac93f1b60fe5eace7c02f64b2bf9a1798cd` / Tree `27cabe57cb432b58f466c7be871c8505c24e625b`, main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`, frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. This editorial check does not retroactively convert independent NOT_VERIFIED into independent PASS.

## Binding verdict

- Selection: **PASS_WITH_LIMITATIONS**; r3/r4 32 selection assignments byte-identical; 19 SELECTED / 1 HOLD / 12 REJECT; 19/19 unique placements in 8 packages, 31 required sections; 68/68 Attention plus separate selected-19 risk register. These are structural/provenance facts, not proof every primary source was independently re-read.
- Architecture: **REQUEST_CHANGES**. Earlier ISA-001/003/005/006/008/009 PASS; ISA-002 appropriately explicit UNRESOLVED vendor conflict, ISA-004 vendor-only LIMITED, ISA-007 page estimate LIMITED. No claim of independent benchmark reproduction.
- New P0 0, P1 0 (within reviewed scope), P2 three: **R4-010 ACCEPT MUST_FIX**, **R4-011 ACCEPT MUST_FIX**, **R4-012 ACCEPT MUST_FIX**. All three are edition-local Architecture/provenance corrections. The unknown underlying publisher revision must remain reported, never invented away.
- Trusted Selection Bridge: **NO / HOLD** until completed r5 provenance and independent targeted re-check. Trusted Architecture Bridge: **NO / HOLD**. Both Human Gates: PENDING. Neither Core validator report nor this editorial verdict is an Operator receipt or Human approval.

## R4-010 / P2 / runner generated_at later than containing commit: ACCEPT

Observed `sources/2026-W43/orchestration/v2/interactive/selection-architecture-input.json#/runner/generated_at`, corresponding audit and r4 compat have `2026-10-25T12:00:00Z` while real audited commit author+committer timestamp is `2026-10-25T08:40:48Z`. This is a **3h19m12s future offset**. Git commit API confirmed; frozen runner validates presence of the field, not its chronology or semantics.
Repair: inspect real logs / clock / exact contract. Do not fabricate a historical r4 timestamp. Preserve faulty r4 proposal in new immutable edition-local history and mark it superseded, then conduct r5 actual run using an observed, contemporaneously recorded UTC runner invocation timestamp (or clearly documented schema-specific semantic if proven) and independently check first-containing commit chronology. Rebind input/compat/audit/output hashes, preserving Matrix/Selection and native 68 output. Source of time must be logged. If trustworthy provenance impossible, STOP `BLOCKED_R5_RUNNER_PROVENANCE` rather than stamping guessed history.

## R4-011 / P2 / +47 versus +50 Elo: ACCEPT

First-party fal publisher blog `https://fal.ai/blog/introducing-flux-3-max-by-fal` says +47 image-to-video Elo improvement versus FLUX 3; fal publisher product page `https://fal.ai/flux-3-max` and publisher-issued PR `https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html` state FLUX 3 1,089 to FLUX 3 Max 1,139 (**+50**), PR published 2026-10-19 15:46 ET within W43 window. Exact AA historical snapshot/original votes NOT re-collected. Do NOT silently choose +47 or +50 as a universal truth. Either version/source/observation-dated crosswalk in P4 §4.3 and boundaries, or omit unqualified delta. `1,139-1,089=50` must calculate correctly. Mark vendor-reported/AA originally unarchived; separate human preference ratings from fal inference benchmark.

## R4-012 / P2 / keyframes endpoint availability conflict: ACCEPT

fal blog has `keyframes-to-video` link. fal product page FAQ says `Two at launch: text to video and image to video`, last updated there as of 2026-10-18. **Publisher-issued PR from Oct 19 explicitly claims keyframes-to-video availability through unified API**, creating a stronger three-way first-party contradiction than mere link-vs-FAQ. There is no verified W43 historical API-schema/working-call/general-availability proof. P4 §4.1 must distinguish announcement, link, schema, live call, regional general availability and dates; do not assert available/not-available without proof. Explicitly carry `UNRESOLVED_VENDOR_DOC_CONFLICT` for endpoint availability, preserving vendor-attributed Oct19 PR assertion and Oct18 FAQ boundary.

## ISA-004 / new source provenance clarification

fal-issued Oct19 PR explicitly says FLUX 3 Max **10.95 s vs Seedance 2.5 277.80 s**, as distinct from fal blog/product **12.45 s vs 277.80 s**; blog quotes **26.5×/96.2%**, arithmetically incompatible with blog timings. Correct derived ratios: 277.80/10.95≈25.37×; 277.80/12.45≈22.31×; time decrease for the latter ≈95.52%. First-party PR distributed by PRNewswire is publisher-authored source, **not a third-party benchmark**; lack of locally archived original bytes is separate from publisher provenance. Preserve source/observation time/byte type and unknown test apparatus. PR headline “22× faster” is a lower-bound-style statement; do not call it mathematically false without examining the exact intent. No independent latency/Elo reproduction.

## Carry-over constraints

- Authorize **one bounded r5 rework** for three P2 plus coherent P4 speed/source crosswalk and time provenance, **not** wholesale rediscovery, reselection, r4 accepted Evidence rewrite, frozen Core change, or a new branch.
- Exact 6-way HEAD/Tree preflight before Muse writes; r4 proposal immutable snapshot; original r3 archive unchanged; 32/19/1/12 Selection and 19 placements, 8 packages/31 requirements, 68 attention and five LIMITED preserved, unless a genuinely upstream evidence contradiction triggers `SELECTION_REVIEW_REQUIRED` and STOP.
- Preserve current `EVIDENCE_REVIEWED`, Selection/Architecture checkpoints pending and both Human Gates pending. No trusted stage, Issue #448 request, human approval, Draft/TeX/PDF in r5.
- Sol adjudicates completion and invokes separate independent read-only **targeted** r5 repair verification before any Stage. Then authorized Operator must advance Selection and Architecture as separate requests and verify real receipts. Human Architecture Review only after both successful checkpoints; Human Owner alone approves.
