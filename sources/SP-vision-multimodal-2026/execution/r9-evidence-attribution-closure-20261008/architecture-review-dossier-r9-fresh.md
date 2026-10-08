# TS-003 Human Architecture Review Dossier — r9 candidate, corrected Evidence authority (fresh)

Status: `ARCHITECTURE_REVIEW_R9_PENDING / DOSSIER_FRESH / NO_APPROVAL_RECORDED`

- Edition: `SP-vision-multimodal-2026` (THEMATIC / LONGFORM_SPECIAL)
- Revision: Architecture r9 candidate (`architecture-v2.json`, status PROPOSED)
- Lifecycle: `ARCHITECTURE_ESTABLISHED`; gates: architecture_review `pending`,
  publication_preview `pending`; no active approval.
- Reviewed bytes: the exact pushed head of branch
  `special/vision-multimodal-2026-work` for run
  `execution/r9-evidence-attribution-closure-20261008` (HEAD/Tree in the run's
  final report; verifiable via the branch head).
- Prior authority: r8 APPROVED records preserved as history; previous r9 dossier
  (`p02-detr-bridge-intake-r9-20261008/architecture-review-dossier-r9.md`) is
  SUPERSEDED by this fresh dossier (kept untouched as history; NOT the active
  review surface). Previous r9 candidate semantics are preserved; only Evidence
  attribution + hashes changed (rebind diff
  `architecture-r9prev-to-r9rebound.diff`, basis-only).

## 1. What changed since the previous r9 surface

- Technical P02 lineage repair: UNCHANGED (Deformable/DAB/DN bridges → DINO
  convergence; parallel/convergent wording; page budget 6; 15 packages identical).
- External review found a source-binding defect: predecessor cards carried
  DINO-authored inheritance as predecessor-source-local AUTHOR_CLAIMs.
- Evidence authority corrected (no new Discovery/intake; counts 125/124 held):
  VM-D011 +1 DINO-source-local AUTHOR_CLAIM (paper-stated predecessor lineage);
  VM-D123 claim-3 rewritten Deformable-native; VM-D124 claim-3 removed;
  VM-D125 claim-3 removed. Statuses revalidated, not forced (119/5 held).
- Downstream rebound through normal machinery: Evidence acceptance `6b55033d…`,
  Views, ledger (125 rows), completeness (VM-O02 SATISFIED, 14/2), Selection 124,
  matrix, Architecture candidate (semantics zero-delta), summary/attention.
- VM-D011 now owns the DINO-authored predecessor lineage claim; VM-D123/124/125
  are source-local again (fresh Sol consumption review r9b verifies every
  AUTHOR_CLAIM tuple: text/class/source_ids/registered source/context/subject).
- No Draft regenerated (rev5 historical only; draft checkpoint pending).

## 2. Research coverage

Discovery 125 (122 carried + 3 bounded bridge primaries); no new intake in this
run. Negative-space position unchanged (Conditional/Anchor DETR documented
omissions). X/Grok NOT_REQUIRED (unchanged).

## 3. Evidence quality

Acceptance `6b55033d02efecf69d784ebe8af534058222f84e37668b16c6341f8cc2deacd5`:
124 results, VERIFIED 119 / PARTIAL 5. Four material authorities CONSUMED with
correct source binding (see §1 + Sol r9b review). Screening 125 (D122 DROP
carried). No forced statuses.

## 4. Candidate map

124 SELECTED (121 carried + Deformable PRIMARY / DAB SUPPORTING / DN PRIMARY).
DINO capstone toward Grounding DINO; name disambiguation preserved.

## 5. Omission review

Unchanged from the previous r9 dossier (§4 there), plus: no new omission created
by the attribution repair (claim removals moved statements to their correct
subject home; nothing deleted from the authority).

## 6. Editorial thesis / packages / pages

Unchanged: r9 P02 design preserved in full (bridges, convergence wording,
disambiguation, budget 6). Other 15 packages identical.

## 7. Counterfactuals

Unchanged: wording-only fix rejected (defect was authority, correctly repaired as
authority); taxonomy expansion rejected again (no new contradiction found —
had one appeared, the run would have STOPPED per bounds).

## 8. Limitations / risks

- New DINO claim-3 is bounded to what DINO explicitly states (no
  over-generalization; Sol-verified).
- rev5 Draft not regenerated; queued Draft corrections (§17 list) still deferred.
- Coverage Freeze active with the single recorded P02-bridge exception (unchanged).

## 9. Sol findings and recommendation

- Fresh Sol evidence-consumption review r9b: PASS (supersedes the incorrect r9 PASS).
- Sol blocking findings: none.
- Recommendation: Human APPROVED (continue to fresh Draft) or REQUEST_CHANGES
  with a pre-Architecture boundary. No worker approval; no Draft; no publication.

## 10. Human decision options (only now that the above is presented)

- `APPROVED` — record against the durable reviewed commit via the Human Gate
  mechanism; then continue to drafting.
- `REQUEST_CHANGES` — supply requested changes + one allowed pre-Architecture
  regeneration boundary; Core invalidates only affected downstream authority.
