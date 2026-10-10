# W40 r11 Selection editorial counterfactual — A (unchanged) vs B (adopt both) (staged, NOT canonical)

Status: STAGED_R11 / PROPOSED_NOT_ACCEPTED / NO_CANONICAL_MUTATION
Basis (unchanged canonical): evidence-accepted set `0a62346f…` (35: 29 VERIFIED / 6 PARTIAL),
views-accepted file `51887616…` (set `1effd744…`; 29 MATERIAL / 4 HOLD / 2 CONTEXT),
ledger `ce63f3a9…` (37 rows), completeness `f83b2d94…`, dossier-r10 + proposal-r10
(35 assignments: 28 SELECTED = 20 PRIMARY / 8 SUPPORTING + 1 INSPECT + 4 HOLD + 2 REJECT).
Production State stays EVIDENCE_REVIEWED; Selection/Architecture pending; no SELECTED/MATERIAL change.

## Common ground (both plans)

- P6a = training-methods-and-systems (ContextLM + Olmo-core 3), P6b =
  evaluation-and-execution-infra (AgentPerf + OpenTTS PRIMARY; RL-Env SUPPORTING).
  Technical depth per r10 dossier is PRESERVED in both plans (equations/conditions/
  ablations for ContextLM/Olmo-core; serving-only scope + TTS metric disclaimers +
  Hub interop for P6b). Neither plan thins P6a/P6b to make room.
- P1 (Sonnet/GPT-6.1/Argon), P2a (Holo4) / P2b (ELYZA), P3 (Ollama/Clef/Decider),
  P4 (dots + Agents API; hub spine), P5 (five safety/provenance subsections),
  P7 (FLUX/VSS/ASR + Relay + Ross note), P8 (short digest; DGX INSPECT) are
  IDENTICAL in both plans.
- Vendor/publisher figures stay attributed, never independently reproduced.
  Guard stays v1/v2-only; Olmo report cells/ablations/code limits stay declared;
  FLUX weights/license stay unpinned; post-window (Oct 6/8/9) and Oct 2 day-only
  Cloudflare pair stay excluded in both plans.

## Plan A — current Selection maintained (28 SELECTED; both stay HOLD)

- Assignments: 28 SELECTED (20 PRIMARY / 8 SUPPORTING) + DGX INSPECT + 4 HOLD
  (Pixel Canary, TBC, AstaBrief, AutoSynthData) + 2 REJECT, exactly as proposal-r10.
- P6a stays 2 PRIMARY (ContextLM, Olmo-core 3). P6b stays 2 PRIMARY + 1 SUPPORTING.
- Editorial stance: the two in-window HF-hosted articles are acknowledged as real
  dated announcements but judged OUT OF SCOPE for the W40 narrative (e.g., report
  generation judged a product-feature story; synthetic-curriculum judged a methods
  note without released code). HOLD rationales would need rewriting from
  "TIME_UNRESOLVED" to scope-based reasons — which itself requires canonical
  upstream revision (see re-entry report), so even Plan A is NOT zero-cost if it
  wants to stay honest about the new clocks.
- Costs: (a) omits the only open-weights cited-report model release in-window and the
  only environment-validated synthetic-curriculum method in-window; (b) leaves P6a
  without any data-generation-curriculum voice and leaves science-report generation
  entirely to Olmo-core/ContextLM side remarks; (c) invites a reader-visible gap:
  two issuer-announced Oct 2 items with in-window clocks absent without a published
  scope reason. Benefits: smallest narrative churn; no new comparison tables; P8
  digest untouched.
- Verdict on Plan A: editorially DEFENSIBLE only with an explicit, Sol-approved
  scope rationale (not the now-false TIME_UNRESOLVED). Without that, omission reads
  as stale HOLD rather than judgment.

## Plan B — conditional adoption (both qualify; +2 SELECTED, P6a/P6b depth kept)

- Assignments (PROPOSED, not accepted): 30 SELECTED (22 PRIMARY / 8 SUPPORTING) +
  DGX INSPECT + 2 HOLD (Pixel Canary, TBC) + 2 REJECT. Deltas: AstaBrief HOLD→PRIMARY,
  AutoSynthData HOLD→PRIMARY. No other assignment changes.
- Placement (P6a/P6b depth maintained):
  - AstaBrief → NEW P6a third PRIMARY subsection (or a compact P6a-extension):
    "open-weights cited-report generation (Qwen3-8B → SFT47K/DPO6K, one-pass pipeline,
    51.1s vs 178.5s, Apache-2.0 weights / cc-by-nc-4.0 data, 2025-era baselines,
    evaluation-not-rerun caveat, scope-preservation limit)". Comparison table:
    ContextLM (method) vs Olmo-core (systems) vs AstaBrief (post-training + pipeline
    for grounded synthesis) — mechanisms/metrics/conditions never blended.
    Alternative placement (NOT recommended): P2 open-reasoning — rejected because
    AstaBrief is a report-generation post-training story, not a general reasoning release.
  - AutoSynthData → NEW P6a fourth PRIMARY subsection (methods):
    "capability-gap-driven synthetic curriculum (target/multiply phases, sample/batch
    gates, positive/negative verifier gates, bounded repair; Hybrid +7.2pp/35% and
    ITSM 18.77%→27.18% publisher-measured, SFT-only, Gym-scoped; NO standalone
    code/dataset)". Comparison table: data Mixes (SFT/DPO curation in AstaBrief) vs
    curriculum generation (AutoSynthData) vs infra (Olmo-core) — kept distinct.
  - P6b UNCHANGED (no migration of either item into evaluation-infra; RL-Env stays
    the Hub-interop SUPPORTING item; AutoSynthData's Gym usage is cited as background,
    not merged with RL-Env).
  - P8 digest UNCHANGED (neither item belongs in enterprise digest; both are
    training-methods stories).
- Space budget: P6a grows from medium-large to large (two added subsections with
  tables); P1/P2/P6b/P3/P5/P7 keep relative depth; P8 stays small. Total narrative
  grows modestly; compression guard (28-item spine vs ≤1-collapse tripwire) would be
  re-baselined to a 30-item spine by Sol, not by this unit.
- What Plan B does NOT claim: no weight-release instant for AstaBrief beyond the
  article event (model createdAt Feb 9 / datasets Sep 29 distinguished); no
  AutoSynthData code/dataset/service release (method-only, Gym distinguished);
  no cross-vendor ranking; no independent benchmark reproduction.

## Recommendation (for Sol, NOT an acceptance)

- Both items clear the in-window bar as article events AND are technically material
  (AstaBrief: only open-weights cited-report model + data release in-window with
  citational-grounding lessons; AutoSynthData: only environment-validated synthetic
  curriculum with explicit verifier-gate methodology in-window). Plan B is the
  editorially stronger narrative PROVIDED Sol authorizes the canonical upstream
  revisions listed in the re-entry report.
- If Sol judges either item out-of-scope on merit (not time), Plan A remains available
  but needs rewritten HOLD rationales via the same lawful re-entry path.
- Either way: no canonical files change in this unit; the next lawful step is Sol's
  scope adjudication (r11), then a separately authorized bounded regeneration run.
