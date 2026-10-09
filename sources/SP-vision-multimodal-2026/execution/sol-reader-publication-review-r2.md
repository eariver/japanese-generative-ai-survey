# TS-003 Sol Reader / Publication Review r2

Status: `SOL_READER_PUBLICATION_REVIEW_R2 / REQUEST_CHANGES / STALE_PUBLICATION_PROVENANCE_REBIND`

Date: `2026-10-03 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed publication candidate r2 commit:

`0ce457df8090fdfee45a199c271ffea73bf587ec`

Reviewed tree:

`b08cea28b7805988b5548d441277cc69a3804061`

Candidate PDF:

`surveys/special/vision-multimodal-2026/main.pdf`

Candidate PDF SHA-256:

`a18caa91e4530968b99f57e88324a0d3057b58627f888c91acd9e3b341a8028d`

Candidate PDF size/page count:

`684804 bytes / 38 pages`

Accepted reader authority:

`Draft r9 @ 79d2b3e291e10896ed616bd698abefc1e479ddbe`

Decision:

`REQUEST_CHANGES`

Candidate r2 correctly carries the accepted r9 reader prose into the canonical TeX/PDF surface and all non-stage deterministic checks report PASS. However, canonical publication provenance/review artifacts still contain stale r6 authority references and stale pre-r7 section titles. The publication bundle is therefore internally inconsistent and cannot yet be used as the Human Publication Preview candidate.

No Draft r9 prose change is required.

## 1. What passed

Independent Sol verification confirms:

- r2 is one normal child of the authorized publication-regeneration start;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- production state remains byte-identical at `DRAFT_COMPLETE`;
- no stage validation/advance, Human Preview decision, Freeze, or Release occurred;
- canonical `main.tex` contains the accepted r9 terminology repairs, including:
  - `ボックス`;
  - `オープンボキャブラリー`;
  - `バックボーン`;
  - `密に融合する`;
  - `検出へ適応させる`;
  - corrected P15 punctuation;
- candidate PDF is 38 pages and worker deterministic preflight reports:
  - 0 blocking findings;
  - 0 layout findings;
  - no undefined citations/references;
  - 111/111 citation bindings;
- worker visual-review artifact records all 38 pages inspected with no clipping, overflow, missing glyphs, collisions, broken tables, stranded headings, or blank pages;
- reader-surface gate reports zero reader-surface findings;
- bibliography remains Evidence-bound and unchanged where expected.

The reader prose itself is not reopened by this review.

## 2. Blocking F1 — canonical main.tex declares stale Draft r6 provenance

The first line of canonical:

`surveys/special/vision-multimodal-2026/main.tex`

still reads:

`% Generated deterministically from accepted Draft r6 bytes + approved Architecture/Profile/Synthesis authority. Do not hand-edit.`

Candidate r2 was authorized and built from accepted Draft r9, not r6.

This comment is not reader-visible in the rendered PDF, but it is canonical publication-source provenance. A publication bundle must not claim one reader authority while its primary source metadata names another.

Required repair:

- regenerate the source with Draft r9 provenance;
- do not hand-patch only the committed TeX if the execution renderer would recreate the stale line;
- repair the r3 renderer/provenance source so regeneration is deterministic.

## 3. Blocking F2 — reader-surface semantic review still binds Draft r6 and stale headings

Canonical:

`sources/SP-vision-multimodal-2026/publication/v2/reader-surface-semantic-review-v2.json`

contains:

`All 16 packages render accepted Draft r6 headline/deck/blocks byte-identically...`

This is false for the current authority.

Its evidence locations also retain stale pre-r7 reader headings, including:

- `Section 2 — 箱から集合予測、開かれた語彙へ`;
- `Section 8 — 言葉を箱とマスクに結ぶ接地`;
- `Section 9 — 凍結した部品をつなぐ橋`.

The actual canonical r2 TeX headings are:

- `Section 2 — ボックスから集合予測、オープンボキャブラリーへ`;
- `Section 8 — 言葉をボックスとマスクに結ぶ接地`;
- `Section 9 — 凍結した視覚・言語モデルを接続する`.

Therefore the semantic-review PASS is not correctly bound to the surface it claims to review.

Required repair:

- regenerate semantic review from current r9-derived TeX/manuscript;
- authority text must name Draft r9;
- evidence locations must be derived from the actual current headings, not hard-coded historical strings.

## 4. Blocking F3 — semantic-editorial review still describes accepted r6

Canonical:

`sources/SP-vision-multimodal-2026/publication/v2/semantic-editorial-review-v2.json`

contains in `POST_TRANSFORM_SEMANTIC_REVALIDATION`:

`TeX transform revalidated: headlines/decks/blocks/boundaries match accepted r6 bytes modulo escaping...`

This must name accepted r9 and be regenerated/bound to the current r9 publication authority.

The rest of the current semantic-editorial evidence locations appear to use the current section titles; the blocker is the stale authority statement.

## 5. Provenance consistency rule

Candidate r3 must establish one coherent authority chain:

`Sol Draft Review r9 PASS`
→ accepted r9 Draft Results / synthesis
→ r9-derived reader manuscript
→ r9-derived main.tex
→ semantic review of that exact source
→ semantic-editorial review of that exact source
→ deterministic bundle/gate
→ exact committed PDF
→ exact-PDF visual review.

No canonical current artifact may assert accepted r6 or use stale r6/r7 headings as evidence locations.

Historical execution reports/snapshots may retain their original r6/r7 wording. The zero-stale-reference scan applies to the **current canonical publication bundle and current r3 execution artifacts**, not immutable historical records.

## 6. PDF status

The r2 PDF contents are consistent with r9 reader prose in the source regions independently inspected, and worker PDF preflight/visual review is clean.

However, because the canonical review/provenance bundle is internally stale, r2 is not accepted as the Human Publication Preview candidate.

Independent Sol pixel-level final acceptance is deferred to the corrected exact r3 PDF/bundle. The web PDF screenshot path was unavailable for this GitHub binary during r2 review, so no claim of independent pixel-level Sol PASS is made for r2.

## 7. Core checkpoint blocker remains separate

The known shared-Core checkpoint-staleness issue remains unchanged.

Do not:

- rewrite historical `ARCHITECTURE_ESTABLISHED.json`;
- mutate checkpoint provenance;
- fake stage validation PASS;
- advance lifecycle.

Candidate r3 remains a `DRAFT_COMPLETE` publication candidate for Sol review.

## 8. Required candidate r3 repair scope

This is a publication-provenance-only repair/regeneration.

Immutable:

- Draft r9 reader prose;
- Draft Results;
- profile synthesis prose;
- Draft Packages;
- Evidence;
- Selection;
- Architecture;
- bibliography source set;
- source/evaluator attribution;
- claim boundaries;
- main/Core;
- production state.

Authorized changes:

- r3 execution renderer/review-generation scripts;
- canonical `main.tex` provenance comment;
- current publication/v2 review/manifest/gate/deterministic artifacts that must be rebound to the corrected source hash;
- exact PDF rebuild and exact-PDF review artifacts;
- r3 execution report.

No reader-visible wording change is authorized.

## 9. Candidate r3 acceptance criteria

Before returning to Sol:

1. canonical main.tex provenance says accepted Draft r9, not r6;
2. canonical reader-surface semantic review says accepted Draft r9;
3. semantic review evidence locations exactly match current canonical section headings;
4. semantic-editorial post-transform review says accepted r9;
5. current canonical publication/v2 + main.tex contain zero stale `Draft r6` / `accepted r6` authority references;
6. current canonical review artifacts contain zero stale headings:
   - `箱から集合予測、開かれた語彙へ`;
   - `言葉を箱とマスクに結ぶ接地`;
   - `凍結した部品をつなぐ橋`;
7. reader-visible TeX prose is byte-/text-equivalent to candidate r2 except non-rendering provenance comment;
8. Draft r9 remains unchanged;
9. bibliography remains unchanged unless deterministic metadata binding requires only hashes;
10. all non-stage publication checks rebuilt and PASS;
11. exact PDF rebuilt, SHA/size/pages recorded;
12. all pages visually re-reviewed;
13. production state remains byte-identical `DRAFT_COMPLETE`;
14. Core stage validation remains deferred;
15. no Human Preview/Freeze/Release.

Terminal:

`TS-003 READER_PUBLICATION_R2_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 PUBLICATION_CANDIDATE_R3_PROVENANCE_REBIND_REQUIRED`

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
