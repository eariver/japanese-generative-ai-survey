# W38 execution instruction — Publication Preview r1 REQUEST_CHANGES for Issues #511 / #512, edition-local repair only

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / ISSUES_511_512 / NO_CORE_CHANGE / REGENERATE_TO_FRESH_PREVIEW`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W38-v2-work`

## 1. Human decision authority

The Human Owner opened and explicitly directed repair of:

- Issue #511 — `[Publication][W38] TypeSafe Jevの公開日authorityが一次資料とcollector/publicationで不一致`
- Issue #512 — `[Publication][W38] Community observationの25件ledgerがreader-facing surfaceから全件auditできない`

The Human then explicitly instructed Sol:

> Issue #511, #512をCore v2を改修せずに対応してください。

Treat this as the Human Publication Preview r1 decision:

`REQUEST_CHANGES`

The reviewed Publication Preview r1 authority is:

- reviewed repository commit: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61`
- Publication Candidate SHA-256: `43c7d33a457d74b04cbba571e006453f8cea27f4dab134e6265bb55f115ce409`
- exact PDF:
  - path: `surveys/weekly/2026-W38/main.pdf`
  - SHA-256: `767f4d98c366ae3c7247da635a6ea0b68753f58327104287ab4fb9d8ec9a2543`
  - bytes: `344241`
  - pages: `11`
- Human Preview r1 shell:
  - `sources/2026-W38/execution/reviews/publication-preview-r1.md`
- Human Preview r1 dossier:
  - `sources/2026-W38/execution/reviews/publication-preview-r1-dossier.md`
- independent Sol review:
  - `sources/2026-W38/execution/reviews/sol-w38-publication-preview-r1-independent-review-20260919.md`

The independent Sol review originally found the r1 bytes otherwise publishable. Issues #511 and #512 are now the explicit Human change request and supersede that prior PASS for the purpose of the Human gate.

## 2. Allowed regeneration boundary

Use canonical Publication Preview `REQUEST_CHANGES` with regeneration boundary:

`ARCHITECTURE_ESTABLISHED`

Reason:

- both repairs affect Draft/publication provenance and reader surface;
- #511 requires a corrected temporal authority supplement beneath Draft;
- #512 requires a new reader-auditable public ledger surface;
- neither changes event identity, W38 ordinary-window membership, materiality, selection, package identity, package order, or the approved seven-package Architecture.

Therefore:

- **do not rerun Discovery;**
- **do not rerun Screening;**
- **do not rerun Materiality;**
- **do not rerun Completeness;**
- **do not rerun Selection;**
- **do not regenerate or modify Architecture;**
- preserve canonical Human Architecture approval.

The existing accepted collector/Evidence/Architecture bytes are historical authority and must not be silently rewritten after approval. Repair temporal provenance by append-only edition-local correction authority as specified below.

If current canonical gate implementation requires an earlier boundary that would invalidate Architecture approval, STOP and report the limitation. Do not bypass the gate and do not modify Core.

## 3. Mission

1. Guard exact repository state.
2. Canonically record Human Publication Preview r1 `REQUEST_CHANGES` for Issues #511/#512 with boundary `ARCHITECTURE_ESTABLISHED`.
3. Repair #511 by creating an append-only TypeSafe/Jev temporal correction authority that explicitly distinguishes:
   - first-party blog displayed publication date;
   - separate founder/creator public launch announcement timing.
4. Repair #512 by publishing a reader-facing 25-row community-observation manifest derived from the canonical row-level X ledger and Sol count correction.
5. Regenerate Draft/publication reader surfaces from the approved Architecture plus the two edition-local correction authorities.
6. Regenerate exact PDF through the canonical CI/pipeline path.
7. Re-run all required deterministic/semantic/editorial/visual checks.
8. Produce fresh Human Publication Preview r2 `PENDING`.
9. STOP.

No Freeze.

No Release.

No Human Preview r2 decision.

## 4. Invocation starting guard

The Muse invocation MUST provide the Exact Starting SHA/tree corresponding to the commit containing this request.

Before any production write, read-only verify:

- remote W38 HEAD == Exact Starting SHA supplied by invocation;
- remote W38 tree == Exact Starting Tree supplied by invocation;
- Exact Starting SHA parent == `a578063bd611a0b127aec9c58b280e63b2cdb858`;
- parent tree == `968370d29b84957ae61cc32389f298b77cf62faa`;
- remote `main` == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- main tree == `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
- remote `production/survey-core-v2` == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current W38 lifecycle == `RELEASE_CANDIDATE`;
- current next_action == `PUBLICATION_PREVIEW`;
- Architecture Human gate == `approved`;
- Publication Preview Human gate == `pending`;
- current r1 Candidate/PDF identities match §1;
- Architecture SHA remains `c123f9af386d0c85e0abc41f4fd91ada7807b6a42816718f1c4e02a01ae5bc48`;
- Architecture review-summary SHA remains `e286edc9817584c23996f160c0d6f8dbd3b6336e698976ce928e937dacd7969b`;
- Architecture review-attention SHA remains `044545e97c2e161144a5e78150a0d825573b6ccd229e13aac90aaa21b00e3e09`.

Mismatch -> zero production writes, report expected vs actual, STOP.

If local clone is stale, use the existing bounded fetch + fast-forward-only sync authority. Do not use stale local `main` as authority.

No new branch.

No force/reset/rebase/squash/history rewrite.

## 5. Shared-Core freeze — mandatory

The Human explicitly requested repair **without Core v2 modification**.

Zero writes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Do not modify:

- `main`
- `production/survey-core-v2`

Do not open a Core repair PR as part of this execution.

Generic carry-forward observations may be documented edition-locally or left on Issues #511/#512, but implementation is W38-only.

## 6. Mandatory read order

Read at minimum:

1. this request;
2. Issue #511;
3. Issue #512;
4. `sources/2026-W38/execution/reviews/publication-preview-r1.md`;
5. `sources/2026-W38/execution/reviews/publication-preview-r1-dossier.md`;
6. `sources/2026-W38/execution/reviews/sol-w38-publication-preview-r1-independent-review-20260919.md`;
7. `sources/2026-W38/gates/review-index.json`;
8. current Human Gate CLI/help;
9. `sources/2026-W38/collectors/primary/runs/20260919T000000Z/typesafe-jev-20260915.md`;
10. accepted Evidence containing `w38-primary-typesafe-jev-20260915`;
11. `sources/2026-W38/architecture-v2.json` — read-only;
12. `sources/2026-W38/external/x/weekly-x-2026-W38/raw/grok-x-result-r2.md`;
13. `sources/2026-W38/execution/reviews/sol-grok-x-r2-review-20260919.md`;
14. current W38 Draft and reader-facing TeX/Bib;
15. current Publication Candidate and reader-surface validation files.

## 7. Canonically record Human Preview r1 REQUEST_CHANGES

Use the current canonical Human Gate protocol.

Required semantics:

- gate: `PUBLICATION_PREVIEW`
- decision: `REQUEST_CHANGES`
- reviewed repository commit: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61`
- reviewed_by: `Human Owner`
- requested changes:
  - Issue #511 TypeSafe/Jev temporal-authority correction;
  - Issue #512 full community-ledger reader auditability;
- regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- review reference must bind:
  - Issues #511/#512;
  - Publication Preview r1 shell/dossier;
  - this execution request;
  - explicit Human instruction quoted in §1.

Determine canonical revision from repository state. Do not infer from filenames.

Use actual system wall clock for `reviewed_at`.

After record/write/commit, read back:

- review record;
- review index;
- exact reviewed commit;
- requested changes;
- boundary;
- resulting lifecycle/state.

If canonical Human Gate protocol refuses this decision/boundary, STOP. Do not hand-edit Human Gate JSON.

## 8. Issue #511 — independently established temporal model

Sol independently re-read the current TypeSafe first-party page:

`https://typesafe.ai/blog/introducing-system-one-models-and-jev`

Current displayed first-party page date:

`Sep 14, 2026`

The page also says Jev is available/released “today”.

The canonical W38 X ledger separately contains:

`https://x.com/CompleteSkeptic/status/2099925682726002904`

Snowflake UTC:

`2026-09-15T18:17:52.151Z`

The ledger identifies `@CompleteSkeptic` as TypeSafe AI CEO / Jev creator and retains this row as the Jev launch announcement.

External public corroboration available at repair time also reproduces the founder post as a Sep 15 launch announcement. However the authoritative W38 correction should bind directly to:

1. the TypeSafe first-party blog page for the displayed **blog publication date**; and
2. the direct founder/creator X post already in the accepted W38 ledger for the distinct **public launch announcement time**.

### Required normalized model

Do not collapse these into one date.

Represent at minimum:

- `blog_displayed_publication_date = 2026-09-14`
- precision: `DAY`
- authority: TypeSafe first-party blog page
- `founder_launch_announcement_at = 2026-09-15T18:17:52.151Z`
- authority: direct public X status by Diogo Almeida / `@CompleteSkeptic`
- relationship: distinct public launch announcement; not the blog publication-date field
- W38 relation: both are within ordinary W38 window
- event identity/materiality/selection/package identity: unchanged

Do not speculate about why the blog date and launch post date differ.

Do not silently reinterpret one as timezone conversion unless an authoritative source explicitly establishes that.

## 9. #511 append-only correction artifacts

Do not overwrite historical approved bytes solely to erase the mistake.

Create edition-local append-only correction authority, at minimum:

### Collector correction

Create a new corrected/supplemental collector record, e.g.:

`sources/2026-W38/collectors/primary/corrections/typesafe-jev-temporal-correction-20260919.md`

It must:

- bind the original collector record by path + SHA;
- state that original `published_date_on_page: Sep 15, 2026` is invalid as the blog displayed-date authority;
- record the current displayed Sep 14 date;
- separately bind the Sep 15 founder launch status URL + exact Snowflake UTC;
- preserve all non-temporal technical claim boundaries;
- state original collector filename/date suffix is historical/non-authoritative and is not being rewritten.

### Evidence correction

Create a machine-readable edition-local Evidence temporal supplement, e.g.:

`sources/2026-W38/evidence/v2/corrections/typesafe-jev-temporal-correction-r1.json`

It must:

- bind the accepted Evidence package/record containing `w38-primary-typesafe-jev-20260915`;
- identify exactly which temporal statements are superseded;
- provide the normalized two-date model from §8;
- state all non-temporal Evidence claims remain unchanged;
- state W38 ordinary-window membership unchanged;
- state no materiality/selection/Architecture change required.

If repository conventions already provide a canonical edition-local correction mechanism, use that instead.

Do not modify shared schemas/scripts to add one.

### Architecture treatment

Do **not** modify approved Architecture bytes.

Where Architecture contains the old “Sep 15 date” limitation, treat that temporal phrase as superseded for downstream Drafting by the explicit #511 correction authority.

Document this supersession in the repair session and r2 Preview dossier.

No Architecture Human gate reopen is required because event identity, package identity, materiality and W38 membership are unchanged.

If current Core cannot support this without modifying Architecture, STOP and report rather than bypassing.

## 10. #511 reader-facing corrections

Regenerated publication must no longer present the TypeSafe blog itself as a Sep 15 publication.

Use wording semantically equivalent to:

- TypeSafe blog: `9月14日付`
- founder/creator launch announcement: `9月15日`

Where a single date is unnecessary, prefer prose that avoids collapsing the dates.

Update consistently:

- Draft package/result as regenerated downstream output;
- This Week in AI/frontmatter chronology;
- Jev section;
- Week in Review;
- Sources & Limitations;
- bibliography metadata;
- temporal notes;
- any candidate-facing reader manuscript metadata.

Bibliography date for the TypeSafe blog must reflect the first-party page date Sep 14.

If the Sep 15 founder launch post is used to support launch timing, cite the direct public X status separately and clearly as launch/announcement provenance, not as the blog's publication date.

Temporal confidence for the blog remains day-level.

## 11. Issue #512 — public community ledger manifest

Create an edition-local reader-facing public manifest:

`surveys/weekly/2026-W38/community-observation-ledger.md`

or another clearly publication-facing W38 path if existing convention dictates.

This manifest must expose all 25 accepted public X rows without exposing internal candidate/pipeline state.

Required columns:

- row number;
- account;
- role: `OFFICIAL`, `INDEPENDENT`, or `COMMUNITY`;
- direct canonical public X status URL;
- Snowflake-derived UTC;
- public temporal class:
  - `ORDINARY_WINDOW`
  - `LATE_BREAKING`

Do **not** include:

- candidate IDs;
- Screening/Selection/Evidence states;
- lane IDs;
- discovery-origin internals;
- private paths;
- worker notes;
- internal review state.

Manifest header must state:

- W38 ordinary window:
  `[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`
- total rows: 25
- ordinary: 23
- late-breaking: 2
- pre-window: 0
- time-unverified: 0
- X/community observation is context-only and establishes no technical specifications, performance, price, license, availability, safety, or source-publication date by itself.

### Count authority

The row-level 25-row ledger is authoritative.

Derived role/account counts must use the independent Sol correction, not the stale r2 summary prose:

- ordinary unique accounts: 15
- INDEPENDENT: 7
- OFFICIAL: 3
- COMMUNITY: 5

Do not repeat the stale raw-summary `16 / 7+3+6` values.

## 12. #512 stable reader citation

The full 25-row manifest must be reader-followable from the publication.

Preferred procedure:

1. create manifest;
2. commit + non-force push;
3. read back remote commit containing exact manifest bytes;
4. construct a **commit-pinned GitHub URL** for that manifest;
5. use that commit-pinned URL in the reader-facing bibliography/source note;
6. keep the existing 9 representative direct X status citations for concise thematic examples.

The exact `25 / 23 / 2` claim must cite or directly point readers to the full manifest.

Do not use:

- an internal `sources/.../raw` path as the reader citation;
- a private/unresolvable path;
- a branch-only mutable URL if a commit-pinned URL is practical;
- a GitHub path that exposes candidate/Screening/Selection internals.

The publication-facing manifest itself may live in the public survey directory.

## 13. Existing Grok/X raw inconsistency

The accepted raw r2 row table contains 25 correct unique status rows and the correct temporal class total 23 ordinary / 2 late.

Its later run-health prose contains stale derived account totals:

- `ordinary unique accounts: 16`
- `ordinary COMMUNITY accounts: 6`

Independent Sol correction established:

- 15 ordinary unique accounts
- 7 independent
- 3 official
- 5 community

Do not rewrite the historical Grok raw.

The new public manifest must be derived from the row-level ledger and Sol-corrected arithmetic.

The r2 Preview dossier must disclose this provenance clearly.

## 14. Publication regeneration

After canonical REQUEST_CHANGES and creation of the two repair authorities:

- regenerate Draft/publication from `ARCHITECTURE_ESTABLISHED`;
- preserve the seven approved packages and order;
- no new technical research beyond TypeSafe temporal re-read needed for #511;
- no new X collection needed for #512;
- preserve all prior vendor-claim and community-context boundaries;
- regenerate reader manuscript, quality bundle, semantic/editorial review, visual review, reader-surface gate, publication candidate and PDF through current edition-local pipeline.

Do not patch final PDF bytes.

## 15. Required #511 assertions before r2 Preview

Before creating r2 Preview, verify:

- TypeSafe blog displayed date in correction authority == Sep 14, 2026;
- direct founder launch status URL is bound separately;
- founder status Snowflake UTC == `2026-09-15T18:17:52.151Z`;
- no reader-facing sentence calls the TypeSafe blog itself “Sep 15 publication”;
- bibliography TypeSafe blog date == Sep 14;
- if Sep 15 is stated, it is labeled as founder/creator launch announcement;
- W38 membership remains ordinary;
- no event identity/package/Architecture change;
- no stale Sep 15-only temporal model remains in regenerated Draft/publication surfaces.

## 16. Required #512 assertions before r2 Preview

Verify:

- manifest has exactly 25 unique direct X URLs;
- exactly 23 rows `ORDINARY_WINDOW`;
- exactly 2 rows `LATE_BREAKING`;
- no duplicate status ID/URL;
- every manifest UTC matches Snowflake-derived UTC in canonical row ledger;
- no internal candidate/Screening/Selection/Evidence vocabulary in manifest;
- reader publication exposes a commit-pinned public URL to manifest;
- exact 25/23/2 statement is auditable from that URL;
- 9 representative X citations remain valid;
- X remains context-only.

## 17. Timestamp provenance

Issue #507 remains active generic Core debt.

All **new** Human/Worker review/provenance records must use actual timezone-aware wall clock.

Never copy invalid Production State history timestamps into Human-facing chronology.

After each review-surface commit/read-back:

- new record timestamp <= containing commit timestamp;
- new record timestamp <= actual system wall clock.

If not, mark surface not presentable and repair append-only before proceeding.

Existing invalid historical state times remain governed by existing W38 correction ledgers.

## 18. PDF / visual check

Regenerated exact PDF must be independently/rendered-reviewed by Worker before r2 handoff.

Check all pages for:

- clipping;
- overlap;
- garbled Japanese;
- citation/bibliography breakage;
- source-note overflow;
- layout holes;
- p.8 closing-page behavior.

Do not reintroduce the original #508 orphan-box defect.

## 19. Issue closure discipline

Do not close #511 or #512 merely because files were edited.

At normal stop:

- leave both Issues open;
- report exact evidence that each Acceptance Criteria item is satisfied;
- Sol will independently read back r2 and decide whether to close/comment the issues.

## 20. Fresh Human Publication Preview r2

Create:

- `sources/2026-W38/execution/reviews/publication-preview-r2.md`
- `sources/2026-W38/execution/reviews/publication-preview-r2-dossier.md`

They must bind:

- new exact reviewed repository commit;
- new Publication Candidate SHA;
- new PDF SHA/bytes/pages;
- #511 correction authority paths/hashes;
- #512 public manifest path/hash + commit-pinned public URL;
- canonical r1 Human REQUEST_CHANGES record;
- Architecture approval retained;
- no Core changes;
- no Human r2 decision.

Human r2 decision:

`PENDING`

## 21. Normal stop condition

Successful stop:

- r1 Human Publication Preview canonically `REQUEST_CHANGES`;
- regeneration boundary `ARCHITECTURE_ESTABLISHED`;
- Architecture approval retained;
- #511 corrected via append-only temporal authority + regenerated reader publication;
- #512 corrected via full public ledger manifest + publication citation;
- new Candidate ready;
- regenerated PDF ready;
- all required checks pass;
- fresh Human Publication Preview r2 exists;
- r2 Human decision `PENDING`;
- Freeze pending;
- Release pending;
- shared-Core changed paths = 0;
- main unchanged;
- Production Line unchanged;
- Issues #511/#512 remain open pending independent Sol verification.

Then STOP.

## 22. Final report

Report at least:

- invocation Starting SHA/tree;
- canonical r1 REQUEST_CHANGES review revision/path/hash/reviewed_at;
- regeneration boundary;
- #511:
  - first-party blog displayed date;
  - founder launch announcement URL/time;
  - correction collector path/hash;
  - Evidence temporal supplement path/hash;
  - affected regenerated reader surfaces;
- #512:
  - manifest path/hash;
  - manifest-containing commit;
  - commit-pinned public URL;
  - 25/23/2 and 15=7+3+5 reconciliation;
- Architecture unchanged SHA;
- seven packages/order unchanged;
- new Draft identity;
- new Candidate SHA;
- new PDF path/SHA/bytes/pages;
- semantic/editorial/visual/reader-surface results;
- timestamp provenance result;
- ending HEAD/tree;
- current lifecycle / next action / terminal reason;
- r2 Preview shell/dossier paths;
- Human r2 status = `PENDING`;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0;
- Issues #511/#512 left open for Sol verification.
