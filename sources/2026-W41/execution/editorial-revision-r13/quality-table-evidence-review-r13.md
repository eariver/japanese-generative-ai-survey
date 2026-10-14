# W41 textGrain quality-table evidence review (MAJOR-04)

Status: `EDITION_LOCAL / EVIDENCE_REVIEW / READ_ONLY`
Date: 2026-10-13 JST
Question: do the saved sources pin the Astra quality-table column headers?

## 1. Saved-excerpt check (canonical, read-only)

`external/evidence-supplement/r4/textgrain-blog-r4.source-excerpt.md` line 8:

> Astra watermark-quality table (max): AA Index 49.57/49.76, AutomationBench 34.09/34.86,
> DeepSWE 72.80/71.68, TB4 53.90/56.06, TBSci 56.90/60.00, BrowseComp 87.92/87.35,
> HealthBench 64.27/64.60, GPQA 94.44/93.94.

Value pairs only — **no column headers, no comparison condition** in the saved bytes.
A DailyX secondary note (`external/daily-x/raw/2026-10-06_0700.md:113`) describes the table
as watermark on/off comparison, but a secondary note is not the official header.

## 2. Known-official-original re-verification (read-only, NOT adopted as Evidence)

The live official page `https://openai.com/index/eu-text-provenance/` (fetched 2026-10-13,
verbatim text) carries, under "Impact of watermarking on output quality", the header row:

- `Benchmark | Unwatermarked text (Astra, max) | Watermarked text (Astra, max)`

with the same eight rows and pairs as the saved excerpt (DeepSWE v1.1, Terminal-Bench 4.0,
Terminal-Bench Science 0.1, BrowseComp, HealthBench Professional, GPQA Diamond), plus the
sentence "we do not see meaningful performance differences with and without watermarking."

Nothing from this fetch was adopted as canonical Evidence; accepted Cards, manifests,
checkpoints, and State are untouched. It serves only as editorial header confirmation.

## 3. Editorial decision

Column headers are **confirmed** (Unwatermarked vs Watermarked, Astra max). The r13 P5
proposal therefore carries a full quality comparison table (t3) plus a reading paragraph
(p13), both labeled vendor-run without independent reproduction, and both keeping
detection-rate evaluation on a separate axis from answer-quality evaluation.

`QUALITY_TABLE_AUTHORITY_INSUFFICIENT` is **not** declared: the header question is
resolved by the official original; the remaining limits (vendor-run, no independent
reproduction, PDF unread) are stated in prose rather than blocking the table.

## 4. must_cover consequence

P5 `must_cover_coverage[0]` (textGrain figures incl. quality table) now maps to
`["p2", "p3", "t2", "p13", "t3"]` — the quality substance has real reader blocks,
not a name-only mention.

(End of file)
