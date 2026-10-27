# W43 r8 PDF links / fonts / structure (actual PDF bytes, not TeX strings)

Date: 2026-10-27 JST. PDF: 487351 bytes, SHA256 `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`. Parser: PyMuPDF 1.28.2 + `pdfinfo`/`pdffonts` (poppler). All claims from binary annotations/fonts/boxes, not TeX source alone.

## Link annotations

- Total `/Annot` URI actions: 75 (all pages).
- Unique `http` targets: 28. Full list:
  - https://1password.com/blog/1password-for-ai-agents
  - https://api-docs.deepseek.com/news/news261017
  - https://api.github.com/repos/TanStack/ai/releases/tags/%40tanstack%2Fai%401.0.0
  - https://claude.com/resources/articles/auto-mode-default-in-claude-code
  - https://claude.com/resources/articles/claude-duet
  - https://developers.openai.com/api/docs/guides/decisions
  - https://developers.openai.com/api/reference/resources/decisions/methods/create
  - https://developers.openai.com/api/reference/typescript/resources/decisions/methods/create
  - https://elevenlabs.io/blog/realtime
  - https://fal.ai/models/blackforestlabs/flux-3-max/text-to-video
  - https://github.com/MemTensor/MemT-1.0/blob/main/README.md
  - https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE
  - https://github.com/deepseek-ai/DeepInfer/blob/main/README.md
  - https://github.com/deepseek-ai/DeepInfer/blob/main/deepinfer/environ.py
  - https://github.com/inclusionAI/Ming-3.0-tts
  - https://huggingface.co/RecursiveSI/flint
  - https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/commits/main
  - https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-4GB
  - https://mistral.ai/news/voxtral-3
  - https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
  - https://openai.com/index/decisions-api
  - https://openai.com/index/low-resource-programming-languages/
  - https://openai.com/index/scaling-ai-research-for-complex-biological-data/
  - https://openai.com/index/securing-our-frontier-model-training-environment/
  - https://recursive.com/updates/introducing-recursive-flint
  - https://registry.npmjs.org/@tanstack%2Fai
  - https://www.kimi.ai/blog/kimi-k3-1-pro
  - https://x.com/Kimi_Moonshot/status/2113680701770068067
- 28 unique vs 36 bibkeys is EXPECTED: 36 keys legitimately share URLs (e.g. multiple DeepInfer paths, GH vs npm separation, date-only entries with `URL未取得`). Not a failure. No malformed URIs; CJK punctuation in URIs: 0.
- Official Decisions Guide present: `https://developers.openai.com/api/docs/guides/decisions` (annotated, selectable, p18 + bib). Scoped npm `%2F` URL present: `https://registry.npmjs.org/@tanstack%2Fai` + GH `%40tanstack%2Fai%401.0.0` — both annotated, encoded forms preserved.
- Link action validity: all 75 annots are URI kind; no dead GoTo/broken actions observed. `NOT_VERIFIED`: live HTTP reachability not probed (offline build integrity only).

Raw JSON: `pdf-links-fonts-raw-r8.json` (see below for generation).

## Fonts (embedded subsets)

`pdffonts` / PyMuPDF `get_fonts`: 14 embedded subsets, all embedded (no system-only):
- HaranoAjiMincho-Regular/Bold (CJK body), HaranoAjiGothic-Regular/Bold (CJK headings/boxes)
- LMRoman7/8/9/10-Regular, LMRoman10/12-Bold, LMRoman12-Regular, LMSans10-Bold, LMMono8/10-Regular
- No unembedded/Type3 failures. Selectable Unicode verified: Japanese `週刊生成` + `承認` extract correctly.

## Page boxes / structure

- `pdfinfo`: 22 pages, A4 `595.276×841.89 pts` all pages, PDF 1.7, Creator LuaLaTeX, Producer LuaTeX-1.24.0, Title `Japanese Generative AI Technical Survey – 2026-W43`, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`, no encryption/forms/JS.
- All pages: MediaBox/CropBox A4, rotation 0. Text layer present all pages (PyMuPDF extraction succeeds incl. CJK).
- Where unsupported: independent PDF byte reproducibility (`byte-identical rebuild`) NOT claimed — nondeterministic metadata (CreationDate) differs; semantic/visual equivalence proven instead.

## Generation

```bash
python3 - <<'PY'
import fitz, json, pathlib
doc=fitz.open('sources/2026-W43/execution/core-free-preview-r8/main.pdf')
rec={"pages":len(doc),"annots":[{"page":i,"uri":l.get("uri")} for i,p in enumerate(doc,1) for l in p.get_links() if l.get("kind")==2],
"unique_uris":sorted({l.get("uri") for p in doc for l in p.get_links() if l.get("kind")==2}),
"fonts":sorted({f[3] for i in range(len(doc)) for f in doc[i].get_fonts()}),
"boxes":[{"page":i,"w":round(p.rect.width,2),"h":round(p.rect.height,2)} for i,p in enumerate(doc,1)]}
pathlib.Path("sources/2026-W43/execution/core-free-preview-r8/pdf-links-fonts-raw-r8.json").write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding="utf-8")
PY
```
