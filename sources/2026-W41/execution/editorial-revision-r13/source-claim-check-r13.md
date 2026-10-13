# W41 r13 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-13 JST
Method: official `draft-check` CLI 6/6 PASS + `synthesis-check` PASS + programmatic
audits + excerpt spot-check.

## Programmatic audits (executed, all PASS)

- All `evidence_refs` resolve to real Card IDs with matching subject binding.
- must-cover 27 exact-once, no blanket; boundaries 42 exact-once.
- Attribution modes cover all referenced classes.
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`).
- No invented source IDs/experiments; no disposition changes (20/13/2/1 intact);
  Grok+HOLDs+INSPECTs absent from prose.
- New specifics anchored: EGemma set → `36ef2bcb…` claim-1 + excerpt;
  MoE table → Kolibri/Beam/Mistral claim-1s; 49B wording → ml4 claim-2 scope
  (downgraded, no direct attribution); t2 wording → textgrain claim-1 scope;
  billing wording → haiku claim-1 scope (no complementation); quality t3/p13 →
  textgrain claim-1 scope (Astra table anchor).

## Excerpt spot-check

- EGemma p5 vs `embeddinggemma-blog-r4.source-excerpt.md`: 5 modalities ✓,
  740M ✓, 270/170/300M ✓, MRL→128/256/512 ✓, 8K ✓, 5.5min/29/58 ✓, Apache-2.0 ✓,
  HF+Kaggle ✓. Application example marked as practice, not vendor proof ✓.
- MoE p13 vs Cards: 78.1B/3.46B, 501B/23B, 1.05T/52B ✓; memory/compute split in prose ✓.
- Mistral p8: 52B primary, 49B secondary-unfetched, per-1M pricing kept ✓.
- t2 vs textgrain excerpt: 92/66/17 triple unchanged ✓, bounded note ✓.
- Haiku p5/t1: cache-read split only, unit basis unknown, no estimation ✓.
- Quality t3 vs official original (read-only re-verification 2026-10-13):
  headers Unwatermarked/Watermarked (Astra, max) ✓, 8 rows ✓, values match excerpt ✓.
  Fetch NOT adopted as Evidence; Cards/manifest/checkpoints/State untouched.

## Guard checks

- Legacy spans: 0 in reader fields/preview/synthesis-result; 1 lawful P4 machine trace.
- Old over-assertions (テキスト除外, 今日落とせる, GrokのX告知は, 試算に使える, 値札付き):
  0. Relative dates (non-W41-clear): 0. Priority C patterns: 0.

(End of file)
