# Weekly Pipeline Operations Guide

Status: operational companion to `docs/weekly-pipeline-design-v0.1.md`.

## 1. GitHub Actions workflow

Use:

```text
Actions -> Weekly pipeline spine -> Run workflow
```

Available commands:

### `plan`

Purpose:

- calculate the latest completed weekly issue label;
- calculate Friday 18:00 `America/New_York` cutoff;
- carry forward the latest prior `collection_anchor_at`;
- emit `plan.json` and `plan.md` as an Actions artifact.

No repository write or LLM call occurs.

### `validate`

Required input:

```text
issue_id
```

Targets:

```text
selection
draft
release-candidate
frozen
```

This performs deterministic repository-structure checks and known static hazards. It does not replace claim review, chronology review, TeX compilation or visual review.

### `raw-index`

Required input:

```text
issue_id
```

Purpose:

- scan every file under a `raw/` path inside `sources/<issue>/`;
- compute SHA-256 and byte size;
- refuse to proceed if an already-indexed Raw file was modified or removed;
- add newly discovered Raw files to the index;
- upload generated `raw-index.json` and a report as an Actions artifact.

The workflow does **not** commit the generated index automatically. The initial or changed index should be reviewed before being written to the repository.

### `raw-check`

Required input:

```text
issue_id
```

Purpose:

- compare committed `raw-index.json` against current Raw files;
- fail on modified, removed or unindexed Raw files.

This is the normal integrity check after a baseline index has been committed.

## 2. Local CLI equivalents

### Plan

```bash
python scripts/weekly_pipeline.py plan
```

### Initialize state

```bash
python scripts/weekly_pipeline.py init --issue-id 2026-W33
```

Initialization refuses to overwrite an existing `pipeline-state.json` unless `--force` is explicitly supplied.

### Validate issue state/artifacts

```bash
python scripts/weekly_pipeline.py validate \
  --issue-id 2026-W32 \
  --target frozen
```

### Create/update Raw provenance index

```bash
python scripts/raw_provenance.py \
  --issue-id 2026-W32 \
  update
```

### Verify Raw provenance

```bash
python scripts/raw_provenance.py \
  --issue-id 2026-W32 \
  check
```

## 3. Initial W32 bootstrap procedure

The frozen W32 issue already contains `pipeline-state.json` and therefore supplies a conservative collection anchor to later weekly plans.

To establish Raw immutability for the existing W32 Grok files:

1. Run `Weekly pipeline spine` manually.
2. Choose `command = raw-index`.
3. Set `issue_id = 2026-W32`.
4. The `target` input is ignored by this command; its default may remain unchanged.
5. Download the `weekly-raw-provenance-2026-W32` artifact.
6. Review `raw-provenance-report.json` and `raw-index.json`.
7. Commit the reviewed `raw-index.json` to `sources/2026-W32/raw-index.json`.
8. Re-run with `command = raw-check` to confirm the committed baseline.

After this bootstrap, any accidental edit to an indexed Raw file becomes a deterministic CI failure rather than an editorial convention that must be remembered manually.

## 4. Important boundaries

- `raw-index` verifies bytes; it does not judge whether the collector output is correct.
- Collector technical claims still require primary-source verification.
- New Raw files are allowed, but they must be intentionally added to the index.
- Existing indexed Raw files are immutable; corrections belong in normalized/evidence layers.
- A successful deterministic workflow never authorizes unattended publication.
