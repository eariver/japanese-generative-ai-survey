# W43 r6 TanStack publisher timestamp crosswalk (edition-local, noncanonical)

Status: `EDITION_LOCAL_SOURCE_NOTE / NO_CANONICAL_MUTATION`
Date: 2026-10-25. Starting HEAD `b7445700dd852024ac27f1feaed58a61de9a9a42` / Tree `e5cd33332af5aa52ba6358d3296510ee2ac44d6b`.
Purpose: R5-N02 — resolve the inverted `registry 15:18:14Z/release 15:21:49Z` Architecture label against publisher metadata. No accepted Evidence/Views/Selection bytes were mutated; the established Selection rationale (npm 15:21:49Z + GH release 15:18:14Z) is independently confirmed below and left byte-identical.

## 1. GitHub release API (independently fetched 2026-10-25 ~11:08Z UTC)

- Request: `gh api repos/TanStack/ai/releases/tags/@tanstack%2Fai%401.0.0`
- Response keys/values: `tag` = `@tanstack/ai@1.0.0`; `name` = `@tanstack/ai@1.0.0`; `created_at` = `2026-10-22T15:17:40Z`; **`published_at` = `2026-10-22T15:18:14Z`**.
- Conclusion: the **GitHub Release publish instant is 15:18:14Z**. The r5 Architecture label attaching 15:21:49Z to "release" was inverted.

## 2. npm registry metadata (independently fetched 2026-10-25 ~11:08Z UTC)

- Request: `GET https://registry.npmjs.org/@tanstack%2Fai` (Accept: application/json).
- Response keys/values: `time["1.0.0"]` = **`2026-10-22T15:21:49.491Z`** (second precision 15:21:49Z); `time.modified` = `2026-10-22T15:21:49.960Z`.
- Conclusion: the **npm registry publish instant is 15:21:49Z**. The r5 Architecture label attaching 15:18:14Z to "registry" was inverted. The established Selection rationale (`npm 1.0.0 15:21:49Z + GH release 15:18:14Z`) is independently confirmed and therefore NOT rewritten.

## 3. r6 Architecture binding (fixed, source-attributed)

- P8 §8.2 now reads `GitHub release 15:18:14Z(GitHub API published_at、確認2026-10-25)/npm registry 15:21:49Z(registry time["1.0.0"]、確認2026-10-25)`.
- The TanStack Oct23 blog remains day-only (`UNRESOLVED分離[製品時刻に読まない]`) and is never used as the product clock.
- No live API call, schema check, or general-availability proof beyond the two publish timestamps is claimed.
