# Survey LaTeX template

Baseline engine: LuaLaTeX.

Japanese typesetting uses `jlreq` + LuaTeX-ja and the HaranoAji preset distributed with TeX Live.

## Local build

From the repository root:

```bash
latexmk -cd surveys/weekly/2026-W32/main.tex
```

Clean generated files:

```bash
latexmk -cd -C surveys/weekly/2026-W32/main.tex
```

The weekly issue keeps article/package fragments under `surveys/weekly/<issue>/sections/` and bibliography data in `references.bib`.

Semantic boxes provided by `jgaisurvey.sty`:

- `claimboundary`: uncertainty / author-claim / verification boundary
- `communitynote`: X/community observation; never technical-fact evidence by itself
- `latebreaking`: post-cutoff material
- `sourceclass`: compact source-class badge

Do not put generated PDFs or TeX auxiliary files into source control unless the editorial workflow explicitly changes that policy.
