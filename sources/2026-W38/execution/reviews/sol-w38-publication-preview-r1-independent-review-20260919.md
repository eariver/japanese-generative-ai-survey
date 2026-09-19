# W38 Publication Preview r1 — Independent Sol review

Status: `PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Edition: `2026-W38`

Audit started: `2026-09-19T16:06:21+09:00` / `2026-09-19T07:06:21Z`

Human decision: `PENDING`

## 1. Exact reviewed authority

Human Publication Preview r1 binds:

- reviewed repository commit: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61`
- Publication Candidate:
  - path: `sources/2026-W38/publication/v2/publication-candidate-v2.json`
  - candidate SHA-256: `43c7d33a457d74b04cbba571e006453f8cea27f4dab134e6265bb55f115ce409`
- exact PDF:
  - path: `surveys/weekly/2026-W38/main.pdf`
  - SHA-256: `767f4d98c366ae3c7247da635a6ea0b68753f58327104287ab4fb9d8ec9a2543`
  - bytes: `344241`
  - pages: `11`
  - CI run: `35425249262`
  - artifact: `10577998030`

The current Human-facing preview shell/dossier was added in commit:

`7c9a39587164fa8e94e8dc1e24ec3769677d452d`

## 2. Architecture approval provenance

Canonical Human Architecture decision is valid:

- decision: `APPROVED`
- reviewed production commit: `56b6d3d65c5b4105a410e61a22eb083e66fa344c`
- reviewed_at: `2026-09-19T05:46:14Z`
- canonical record: `sources/2026-W38/gates/reviews/architecture-r1.json`
- immutable approval snapshot: `sources/2026-W38/gates/reviews/approvals/architecture-r1.json`

The approval record timestamp precedes its containing downstream commit (`85b430162bf3bc37656b9adfc50017f318d50055`, commit time `2026-09-19T05:55:55Z`).

No Human Architecture decision was recorded for the superseded r1 surface.

## 3. Frozen upstream authority

No upstream semantic regeneration was detected after Human approval.

Expected counts remain:

- Discovery: 13
- Screening: 12 KEEP / 1 DROP
- Evidence: 9 VERIFIED / 3 PARTIAL
- Materiality: 11 MATERIAL / 1 CONTEXT / 1 EXCLUDED
- Selection: 11 SELECTED / 1 HOLD
- Architecture: 7 packages

The seven approved packages remain in drafting order with no semantic add/merge/split/reorder.

## 4. Independent semantic/editorial audit

Finding: `PASS`

Independent review of the reader-facing TeX/PDF found no blocking semantic deviation from approved Architecture.

Verified boundaries include:

- Astra for Law remains a legal vertical configuration, not a new base-model claim.
- Vals and other vendor measurements remain explicitly vendor-reported/unreproduced.
- Gemini 3.8 Live X observations are context only and are not promoted into official capability facts.
- LSVP is treated as a verified-access regime; Mythos release timing is not inferred.
- Amodei essay -> R&D metrics -> Accenture remains an editorial governance arc, not a causal claim.
- Accenture `$1B` values are stated expectations, not audited expenditure.
- Jev parameter count/topology/training details are not invented; speed/cost claims remain vendor-stated.
- Devin Code Scans pilot outcomes remain first-party trial results, not independently reproduced facts.
- CAI-Image / Tsubaki creator tooling is not ranked against foundation video models.
- DeepSeek routing remains narrow context and is not promoted into an eighth package/release.
- GLM-5.5 rumor is not surfaced as a W38 technical development.
- X/community evidence remains supplementary observation; technical facts use primary sources.

No cluster-wide generalization, partnership overstatement, or late-breaking-as-ordinary promotion was found.

## 5. Japanese reader-surface audit

Finding: `PASS`

The magazine reads as Japanese technical editorial prose rather than an execution/audit report.

No blocking leakage of internal vocabulary such as Screening, Selection, Materiality, VERIFIED, PARTIAL, HOLD, internal repository paths, or candidate identifiers was found in reader-facing prose.

Qualifications are generally expressed in natural Japanese (for example, vendor-attribution and independent-reproduction caveats are separated into readable boundary boxes).

## 6. Citation/public auditability

Finding: `PASS`

- bibliography contains 19 cited entries;
- technical claims cite primary/official sources separately;
- 9 reader-facing X references use public direct status URLs;
- no internal repository/blob path is used as a reader citation;
- late-breaking X rows remain excluded from ordinary totals;
- C3 official-only X support is not represented as independent technical corroboration.

## 7. Exact PDF independent visual audit

The exact CI artifact `10577998030` was independently downloaded and extracted.

Independent SHA-256 recomputation:

`767f4d98c366ae3c7247da635a6ea0b68753f58327104287ab4fb9d8ec9a2543`

This exactly matches the Publication Candidate.

The PDF was independently rendered at 160 DPI across all 11 pages.

Visual findings:

- no clipped text;
- no overlap;
- no broken/garbled Japanese glyphs;
- no black-square/font substitution defects;
- cover and contents render correctly;
- all seven package sections are readable in order;
- Sources & Limitations and References render correctly;
- bibliography continues cleanly through p.11.

### p.8 / Issue #508 check

p.8 contains the complete closing subsection `次に何を見るべきか` plus its `この総括の読み方` claim-boundary box.

This is **not** the original W37 #508 failure mode where only a trailing Claim Boundary was orphaned onto an otherwise empty page.

W38 uses the same edition-local pattern that was accepted in the final W37 publication: an explicit page break before the closing subsection so the subsection and its box travel together.

p.8 has substantial unused lower-page space and is visually lighter than surrounding pages, but the closing subsection is coherent, not orphaned, clipped, or structurally broken. This is therefore treated as an aesthetic/non-blocking characteristic, not a Publication Preview blocker.

Generic Weekly layout hardening remains appropriately tracked by open Issue #508.

## 8. Timestamp provenance

Human-facing Preview r1 generation timestamp:

`2026-09-19T06:10:14Z`

Containing preview-shell commit:

`7c9a39587164fa8e94e8dc1e24ec3769677d452d`

Commit time:

`2026-09-19T06:11:40Z`

Result:

`VALID / NOT_FUTURE_DATED`

The inherited Production State history values `06:47/06:48/06:49Z` remain invalid as actual wall-clock chronology and are correctly isolated by:

`sources/2026-W38/execution/provenance/w38-downstream-monotonicity-note-20260919.md`

They are not used as Human-facing review chronology.

## 9. Operational incidents

Two edition-local incidents were reviewed:

1. one pre-commit TeX typo repaired before CI;
2. deletion of one deterministic validation report followed by exact-byte reconstruction verified against the sealed checkpoint SHA.

Neither changes reader-facing semantics, Architecture authority, Candidate identity, or exact PDF bytes.

The validation-report deletion was unnecessary worker error, but recovery provenance is explicit and cryptographically bound. It is not a Publication Preview content blocker.

## 10. Minor non-blocking metadata observations

- `execution/index.md` retains duplicated stale lines `Candidate SHA-256: none` / `PDF SHA-256: none` after the correct Candidate/PDF values. This is navigation hygiene only; canonical Candidate authority is unambiguous.
- Production State `target_gate` remains `ARCHITECTURE_REVIEW` while `next_action` is `PUBLICATION_PREVIEW`. This is consistent with the existing Core semantics also observed in released W37 and is not treated as a W38 edition defect.

Neither item affects the Human-reviewed publication bytes.

## 11. Protected refs / Core scope

At independent audit:

- remote `main` remains `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- Production Line remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- no shared-Core path change was found in the W38 downstream diff;
- no Freeze or Release has occurred.

## 12. Independent Sol verdict

Blocking findings: **0**

Non-blocking observations:

- intentionally light p.8 closing page;
- generic #508 layout hardening remains open;
- inherited #507 State-history chronology remains correction-ledger-only;
- minor execution-index stale duplicate fields;
- documented worker validation-report deletion/recovery incident.

Verdict:

`PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

This is an Independent Sol review only.

Human Publication Preview decision remains:

`PENDING`

The Human decision must be explicitly provided as `APPROVED` or `REQUEST_CHANGES`.
