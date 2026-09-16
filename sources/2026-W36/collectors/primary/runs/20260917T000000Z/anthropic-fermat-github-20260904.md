# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://github.com/anthropics/fermats-last-theorem
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-04
- retrieval: webfetch markdown of Anthropic fermats-last-theorem GitHub repository front page linked from science article; stored verbatim as returned. Page shows no explicit publication date; 2026-09-04 is edition-attributed from linked science article.
- authority_class: PRIMARY_REPOSITORY

# Retrieved content (verbatim as returned)

GitHub - anthropics/fermats-last-theorem · GitHub

[anthropics](/anthropics) / **[fermats-last-theorem](/anthropics/fermats-last-theorem)** Public

-   [Notifications](/login?return_to=%2Fanthropics%2Ffermats-last-theorem) You must be signed in to change notification settings
-   [Fork 102](/login?return_to=%2Fanthropics%2Ffermats-last-theorem)
-   [Star 1.2k](/login?return_to=%2Fanthropics%2Ffermats-last-theorem)

-   [Code](/anthropics/fermats-last-theorem)
-   [Issues 8](/anthropics/fermats-last-theorem/issues)
-   [Pull requests 1](/anthropics/fermats-last-theorem/pulls)
-   [Actions](/anthropics/fermats-last-theorem/actions)
-   [Projects](/anthropics/fermats-last-theorem/projects)
-   [Security and quality 0](/anthropics/fermats-last-theorem/security)
-   [Insights](/anthropics/fermats-last-theorem/pulse)

main

## Latest commit

## History

[1 Commit](/anthropics/fermats-last-theorem/commits/main/) 1 Commit

## Folders and files

[Definitions](/anthropics/fermats-last-theorem/tree/main/Definitions "Definitions")
[P2M](/anthropics/fermats-last-theorem/tree/main/P2M "P2M")
[Theorems](/anthropics/fermats-last-theorem/tree/main/Theorems "Theorems")
[html](/anthropics/fermats-last-theorem/tree/main/html "html")
[tools/docs-site](/anthropics/fermats-last-theorem/tree/main/tools/docs-site "tools/docs-site")
[verification](/anthropics/fermats-last-theorem/tree/main/verification "verification")
[.gitattributes](/anthropics/fermats-last-theorem/blob/main/.gitattributes ".gitattributes")
[.gitignore](/anthropics/fermats-last-theorem/blob/main/.gitignore ".gitignore")
[ATTRIBUTION.md](/anthropics/fermats-last-theorem/blob/main/ATTRIBUTION.md "ATTRIBUTION.md")
[FinalCheck.lean](/anthropics/fermats-last-theorem/blob/main/FinalCheck.lean "FinalCheck.lean")
[LICENSE](/anthropics/fermats-last-theorem/blob/main/LICENSE "LICENSE")
[NOTICE](/anthropics/fermats-last-theorem/blob/main/NOTICE "NOTICE")
[PROOF-PATH.md](/anthropics/fermats-last-theorem/blob/main/PROOF-PATH.md "PROOF-PATH.md")
[README.md](/anthropics/fermats-last-theorem/blob/main/README.md "README.md")
[formalization.yaml](/anthropics/fermats-last-theorem/blob/main/formalization.yaml "formalization.yaml")
[lake-manifest.json](/anthropics/fermats-last-theorem/blob/main/lake-manifest.json "lake-manifest.json")
[lakefile.lean](/anthropics/fermats-last-theorem/blob/main/lakefile.lean "lakefile.lean")
[lean-toolchain](/anthropics/fermats-last-theorem/blob/main/lean-toolchain "lean-toolchain")

# Fermat's Last Theorem in Lean 4

A complete, machine-checked proof of Fermat's Last Theorem in [Lean 4](https://lean-lang.org), built on [Mathlib](https://github.com/leanprover-community/mathlib4) (Lean 4.33.1; Mathlib `v4.33.0`, pinned by commit in `lakefile.lean`). The argument is that of Frey, Serre, Ribet, Wiles and Taylor-Wiles. `PROOF-PATH.md` names each step and the Lean theorem that carries it, and the `html/` folder presents the whole proof as web pages you can browse offline.

Research artifact. Not maintained and not accepting contributions.

## The statement

`Theorems/Thm_fermat_last_theorem.lean` declares

theorem fermat\_last\_theorem (n : ℕ) (hn : 3 ≤ n) (a b c : ℕ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) : a ^ n + b ^ n ≠ c ^ n

and the default build target `FinalCheck.lean` contains

/-- info: 'fermat\_last\_theorem' depends on axioms: \[propext, Classical.choice, Quot.sound\] -/
#guard\_msgs in
#print axioms fermat\_last\_theorem

so the build fails unless the proof rests on exactly Lean's three standard axioms (no `sorry`, no added `axiom`, no `native_decide`). `FinalCheck.lean` also derives Mathlib's own statement, `FermatLastTheorem`, from this theorem.

## How it was verified

-   **Build.** A from-scratch `lake build` on Lean 4.33.1 (which includes the 2026 kernel soundness fixes), with Mathlib compiled from source. All 60,475 modules of this repository built, every declaration was checked by the Lean kernel, and the axioms are as above.
-   **comparator.** [leanprover/comparator](https://github.com/leanprover/comparator) `v4.33.0` checked the build against `verification/comparator/Challenge.lean`, which states the theorem using only Mathlib. Verdict: `Your solution is okay!`
-   **A second kernel.** [nanoda](https://github.com/ammkrn/nanoda_lib) 0.4.13, an independent Lean kernel written in Rust, accepted an export of the same environment: `Checked 1052234 declarations with no errors`.

No module contains `axiom`, `sorry`, `native_decide`, `unsafe`, `extern`, `implemented_by`, `partial def` or `#eval` (`Challenge.lean` uses `sorry` by design and is not part of the package).

## Reading the proof in a browser

The `html/` folder (about 390 MB) presents this repository as static web pages: the route of the proof step by step; a page for each of the 29,511 theorems and for each of the 1,450 definition modules; a search box over all theorem and definition names; the landmark theorems as a graph. Open `html/index.html` in a web browser; everything works offline, with no web server.

## Check it yourself

-   You need Linux or macOS (some paths are too long for Windows), [elan](https://github.com/leanprover/elan) (it installs Lean 4.33.1 from `lean-toolchain`), and a network connection: Lake fetches Mathlib from GitHub and compiles it from source (about 13 minutes at 96 jobs).
-   The build needs about 5 GB of memory per parallel job (a few modules need up to 36 GB); about 67 GB of disk under `.lake/`, plus C files (about 220 GB) that can be deleted as the build goes. Ours took 5 h 32 min at 96 jobs, with a peak of 153 GB of memory.
-   comparator takes about 15 hours (ours: 14 h 46 min). Run nanoda after the comparator script.

git clone <this repository\> flt && cd flt
LEAN\_NUM\_THREADS=96 lake build
verification/comparator/run.sh
verification/nanoda/run.sh

## About the sources

`FinalCheck.lean` is the default target; `Theorems/` holds the statements, `P2M/Sol/` the proofs, `Definitions/` the definitions, `verification/` the two checks, `html/` the web pages and `tools/docs-site/` the program that generated them. The Lean sources were produced by AI agents building on human-written open-source Lean, with Lean as the arbiter, and are written to be checked rather than read: names are machine-generated. Comments were removed, apart from upstream notices, doc strings and citations (listed in `ATTRIBUTION.md`).

## Licence and attribution

Copyright 2026 Anthropic, PBC; released under the Apache License 2.0 (`LICENSE`). Portions derive from three Apache-2.0 projects credited in `NOTICE`: the [Imperial College London FLT project](https://github.com/ImperialCollegeLondon/FLT) led by Kevin Buzzard, [flt-regular](https://github.com/leanprover-community/flt-regular) and Mathlib.

## About

No description, website, or topics provided.

**1.2k** stars / **102** forks / **13** watching / 8 Issues / 1 Pull request

[truncated for edition-local storage]
