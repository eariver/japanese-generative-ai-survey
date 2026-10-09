# TS-003 Sol Reader / Publication Review r4

Status: `SOL_READER_PUBLICATION_REVIEW_R4 / PASS / R4_EXACT_PDF_ACCEPTED`

Date: `2026-10-03 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed recovery commit:

`59f89f89d9606ddb1328aeff07e4f63c0aae4ae7`

Reviewed tree:

`7c3b31c92229e6b63ffd6b8c758dcac6e1b5cbba`

Decision:

`PASS / CANONICAL_DRAFT_R1_RECOVERED / READER_EDITORIAL_R9_REBOUND / R4_EXACT_PDF_ACCEPTED`

Authority distinction preserved:

`CANONICAL_DRAFT_AUTHORITY = checkpointed Draft r1`

`READER_EDITORIAL_AUTHORITY = Sol-accepted r9 refinement, publication layer only`

This review does not claim that r9 is canonical Draft authority. Canonical Draft
authority is checkpointed r1 via immutable `ARCHITECTURE_ESTABLISHED.json`.
Reader wording is edition-local editorial authority
(`publication/editorial/reader-editorial-authority-r9.json`), Sol-accepted r9
refinement for publication rendering only.

Historical `ARCHITECTURE_ESTABLISHED.json` remains immutable (blob
`3c8024311d911f4e3a44e29859fc5cf481e0073e`). The r1 canonical recovery
(18/18 checkpoint match, 16/16 packages unchanged) resolved the Frozen Core
prior-artifact drift without rewriting history, checkpoint replacement,
lifecycle rollback, or shared-Core change.

R4 is the exact PDF now accepted for subsequent Publication Preview authority.

Accepted r4 PDF:

path:

`surveys/special/vision-multimodal-2026/main.pdf`

Git blob:

`88fb15bd854cc7046f41ed98ef57365a7f8e2de7`

SHA-256:

`78f4cc8c79c008c92a4af2a8e5f343f7a5d0c22e59f89d2fbe48c562318c214c`

byte count:

`684804`

page count:

`38`

This PASS authorizes DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE
progression to the Publication Preview Human gate. It does not approve
Publication Preview, Freeze, Release, or any new research.

## 1. Guard and lineage verification

Independent Sol verification confirms:

- recovery commit is one normal child of `4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633`;
- recovery commit is `59f89f89d9606ddb1328aeff07e4f63c0aae4ae7`;
- recovery tree is `7c3b31c92229e6b63ffd6b8c758dcac6e1b5cbba`;
- main remains `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- production state remains `DRAFT_COMPLETE` (blob `cc0c7fc11746c64ef15027a8b38af45bdc916da3`);
- Architecture Review remains approved; Publication Preview remains pending;
- validation/publication_preview/freeze/release remain pending; terminal null;
- r1 source commit `d1053e957d92cddd9d2759ec9713db59c66263ad` restored 18/18;
- r9 commit `79d2b3e291e10896ed616bd698abefc1e479ddbe` preserved as editorial source only;
- terminology blob `cf39a5860d64b5d85a3a382911680dcadaa954a1`, status `DRAFT_R9_BINDING`;
- no stage advance, checkpoint mutation, Human approval, Freeze, or Release occurred before this review.

## 2. Canonical recovery verification

- 18 restored files match `ARCHITECTURE_ESTABLISHED.json` SHA-256 `18/18 EXACT MATCH`;
- 16 `draft-package.json` unchanged `16/16 UNCHANGED`;
- checkpoint blob unchanged; lifecycle held at `DRAFT_COMPLETE` to make validation pass honestly;
- reader/editorial authority `7ab5751f3a8bb9ab897d4968481a738764868d768eac6eacb3b242c9032ae9d0` validated independently (Evidence sets bounded, limitations preserved, Arch order intact);
- renderer rebound: canonical r1 for provenance/integrity, editorial r9 for wording, approved Architecture/Profile, accepted Evidence for bibliography; misleading `accepted Draft r9 bytes` provenance replaced with checkpointed-r1 + editorial-transform wording;
- manuscript locations derived from editorial authority / generated TeX, not r1 prose;
- semantic/editorial no longer claims TeX identical to canonical Draft r9; explicitly validates canonical=r1 vs reader=editorial separation with no new facts/sources.

## 3. r3 -> r4 reader-visible identity

R4 is not byte-identical to r3. Independently checked r3->r4 differences were
confined to PDF build metadata/trailer identity; reader-visible content,
extracted text, page geometry, content rendering, citation surface, pagination,
and normalized PDF content were preserved.

- r3 PDF SHA `637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`, 684804B, 38pp, `CreationDate D:20261003015043+09'00'`;
- r4 PDF SHA `78f4cc8c79c008c92a4af2a8e5f343f7a5d0c22e59f89d2fbe48c562318c214c`, 684804B, 38pp, `CreationDate D:20261003042922+09'00'`;
- `main.tex` non-comment identical (only 17 provenance comment lines changed);
- `references.bib` non-comment identical (only header comments changed);
- `pdftotext` SHA identical `a330bcb7237fb4fe5b46a66e450f2a3082c56a1887ee7eb68fd567b33859c308`, 5107 lines;
- 150dpi PNG `38/38` hash-identical; per-page text identical 38/38; normalized PDF (strip CreationDate/ModDate/ID) byte-identical.

No unexpected reader-visible difference. No content-stream semantic difference.
No citation difference (111/111). No pagination difference.

## 4. Exact r4 publication checks

- `main.tex` blob `7def79c1cb026f4882a68c3e66db25086541dd75`, SHA `da750a40a1c37e73abdd7a763c3ef6784e5d3991f97f04bac5393ed118c3a484`;
- `references.bib` blob `5e85ebf0af1a8e11f89f3490e1cb6b2a090241db`, SHA `2a3745c759a1c5b9441008c5689af4750f39ca9a413c95e9a0ad97407114b05c`;
- manuscript SHA `581fa7066eed88eefabbb17da289e67da42278db331b0f1006a6270bbbbf5e9d` binds exact TeX;
- bundle SHA `807433669d6a01acf5bc347196c725dc42f42cd2d4a3d5f11c9e058e01e0a5fe`;
- semantic/editorial SHA `89f3c64010ea9b09b7027d7a1d3154843644064def72d32079c613c47e024f2f`;
- visual SHA `2038b29595eb377a30e62689a56c2b0bc3da26edf01ce9b0e6b165dd9a316922`;
- gate SHA `3f92a567d6c8f17f7b520d01f644d35a59e01d3c40a2d29304eb5657697d3547`;
- editorial authority SHA `7ab5751f3a8bb9ab897d4968481a738764868d768eac6eacb3b242c9032ae9d0`;
- PDF preflight PASS, 0 blocking, 0 layout, 38 pages;
- manuscript/bundle/semantic/visual/gate Core validators PASS;
- Frozen Core `DRAFT_COMPLETE` non-advancing validation PASS (drift cleared).

## 5. Next authorized stop

Advance `DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE` to
`PUBLICATION_PREVIEW / HUMAN_GATE_REACHED` using unchanged r4 bytes via
canonical Core contract. Do not rebuild TeX/bib/PDF. Do not approve Publication
Preview. Do not Freeze/Release.

Terminal:

`TS-003 SOL_READER_PUBLICATION_REVIEW_R4_PASS`

`TS-003 CANONICAL_DRAFT_R1_RECOVERED`

`TS-003 READER_EDITORIAL_R9_REBOUND`

`TS-003 R4_EXACT_PDF_ACCEPTED`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
