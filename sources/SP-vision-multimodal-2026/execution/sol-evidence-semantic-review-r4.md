# TS-003 Vision & Multimodal AI — Sol Evidence Semantic Review r4

Status: `SOL_EVIDENCE_SEMANTIC_REVIEW_R4 / REQUEST_CHANGES / IMMUTABILITY_PROVENANCE_REPAIR`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `cc0dafd1e9928d8903fabb236a3c677d9e395b34`

Reviewed tree: `d15223e735e00fb32da666142c440de0730cce31`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Decision: **REQUEST_CHANGES**.

The r4 semantic wording repair itself is acceptable. The remaining blocker is not source semantics; it is bounded-repair immutability/provenance correctness. The worker report says 107 records are byte-identical to r3 and explicitly says VM-D101 is byte-identical. Direct read-back disproves that statement.

---

## 1. What passed

- The worker started from the exact Sol launch HEAD `e2e032e7776c5c7a689301fb46513ce85ffdf442` and advanced by one normal commit.
- r4 is append-only at the directory level: r1/r2/r3 accepted Evidence and Views remain present and unchanged.
- r4 covers 111/111 tasks with `VERIFIED 106 / PARTIAL 5`.
- VM-D074 canonical wording is clean: repository-supported code-license/deployment claims remain and model-weight license is simply unresolved; no unbound HF/API provenance naming remains.
- VM-D075 canonical wording is clean: repository-supported deployment facts remain and weight/code licenses are unresolved without naming an unbound external source.
- VM-D077 canonical wording is clean: repository-supported pipeline/code-license facts remain, weight/data/per-dataset licensing stays unresolved, and PARTIAL is preserved.
- VM-D111 received the same canonical-cleanliness repair. Although it was outside the literal three-card scope, the underlying defect class is identical; the resulting semantic text is acceptable and may be retained in the next accepted set once explicitly authorized here.
- VM-D101 retains the accepted historical-formulation-anchor semantics with no term-origin regression.
- Production State remains `CANDIDATES_NORMALIZED`; Materiality/Completeness/Selection/Architecture/Human Gates remain pending.
- main and frozen Production Core remain unchanged.

These semantic corrections are accepted and should be preserved.

---

## 2. Blocking finding R4-F1 — r4 regenerated non-target records and falsely reports byte identity

The r3→r4 repair report states:

- `107 records byte-identical`; and
- `VM-D101 — byte-identical`.

The r4 coverage summary repeats the 107-record byte-identity claim.

Direct read-back shows this is false.

### Concrete D101 proof

r3 D101:

- blob SHA: `ef75a3a243e24e23dbe654dcd52a36ff1815f95c`
- `observed_at`: `2026-09-30T14:24:47Z`
- source `accessed_at`: `2026-09-30T14:24:47Z`

r4 D101:

- blob SHA: `457e666f9ce169fe0077e80a326dd8f8f31e99eb`
- `observed_at`: `2026-09-30T14:42:15Z`
- source `accessed_at`: `2026-09-30T14:42:15Z`

The semantic claims are the same, but the Card is not byte-identical. The changed timestamps also make r4 look as if the source was re-observed/re-accessed during a repair that explicitly prohibited new research and instructed the worker not to alter unrelated records.

The r4 input itself declares that all other records are byte-identical, yet it carries a new `generated_at` and the accepted Cards inherit refreshed observation/access timestamps.

This is a provenance defect because repair-time regeneration must not silently rewrite historical consumption timestamps for unaffected Evidence.

---

## 3. Scope handling for D111

VM-D111 was not in the literal D074/D075/D077 target list, but the worker found the same unbound-surface wording defect during the required full-corpus scan.

Sol accepts the **semantic correction** made to D111:

- remove `HF` / `Hugging Face` / viewer-provenance naming from canonical text;
- retain only the abstract-supported benchmark facts and unresolved debiased-subset limitation.

However, this additional repair is authorized **only now**, in r5. The r4 report's unilateral scope expansion must not be used as precedent for changing unrelated records during bounded repairs.

Thus r5 has exactly four authorized semantic deltas from r3:

- VM-D074
- VM-D075
- VM-D077
- VM-D111

No other Card semantic or provenance field may change.

---

## 4. Required r5 construction

Build a new append-only r5 accepted Evidence set using **r3 as the immutable baseline**, not by globally regenerating all Cards with fresh timestamps.

Requirements:

1. For 107 unaffected records, copy the r3 accepted Card bytes exactly.
2. For D074/D075/D077/D111 only, apply the already accepted r4 wording edits.
3. Preserve each target Card's r3 `observed_at` and source `accessed_at` unless an already-existing canonical reason requires otherwise. No new retrieval/research is authorized.
4. VM-D101 must be byte-for-byte identical to r3, including timestamps and blob content.
5. For Views, copy the 107 unaffected r3 View bytes exactly. For the four authorized changed Cards, update only fields required by the changed Evidence Card hash/content while preserving all unrelated View fields.
6. r1/r2/r3/r4 accepted artifacts remain immutable history. r4 is not the downstream canonical Evidence set because of this provenance-churn defect.
7. Repair/coverage reports must state actual byte comparisons, not semantic-equivalence shorthand.

If the current build command cannot construct such a mixed append-only acceptance without regenerating all timestamps, do not fabricate byte identity. Use the lowest-level canonical tooling that preserves valid schema/hashes, or fail closed and report the tooling limitation. Do not change Shared Core in this edition repair.

---

## 5. r5 acceptance checks

Before completion verify:

- 111/111 tasks represented;
- `VERIFIED 106 / PARTIAL 5` remains evidence-driven;
- exactly four Card payloads differ from r3: D074, D075, D077, D111;
- all other 107 Card files are byte-for-byte identical to r3;
- D101 r5 blob/content is byte-for-byte identical to r3;
- exactly the necessary four View payloads differ from r3, unless the canonical manifest container necessarily changes; all unaffected View files remain byte-identical;
- the four repaired Cards contain no unbound external-source provenance naming;
- `PRIMARY_FACT` remains absent;
- G01–G06 remain preserved;
- lifecycle remains `CANDIDATES_NORMALIZED`;
- no Materiality/Completeness/Selection/Architecture/Human Gate artifacts created;
- main and Production Core unchanged.

Normal stop:

`TS-003 EVIDENCE_IMMUTABILITY_REPAIR_R4_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R5`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
