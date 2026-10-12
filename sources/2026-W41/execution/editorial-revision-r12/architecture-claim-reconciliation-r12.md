# W41 P5 Architecture claim reconciliation — `text excluded` (R11-M05)

Status: `RECONCILED_BOUNDED_READING / ARCHITECTURE_UNCHANGED`
Date: 2026-10-13 JST
Scope: R11-M05 (Authority整合性). Architecture text is NOT modified; this document
records the interpretation under which the approved wording and the evidence coexist.

## 1. ARCHITECTURE_LITERAL_WORDING (verbatim, read-only)

Approved `sources/2026-W41/architecture-v2.json` (`9a79e8d3…`), package P5:

- purpose (excerpt): "SynthID portal scope expansion (modalities, partners, scale as
  blog-stated, **text excluded**)".
- must_cover_requirements[2]: "SynthID scope table (English-global date, image/video/audio
  modalities, named partners plus soon-Apple, vendor scale counts, **text excluded**) with
  portal-JS-shell-unfetchable and accuracy-absent boundaries."

## 2. EVIDENCE_SUPPORTED_READER_CLAIM (what the saved sources support)

- Supplement excerpt (`synthid-blog-r4.source-excerpt.md`): the post enumerates
  **images, video, and audio** as SynthID scope; partner list and scale counts stated.
  A reviewer NOTE records "text NOT listed as a supported type **on this post**".
- Accepted Card (`e9e…` no — SynthID task `evidence:2026-W41:ef2ef9a25ec009ba`):
  claim-1 states portal scope as image/video/audio with vendor-stated scale;
  limitation-1 states the portal body is unrendered and accuracy benchmarks are absent.
- Supported reader claim (upper bound): "The saved official blog explicitly lists
  image, video, and audio as verification scope; **whether text is supported cannot be
  determined from this excerpt**."
- NOT supported: "The SynthID verification portal does not support text" as a settled
  product fact. Enumeration-absence ≠ capability-absence, and the portal body itself
  was never fetched.

## 3. EDITORIAL_RECONCILIATION

The literal "text excluded" is read in the **bounded, scope-table sense**: within the
must-cover's own frame — a scope table built from the saved blog — text has no row,
because the saved enumeration contains image/video/audio only. The surrounding architecture
words ("modalities", "scope table", "as blog-stated", "scope-only") all point at
describing the blog's enumeration, not at asserting product capability. Under this
reading:

- must_cover[2]'s intent (a scope table that handles text as absent-from-listing, plus
  unfetchable/accuracy boundaries) is substantively met by r11/r12 p6 (bounded text
  sentence), t1 (text row marked as unconfirmable-from-source), p7/p11 (portal limits),
  with coverage mapped to exactly those blocks.
- Reader prose (r11 and r12) never upgrades the bounded reading to a non-support
  verdict: fixed phrasing is "取得した公式ブログで検証対象として明示されているのは
  画像・映像・音声であり、テキストの対応状況はこの資料からは確認できない。"
- The P4-style machine-trace problem does not arise here: no accepted Card carries a
  categorical "text unsupported" span, so nothing needed OMISSION on this point; the
  limitation-1 boundary is EXPLICITLY_STATED with the bounded wording.

No `ARCHITECTURE_LITERAL_CONFLICT_UNRESOLVED` is declared: the bounded reading is
compatible with both the literal words and the evidence, and it is the only reading
used in reader surfaces. If Sol judges the literal words to compel the stronger
(non-support) reading instead, this document must be superseded and the conflict flag
raised — no Architecture bytes were changed either way, and no Human approval was
re-recorded.

(End of file)
