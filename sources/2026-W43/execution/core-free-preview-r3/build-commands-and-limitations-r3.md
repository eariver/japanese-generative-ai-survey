# W43 r3 build commands and limitations

Start `36bb0eb2…` verified (parent `f29e77eb…`, diff contract only; main/frozen 6-way PASS).
r3.5 inputs pinned exact; r3.5 checker exit 0 PASS (unchanged).

## Commands (exit 0)

- `python3 /tmp/opencode/w43_r3_proj.py` → projection `63ad2617…` (POST preserved, TanStack note, dup cleanup).
- `python3 /tmp/opencode/w43_r3_tex_gen.py` + bib transplant (r2 complete block) → TeX `bb0e7e1d…` (20/3/36).
- `lualatex …/core-free-preview-r3/main.tex` x2 → PDF `d0fa8b56…` 483305B 22p, 0 Illegal/Overfull/Errors, metadata detokenize-preserved.
- `print-semantic-fidelity-check-r3.py` → `PRINT_SEMANTIC_PASS` (10 pos + 4 neg), exit 0.
- `pdftoppm -png -r 150` → 22 PNGs; PIL → 3 contact sheets; 300dpi spot p-18/p-21 verified.

## r2 -> r3 deltas (only print-fidelity repairs)

- F-R3-01: L473 POST restored (r1/r2 loss eliminated); TeX `\texttt{POST /v1/decisions}`; p-18 verified.
- F-R3-02: URL regex excludes JP punct; body URL clean; SHA via `\nolinkurl`; 34 http URLs 0 malformed.
- F-R3-03: 18/15/2/1/0 audit (false 0-unused corrected); TanStack exact-key 典拠 line added to p8-f2 (only body addition).
- F-R3-04: allowlist (TITLE/TOKEN/PATH/DUP/TANSTACK/POST-identical) + validator with 4 negatives.
- Body otherwise identical; pagination unchanged 22p.

## Limitations

22p honest (1/1/18/2) vs 38/44; all 31 visible (20/11 worker-observed, no new authority). No padding, no new research. Edition-local only; State/Core/Architecture/Selection/Evidence/Gates/main/Frozen untouched; no Stage/Freeze/Release. `.aux/.toc/.out` excluded; `main.log` force-added (required artifact).
