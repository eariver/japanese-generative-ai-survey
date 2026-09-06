# W34 Core-integrated Evidence regeneration — execution worklog

## Authority and boundary

- Issue: `2026-W34`
- Initial W34 production branch SHA: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`
- Reviewed/integrated Core main: `d54f9c7b3a7cef064c6701ab864daab27118cdce`
- Core integration merge commit: `fb83242ddd35f8cf468941f8a76a4bafb331939f`
- This run uses only the existing `weekly/2026-W34-v2-work` branch.
- The initial old Architecture Review surface was not presented to a Human; the W34 Human review record count was zero.
- No Discovery or accepted Screening authority was changed. No rescreening was performed.

## Operator invalidation

- Invalidated commit: `fb83242ddd35f8cf468941f8a76a4bafb331939f`
- Gate: `ARCHITECTURE_REVIEW`
- Regeneration boundary: `CANDIDATES_NORMALIZED`
- Canonical record: `sources/2026-W34/execution/operator-invalidations/architecture-invalidation-0001.json`
- Record SHA-256: `7a9a2c7bdde82e75f96245d8694286b10d2344edd1edb5388fc92ed57ccb8ab7`
- `human_decision`: `false`
- Human review record/index rows created: `0`
- The eventual `target_gate` was not used as the current pending-Gate identity; the integrated Core resolved the pending Gate from lifecycle/config mapping, pending status, null provenance, and `HUMAN_GATE_REACHED`.
- Mutable downstream canonical artifacts and downstream checkpoints were superseded by the canonical operator cleanup. Historical accepted runs and Git history were retained.

## Evidence Authority Supplement

- Supplement: `sources/2026-W34/execution/luna/w34-core-repair-r1/evidence-authority-supplement.json`
- Supplement SHA-256: `483c06b815725f41543249c0ad2d056f9ee127392edc598ea15a20f917caf614`
- Preserved substantive exact authority bodies: `61`
- Unique authority body SHA-256 values: `60`
- Evidence tasks with Supplement authority: `50`
- Inputs were the preserved r2 ledger, retrieval provenance, and exact raw bodies. No broad new Web research was performed.
- Zero-byte, timeout, HTTP-error, non-substantive, unsupported, or arbitrary sources were not bound.

## Regenerated active authorities

Historical accepted Evidence/View runs remain immutable and coexist with the new runs. Active authority is checkpoint-bound, not directory- or mtime-selected.

- Active Evidence acceptance: `sources/2026-W34/evidence/v2/accepted/377134b62c98bf0b65a7cf8cda1ef538eac0e2afcd7aa9aeeeda0f1d09493ada/evidence-accepted.json`
  - SHA-256: `42cddac765343a71fee1969ed52ab7628df60825ce31cc14724d5dc6c432729e`
  - `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 / REJECTED 7`
- Active Edition Views acceptance: `sources/2026-W34/evidence/v2/views/accepted/bcaa69b03f5d2ae6ba6024474b13fa36cd4b2382c4d1e1ac76dc36edeab9f81e/edition-views-accepted.json`
  - SHA-256: `ed0e11123e0dd3f5eff8e40081608c3fa50d5be1049cc114d1465ba8194b3fc6`
  - `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7`
- Materiality: `sources/2026-W34/materiality-ledger-v2.json`
  - SHA-256: `0c160b6f2555277eb3ab51252882063430356c6f09bc87d7e6d269a69b57696`
  - `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 / DUPLICATE 4 / EXCLUDED 26`
- Completeness: `sources/2026-W34/profile-completeness-v2.json`
  - SHA-256: `4da8785863be5904f0f4decb843b3d580a88419a2d1222ce5d310881ec887424`
  - status: `LIMITED`, with candidate-local authority, chronology, access/body, and window limitations retained.
- Candidate Matrix: `sources/2026-W34/candidate-matrix-v2.json`, SHA-256 `98977612bdd152ec03c9d8c6fcb2f3f37efd2e0e6fccafb46b56d32ab302a651`
- Candidate Selection: `sources/2026-W34/candidate-selection-v2.json`, SHA-256 `160e3ae0fda3d8432707566b445740e5f3cf67102355fc5824762aefde50090c`
  - `SELECTED 1 / INSPECT 15 / HOLD 64`
- Architecture: `sources/2026-W34/architecture-v2.json`, SHA-256 `e22fe06c8962355b7429253b0cb4d82d13cbddbcfc60df05daaa6c8b2d3bc279`
  - `PROPOSED`, one package titled `Verified developer-tooling change`, primary candidate Transformers v5.15.1.
- Architecture Review Summary: `sources/2026-W34/architecture-review-summary-v2.json`, SHA-256 `9f9db1ec6e1fcf88381671b9272434c24676ea845dd172d50efcde7088f0a0f2`
  - `READY_FOR_ARCHITECTURE_REVIEW`
- Architecture Review Attention: `sources/2026-W34/architecture-review-attention-v2.json`, SHA-256 `ccd4cdd709f6205f22dae0e422bf13eba033f689980cf3d0f34b29057e58faad`

## Canonical stage progression

- `CANDIDATES_NORMALIZED` validation/review/checkpoint: PASS; checkpoint SHA-256 `daa074a0477b4aec85ff42482c5f1412f1e0529f2fff15c971c1dcb3cefae756`
- `EVIDENCE_REVIEWED` validation/review/checkpoint: PASS; checkpoint SHA-256 `00608c3433509b23ee0492f72ded65a461f37ac4b5b226158dec53974f058cbc`
- `SELECTION_COMPLETE` validation/review/checkpoint: PASS; checkpoint SHA-256 `b4db3258ec2ac69b17a8c13d2e7e726e3fc11075c5e49ea14b54cbb798904a34`
- Final lifecycle: `ARCHITECTURE_ESTABLISHED`
- Final next action: `ARCHITECTURE_REVIEW`
- Final terminal reason: `HUMAN_GATE_REACHED`
- Architecture Review: pending, provenance null
- Publication Preview: pending, provenance null
- Final Production State SHA-256 before canonical commit: `585f95681ba5501edf782479a1ceb0bb211a49b0261c0ea0934e5d023842909c`
- Canonical review-surface remote commit: `d436e2b1b4a181557170dc784c58994a0a9c8538`
- Canonical review-surface tree: `63437319bbf30d04416e3016e9d1554a835dc42f`
- Canonical review-surface parent: `01e1bc5920ef13b2797e5d538950c630a5b80855`

## Explicit non-actions

- Human decisions created: `0`
- Human approvals created: `0`
- Human REQUEST_CHANGES created: `0`
- Sidecar executions: `0`
- Drafting / Publication Candidate / Publication Preview / Freeze / Release: not started
- Shared-Core writes after integrating reviewed main: `0`
- W34 branch writes are limited to the normal integration, operator invalidation, and this canonical regeneration record.
- The exact final remote review-surface commit SHA is `d436e2b1b4a181557170dc784c58994a0a9c8538`; this is the commit presented for Human Architecture Review.
