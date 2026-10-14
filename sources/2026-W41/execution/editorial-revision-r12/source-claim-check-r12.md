# W41 r12 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-13 JST
Method: official `draft-check` CLI 6/6 PASS + programmatic audits + excerpt spot-check.

## Programmatic audits (executed, all PASS)

- All `evidence_refs` resolve to real Card IDs with matching subject binding (Core validator).
- must-cover 27 exact-once, no blanket; boundaries 42 exact-once.
- Attribution modes cover all referenced classes.
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`).
- No invented source IDs/experiments; no disposition changes (20/13/2/1 intact);
  Grok+HOLDs+INSPECTs absent from prose.
- New specifics anchored: EGemma multimodal set → claim-1 of `36ef2bcb…`
  (excerpt lines 2–6); MoE table → Kolibri/Beam/Mistral claim-1s;
  49B wording → ml4 claim-2 scope (SOCIAL_OBSERVATION, downgraded to secondary record);
  t2 wording → textgrain claim-1 scope (edit-weakening numbers); billing wording →
  haiku claim-1 scope (cache-read figures only).

## Excerpt spot-check (saved supplement bytes vs prose)

- EGemma p5 vs `embeddinggemma-blog-r4.source-excerpt.md`: 5 modalities ✓, 740M ✓,
  270M/170M/300M ✓, MRL 768→128/256/512 ✓, 8K ✓, 5.5min/29/58 ✓, Apache-2.0 ✓,
  HF+Kaggle ✓. Evaluations beyond blog: marked unfetched ✓.
- MoE p13 vs Cards: 78.1B/3.46B, 501B/23B, 1.05T/52B ✓ (no other pair asserted).
- Mistral p8 vs docs/X-record: 52B primary, 49B secondary-unfetched ✓.
- t2 vs textgrain excerpt: 92/66/17 triple unchanged ✓, condition note bounded ✓.
- Haiku p5/t1 vs claim-1: cache-read $0.01/$0.05 as the only confirmed split ✓,
  input/output/unit basis marked unknown ✓, no estimation claim ✓.

## Guard checks

- Legacy spans: 0 in reader fields/preview/synthesis-result; 1 lawful P4 machine trace.
- Old over-assertions (テキスト除外, 今日落とせる, GrokのX告知は, 試算に使える): 0.
- Priority C patterns: 0. Relative dates (non-W41-clear): 0.

(End of file)
