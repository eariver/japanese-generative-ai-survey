# W43 Discovery identity reconciliation r3 (2026-10-24T12:36:18Z re-verified)

r1 (`discovery-v2-proposal-r1.jsonl`, 36) and r2 (`discovery-v2-proposal-r2.jsonl`, 51) are immutable history. r3 (`discovery-v2-proposal-r3.jsonl`) is the coherent active canonical proposal: **49 rows, 49/49 schema PASS, IDs unique, Core graph PASS, 58 raw_refs all exist, 44 event families** (41 singleton rows + 3 multi-row families).

## Disposition map (51 r2 IDs → r3)

| r2 ID | r3 disposition | Active r3 ID | Rationale |
|---|---|---|---|
| `w43-primary-kimi-20261023` | AMENDED (same stable ID) | `w43-primary-kimi-20261023` | Single canonical event at `2026-10-23T17:15:24Z` (13:15:24 EDT, 19-digit); summary/locator/raws corrected; X HTML + blog bound. |
| `w43-r2-kimi-corrected-20261023` | MERGED (excluded from active) | `w43-primary-kimi-20261023` | Same announcement/API event, not a second candidate; correction absorbed, no double count. |
| `w43-lead-ambench-20261016` | EXCLUDED (superseded) | — (see below) | Contradictory "time unknown" claim; replaced by explicit version rows. |
| `w43-r2-ambench-v2-20261020` | RETAINED (+published_at filled) | `w43-r2-ambench-v2-20261020` | v2 `2026-10-20T15:40:19Z` IN as revision only; delta unchecked. |
| *(new)* | ADDED | `w43-r3-ambench-v1-out-20261016` | v1 `2026-10-16T21:46:19Z` OUT background; replaces unknown row. |
| `w43-lead-orlicense-20261016` | EXCLUDED (superseded) | — | Contradictory "time unknown"; r2 OUT row is authoritative. |
| `w43-r2-out-orlicense-20261016` | RETAINED (+published_at filled) | same | v1 `2026-10-16T18:13:25Z` OUT background. |
| `w43-primary-nemotron-e4b-20261023` | AMENDED (same stable ID) | same | 64K ctx (not 1M); r2 note-05 bound; capture class corrected. |
| `w43-r2-out-moss-base-20261016` | RETAINED (+published_at filled) | same | Repo created `2026-10-16T01:18:13Z` OUT background. |
| `w43-r2-out-arc-20261013` | RETAINED (+published_at filled) | same | Page `2026-10-13` OUT background; Qwen3.8 row ≠ identity proof. |
| `w43-r2-out-deepinfer-repo-20261016` | RETAINED (+published_at filled) | same | Repo created `2026-10-16T07:47:23Z` OUT background. |
| All other 40 r2 IDs | RETAINED (observed_at re-verified to r3 UTC) | same IDs | No identity contradiction; r3 re-verification timestamp applied. |

Active: 51 − 3 excluded + 1 added = **49**. New/excluded/retained counts reconcile exactly.

## Multi-row families (explicit, no double counting)
- `moss-image` (4): code/weights-OUT / trainer-IN / report-announce-IN / api-IN — distinct events, one family.
- `deepinfer` (2): repo-OUT / announce-IN — distinct events, one family.
- `ambench` (2): v1-OUT / v2-revision-IN (delta unchecked) — versions, one family.
- All other active rows are singleton families (41), incl. `kimi-k31-pro` (single merged row), `orlicense`, `nemotron-bolt-e4b`, `arc-argon`.

## published_at integrity
Every active row carries non-contradictory `published_at`: exact UTC where verified (Kimi `17:15:24Z`, AM-Bench v1/v2, OR-License, MOSS repo/report-announce/api, DeepInfer repo, MemT v1, Ming repo, Nemotron E4B research page, all Oct 17–23 primaries), day precision where only day is proven (ARC `2026-10-13`), null only where no event exists (12 W42 carry rechecks + a few locator-only leads). No active "time unknown" family rows (2 residual string hits are errata prose, not claims).

## Dedup assertion: PASS
One Kimi row; version/repo-vs-announce pairs explicit; no two active rows claim the same technical release. Publisher vs independent measurement kept (vendor benches vs AA vs repo/API facts).
