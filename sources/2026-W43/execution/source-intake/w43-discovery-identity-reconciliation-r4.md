# W43 r3→r4 identity reconciliation (2026-10-24T13:30:22Z re-verified)

r1/r2/r3 proposals immutable. r4 (`discovery-v2-proposal-r4.jsonl`, 51 rows, 51/51 schema PASS, Core graph PASS, 46 families) = 49 r3 rows carried + 2 new. r3 `observed_at` values preserved on carried rows (no backfill, no rewrite).

| r3 ID / new | r4 disposition | Active r4 ID | Rationale |
|---|---|---|---|
| 49 r3 IDs (incl. Kimi merged, Nemotron amended, v1-OUT/v2-IN, 12 carry rechecks, 4 MOSS, 2 DeepInfer, nemotron, arc, orlicense rows) | RETAINED byte-identical (incl. r3 `observed_at`) | same IDs | No contradiction found in r3 active set; r4 adds without rewriting. |
| *(new)* Flint announce/weights Oct 21 | ADDED | `w43-r4-flint-20261021` | New in-window first-party event missed r1–r3; binds Flint primaries + exact Grok Raw (one family, no duplicate Selection identity). |
| *(new)* Grok sensor ledger | ADDED | `w43-r4-grok-x-ledger-20261024` | PARTIAL ledger binding exact Grok Raw; manifest `discovery_ids` = [Flint, ledger]. |

Active counts: r3 49 rows / 44 families → **r4 51 rows / 46 families** (+flint, +grok-x-ledger families). No rows excluded or merged in r4 (r3 dedup stands). Multi-row families unchanged (moss-image 4, deepinfer 2, ambench 2) + 2 new singletons.

`published_at` integrity: Flint `2026-10-21` (index + HF createdAt); ledger `null` (observation, not event — permitted). All other rows unchanged from r3.
