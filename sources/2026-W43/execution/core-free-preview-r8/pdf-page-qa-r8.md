# W43 r8 PDF page QA (all 22 pages viewed at readable/full resolution)

Date: 2026-10-27 JST. PDF: `main.pdf` 487351 bytes, SHA256 `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`, 22 A4 pages (595.276×841.89 pts). Renderer: Ghostscript 10.06.0 `png16m r150` → `pages/p-01..p-22.png` + 3 contact sheets. Viewer: full-resolution PNG inspection (all 22).

Build: LuaHBTeX 1.24.0, lualatex ×2, exit 0/0, 0 LaTeX errors, 2 Overfull `\vbox (2.61676pt)` (output-active, pp14–15 boundary, benign — visually verified no clipping).

## Per-page matrix (PNG SHA256 full)

- p01 `0e3e3cb0d0c10461428d708430038d30853578feb27e0ce58989f48cfff8a144` — Cover: title, 2026-W43, 2026-10-24, Japanese cover story, cutoff/Repo/Build lines, Evidence-chain note, proof footer `NONCANONICAL… NOT A PUBLICATION PREVIEW`. No meta leak. No clipping.
- p02 `5cca832bb3e2feef516d7bf8d2e07d484914b65e31800cb603aad0c96fb8434d` — TOC (目次): 8 sections pp3/6/9/11/12/14/15/17, matches actual starts. No clipping, links blue, page number 2.
- p03 `1a9a0ff950f91a95a54ec5426c1db3a1e1a84b2cc9bf7958d378b2fef36634b0` — §1 start two-column, N10 sentence in correct (non-inverted) form, Table 1 full-width readable, no row drop, prose continues. No clipping.
- p04 `1e2a091fe4967bba68fb0bf1015044ce0e8d38dbedf370f6ceade0db6e71a3ef` — Table 2 full-width: **A corrected** `totalとactive per tokenは計数規約が異なり、直接比較できない` visible; old `承認済みArchitecture…` absent. Two-column prose both sides, Table 3, no corruption. TOC p3 ok.
- p05 `3ac4b8269aa7ba8edf69330f5aa3f7d11322c29f7c0f597be150ce99681fcf6a` — Table 4, two-column prose, blue figure box (文脈長の二層) + gray reading note, all readable. No clipping.
- p06 `435c0200eccbac4d4b7ecbf1718d010bbdd49c61e34e4ecbb0f44d8b2b86875f` — §2 start two-column, Table 5 full-width, code-adjacent prose, no truncation.
- p07 `c8abb11d5ecf287e1679163cba850ee9fdc52fdf309c96e3a7774c6aab005b2d` — Table 6, two-column, section `論文とソフトウェアの権利を分ける`, no clipping.
- p08 `6afd1d2b12abd499e60f3417d6b2412dc106527b9e32086171204e27af0d38b6` — Table 7, long code block (設定例A/B, environ.py, SamplingParams) full-width readable, no wrap loss, §2 recap prose. No clipping.
- p09 `b0f33faf3a1c8ff983606b7ad59db32c601d172cda0415bac5a6db60766764f3` — §3 start two-column, Table 8, `資格に触れずに働く設計`, no corruption.
- p10 `686e001a0408d05866f877f8336454e4641603ccb9b0b7b2415d233d37ddc4bf` — Table 9, blue figure (資格・承認フロー), gray reading note, two-column, no clipping.
- p11 `d47c55cd3389851c021f91986369f19cc885135bef6493e9b956d1099d2ef5dc` — §4 start: **B corrected** — new epistemic sentences `PR・ブログは可用主張を示すが…発行者間の確定した矛盾とはしない…提供確定は導けず` visible; old `承認済みArchitecture…legacy` + redundant sentence absent. Table 10 full-width (25.37x/22.31x/95.52%) intact. Two-column, no corruption. TOC p11 ok.
- p12 `3904602066490f3ad4c694da8307232f423406252f38f2d5d468a7483b75e300` — §4 cont + §5 start, reading note, Table 11 header, two-column. No clipping.
- p13 `8fa0fc962ef6f69b18b739b8ddb892993689e237508a4536577f7b915366fda9` — Tables 11/12 full-width, §5 prose two-column, no row loss.
- p14 `8ea35d0b47a7df4b6768ac15d59c03efe82a27a8780b1b08f5f916a0013391cc` — Table 13/16 full-width, §6 start, reading note, two-column. Overfull vbox boundary but visually no clipping/tail loss.
- p15 `3a179de5af8190f5e9b9af959330cc58084a49d566aa52716ad75d3414c0c962` — §6 cont, blue figure (協調開示の五段階) + reading note, §7 head at bottom. No clipping despite overfull warning.
- p16 `722dcc520069a309e3bb522b05168aaf72adcd12467036182a09bd8ccd3f3018` — §7 two-column, Table 14, prose, no corruption.
- p17 `b2187f03ff2ecb817530dd13878cb99e87b257c9fd42aa77a52a2521db67a993` — Tables 15/16, §7 cont + §8 head, reading note, two-column. No clipping.
- p18 `546f9456a6aaa812b7b00fc25788ebef9ba0110d90999a23b7c9fe37ccf62cd3` — §8: Table 17, **long Decisions JSON code block full-width intact** (model gpt-6-luna, questions/answers, probabilities, confidence 0.93), no token loss, URL `https://developers.openai.com/api/docs/guides/decisions` blue and split but selectable (see links QA). No clipping.
- p19 `4060661adb8df062f5bfd95347d9fcb15ae49439537b02efa7f235bf6dcf4517` — Table 18/19/20, §8 prose, reading note, `今週の総括` head at bottom. 5 recap paras start here (TeX-verified 5/5 identical). No clipping.
- p20 `c7a2a7af4c9c63e6d85dc62e66f102be4594e64b0b151fa12058bcff3a7b304c` — Recap paras cont two-column (Kimi/API vs Flint, Duet/1Password, FLUX recomputation, Voxtral language counts, Decisions/TanStack). No blank body, no production note. `出典一覧と確認水準` + `参考文献` heads at bottom.
- p21 `95d5a44dc637e4669174c0e427d4ea4ca5f1f7fc7dd9d3f4c0fbe2a7b82a2b1b` — Bibliography two-column start ([KIMI-X]…[DI-README]), URLs blue, wrapped but complete, no key loss. 36 keys order preserved (TeX-verified).
- p22 `0663c19fe3dfabf0bd9d054a1223eb73e28f3acf6997aa4a7e0522fc4b249773` — Bibliography cont: **[recap] C corrected** `本号の各主題を整理した派生記述` visible; old `P1-P8横断の編集合成` absent. End proof footer `NONCANONICAL… NOT A PUBLICATION PREVIEW`, page number 22. No blank tail beyond footer.

Contact sheets: `contact-sheet-01.png 822241a2…`, `02 cacb6423…`, `03 964bbc2f…` (thumbnails only; verdicts from full-res above, not sheets).

TOC mismatch: none (3/6/9/11/12/14/15/17 all match). Clipping/table corruption/URL wrapping: none observed. A p04 / B p11 / C p22 confirmed at actual new pages; old strings absent from printed text (PDF text search 0 hits).
