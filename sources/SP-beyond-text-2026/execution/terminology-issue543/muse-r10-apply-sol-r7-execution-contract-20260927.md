# TS-002 Issue #543 — Muse r10 apply-only execution contract

Date: 2026-09-27 JST  
Status: `EXECUTION_AUTHORITY / HUMAN_R10_REQUEST_CHANGES / APPLY_SOL_R7_ONLY / FROZEN_CORE_IMMUTABLE`

## 1. Human authority

Human Owner has explicitly approved:

- Publication Preview revision: `r10`
- Decision: `REQUEST_CHANGES`
- Regeneration boundary: `DRAFT_COMPLETE`
- Scope: apply the Sol r7 final independent full-scan authority and the bounded citation corrections `SOL-CIT-003` / `SOL-CIT-004` only.

Architecture approval remains preserved. Publication approval is not granted. Freeze / Release / merge remain unauthorized.

The Human authority is recorded in Issue #543 and must be read back before writes.

## 2. Exact launch guard

Repository: `eariver/japanese-generative-ai-survey`

Existing branch:
`special/beyond-text-2026-work`

Expected remote work HEAD before this contract file was added:
`32314525f642c65b9a80fd3dbb1199d58bc367b3`

This contract file is itself edition-local authority and therefore the launch HEAD for Muse is the branch HEAD that contains this file. Muse must obtain the actual remote branch HEAD/tree with `git ls-remote origin` plus fetched object/tree readback and compare them with the exact values supplied by Sol in the launch message.

Reviewed main authority remains:
- main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
- main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

If any launch guard differs, perform zero repository writes and stop with expected/actual values.

If remote matches and local only is stale, fast-forward only. No reset, rebase, force, new branch, fallback branch, repair branch, or history rewrite.

## 3. Frozen Core v2 — immutable

Core v2 was previously frozen and MUST NOT be modified.

Immutable identities:

Core implementation SHA:
`95c03bf5285cb4b2c1103a14c460574183a8cb93`

Pipeline contract SHA-256:
`ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`

Quality contract SHA-256:
`b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`

Research profile SHA-256:
`0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`

Publication profile SHA-256:
`a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

Verify before and after execution.

Do not modify shared Core scripts, schemas, contracts, config, templates, stage plan, transition rules, compatibility logic, or implementation.

If the frozen Core cannot execute the authorized r10 transition, stop. Do not repair Core.

## 4. Normative editorial authority

Use the existing Sol maps r2 through r6 as frozen prior authority and apply the following new authority exactly:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r7-final-independent-fullscan-20260927.md`

Formal Sol review:

`sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue543-r7-final-independent-fullscan-20260927.md`

Muse is executor/validator only. Do not reinterpret canonical terminology, source meaning, Japanese wording, or citation binding.

If a new suspicious reader-facing term not covered by r2-r7 is discovered, do not edit it. Record exact sentence/section/citation/source-visible canonical English, mark `CANDIDATE_FOR_SOL_REVIEW`, and stop at `DRAFT_COMPLETE` under the same r10 authority.

Do not propose a Japanese replacement in the Muse candidate file.

## 5. Human gate operation

Read back that current state before r10 is `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending` and that publication-r9 is the latest canonical review record.

Using only the existing frozen Core canonical Human Gate operation, record:

- `publication-r10`
- decision: `REQUEST_CHANGES`
- regeneration boundary: `DRAFT_COMPLETE`
- Architecture approval preserved
- Publication approval absent

Do not synthesize any other Human decision.

## 6. Citation authority

Existing bounded citation corrections remain frozen:

- `SOL-CIT-001`: DAC Balanced data sampling -> `btd008`
- `SOL-CIT-002`: Wan2.2 open-weight boundary -> `btd124`

r10 newly authorizes exactly:

- `SOL-CIT-003`: Section 4 SPADE/GauGAN-bound claims -> `btd041`
- `SOL-CIT-004`: Section 4 T2I-Adapter-bound claims -> `btd037`

Apply `SOL-CIT-003/004` semantically/context-bound. Do not perform a blind global key swap.

No other citation addition, deletion, substitution, or rebinding is authorized. If another citation correction appears necessary, stop and return it to Sol.

## 7. r7 application

Apply every r7 editorial decision exactly, including the independent full-text residual classes covering:

- text-modality compounds (`文条件づけ`, `文整合`, `文符号器`, `文枝`, `文類似`, `文品質`, and exact r7-listed grammatical variants)
- prompt/template ensemble and guidance-scale sweep terminology
- reader-facing English residues such as `jointly`, `joint 空間`, `baseline`, `framing` where r7 gives a replacement
- adapter/adaptation terminology currently mistranslated as `適合` where r7 distinguishes adaptation from distributional fit/alignment
- model/evaluation `背骨` -> r7-defined reader-facing `backbone` terminology
- MusicGen tokenizer/codebook terminology
- Music ControlNet source-specific control terminology
- MuSTANGO source-specific music-control network terminology
- Imagen Video source-specific terminology
- Unified-IO source-specific terminology
- all other exact mappings listed in r7

Do not broaden replacements beyond the semantic contexts defined in r7.

## 8. Ledger

Update the Issue #543 terminology decision ledger JSON and Markdown in lockstep.

Add r7 decisions with discovery source:
`SOL_R10_R7_INDEPENDENT_FULLSCAN`

For every r7 row record original, canonical source term, source/Evidence binding, adopted reader-facing wording, REPLACE/RETAIN, rationale, and before/after count.

Final JSON/MD row sets and summaries must be synchronized.

## 9. Pre-validation closure scan

After r7 and citation repairs, before validation, run an independent reader-facing full-source scan over `main.tex` plus headings/tables/front matter/synthesis/reception for:

- all r2-r7 prohibited left-hand-side terms
- #533/#539 frozen zero-count regression terms
- Chinese/overliteral ML compounds
- model/network/component/backbone identity loss
- text/image/video/audio/music modality terminology
- encoder/decoder/attention/adapter/adaptation terminology
- sampling/guidance/flow/solver/distillation terminology
- benchmark/metric identity
- source-specific named mechanisms
- generic English residue where the surrounding Japanese prose should use the r7 canonical rendering

Also verify the citation bindings around Section 4 after `SOL-CIT-003/004`.

### If unresolved candidate count > 0

Do not self-resolve. Record:

`sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r10.md`

and remain at `DRAFT_COMPLETE`. Do not create r11.

### If unresolved candidate count = 0

Proceed with frozen Core through:

`DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE`

and stop at:
`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

## 10. Semantic invariants

Except for r7 reader-facing terminology and SOL-CIT-003/004, preserve:

- Issue #529 longform semantic depth
- technical conclusions
- section/subsection order
- Architecture approval
- Evidence statuses and PARTIAL/NEEDS_MORE/HOLD boundaries
- vendor attribution and closed-system boundaries
- numerical meaning and units
- 139/139 bibliography coverage
- references.bib content unless strictly required by the already-authorized citation key correction (normally no references.bib edit is expected)
- X reception bounded role

## 11. Write allowlist

Writes are limited to:

`sources/SP-beyond-text-2026/**`
`surveys/special/beyond-text-2026/**`

Before push, inspect every changed path from the exact launch commit. If any path is outside the allowlist, do not push; stop and report.

## 12. Validation and rendering

Only when unresolved=0, run:

- deterministic manuscript validation
- semantic/editorial validation
- citation validation
- 139/139 coverage verification
- terminology zero-count/regression scan
- exact PDF build
- rendered-PDF terminology scan
- all-page visual QA
- clipping/overflow/broken-glyph/blank-page/table checks
- bibliography regression

## 13. Final stop and report

Issue #543 remains OPEN. Muse must not close it.

No Freeze, Release, merge, or new Human approval.

Final report must include:

- starting/final HEAD and tree
- main guard
- canonical publication-r10 record/path
- frozen Core implementation SHA and four hashes before/after
- changed-file list and allowlist audit
- r7 application summary and ledger totals
- unresolved candidate count / candidate-file presence
- citation diff proving only SOL-CIT-003/004 were newly changed and SOL-CIT-001/002 preserved
- 139/139 coverage
- semantic invariants
- PDF page count and SHA-256 if regenerated
- candidate SHA-256 if regenerated
- CI/workflow result
- rendered-PDF scan and all-page visual QA
- final lifecycle / Human Gate state
