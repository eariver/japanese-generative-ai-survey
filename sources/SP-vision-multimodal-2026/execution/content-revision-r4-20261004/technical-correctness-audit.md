# Technical correctness audit — content-revision-r4

Worker-level verification (not a Sol review; fresh independent JSON content review still owed).

## Cross-benchmark contamination (MMMU/MMBench)

- MMMU block (p15-b4) no longer contains any bilingual-scope condition (scan: `英語と中国語` 0,
  `二言語` in p15-b4: 1 residual — `言語範囲の条件はこの記録では言語の広がりの主張に使わず` — a scope
  LIMITATION sentence, not a bilingual-fact claim; kept intentionally).
- MMBench block (p15-b6) retains `英中二言語`/`二言語` scope (correct home, untouched).
- QA item `cross-benchmark-contamination` recorded PASS in worker QA.

## Private/hidden evaluation wording

- No sentence in P15 or synthesis implies private-set agreement proves absence of contamination.
  All 4 residual `証明` hits are explicit negations (`証明ではない` / `証明にはならない`).
  Framing limited to auxiliary mitigation/detection (`補助的な手段`).

## DINO temperature

- `温度` in DINO block (p06-b4): 0 residual. SigLIP block (p06-b6) `温度と初期バイアス` kept
  (different candidate, card-scoped, out of review scope).

## P04 four-node cap

- P04 blocks reference exactly VM-D019/020/021/022 (MiDaS/OpenPose/Visual Genome/DUSt3R);
  no node added. Discovery IDs per block unchanged.

## P09 pixel-unshuffle

- Revised: `空間情報をチャネル方向へ再配置してまとめる手順であり、単純な縮小とは異なる形で
  高解像度情報を保持する` (limited, Evidence-grounded; no information-theoretic absolutes).

## P12 OSWorld numbers

- p12-b2 keeps `約30回/約318回/500手順/20.6%/54.8%` (card-scoped, unchanged); no token
  magnification derived (scan: no `倍` rate sentence; only qualitative `トークン数と費用と
  待ち時間が増え` retained).

## P14 I-JEPA / V-JEPA

- `潜在表現を予測する` (latent/representation prediction) restored in 3 sentences;
  V-JEPA decoder grounding fixed (`獲得された特徴の内容を確かめる調べ`);
  `デコーダ` normalization applied (9件); four-pole headers intact.

## P13 lineage

- Seven lineage nodes intact (SayCan→RT-1→PaLM-E→OpenX→RT-2→OpenVLA→Gemini Robotics);
  no re-expansion (net −558 chars from recap removal only).

## P07B completeness

- Chain node blocks (b1–b12) untouched except terminology; six-group parallel organization kept.

## P11 three contracts

- Offline-breadth / online-streaming / stored-timeline separation sentences kept;
  VM-D112 stays stored-timeline (P11-b7), not streaming.

## Overlay reference integrity

- P15 result refs: union-only verified (overlay validator 0 errors; every cross ref's
  task resolves in overlay allowlist with exact Card-bytes match and subject binding).
- Map-outside / unselected / unknown refs: 0 (validator FAIL paths exercised with 0 hits;
  frozen generic validator's 64 errors are ALL the known `outside Draft Package` class —
  i.e., exactly the overlay refs, no other error class).
