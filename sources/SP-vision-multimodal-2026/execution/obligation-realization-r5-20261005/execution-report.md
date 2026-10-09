# Final execution report — TS-003 r5 Final Obligation-Realization Repair (日本語)

## 起点 / 終点

- Starting HEAD / Tree: `2a76ec127257e9af01b785b3c82ef5ee967b06f9` /
  `f7f3ade5800bc1a759e7345769c3b69df95d6c88`（remote一致をread-only確認）
- Final HEAD / Tree: `42d4da2fe2f9c78d933dc8809125ac0c19e9c3e8` / `9d8475a30db412e2d781298047c989d1296326ed`（remote一致確認済み、working tree clean）

## Scope遵守

- Discovery count unchanged: 122 lines維持（新規candidateなし）。
- UI-TARS/OS-Atlas/Aguvis/ShowUI/π₀.5/π₀.7/UWM/WorldVLA/DreamZeroはdeferred ledgerのみ。

## A. D075 regression repair（root cause記録）

- Root cause: post-freeze integrity replay（phase_c）が旧D075 card（caab11b setの
  unresolved版）をbasis-rebindだけでcarryし、前runで検証済みのstaged license cardを
  消費しなかったため、canonical D075が旧状態へregressした。Architecture側のresolved
  bucket行だけが残りcross-artifact矛盾となった。
- Fix: staged license card（claim-1 tail resolved buckets＋claim-2 weights＋
  limitation-2除去）を現package basisで再検証の上消費。D075 old/new SHA:
  `2557ede96a69` → `f42cc795b215`。復元authority: code Apache 2.0 repo-bound、
  30B-A3B-Instruct weights Apache 2.0 bound scope、living-surface維持、
  unresolved limitation除去。

## B. D090 Evidence-depth delta

- claim-1/limitation不変。＋claim-2観測契約（screenshot完全/a11y-tree/terminal streams、
  §2.3/App A.2）＋claim-3行動契約（pyautogui code actions＋COMPUTER_13、§2.4/App A.3）。
  D090 old/new SHA: `52116aea34e6` → `be73f6164ab0`。

## C. D092 stale-boundary correction

- Limitationのみ更新：ScreenSpot-Proをcanonical D120として承認、
  未review successorはdeferred維持。D092 old/new SHA: `9420b747bcbf` → `1188bdb5de56`。

## D. VM-O11/O13・P10/P12

- VM-O11 old/new rationale: SATISFIED維持。旧（4 instruments distinct）→
  新（＋三role chain: diagnostic attribution／scaffold effect PARTIAL維持／
  tool-assisted perception。post-training史の包括主張なし）。
- VM-O13 old/new rationale: SATISFIED維持。旧（thesis列挙）→
  新（＋interface比較・mapping note言及）。
- P10 semantic diff: purposeに三role chain追加、must_coverに1行追加。
- P12 semantic diff: purposeにinterface比較追加、must_coverに1行追加、
  stale D092 successor行を除去（新limitationへensure）。
- Cross-package authority map readback: 6 entries（P07A←D114、P07B←D114/D115、
  P10←D111/D112、P11←D115）。homes不変、重複配置なし。

## Replay結果

- Evidence result-set: `caab11b84274` → `f6ef98cb6b5e6246`（118不変＋3修正）。
- Selection disposition diff: 0（121 selected維持、placements不変）。
- P09: stale VM-D075 unresolved行を除去。canonical bucket 3行（code／weights split／
  released-data）維持。16-package skeleton preserved。
- P15 map 40維持。G01/G02維持。G06 resolved維持。
- Summary/Attention fresh regeneration。FINAL freeze preserved。
- π₀.5 explicit defer rationaleをdeferred ledgerへ記録。
- Shared Core changed: NO。Draft changed: NO（TeX/PDFなし）。
- Lifecycle `ARCHITECTURE_ESTABLISHED`。r5 PENDING（r5 recordなし）。
