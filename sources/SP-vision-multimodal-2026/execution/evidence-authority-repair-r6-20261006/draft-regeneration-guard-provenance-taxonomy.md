# Draft-regeneration guard — provenance taxonomy (for the post-r6 fresh Draft run)

Do NOT rewrite Draft in this run. The next Draft regeneration (after Human
Architecture Review r6 approval) MUST distinguish at least:

1. author/developer self-reported measurement
   - academic/project paper authors evaluating their own model/system
   - examples: InternVL/Molmo author-measured comparisons, Whisper/BEATs/CLAP
     paper-reported numbers, benchmark-author measurements (MMMU/POPE/MMBench/
     Video-MME/LongVideoBench/StreamingBench author-measured scores)

2. vendor/provider-reported measurement
   - provider model card / product / commercial surface measurement
   - examples: Gemini model-card figures, Qwen vendor-measured claims,
     Agentic Video Understanding vendor ceilings

3. independent third-party measurement
   - reproduction or evaluation by parties other than authors/vendors

Do NOT call InternVL/Molmo/Whisper/BEATs author-measured results
`vendor-measured` merely because their developers measured them.

P15's existing provenance distinction (vendor vs independent) is preserved in
the Architecture design and must be made consistent across the regenerated Draft
under this three-way taxonomy. The over-broad template
`すべてのベンダー測定` / `すべてのベンチマーク主張はベンダー測定` must NOT be
carried into the regenerated Draft.
