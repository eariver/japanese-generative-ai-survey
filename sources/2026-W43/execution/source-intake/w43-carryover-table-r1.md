# W43 carry-over / recheck table r1 (2026-10-24)

Source: `sources/2026-W42/candidate-selection-v2.json` (28 SELECTED / 7 HOLD / 5 INSPECT).
Policy: `docs/weekly-carryover-policy.md`. These 12 are leads, NOT auto-selected W43 stories and NOT an assertion of mandatory Core carry-over records.
Recheck evidence: `collectors/primary/runs/20261024T120000Z-muse-r1/bundle-06-w42-carryover-recheck-20261024.md`.
Discovery binding: `discovery/discovery-v2-proposal-r1.jsonl` records `w43-carry-*` (12, BASE + `weekly:carry-over`, PROPOSED_NOT_ACCEPTED).

| W42 candidate | W42 disposition | W43 recheck | W43 disposition | Reason / gate |
|---|---|---|---|---|
| `b80ab4ccd3469c31` timing proof | HOLD | RECHECKED_UNRESOLVED | NO_NEW_AUTHORITY | No dated issuer clock; Granite comparison still not Decision-1 evidence. |
| `10d76dec5907fe46` X-only order | HOLD | RECHECKED_UNRESOLVED | QUARANTINE | No contract/release/security doc; Meta shopping is separate. |
| `800408dab7fcce56` X-only metrics | HOLD | RECHECKED_UNRESOLVED | QUARANTINE | No verified infra metrics. |
| `1b1aea9beacefbcd` missing harness paper | HOLD | RECHECKED_UNRESOLVED | NO_NEW_AUTHORITY | AM-Bench/OR-License are different papers; must not conflate. |
| `2177831df4f20832` unverified model name | HOLD | RECHECKED_UNRESOLVED | QUARANTINE | No issuer/weights identity; Kimi/Qwen-Image do not verify Qwen3.8-27B. |
| `517550f1eb0dda9d` video method/license | HOLD | RECHECKED_UNRESOLVED | NO_NEW_AUTHORITY | FLUX Max is separate family; LTX method/license still thin. |
| `017c9bbc00134ae8` uncorroborated allegation | HOLD | RECHECKED_UNRESOLVED | QUARANTINE | Patch the Planet is different process; do not repeat as fact. |
| `b2ee0e1dffa42188` Fish Audio | INSPECT | RECHECKED_UNRESOLVED | NO_CURRENT_ACTION | Voxtral/Eleven are separate; Fish usability/license/eval still thin. |
| `7151fcdc6c3ee392` Claude Code perf | INSPECT | SUPPORTING_BACKGROUND | CONTEXT_ONLY | No causal benchmark; GitHub Oct 19-23 keeps lane warm only. |
| `c3439ff42a96e600` Le Chonk | INSPECT | RECHECKED_UNRESOLVED | NO_CURRENT_ACTION | Voxtral 3 is speech, not grounding weights; gap stands. |
| `2cd2da5b249062c9` OCP/SMLIB | INSPECT | RECHECKED_UNRESOLVED | CONTEXT_ONLY | No SMLIB contribution proof; open-standards context at most. |
| `7eb212557bbc5909` EU adoption | INSPECT | RECHECKED_UNRESOLVED | NO_CURRENT_ACTION | No representative sample; Oct 21-22 deployment is not methodology repair. |

Principle: a W42 Release event does not become W43 content via follow-up discussion. Only genuinely new in-window claims/actions anchor fresh W43 identities. Older work (Wonder Oct 12, Spark Open Oct 15, Nemotron Super VL Oct 15, Step 5 weights Oct 15, Qwen-Image Oct 9, Grok Voice Oct 14, Jais 3 / d1-ultra / GPT-Live Oct 15) is BACKGROUND, never relabeled as W43 news.
