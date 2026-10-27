# W43 reader-to-r8 content mapping (native Draft basis vs approved r8 proof)

Method: headline equality, deck key-phrase presence, block-type census per package; r8 section text scanned for draft block key terms. r8 prose is an approved editorial enrichment of the native Draft basis — NOT byte-equal; no silent equivalence claimed.

## P1: 公開前の巨大さと手元の重み――KimiのAPI先行とFlint・Nemotronの対照
- draft blocks: 20 {'HEADING': 4, 'PARAGRAPH': 10, 'TABLE': 4, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 4/4
- draft TABLE blocks: 4 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 8/8

## P2: 推論を切り出し記憶を持たせる――DeepInferとMemTの実装条件
- draft blocks: 20 {'HEADING': 5, 'PARAGRAPH': 11, 'TABLE': 2, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 5/5
- draft TABLE blocks: 2 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 8/9

## P3: 働く前に権限を決める――Duetと1Password・auto-modeの境界
- draft blocks: 16 {'HEADING': 4, 'PARAGRAPH': 8, 'TABLE': 2, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 4/4
- draft TABLE blocks: 2 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 2/2

## P4: 速さの見出しを割り算から読む――FLUX 3 Maxの数表検証
- draft blocks: 12 {'HEADING': 3, 'PARAGRAPH': 6, 'TABLE': 1, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 3/3
- draft HEADING verbatim hits: 3/3
- draft TABLE blocks: 1 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 7/9

## P5: 声の三様式を読む――VoxtralとMing・Elevenの条件と原表
- draft blocks: 16 {'HEADING': 4, 'PARAGRAPH': 8, 'TABLE': 2, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 4/4
- draft TABLE blocks: 2 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 5/5

## P6: 見つけて直し隔離して学ぶ――協調開示と学習環境の安全
- draft blocks: 10 {'HEADING': 2, 'PARAGRAPH': 6, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 2/2
- draft TABLE blocks: 0 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 4/4

## P7: 手順が結果を決める――生体摂動と低資源言語の評価設計
- draft blocks: 13 {'HEADING': 3, 'PARAGRAPH': 6, 'TABLE': 2, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 2/3
- draft TABLE blocks: 2 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 6/6

## P8: 判断をAPIに道具を束ねる――DecisionsとTanStack・DeepSeek配布
- draft blocks: 14 {'HEADING': 3, 'PARAGRAPH': 7, 'TABLE': 2, 'NOTE': 1, 'CLAIM_BOUNDARY': 1}; status=ESTABLISHED
- r8 section present (headline-equal): YES
- deck key-phrase hits in r8 section: 4/4
- draft HEADING verbatim hits: 3/3
- draft TABLE blocks: 2 (r8 renders full-width tables per section; counts verified separately: 20 total)
- distinctive-term hits: 7/7

## Recap and bibliography
- r8 recap section present: YES (5 paragraphs, verified in r8 QA)
- r8 bibkey count: 36 (expected 36)
- CURATED_REVIEW_REQUIRED keys present (spot): counted in QA as 15

## Fixed A/B/C caveats (must survive)
- A p04 Flint total-vs-active: PRESENT
- B p11 FLUX FAQ: PRESENT
- C p22 recap derived: PRESENT

## Native-basis census
- total draft blocks P1–P8: 121 {'HEADING': 28, 'PARAGRAPH': 62, 'TABLE': 15, 'NOTE': 8, 'CLAIM_BOUNDARY': 8}
- synthesis: status=ESTABLISHED version=v1.0

