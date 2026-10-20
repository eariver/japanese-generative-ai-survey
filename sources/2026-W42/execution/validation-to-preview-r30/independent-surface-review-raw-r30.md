# Raw independent semantic surface review — persisted verbatim (r30)

Provenance: separate review subagent (Sol review role; not the r30 build worker), read-only, 2026-10-20 JST.
The r30 worker did not author, edit, or selective-quote this report; the checks JSON below is transcribed exactly as returned (only embedded here as the raw record; the formal `reader-surface-semantic-review-v2.json` derives `checks`/`findings`/`decision` from it with mechanical digest + surface binding).
Original attachment boundary markers preserved.

RAW_SEMANTIC_SURFACE_REPORT_BEGIN
# J-GAS Weekly 2026-W42 — Independent Semantic Surface Review (Sol review role, read-only)

- review_target_tex: surveys/weekly/2026-W42/main.tex
- tex_sha256_expected: 2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3
- tex_sha256_observed: 2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3
- tex_sha_match: MATCH — independently computed with sha256sum on 2026-10-20T00:13:39Z; review proceeds.
- pdf_reference: surveys/weekly/2026-W42/main.pdf
- pdf_sha256_expected: 8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9
- pdf_sha256_observed: 8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9
- pdf_match: MATCH (reference only; not the review verdict basis)
- method: read-only; TeX bytes read directly; substring/count checks executed by reviewer; r18 JSON parsed for spot-checks; architecture-v2.json and reader-manuscript-v2.json read as navigation only, placement re-verified in TeX; L02/L03/L04 worker reports treated as provenance, not verdict.

```json
[
  {
    "check_id": "READER_PIPELINE_INDEPENDENCE",
    "status": "PASS",
    "detail": "I stripped TeX comment lines and scanned rendered prose for pipeline leakage myself. No DRAFT_COMPLETE, candidate:, Evidence Card, Screening, HOLD_OUT, sources/2026-W42, TODO/FIXME, APPROVED, RELEASED, or r18/r26/r29/GATE tokens appear in rendered text. The only two substring hits (sources/ inside a dev.meta.ai blog URL, architecture inside a maia-300-architecture URL) are parts of public URLs, not internal paths. Provenance notes mentioning r18/r26/r29 exist only in TeX % comments, which are not reader-visible; I checked them separately and they do not leak into print.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 1", "surveys/weekly/2026-W42/main.tex: Section 2", "surveys/weekly/2026-W42/main.tex: bibliography B02/B09 URLs", "surveys/weekly/2026-W42/main.tex: % comment lines 1-3"]
  },
  {
    "check_id": "R18_INTEGRITY_EXACT_SURFACE",
    "status": "PASS",
    "detail": "I parsed reader-preview-r18.PROPOSED.json myself and substring-tested three body passages I chose (t1-02 P1 lead, t2-04 Maia vendor-only paragraph, t7-02 GLM-Legal anchor paragraph): all three are verbatim present in the TeX. I also verified two table cells I chose (T2 LFM license-cap cell and T3 Nemotron OpenMDW cell) are verbatim present. Cover headline and deck strings are preserved and no diagnostic stamp or APPROVED/RELEASED claim renders. I did not re-run the full 150-block containment proof; that full-count provenance comes from the archived r29 report, which I cite only as provenance.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 1 (t1-02)", "surveys/weekly/2026-W42/main.tex: Section 2 (t2-04)", "surveys/weekly/2026-W42/main.tex: Section 7 (t7-02)", "surveys/weekly/2026-W42/main.tex: Table T2", "surveys/weekly/2026-W42/main.tex: Table T3", "surveys/weekly/2026-W42/main.tex: cover lines 10-13"]
  },
  {
    "check_id": "ARCHITECTURE_AND_READER_COVERAGE",
    "status": "PASS",
    "detail": "I located genuine prose for at least one must-cover requirement per package in Sections 1-7 myself, rather than copying the manifest FULFILLED labels. P1 Minecraft limits, P2 Maia mechanisms plus vendor-only deltas plus LFM non-comparability, P3 architecture table plus Beam full-file versus tag-only distinction plus Nemotron vendor attribution, P4 single-team Codex plus Scion non-replacement boundary plus Decider chain, P5 four categories plus vendor-measured distillation plus METR mechanism-only, P6 wet-lab denominators with MSA caveat plus failure-inclusive Earth AI cost plus June-background Deep Review, and P7 Vals anchor plus ASPIRE background split plus Glimpse HSS shortfall are each present where claimed. No package is missing its chapter home.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 1", "surveys/weekly/2026-W42/main.tex: Section 2", "surveys/weekly/2026-W42/main.tex: Section 3 + Table T3", "surveys/weekly/2026-W42/main.tex: Section 4 + Table T4", "surveys/weekly/2026-W42/main.tex: Section 5 + Table T5", "surveys/weekly/2026-W42/main.tex: Section 6 + Table T6", "surveys/weekly/2026-W42/main.tex: Section 7 + Table T7"]
  },
  {
    "check_id": "BIBLIOGRAPHY_AND_R18_BODY_INVARIANCE",
    "status": "PASS",
    "detail": "By direct regex count I verified 90 bibitems B01-B90 with zero missing and zero extra, 169 \\cite occurrences expanding to 90 unique keys with zero unregistered cites and zero uncited bibs, 71 \\url entries, 17 Japanese secondary-reference markers, and zero untranslated [SECONDARY] strings. Alias/duplicate-matrix and full URL-liveness re-verification were beyond what I could do by reading alone; the only live-source facts I rely on are the worker L02 fetches for B16/B54/B57, which I treat as disclosed worker evidence with the PARTIAL drifts recorded separately.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: bibliography B01-B90", "surveys/weekly/2026-W42/main.tex: B16", "surveys/weekly/2026-W42/main.tex: B54", "surveys/weekly/2026-W42/main.tex: B57"]
  },
  {
    "check_id": "CLAIM_EVIDENCE_SEMANTIC_BOUNDARIES",
    "status": "PASS",
    "detail": "Vendor-attribution discipline is present throughout the prose I read: performance numbers are framed as publisher measurement, pending reports (Wonder safety report, third-party guarantees) are marked unissued, and X posts are announcement-only. B16 reads as full-LICENSE-file confirmed with standard Apache conditions retained, consistent with L02 CONFIRMED. B54 and B57 retain their caveats in prose but are affected by the L02 PARTIAL drifts (79-vs-81 denominator and 72-min latency; October day-precision on month-only evidence), which I record as open WARNING findings rather than silent passes.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 1 (Wonder pending report, Vals citation boundary)", "surveys/weekly/2026-W42/main.tex: Section 3 (B16 Beam prose)", "surveys/weekly/2026-W42/main.tex: Section 7 (B54 Vals prose)", "surveys/weekly/2026-W42/main.tex: Section 7 (B57 ASPIRE prose)", "surveys/weekly/2026-W42/main.tex: Table T7"]
  },
  {
    "check_id": "FINAL_SYNTHESIS",
    "status": "PASS",
    "detail": "I read the Section 7 tail (PLawBench/beta note through the three-item closing sentence) in full. It re-bundles the three P7 items as usable-condition records (legal anchor with price/weights conditions, robotics with date/dependency conditions, vision with mechanism/shortfall conditions) without introducing new numbers, dates, or causal claims. The preceding recap sentences restate values already established earlier in the section. No new factual assertion requiring a citation appears in the tail.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 7 tail"]
  },
  {
    "check_id": "WEEKLY_COMMUNITY_MOVEMENT",
    "status": "PASS",
    "detail": "Community and X signals are kept as distribution/announcement context, never as technical evidence, in the passages I read. SNS/X sentences explicitly limit posts to existence proof and deny them measurement status, and the bibliography labels X items as secondary reference. No ranking, benchmark, or license conclusion is grounded on a post alone. The requirement's placement across Sections 1-3 is genuine: each chapter carries its own announcement-existence sentence plus a reader box restating the discipline.",
    "evidence_locations": ["surveys/weekly/2026-W42/main.tex: Section 1", "surveys/weekly/2026-W42/main.tex: Section 2", "surveys/weekly/2026-W42/main.tex: Section 3", "surveys/weekly/2026-W42/main.tex: bibliography B08/B10/B63-B64/B67-B68/B70-B71"]
  },
  {
    "check_id": "R18_PDF_SEMANTIC_BINDING",
    "status": "PASS",
    "detail": "I read the manifest primary_source block and compared it to the file I hashed: path surveys/weekly/2026-W42/main.tex, sha256 2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3, and byte count 96790 all match the TeX bytes on disk. This TeX is therefore the manifest-bound primary source. I additionally confirmed 7 sections, 7 tabularx tables, and 7 table captions structurally, consistent with the manifest's 7-chapter shape.",
    "evidence_locations": ["sources/2026-W42/publication/v2/reader-manuscript-v2.json: primary_source", "surveys/weekly/2026-W42/main.tex: Sections 1-7", "surveys/weekly/2026-W42/main.tex: Tables T1-T7"]
  }
]
```

## Overall decision
- decision: PASS
- basis: All eight surface checks pass on the exact TeX bytes I hashed. Structural identity (7 sections, 7 tables, 90 bibitems, 0 unregistered cites, 0 untranslated markers, neutral cover with no diagnostic stamp) holds. The three L02 PARTIAL drifts are openly recorded below as WARNING/UNRESOLVED findings; none breaks a must-cover requirement or warrants FAIL by my judgment.

## Findings
1. finding_id: W42-SOL-SURF-F01
   locator: surveys/weekly/2026-W42/main.tex Section 7 + Table T7 (B54 prose: "79件中7位")
   text_span: "19.17％・79件中7位"
   severity: WARNING
   reason: Worker L02 confirms the Vals anchor (19.17%, $0.15/test, LegalBench 86.23%) but documents live-source denominator drift: Updates prose pins #7 of 79 while header/table now show #7 of 81 as the leaderboard grew. The TeX pins the 79 snapshot without naming the drift, so a reader comparing against the live page will see a denominator mismatch.
   proposed_normalization: Add a parenthetical snapshot marker in a future revision (e.g. window-snapshot denominator) or a one-line disclosed-limitation note; do not silently change the number without re-audit.
   disposition: UNRESOLVED
2. finding_id: W42-SOL-SURF-F02
   locator: surveys/weekly/2026-W42/main.tex Section 7 (B54 prose, twice: lead paragraph and design paragraph)
   text_span: "1件72分"
   severity: WARNING
   reason: Worker L02 fetch finds current card latency "37 min 25 s" and no 72-min field in the fetched excerpt; the 72-min figure is either source drift or a different timing field (total vs per-test) that cannot be re-fetched for the window. The TeX repeats 72 min twice as a measurement condition, so the field-level provenance is weaker than the ranking anchor.
   proposed_normalization: Qualify the figure as window-state reported value with disclosed limitation, or drop the minute figure to price-only if the field cannot be sourced; no silent revision.
   disposition: UNRESOLVED
3. finding_id: W42-SOL-SURF-F03
   locator: surveys/weekly/2026-W42/main.tex Section 7 (B57 prose: "10月16日の今週の出来事", "10月16日のX投稿は告知")
   text_span: "10月16日"
   severity: WARNING
   reason: Worker L02 confirms repo existence, Apache-2.0 apportionment, and June-vs-October split, but the fetched README shows month granularity ([2026-10]) only with no Oct-16 commit/release timestamp in the excerpt. The TeX asserts day precision twice; table T7 itself says month-granularity, creating a prose/table precision asymmetry. No separate ASPIRE X-post bib key exists, so the X sentence is correctly announcement-discipline prose, not a dated citation.
   proposed_normalization: Soften prose day-precision to month-anchored wording consistent with Table T7, or retain with an explicit disclosed-limitation note; do not invent a commit timestamp.
   disposition: UNRESOLVED
4. finding_id: W42-SOL-SURF-F04
   locator: surveys/weekly/2026-W42/main.tex % comment lines 1-3
   text_span: "built from r18 Reader bytes (v18.0)"
   severity: INFO
   reason: TeX comments reference internal pipeline identifiers (r18/r26/r29), which is normal build provenance. I verified these lines are % comments and do not render; no reader-visible leakage. Recorded for completeness only.
   proposed_normalization: None required.
   disposition: RESOLVED (no reader effect)

## Limits of this review (not verified by me)
- Full 71-URL liveness and all-90-key source-content re-verification were not performed by me; I verified bibliography/citation internal integrity by reading plus L02 worker fetches for B16/B54/B57 only.
- Full 150-block verbatim containment was not re-run by me beyond my chosen spot-checks; the archived r29 independent report's full-count proof is cited as provenance, not as my verdict.
- Visual/print rendering was not re-performed by me; L03 worker 21/21 byte-identical re-render is cited as worker evidence only.

- reviewer_identity: Independent review subagent (Sol review role; not the r30 build worker)
- reviewed_at_utc: 2026-10-20T00:13:39Z
RAW_SEMANTIC_SURFACE_REPORT_END
