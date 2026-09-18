# Grok X Source Intake Follow-up — W37 r2 provenance completion

Status: `W37_EDITION_LOCAL / GROK_FOLLOWUP_R2 / PROVENANCE_COMPLETION_WITH_CONDITIONAL_EXPANSION`

Issue: `2026-W37`

Original run:

`weekly-x-2026-W37`

Original task:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-task.md`

Original result:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-x-result.md`

Required follow-up result filename:

`grok-x-result-r2.md`

Do **not** overwrite the original result.

## 1. Purpose

The W37 r1 result showed good topical breadth, open-world discovery, and a useful 10-candidate pool, but its final artifact did not preserve enough direct X post URLs to make the claimed breadth auditable.

The r1 result claimed approximately:

- ordinary-window unique X post URLs: `~28`
- total examined/retained X post URLs: `~45`
- unique independent accounts: `~22`

However, the final Markdown preserved only seven direct `x.com/.../status/...` URLs.

This follow-up therefore has two goals:

1. **Materialize the X provenance already observed in r1 into the result artifact.**
2. **Only if the materialized provenance falls below the W37 diagnostic floors, perform the mandatory expansion pass.**

This is not permission to invent, reconstruct, infer, or guess URLs that were not actually observed.

## 2. Preserve r1 as history

Treat `grok-x-result.md` as immutable r1 history.

Create a new result:

`grok-x-result-r2.md`

The r2 result may restate or correct r1 candidate assessments, but must clearly distinguish:

- `R1_CLAIM_RECONFIRMED`
- `R1_CLAIM_DOWNGRADED`
- `NEW_R2_OBSERVATION`

Do not silently alter a previous count or source-breadth claim.

## 3. Mandatory provenance materialization

For every r1 candidate C1–C10, produce a provenance table containing, at minimum:

- candidate ID
- direct X post URL
- account handle
- account/source role: `OFFICIAL`, `INDEPENDENT`, or `COMMUNITY`
- post date/time when available
- ordinary-window / late-breaking / pre-window-carry-in classification
- why the post supports the candidate
- discovery origin
- whether the URL was already observed in r1 or newly found in r2

Use **direct post/status URLs** whenever available.

Do not use:

- account profile URLs as substitutes for posts;
- X search-result URLs;
- textual references such as “AskClaw AMBER weekly posts” without the actual post URL;
- reconstructed URLs based on account name, date, quoted text, or post ID guesses.

If a claimed r1 source cannot be re-located, write:

`R1_SOURCE_NOT_RELOCATED`

and downgrade any count/classification that depended on it.

## 4. Recalculate candidate-level breadth from enumerated URLs

After all usable direct URLs are listed, recompute for each C1–C10:

- unique direct X URL count
- unique account count
- independent-account count
- official-account count
- source-breadth classification

Use only enumerated URLs in the r2 artifact for these counts.

Allowed classifications:

- `MULTI_ACCOUNT_X`
- `SINGLE_SOURCE_X`
- `OFFICIAL_ONLY_X`
- `UNVERIFIED_X_REFERENCE`

Do not retain `MULTI_ACCOUNT_X` merely because r1 prose claimed multiple accounts. It must be supported by the actual enumerated URLs.

A broad community-momentum claim requires at least two independent/non-affiliated accounts with direct post URLs.

## 5. Candidate-specific repair requirements

### C1 — GPT-6 Astra

r1 claimed:

- unique X URL count: `>10`
- independent-account count: `≥8`
- `MULTI_ACCOUNT_X`

but preserved only OpenAI official URLs.

r2 must either:

- enumerate the independent-account URLs supporting those claims; or
- downgrade the counts/source-breadth/community-momentum wording.

### C2 — DeepSeek-V4.1-Flash

r1 claimed:

- unique X URL count: `≥6`
- independent-account count: `≥4`
- `MULTI_ACCOUNT_X`

but preserved only official DeepSeek thread URLs.

Enumerate the independent evaluation/integration URLs, including the AMBER-related source if actually observed, or downgrade the claim.

### C3 — SWE-2 / Cognition / Fusion CLI

r1 referenced:

- AskClaw AMBER weekly posts
- Fusion CLI cost/performance discussion
- Artificial Analysis references

but preserved no direct X post URL for these claims.

r2 must provide direct URLs or downgrade C3 to the level actually supported.

### C4 — MiniCPM5-2B

r1 classified C4 as `MULTI_ACCOUNT_X` but preserved one direct independent URL.

Enumerate the additional independent URLs or downgrade to `SINGLE_SOURCE_X`.

### C5–C10

For every non-strong candidate, provide direct URLs when they existed in the r1 observation set.

Do not omit provenance merely because the candidate was not selected as strong.

## 6. Run-level provenance audit

Once the URLs are materialized, calculate from the explicit r2 URL list:

- total unique direct X post URLs
- ordinary-window unique direct X post URLs
- late-breaking unique direct X post URLs
- pre-window carry-in URLs
- total unique accounts
- unique independent accounts
- unique official accounts
- candidate pool count
- candidates with zero direct URLs
- `MULTI_ACCOUNT_X` count
- `SINGLE_SOURCE_X` count
- `OFFICIAL_ONLY_X` count
- `UNVERIFIED_X_REFERENCE` count
- candidates discovered via `OPEN_WORLD_X`
- candidates discovered via `ACCOUNT_GRAPH_EXPANSION`
- candidates discovered via `KEYWORD_SNOWBALL`

These counts must be derived from the actual enumerated rows in r2, not from memory or approximate observation notes.

Avoid `~`, `>`, and `≥` for the final provenance audit. Use exact integer counts.

## 7. Conditional mandatory expansion

After provenance materialization and exact recounting, trigger the W37 mandatory expansion pass if **any** of the following is true:

- ordinary-window unique direct X post URLs < **12**
- unique independent accounts < **6**
- full deduplicated candidate pool < **8**
- 4 or more lanes remain `NONE_FOUND`, `NONE_FOUND_CONFIRMED`, or `UNCERTAIN`
- more than half of strong candidates are `SINGLE_SOURCE_X` or `OFFICIAL_ONLY_X`

If the expansion trigger does **not** fire, do not perform broad redundant re-research merely to increase counts.

If it **does** fire, perform one complete expansion pass using:

1. alternate terminology for weak lanes;
2. independent developer/researcher/OSS-maintainer searches;
3. keyword snowballing from unfamiliar entities;
4. one-hop graph expansion from promising posts/accounts;
5. explicit search for failed reproduction, disagreement, constraints, regressions, and low-engagement but technically concrete observations.

Any new source discovered in r2 must be marked `NEW_R2_OBSERVATION`.

After one complete expansion pass, low counts may remain if the week is genuinely quiet or access-limited. Report that honestly. Do not manufacture sources to satisfy the diagnostic floor.

## 8. Open-world provenance completion

Preserve and audit the r1 open-world findings.

For each candidate previously attributed to:

- `OPEN_WORLD_X`
- `ACCOUNT_GRAPH_EXPANSION`
- `KEYWORD_SNOWBALL`

provide the direct X URL(s) that led to or materially supported that discovery.

If the discovery arose from a primary-source page reached from X, still preserve the originating X post URL when available.

If no direct X origin can be retained, mark the open-world origin as unverified rather than silently keeping it.

## 9. Output structure

The r2 result must contain these sections in this order:

1. **r2 scope and relation to r1**
2. **Candidate provenance tables — C1 through C10**
3. **Corrected candidate-level breadth classifications**
4. **Full direct-X URL ledger**
5. **Open-world provenance ledger**
6. **Exact run-health / breadth audit**
7. **Conditional expansion decision**
8. **Expansion observations** — only if triggered
9. **Corrections / downgrades from r1**
10. **Remaining limitations**
11. **Primary-source candidates for downstream verification**

The **Full direct-X URL ledger** must contain one row per unique direct X post URL and at least:

- URL
- account
- role
- timestamp/date if available
- candidate ID(s)
- window classification
- r1/r2 observation provenance

## 10. Evidence boundary remains unchanged

This follow-up is still **Raw Observation**.

Do not use X alone to establish:

- model specifications
- parameter counts
- benchmark truth
- pricing
- license terms
- release availability
- architecture facts
- transaction status
- security/capability facts

Those remain subject to downstream primary-source verification by ChatGPT/Sol.

The purpose of r2 is to make X observation provenance auditable, not to promote X into technical Evidence authority.

## 11. Save location

Save the completed follow-up only as:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-x-result-r2.md`

Do not overwrite:

- `grok-task.md`
- `grok-x-result.md`

If `grok-x-result-r2.md` already exists, save the next revision suffix and report the actual filename.
