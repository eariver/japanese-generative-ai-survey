# W43 Sol Screening r2 independent review — mechanical PASS, bounded chronology correction

Status: `SOL_SCREENING_R2_REVIEW / MECHANICAL_PASS / LIMITED_REQUEST_CHANGES_CHRONOLOGY`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Reviewed W43 branch HEAD/Root Tree: `757d62c59d82d0e9745e27734756ee984c79623e` / `d5bfb59280bc65b40bf7d491eb4be152cab521c8`
Reviewed main SHA/Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`
Frozen Core SHA/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## Reviewed authority

- Muse Screening r2: `execution/SOL_SCREENING_REVIEW_HANDOFF-r2.md`, `execution/sessions/muse-w43-screening-native-r2-20261025.md`, `execution/source-intake/w43-screening-summary-r2.md`.
- Worker r2 normal commit has exact starting parent `d38035814c9cd4541849b37d542c709812a876c8`. All 23 changed paths are W43 edition-local; no Production State, Human Gate, Source Intake, Frozen Core, W42, or protected path mutations.
- Actual frozen first-party agent-first adapter `scripts/survey_agent_tool_v2.py` used for Screening prepare and accept, confirmed from worker log and same Core paths. Worker reports 5/5 adapter unit tests PASS; isolated tampered State rejected with 12 real errors; legacy direct path still FAIL (expected and correctly retained in Issue #568). Sol independently inspected frozen source to verify allowed helper, current SHA admission, agent-first State verifier and scoped finally restoration. Sol has NOT independently run worker-local CLI.
- Content-addressed accepted Screening:
  `sources/2026-W43/screening/v2/accepted/185257742e7a5ad7d2253312e4cc1bd731da6fd9fe484f7b978a8de85f5e93af/screening-accepted.json`
  51 records in 4 batches (13/13/13/12). Package SHA256 `b7e9a6d4b138ef3c9ceb06f76537d9bf23ba26796475b9c2933e9ad36b718aa0`; copied accepted `package.json` Git blob `e953040252dc0f1ff42bb0e8ee534d6122c3bf41` is exactly equal to active r1 Screening package. Accepted result digest `185257742e7a5ad7d2253312e4cc1bd731da6fd9fe484f7b978a8de85f5e93af`, 51/51 unique IDs, no unsupported verdicts/invalid confidence fields.
- Actual decisions: `KEEP 17 / MAYBE 11 / INSPECT 4 / DROP 19`. Seventeen technical KEEP rows have substantive verification targets; 12 W42 carries have explicit dispositions (11 DROP / 1 MAYBE), eight out/background rows DROP, four locator/RSS INSPECT. X observation ledger MAYBE as audit binder, not technical model news. No inflated independent reproductions. Worker reports agent-first Core Screening `validate_acceptance` and Stage precheck PASS. Sol read back every decision and the accepted package structure.

## Human decision

**NONE / NOT_APPLICABLE.** Sol Screening editorial review is not an Architecture Review or Publication Preview Human Gate. Both real Human Gates are `pending`. This review grants NO machine `ADVANCE_STAGE` authorization until chronology regression is repaired.

## Requested changes

One concrete **regression in the immutable accepted Screening decision**:
- Record `w43-primary-kimi-20261023` has reason `Oct 23 17:15:24Z (45min inside cutoff, X HTML archived)`. That arithmetic is wrong: W43 ordinary end `2026-10-23T22:00:00Z`; announcement `2026-10-23T17:15:24Z`. Difference = **4h44m36s**, not 45 minutes.
- The actual accepted Discovery record (unchanged) already says `17:15:24Z (13:15 EDT, 4h44m before cutoff)` and `metadata.r3_correction = 'r1 21:15Z/22-digit/45-min errors fixed'`. Screening r2 thus *reintroduced the identical old error* explicitly removed at Discovery r3.
- Keep Kimi's **KEEP**, event identity, 19-digit X post ID, official first-party raw, future Nov 4 weights, confidence, scope, vendor-claim caveats and verification targets. Correct ONLY its Screening decision `reason` to say `Oct 23 17:15:24Z (4h44m36s before Oct 23 22:00Z cutoff, X HTML archived)`.
- No other substantive Screening defects found in readback, including 17 KEEP / 11 MAYBE / 4 INSPECT / 19 DROP and X/carry/OUT dispositions. The attached worker summary had a self-corrected '(7)' then '8' OUT background typo, but overall eight-list/count and result decisions agree; this does not require regenerating Screening.
- **Do not mutate the historical r2 original** or accepted content-addressed directory. Create one new screened result set under a distinct SHA by using frozen Core-native Screening `prepare` and `accept`, with a new W43 package run dir, reproducing all 51 decisions except the one text reason. Avoid reclassifying or re-researching content.

## Regeneration boundary

**Edition-local Screening metadata correction r3 ONLY**. Keep 51 immutable accepted Discovery records/X raw, State `DISCOVERY_COLLECTED`, Stage checkpoint, prior failed r1/accepted r2, Frozen Core and Human Gates unchanged. Use original frozen agent-first `survey_agent_tool_v2.py` for Core `prepare` and `accept`; negative integrity tests, result/input SHA and exact 51-ID diffs. Do not manually forge content-addressed acceptance or `ADVANCE_STAGE`. Stop `SOL_SCREENING_REVIEW_READY_R3` for Sol final readback. If Core fails: BLOCKED/stop, no bypass.

## Shared-Core implication

**None new**. Legacy direct-CLI mismatch tracked in existing Issue #568 and remains open; frozen native adapter passed r2. This editorial chronology regression is W43 edition-local, NOT a Core defect.
