# J-GAS W42 r24 — Sol independent-of-Worker visual disposition

Date: 2026-10-18 JST
Status: `SOL_DIRECT_VISUAL_PREFLIGHT / R24_LAYOUT_QUALITY_BLOCKED_CONFIRMED / REQUEST_CHANGES / R25_PRINT_SYSTEM_FEASIBILITY`
Read-only inspected HEAD: `7e0b0b8eebb778225ef43eabab974260841d1257`
Root tree: `34b32ea4aa2ef3472be39d65ceebf362873d9d2c`

## 1. Identity, authority and positive findings

GitHub checked W42 branch head/tree above, exactly one normal fast-forward r24 commit from `c86aa1032bd361f20859d270a3e325e610a0746b`. Diff remains under edition-local execution paths and append-only index; main and Frozen Core branch heads unchanged. Production remains DRAFT_COMPLETE, Human Architecture r1 APPROVED, Publication Preview pending. NO Gate/Publication/Freeze/Release action or approval.

Worker's `R24_LAYOUT_QUALITY_BLOCKED` is ACCEPTED. This is not `R24_INFLOW_FEASIBILITY_BLOCKED`: the Phase A `cuted v2.10` + `capt-of` compatibility demonstration compiled and produced two in-flow tables in a two-column sample; warning-free or W42 complete compatibility was NOT established. Selected r24 full issue is 21pp, cover1+physical body17+bibliography3, diagnostic-only, PDF SHA256 `8dea62f2b1d33168e44ed55709851cd77ef6a4659ca9faad2f876`, TeX `7ba80abf091c6ba73cf7ccb7eb1371b02a67e07bca44c1aa00cb02cfa4c2c702`. Reader r18 master `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` remains source authority: 7 chapters/28 topics/136 paragraphs/7 table objects/7 notes/90 B-keys,19 aliases,177 citation rows.

The important positive result: rendering tables in source-order with `strip` means the four historical top-of-page `table*` float interpositions at Tables 1/2/3/6 no longer occur in the inspected r24 print. This validates the DIRECTION, not the full implementation.

## 2. Sol directly inspected published PNGs, NOT merely Muse log

Opened individual actual fixed-commit pages: p03, p05, p08, p09, p11, p12, p13, p15, p16, p17, p18. The following are directly witnessed hard print defects; the Sol note does NOT claim all 21 pages were independently opened.

| Finding | Severity | Precise physical proof |
|---|---|---|
| F24-01 | BLOCKER | p11 in-flow Table 4 `比較表：生産性とゲートの条件` runs into bottom/footer/page number: Decider v1.2 row cut off; 93pt vertical overfull. Row present in TeX but absent in displayed full PDF. This is content loss in publication surface, not merely a LaTeX warning. |
| F24-02 | HIGH | p08 has Table 3 `比較表：重み・実装・ライセンス` CAPTION ALONE at the bottom of the page, with all table rows deferred to p09 TOP. The caption/body are separated by the page break. The r24 QA misclassified Table3 as an in-flow placement PASS and did not record this physical caption orphan. |
| F24-03 | MAJOR | p18 contains 508 pdftotext raw characters in a short upper-left fragment, right column empty, bulk of entire page blank; even worse than r22 C2 p18 702. An alternate Table7 anchor reportedly yields just 405 characters. |
| F24-04 | MAJOR | The r24 full-issue `cuted` output routine logs `twocolumn too tall`, `Text page contains only floats`, and large overfull vboxes (including 37pt on p03). Warning semantics must be tied to visual geometry, not dismissed. The p08 caption orphan + p11 footer collision corroborate a real instability. |

Table1 p03 and Table2 p05 were visibly in-flow; Table3 text row material is present on p09 but split from its caption p08; Table6 p15 and Table7 p16 appeared in-flow and without old prose interruption. No assertion that these observations alone are final all-page PASS. r24 full candidate rejected.

## 3. Editorial disposition and next limited unit

Decision: `REQUEST_CHANGES / R24_PRINT_NOT_APPROVED`. No formal Architecture/Gate/Reader/Publication. r24 result remains useful as experimental evidence. Preserve r18 Reader bytes, 7 chapter/28 topic content, table cells/captions/citations unchanged. Avoid the false dichotomy "float only" versus "impossible": next work is a **two-track compatibility/pagination-safe proof**, not another one-off `needspace` patch.

Track A: `cuted` strip with measured full-table height incl caption/rows and conservative preflight before near-page-bottom insertion. Explicitly forbid split caption/body (Table3), clipped rows/footer overlap (Table4), missing glyphs, and extreme voids. If the `cuted` output routine cannot make a whole strip indivisible within a page, this track is disqualified.

Track B: alternative segmentation using documented `multicol` / `multicols*` for the still-two-column body in page-flow segments, with nonfloating full-width table placed between two-column segments; test a realistic multi-table sample and all chapter/table boundaries. The LaTeX `multicol` output routine differs, so compatibility is NOT presumed. If necessary, document a third proven alternative, but prohibit silent all-one-column layout.

External references for the feasibility hypothesis, NOT proof it works in W42:
- CTAN multicol: https://ctan.org/pkg/multicol
- TeX FAQ about two-column last-page balance: https://texfaq.org/FAQ-balance
- CTAN cuted: https://www.ctan.org/pkg/cuted

Failure to find one full-issue method without truncation/voids => documented BLOCKED with rendered proof. Next execution instruction: `sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r25-pagination-safe-wide-table-system-feasibility.md`.
