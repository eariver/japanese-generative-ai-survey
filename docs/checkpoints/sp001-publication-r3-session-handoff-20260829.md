# SP001 Publication r3 — session handoff (2026-08-29 JST)

## Purpose

This checkpoint is the authoritative session handoff for continuing SP001 Core v2 production after the 2026-08-28/29 chat session reached its message limit.

The next session should **resume from the current `special/SP001-v2-work` branch**, verify the repository state again, and continue only the unfinished publication-authority / Publication Preview work described below.

The most important boundary is:

> **The SP001 r3 reader source and exact 14-page PDF are complete and visually reviewed, but the canonical publication authority chain under `sources/SP001/publication/v2/` is still the stale r2 chain bound to the old 13-page PDF.**

Do not regenerate research, screening, evidence, selection, Architecture, or Draft content unless a new concrete defect is discovered. Do not Freeze or Release before explicit Human Publication Preview approval.

---

## 1. Repository / branch snapshot before this checkpoint document

Repository:

`eariver/japanese-generative-ai-survey`

Canonical SP001 work branch:

`special/SP001-v2-work`

Production snapshot commit immediately before this handoff document was added:

`c8b693c20244ac1ef871366c16fb6e7732d08c24`

Tree:

`1690d55e378cf1ecd7da205bb8f4178a6fdd5575`

Commit message:

`Rebuild SP001 Publication r3 after visual pagination repair`

Current `main` at handoff:

`7f3bc0f65f5cf11ffd559fde37f3f5dff90a9be9`

Main tree:

`b87e0d3717460eb9f04bb7485de3a46d687253e2`

That `main` commit is the Human-approved merge of PR #475:

`Core v2: require LONGFORM mixed-layout visual review (#475)`

The checkpoint-document commit created after `c8b693...` is documentation-only and must not be confused with a new reader/PDF production revision. On resume, re-fetch the branch and verify that the only change after `c8b693...` is this checkpoint file unless subsequent work has intentionally advanced the branch.

---

## 2. Human / Core history that controls the current work

### Issue #400 Human Publication Preview decision

SP001 previously reached Publication Preview, but Human review rejected the regenerated candidate. The operative decision is **REQUEST_CHANGES**, not approval.

The blocking concerns evolved through the subsequent repair work, but the remaining publication-quality requirements relevant to r3 are:

1. ordinary narrative must use the normal Special mixed-layout identity rather than collapsing to full-width one-column prose;
2. each model family must preserve family-local technical depth rather than a compressed topic-presence summary;
3. cross-family comparison must be readable rather than an over-dense wide table;
4. final synthesis must remain an independent reader-facing synthesis, not merely a production-oriented checklist.

The prior Human decision must not be reinterpreted as approval. Freeze / Release remain prohibited until a new explicit Human Publication Preview approval is recorded.

### Approved Architecture remains authoritative

Architecture Review remains approved. The r2 approved Architecture is still the authority for the regenerated Draft:

- 6 packages;
- soft target: 18 pages;
- maximum: 24 pages;
- final package: `PKG-6-FRONTIER-SYNTHESIS`.

The current 14-page result is below the soft target but is not automatically defective. Page count is an outcome, not a padding quota.

### Shared-Core repairs already completed

The relevant shared-Core repairs were handled separately and merged only after Human approval / fixed-head audit. In particular:

- PR #473 repaired LONGFORM reader substantive-fidelity / depth validation behavior.
- PR #474 repaired historical Publication Preview rejection recording so a historical candidate rejected by current validation can still be canonically rejected while exact reviewed bytes remain bound.
- PR #475 added the LONGFORM mixed-layout visual-review requirement triggered by Issue #400.

Do not reopen Core maintenance unless the current r3 authority-generation path exposes a genuinely shared defect. Edition-local production should use the current `main` Core as source of truth.

---

## 3. PR #472 is transport only — NEVER MERGE

PR #472:

`Survey Core operator transport: SP001 Publication revision r1`

At handoff it is:

- open;
- unmerged;
- mergeable;
- base: `main`;
- base SHA: `7f3bc0f65f5cf11ffd559fde37f3f5dff90a9be9`;
- head: `special/SP001-v2-work`;
- head SHA before this checkpoint commit: `c8b693c20244ac1ef871366c16fb6e7732d08c24`.

Its own body states that it is execution transport only and **NEVER MERGE**.

This prohibition remains standing. Do not merge PR #472 even when SP001 later reaches Publication Preview or Release.

---

## 4. Current Production State

`sources/SP001/production-state.json` currently remains:

- `research_profile`: `THEMATIC`
- `publication_profile`: `LONGFORM_SPECIAL`
- `lifecycle_state`: `DRAFT_COMPLETE`
- Architecture Human Gate: `approved`
- Publication Preview Human Gate: `pending`
- validation checkpoint: `pending`
- publication preview checkpoint: `pending`
- next action: `stage:reader-publication-validation`

Therefore the repository has **not yet canonically transitioned the r3 reader/PDF through publication validation**.

Do not hand-edit Production State. Advance it only through the current Core v2 canonical APIs / orchestration path after the r3 authority chain passes validation.

---

## 5. Exact r3 reader / PDF already completed

### Reader source basis

Canonical reader source:

`surveys/special/SP001/main.tex`

Exact r3 source SHA-256 recorded by the final build audit:

`838d1fbb5618b447b7f13334c5e67bc55cfca7613dbf7f492e6ae29fe128026a`

Source-basis repository commit recorded by the build audit:

`9902583868f542dd55e7f60b70010a6ec5d62d1a`

The later canonical production snapshot commit `c8b693...` contains the rebuilt PDF and r3 build audit after the bounded pagination repair.

### Exact PDF

Path:

`surveys/special/SP001/main.pdf`

Exact r3 PDF properties:

- page count: **14**
- byte count: **322,591**
- SHA-256: **`ef68866d51c7e552813c995b1b47745cfa125cfcf8dd71d3b6f54997a62e0f38`**
- TeX Live: 2026
- engine: LuaLaTeX / latexmk
- final build audit status: `PASS`
- blocking build-log findings: none

Build audit:

`sources/SP001/publication/v2/pdf-build-audit-r3.json`

### Bounded pagination repair already applied

An earlier r3 build had a 15th page containing only the final bibliography tail. This was repaired by a bounded one-column bibliography compaction. The final result is 14 pages, with the Reader verification matrix and References fitting on page 14.

Do not restore the orphan page merely to increase page count.

### Known non-blocking TeX warnings

The final build audit records several 8.99994pt `Overfull \\hbox` findings around table-like wide surfaces. They were not classified as blocking because every final PDF page was visually inspected and no clipping / overlap / broken glyph / unreadable overflow was observed.

Do not treat these log lines alone as a reason to regenerate the PDF. Reopen layout only if exact-PDF inspection or a current validator demonstrates a real publication defect.

---

## 6. Final r3 visual QA result

All 14 pages of the exact PDF were re-reviewed after the pagination repair and judged **PASS**.

Observed layout:

- ordinary narrative: balanced two-column;
- source-backed Technical Notes: full-width;
- wide comparison / synthesis surfaces: full-width;
- final synthesis: full-width where appropriate;
- References: one-column;
- no clipping;
- no overlap;
- no broken glyphs;
- no near-empty internal/final page;
- previous page-15 orphan removed.

### Core #475 mandatory LONGFORM visual evidence

For a normal `LONGFORM_SPECIAL`, PR #475 requires a `LONGFORM_MIXED_LAYOUT` Visual check with these exact evidence locations:

- `reader-layout:balanced-two-column-narrative`
- `reader-layout:wide-surfaces-full-width`
- `reader-layout:references-one-column`

SP001's approved Architecture does **not** authorize a nonstandard narrative-column exception, and no exception is needed. Therefore do not use `reader-layout:architecture-approved-narrative-exception` for this candidate.

The final 14-page PDF has already been visually judged to satisfy all three normal markers. The fresh r3 Visual Review should record them against the exact r3 PDF, not copy the old r2 Visual Review mechanically.

---

## 7. r3 semantic / depth result already judged

The exact PDF is 14 pages versus the approved Architecture soft target of 18. This was explicitly reviewed and judged substantively acceptable because the regenerated r3 reader contains the required depth rather than merely being short:

- all 6 Architecture packages are represented;
- DeepSeek retains family-local chronology and technical transitions (LLM -> V2 -> R1 -> V4), including model/active scale, MLA/DeepSeekMoE, RL staging, context/agentic endpoint distinctions;
- Qwen retains family-local model breadth, distribution, quantization/fine-tuning/deployment, Qwen3.8 agent/coding/research positioning, and license boundaries;
- GLM and Kimi likewise retain family-local technical/system depth;
- each major family has source-backed Technical Notes;
- the former over-dense cross-family comparison was split into readable comparison surfaces;
- `PKG-6-FRONTIER-SYNTHESIS` remains an independent final synthesis with explicit comparison axes and reader-facing role.

Therefore **do not pad the report simply to reach 18 pages**.

The fresh r3 semantic/editorial review must explicitly bind the current below-target substantive decision with these exact evidence markers required by the repaired Core contract:

- `page-plan:14/18`
- `density-review:below-target-substantive`

It must also continue to bind all package/block-level depth evidence and the final synthesis reader role required by current Core v2. Generate this review from the exact r3 reader/source state; do not merely edit the old r2 hash fields.

---

## 8. Critical stale-authority boundary

Although the r3 reader and PDF are complete, the following files under `sources/SP001/publication/v2/` are still **stale r2 authority** and must be regenerated:

- `reader-manuscript-v2.json`
- `quality-regression-bundle-v2.json`
- `quality/` result chain as required by current generator/validator
- `semantic-editorial-review-v2.json`
- `visual-review-v2.json`
- `publication-candidate-v2.json`

The current stale Publication Candidate proves this clearly. It is still bound to:

- PDF SHA-256: `590a53e11934ae25176050e5105b59a2bb09eda4b045e9b211b486e5be90ba2b`
- byte count: 300,377
- page count: 13

That old candidate is historical r2 authority. It must **not** be presented as the new Human Preview candidate and must not be relabeled as r3 without regenerating the complete authority chain.

The old Reader Manifest, Quality Bundle, Semantic Review, and Visual Review similarly bind the old source/PDF bytes and are not valid evidence for the r3 exact PDF.

---

## 9. Exact next work to perform

Resume at publication validation, not at Draft authoring.

### Step 1 — Reconfirm repository identity

At the beginning of the next session:

1. fetch current `main`;
2. fetch `special/SP001-v2-work`;
3. read this checkpoint;
4. compare the current branch with production snapshot `c8b693c20244ac1ef871366c16fb6e7732d08c24`;
5. confirm any intervening change is understood before writing production authority.

If the only intervening commit is this checkpoint file, proceed. If production files changed, investigate before continuing.

### Step 2 — Reconfirm exact r3 bytes

Before generating authority, verify:

- `surveys/special/SP001/main.tex` SHA-256 = `838d1fbb5618b447b7f13334c5e67bc55cfca7613dbf7f492e6ae29fe128026a`
- `surveys/special/SP001/main.pdf` SHA-256 = `ef68866d51c7e552813c995b1b47745cfa125cfcf8dd71d3b6f54997a62e0f38`
- PDF byte count = 322,591
- PDF page count = 14
- `pdf-build-audit-r3.json` remains `PASS` with zero blocking findings.

If these exact bytes differ, do not blindly reuse this checkpoint's authority instructions; determine why the artifact changed.

### Step 3 — Generate a fresh r3 Reader Manifest

Use the current Core v2 reader/publication API. Regenerate `reader-manuscript-v2.json` from the exact r3 source rather than manually updating its hashes.

The manifest must bind the exact current reader source blocks, all six packages, and the final synthesis location/role expected by current Core validation.

### Step 4 — Generate the deterministic Quality Bundle

Regenerate the quality result chain and `quality-regression-bundle-v2.json` against the fresh r3 Reader Manifest and exact r3 PDF/source as required by current Core.

Do not reuse old PASS statuses when their artifact hashes point to r2.

### Step 5 — Generate fresh Semantic / Editorial Review

Generate `semantic-editorial-review-v2.json` against the exact r3 reader/PDF.

Required r3-specific evidence includes at least:

- all current LONGFORM package/block depth bindings;
- final package / final reader synthesis role bindings;
- `page-plan:14/18`;
- `density-review:below-target-substantive`.

The semantic judgment is already made in this session: 14 pages are acceptable because depth is substantive; no padding is required. The next session should materialize that judgment into the canonical review structure and let the current validator verify it.

### Step 6 — Generate fresh Visual Review

Generate `visual-review-v2.json` against the exact 14-page r3 PDF.

Record the `LONGFORM_MIXED_LAYOUT` check and all three exact normal-layout evidence locations:

- `reader-layout:balanced-two-column-narrative`
- `reader-layout:wide-surfaces-full-width`
- `reader-layout:references-one-column`

Also retain the normal exact-PDF visual checks for typography, clipping, overlap, broken glyphs, page balance, etc. The decision is PASS based on the completed 14-page visual inspection.

### Step 7 — Generate fresh Publication Candidate

Only after Reader Manifest, Quality Bundle, Semantic Review, and Visual Review are all fresh and valid, generate `publication-candidate-v2.json` through the current Core API.

The candidate generator must revalidate:

- exact source bytes;
- exact PDF bytes;
- page count;
- manifest hash;
- quality bundle hash;
- semantic review hash;
- visual review hash.

Expected PDF binding if no artifact changes occurred:

- SHA-256 `ef68866d51c7e552813c995b1b47745cfa125cfcf8dd71d3b6f54997a62e0f38`
- 322,591 bytes
- 14 pages.

### Step 8 — Run current Core validation and canonical state transition

Run the current `main` Core validator / orchestration path from the work branch. Do not bypass a failing validator by hand-editing JSON.

If a failure reflects a real r3 semantic/visual defect, repair the edition at the smallest justified boundary and regenerate all descendant authority.

If a failure instead exposes a general shared-Core defect, stop SP001 production, classify it as shared maintenance, repair Core separately, complete the fixed-head audit / Human approval process, merge it, then resume SP001. Do not special-case SP001 inside Core.

On success, let Core perform the valid lifecycle transition from `DRAFT_COMPLETE` to the next canonical publication-validation state (expected to include `VALIDATED_DRAFT` under the present lifecycle; verify current code rather than hand-coding the transition).

### Step 9 — Prepare Human Publication Preview artifact / gate

After the fresh r3 Publication Candidate is valid and the lifecycle is at the correct pre-Human gate state:

1. prepare/export the exact r3 Human Publication Preview artifact using the existing Core/publication-preview path;
2. bind the exact candidate/PDF bytes and repository commit required for durable Human review;
3. let the Human Gate review index determine the correct next Publication Preview revision number rather than guessing it;
4. stop at the Human Publication Preview Gate.

Do **not** record Human approval yourself.

---

## 10. Stop conditions / prohibitions

The next session must preserve all of the following:

- **NO Freeze** before explicit Human Publication Preview approval.
- **NO Release** before explicit Human Publication Preview approval and subsequent valid freeze path.
- **NEVER MERGE PR #472.**
- Do not infer or manufacture a Human gate decision.
- Do not reopen approved Architecture merely because the final report is 14 pages rather than the 18-page soft target.
- Do not pad pages to meet the soft target.
- Do not use the prior 19-page version as current technical authority. It may only be treated as historical quality/layout reference; the approved current Architecture, accepted Evidence, r3 Draft Results, and exact r3 reader are authority.
- Do not reuse stale r2 publication hashes/reviews for r3.
- Do not hand-edit Production State or gate records to force progression.
- Do not create a generic command / Human-decision execution surface.
- If a shared-Core problem is found, separate maintenance from edition production and require the normal Core fixed-head audit + explicit Human approval before merge.

---

## 11. Recommended first instruction in the next chat

A concise continuation prompt can be:

> `eariver/japanese-generative-ai-survey` の `special/SP001-v2-work` を確認し、`docs/checkpoints/sp001-publication-r3-session-handoff-20260829.md` を参照してSP001編纂を続行してください。現在のmain/branch/headとexact r3 PDF bytesを再確認してから、fresh r3 publication authority chainを生成し、Core validatorを通してHuman Publication Preview Gateまで自律的に進めてください。Freeze/Releaseは禁止、PR #472は絶対にmergeしないでください。

---

## 12. Handoff summary

At handoff, the substantive editorial/layout work for SP001 Publication r3 is complete:

- exact r3 reader source completed;
- exact 14-page PDF completed;
- orphan final bibliography page repaired;
- all 14 pages visually reviewed PASS;
- Core #475's three normal mixed-layout conditions visibly satisfied;
- below-target 14/18 substantive-depth judgment completed;
- no need for further research or padding identified.

What remains is **canonical materialization and validation of the r3 publication authority chain**, followed by the Human Publication Preview Gate.

The stale r2 authority chain is the only reason the current Production State remains `DRAFT_COMPLETE / stage:reader-publication-validation`.

Stop after presenting the fresh exact r3 candidate for Human Publication Preview review.