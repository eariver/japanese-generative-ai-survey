# W40 staged Architecture outline r16 — count-corrected successor (NOT Architecture)

Status: STAGED_R16 / OUTLINE_ONLY / NO_ARCHITECTURE_ACCEPTANCE
Successor of (r15 preserved immutable):
`execution/architecture-staged-outline-r15.md`
Binding: `execution/architecture-boundaries-r15.json`
(SHA-256 `1736737e9488e3a6e2a94471bfc506fdc43c9f18d5321bbc31b25bb99eb749c7` —
recomputed r16 from actual bytes, unchanged).
This outline duplicates NO literal boundary strings (verbatim arrays live ONLY in the
SHA-bound JSON) and edits NO authority bytes. It corrects r15's DOCUMENTATION counts
(A01/A05); the r15 source JSON was never defective. Candidate IDs, usages, Roles,
destinations identical to coverage-r14/outline-r15. COND-A/B stay out.
Creates NO `architecture-v2.json`, NO checkpoint, NO State change; claims NO
Reader Manifest `architecture_coverage`.

## Corrected package table (rebuilt r16 from actual bytes; A01/A05)

| Pkg | raw | unique | dedup | PRIMARY (IDs) | SUPPORTING (IDs) |
|---|---|---|---|---|---|
| P1 frontier-models | 14 | 12 | 2 | 50847d0a9, 34e0532a2, 2fc5e5025 | — |
| P2 open-reasoning | 8 | 8 | 0 | 6fa837285, 61859ff02 | — |
| P3 decision-inference | 13 | 13 | 0 | c779a6e34, 230500269, f92f1c9c9 | — |
| P4 devday-product-surface | 10 | 8 | 2 | 5e276e2fc, ebe4568ec | 74c6428e8 |
| P5 safety-provenance | 18 | 17 | 1 | 1e165c26e, 415837190, 488969327 | 30e4d9ba0, 8479c9784 |
| P6a training-methods-and-systems | 10 | 10 | 0 | 4368e1305, 24719b616 | — |
| P6b evaluation-and-execution-infra | 15 | 15 | 0 | 245268468, cb642e557 | 08da5f196 |
| P7 multimodal-serving-observability | 19 | 16 | 3 | 22bb2c7fa, 3f5be21c2, 6dd7c91d3 | 79687e931, db63bd8b3 |
| P8 enterprise-industry-digest | 6 | 6 | 0 | — | 45d769ec1, dcad0b509 |
| TOTAL | 113 | 105 | 8 | 20 | 8 |

(Full IDs: `candidate:2026-W40:` + suffix. architecture_role values per coverage-r14.)

Corrections vs r15 outline (documentation only): P1 raw 12→14, P4 raw 11→10,
P5 raw 19→18, P7 raw 16→19. Dedup breakdown corrected: **P1−2 / P4−2 / P5−1 / P7−3**
(r15's "P4−3/P5−2" withdrawn):
P1: "All benchmark deltas vendor-run; independent reproduction pending." ×2 and
"Day-only date." ×2; P4: "Day-only date." ×3; P5: "Day-only date." ×2;
P7: "Day-only date." ×4. Verified r16 by Counter over Matrix bytes (see validation
addendum). 113−8=105.

Candidate-level distribution (A02, recomputed r16): one candidate ×7, nine ×5,
seven ×4, eleven ×3 → `1×7+9×5+7×4+11×3=113`, `1+9+7+11=28`. (r15 handoff's
`9×5+17×4+9×3` withdrawn — it neither sums to 113 nor to 28.)

## Boundary references (exact, by SHA-bound JSON path)

Per-package verbatim arrays: `architecture-boundaries-r15.json → packages.{P1…P8}.boundaries`
(raw→unique per table above). Per-candidate arrays: `→ entries[i].remaining_boundaries`
(distribution above). Membership rule: every candidate string is a literal element of
each of its destination packages' arrays (validation-addendum-r16: missing 0/113;
ephemeral Core PROPOSED re-run 0 errors with disclosed placeholders; NOT formal PASS).

## Content requirements (unchanged from r15 staging guidance)

P1 largest … P8 small digest (see r15 outline, preserved). Each literal boundary string
is the drafting checklist for its package. P6a/P6b share `WEEKLY:training-eval-infra`
with no fictional split role. DGX evidence-only; W39 HOLDs unplaced; COND-A/B out.
Compression guard unchanged. Eq.5 primary note:
`technical-prep-r16/contextlm-eq5-primary-note.md` (A04; Eq.6/metrics untouched).
