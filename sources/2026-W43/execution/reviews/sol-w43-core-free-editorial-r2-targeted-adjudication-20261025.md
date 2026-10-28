# J-GAS W43 — Sol targeted r2 Core-free Japanese Draft editorial adjudication

Status: `R2_STRUCTURAL_PASS / EDITORIAL_REVISION_REQUIRED / NATIVE_DRAFT_UNVALIDATED / NO_ARCHITECTURE_REVISION`
Date: 2026-10-25 JST.
Repository `eariver/japanese-generative-ai-survey`, existing branch `weekly/2026-W43-v2-work`.
Review target Muse r2 commit `a74e0e9537813b12b803fc133a727b064876118c` / Tree `f60b35fb9a7c1500d3eb8dcf245ba1cafb51d0f1`.
Prewrite six-way remote guard work/main/frozen exact PASS; protected reviewed main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`; frozen `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## Confirmed

- Exactly one fast-forward normal Muse commit (direct parent prior instruction `79f26a8bf15d7afd408c1b1ed9d6fe9ca8f2ccf1`) and five edition-local changes: r2 preview, r2 86-row ledger, editorial QA, Muse session log, index. No shared Core, State, Architecture, Selection, Evidence, approved Gates, TeX/PDF.
- 8 P1–P8 chapters with 113 original blocks; 62 prose paragraphs, 15 text-delimited tables, 8 notes, 28 headings; 5-paragraph standalone closing `今週の総括` after P8 and before sources. Human Architecture r1 approved and unchanged; machine Draft checkpoint pending.
- Ledger 86 rows = 62 Paragraph + 15 Table + 8 Note + 1 summary. Of those 73 entries severity none, 7 P1 and 6 P2 with `r2_status=FIXED`. One suggestion declined as unsupported license version. Confidence breakdown by direct GitHub JSON recount: `VERIFIED_DIRECT=16; SOURCE_REPORTED=56; LIMITED=8; UNRESOLVED=4; SOURCE_NOT_VERIFIED=2`. This **does not** mean 86 independently reproduced facts. 13 ledger `best_url` null (some are commentary or intentionally unavailable; distinguish from factual assertion needing source).
- 31/31 mapped Architecture must-cover requirements, 19/19 placements and 5 LIMITED caveats carried; Review Attention inherited 68/68 from earlier Architecture (not regenerated). No unselected story promotion detected.
- 13 textual changes from r1 to r2, including correction of Kimi/Flint context attribution, Flint vs Nemotron licenses, Voxtral date-only and language '50超', and P7 model comparator disambiguation. Sol compared r1/r2 line level and opened QA/ledger; no independent reproduction of all 86-source original fetches is claimed.
- Full independent r5 Architecture audit plus r6 corrections remain authoritative for architecture; r2 local Muse 4-way editorial review is not a second independent end-to-end source audit.

## Binding follow-up findings (edition-local; NOT Human Architecture REQUEST_CHANGES)

**R2-SOL-01 P2 SOURCE AUTHORITY / stale labels.** Ledger rows `p1-t2`, `p1-p10` remain `SOURCE_NOT_VERIFIED` despite `r2_status=FIXED`. Sol directly read archived first-party:
- `sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/flint-card-README.md`: explicit **~2.2B active body** (active incl output head, excludes input embedding), explicit **262,144-token documented context configuration**, Apache 2.0 weight license.
- `sources/2026-W43/collectors/primary/runs/20261024T133000Z-muse-r4/raw/recursive-flint-announce-20261024T132900Z.html`: explicit published prose "Flint supports context windows of up to **512k** tokens. For the best results ... recommend staying within **256k** tokens." 
These are TWO DIFFERENT LAYERS: announcement-supported capacity 512k, recommended 256k, model-card configured 262,144 tokens. A source for the *published claim* exists in frozen primary archive; neither supports independent 512k measured quality. Update ledger to cite both exact archived paths + proper primary publisher URL `https://recursive.com/updates/introducing-recursive-flint`, `https://huggingface.co/RecursiveSI/flint`, distinguish literal original document strings from accepted Evidence Card summary omissions, and change confidence to `SOURCE_REPORTED` where justified. Do not misrepresent model card as source of announcement 512k. Source content of all three claims is supported; **the stale ledger code is a citation/traceability issue**, not a reason to rewrite approved Architecture.

**R2-SOL-02 P2 MIXED-ORIGIN TABLES / attribution.** At least `p1-t2` and `p1-t4` contain multiple models but have only ONE ledger `best_url`; one link cannot prove all rows. Extend edition-local ledger with per-row/per-claim original-source references (Kimi, Flint, Nemotron individually) and distinguish publisher reported from independently reproduced; do similar for cross-product tables P3/P5/P7/P8. 13 `best_url=null` rows include derived/limited/review notes: classify legitimate no-source synthesis, or provide real relevant provenance for claims. No invented URL or fake `VERIFIED_DIRECT`.

**R2-SOL-03 P2 TECHNICAL DEPTH / repetition.** r2 is roughly 22.2k characters + 15 raw tables for an intended 35-page body. QA acknowledges the manuscript is thin, but says missing page depth may be absorbed by figures, bibliography and index; **that is not a substitute for technical narrative depth**, especially P2 / P5 / P6 / P7 / P8. R1 chapter text counts (r2 largely unchanged): P2 ~3944 for 6pp, P5 ~2740 for 4.5pp, P6 ~1712 for 4pp, P7 ~2230 for 4.5pp, P8 ~2908 for 3.5pp. Some follow-up paragraphs restate methodological caveats already given rather than provide new technical mechanism, concrete configurations, compared baselines, evaluation design or causal interpretation. Deepen ONLY where archived first-party Evidence supports, remove repeated paragraphs and add substance instead; not quotas/filler and no source discovery outside approved boundary. In particular P6/P7 cannot be declared 4–4.5pp of substantive explanation based solely on page furniture.

**R2-SOL-04 P3 QA arithmetic / table formatting.** QA says `TABLE_OK 13` but explicitly names 12 clean tables + 3 repaired = 15; correct count/title. All 15 are still code-fenced delimiter-separated text, not reader-ready tables. Mark layout/methodology needed for eventual renderer, do not call table layout validated.

**R2-SOL-05 P2 READER CONCLUSION INTEGRATION.** Keep full 5-paragraph `今週の総括` after P8, not P9. The afterword currently retains an "編集注記（本文採用時には削除・別掲）"; make next clean reader preview separate any operator-only meta from the publication-facing conclusion. Source-backed high-level analysis only, no new W44 releases.

## Editorial verdict / production boundary

**R2 is accepted as an edition-local reviewable *working draft*; NOT approved as final reader manuscript and NOT native validated.** The 13 original Muse findings appear textually corrected, but citation audit normalization and genuine substance still require r3. This is a bounded manuscript revision, not Architecture reconsideration, no selection change, no Core repair, no Human gate update.

Produce a new **r3 edition-local** reader preview, per-claim citation ledger and editorial QA with stable source crosswalk, plus safe publication-looking tables where evidence supports. Then independent editorial Sol reviews r3. TeX/PDF and human Publication Preview shall not advance until separate Sol decision and explicit truthfully governed bypass path; machine `DRAFT_COMPLETE` remains pending. No work here claims legal Core Stage PASS or grants release authority.
