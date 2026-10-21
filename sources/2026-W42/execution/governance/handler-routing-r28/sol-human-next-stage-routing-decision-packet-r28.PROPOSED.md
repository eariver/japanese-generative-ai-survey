# W42 r28 — Sol/Human next-stage routing decision packet (PROPOSED, NOT a Gate)

Status: `HUMAN_REVIEW_REQUESTED / ROUTE_DECISION_AWAITS_SOL_PRESENTATION / NO_CANONICAL_ADVANCE`.
Human conditional Route A approval stands; r1 stays byte-exact; no Reader/Gate/Publication/Freeze/Release.

## Decision tree

1. **Routing proven? YES** — operator-bridge `ADVANCE_STAGE` executes the exact DRAFT_COMPLETE→VALIDATED_DRAFT
   contract without the missing registry names (proof docs in this directory). No Core maintenance required for routing.
   - IF Sol/Human accept this proof → authorize a future bounded canonical unit (separate contract) to author the 7
     exact-byte artifacts and submit an operator-bridge `ADVANCE_STAGE` request (`expected_from_state: DRAFT_COMPLETE`).
   - IF rejected → Route C: record blocker; Core-maintenance triage owns any registry/config work (separate repo workflow, never edition-local).
2. **No alias/shim route exists or is authorized.** The semantic-publication pair is proven contract-incompatible;
   the r11 shim prohibition stands. Any future proposal to rebind names must go through Core maintenance, not W42 edition work.
3. **Secondary gap (config lists 6, code requires 7 incl. `reader-surface-gate`)** travels with the packet as a build
   instruction for the future canonical unit, and as a Core-maintenance awareness item. It does not invalidate routing.

## Earliest safe canonical operation IF separately authorized (no promise of publication)

1. Bounded unit authors, under r1 and the Human ~21pp acceptance: formal `reader-manuscript-v2.json` (r18-derived,
   coverage 1:1 with r1 packages×must-cover), canonical `surveys/weekly/2026-W42/main.tex` + exact PDF,
   `quality-regression-bundle-v2.json`, `semantic-editorial-review-v2.json` + `visual-review-v2.json` (ChatGPT reviews),
   `reader-surface-gate` PASSED record — all byte-exact and mutually binding.
2. Operator-bridge `ADVANCE_STAGE` request (expected_from_state `DRAFT_COMPLETE`) advances to `VALIDATED_DRAFT`
   (checkpoint `validation`).
3. `stage:publication-candidate` → `RELEASE_CANDIDATE` → Human Publication Preview Gate (separate decision, separate dossier).

## Questions for Sol/Human (answer explicitly; silence decides nothing)

1. Accept the bridge-path routing proof as satisfying the Human approval §3 condition precedent? (Yes / No / Needs-more-evidence: specify)
2. Authorize the future bounded canonical unit described above? (Yes with contract / Defer / No)
3. Direct the 6-vs-7 artifact-list asymmetry to Core maintenance now, or carry it as a build instruction for the canonical unit? (Now / Carry)
4. Confirm the registry gap needs NO Core change for W42 (orchestrator CLI unused by authorized transports)? (Confirm / Dispute with evidence)

## Known unknowns

- Formal manuscript/candidate bytes, semantic/visual verdicts, surface-gate PASSED status — all future-unit work.
- Whether other editions/profiles rely on the orchestrator-CLI path (out of W42 scope; Core maintenance may care).
- Sandbox log `/tmp/r28-sandbox/r28_routing_tests.log` is machine-local and not committed; the committed docs above
  record commands, code lines, and hashes needed to reproduce.
