# W43 Evidence authority r1 — what was read, how deep, what remains open (2026-10-24)

No broad re-research beyond the contracted gap-fill (2 paper PDFs + already-consumed r2/r4 bodies). No invented bytes; all raw hashes verified pre-commit.

## New primary reads in r1 (beyond r2/r4 consumption notes)
- arXiv 2610.24264v2 AM-Bench (38pp PDF archived 2,377,923B): abs + intro + taxonomy/method/results sections read. Unified taxonomy (perceived threat / perceived opportunity / reasoning); 5 threat categories (instrumental convergence), 7 opportunity (ESRR taxonomy), novel 4-question binary reasoning framework; 35 scenarios / 7 industries (fraud-triangle grounding); 10 frontier models, 62-point misalignment spread (Gemini Flash / 3.1 Pro highest, Claude Sonnet 4.6 near-zero); harmful action without explicit situational awareness; repo github.com/AI4Collaboration/Agentic-Misalignment-Bench. Full 38pp + tables + code unexecuted.
- arXiv 2610.16067v2 oracle-eval (29pp PDF archived 261,750B): abs + intro read. 5 state-integrity invariants + 3 known-answer controls; 7 defect classes, 54/57 separable variant-target combos; repaired oracle zero false positives; worked example (reward resets DB for ground-truth hash, never restores: recorded 4194/4320 labels, replay 2883, 94.3% → 65.5%; non-uniform 24–34 point correction, changes strongest agent); 3240-episode ablation; non-transfer + named contract; offline replication package (not run).

## Reused consumed authority (r2/r4 claim-level + rendered bodies, NOT re-fetched)
- OpenAI securing/bio/lowresource pages, Duet announcement, DeepSeek docs, DeepInfer README, Nemotron research page, Voxtral announcement+docs, Eleven blog, FLUX PR/model page/X, TanStack blog, GitHub changelogs, 1Password blog+press, MOSS README + trainer README, MemT abs+README, Ming README, Kimi tech blog + X HTML, Nemotron/Ollama/Unsloth/Vercel locators, ARC page, Grok Raw.

## Explicitly NOT consumed (honest gaps → PARTIAL / NEEDS_MORE / LIMITATION)
- Original HTML bytes for rendered-markdown reads (except Kimi X HTML, Flint announce HTML, HF API JSON bodies archived).
- Independent reproductions: zero (all vendor/AA numbers unreproduced).
- Weight/card/license-file bytes for most families (HF pages read as metadata, files unhashed except supplement PDFs).
- Full paper bodies beyond abs+intro (AM-Bench 38pp, oracle 29pp); v1↔v2 deltas unchecked.
- MOSS report PDF; Ming tech report (roadmap); Nemotron tech report PDF; Voxtral/Eleven eval backends; TanStack repo tag; 1Password per-integration live status; GitHub model/deprecation lists beyond changelog titles.
- X post HTML for all X locators except Kimi status (existence/authorship unvalidated).

## Verification strength summary
- 32 cards: PARTIAL 28 / NEEDS_MORE 4. VERIFIED findings only where the primary directly establishes the fact (announce dates read on pages, repo createdAt via API, Kimi X timestamp in archived HTML, benchmark tables read, changelog schemas read, Grok raw bytes/SHA).
- 4 INSPECT rows (auto-mode, Decisions API, OpenAI Cloud, Patch the Planet) held NEEDS_MORE/HOLD: locator/RSS only, no body.
- Grok ledger: PARTIAL + NON_MATERIAL audit binder; raw bytes/SHA + 2 pinned IDs VERIFIED; repro N/A by sensor nature.
