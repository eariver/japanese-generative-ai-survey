# TS-003 execution instruction — publication candidate r3 provenance rebind

Status: `EXECUTION_AUTHORITY / SOL_READER_PUBLICATION_R2_REQUEST_CHANGES / PROVENANCE_REBIND_ONLY`

Date: `2026-10-03 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Reader / Publication Review r2:

`sources/SP-vision-multimodal-2026/execution/sol-reader-publication-review-r2.md`

Decision:

`REQUEST_CHANGES`

Reviewed publication candidate r2 commit:

`0ce457df8090fdfee45a199c271ffea73bf587ec`

Reviewed r2 tree:

`b08cea28b7805988b5548d441277cc69a3804061`

Accepted reader authority:

`Draft r9 @ 79d2b3e291e10896ed616bd698abefc1e479ddbe`

Accepted Draft r9 tree:

`4d96d07db9147b3c9a973a6f3bdc6b4cd09d8b53`

Sol Draft Review r9:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r9.md`

Decision:

`PASS`

Binding terminology map:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Expected map blob:

`cf39a5860d64b5d85a3a382911680dcadaa954a1`

Expected map status:

`DRAFT_R9_BINDING`

Frozen Core:

`production/survey-core-v2@774dd39a951c9ac3818e83dfffd4c7666efb0a20`

## 2. Start guards

The Sol launch message supplies the sole exact current work-branch HEAD/tree.

Before any write, read-only verify:

- work HEAD/tree == launch-message expected HEAD/tree;
- main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- map blob == `cf39a5860d64b5d85a3a382911680dcadaa954a1`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- candidate r2 PDF exists with SHA-256 `a18caa91e4530968b99f57e88324a0d3057b58627f888c91acd9e3b341a8028d`.

If any guard differs: zero writes, report expected vs actual, stop.

No new/fallback/repair/review branch, reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

1. this request;
2. `execution/sol-reader-publication-review-r2.md`;
3. `execution/sol-draft-review-r9.md`;
4. `execution/drafting-language-policy-ja.md`;
5. `execution/drafting-terminology-map-ja.md`;
6. accepted Draft r9 Results + synthesis;
7. candidate r2 canonical `main.tex`;
8. candidate r2 canonical publication/v2 artifact family;
9. r2 execution scripts/report;
10. Frozen Core publication schemas/validators.

## 4. Mission

Produce publication candidate r3 by correcting **publication provenance and review binding only**.

Do not rewrite accepted Draft r9.

Do not change reader-visible wording.

The defect is that candidate r2's actual TeX body is r9-derived while some canonical source comments/reviews still claim r6 and retain stale old headings.

Correct the generator/review-generation path and regenerate the canonical publication bundle coherently.

## 5. Required repair A — primary-source provenance comment

Current first line of canonical `main.tex` incorrectly names accepted Draft r6.

Regenerate it to name accepted Draft r9.

Preferred form:

`% Generated deterministically from accepted Draft r9 bytes + approved Architecture/Profile/Synthesis authority. Do not hand-edit.`

A more precise equivalent may include the accepted r9 commit/Sol PASS, but it must not name r6.

This change is non-rendering metadata only.

Do not alter any reader-visible TeX content.

## 6. Required repair B — reader-surface semantic review

Regenerate:

`sources/SP-vision-multimodal-2026/publication/v2/reader-surface-semantic-review-v2.json`

from current candidate r3 source/manuscript.

It must:

- say accepted Draft r9, never Draft r6;
- use current actual section titles;
- not contain stale titles:
  - `箱から集合予測、開かれた語彙へ`;
  - `言葉を箱とマスクに結ぶ接地`;
  - `凍結した部品をつなぐ橋`;
- instead bind:
  - `ボックスから集合予測、オープンボキャブラリーへ`;
  - `言葉をボックスとマスクに結ぶ接地`;
  - `凍結した視覚・言語モデルを接続する`;
- bind the exact current `main.tex` SHA-256.

Do not manually patch only the JSON if the generator would reproduce stale r6 strings. Repair the edition-local generation path.

## 7. Required repair C — semantic-editorial review

Regenerate:

`sources/SP-vision-multimodal-2026/publication/v2/semantic-editorial-review-v2.json`

The `POST_TRANSFORM_SEMANTIC_REVALIDATION` detail must say accepted r9, not accepted r6.

All evidence locations must match current canonical headings.

## 8. Current-bundle stale-reference audit

After regeneration scan the current canonical bundle:

- `surveys/special/vision-multimodal-2026/main.tex`;
- all files under `sources/SP-vision-multimodal-2026/publication/v2`;
- r3 execution artifacts.

For current-authority statements, require zero hits for:

- `accepted Draft r6`;
- `accepted r6`;
- `Generated deterministically from accepted Draft r6`.

For current evidence-location/title strings, require zero hits for:

- `箱から集合予測、開かれた語彙へ`;
- `言葉を箱とマスクに結ぶ接地`;
- `凍結した部品をつなぐ橋`.

Immutable historical r1/r2 execution artifacts outside current canonical publication/v2 are allowed to retain historical wording.

## 9. Reader-text identity check

Compare candidate r2 vs r3 reader-visible TeX.

Allowed source change:

- non-rendering provenance comment;
- mechanically necessary hashes/metadata outside reader-visible prose.

Require all reader-visible content to remain textually identical to candidate r2.

Specifically:

- title/front matter text;
- section headings;
- decks;
- all body paragraphs;
- CLAIM_BOUNDARY boxes;
- synthesis;
- citation placements.

If any reader-visible text differs, STOP for Sol unless it is a pure formatting escape with identical rendering/meaning.

Draft r9 files must remain byte-identical.

## 10. Publication family regeneration

Because `main.tex` source hash changes, rebuild/rebind all current canonical artifacts whose hashes transitively depend on it, including as applicable:

- reader-manuscript-v2;
- reader-surface-semantic-review-v2;
- reader-surface-gate-v2;
- quality-regression-bundle-v2;
- semantic-editorial-review-v2;
- visual-review-v2;
- deterministic checks;
- exact PDF digest/preflight.

Do not leave a mixed r2/r3 artifact family.

## 11. PDF rebuild and visual review

Rebuild exact PDF using canonical LuaLaTeX/Biber path.

Because reader-visible content is unchanged, rendered layout should remain equivalent to candidate r2, but do not assume this.

Record:

- exact PDF path;
- blob SHA;
- SHA-256;
- byte count;
- page count.

Re-run exact-PDF visual review for every page and record:

- clipping/overflow;
- glyph issues;
- collisions;
- tables/boxes;
- page breaks/headings;
- bibliography readability;
- blank-space anomalies;
- copy/punctuation artifacts.

Any reader-visible defect requires STOP for Sol; do not edit Draft prose.

## 12. Non-stage checks

Require all current non-stage publication checks PASS:

- reader manuscript/fidelity;
- semantic review;
- reader-surface gate;
- semantic-editorial review;
- deterministic quality bundle;
- PDF preflight;
- visual review;
- citation/bibliography integrity.

## 13. Known Core blocker

Do not run `DRAFT_COMPLETE -> VALIDATED_DRAFT` stage validation.

Record:

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`.

Do not rewrite historical checkpoints or production-state checkpoint provenance.

Do not advance lifecycle.

## 14. Required r3 report

Create:

`sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r3-20261003/reader-publication-validation-report.md`

Report:

- startup guards;
- Sol r2 review authority;
- accepted Draft r9 authority;
- candidate r2 identity;
- exact provenance defects repaired;
- renderer/review-generator changes;
- candidate r2 -> r3 reader-visible identity proof;
- stale-reference scan result;
- exact changed-path inventory;
- rebuilt publication artifact hashes;
- PDF path/blob/SHA-256/size/page count;
- exact-PDF visual review;
- non-stage checks;
- production-state byte identity;
- known Core defer status;
- main/Core unchanged;
- final HEAD/tree.

## 15. Stop boundary

Keep production state at `DRAFT_COMPLETE`.

Do not:

- stage validate/advance;
- create or approve Human Publication Preview;
- Freeze;
- Release;
- change Draft r9;
- change research/Evidence/Selection/Architecture.

Normal terminal:

`TS-003 PUBLICATION_CANDIDATE_R3_PROVENANCE_REBIND_COMPLETE`

`TS-003 CURRENT_PUBLICATION_BUNDLE_BINDS_ACCEPTED_DRAFT_R9`

`TS-003 EXACT_R3_PDF_READY_FOR_SOL_REVIEW`

`ALL_NON_STAGE_PUBLICATION_CHECKS_PASS`

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`

`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
