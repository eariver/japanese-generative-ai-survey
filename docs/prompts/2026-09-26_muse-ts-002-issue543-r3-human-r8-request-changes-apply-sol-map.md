# TS-002 Issue #543 — Human-authorized r8 REQUEST_CHANGES + Sol-map apply-only execution

Status: `EXECUTION_AUTHORITY / HUMAN_R8_REQUEST_CHANGES / CORE_V2_FROZEN / APPLY_SOL_MAP_ONLY`
Date: 2026-09-26 JST

## 1. Human authority

Human Owner explicitly authorized the next Publication Preview revision after Muse correctly stopped on the Core transition constraint:

> 「はい、承認します。ただし、継続してCore v2自体は改修しないでください。以前Freezeしたところから変更不可です。」

Interpret this narrowly and exactly as:

- authorize creation of the next canonical Publication Preview revision, expected to be `publication-r8`, with decision `REQUEST_CHANGES`;
- regeneration boundary is `DRAFT_COMPLETE`;
- purpose is only to apply the already-decided Issue #543 r2 Sol authoritative terminology map;
- Architecture approval remains valid;
- Publication Preview remains pending after regeneration;
- this is NOT Publication Preview approval;
- Freeze / Release remain unauthorized.

Do not infer any broader Human authority.

## 2. Frozen Core v2 is immutable

The shared Survey Production Core v2 is frozen and MUST NOT be modified.

The current edition state records:

- `implementation.repository_commit_sha = 95c03bf5285cb4b2c1103a14c460574183a8cb93`
- pipeline contract SHA-256 = `ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`
- quality contract SHA-256 = `b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`
- research profile SHA-256 = `0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`
- publication profile SHA-256 = `a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

These values are immutable for this execution.

### Forbidden writes

Do not modify shared/core implementation or shared contracts, including but not limited to:

- `scripts/**`
- `schemas/**`
- `config/**`
- `templates/**`
- `.github/**`
- shared Production Core implementation modules
- shared pipeline/quality/profile contract files

Do not create a Core repair, maintenance patch, compatibility workaround, migration, new schema, new state transition, or alternate transition mechanism.

If the existing frozen Core cannot execute the authorized r8 flow, STOP and report. Do not repair Core.

### Edition-local write allowlist

During Muse execution, repository writes are allowed only under:

- `sources/SP-beyond-text-2026/**`
- `surveys/special/beyond-text-2026/**`

The prompt files and Sol authority files already present before execution are read-only authority and need no further edits.

Before final push, compare changed paths against the starting execution commit. Any changed path outside the two allowlisted roots is a blocker and MUST NOT be pushed.

## 3. Starting guard

Use the exact remote work HEAD/tree and main HEAD/tree supplied in the operator launch message that references this prompt.

Authority must be remote repository state (`git ls-remote origin` + fetch/object readback), not cached/local refs.

If any guard mismatches, zero writes and stop.

After guard PASS, record the following preconditions read-only:

- lifecycle is `RELEASE_CANDIDATE`;
- Architecture review is approved;
- Publication Preview is pending;
- current review index ends at `publication-r7`;
- no `publication-r8` exists;
- current candidate is the 76-page candidate with:
  - PDF SHA-256 `94f6b211b190edd5c5eb685052631be445b50119e3aa3125fe32f007a4f16014`
  - Candidate SHA-256 `77d6be816aaec5a17ddf176cf741d6d563ebaa308f05ccfe9c719f499b1aab7c`.

If these preconditions do not match, stop and report before writing.

## 4. Canonical Human Gate transition

Use ONLY the already-existing frozen Core v2 canonical Publication Preview revision operation — the same mechanism previously used to create r1-r7.

Create the next revision from the actual review index. Expected result is `publication-r8`; do not hard-code r8 if the index unexpectedly differs — instead STOP because the starting precondition would be false.

Required Human decision:

- gate: `PUBLICATION_PREVIEW`
- decision: `REQUEST_CHANGES`
- reviewed_by: `Human Owner`
- regeneration boundary: `DRAFT_COMPLETE`
- reviewed candidate: current 76-page candidate identified in §3
- review reference: Human Owner authorization in the ChatGPT supervision session on 2026-09-26 JST, plus GitHub Issue #543 and Sol authoritative terminology map
- requested changes: apply the Sol authoritative terminology map r2 exactly, with the single Sol-authorized citation-binding correction and no independent editorial reinterpretation

Do not fabricate an APPROVED decision.
Do not manually edit gate/state JSON as a substitute for the canonical operation.
Do not use operator invalidation.
Do not cross Architecture approval.

After the canonical operation, verify read-back that:

- `publication-r8.json` (or the mechanically derived next revision) exists;
- decision is `REQUEST_CHANGES`;
- lifecycle legally returned to `DRAFT_COMPLETE`;
- Architecture approval remains approved;
- no shared Core file changed.

If not, stop immediately.

## 5. Normative editorial authority

Apply exactly:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r2-20260926.md`

Do not reinterpret, broaden, narrow, or substitute its decisions.

Muse is executor/validator only.

For occurrences clearly matching the map's semantic context:

- apply the exact Sol mapping;
- purely grammatical inflection is allowed only when meaning is unchanged.

For any occurrence whose semantic context does not clearly match:

- do NOT decide the wording;
- leave it unchanged;
- record it in:
  `sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r2.md`
  as `CANDIDATE_FOR_SOL_REVIEW`.

New suspicious terminology discovered during the broad scan must also be reported only, not autonomously rewritten unless an existing Sol mapping unambiguously covers it.

## 6. Citation rule

Citation binding is frozen except the one explicit Sol-authorized exception `SOL-CIT-001` in the authoritative map:

- split the EnCodec boundary from DAC `Balanced data sampling`;
- bind the DAC full-band balanced-sampling claim to `btd008` as directed by Sol.

Any other citation change requires STOP + report to Sol.

Maintain 139/139 coverage.

## 7. Frozen semantic scope

Do not alter:

- Issue #529 semantic depth;
- Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture;
- Evidence status or PARTIAL / NEEDS_MORE boundaries;
- technical conclusions;
- numerical meaning or units;
- vendor attribution;
- closed-system boundaries;
- section/subsection architecture;
- bibliography authority set.

`references.bib` must remain byte-identical unless an explicitly existing Sol mapping requires otherwise; currently none does.

## 8. Apply, ledger, and candidate reporting

Update the existing Issue #543 terminology ledger JSON and Markdown views so they reflect Sol decisions and remain synchronized.

Do not convert `CANDIDATE_FOR_SOL_REVIEW` entries into editorial decisions.

Report separately:

- Sol-map entries applied;
- Sol-map entries not found/already satisfied;
- occurrences returned to Sol due to semantic mismatch;
- new suspicious candidates discovered after map application.

## 9. Validation and regeneration

Using only the frozen existing Core v2 implementation:

1. validate the repaired draft;
2. run semantic/editorial and reader-surface validation;
3. verify number/unit semantics and citation coverage;
4. run source broad terminology scan;
5. advance through the existing legal `DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE` path;
6. regenerate exact PDF and Publication Candidate;
7. run rendered-PDF broad terminology scan;
8. run all-page visual regression, including tables, headings, metric names, architecture/component names, two-column boundaries, bibliography transition;
9. verify no clipping, overflow, broken glyphs, or systematic blank pages.

Do not change the Core to make any validation pass.
If the frozen Core rejects an edition-local result, fix only the edition-local content if the fix is already authorized by the Sol map; otherwise stop and return to Sol.

## 10. Core immutability final audit

Before final push, prove:

- `implementation.repository_commit_sha` remains `95c03bf5285cb4b2c1103a14c460574183a8cb93`;
- all four contract/profile hashes in §2 are unchanged;
- no changed path lies outside:
  - `sources/SP-beyond-text-2026/**`
  - `surveys/special/beyond-text-2026/**`;
- no shared Core implementation/schema/config/template file changed.

A failure of any item is a hard blocker. Do not push a violating commit.

## 11. Stop condition

Normal terminal state:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

Equivalent Core state must be:

- lifecycle `RELEASE_CANDIDATE`;
- validation passed;
- publication_preview pending;
- Architecture approved;
- terminal_reason `HUMAN_GATE_REACHED`;
- Freeze pending;
- Release pending.

Do not Freeze.
Do not Release.
Do not merge.
Do not close Issue #543.
Do not create another Human revision after r8.

## 12. Completion report

Report at minimum:

- starting/final remote HEAD + tree;
- main guard;
- r8 canonical review record path/id and read-back;
- evidence that Architecture approval remained intact;
- frozen Core SHA/hash invariants;
- changed-path allowlist audit;
- Sol mapping application counts;
- `CANDIDATE_FOR_SOL_REVIEW` count and exact entries;
- ledger synchronization result;
- citation exception read-back and 139/139 coverage;
- exact PDF pages + SHA-256;
- Candidate SHA-256;
- CI/validation result;
- rendered broad-scan result;
- all-page visual regression result;
- final Core state;
- confirmation that Freeze/Release were not performed.
