# J-GAS W43 — 編纂Solによる包括独立監査の裁定

Date: 2026-10-26 JST
Status: R32_FULL_REQUEST_CHANGES_ACCEPTED / TEN_ISSUES_ONE_BATCH / NOT_PDF_READY
Repository: eariver/japanese-generative-ai-survey
Existing branch: weekly/2026-W43-v2-work

独立監査原文 20261026022400_SolReview.md、固定対象 efac8324ff7a9f35ad34be391ba2ea328cfc1722、Tree 61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43。
P0=0・P1=3・P2=7を全件採用する。Museの自己評価ではなく、独立監査の31要件20件COMPLETE・11件PARTIALを新たな基準とする。Human承認済みArchitecture r6に差戻さない。

## Preview前に必須のP1是正
- R32-FULL-001: P2 MemTの66倍は128K履歴のフル文脈KV cache比で保存容量を削減した発行元主張。スループット・速度・持続性能ではない。1.86倍の異なる指標は一次原表を取得できなければ未確認と明示。11ベンチ上位は評価対象のparametric-memory方式内での順位で、textual-memory方式全体を上回るとは言えない。本文・表・台帳・出典を同時に直す。
- R32-FULL-002: P6協調開示五段階の4は影響製品の更新準備、5はパッチ提供後の案内と展開支援。DaybreakとPHP checkerは工程外の関連施策に配置する。描画抽出RENDERED_TEXTと原HTMLを区別し、CVEの存在・不存在を誤断定しない。
- R32-FULL-003: 20表の全物理データ行へrow_idを付与し、ledger.table_rowsと追加29claimsのrow_idを結合。p3-t2の分類器行欠落を補い、p1-t2の編集注記をデータ行扱いにしない。製品/数値/単位/版/出典・時刻を含む双方向機械照合をEdition-localスクリプトで実施。79件などの総数だけでは合格させない。

## 同じ一括修正に含むP2
004 npm @tanstack/aiと時刻出典のスコープ修正。005読者本文冒頭の運用メタ情報分離。006未照合FAQからの公式資料間矛盾を断定しない。007Duetとcoming-soonの1Password概念経路を分離。008Voxtralの料金単位と評価比較対象を確認または明示的未検証にする。009P7費用・品質条件とP8 MITライセンスのartifact別範囲。010 DeepInferの未確認importを実行例に見せない、日本語・留保反復の整理。

## 実行と停止の条件
前の小改稿r3.2.1指示は未実行であり、今回の統合r3.3契約が優先する。19 SELECTED、8章、31要件、5 LIMITED、68 Attention、五段落の「今週の総括」を維持。過去r1～r3.2の履歴を改変しない。
Museは既存branchへedition-local r3.3の読者原稿・ledger・source crosswalk・QA・全表検証スクリプトと結果・handoffを一括作成する。全P1と表joinの是正を満たせなければ「完了」扱いにしない。
完了後、編纂Sol確認と独立Solによる固定SHA差分クローズ監査を一度実施。重大誤りが解消した場合のみCore非依存で明示的に非正規のPDF Previewを組版し、実ファイルをHumanへ提示する。Previewの提示は正式Human Preview Gate承認・Freeze・Releaseを含まない。
Frozen Core v2は不変、機械Draftはpending。