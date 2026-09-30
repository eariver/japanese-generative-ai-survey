# TS-003 Vision & Multimodal AI — Sol Evidence Semantic Review r2

Status: `SOL_EVIDENCE_SEMANTIC_REVIEW_R2 / REQUEST_CHANGES / MINIMAL_EVIDENCE_REPAIR`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `65decf2e0b39c72a56d3f1be56c7d8d3ef808223`

Reviewed tree: `9d5051afaf2e2c4b10507e2d5010ffc40d503ed2`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Decision: **REQUEST_CHANGES**.

The r1→r2 repair materially improved the Evidence package and correctly preserved the bounded execution contract. Most r1 blockers are closed. However, two narrowly scoped semantic-fidelity defects remain and must be repaired before Evidence can be accepted for Materiality/Completeness.

---

## 1. What passed

- Launch parent is exactly the prior Sol launch HEAD `8fde4cbdf175d46ae0f84a184e2c4b8ed0cbfe90`; the worker advanced by one normal commit.
- The r2 commit is append-only relative to that parent. Compare shows the new r2 Evidence/Views/execution artifacts as additions; no r1 accepted artifact was modified or deleted.
- r2 generated a new accepted Evidence set `3f6be211...` with 111 Cards and a new Views set `73c06689...` with 111 Views.
- Status counts remain honestly `VERIFIED 106 / PARTIAL 5`; no status inflation was used to claim closure.
- Paper-bound current-system Cards VM-D065 and VM-D066 no longer carry repository deployment/license facts. Their current claims are paper-supported and their edition boundary judgments are now `INFERENCE`.
- VM-D071 no longer makes the undifferentiated `Apache 2.0` claim for weights/data/code and now exposes the paper's own openness framing together with closed dependencies.
- `PRIMARY_FACT` synthesis misclassification was removed from the repaired corpus.
- main and frozen Production Core are unchanged.
- canonical Production State remains `CANDIDATES_NORMALIZED`; Evidence checkpoint remains pending by design; Materiality/Completeness/Selection/Architecture remain pending.
- G01–G06 remain unresolved/partially unresolved as required.

These improvements should be preserved. Do not rerun Discovery or Screening and do not rebuild unrelated Evidence semantics.

---

## 2. Blocking finding R2-F1 — fresh HF/API facts are still not canonically source-bound

The r2 repair correctly removed repo-derived facts from paper-only Cards, but then introduced a narrower version of the same defect into three repository Cards.

The canonical r2 Evidence Card `sources` arrays for VM-D074, VM-D075 and VM-D077 each contain only the Discovery-bound GitHub repository root as `src-1`. Nevertheless their claims explicitly rely on freshly consumed Hugging Face release/API surfaces that are **not present in the Card `sources` array and are not identified by a source_id**.

Confirmed cases:

### VM-D074 — Qwen3-VL repository

The Card binds only `https://github.com/QwenLM/Qwen3-VL`, but claim 3 states the weights are Apache 2.0 based on `HF Qwen/Qwen3-VL-8B-Instruct release tag ... sha 0c351dd0` and its context says `Repo LICENSE + HF release API consumed`.

### VM-D075 — Qwen3-Omni repository

The Card binds only `https://github.com/QwenLM/Qwen3-Omni`, but claim 1 states `Weights license is license:other per HF ... release tag (sha 26291f79...)` and its context says `Repo README + HF release API consumed`.

### VM-D077 — Molmo 2 repository

The Card binds only `https://github.com/allenai/molmo2`, but claim 2 uses HF release tags to establish model-weight licensing and dataset availability and says `Repo LICENSE + HF release API consumed`.

The r2 source-binding audit marks these as PASS because the Cards remain task-bound, but that check is insufficient for CV2-DM-020: a claim is not source-faithful merely because it cites a valid task source when part of the claim actually comes from an unlisted external source.

### Required repair

Do **not** expand Discovery or rerun Screening just to admit these supplemental HF/API surfaces.

For canonical Evidence r3, use one of the following only when supported by the current Evidence/task authority:

1. If the existing canonical Evidence machinery legitimately permits the exact HF/API surface to be admitted as a bound Evidence source without changing Discovery/Screening authority, add the actual source entry and bind the affected claim to that source_id, then validate normally.
2. Otherwise, remove the HF/API-derived license/tag/dataset facts from the canonical Evidence Card. Keep them only in the execution/audit report as supplemental non-canonical observations. Retain only facts actually established by the Card's bound repository source.

Do not relabel an HF-derived fact as repository-derived merely to satisfy the validator.

Expected conservative outcomes if exact supplemental binding is not supported:

- VM-D074: repository-supported deployment facts remain; weight-license status becomes unbound/unresolved unless the bound repository itself establishes it.
- VM-D075: repository-supported deployment facts remain; HF-derived `license:other` assertion is removed from canonical Evidence and license remains unresolved unless the bound repository establishes it.
- VM-D077: repo-supported pipeline/code facts remain; HF-derived weight-license and dataset-tag assertions are removed from canonical Evidence; data-license mixture remains PARTIAL/UNRESOLVED.

---

## 3. Blocking finding R2-F2 — D101 still contains stale term-origin semantics in Card and View

The r2 claim body improved the World Models lineage, but stale r1 semantics survive in multiple canonical fields.

### D101 Card residuals

- claim-1 context still says `term-origin content consumed`.
- verification target `non-ancestry statement` still has finding: `Terminological origin with explicit non-ancestry to Genie recorded; required in later prose.`

This directly contradicts the r2 repair report's statement that `Terminological origin` was removed and the Sol r1 requirement not to assert a term-history conclusion that was not researched.

### D101 Edition View residuals

The r2 View still contains:

- `transition_ids: ["d14-term-origin"]`
- `inheritance_note: "Dream-training terminology inherited ... by later world-model discourse."`

Those annotations preserve exactly the historical-term lineage that r1 asked to replace with a branch-separated historical-formulation anchor.

### Required repair

Remove all positive term-origin / terminology-inheritance assertions from D101 canonical r3 Card and View.

D101 should express only:

- Ha & Schmidhuber 2018 as a **major historical neural-world-model / dream-training formulation anchor for this edition**;
- Dreamer as latent-dynamics/model-based-decision branch;
- JEPA/V-JEPA as predictive-representation branch;
- Genie as interactive-generative branch;
- no direct ancestry asserted between these branches unless a source explicitly supports it;
- no broad claim about origin or inheritance of the term `world model`, because that history was not researched here.

Replace `d14-term-origin` with a non-origin formulation-anchor transition identifier that is valid for the edition-local schema, or remove the transition annotation if no valid non-origin identifier exists. Do not invent an invalid schema value.

---

## 4. r3 repair boundary

This is a **minimal Evidence repair only**.

Do not:

- rerun Discovery;
- alter Screening;
- change the 111-task set;
- change unrelated Cards merely for style;
- advance Production State;
- build Materiality Ledger or Profile Completeness;
- run Selection or Architecture;
- create Human Gate decisions;
- modify main or Production Core.

Create a new append-only r3 Evidence acceptance and r3 Views acceptance from the same canonical task package. Preserve r1 and r2 accepted artifacts unchanged.

The r3 semantic audit must explicitly test:

- no claim or verification text mentions an external HF/API/repo/vendor surface unless that exact authority is represented by a valid bound source_id for that Card;
- the strings `Terminological origin`, `term-origin content`, `d14-term-origin`, and positive `terminology inherited` wording are absent from D101 canonical Card/View;
- r3 statuses remain honest; do not optimize VERIFIED count;
- lifecycle remains `CANDIDATES_NORMALIZED`.

Normal stop:

`TS-003 EVIDENCE_SEMANTIC_REPAIR_R2_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R3`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
