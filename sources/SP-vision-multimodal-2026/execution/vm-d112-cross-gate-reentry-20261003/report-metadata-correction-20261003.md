# Report Metadata Correction (append-only, no historical rewrite)

Classification: `REPORT_METADATA_CORRECTION_ONLY`

This note corrects HEAD metadata stated in prior-turn reports. No historical
commit, report file, or authority bytes are altered by this note.

- A prior turn final report incorrectly stated starting HEAD `e5c464...`.
- `turn-r8-v4-verification-report.md` incorrectly states starting HEAD `808289...`.
- Actual immediately prior branch HEAD for that turn was `84fce3059407284e5f3f08be662eb344d3c96b40`.
- Git confirms `3f3ff843...` has direct parent `84fce305...` (verified via
  `git log --format="%H %P"`: `3f3ff84331cf370743d690b3e5c78693291a8a63`
  parent `84fce3059407284e5f3f08be662eb344d3c96b40`).

No technical content, review outcome, or authority is changed by this correction.
