# Evidence interactive input — provenance and resume note

Status: `AUTHORED / VALIDATED_AGAINST_TASKS / RUN_BLOCKED_BY_SHARED_CORE_DEFECT`

## Contents

- `interactive-evidence.json` (SHA-256 `6cac92b1a51e109a9596752d60263e7341506025211cca8dc619fa80f4229c85`):
  160 interactive Evidence records (exact non-DROP set) + runner block +
  Completeness block (EFF-O01–O12). Authored by Muse (Luna/Work role) from
  consumed authority (95 arXiv abstracts via API + 9 fetched full pages +
  search-excerpt gap-fill) at HEAD `bece7052f8da9a5fb21bb09726f6f0cb7e0075e5`.
- `part_a.py` … `part_e.py`: per-record curated specs (claims, limitations,
  verification findings, materiality, lineage).
- `build_evidence_input.py`: deterministic builder joining specs with
  canonical Discovery + Screening acceptance; asserts exact 160-ID coverage
  and exact per-task verification-target match.
- `task-targets.json` (SHA-256 `6909e1f21c368fdf4ad59b1f85aa81a966f376460bf8fe00f0c5da81969fbfe6`):
  per-task verification targets dumped from the Core-built Evidence Task
  package (transient build, since the package builder writes to temp).

## Validation performed pre-run

- 160/160 non-DROP IDs covered, zero extras.
- Every record's verification array covers exactly its task's
  `verification_targets` (byte-exact target strings).
- Record census: status 155 PARTIAL / 5 VERIFIED; materiality 134 MATERIAL /
  24 CONTEXT / 2 HOLD (D032, D093).
- Completeness block covers exactly profile obligations EFF-O01–O12
  (3 SATISFIED / 9 LIMITATION, overall LIMITED, closure LIMITED with
  `targeted_gap_fill_completed: true`).

## Why the run is blocked

`run_evidence_v2_interactive.py` fail-closes on 67 tasks whose Discovery
`source_type` is absent from Core's Evidence `SOURCE_CLASS_MAP`
(first error: `PRIMARY_DOC` on EFF-D004). See
`execution/defects/shared-core-evidence-source-map-gap-20260922.md`.
Shared Core was left unchanged per production/Core-boundary rules.

## Resume (after reviewed Core repair)

1. Verify `interactive-evidence.json` still matches this SHA-256.
2. Re-run the Core runner with this file as `--input` (no edits); the runner
   archives input bytes into the acceptance directory itself.
3. Expect: 160 Evidence Cards + 160 Edition Views + Materiality Ledger +
   Profile Completeness (`LIMITED`), then Core-advanced State to
   `EVIDENCE_REVIEWED`.
4. Any post-repair input change requires rebuilding via
   `build_evidence_input.py` (needs `part_*.py` + canonical bytes) and a new
   SHA recorded here; never hand-edit the JSON.
