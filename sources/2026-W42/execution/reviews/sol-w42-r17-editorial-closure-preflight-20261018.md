# W42 r17 — Sol editorial closure preflight and short bounded correction

Date: 2026-10-18 JST
Status: `SOL_EDITORIAL_PREFLIGHT / R17_MUSE_COMPLETE / R18_TARGETED_FIX_REQUIRED / NO_PUBLICATION_AUTHORITY`
This is a **Sol read-only examination**, NOT an independent external r17 audit and not a Human Architecture decision.

## 1. Verified current repository identity

Repository `eariver/japanese-generative-ai-survey`; existing branch `weekly/2026-W42-v2-work`; r17 HEAD `8509ee3354cc2b4e83abe5b230b8733485676320`, direct Git Data Tree `87ba200f48d791cc24a465b752c7a55222b28c92`. Parent Sol r17 dispatch `6f434325abdf2f26d7cc7a54200a06b159423437`. Main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`; frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`. Latest canonical `production-state.json` blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`: `DRAFT_COMPLETE`, Human architecture approved, publication pending.
1 commit/54 changed files since r17 Sol dispatch, **all within W42 `execution/`**; r16 older bytes retained per Muse.
Current r17 reports 136 paragraphs, 25,085 paragraph-only chars; frozen draft-check 7/7 PASS and synthesis-check PASS, 90 bibliography keys and 177 ledger rows. `diagnostic-r17/main.log` actual output 21 pages, 512,182 bytes, no over/underfull/missing-character/undefined-control warnings seen by Sol. Muse manifest PDF SHA256 `6b673a9329ec02d41cf22f6a6a634a315d8d5ad480f6d7274c5f5c7b4ffb5b8e`; Sol has **not independently reconstructed the PDF binary digest**. Actual GitHub PNG p17 fetched and visually opened by Sol; table 7 now appears on p17 with P7 text below, not isolated on p18. The other 20 PNGs not yet independently viewed by Sol. Split contact sheets exist but no independent full review certified.

## 2. What r17 repaired (credit, without self-certification)

- P2 Maia corrected `96ポッド` to 96 accelerators in one rack/pod, repaired 750 GB/s bandwidth unit.
- P2 LFM legal-entity annual revenue/qualified §5(c), hosting distribution semantics; P1 4 player agents + Observer + random generated seed terminology.
- P6 & P7 numeric repetitions reduced; 90/90 bibliography URL parser validity and 19 alias mappings confirmed by Sol independent string inspection; B74 now pure `https://github.com/OpenBMB/MiniCPM-V`.
- r16 p18 single-table orphan removed. r17 diagnostic remains **21 total pages**, now **cover1 + body p2–p17 (16 physical) + bibliography p18–p21 (4)**, with article effective ~15.5–17 *estimated by Muse*, and 26.5 planned substantive-body pages not met.
- All r17 artifacts NONCANONICAL. No formal Reader, Publication, human gate, freeze or release authority exists.

## 3. NEW reader-surface finding (Sol directly verified)

**S17-01 / MAJOR READER SURFACE: editorial-machine block IDs leaked into published prose**. Directly present in r17 `reader-preview-r17.PROPOSED.json`, all 7 per-chapter proposal source and `diagnostic-r17/main.tex`:
- P1 `t1-23`: `失敗の内訳はt1-16に集約し、ここでは…`. Actual TeX line ~82.
- P6 `t6-08`: `（開放問の数値はt6-06に集約しここでは繰り返さない）`. Actual TeX line ~607.
- P7 `t7-19`: `（t7-07の数値行はここでは繰り返さない）`. Actual TeX line ~739; **the text is visibly printed** on p17 PNG inspected by Sol.
These are **NOT reader prose**; they are internal editing notes and references to block IDs. They were introduced while de-duplicating r16. Frozen draft-check and no-CLAIM_BOUNDARY scans failed to catch them. Every reader-facing HEADING, PARAGRAPH, TABLE, NOTE, headline/deck and TeX text should receive internal-ID/notices leak checks. Editors should explain findings in natural Japanese, not mention block IDs or process notes. Do not simply remove analytical negative evidence.

**S17-02 / MAJOR HUMAN DECISION DATA: arithmetic of nonbody pages**. The newly PROPOSED `human-architecture-pageplan-decision-brief-r17.PROPOSED.md` says r17 cover **1 page**, bibliography **4 pages**, while computing `26.5+4=30.5` to compare against magazine max30. Correct comparison, **IF approved 26.5 body pages and observed r17 bibliography+cover layout persisted**, is `26.5+1+4=31.5` total physical pages. Note: the approved architecture's own estimate of nonbody 1–2 pages differed and cannot be retroactively changed; its official max30 and target28 remain unchanged. Correct all r17-derived, newly written page briefs and comparisons before Human sees them. Distinguish observed physical, effective area, and a conditional extrapolation, not a real 31.5-page generated PDF.

**S17-03 / MINOR VISUAL / FLOW**: independent p17 PNG shows Table 7 at page top with running prose below beginning in the middle of a sentence carried from p16. Orphan page eliminated but natural introduction-to-table placement should be checked. r17 review notes B57 two-character `ASPI/RE` reference URL carry across bibliography page boundary. Improve if feasible without padding, reducing font or distorting citations; otherwise report reason and leave as limitation.

**S17-04 / EDITORIAL DECISION BOUNDARY**: r17 proposed page plan Option B 7 chapter allocations sum 17.0 (valid: 2.5+2.5+3+2.5+2+2.5+2 =17), but neither Sol nor Muse may approve that. Keep 7 chapters, 28 selection, 26.5 approved planned body, target28/max30 until independent closure + Human decision. The proposed optional suggestion to fill a magazine signature with unrelated editorial/advertising matter is NOT an approved method of reaching the approved technical depth. Human review should compare substantive-reader sufficiency and evidence limits directly, not paper over a gap. The precise frozen Core legal path for amendment after Human r1 approval is not yet verified; research it **read-only** before promising an automated re-gating operation.

## 4. Sol decision and next boundary

r17 completed its bounded execution but **NOT editorial closure / NOT ready for Human page-plan decision** because S17-01 and S17-02 are objective defects. Do not send it to a new independent PASS audit while these are known open. Delegate **one short r18 focused correction**, preserving all r17 history and technical source readings; re-render noncanonical from corrected reader, recheck exact text and visual surface, update proposed Human brief with correct arithmetic, stop for a short independent **r18 closure audit**, then Sol will prepare Human decision options. No broad research, page padding or architecture manipulation.

r18 contract: `sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r18-reader-surface-leak-and-pageplan-arithmetic-repair.md`.
