# 2026-W32 Raw Provenance Baseline

Status: **ACTIVE_BASELINE**

This record was added after the `2026-W32 v0.2` PDF freeze as operational provenance metadata. It does **not** modify the frozen article text, bibliography, TeX layout, or PDF-producing source commit recorded in `freeze-v0.2.md`.

## Baseline generation

- GitHub Actions workflow: `Weekly pipeline spine`
- Run: `31353421027`
- Source commit used by the run: `4a89f8081c10f29894716dd189e0adc925d24441`
- Artifact ID: `9049756818`
- Artifact name: `weekly-raw-provenance-2026-W32`
- Artifact ZIP digest: `sha256:16f95ff54384a102727052ddc54bd10baa25437a5ce4e7c1301fd59997ad88b4`
- Baseline index path: `sources/2026-W32/raw-index.json`

The Actions report returned `passed: true`, with no previously indexed file modified or removed. This was the initial baseline, so three existing Raw files were added.

## Indexed Raw files

| Path | Bytes | SHA-256 |
|---|---:|---|
| `sources/2026-W32/grok/raw/x-trend-sensor-2026-08-09-v0.4-rerun.md` | 26851 | `5e93de8362a1929beae3c34ed96e284e44fe0fb9197b22d687c9673847f54e22` |
| `sources/2026-W32/grok/raw/x-trend-sensor-2026-08-09.md` | 15729 | `5ea610f06955958c0f3fd4d8a644ceeee562279e7af5c36b4114a937d28b5294` |
| `sources/2026-W32/grok/reactions/raw/x-community-reaction-2026-08-09-v0.1.md` | 31249 | `005ea9f0bcf93ecb1c5ca866c3b6129ec657be2effa9f86b6e470b1191b5594a` |

## Enforcement

After the baseline was committed, `Weekly pipeline spine` was extended with a `raw-integrity` push/PR job.

Any issue with a committed `raw-index.json` is now checked automatically. A modified, removed, or newly-unindexed Raw file blocks CI.

Corrections to Raw collector observations belong in downstream normalized/evidence artifacts; indexed Raw bytes are immutable provenance.
