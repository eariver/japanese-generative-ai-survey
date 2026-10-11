# W41 completeness report r1 (proposal for Sol review)

Status: `PROPOSED_NOT_ACCEPTED / SOL_REVIEW_REQUIRED`
Proposal: `discovery/discovery-v2-proposal-r1.jsonl` — 20 records, schema-validated, NOT accepted. State remains `ISSUE_INITIALIZED`.

## Coverage by lane

- Frontier/proprietary models: GPT-6+Intelligent UI, Haiku 5.5, Ultrafast, Decisions beta, Gemini agent — STRONG (first-party).
- Open weights: Mistral Large 4 (weights pending), Beam (weights pending), Clef-omni (time unresolved) — BOUNDED (availability caveats explicit).
- Agents/coding/computer use: Ironclad research (provisional), math release (corpus+repo) — MODERATE.
- Safety/cyber/governance: Cyber Mission, Usage Policy, unintended-actions (time unresolved) — MODERATE.
- Serving/local/quantization: llama.cpp rolling builds only, v0.6.0 unobserved — THIN, dated negative.
- Image/video/audio generation: QUIET with dated note.
- Japanese domestic: pre-window RSI context only; no in-window release — QUIET with dated note.
- Training/evaluation: vendor RL-scale context only — THIN.
- X/Grok: AWAITING_GROK — LANE NOT PASSED (task issued, one independent pre-window X datapoint).

## Materiality pre-triage (proposal level, NOT Selection)

Strong candidates: Haiku 5.5, Mistral Large 4, GPT-6/Intelligent UI, Beam, Ultrafast, math corpus, Cyber Mission. Context-leaning: Usage Policy, unintended-actions (if time-resolved), Clef-omni (if time-resolved), Decisions beta (if first-party pinned). Weak/excluded at proposal: pre-window items, quiet-lane fillers (none created).

## Top uncertainties / blockers for Sol

1. Oct 9 day-only events (Clef-omni, unintended-actions) need clock-time proof or stay HOLD/CONTEXT.
2. Decisions beta needs first-party doc pin; Ironclad needs page-body re-read.
3. X lane incomplete (AWAITING_GROK) — completeness cannot PASS until reconciled or explicitly deferred by Sol.
4. Mistral 49B figure superseded by current 52B on both blog+docs (reconciliation recorded; watch for version drift).
5. `production/survey-core-v2` HEAD check in the r1 contract refers to an operator-environment path absent from this checkout; substituted with the verifiable equivalent (Core scripts/config/schemas/workflows byte-identical to reviewed main `83f581eb`).
