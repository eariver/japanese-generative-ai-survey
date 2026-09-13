# W34 Evidence Authority Expansion r2

## Session identity

- Issue: `2026-W34`
- Branch: `weekly/2026-W34-v2-work`
- Exact starting SHA: `6f3d45ef30036df91e1c75f31e9c0e547de411a7`
- Reviewed main SHA: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Session directory: `sources/2026-W34/execution/luna/w34-evidence-authority-expansion-r2/`
- Work type: additive pre-Human operator-quality Evidence research and capture

## Start guard

Read-only remote verification passed before any repository write:

| Ref | Required SHA | Observed SHA | Result |
|---|---|---|---|
| `origin/weekly/2026-W34-v2-work` | `6f3d45ef30036df91e1c75f31e9c0e547de411a7` | `6f3d45ef30036df91e1c75f31e9c0e547de411a7` | PASS |
| `origin/main` | `a9f121f0d65591f52b53515712d7c0bae573b2ef` | `a9f121f0d65591f52b53515712d7c0bae573b2ef` | PASS |

The local checkout was detached at the exact starting commit for read-only inspection. No new branch was created.

## Mandatory read and Core preflight

The requested current-branch authority files were read in order: `AGENTS.md`; the production Core session bootstrap; Weekly Profile, X intake, and execution-record policy; the W34 production profile and State; execution index; checkpoint instruction; prior r1 worklog; profile completeness; candidate matrix; candidate selection; Architecture; Architecture Review Summary and Attention; and the active accepted Evidence and Edition Views records.

The reviewed main Core was inspected read-only. The result is recorded in `core-recovery-assessment.json`:

- Supported pre-Human regeneration mechanism: **unavailable**.
- Evidence runners require `CANDIDATES_NORMALIZED` and refuse canonical overwrite.
- Selection and Architecture runners require `EVIDENCE_REVIEWED` and refuse canonical overwrite.
- Stage validation rejects local transitions while State has `terminal_reason=HUMAN_GATE_REACHED`.
- The only invalidation/revision route requires an actual Human `REQUEST_CHANGES` record.
- Therefore no Human decision was created, no review round was incremented, and no State/checkpoint rollback or manual repair was attempted.

## Additive authority expansion

The 80 non-DROP accepted Evidence tasks were each given a task-specific primary-source verification attempt. DailyX, Grok, and ordinary X observations remained discovery/locator signals. The ledger records the candidate-local claim, chronology, W34 relation, attempted official locators, capture outcome, raw path, SHA-256, unresolved reason, and next disposition.

- KEEP attempts: 45/45
- INSPECT attempts: 16/16
- MAYBE attempts: 19/19
- Total verification records: 80/80
- Retrieval targets attempted: 83
- Newly captured exact, substantive authority target bodies: 61 (60 unique SHA-256 bodies; the OpenAI API changelog was intentionally captured under two task relations)
- Non-substantive success bodies retained for provenance: 4
- HTTP error responses retained for provenance: 4
- Timeout/empty-body attempts retained for provenance: 14

See `verification-ledger.json` for the task-level ledger and `source-retrieval-provenance.json` for every response body/header outcome. The existing Transformers v5.15.1 primary raw record was retained unchanged and referenced as a regression source; it is not counted as newly captured.

## Before / research-only after

| Surface | Previous accepted canonical result | Research-only result in this session | Canonical replacement |
|---|---|---|---|
| Evidence | `PARTIAL 80 / 80` | `VERIFIED 32`, `PARTIALLY_VERIFIED 27`, `UNRESOLVED 14`, `OUT_OF_WINDOW 7` | Not generated; Core path unavailable |
| Edition Views | `MATERIAL 1`, `CONTEXT 45`, `HOLD 34` | 19 MAYBE tasks individually researched; no canonical rejudgement written | Not generated |
| Completeness | `LIMITED` | Limitations narrowed to task-local authority, access, and chronology boundaries in ledger | Not regenerated |
| Selection | `SELECTED 1`, `HOLD 64`, `INSPECT 15` | No selection mutation; current accepted selection preserved | Not regenerated |
| Architecture | 1 package: `Transformers v5.15.1` | No Architecture mutation; current unpresented surface preserved in history | Not regenerated |

The research-only result is not a replacement acceptance. It is preserved to enable Sol review of the Core gap without fabricating a Human revision.

## Major retained unresolved boundaries

Candidate-local primary authority remains unresolved for C002, C007, C026, C027, C035, C037, C038, C044, C054, C056, C058, C085, C093, and C097. Additional partially verified candidates retain explicit blocked-body or chronology boundaries, especially AWS/Google Cloud pages and claims that combine a first-party event with a secondary technical detail. The ledger must be consulted before any later supported regeneration.

## Preservation and exclusions

- The pre-existing operator-generated Architecture Review surface at the starting commit remains recoverable in Git history.
- Existing accepted Screening authority was not changed.
- Existing accepted Evidence, Edition Views, Materiality, Completeness, Selection, and Architecture artifacts were not deleted or overwritten.
- No shared Core file was edited.
- No publication-boundary validator or authority-auditor sidecar was run.
- No Human review record was created (`0`); no `REQUEST_CHANGES`, `APPROVED`, reviewer, timestamp, or review reference was invented.

## Stop status

`NEEDS_SOL_REVIEW / PRE_HUMAN_EVIDENCE_REGENERATION_CORE_GAP`

Formal Evidence-to-Architecture regeneration and stage validation were intentionally not run because the reviewed Core does not legally support that operation at the current unpresented Human Gate. The final pushed branch SHA is reported in the completion handoff.
