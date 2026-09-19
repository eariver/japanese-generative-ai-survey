# W38 execution wrapper — stale-local synchronization then resume Architecture pipeline

Status: `EXECUTION_AUTHORITY / LOCAL_SYNC_EXCEPTION / FAST_FORWARD_ONLY / THEN_RESUME_EXISTING_W38_REQUEST`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W38-v2-work`

## 1. Purpose

A prior Muse invocation stopped safely because its local clone was stale:

- local W38 branch: `e2a897dc50e13278d11a62f463db6ed5a484f4f4`
- remote W38 branch at that time: `de9a52a1ef2c83d11f2aacbc846f4e7ed8abb01e`
- local `main`: stale/diverged
- remote `main`: correct reviewed authority

Independent GitHub verification confirms that the stale local W38 commit is an ancestor of the current remote W38 branch and the remote branch is strictly ahead with no divergent commits.

This wrapper authorizes one bounded **local synchronization phase** before the normal execution guard.

It does not authorize any remote write during synchronization.

After synchronization, restart the existing W38 execution request from its beginning.

## 2. Synchronization exception

The following local operations are explicitly authorized before the ordinary no-write guard:

1. read-only working-tree/status inspection;
2. `git ls-remote origin`;
3. `git fetch` limited to the three required remote refs;
4. local remote-tracking-ref updates caused by that fetch;
5. fast-forward-only advancement of the already checked-out W38 local branch to the fetched W38 remote-tracking ref.

These operations are a synchronization preflight, not production-stage execution.

This exception does **not** authorize:

- any GitHub/remote write;
- force push;
- reset;
- rebase;
- checkout/reset of local `main`;
- merge commit;
- squash;
- history rewrite;
- branch creation;
- content editing before synchronization succeeds.

## 3. Remote authority before sync

Before fetching, use `git ls-remote origin` and require:

- `refs/heads/weekly/2026-W38-v2-work` == the Exact Starting SHA supplied by the invocation;
- `refs/heads/main` == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- `refs/heads/production/survey-core-v2` == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`.

If any remote ref differs, STOP with zero writes other than no-op local reads.

Do not use local `refs/heads/main` as reviewed-main authority.

## 4. Working-tree safety guard

Before fetch/fast-forward:

- current branch must be `weekly/2026-W38-v2-work`;
- `git status --porcelain` must be empty;
- there must be no uncommitted or untracked work that would be overwritten.

If the working tree is not clean, STOP. Do not stash, clean, reset, or delete anything.

## 5. Bounded fetch

Fetch only the required refs, without tags:

```bash
git fetch --no-tags origin \
  refs/heads/weekly/2026-W38-v2-work:refs/remotes/origin/weekly/2026-W38-v2-work \
  refs/heads/main:refs/remotes/origin/main \
  refs/heads/production/survey-core-v2:refs/remotes/origin/production/survey-core-v2
```

After fetch, verify:

- `refs/remotes/origin/weekly/2026-W38-v2-work` == Exact Starting SHA;
- its tree == Exact Starting Tree;
- its parent == Expected Starting Parent supplied by the invocation;
- `refs/remotes/origin/main` == reviewed main SHA;
- `refs/remotes/origin/main^{tree}` == reviewed main tree;
- `refs/remotes/origin/production/survey-core-v2` == pinned Production Line SHA;
- its tree == pinned Production Line tree.

If any check fails, STOP. Do not fast-forward the local branch.

## 6. Fast-forward-only local W38 synchronization

Verify that the current local W38 HEAD is an ancestor of fetched remote W38:

```bash
git merge-base --is-ancestor HEAD refs/remotes/origin/weekly/2026-W38-v2-work
```

The command must succeed.

Then, while staying on the existing W38 branch:

```bash
git merge --ff-only refs/remotes/origin/weekly/2026-W38-v2-work
```

This must produce only a fast-forward. No merge commit is allowed.

Do not touch local `main`.

After the fast-forward verify:

- local `HEAD` == Exact Starting SHA;
- `HEAD^{tree}` == Exact Starting Tree;
- `HEAD^` == Expected Starting Parent;
- working tree clean.

At this point local synchronization is complete.

## 7. Resume authority

After successful synchronization, execute the existing request from its beginning:

`sources/2026-W38/execution/requests/sol-w38-resume-from-grok-r2-through-architecture-review-20260919.md`

Its production semantics remain unchanged.

Normal endpoint remains:

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review pending`

The no-write guard in that request applies normally **after this explicitly authorized synchronization phase**.

For main/prod verification in the resumed execution, use the fetched remote-tracking refs / remote authority, not stale local branch refs.

## 8. Forbidden interpretation

Do not stop merely because local `main` differs from `origin/main`.

Local `main` is not the reviewed authority for this execution and must not be checked out, merged, reset, or synchronized.

Do not stop merely because the initial local W38 HEAD is stale when:

- remote refs match the invocation,
- the working tree is clean,
- and the local W38 HEAD is an ancestor of the fetched exact remote W38 HEAD.

That is precisely the bounded condition this wrapper is designed to repair.

## 9. Report

Include in the final execution report:

- initial stale local W38 HEAD;
- pre-fetch `ls-remote` values;
- fetched remote-tracking SHAs/trees;
- ancestor check result;
- fast-forward old -> new;
- confirmation no merge commit/reset/rebase/force was used;
- confirmation local `main` was not modified;
- then all reporting required by the resumed W38 execution request.
