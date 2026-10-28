# W43 source-key audit r5 (programmatic, exclusive, span-evidenced)

Method: `source-key-classify-r4.py` (copied here as method reference) counts exact key strings in r3 TeX body pre-bibliography after stripping `%` comments and `\label{...}`; plus `citation-span-and-confidence-r5.md` verifies exact quote/span presence in projection AND TeX-visible text for all 13 natural + 2 further cases.

## Distribution (computed, not presupposed)

- EXACT_VISIBLE_CITATION: 19 (reader-visible key spans; includes tanstack-gh/npm added by r3 repair)
- EXACT_MACHINE_ONLY: 1 (`recap`: sole occurrence is `\label{sec:recap}`; body section IS the content — auxiliary flag, no double count)
- EXPLICIT_NATURAL_REFERENCE: 13 (exact quote/span verified in proj + TeX visible; see span doc; all CURATED_REVIEW_REQUIRED)
- FURTHER_READING: 2 (DI-ENV, DI-LICENSE: same-commit file provenance; natural language present; CURATED_REVIEW_REQUIRED)
- UNAVAILABLE_NO_CLAIM_PROOF: 1 (decisions-ref-create: 404; transparent record only)
- ORPHAN/AMBIGUOUS: 0

Total 19+1+13+2+1+0 = 36. Corrects r3 18/15/2/1/0 (tanstack-gh/npm were NATURAL despite exact print; recap was counted exact despite label-only).

## Rules enforced

- One exclusive primary class per key; auxiliary flags allowed, never double-counted.
- Reader-visible = TeX body minus comments/labels (code spans, 典拠 notes, captions, prose count).
- No claim-provenance from 404 (`decisions-ref-create`) or RAW_NOT_ARCHIVED npm body; GH proves GH only (`tanstack-gh` vs `tanstack-npm` kept separate in body, note, bib).
- A key without body reference retained ONLY as labeled further reading or transparent unavailable-record.

Full per-key table: see r4 `source-key-audit-r4.md` (identical classification; r5 adds programmatic proof + span evidence in `citation-span-and-confidence-r5.md`).
