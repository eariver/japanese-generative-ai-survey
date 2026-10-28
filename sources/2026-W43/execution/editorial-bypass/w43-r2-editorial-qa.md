# W43 Core-free editorial QA r2 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE`
Date: 2026-10-25. Branch: `weekly/2026-W43-v2-work`.
r2 preview: `execution/editorial-bypass/w43-r2-reader-preview-UNVALIDATED-20261025.md`
Ledger: `execution/editorial-bypass/w43-r2-citation-confidence-ledger.json` (86 rows: 62P+15T+8N+1 recap; SHA256 `aa42099652b17c3c1052438dcf0babd3792d0d1888fb86876461687a80a5095c`)
Method: 4並列 per-claim監査（P1–P2／P3–P4／P5–P6／P7–P8）＋ FLUX算術の独立再計算 ＋ GH/npm時刻の再照合。

## 1. 31 must-cover × block coverage（全Y）

| Req | Blocks | Y/N |
|---|---|---|
| §1.1 Kimi API先行・時刻・料金・FUTURE | p1-p1, p1-t1, p1-p7, p1-n1 | Y |
| §1.2 MoE対比・計数規約 | p1-p3, p1-p4, p1-t2（r2帰属修正） | Y |
| §1.3 文脈長三層 | p1-p2, p1-t2, p1-p10（r2でFlint帰属・512K追加） | Y |
| §1.4 学習・量子化・bench帰属 | p1-p5, p1-t3, p1-p8, p1-p9 | Y |
| §1.5 重み可用性・約款・価格 | p1-p6, p1-t4（r2でFlint=Apache-2.0分離） | Y |
| §2.1 DeepInfer核・並列 | p2-p1, p2-t1, p2-p8 | Y |
| §2.2 排他二構成・抜粋 | p2-p2（r2軟化）, p2-p3, p2-p9 | Y |
| §2.3 実装条件・除外 | p2-p4, p2-p3 | Y |
| §2.4 MemT記憶・分母分離 | p2-p5, p2-t2, p2-p10 | Y |
| §2.5 paper/README分離・SGLang | p2-p6, p2-p11 | Y |
| §2.6 限界DEPTH_LIMITED | p2-p7, p2-n1 | Y |
| §3.1 待機・提供段階 | p3-p2, p3-t1, p3-p7 | Y |
| §3.2 資格フロー・coming soon区別 | p3-p3, p3-p4, p3-p8 | Y |
| §3.3 安全積層・未検証明示 | p3-p3, p3-p5, p3-p9 | Y |
| §3.4 auto-mode三段 | p3-p6, p3-t2 | Y |
| §4.1 post-train・keyframes矛盾 | p4-p2（r2出典注記）, p4-p3 | Y |
| §4.2 速度再計算 | p4-p4, p4-t1（25.37x/22.31x/95.52%再計算VERIFIED） | Y |
| §4.3 Elo・価格 | p4-p5（r2で1089導出値注記）, p4-p6 | Y |
| §5.1 Voxtral言語数UNRESOLVED | p5-p2（r2日付のみ・50超）, p5-p3, p5-t1（r2で50超） | Y |
| §5.2 内部評価・判定器 | p5-p4 | Y |
| §5.3 Ming開放・AA距離 | p5-p5, p5-t2, p5-p8 | Y |
| §5.4 Eleven互換・指南未開封 | p5-p6, p5-p9 | Y |
| §6.1 協調開示五段階・CVE留保 | p6-p2, p6-p3, p6-p6 | Y |
| §6.2 隔離・頁/RSS時計 | p6-p4, p6-p7 | Y |
| §6.3 来歴・W42区別 | p6-p3, p6-p5 | Y |
| §7.1 Bio手順・盲検・来歴 | p7-p2, p7-t1, p7-p6 | Y |
| §7.2 Low-resource二層・費用 | p7-p3, p7-p4（r2修飾子補完）, p7-t2（r2同）, p7-p7 | Y |
| §7.3 限界・来歴保存 | p7-p5, p7-n1 | Y |
| §8.1 Decisions GA・料金・上限 | p8-p2, p8-t1, p8-p6 | Y |
| §8.2 TanStack安定/実験・二時刻 | p8-p3, p8-p4, p8-p7（15:18:14Z/15:21:49Z再確認） | Y |
| §8.3 DeepSeek配布・移行・約款 | p8-p5, p8-t2, p8-p8 | Y |

## 2. 19 placements（12 PRIMARY＋7 SUPPORTING、重複・昇格なし）

P1: Kimi PRIMARY／Flint PRIMARY／Nemotron SUPPORTING。P2: DeepInfer PRIMARY／MemT PRIMARY。
P3: Duet PRIMARY／1Password SUPPORTING／auto-mode SUPPORTING。P4: FLUX PRIMARY。
P5: Voxtral PRIMARY／Ming SUPPORTING／Eleven SUPPORTING。P6: Patch PRIMARY／Securing PRIMARY。
P7: Bio PRIMARY／Low-resource PRIMARY。P8: Decisions PRIMARY／TanStack SUPPORTING／DeepSeek SUPPORTING。
HOLD（moss-trainer）・REJECT 12件・Metrics OUT・Grok NEVER_STORYの記事昇格なし。未選択候補の主役化なし。

## 3. 5 LIMITED・68 Attention・Gate継承

32 PARTIAL Evidence Cards＋32 Views、51 Materiality、Completeness LIMITED、residual 5はいずれも本文の境界注記（各章NOTE＋文中限定）に継承。68/68 native Review AttentionはArchitecture不変のため継承（再生成なし）。
Human Architecture r1 APPROVED維持。`今週の総括`はDraft要件であってArchitecture改訂・P9・32件目ではない。

## 4. Issue list（P0なし）

P0: 0件。REQUEST_CHANGES事由なし。
P1（7件、全てr2修正済み）: p1-p3（2.2B規約の帰属）／p1-t2（文脈帰属）／p1-p6（約款一括り）／p1-t4（Flint約款 cell）／p1-p10（文脈帰属・512K）／p5-p2（12:00過剰精度・50表記）／p7-p4（Sol修飾子・Luna比較対象）。
P2（6件、全てr2修正済み）: p2-p2（決定的側の断定軟化）／p4-p2（FAQ出典注記）／p4-p5（1089導出値注記）／p5-t1（50超）／p5-p7（50超）／p7-t2（GPT-6.1表記）。
棄却1件: p2-p6への「CC BY-NC-SA 4.0」版付与提案は証拠に版表示がなく捏造になるため棄却、無版のまま維持。

## 5. Table verdicts（15件）

TABLE_OK 13件: p1-t1, p1-t3, p2-t1, p2-t2, p3-t1, p3-t2, p4-t1, p5-t2, p7-t1, p7-t2, p8-t1, p8-t2（内容正確）＋ p1-t2/p1-t4/p5-t1（r2修正後OK）。
TABLE_UNRESOLVED 0件（残留なし）。ただし全15表は区切り文字テキスト形式のままであり、出版用表組み・桁区切り・版管理は将来の組版工程の責務（TABLE体裁は未解決だが内容は解決済み）。

## 6. Page-depth assessment（水増しなし）

r2本文は約22,200字（62段落・平均約280字の密な技術文）＋15表＋8注記＋総括5段落。35pp body見積（37pp見込・38目標・44上限）に対しては薄い部類であり、113ブロック数が37ppを保証しないことを明示する。証拠の裏づけを超える膨張は行わず、不足分は「表の組版・図版・出典一覧・索引」という出版工程の側で吸収すべきであり、本文の水増しでは吸収しない。P2/P5/P7/P8の機構・評価表は要件密度を満たす。

## 7. 「今週の総括」（配置・抜粋）

- 配置: P8最終NOTEの後・出典一覧の前、見出し exactly `今週の総括`、実質5段落＋編集注記（採用時削除指定）。P9該当なし、新規候補配置なし。
- 対応: 段1＝P1–P2（公開状態・計数・排他・分母）、段2＝P3・P8（権限・料金時刻約款）、段3＝P4–P5（再計算vs独立測定・言語不一致）、段4＝P6–P7（開示工程・隔離・盲検・hidden）、段5＝展望（FUTURE・W44 OUTの先取り禁止）。
- r2改訂（50超・Flint約款分離・GPT-6.1等）と矛盾する数値・時刻・固有名修飾を含まないことを確認。変更不要。
- 抜粋（段1）: 「今週の生成AI関連の発表を貫くのは、モデルの能力が向上したという事実だけではなく、その能力を**どの時点で、どの条件で、実際に利用できるのか**という問題である。」

## 8. Residual risks（将来工程への引継ぎ）

1. Oct18 FAQ原文・PRNewswire PR原文・AA原表・Voxtral細部URL（9言語カード・22表）は未取得のまま（UNRESOLVED維持、捏造せず）。
2. 全ベンチ・速度・Elo・費用は発行元測定のまま（独立再現なし）。
3. 表15件の組版・図版化は未実施。4. Core Draft Stageは依然BLOCKED（別途所有者判断が必要な将来出版経路は本QAの範囲外）。
4. `runner.generated_at=2026-10-25T14:00:00Z`は実行時刻として未検証のまま（いかなる provenance にも昇格させない）。

## 9. 非改変の記録

Canonical State（`ARCHITECTURE_ESTABLISHED`）、Gate・Architecture・Selection・Evidence・main・Frozen Coreに変更なし。Native Draft Package/Result・Synthesis・QA receipt・`DRAFT_COMPLETE`・`ADVANCE_STAGE`要求・TeX/PDF・Publication Previewは生成・要求せず。本r2一式は `execution/editorial-bypass/` 下の非正規編集資産であり、正式検証PASSを主張しない。
