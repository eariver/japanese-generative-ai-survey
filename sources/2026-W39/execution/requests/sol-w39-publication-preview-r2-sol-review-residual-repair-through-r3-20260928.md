# W39 Publication Preview r2 — Sol residual repair through fresh r3

Status: `EXECUTION_AUTHORITY / SOL_PUBLICATION_PREVIEW_R2_RESIDUAL_REPAIR / HUMAN_DECISION_STILL_PENDING / PUBLICATION_LOCAL_ONLY`

Date: `2026-09-28 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W39-v2-work`

## 1. Purpose

Publication Preview r2 was produced successfully and remains `PENDING` for Human decision. Sol independently reviewed the final r2 reader-facing bytes and found residual Issue #501-style wording plus one clear typo that were not fully captured by the worker's residual scan.

This execution is a **pre-Human-decision publication-local correction**. It MUST NOT create, infer, or record a Human `APPROVED` or `REQUEST_CHANGES` decision for r2.

The goal is to repair only the remaining reader-surface defects, rebuild/revalidate the publication candidate, re-prove PDF byte identity, and produce a fresh Publication Preview r3 with Human decision still `PENDING`.

Normal terminal state:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R3_PENDING`

Do not Freeze or Release.

## 2. Starting authority and immutable upstream authority

Invocation MUST bind to the exact current remote work-branch HEAD/tree that contains this request.

Before any write, verify read-only:

- remote `weekly/2026-W39-v2-work` HEAD == invocation Exact Starting SHA;
- remote work tree == invocation Expected Starting Tree;
- reviewed `main` HEAD == `519aed90607f6e787bb3a7c00b651777835fd657`;
- reviewed `main` tree == `3a59771e7e5622c4d3c4bebad55fec52b42151c4`;
- frozen `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Publication Preview r2 shell commit `e9a58f8389a58f2e64680f0904ccf439d60beb91` is an ancestor;
- reviewed r2 publication authority commit `d95a811abd014ad4476d8f305b792920aa6e87fe` is an ancestor;
- Sol r2 residual terminology commit `f331e329af4168ac5b0c56f690bf84b944446c33` is an ancestor.

If any guard fails, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, force push, reset, rebase, or history rewrite.

## 3. Human-gate boundary

Current Human Publication Preview decision remains `PENDING`.

Do NOT create a `publication-r2.json` Human decision artifact and do NOT mutate the existing r1 Human `REQUEST_CHANGES` record.

Treat this as a Sol reviewer correction before r2 receives a Human decision.

Architecture approval remains valid and immutable. Do not alter Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture.

Only publication-local reader surfaces and regenerated publication/validation artifacts may change.

## 4. Combined terminology authority — all three corpora are mandatory

The terminology review authority for this run is the union of:

1. `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
2. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
3. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`

These files are **read-only QA authority**, not auto-replacement dictionaries.

Enumerate every observed/search form from all three corpora and search all W39 canonical reader-facing surfaces.

For every hit, decide occurrence-by-occurrence:

- `REPLACE`, or
- `RETAIN_WITH_CONTEXT_REASON`.

For forms with no hit, record `ZERO_HIT_CHECKED`.

Do not limit the scan to the words that Sol listed from r2. Terms absent from the current edition must still be checked and recorded as zero-hit.

If the correct technical identity is unclear, read back accepted W39 evidence/source authority before editing. Do not invent technical identities from general knowledge.

## 5. Sol-confirmed residual defects from final r2 bytes

At minimum, independently adjudicate and repair the following final-reader-surface occurrences where context confirms they are defective:

- `卓上版` in the GPT-6 availability sentence — replace with the actual product/interface availability wording supported by accepted source authority;
- `腕前のベンチマーク結果` — use natural benchmark/evaluation wording;
- `貯めて使える制限の戻し` — restore the actual usage-limit / rollover / banking concept supported by source;
- `発表側の手つき` — replace with natural attribution wording such as vendor-reported benchmark methodology/context;
- `大勢の利用での試し（A/B）` — use `A/Bテスト` / production A/B testing wording if supported;
- `学びの長さ` — use training duration/long-RL wording supported by source;
- `三つのモデルで寄せた` — use natural performance-comparison wording;
- benchmark/evaluation-context `測り` / `計り方` where still metaphorical rather than ordinary Japanese;
- `中身の正しさは本号では量らない` — use verification/evaluation wording;
- `プレプリントの記録だけで立つ` — use evidence/source-bound wording;
- `四組織による作` — use development/collaboration wording;
- `公式の場の示し` — use official announcement/post/document wording;
- reasoning-effort-context `力の入れ方` — preserve actual `reasoning effort` / effort-level identity;
- `書きぶり` where used as a substitute for release/availability wording;
- the clear typo `ツール定義を使るとき` — correct grammar (`使うとき`) while preserving meaning.

These are minimum known findings, not the complete search universe.

## 6. Final-bytes residual scan is mandatory

The r2 worker dossier stated that a seed-external residual scan had repaired terms including `書きぶり`, but final r2 TeX still contained `ただし書きぶりは…`. Therefore, scanning an intermediate draft is insufficient.

After **all** edits and after the final TeX has been generated, perform a fresh independent read/search over the exact final reader-facing bytes that will be built into the PDF.

The final-byte scan must look for:

- remaining forced/novel kanji substitutions;
- metaphorical substitutes for model/agent/cache/benchmark/runtime/security/privacy concepts;
- Chinese-like literalizations;
- named-model/benchmark/metric/method identity loss;
- typos/grammar corruption introduced during repair;
- phrases claimed as repaired in the occurrence ledger/dossier but still present in final TeX;
- newly introduced overtranslation not already present in any seed file.

If a new generic defect is found, append it to a new explicit successor supplement before finalizing, then re-run the combined scan.

The completion criterion is not “all listed words were edited”; it is “no unresolved reader-facing overtranslation or typo remains in the exact final bytes”.

## 7. Occurrence ledger r3

Create a fresh r3 occurrence ledger and human-readable summary under:

`sources/2026-W39/execution/terminology/`

The ledger must record, at minimum:

- corpus source;
- observed/search form;
- file + locator;
- context excerpt;
- canonical/source concept;
- decision (`REPLACE` / `RETAIN_WITH_CONTEXT_REASON` / `ZERO_HIT_CHECKED`);
- replacement or retained form;
- reason;
- whether source recheck was needed;
- source recheck result;
- post-edit final-byte validation.

Do not count frozen internal Draft/package artifacts as repaired reader surfaces. They may remain unchanged under the sealed Architecture/Draft boundary, but the ledger must clearly distinguish `FROZEN_INTERNAL_NON_READER` from reader-facing `RETAIN_WITH_CONTEXT_REASON` so totals cannot hide reader defects.

Report separate totals for:

- reader-facing hits;
- reader-facing REPLACE;
- reader-facing RETAIN_WITH_CONTEXT_REASON;
- ZERO_HIT_CHECKED forms;
- frozen internal non-reader occurrences;
- seed-external residuals found and repaired.

## 8. Reader-facing regeneration

Repair the canonical reader-facing source layer, not final PDF bytes by hand.

Regenerate/revalidate as required by the current frozen Core publication pipeline:

- reader manuscript / reader-surface inputs;
- TeX/Bib;
- identifier/citation bindings;
- semantic editorial review;
- reader-surface gate;
- deterministic publication checks;
- visual review;
- PDF;
- publication candidate;
- stage validation.

Do not change accepted facts, numbers, dates, evidence strength, attribution, temporal boundaries, HOLD/PARTIAL handling, citation set, Architecture package order, or thesis except where wording correction is necessary to preserve the same meaning.

## 9. PDF byte-binding invariant — must remain independently proven

r2 successfully repaired the r1 provenance defect. r3 must preserve that property for the newly generated PDF.

For the exact r3 reviewed candidate, independently compute from real bytes and require:

`SHA256(repository main.pdf)`
`== repository main.pdf.sha256`
`== SHA256(Actions artifact main.pdf)`
`== artifact main.pdf.sha256`

Also require identical byte counts for repository PDF and artifact PDF.

Do not claim PASS from workflow success, filenames, sidecars, or equal byte counts alone.

Record the exact workflow run ID, artifact ID, PDF SHA-256, byte count, and page count in the r3 review shell/dossier.

If exact-byte identity cannot be achieved without modifying Shared Core/CI, stop and report the blocker. Do not modify frozen Core.

## 10. Review/dossier truthfulness

The r3 dossier must be computed from final r3 bytes.

Do not state that a residual term was repaired unless it is absent (or explicitly context-retained with reason) in the exact final reader-facing files.

Any wording such as “all residuals repaired” must be backed by the final-byte scan and occurrence ledger.

Worker/Agent review findings must remain attributed to Worker/Agent. Do not claim Sol or Human approval.

## 11. Fresh Publication Preview r3

If all required repairs, validations, final-byte terminology scan, and PDF identity checks PASS, create:

- fresh `publication-preview-r3.md`;
- fresh `publication-preview-r3-dossier.md`;
- any r3 validation/terminology artifacts required for reproducibility.

Final state must remain:

- lifecycle `RELEASE_CANDIDATE`;
- terminal `HUMAN_GATE_REACHED`;
- next action `PUBLICATION_PREVIEW`;
- Human Publication Preview decision `PENDING`.

Do not Freeze or Release.

## 12. Commit/push discipline

Use only existing branch `weekly/2026-W39-v2-work`.

Normal commits + non-force push only.

After every write group, read back remote HEAD. Before the next write group, verify the expected prior remote HEAD.

No Shared Core, `main`, or production-line branch changes.

## 13. Required final report

Report at minimum:

- starting HEAD/tree;
- ending HEAD/tree;
- commit list;
- changed paths by category;
- confirmation that Architecture/upstream bytes were unchanged;
- three-corpus search-form totals;
- reader-facing hit / REPLACE / RETAIN totals;
- ZERO_HIT_CHECKED total;
- frozen-internal occurrence total;
- seed-external residual count and exact repaired forms;
- typo corrections;
- final reader-surface gate result;
- semantic/deterministic/visual validation results;
- repository PDF SHA/bytes/pages;
- Actions run/artifact IDs;
- artifact PDF SHA/bytes;
- both sidecar values;
- explicit four-surface identity verdict;
- final lifecycle / next action / terminal reason;
- r3 Human review path;
- Human decision = `PENDING`;
- Shared Core changed paths count = `0`.

Stop at fresh Publication Preview r3.