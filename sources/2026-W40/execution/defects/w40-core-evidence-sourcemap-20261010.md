# Shared-Core defect (deferred maintenance, NO patch applied)

Date: 2026-10-10Z (Muse r4 Evidence preparation)
Edition: 2026-W40 (branch `weekly/2026-W40-v2-work`)
Core file (READ-ONLY, not modified): `scripts/survey_evidence_v2.py` (`SOURCE_CLASS_MAP`)

## Symptom (exact evidence)

`survey_evidence_v2.task_authority_sources()` raises for W40 canonical Discovery
`source_type` values established during Sol-reviewed Discovery (r1 register
authority classes, preserved through r3 PASS):

- `PRIMARY_RESEARCH_ABSTRACT` (records `w40-primary-contextlms-20260929`,
  `w40-prewindow-lift-20260925`; arXiv abs pages) →
  `ValueError: unsupported source_type for Evidence authority: 'PRIMARY_RESEARCH_ABSTRACT'`
- `EVALUATOR_PUBLISHER` (record `w40-primary-aa-agentperf-20260929`;
  Artificial Analysis article) →
  `ValueError: unsupported source_type for Evidence authority: 'EVALUATOR_PUBLISHER'`

Reproduction (read-only, no writes):

```text
PYTHONPATH=<repo> python3 -c "
from pathlib import Path
from scripts import survey_evidence_v2 as ev
from scripts import survey_production_v2 as core
repo = Path('.').resolve()
pkg = core.load_json(repo / 'sources/2026-W40/evidence/v2/packages/r1/package.json')
for m in pkg['tasks']:
    tp = Path('sources/2026-W40/evidence/v2/packages/r1') / m['path']
    ev.task_authority_sources(repo, core.load_json(tp), pkg)  # raises on 3 tasks above
"
```

(`x-community-signal` IS mapped to SOCIAL, so the Grok ledger task is unaffected.)

## Impact assessment (bounded)

- Discovery Acceptance (37), Screening acceptance (37), Evidence package
  preparation (35 tasks) all succeeded — only the task-source authority
  resolution for the 3 records above is affected.
- Reviewer-input Evidence records (`evidence/v2/results/r1/interactive-evidence.json`,
  35/35 structurally valid) were validated WITHOUT the task-source binding
  check (`task_source_ids=None`); record fields, exact non-DROP coverage, and
  completeness were fully validated.
- Future `accept_evidence_results` (post-Sol review) WILL fail closed on these
  3 tasks through the same map gap. This blocks Evidence Acceptance mechanics,
  NOT the Sol authority-consumption review of the 35 records' substance.

## Requested disposition (Sol / Core maintenance, separate from edition)

1. Add `PRIMARY_RESEARCH_ABSTRACT` (→ `PRIMARY_PAPER`: arXiv abs pages) and
   `EVALUATOR_PUBLISHER` (→ publisher-measured evaluation; closest existing
   class or a new explicit class) to `SOURCE_CLASS_MAP` via reviewed Core
   repair, OR direct an edition-local reclassification that Sol accepts.
2. Do NOT silently remap inside the edition (shared roots are read-only during
   production).
3. After repair, rerun the task-source binding check over the 35 records as
   failed formal evidence (must be rerun cleanly after reviewed repair).

## Edition-local handling in r4 (no Core change)

- Map gap openly recorded here + in handoff residual blockers.
- No invented source classes; no Core file touched (`git diff` over
  `config/ schemas/ scripts/ .github/workflows/ docs/` must stay empty).
