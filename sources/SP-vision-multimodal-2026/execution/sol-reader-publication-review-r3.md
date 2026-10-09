# TS-003 Sol Reader / Publication Review r3

Status: `SOL_READER_PUBLICATION_REVIEW_R3 / PASS / EXACT_R3_CANDIDATE_ACCEPTED`

Date: `2026-10-03 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed publication candidate r3 commit:

`78b770fbabd4af29afe8a0342b747b01ae4b952b`

Reviewed tree:

`bb94e9ff177b176b778d8c72775767b0692c8bec`

Accepted reader authority:

`Draft r9 @ 79d2b3e291e10896ed616bd698abefc1e479ddbe`

Candidate PDF:

`surveys/special/vision-multimodal-2026/main.pdf`

Candidate PDF SHA-256:

`637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`

Candidate PDF size/page count:

`684804 bytes / 38 pages`

Decision:

`PASS`

Publication candidate r3 is accepted as the exact r9-derived publication candidate. No Draft or reader-visible repair is required.

This PASS does not authorize lifecycle advancement, Human Publication Preview approval, Freeze, or Release. The known shared-Core checkpoint-staleness blocker must be repaired through a sanctioned Core mechanism before normal stage validation can complete.

## 1. Guard and lineage verification

Independent Sol verification confirms:

- r3 worker commit is one normal child of the authorized start `1df8324051e4b7ccd27d2865db5cb3530fcd1feb`;
- r3 commit is `78b770fbabd4af29afe8a0342b747b01ae4b952b`;
- r3 tree is `bb94e9ff177b176b778d8c72775767b0692c8bec`;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- production state remains byte-identical at `DRAFT_COMPLETE`;
- Architecture Review remains approved;
- Publication Preview remains pending;
- validation/publication_preview/freeze/release remain pending;
- no stage validation/advance, checkpoint mutation, Human approval, Freeze, or Release occurred.

## 2. Provenance rebind verification

Canonical `main.tex` now declares:

`Generated deterministically from accepted Draft r9 bytes + approved Architecture/Profile/Synthesis authority.`

Canonical `references.bib` likewise identifies Draft r9 in its non-rendering provenance comment.

Canonical reader-surface semantic review now:

- names accepted Draft r9;
- binds exact current `main.tex` SHA-256;
- uses current section titles, including:
  - `ボックスから集合予測、オープンボキャブラリーへ`;
  - `言葉をボックスとマスクに結ぶ接地`;
  - `凍結した視覚・言語モデルを接続する`.

Canonical semantic-editorial review now states that post-transform fidelity is against accepted r9.

Independent Sol scan of the current canonical publication bundle found zero active stale authority/evidence usage for:

- accepted Draft r6;
- accepted r6;
- the old r6-generation provenance statement;
- the three replaced pre-r7 section headings.

The r3 execution report itself necessarily quotes some of those historical strings while describing the repaired defect; those mentions are historical/descriptive, not current publication authority or current evidence locations.

## 3. r2 -> r3 reader-visible identity

Independent Sol full-file comparison confirms:

- `main.tex`: 357 lines vs 357 lines;
- exactly one changed line: line 1, the non-rendering provenance comment;
- lines 2-357 are byte/text identical.

Independent bibliography comparison confirms:

- `references.bib`: 888 lines vs 888 lines;
- exactly one changed line: line 1, the non-rendering Draft r6 -> Draft r9 provenance comment;
- bibliography entries and source metadata are otherwise byte/text identical.

Therefore candidate r3 introduces no reader-visible prose, citation-placement, section-order, boundary, or bibliography-content change relative to the already reviewed r2 surface.

## 4. Exact PDF binary verification

Candidate r2 PDF:

- SHA-256 `a18caa91e4530968b99f57e88324a0d3057b58627f888c91acd9e3b341a8028d`;
- 684804 bytes.

Candidate r3 PDF:

- SHA-256 `637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`;
- 684804 bytes.

Independent Sol byte-level comparison decoded both committed PDF blobs and found only 68 differing bytes.

Every difference is confined to non-page-content PDF metadata/trailer fields:

- `CreationDate`;
- `ModDate`;
- trailer document `ID`.

The first differing byte occurs in the PDF Info metadata near the end of the file; the remaining differences are the trailer ID. No page/content-stream byte differs.

Therefore r3 has the same rendered page content as r2; only rebuild metadata/identity changed.

## 5. PDF / publication checks

Worker-generated current canonical checks report:

- PDF preflight PASS;
- 0 blocking log findings;
- 0 layout log findings;
- 38 pages;
- reader-surface gate PASS with 0 findings;
- semantic review PASS;
- semantic-editorial review PASS;
- deterministic quality bundle PASS;
- citation integrity 111/111, 0 undefined, 0 uncited;
- exact-PDF visual review PASS across all 38 pages;
- no clipping, overflow, missing glyphs, collisions, broken boxes/tables, stranded headings, blank-page anomalies, or punctuation artifacts.

Sol independently verified the exact r3 PDF binary relationship to r2 as described above and independently reviewed the current TeX authority/provenance surface.

The web PDF screenshot path for this commit was not available through the current browser cache, so this review does not falsely claim a separate browser-render screenshot pass. The exact-page visual evidence is the worker's committed 38/38 review plus Sol's proof that r3 page-content bytes are unchanged from r2.

## 6. Reader authority remains accepted Draft r9

No Draft r9 file changed in the r3 commit.

No research, Evidence, Selection, Architecture, claim-boundary, source-role, or terminology authority changed.

The cumulative Terminology Map remains:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

blob:

`cf39a5860d64b5d85a3a382911680dcadaa954a1`

status:

`DRAFT_R9_BINDING`.

## 7. Known shared-Core blocker

The remaining blocker is not a TS-003 reader/PDF defect.

Frozen Core stage validation still treats the historical Draft identities bound in the `ARCHITECTURE_ESTABLISHED` checkpoint as immutable current Draft identities. TS-003's legitimate reviewed Draft r2-r9 succession therefore fails the current artifact-drift comparison even though the historical checkpoint itself must remain immutable.

Do not rewrite historical checkpoint provenance and do not fake validation PASS.

A sanctioned Core-level Draft supersession/revision-authority mechanism is required so that:

- historical checkpoints remain immutable;
- reviewed Draft revisions can become current authority;
- validation can verify the accepted successor chain;
- unreviewed drift still fail-closes.

## 8. Next authorized stop

Proceed to a bounded shared-Core repair for post-`DRAFT_COMPLETE` reviewed Draft supersession / validation authority.

After that repair is independently reviewed and integrated into the frozen Core authority, return to TS-003 and run the normal reader-publication stage validation against this accepted exact r3 candidate.

Do not rebuild or modify reader-visible TS-003 content unless the Core repair requires a deterministic metadata rebind.

Do not create Human Publication Preview approval yet.

Do not Freeze/Release.

Terminal:

`TS-003 SOL_READER_PUBLICATION_REVIEW_R3_PASS`

`TS-003 EXACT_R3_PUBLICATION_CANDIDATE_ACCEPTED`

`TS-003 READER_VISIBLE_SURFACE_LOCKED`

`CORE_CHECKPOINT_STALENESS_REPAIR_REQUIRED_BEFORE_STAGE_ADVANCE`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
