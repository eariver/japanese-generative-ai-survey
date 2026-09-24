# TS-002 Sol Evidence Provenance Readback r1

Status: `PASS / MATERIALITY_ADVANCE_AUTHORIZED`

Issue: `SP-beyond-text-2026` / GitHub Issue #526
Date: 2026-09-25 JST
Branch: `special/beyond-text-2026-work`
Reviewed execution commit: `6040cac486a49e3961aa9bd1a82af242348dadcd`
Reviewed tree: `838b6100025d84a85ee22d2371dac5d7aacb73ee`
Reviewed main: `0bbb02b3c5963403860897daec2feaf61e82589a`

## Decision

The bounded provenance rebind is accepted.

The prior semantic-depth decision remains in force:

- Evidence semantic depth: PASS
- Layer A factual Evidence / Layer B transition synthesis separation: PASS
- Source-body consumption discipline: PASS_WITH_DECLARED_PARTIAL_AND_BLOCKED
- Provenance rebind: PASS
- Materiality / Completeness / Selection / Architecture advance: AUTHORIZED

## Readback findings

1. Remote work branch fast-forwarded directly from `1e6679011bf33b0353bfae06cde8991415935abf` to `6040cac486a49e3961aa9bd1a82af242348dadcd`; no alternate branch/history rewrite observed.
2. Main remained at the reviewed `0bbb02b3c5963403860897daec2feaf61e82589a` / tree `e4ddde5ed5059d303b818f54e27204369b256bcb`.
3. 24 Discovery source identities were rebound and old locators preserved in `execution/provenance-rebind-20260924/provenance-repair-manifest.json`.
4. The 21 r2 `corrected_body_id` transcription defects were propagated into canonical Discovery and downstream hash-bound artifacts.
5. BT-D062 was correctly rebound from the SeamlessM4T-v1 authority to `2312.05187`, re-consumed from the v2/Seamless body, and rebuilt using v2-only facts.
6. BT-D089 was rebound to the ICASSP 2015 / IEEE LibriSpeech authority and correctly remained PARTIAL.
7. BT-D024 was rebound to `CompVis/stable-diffusion` and correctly remained NEEDS_MORE because repository-body/version binding was not consumed during the bounded repair.
8. The new Evidence result set preserves the declared uncertainty boundary: 126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE. No unresolved source was promoted merely because its locator was repaired.
9. Discovery remains 139 records; Screening semantics remain KEEP 134 / MAYBE 3 / INSPECT 2 / DROP 0; Evidence and Edition Views remain 139 each.
10. r1 Evidence and semantic-depth r2 Evidence were preserved as immutable prior authority.
11. `validation-rebind.json` reports all required checks passing, including no known wrong locator in VERIFIED cards, transition-ledger reference validity, shared-Core immutability, and Materiality not yet entered.

## Residual boundaries to carry forward

The following are not repair failures and must remain visible to Completeness / Selection / Architecture:

- BT-D022 EDM: abstract-level only; body-level design-space ablations remain unresolved.
- BT-D024 Stable Diffusion public repository: identity corrected, exact body/version binding unresolved.
- BT-D059 VALL-E 2: partial body/table coverage.
- BT-D072: blocked authority.
- BT-D076 Movie Gen: method/evaluation body incomplete.
- BT-D083 FID: full body not consumed.
- BT-D089 LibriSpeech: body not consumed.
- BT-D091 ITU BS.1534: full Recommendation gated.
- BT-D098, BT-D106, BT-D120, BT-D125, BT-D134: retain their current PARTIAL / NEEDS_MORE boundaries.
- LOW_SIGNAL lanes already recorded by Discovery/X/Evidence must not be upgraded by narrative confidence.

## Editorial constraint for next stages

TS-002 is not to be compressed into a product catalog or a short diffusion-centric survey.

Materiality, Completeness, Selection, and Architecture must preserve the semantic coordinate established by the 43-entry transition ledger:

`representation -> generative process/objective -> conditioning/alignment -> control/reference -> editing -> temporal/long-horizon structure -> runtime/deployment -> evaluation validity -> multimodal convergence`

For major historical transitions, the selected architecture should retain, where evidence supports it:

`prior bottleneck -> changed representation/mechanism/objective -> improvement -> trade-off/new failure -> successor/inheritance`

The 64-96 page planning range remains editorial guidance, not a hard cap. Completeness or Selection must not reduce depth merely to minimize page count.

## Authorized next stop

Proceed through canonical Materiality -> Completeness -> Selection -> Architecture and stop at a fresh Human Architecture Review.

Do not enter Draft, Validation, Publication Preview, Freeze, or Release before that Human Gate.
