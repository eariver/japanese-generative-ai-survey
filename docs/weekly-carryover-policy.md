# Weekly carry-over policy

Effective: 2026-08-15.

## Purpose

Weekly issue boundaries must not cause unresolved, weakly verified, or post-cutoff items to disappear merely because the next Source Intake starts from a fresh collection window.

The publication already separates the editorial cutoff from the collection window and permits Late Breaking treatment. This policy adds an explicit cross-issue carry-over ledger so that the follow-up obligation is auditable and mechanically checked.

## Carry-over roles

The following prior Candidate Selection roles require an entry in the next Weekly issue's carry-over ledger:

- `HOLD_OUT` — Evidence or chronology remained unresolved and the item was deliberately excluded from the prior architecture.
- `WATCHLIST` — a retained weak/secondary signal that may become material with new primary evidence or technical momentum.
- `LATE_BREAKING` — a post-cutoff item that received only abbreviated treatment and therefore requires a next-issue recheck.

Items explicitly rejected for a disproved identity/chronology do not automatically carry over. They may be added only when a new source or correction reason exists.

## Ledger location and stages

Each Weekly issue after W32 stores:

```text
sources/<issue>/carryover/carryover-ledger-v0.1.json
```

The ledger has two validation stages.

### Before Screening

Every expected item from the previous issue must exist in the ledger. Entries may still have `PENDING_RECHECK` status. The purpose of this gate is coverage: the item cannot vanish before Screening simply because the normal collectors did not rediscover it.

### Before Candidate Selection

The same ledger is checked again. No entry may remain `PENDING_RECHECK`. Every prior obligation must have a documented resolution such as promotion into the current Evidence pool, supporting-evidence mapping, continued unresolved status, previous-issue backfill/erratum, or an explicit no-current-action conclusion.

## Allowed ledger statuses

- `PENDING_RECHECK`
- `RECHECKED_UNRESOLVED`
- `RESOLVED_PROMOTED_CURRENT`
- `RESOLVED_SUPPORT_CURRENT`
- `BACKFILL_PREVIOUS_ISSUE`
- `NO_CURRENT_ACTION`

These statuses describe the carry-over obligation only. They do not replace Screening decisions, Evidence Card status, Candidate Selection roles, or publication chronology.

## Source of expected carry-over entries

For structured Weekly issues, the validator derives the expected set from the previous issue's approved `selection/candidate-selection-v0.1.json` and the carry-over roles above.

Legacy `2026-W32` predates the structured selection contract. `2026-W33` therefore uses a one-time curated seed file that records the W32 carry-over set and is SHA-bound by the W33 ledger.

## Correction boundary

A carry-over recheck may reveal that primary evidence already existed during the previous issue and was simply missed. That is not a current-week release. It must be recorded as previous-issue backfill/erratum and must not be silently redated into the current issue.

Likewise, a current-week integration may be valid even when the underlying model's original release remains unverified. Integration chronology and model chronology must remain separate.

## Human review

Normal carry-over bookkeeping is an internal deterministic/editorial checkpoint. A separate Human Gate is required only when the resulting correction changes already published bytes or otherwise triggers the exceptional post-Release correction policy. An explicit human approval to record an erratum/backfill is sufficient authority to add a non-destructive correction record while preserving the original frozen Release.
