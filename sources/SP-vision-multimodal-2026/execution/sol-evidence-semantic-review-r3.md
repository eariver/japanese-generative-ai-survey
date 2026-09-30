# TS-003 Vision & Multimodal AI — Sol Evidence Semantic Review r3

Status: `SOL_EVIDENCE_SEMANTIC_REVIEW_R3 / REQUEST_CHANGES / MICRO_REPAIR_ONLY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `3e81702b7aef436b21fa22f4fabe61b8b08cfc70`

Reviewed tree: `0bcbe06034f4e22b3d34b0c54a7d70b9095b1d66`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Decision: **REQUEST_CHANGES**, but only for one contract-level residual. The substantive r2 blockers are otherwise closed.

---

## 1. What passed

- The worker started from the exact Sol launch commit `52513434747d3b8caa0deb56cd3a2bc78d6b818c` and advanced by one normal commit.
- Compare shows the r3 work as append-only additions: new accepted Evidence set `c6763f1c...`, new Views set `fc8556a3...`, and execution artifacts. r1/r2 accepted artifacts were not modified or deleted.
- r3 covers 111/111 tasks and preserves honest status counts `VERIFIED 106 / PARTIAL 5`.
- VM-D074 no longer asserts a Hugging Face-derived weight-license fact as canonical Evidence; repository-supported code-license/deployment facts remain, and weight license is unresolved.
- VM-D075 no longer carries the HF-derived `license:other` assertion as a canonical fact; deployment claims remain repository-bound and license is unresolved.
- VM-D077 no longer carries HF-derived weight-license/dataset-tag assertions as canonical facts; repo-supported code license/pipeline scope remain and the record stays PARTIAL.
- VM-D111 was proactively narrowed for the same source-binding class; this is within the semantic-fidelity repair boundary and does not expand scope.
- VM-D101 Card is repaired to a historical formulation anchor with branch-separated lineage; no positive term-origin claim remains.
- VM-D101 View now uses `d14-historical-formulation-anchor` and explicitly disclaims terminology inheritance.
- `PRIMARY_FACT` synthesis remains absent.
- G01–G06 remain open as required.
- Production State remains `CANDIDATES_NORMALIZED`; Materiality/Completeness/Selection/Architecture/Human Gates are still pending.
- main and frozen Production Core remain unchanged.

These repairs are accepted and must be preserved.

---

## 2. Blocking residual R3-F1 — unbound external-surface names remain inside canonical claim text

Sol r2 required this exact semantic check:

> no canonical r3 claim or verification finding mentions an external HF/API/repo/vendor authority unless that actual authority is represented by a valid bound source_id for that Card.

The worker correctly removed the **facts** derived from unbound Hugging Face/API surfaces, but three canonical Cards still mention those unbound external surfaces inside the claims/contexts as provenance commentary.

### VM-D074

Claim 3 says:

- `the Hugging Face release surface is not a bound source for this Card`
- `the HF-derived tag observation is retained only in the audit note`

and therefore the canonical claim text still mentions an unbound external authority.

### VM-D075

Claim 1 and limitation 2 still say:

- `the Hugging Face release surface is not a bound source for this Card`
- `HF-derived license observation ... audit note`

The substantive license assertion is gone, but the canonical Card still names the unbound external surface.

### VM-D077

Claim 2/context still says:

- `Hugging Face release surfaces are not bound sources for this Card`
- `HF release API facts removed to non-canonical audit note`

Again, the substantive facts are removed, but the canonical Evidence surface itself still mentions the unbound source.

This is now a **contract-cleanliness issue only**, not a substantive source-fidelity failure. The correct place for those external-source notes is the non-canonical repair/audit report, where they already exist.

---

## 3. Required micro-repair

Do not research anything new.

Do not rerun Discovery or Screening.

Do not alter the 111-task set.

Do not touch VM-D101 unless needed to keep generated Views synchronized; its current semantic content is accepted.

For VM-D074, VM-D075 and VM-D077 only:

- remove all canonical claim/limitation/context/verification wording that names `HF`, `Hugging Face`, `release API`, `release tag`, or any other unbound external source;
- retain the semantic result without naming that unbound source, e.g. `model-weight license unresolved in canonical Evidence` or `released-data licensing remains unresolved`;
- keep repository-internal LICENSE/README facts where supported by the bound GitHub repository source;
- keep the supplemental HF/API observations only in the execution/audit report, not in canonical Evidence or Views.

If the build process regenerates all Cards/Views, unchanged records must remain semantically/byte stable where possible. Do not use this micro-repair to rewrite unrelated Evidence.

---

## 4. r4 acceptance checks

Before stopping, verify all of the following:

1. 111/111 tasks remain represented.
2. r1/r2/r3 accepted artifacts remain immutable.
3. VM-D074/D075/D077 canonical Card text contains no `HF`, `Hugging Face`, `release API`, `release tag`, or other reference to an unbound external surface.
4. Their unresolved license/data status remains explicit without external-source naming.
5. VM-D101 retains the accepted branch-separated formulation-anchor semantics and does not regress.
6. `PRIMARY_FACT` synthesis remains zero.
7. G01–G06 are unchanged unless genuinely resolved by already-bound authority; no new research is permitted.
8. VERIFIED/PARTIAL counts remain evidence-driven; no status optimization.
9. Production State remains `CANDIDATES_NORMALIZED`.
10. No Materiality/Completeness/Selection/Architecture/Human Gate artifacts are created.
11. main and Production Core remain unchanged.

Normal stop:

`TS-003 EVIDENCE_SEMANTIC_MICRO_REPAIR_R3_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R4`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
