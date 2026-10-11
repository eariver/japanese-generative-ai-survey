# W40 Selection dossier r12 (PROPOSED reviewer input for Sol compat review — Core-gap bypass)

Status: `PROPOSED_NOT_ACCEPTED` — NOT canonical `SELECTION_COMPLETE`. Companion to
`selection-preview-r12.json` (35 assignments: 28 SELECTED = 20 PRIMARY / 8 SUPPORTING +
1 INSPECT + 4 HOLD + 2 REJECT; machine-recomputed in `count-audit-r12.json`) built on
UNCHANGED canonical staging `candidate-matrix-r10-staging.json` (SHA `f07b1166…`),
crosswalk-r10, evidence-accepted `ca5e21a7…` (set `0a62346f…`), views-accepted
(file `51887616…`, set `1effd744…`), ledger `ce63f3a9…`, completeness `f83b2d94…`.
Core `validate_selection` PASS (0 errors, unmodified reviewed-main Core).
This dossier revises ONLY the two HOLD rationales vs r10 (no merit/HOLD→SELECTED change).

## Reviewer assumptions (r10 + Sol r11 scope decision)

Sol r11 (`sol-w40-selection-r11-scope-decision-20261010.md`):
`SOL_W40_SCOPE_PLAN_B_APPROVED / CORE_REENTRY_CONTRACT_GAP / SELECTION_ACCEPTANCE_HOLD`.
Both HF-hosted issuer articles are IN-WINDOW and technically MATERIAL; the historical
"no precise original article timestamp" claim is WITHDRAWN. Canonical Evidence PARTIAL +
View/Materiality HOLD are nevertheless RETAINED in this unit for lack of a lawful
same-State upstream supersession (Issue #562); frozen Core would reject promotion.
Plan B (30 SELECTED) remains the desired eventual scope AFTER reviewed Core
supersession — NOT established here. DGX stays INSPECT; W39 carryovers stay HOLD;
Cloudflare pair stays unadmitted; post-window stays excluded.

## What changed vs r10 (exactly two rationale strings)

- `candidate:2026-W40:00ac1151955c20ff` (AstaBrief): HOLD retained, rationale now states
  VERIFIED IN-WINDOW `2026-10-02T15:19:50.340Z`, Sol Plan-B materiality, canonical-limitation
  reason, and pointer to staged non-canonical supplement
  `execution/editorial-supplement/r12/astabrief-note.md`. No role, usage NONE.
- `candidate:2026-W40:ba7d989d5b799f66` (AutoSynthData): HOLD retained, rationale now states
  VERIFIED IN-WINDOW `2026-10-02T04:01:31.290Z`, Sol Plan-B materiality, canonical-limitation
  reason, standalone-absence + Gym-separation caveats, and pointer to
  `execution/editorial-supplement/r12/autosynthdata-note.md`. No role, usage NONE.
- All other 33 assignments (28 SELECTED roles, DGX INSPECT, 2 W39 HOLD, 2 REJECT):
  byte-identical rationales/dispositions/usages/roles to r10.

## Packages (frozen 28; identical depth to r10)

P1 frontier-models (PRIMARY ×3: Sonnet/GPT-6.1/Argon, largest depth).
P2a generalist open weights (Holo4) + P2b Japanese-specialist (ELYZA), large.
P3 decision-inference (Ollama/Clef/Decider, separated axes).
P4 devday-product-surface (dots + Agents API PRIMARY; hub SUPPORTING spine).
P5 safety-provenance (five subsections: runtime/governance/watermark/attribution/MCP-auth).
P6a training-methods-and-systems (ContextLM + Olmo-core 3 PRIMARY; depth kept).
P6b evaluation-and-execution-infra (AgentPerf + OpenTTS PRIMARY; RL-Env SUPPORTING).
P7 multimodal-serving-observability (FLUX/VSS/ASR + Relay + Ross note).
P8 enterprise-industry-digest (short; DGX INSPECT decision for Sol).
Supplemental notes (AstaBrief/AutoSynthData) are NOT packages, carry NO roles, and
MUST NOT be cited as Core-accepted chapters. Their future home is either (a) P6a
expansion after reviewed Core supersession, or (b) a clearly separate human-reviewed
supplement if independently authorized — Sol decides later.

## Semantic conflict disclosed (source truth vs canonical HOLD)

Source truth (Sol-verified): both article events are in-window and material.
Canonical staging: both rows `materiality=HOLD`, views HOLD, ledger HOLD.
The r12 preview HONESTLY retains HOLD with corrected rationales instead of silently
promoting or falsely declaring out-of-window. `validate_selection` passes precisely
because non-SELECTED HOLD assignments carry no roles — the validator checks formal
consistency, not editorial completeness. The gap between "should eventually be
SELECTED" (Sol Plan B) and "cannot lawfully be SELECTED yet" (frozen Core) is the
documented CORE_REENTRY_CONTRACT_GAP, not a hidden defect.
