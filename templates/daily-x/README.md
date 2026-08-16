# Daily X TeX template

`jgaidailyx.sty` はDaily X専用のLuaLaTeXスタイル。

設計要件:

- A4縦、10pt。
- 1ページ目のタイトル領域のみ全幅。
- タイトル直後から序論、個別トピック、結言まで全て2段組。
- X URLは自動改行可能。
- 最終ページは `flushend` で左右段を均衡。

各号の `.latexmkrc` から `templates/daily-x//` を `TEXINPUTS` に追加して利用する。
