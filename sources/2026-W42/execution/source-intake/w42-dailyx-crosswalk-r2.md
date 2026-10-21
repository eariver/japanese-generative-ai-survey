# W42 Daily X crosswalk r2 — MECE fix (73/73, each topic exactly once)

Supersedes r1 counts (which overlapped IN/DUP/UNVER). Raw originals unchanged. Window: UTC `[2026-10-09T22:00:00Z, 2026-10-16T22:00:00Z)`.

## Mutually exclusive buckets (sum = 73)

| Bucket | Meaning | Count | Members |
|---|---|---|---|
| B1 PROPOSED | Canonical basis of a proposal record (r1 carried or r2 added-grok-scale) | 40 | R1: 1-1,1-2,1-6,1-8,1-9,1-12 (6); R2: 2-1,2-5,2-7,2-8,2-9,2-11 (6); R3: 3-1,3-2,3-3,3-5,3-6,3-7 (6); R4: 4-1,4-2,4-3,4-5,4-6,4-9 (6); R5: 5-3,5-4 (2); R6: 6-1,6-2,6-3,6-4,6-5,6-6,6-7 (7); R7: 7-2,7-3,7-4,7-5,7-7,7-9,7-11 (7) |
| B2 DUP | Later mention of a B1/B5-family event, folded (no separate record) | 13 | 3-4 (→1-2 family), 3-8 (→3-1), 4-4 (→4-1), 4-7 (→3-5), 4-8 (→3-1), 5-1 (→4-1), 5-2 (→3-1), 5-7 (→4-1/5-1), 5-9 (→4-2), 5-10 (→4-5/4-6 bundle), 7-1 (→6-2), 7-6 (→4-1), 7-8 (→6-1) |
| B3 OUT-BG | Official event outside W42 (background only, never promoted by chatter) | 4 | 1-3 (Haiku 5.5 Oct 7), 1-4 (Gemini agent Oct 8), 2-2 (EmbeddingGemma 2 Oct 6), 2-3 (Motion/Dashboards ~Oct 8) |
| B4 OMITTED | In-window but no record, each with grounded reason below | 16 | 1-5,1-7,1-10,1-11,2-4,2-6,2-10,2-12,3-9,3-10,5-5,5-6,5-8,6-8,7-10,7-12 (16) |

Check: 40 + 13 + 4 + 16 = 73 ✓. Every 1-1..7-12 appears exactly once (verified by script below).

## B1 → record map (40 topics → 40 records)
- 1-1→w42-dailyx-grok-purchasing-20261010; 1-2→w42-primary-anthropic-unintended-20261009; 1-6→w42-lead-oss-video-roundup-20261010; 1-8→w42-lead-splashboard-qwen38-20261010; 1-9→w42-dailyx-agenthorizon-20261010 (r2 REVISED); 1-12→w42-lead-sulphur2-20261010.
- 2-1→w42-primary-rosalind-discovery-20261011; 2-5→w42-lead-qwen-turbo-20261011 (r2 REVISED → Qwen-Image-2.1-Turbo dual-trigger); 2-7→w42-dailyx-sakana-mlr-20261011; 2-8→w42-dailyx-harness-paper-20261011; 2-9→w42-dailyx-amazon-worldmodel-20261011; 2-11→w42-carry-ms-decision1-20261011 (CARRY_OVER, unchanged).
- 3-1→w42-primary-muse-wonder-20261012 (r2 REVISED); 3-2→w42-primary-maia300-20261012 (r2 REVISED); 3-3→w42-primary-glm-legal-20261012; 3-5→w42-primary-minicpm-v47-20261012; 3-6→w42-primary-lechonk-20261012; 3-7→w42-primary-nvidia-ocp-20261012.
- 4-1→w42-primary-gemini4-argon-20261013 (r2 REVISED); 4-2→w42-primary-openai-security-20261013; 4-3→w42-primary-scion-20261013; 4-5→w42-primary-lfm25-20261013; 4-6→w42-lead-fish-drama3-20261013; 4-9→w42-primary-distillation-20261012.
- 5-3→w42-primary-openai-eu-agents-20261014; 5-4→w42-primary-nvidia-uk-20261014.
- 6-1→w42-primary-nemotron35-20261015 (r2 REVISED); 6-2→w42-primary-spark-open-20261015 (r2 REVISED); 6-3→w42-primary-metr-20261015; 6-4→w42-primary-simons-math-20261015; 6-5→w42-primary-rosalind-plan-20261015; 6-6→w42-primary-flux3-klein-20261015; 6-7→w42-dailyx-grok-scale-20261015 (r2 ADDED — corrects r1 crosswalk promise).
- 7-2→w42-primary-glimpse-20261016 (r2 REVISED); 7-3→w42-primary-ecdsa-20261016; 7-4→w42-primary-claude-code-perf-20261016; 7-5→w42-primary-codex-gpt6-20261016; 7-7→w42-primary-beam-20261016 (r2 REVISED); 7-9→w42-primary-decider-v12-20261016; 7-11→w42-primary-aspire-20261016.

## B4 omission reasons (grounded, re-checkable)
- 1-5 NVIDIA×Reflection rumor: UNVER single-post FT-cite, no official; superseded by real Beam availability (7-7). OMIT.
- 1-7 subagent tips / 1-10 Cannae demo / 3-10 agent guides / 7-12 Desktop anecdote: community how-to/anecdote, not versioned events. OMIT.
- 1-11 Gemini routing observation: unofficial single observation, no docs. OMIT (reopen only on official routing note).
- 2-4 RSIArena: UNVER single post, no official results. OMIT.
- 2-6 WebMCP/Gateway: standards discussion + tool intro, no versioned spec/release. OMIT.
- 2-10 physical-AI digest / 6-8 Ling/Matrix digest: multi-claim bundles, each claim unfetched. OMIT as bundle (BD CEO, funding, Odyssey-3 each need official).
- 2-12 Falcon ASR: one-liner inside digest post. OMIT.
- 3-9 Coinbase Qwen story: quote of older event, trend color. OMIT (CONTEXT only).
- 5-5 Apple China: Bloomberg-cited press, no Apple official. OMIT.
- 5-6 Claude Code Desktop: affiliated-claim, no changelog. OMIT (fold into 7-4 only with changelog).
- 5-8 EU enforcement: UNVER enforcement claim, no EU official. OMIT (never allege enforcement without authority).
- 7-10 China export control: community posts, no consultation doc. OMIT.

## Non-Daily r2 additions (9, independent of the 73 — Sol §2 + lanes)
- w42-primary-deep-review-20261014, w42-primary-hydrafusion-20261014, w42-primary-agentic-autofix-20261015, w42-primary-ai-scan-20261015, w42-primary-wetlab-agents-20261016, w42-primary-granite-switch41-20261014, w42-primary-earth-ai-20261014 (Sol 7: 6 mandatory + Earth AI INCLUDED with scope reason), w42-support-argon-copilot-20261013, w42-primary-aws-bedrock-20261013.

## r1→r2 diff (39 carried; 0 removed; 8 revised; 10 added; total 49)
- UNCHANGED (31): all other r1 rows byte-identical (verified by diff of canonical fields).
- REVISED (8): wonder, spark-open, maia300, nemotron35, glimpse, beam (SEARCH→BODY upgrades), qwen-turbo (dual-trigger refinement), agenthorizon (IN-paper + author match).
- ADDED (10): as above. REMOVED: none.
- r1 crosswalk correction: 6-7 grok-scale now has its promised record (was B1-listed but absent in r1 proposal).
