# ADDENDUM R17 — withdrawal of r16 Handoff §1 `HEAD == main` wording (R16-F02)

Status: `ADDITIVE_CORRECTION_R17 / HISTORICAL_BYTES_PRESERVED`
Scope: withdraws ONE ambiguous phrase in
`execution/SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_HANDOFF.md` §1.
That file's bytes are PRESERVED IMMUTABLE (no edit); this addendum is the correction
record. Addresses Sol finding `R16-F02` (MINOR, ACCEPTED).

## Withdrawn wording

r16 Handoff §1 stated (exact): "remote main == `afdb3df3…` == reviewed main;
HEAD == main. ALL MATCH → proceeded."

Read as SHA equality between the W40 work branch and main, that sentence is
INACCURATE and is hereby WITHDRAWN. In its author's context `HEAD` meant the remote
symbolic default-branch HEAD (`git ls-remote origin HEAD`), but the bare `HEAD == main`
form falsely implies `weekly/2026-W40-v2-work HEAD == main HEAD`. No Git evidence is
rewritten; the original sentence stays in the historical file with this withdrawal
attached.

## Exact identities (r16 run; independently re-readable from remote)

- r16 preflight W40 branch HEAD == `109ddbddd8c00f81f58302d261750cfd26e14f2e`,
  Tree == `13258c731f72f5b624c48ccb2953b77fcd6da596` (== r17 Starting SHA/Tree by
  succession; r16 instruction's outer values, verified read-only pre-write).
- Remote main HEAD == reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1`,
  SEPARATELY. The two branch SHAs are DIFFERENT (`109ddbddd…` ≠ `afdb3df3…`).
- Remote symbolic `HEAD` == `afdb3df3…` (default branch pointer == main) — the only
  true reading of the withdrawn phrase.
- Final r16 W40 HEAD `aad4b80e6b1c767671a5ecfe8c9d2e3166743bb7`,
  Tree `8f76727e1345dc5220714258ca09b2e7e6f7eb58` (FF child of the r16 start,
  non-force pushed, remote-readback verified).

## Rule going forward (r17 and later)

Always distinguish three separate assertions, never collapse them:
1. `remote W40 branch HEAD == Expected W40 Starting SHA` (work-branch lineage);
2. `remote main HEAD == Reviewed main SHA` (reviewed-Core authority);
3. `remote symbolic HEAD` (default-branch pointer; informational only).
A "match" verdict requires (1) AND (2) AND tree equality; (3) is never a substitute
for either. No false branch-equality implication is authorized.
