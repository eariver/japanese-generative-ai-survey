# W41 r14 source–claim check (programmatic + editorial)

Status: `EDITION_LOCAL / AUDIT_EVIDENCE`
Date: 2026-10-13 JST
Method: official `draft-check` CLI 6/6 PASS + `synthesis-check` PASS + programmatic
audits + excerpt spot-check.

## Programmatic audits (executed, all PASS)

- All `evidence_refs` resolve to real Card IDs with matching subject binding.
- must-cover 27 exact-once, no blanket; boundaries 42 exact-once
  (P5[0] maps p2/p3/t2/p13/t3 with quality substance).
- Attribution modes cover all referenced classes.
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`).
- No invented source IDs/experiments; no disposition changes (20/13/2/1 intact);
  Grok+HOLDs+INSPECTs absent from prose.
- New/changed specifics anchored: t1 scope row → synth claim-1 enumeration;
  quality t3/p13 → textgrain claim-1 (Astra table anchor); AA units → official
  header re-verification (editorial display, not new Evidence).

## Excerpt spot-check (delta scope only; r13-verified carry-overs retained)

- t1 vs synth excerpt: Google-or-partners enumeration ✓, English-global ✓,
  scale pair ✓; no partner-only limitation ✓; no non-support verdict ✓.
- t3 vs official headers: Unwatermarked/Watermarked (Astra, max) ✓, 8 rows/values ✓.
- p13 units: points vs % ✓. p3 tail: no duplication ✓.
- P3 p9/p12/p14 vs clef claim-1 + weight Cards: timestamp metadata, four stages,
  license separation ✓. P4 p3 vs nano claims: card-confirmed / blog-unconfirmed /
  no-existence-verdict ✓.

## Guard checks

- Legacy spans: 0 in reader fields/preview/synthesis-result; 1 lawful P4 machine trace.
- Over-assertions (テキスト除外, 今日落とせる, GrokのX告知は, 試算に使える, 値札付き,
  パートナー由来に限定): 0. Internal metadata (revision/audit/deadline/acquisition
  process): 0. Relative dates (non-W41-clear): 0.

(End of file)
