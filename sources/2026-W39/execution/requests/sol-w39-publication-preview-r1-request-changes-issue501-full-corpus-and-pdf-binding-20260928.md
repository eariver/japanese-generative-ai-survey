# W39 Publication Preview r1 — Human REQUEST_CHANGES at DRAFT_COMPLETE

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / RETURN_DRAFT_COMPLETE / ISSUE501_FULL_CORPUS_TERMINOLOGY + PDF_BYTE_BINDING`

Date: `2026-09-28 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W39-v2-work`

## 1. Human decision authority

The Human Owner reviewed the 2026-W39 Publication Preview r1 and explicitly requested revisions rather than approval.

Decision to record canonically:

`REQUEST_CHANGES`

Allowed regeneration boundary:

`DRAFT_COMPLETE`

This request preserves the already-approved Architecture and all upstream Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture authority.

Do not reopen Architecture unless the current Core contract proves that the requested publication-local repair cannot be represented at `DRAFT_COMPLETE`.

Reviewed Publication Preview r1 authority:

- reviewed production commit: `bb6eacabc86e21da77a91d46d4daa2419be5c988`
- publication candidate status: `READY_FOR_PUBLICATION_PREVIEW`
- candidate SHA: `48684cc5963e54649a78295dc83634ff451537a77c574d9602ed867566da4300`
- repository PDF path: `surveys/weekly/2026-W39/main.pdf`
- candidate-declared repository PDF SHA-256: `4e6bf5131dfb744da648907ddaa8f22102b9fccf3ccf5e1c01e2b335eb4c6a6e`
- byte count: `323893`
- page count: `12`
- Publication Preview shell: `sources/2026-W39/execution/reviews/publication-preview-r1.md`
- dossier: `sources/2026-W39/execution/reviews/publication-preview-r1-dossier.md`

Architecture approval remains valid:

- reviewed Architecture authority: `9767d68e0d83aa667eaeeee6394806c612708682`
- Architecture SHA-256: `b7afb755b04c7d350f43ad99f160df7373645124f2428b37114c4f3bdba94df3`
- canonical Architecture approval: `sources/2026-W39/gates/architecture-approval.json`

## 2. Human requested changes

There are two blocking repair classes.

### RC-1 — Issue #501 reader-facing overtranslation recurrence

Human instruction:

> Sol must identify the terms that need correction and add them to the GitHub terminology list. The next Muse run must use the terminology list to search **all entries, including entries not currently present in W39**, and for every occurrence decide whether it requires replacement or is contextually valid before repairing it.

The generic terminology authority set for this run is the **union** of:

1. `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
2. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`

The W39 supplement was created by Sol after a complete independent read of the W39 reader surface and is tracked back to Issue #501.

Do not use either file as an automatic substitution dictionary.

### RC-2 — Publication PDF byte-binding/provenance defect

Publication Preview r1 states that repository PDF and CI artifact are the exact reviewed bytes.

However, Sol independently downloaded Actions artifact `10946557163` from workflow run `36363430195` and found that the artifact-contained `main.pdf` did **not** hash to the candidate-declared repository PDF SHA.

Observed independent review result:

- candidate/repository sidecar claim: `4e6bf5131dfb744da648907ddaa8f22102b9fccf3ccf5e1c01e2b335eb4c6a6e`
- downloaded Actions artifact `main.pdf`: `a2558be04888ed6e7a68d930d680df6484ebcd68151f8bda127f835d4754d822`
- both observed byte counts: `323893`
- artifact-contained `main.pdf.sha256` still claimed `4e6bf513...`, so the artifact itself was internally inconsistent.

The r2 publication authority must not claim exact-byte identity unless independently demonstrated.

## 3. Invocation preflight guard

The Muse invocation MUST supply the exact current remote branch HEAD/tree that contains this request.

Before any repository write, verify read-only:

- remote `weekly/2026-W39-v2-work` HEAD == invocation Exact Starting SHA;
- that commit contains this exact request file;
- its parent lineage contains Sol terminology supplement commit `7b844cadfb088f43ff187777fb3d9bb96691f77a`;
- reviewed Publication Preview r1 commit `bb6eacabc86e21da77a91d46d4daa2419be5c988` is an ancestor;
- `main` and `production/survey-core-v2` have not been modified by this W39 repair run.

If the branch guard fails, perform no writes and stop with expected/actual SHA/tree.

No new/fallback/repair/review branch. Use the existing W39 branch only.

## 4. First canonical action — record Human REQUEST_CHANGES

Using current reviewed Core Human Gate tooling, canonically record Publication Preview r1 decision:

`REQUEST_CHANGES`

with regeneration boundary:

`DRAFT_COMPLETE`

and bind the decision to the exact r1 reviewed authority above.

The requested-change record must preserve both RC-1 and RC-2, preferably by referencing this execution request verbatim rather than reducing the request to a vague one-line summary.

After recording the decision, use the canonical invalidation/return protocol to return only the affected publication-local downstream authority to `DRAFT_COMPLETE`.

Do not manually fabricate gate/state JSON when canonical tooling exists.

## 5. RC-1 mandatory full-corpus terminology procedure

### 5.1 Enumerate the entire corpus

Parse the complete parent seed and W39 supplement, not merely the W39 examples.

Extract every literal/searchable `observed` form and every explicit observed search form from both files.

The search universe MUST include forms that have **zero occurrences in W39**. This is a hard requirement.

A run that searches only terms currently seen in the PDF is incomplete.

### 5.2 Search all reader-facing canonical surfaces

At minimum search:

- canonical Draft package result fields under `sources/2026-W39/draft/v2/`
- profile synthesis reader-facing fields
- reader-manuscript fields
- generated `surveys/weekly/2026-W39/main.tex`
- all `surveys/weekly/2026-W39/sections/*.tex`
- reader-visible bibliography notes/titles where Japanese normalization may appear
- reader-visible ledger prose where applicable

The authoritative correction must occur at the earliest canonical reader/Draft source supported by Core. Do **not** hand-edit only final PDF bytes.

Generated TeX should be regenerated from corrected canonical Draft/reader authority whenever the pipeline supports it.

### 5.3 Context adjudication for every hit

For every hit, inspect:

1. the exact sentence/paragraph;
2. the intended source technical term/entity;
3. accepted W39 Evidence/authority;
4. whether the Japanese expression is established technical Japanese, an ordinary nontechnical use, or an overtranslation defect.

Choose exactly one:

- `REPLACE`
- `RETAIN_WITH_CONTEXT_REASON`

No blind global replacement.

If the canonical source term is ambiguous from the current sentence, re-read the already accepted source/evidence before deciding. Do not infer a technical identity from generic knowledge when W39 source material does not establish it.

### 5.4 Zero-hit proof

Every corpus search form with no W39 occurrence must be recorded as:

`ZERO_HIT_CHECKED`

This is required evidence that the **whole terminology corpus** was checked, including terms not present in this edition.

### 5.5 Occurrence ledger

Create a durable W39 terminology occurrence ledger under a clear execution path, e.g.:

`sources/2026-W39/execution/terminology/issue501-publication-r2-occurrence-ledger.json`

and, if useful, a human-readable Markdown companion.

Each occurrence record must include at least:

- `seed_source` (`BASE` / `W39_SUPPLEMENT`)
- `observed_form`
- `file`
- `line_or_locator`
- `context_excerpt`
- `canonical_concept`
- `decision`
- `replacement_or_retained_form`
- `reason`
- `source_recheck_required`
- `source_recheck_result`
- `post_edit_validation`

Zero-hit entries must also be present.

### 5.6 W39 supplement is a minimum, not a ceiling

The W39 supplement contains Sol-identified families including, among others:

- `符号の新顔` / code→`符号` misuse
- ML model→`器` / model card→`模型票`
- agent→`使い手` / subagent→`下働き`
- prompt cache→`待ち受け`
- reasoning effort→`強い設定` / `特盛` / `大盛` / `最大`
- dashboard→`盤面`
- cache miss diagnostics→`外したわけを説く道具`
- serving→`給仕`
- kernel/generation loop/mask/stop-check metaphors
- `Cursorの庭`
- `出荷の番人`
- PR→`引き継ぎ`
- feature flag→`旗の上げ下げ`
- release train→`列車の運び`
- benchmark/eval→`物差し`
- community momentum→`景気`
- safety/safeguard metaphor family
- wet lab→`湾岸の濡れ場` / `濡れ仕事`
- grader circularity→`自家の品で自家の物差しを採点する巡り`
- arXiv abstract→`表紙`
- Private AI Compute / enclave / attestation / transparency-log metaphor families
- stealth model→`影の品` family
- API alias/routing→`古い呼び名の求め` family

Do not treat this summary as the search list. The two corpus files themselves are the authority.

### 5.7 Seed-external residual scan

After all known corpus forms have been adjudicated and repaired, perform a fresh full read/search of the resulting reader-facing Japanese for additional coined, metaphorical, Chinese-like, identity-destroying, or non-standard technical wording that is **not yet in either corpus**.

Apply the same semantic test from Issue #501:

> Can a technically literate Japanese reader understand the intended mechanism, product behavior, metric, entity, or limitation without reconstructing the English source phrase?

Any new generalizable defect must be added to the W39 supplement (or an explicitly versioned successor supplement) with canonical concept, preferred direction, classification, rationale, and `auto-rewrite allowed: false`.

Terminology closure is not allowed with unresolved seed-external residuals.

## 6. RC-1 semantic invariants

Terminology repair must not change:

- factual claims;
- numerical values;
- dates/window classification;
- vendor attribution;
- evidence strength;
- benchmark caveats;
- selected/HOLD boundaries;
- X/community-evidence boundary;
- approved seven-package Architecture order/purpose;
- citations or source-entity binding except when necessary to keep a canonical named entity identifiable.

Preserve established Japanese technical terminology. Do not blindly convert all kanji to katakana/English.

Named products/models/benchmarks/datasets/metrics/architecture methods should preserve canonical identity at first use; Japanese explanation may supplement it.

## 7. RC-2 PDF byte-binding repair

After terminology repair and all Draft/reader validation passes:

1. regenerate TeX/PDF using the canonical workflow;
2. compute SHA-256 directly from the exact repository candidate `main.pdf` bytes;
3. generate/recompute `main.pdf.sha256` from those exact bytes;
4. run the CI publication build used as Publication Preview provenance;
5. download the produced Actions artifact independently inside the execution;
6. hash the artifact-contained `main.pdf` itself;
7. hash the artifact-contained `main.pdf.sha256` target and verify it names the same value;
8. compare repository PDF vs sidecar vs artifact PDF.

Required r2 exact-byte invariant:

```text
SHA256(repository main.pdf)
== value in repository main.pdf.sha256
== SHA256(artifact main.pdf)
== value in artifact main.pdf.sha256
```

Byte counts must also match.

Do not declare this PASS from filenames, size equality, workflow success, or a copied sidecar alone.

If the current CI/Core build process is intrinsically nondeterministic such that exact byte identity cannot be made true without Shared Core modification, **do not fabricate a PASS**. Stop and report a blocking Core/CI defect with the exact differing hashes and reproduction steps. Do not modify frozen Shared Core without new Human authority.

## 8. Regenerate publication candidate

Once RC-1 and RC-2 are both actually satisfied:

- rerun required Draft validation;
- regenerate reader manuscript;
- regenerate TeX/Bib as appropriate;
- build the PDF;
- rerun deterministic, semantic-editorial, reader-surface, citation/entity-binding, and visual checks;
- independently render/review the complete PDF, not only first/last pages;
- assemble a fresh publication candidate;
- advance through canonical stages to `RELEASE_CANDIDATE`;
- create fresh Publication Preview **r2** shell + dossier;
- stop at `PUBLICATION_PREVIEW / PENDING`.

Do not Freeze or Release.

Do not infer Human approval.

## 9. Required r2 Human review material

Publication Preview r2 dossier must include:

- exact reviewed commit/tree;
- exact candidate SHA;
- exact repository PDF SHA/bytes/pages;
- exact CI run/artifact IDs;
- exact artifact PDF SHA/bytes;
- explicit equality result for all PDF authority surfaces;
- terminology corpus file SHAs;
- total base-seed search forms;
- total supplement search forms;
- total hits;
- `REPLACE` count;
- `RETAIN_WITH_CONTEXT_REASON` count;
- `ZERO_HIT_CHECKED` count;
- seed-external residual count;
- any newly added generic terminology seeds;
- confirmation that approved Architecture bytes remain unchanged;
- all validation results;
- remaining limitations.

## 10. Repository discipline

Use only:

`weekly/2026-W39-v2-work`

No new branch, fallback branch, repair branch, or review branch.

Normal commits + non-force push only.

No history rewrite, reset, or rebase.

Shared Core, `main`, and `production/survey-core-v2` must not be modified by this execution.

Keep a complete execution/session record under `sources/2026-W39/execution/`.

## 11. Stop conditions

Normal stop:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R2_PENDING`

Blocking stop if any of the following occurs:

- starting authority mismatch;
- canonical Human Gate/invalidation protocol cannot represent the requested boundary;
- terminology corpus cannot be completely enumerated/audited;
- ambiguous source term cannot be resolved from accepted authority without changing evidence;
- PDF repository/sidecar/artifact exact-byte invariant cannot be achieved without frozen Core modification;
- repository integrity failure.

On a blocking stop, report exact evidence and perform no unauthorized workaround.
