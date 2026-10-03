# Failed Cross-Gate Attempt Provenance Correction (append-only)

Classification: `PROVENANCE_CORRECTION_ONLY`

This note does not delete, rewrite, or alter:

```text
sources/SP-vision-multimodal-2026/execution/reviews/human-publication-preview-r1-request-changes-vm-d112-reentry-20261003.md

sources/SP-vision-multimodal-2026/execution/requests/ts003-vm-d112-cross-gate-reentry-20261003.json
```

Those files remain historical records of a failed materialization attempt.

## Facts established by the frozen Core bridge run

- Bridge execution failed **before any Human Gate record was written**.
- `gates/reviews/publication-r1.json` was **not** created (verified absent).
- `gates/review-index.json` was **not** advanced (still architecture r1/r2 only).
- Production State was **not** changed by the attempt
  (`RELEASE_CANDIDATE`, architecture `approved`, preview `pending` throughout).
- Therefore the preparatory wording `Publication Preview r1 REQUEST_CHANGES`
  did **not** become canonical Human Gate authority. It remains proposal
  language inside the historical request record, nothing more.

## What the prior Human approval does and does not cover

- The previously given Human approval authorized edition-local re-entry
  **intent** (VM-D112 pipeline intake with Core Freeze preserved).
- Because no gate record was written, a fresh explicit Human Publication
  Preview REQUEST_CHANGES decision must still be made — and it must refer to
  the exact restored review-surface commit produced by the companion
  compatibility restoration (38pp Phase-2 Candidate `fa01ed1e...` + PDF
  `78f4cc8c...`, validated byte-identical to checkpoint authority).

## What is not claimed

- Do not claim the Human already reviewed the restored r4 Candidate/PDF.
  No such review has occurred. The next Human decision is still pending.
