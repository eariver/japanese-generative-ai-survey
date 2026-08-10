# 2026-W32 CI Validation — v0.2 r1

Status: **CI build passed; visual-review correction required before freeze**  
Validated: 2026-08-10  
Workflow run: `31350323821`  
Job: `93339739532`  
Head SHA: `213e8ba1083c6b826448c20074bd7cc66589d0ec`

## 1. GitHub Actions result

The manually triggered `Build weekly survey PDF` workflow completed successfully.

Successful steps:
- repository checkout;
- LuaLaTeX / latexmk compilation;
- Biber bibliography generation;
- final LuaLaTeX stabilization runs;
- PDF artifact upload.

Toolchain observed in the run:
- TeX Live 2026;
- LuaHBTeX 1.24.0;
- Latexmk 4.88;
- Biber 2.21.

Biber found **36 citekeys**. The final latexmk state was `All targets (main.pdf) are up-to-date`.

## 2. Artifact

Artifact name: `japanese-generative-ai-survey-2026-W32`  
Artifact ID: `9048739449`  
Artifact archive digest: `sha256:a374a11474c9dc6d6ea3b9ff802a13569bd956b4b2720a95e65624dc38e8f7d8`

Generated PDF:
- 16 pages;
- 499,024 bytes before ZIP packaging;
- A4 on all pages;
- fonts embedded;
- unencrypted;
- outline/bookmarks present;
- link annotations present.

The artifact was downloaded and the complete 16-page PDF was rendered for visual review.

## 3. Visual review

Overall layout passed:
- cover framing rendered correctly;
- Contents / This Week in AI rendered correctly;
- two-column article flow was intact;
- semantic boxes were readable;
- References occupied the final two pages;
- no blank page, clipping, obvious overlap, or broken glyph was observed.

### Freeze blocker found

The editorial polish changed pagination. The Astra Lead Story now occupies page 3, but Late Breaking still contained a hard-coded reference to `p.3--4` inherited from the validated v0.1 layout.

This did not cause a TeX build failure, but it is an editorial correctness defect and therefore blocks freeze.

## 4. Correction applied after r1

The page reference was made layout-stable instead of simply changing the number:

- `sections/10-lead-astra.tex` now defines `\label{sec:astra-lead}`;
- `sections/90-late-breaking.tex` now uses `p.\pageref{sec:astra-lead}`.

This prevents the same stale-reference class from recurring when pagination changes.

## 5. CI hardening applied after r1

The workflow now includes a `Validate final TeX log` gate between compilation and artifact upload. It fails the workflow if the final `main.log` still contains publication-blocking diagnostics including:

- undefined references;
- undefined citations;
- a request to rerun Biber/LaTeX;
- Overfull hbox;
- Underfull hbox;
- missing-character warnings.

This aligns CI acceptance more closely with the local publication gate rather than treating mere PDF generation as sufficient.

## 6. Non-blocking diagnostic

The CI log contains `lltjp-array: patch FAILED (\@tabular 2)` while LuaTeX-ja patches the current LaTeX/array stack. The run nevertheless compiles successfully and the affected tables render correctly. This is recorded as a compatibility diagnostic to monitor, not a current publication blocker.

## Gate

**Do not freeze artifact r1.**

A new workflow run from the corrected source and hardened CI must pass, after which its artifact should receive the final visual/PDF review.
