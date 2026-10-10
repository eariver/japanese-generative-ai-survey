# Core v2 maintenance handoff — W40 post-Evidence upstream supersession

Status: `CORE_MAINTENANCE_SPECIFICATION / NO_IMPLEMENTATION_AUTHORITY_IN_W40`
Related issue: https://github.com/eariver/japanese-generative-ai-survey/issues/562
Sol scope review: `sources/2026-W40/execution/reviews/sol-w40-selection-r11-scope-decision-20261010.md`
Reviewed Core main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
W40 branch: `weekly/2026-W40-v2-work`
Reviewed W40 Muse r11 final HEAD/Tree: `5b63d0c9f49610996658afbe072f5c996a92ddb5` / `0c6c67c9a4ef4feeddc23c06e06205c75b43587f`.

This document is an actionable specification for a **separately authorized Core maintainer**, not a permission to change shared Core or the W40 State in the current branch. The user or a Core supervisor must select a currently reviewed existing maintenance branch, supply an exact Starting SHA/Tree and reviewed main SHA, and approve the bounded implementation before it starts. The old remote `refactor/survey-production-core-v2` is 1,244 commits behind reviewed main and MUST NOT be assumed safe or rebased/force-pushed.

## User-visible problem and chosen editorial outcome

At W40 `EVIDENCE_REVIEWED`, two in-window original issuer announcements (AstaBrief, AutoSynthData) were erroneously HOLD due to `TIME_UNRESOLVED`. HF organization-hosted original `datePublished` UTC instants are available before Oct2 22:00Z. Sol approves provisional MATERIAL consideration for both, with original release method and availability caveats. Reviewed Core offers no sanctioned post-`EVIDENCE_REVIEWED` same-State upstream Acceptance correction. Issue #562 defines the gap.

## Required architecture of fix

- Safe new Core command/callable to **supersede a bounded set of earlier accepted authority after evidence review but before Selection/Human review**, without moving lifecycle backwards.
- Authenticate exact remote W40 branch SHA/Tree, reviewed Core implementation SHA, existing Accepted SHA/checkpoint provenance and per-source/materiality change allowlist.
- Enforce `EVIDENCE_REVIEWED`, `next_action=stage:selection`, Selection checkpoint pending, Architecture checkpoint pending, both Human Gates pending, Human review index empty; require exact explicit Sol review ID.
- Separate *original publication article timestamp* from unrelated model/file first-availability; use original HF org articles as primary sources without inflating source class or licenses.
- Before expanding changed upstream: determine whether original Discovery37 and Screening37/INSPECT can legally remain **unchanged**, while versioned Evidence Card Supplement (for AstaBrief and AutoSynthData) plus exact Views HOLD→MATERIAL, Materiality two-row corrections, Completeness revalidation and acceptance/checkpoint provenance are rebuilt. Prove with frozen validators. Expand boundary to Discovery/Screening only if a specific Core contract absolutely requires it; never silently rewrite those accepted artifacts.
- Preserve immutable old acceptance bytes and old SHA in append-only supersession record. All changed new Evidence/Views/Materiality/Completeness artifacts get fresh SHA, source role/time versions and deterministic reproducibility; reject absent issuer evidence.
- Prevent stale-HEAD write, partial commit, unauthorized candidate ID, post-Architecture override, Human review spoof, non-monotonic transition, source-time conflation, unrecorded old↔new SHA and double replay.
- Validate 35 Evidence/Card/View binding, 37 Ledger coverage, LIMITED Completeness, candidate selection preview, and historical checkpoint supersession identity end-to-end; no Selection Acceptance under Core maintenance.
- Tests: Weekly W40 repro + at least one non-Weekly profile regression, boundary and negative tests. No manual monkey-patching of shared scripts on W40 branch.
- Core maintenance must be implemented/reviewed through an explicitly authorized existing Core branch, normal PR and main integration; **no new branch** unless the user separately approves a new one. If no eligible current existing branch exists, report BLOCKED and require branch authorization; do not hijack stale refactor history.

## W40 follow-on ONLY after Core is reviewed

With reviewed new Core main and explicit Sol approval, prepare a separate exact Start SHA/Tree-guarded W40 run: create new source supplement and accepted Evidence/Views/Materiality/Completeness bound to valid older authority, keep State EVIDENCE_REVIEWED, re-review independently before Selection. Provisional 31 MATERIAL/2 HOLD/2 CONTEXT and Plan B Selection 30=22 PRIMARY/8 SUPPORTING require Core-backed verification and final Sol role decision.
