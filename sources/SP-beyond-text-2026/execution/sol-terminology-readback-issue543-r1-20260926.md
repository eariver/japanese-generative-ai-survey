# Sol terminology readback — TS-002 Issue #543 r1

Date: 2026-09-26 JST

## Disposition

`REQUEST_CHANGES / BROAD_SCAN_INCOMPLETE`

Issue #543 cannot be closed yet. The worker performed a substantial broad scan (90 ledger decisions: ISSUE_SEED 45 / BROAD_SCAN 45; REPLACE 73 / RETAIN 13 / ESCALATE 4), regenerated a 76-page candidate, and preserved the production gate. However, Sol independent readback found multiple reader-facing literalizations outside the worker ledger, so the Issue #543 acceptance condition — seed-independent broad terminology closure — is not yet satisfied.

Reviewed authority before this Sol record:

- Branch: `special/beyond-text-2026-work`
- Worker final HEAD: `7e9e140b44584a5ef0295f3a3126905eac19f08a`
- Worker final tree: `9ce6a6d91c0ea7a740b37f9ea9caafc8dde50074`
- main: `0bbb02b3c5963403860897daec2feaf61e82589a`
- main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`
- PDF SHA-256: `94f6b211b190edd5c5eb685052631be445b50119e3aa3125fe32f007a4f16014`
- Candidate SHA-256: `77d6be816aaec5a17ddf176cf741d6d563ebaa308f05ccfe9c719f499b1aab7c`
- Pages: 76
- Core: `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending / HUMAN_GATE_REACHED`

## What passed

- Remote guards passed.
- Human Publication Preview r7 REQUEST_CHANGES was recorded canonically.
- Architecture approval remained approved.
- #533/#539 frozen zero-count regressions were preserved according to the worker audit.
- `autocite` sequence remained 1259; 139/139 binding remained complete.
- `references.bib` remained byte-identical.
- Worker broad scan did materially expand beyond the Issue seed list.
- CI build and validation passed; no Freeze/Release was entered.

## Sol independent broad-scan findings

The following are examples of terms still present in `surveys/special/beyond-text-2026/main.tex` that are not acceptably closed by the current ledger. This list is a minimum set, not permission to limit the next pass to these strings.

### 1. Hardware / modality / evaluation literalizations

- `消費者用図形処理装置` — GPU context; should be source-bound to `consumer GPU` / `民生GPU` rather than a literal expansion of GPU.
- `多峰入出力` — in Gemini image-model context this appears to mean `multimodal input/output`, not a multimodal probability distribution; should be `マルチモーダル入出力` or equivalent source-bound wording.
- `人文横並べ` / `人文・自動評価` — apparent literalization of human side-by-side / human evaluation; should use `人間によるside-by-side評価` / `人間評価` as source permits.
- `並列道具` — likely parallel tool use/calls; source-bind to `並列ツール呼び出し` or the exact canonical term.

### 2. Dialogue / workflow / music literalizations

- `多回合` / `多回合延長` — use `マルチターン` / `複数ターン` where the source means multi-turn.
- `流派` in music-generation controls — where the source means genre, use `ジャンル`.
- `刈込` in editing workflow — where source means trim/trimming, use `トリミング`.
- `続成` — likely continuation/continue generation; source-bind to `継続生成` or the exact product term.
- `音楽 caps` / `音響 caps` — likely `MusicCaps` / `AudioCaps`; restore dataset identity if source-bound.
- `節・副歌` — where the source means verse/chorus, use canonical music terms (`verse / chorus`, `ヴァース / コーラス`) rather than a Chinese-influenced literalization.

### 3. Video / product-surface literalizations

- `鋳造` in the Movie Gen capability sentence — canonical source meaning must be re-read; do not infer blindly.
- `単走` in video-duration wording — source-specific meaning must be established.
- `首尾frame` — if first/last frame, normalize to `開始/終了フレーム` or source canonical naming.
- `外側描画` — if outpainting, use `outpainting（アウトペインティング）`.
- `動作接続器` — likely motion adapter; source-bind to `モーションアダプター` / canonical component name.
- `閉鎖頂点` — determine whether source means closed frontier / closed SOTA / proprietary frontier; current Japanese is not reader-safe.
- `基準測定` — if benchmark, use `ベンチマーク`.
- `検査点` — if model checkpoint, use `チェックポイント`.
- `通貨拘束` — current wording is semantically invalid in context; identify the original concept (likely version/checkpoint currency/recency) and restore a natural technical term.

### 4. Speech / architecture literalizations

- `位置鋭敏注意` — Tacotron/Tacotron 2 context; source-bind to `location-sensitive attention` and a natural Japanese gloss.
- `群化符号` — VALL-E 2/grouped-code context; use the source canonical term such as grouped code modeling/grouped codes.
- `多能高忠実モデル` — verify the underlying descriptor; likely `versatile high-fidelity` and should not retain `多能`.
- `系列網` — if RNN/recurrent network or seq2seq architecture, restore the exact canonical identity.
- `近似波形合成` — if the source is Griffin-Lim, name `Griffin-Lim` rather than a generic literalization.
- `三膨張循環`, `十要素混合` — source-bind to the actual dilation cycle / mixture-component terminology.

### 5. Paradigm / solver terminology still worth reviewing

- `予測子修正子` — likely predictor-corrector; canonical English should remain visible.
- `規模則` — likely scaling law; prefer `スケーリング則` if source-bound.
- `再流` — Rectified Flow `reflow`; preserve canonical `reflow` where appropriate.
- `一致性` in the front-matter three-layer glossary — current edition elsewhere standardized Consistency Model family to `整合性`; check for inconsistency/regression.
- generated-sample sense of `標本` — review whether `サンプル` is the canonical reader-facing choice; statistical-sample uses may be retained separately.

### 6. Metric identity remains insufficiently normalized

Current music/evaluation prose still contains generic labels such as:

- `帯域収束 23.0 dB`
- bare `距離` values
- bare `乖離` values
- bare `整合` values

Where these correspond to named metrics (e.g. FAD, KL divergence, CLAP score or another source-specific metric), restore the canonical metric identity rather than leaving a generic Japanese noun.

## ESCALATE resolution

The current ledger still has four ESCALATE rows. A final-close terminology issue should not leave these unexamined.

### Classification score

The VQ-VAE-2 primary paper explicitly names **Classification Accuracy Score (CAS)**. Therefore the residual `分類得点` in the VQ-VAE-2 boundary paragraph can be resolved to `Classification Accuracy Score（CAS）` rather than left ESCALATE.

### Full-band extraction

The residual `均衡ある全帯域抽出` is not reader-safe. Primary-source readback shows the DAC / Improved RVQGAN paper describes **Balanced data sampling** that deliberately samples known full-band audio sources. This concept is associated with `btd008` (DAC), while the current sentence is bound to `btd007` (EnCodec). This is a source-binding defect surfaced by terminology review, not merely a word-choice problem.

The next pass must determine the exact intended claim. If the intended claim is DAC balanced full-band sampling, a narrowly scoped citation-binding correction to `btd008` (or source-supported equivalent) is authorized even though prior invariants normally freeze citation sequence. Correct source binding takes precedence over preserving an incorrect citation. Record this as an explicit exception in the ledger and invariant audit.

### Other ESCALATE rows

- `自然さ得点`
- `濾波崩壊`
- `膨張形式`

must each be re-read against the active source / consumed primary material. Do not carry them forward as unresolved solely to satisfy a zero-write boundary. If the source still does not support a canonical replacement, retain only with a precise reader-facing explanation that the Japanese term itself is technically valid; otherwise replace.

## Required next pass

Run an Issue #543 r2 broad residual pass on the same branch. This pass must:

1. start from the current remote authority after this Sol review record;
2. treat the examples above as mandatory review seeds, not an exhaustive list;
3. perform another seed-independent scan across the entire reader-facing manuscript;
4. include variants/synonyms, not only exact string matches;
5. re-read primary/Evidence sources for ambiguous canonical terms;
6. resolve the existing ESCALATE rows where possible;
7. permit the one narrowly scoped citation-binding exception described above if source readback confirms it;
8. regenerate the exact PDF and rerun source + rendered broad scan;
9. stop again at Publication Preview pending;
10. do not Freeze or Release.

Issue #543 remains OPEN.
