# §11 root-cause record — cross-package validation gap (edition-local, Core untouched)

Date: 2026-10-07. Run: `execution/r8-authority-binding-repair-20261007`.

## Observed failure

The repository already contained intended cross-package authority
(`execution/obligation-realization-r5-20261005/cross-package-authority-map.json`:
D114→P07A, D114→P07B, D115→P07B, D115→P11, D111→P10, D112→P10), yet the
fresh-121-r7-rev1 FINAL P07B consumed neither D114 nor D115 in any block, and no
P05 block consumed D110.

## Actual cause (verified on committed rev1 bytes)

Two divergent map artifacts plus a spec gap, in combination:

1. The r5 intent map was never merged into the generation-time overlay. The r6/r7
   generation overlay (`cross-package-synthesis-authority-r6/r7.json`) carried only
   P06/P10/P11/P15 (+P07A/D114) consumers — no P07B consumer, no P05 consumer.
2. The Draft generator (`_xrefs`) resolves cross-package refs ONLY through the
   generation overlay's per-consumer allowlist. A discovery ID absent from both
   the canonical package inputs and the overlay allowlist cannot bind.
3. The r7 fresh-input spec assigned no D114/D115 discovery_ids to any P07B block
   (B14 used D041/D044/D047/D048/D050/D056 only) and no D110 to any P05 block.
4. The r7 audit checked overlay-entry existence and P07A result refs — i.e.,
   mapping existence and one consumer — never `does any FINAL P07B/P05 block ref
   the mapped task`. must_cover_coverage additionally checks block-ID presence,
   not required Evidence/entity use. So the omission passed silently.

Not among the causes: stale overlay audit (the audited overlay was current),
exact-placement confusion at result level (refs were correctly absent, not
hallucinated), or missing Architecture authority (P07B must-cover already
required D114/D115; the defect was purely downstream materialization).

## Repair (this run, edition-local only)

- Single effective map `cross-package-map-r8.json` (34 entries) that is BOTH the
  intent record AND the generation-time overlay: 31 carried (SHAs re-verified;
  D114→P07A, D115→P11, D111/D112→P10 retained) + D114→P07B + D115→P07B +
  D110→P05 (new SUPPORTING evaluation authority; no PRIMARY relocation).
- Spec assigns discovery_ids where prose makes the claims: new P07B-D114/P07B-D115
  synthesis blocks, P05-B10 += D110, P07B-B14 += D049 (canonical P07B input),
  p08-b8 += D060 (canonical P08 input), p11-b10 keeps D115.
- Generator consumes the map (`OVERLAY_CONSUMERS` += P07B, P05); edition-local
  overlay validator checks the union index on FINAL results.
- Semantic validator (`audit_r8.py`) checks FINAL effective consumption per
  consumer block (not intent): P07B-D114, P07B-D115, P05-D110, P11-D115,
  P07A-D114, B14-D049 — each FAILS if absent.
- Negative fixtures F1–F6 (/tmp-style in-memory copies; canonical tree untouched):
  omitted-D114, omitted-D115, OCRBench-without-D110, stored-timeline conflation,
  labels wording, app mistranslation — each MUST FAIL and does.
