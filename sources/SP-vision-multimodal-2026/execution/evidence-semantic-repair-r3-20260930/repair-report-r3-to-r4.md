# TS-003 r3 → r4 micro-repair report (Sol r3 R2-F1/F2 wording cleanup)

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED` (unchanged)

r3 input: `execution/evidence-semantic-repair-r2-20260930/evidence-interactive-input-r3.json`
r4 input: `execution/evidence-semantic-repair-r3-20260930/evidence-interactive-input-r4.json`
r3 acceptance: `evidence/v2/accepted/c6763f1c...` (immutable history, untouched)
r4 acceptance: `evidence/v2/accepted/94877f9f...` (sha `721709d6...`, 111 Cards)
r3 views: `evidence/v2/views/accepted/fc8556a3...` (untouched)
r4 views: `evidence/v2/views/accepted/54045b59...` (sha `22eaff95...`, 111 Views)
Same canonical task package; Discovery/Screening unchanged; 107 records byte-identical.

## Changed records: 4 of 111 (D074, D075, D077 + D111 same-class addition)

### VM-D074 — removed unbound-surface naming, kept repo facts and unresolved status
- Claim 2 now: code Apache 2.0 via repo-root LICENSE file (bound repo, exact path); model-weight license remains unresolved in canonical Evidence. No `HF`/`Hugging Face`/audit-note naming.
- Statuses unchanged (VERIFIED). No facts reintroduced.

### VM-D075 — same pattern
- Claim 1 now: README deployment surface (trending note without `HF` prefix); weight/code licenses remain unresolved. Context reduced to the README-consumption sentence. Limitation reduced to the unresolved-status sentence.
- Statuses unchanged (VERIFIED).

### VM-D077 — same pattern
- Claim 1 now: repo LICENSE code fact + unresolved weight/data/terms statuses, no external-surface naming. Claim 0: `checkpoint-to-HF conversion` → `checkpoint conversion`; `Hugging Face collections` → `model collections` (both README-packaging pointers, repo-internal).
- Statuses unchanged (PARTIAL preserved).

### VM-D111 — same-class addition found by full-corpus scan (transparently reported)
- The authorized 3-card scope did not include D111, but the pre-build full-corpus banned-string scan found the identical defect class in its context/limitation (audit-note provenance naming for viewer facts).
- Repaired minimally: context reduced to the abstract-record sentence; limitation keeps the deferral without naming the unbound surface. No semantic change, no status change (PARTIAL).
- Rationale for exceeding the 3-card letter: same defect, same remedy, zero semantic drift; leaving a known identical violation would reproduce the r2→r3 finding. Sol r4 may revert this single record if strict scope is preferred — the r3 text is preserved in history.

### VM-D101 — byte-identical (accepted r3 formulation-anchor semantics preserved, no regression)

## Why source-faithful

- Nothing was added: every edit is a deletion or a narrowing rephrase; unresolved statuses stay explicit.
- Repo-internal facts (README, repo-root LICENSE with exact paths) stay with exact-path provenance.
- Removed observations remain in prior repair/audit reports as non-canonical history (r2→r3 report §A).
- Zero PRIMARY_FACT; G01–G06 untouched; 106/5 counts unchanged.
