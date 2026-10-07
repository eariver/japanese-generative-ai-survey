# §15 root-cause record — P07A VM-D114 audit (edition-local, Core untouched)

Date: 2026-10-07. Run: `execution/r7-targeted-authority-repair-20261007`.
Prior audit: `execution/r6-final-authority-correction-20261006/semantic_audit_r6.py`
(check `P07A D114 bound (B05 refs D114)` reported PASS).

## Reviewer premise vs final bytes

The closure-review premise states the final artifacts show (a) P07A
`draft-package.json` without VM-D114 and (b) B05 refs without VM-D114.

Forensic result on the committed r7 bytes (`c7aaf74f7`, working tree clean):

- (a) is TRUE: P07A `draft-package.json` `evidence_inputs` contains exactly the 4
  canonical Architecture-placement candidates (VM-D039/037/038/040 tasks); no D114.
- (b) is FALSE for the committed bytes: final P07A-B05 `evidence_refs` contain
  `evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e` (VM-D114) CLAIM claim-1/2/3
  alongside `evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61` (VM-D039) CLAIM
  claim-1/2 (re-verified byte-level from the committed blob during this run).

So no `PASS` was ever issued over D114-less B05 refs. The genuine gap is (a):
package-level effective consumption.

## Actual root cause

The prior audit asserted result-level refs only (`B05 refs contain D114`), which the
edition-local overlay fallback guarantees by construction when the overlay entry
exists — it never inspected `draft-package.json` `evidence_inputs` at all. That is
the tautological class: the check could not have failed while the overlay entry
existed, regardless of package state. It did not inspect a stale path or a wrong
version; it inspected the final result but at only one of the two material levels.

## Why package-level inclusion is not available

Frozen Core (`survey_drafting_v2_base.validate_self_contained_draft_package`)
requires package inputs to be exactly one entry per Architecture candidate
placement (`seen == set(expected_usage)`; anything else errors as `references
candidate outside authorized Architecture package`). VM-D114's placement is P06
PRIMARY. Adding it to P07A's package therefore fails canonical validation —
proven by negative fixture F2 in `negative_fixture_p07a.py`, which injects the
D114 input and observes exactly that failure. Literal package-level inclusion
would require an Architecture mutation (adding D114 to P07A supporting
placements — a redesign the closure review explicitly forbids: `NO REDESIGN`,
`r7 APPROVED remains authoritative`) or a shared-Core mutation (prohibited).

The established edition-local mechanism (in force since r5-rev1, accepted through
the r5/r6/r7 Human gate audits) therefore represents cross-package SUPPORTING
consumption at result level through the union index, with exact-SHA binding to
accepted Evidence. P07A-B05 is such a consumption: SigLIP2-specific prose bound
to VM-D114 claims 1–3, CLIP limits bound to VM-D039 claims 1–2.

## Repair made (this run, edition-local only)

- New FINAL-artifact audit (`audit_rev1.py` §§11–12) asserts, on FINAL committed
  bytes: (i) P07A package inputs exact (4 canonical, byte-drift fails);
  (ii) B05 refs contain the D114 task (absence fails); (iii) SigLIP2 specifics on
  D114 and CLIP limits on D039; (iv) overlay P07A/D114 entry exists with
  SHA == accepted == matrix; (v) CLIP/D039 separation.
- Negative fixtures (`negative_fixture_p07a.py`, /tmp only): F1 (stripped B05 refs
  → check fails) and F2 (injected package input → canonical validation fails)
  both detected; control (real artifacts) passes. The validator can no longer
  pass the same failure class silently: any future loss of either level fails loudly.
