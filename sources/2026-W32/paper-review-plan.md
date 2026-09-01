# 2026-W32 Paper Review Plan

Status: pre-editorial review planning  
Purpose: decide how deeply each abstract-screened paper must be reviewed before it can influence the issue structure or article text.

The six paper candidates are not treated as equivalent. Abstract screening is enough to keep them in the inventory, but quantitative claims are not publication-ready until the review level below is completed.

## Review levels

- `FULL`: inspect the full paper, methodology, experimental setup, assumptions, baselines, ablations, limitations, and result tables/figures relevant to the intended claim.
- `TARGETED_FULL`: inspect the full paper with emphasis on dataset/sample construction, taxonomy, methodology, and the specific result sections likely to be cited; exhaustive derivation review is unnecessary.
- `ABSTRACT_ONLY_OK_FOR_INDEX`: abstract-level metadata can remain in an index/watchlist, but no quantitative technical conclusion should be promoted.

## Plan

| Candidate | Primary source | Review level | Why this depth is needed | Minimum review questions |
|---|---|---|---|---|
| `paper-livemem` | https://arxiv.org/abs/2608.02515 | `FULL` | The value is in a new memory/state-continuity mechanism and its empirical behavior after active-context turnover. The abstract-level claim cannot establish how the memory state is trained, maintained, served, or compared fairly. | What changes to the pretrained model are required? How is memory state updated and bounded? What are the LongMemEval baselines? What context budgets are matched? What serving/runtime cost does continuity add? What failure modes and ablations are reported? |
| `paper-llm-serving-in-the-wild` | https://arxiv.org/abs/2608.03036 | `TARGETED_FULL` | This is an empirical adoption study rather than a new serving algorithm. The important risk is sampling/taxonomy validity rather than mathematical derivation. | How were repositories discovered and filtered? How is framework adoption detected? How are serving-method categories coded? What is the sample size and time snapshot? How are popularity and adoption distinguished? What threats to validity do the authors acknowledge? |
| `paper-when-does-disaggregation-pay` | https://arxiv.org/abs/2608.03741 | `FULL` | The headline throughput gains are simulation-dependent. Hardware models, workload assumptions, quantization, topology, and scheduling choices are central to whether the result generalizes. | What is HeteroPanacea validated against? Which GPUs/NPUs/interconnects are modeled? What workload distributions represent agentic inference? What assumptions enable the reported up-to-75% gain? Which conclusions hold only for hypothetical custom NPUs? What sensitivity/ablation results are shown? |
| `paper-sparseety` | https://arxiv.org/abs/2608.02995 | `FULL` | This is a security attack paper. Safe reporting requires separating demonstrated attack conditions from broader implications and understanding the TDX/side-channel threat model. | What attacker privileges are assumed? Which serving optimization leaks accesses? How is the activation oracle constructed? Which models/datasets are tested? What does BLEU >0.95 mean for exact token recovery? What monitoring overhead and detectability tradeoffs exist? Which mitigations are evaluated? |
| `paper-prweaver` | https://arxiv.org/abs/2608.02693 | `FULL` | The main result depends on how malicious PR sequences are constructed, rendered, interleaved, and reviewed. Benchmark validity and auditor setup must be checked before citing detection drops. | How are 208 attacks created and execution-validated? What are the ten repositories? What are the three auditing agents / six systems? What does N=16/N=24 mean operationally? How are carrier fusion and whole-window review generated? Are there contamination or realism limitations? |
| `paper-from-social-coding-to-agentic-coding` | https://arxiv.org/abs/2608.03585 | `FULL` | The numerical productivity and social-knowledge conclusions come from an LLM-based multi-agent simulation, not a direct field experiment. Simulation validity is therefore the central editorial caveat. | How are 1,084 developers and relationships initialized? How are agent decisions calibrated to historical data? What differs between No-CA and CA branches? How is adoption modeled? What is the standardized retrieval benchmark? How sensitive are the productivity/interaction results to simulator/model assumptions? |

## Initial editorial significance before full review

This is **not a final article ranking**; it only determines review effort.

### High leverage for the issue if validated
- `paper-livemem`: potentially gives a distinct Memory topic rather than another generic context-window story.
- `paper-sparseety`: bridges serving optimization and confidentiality/security, providing a technically different safety story.
- `paper-prweaver`: directly relevant to AI code-review / coding-agent trust boundaries.
- `paper-when-does-disaggregation-pay`: can support the systems-level theme around agentic inference and heterogeneous/disaggregated serving.

### Useful but likely secondary unless the full paper reveals stronger findings
- `paper-llm-serving-in-the-wild`: valuable empirical context for the serving ecosystem; likely better as a synthesis/reference anchor than a standalone lead.
- `paper-from-social-coding-to-agentic-coding`: potentially interesting for community/governance discussion, but conclusions must be framed explicitly as simulation results.

## Review order

To minimize unnecessary work before issue architecture:

1. `paper-livemem`
2. `paper-sparseety`
3. `paper-prweaver`
4. `paper-when-does-disaggregation-pay`
5. `paper-llm-serving-in-the-wild`
6. `paper-from-social-coding-to-agentic-coding`

The order is chosen to maximize topical distinctness first, not because it is a final importance ranking.

## Publication gate

Until the assigned review is complete:

- abstract metrics remain `AUTHOR_REPORTED_ABSTRACT_CLAIM`;
- no headline number should be written as independently established fact;
- comparisons to other systems must preserve the paper's exact setup and baseline definitions;
- limitations and simulation/threat-model assumptions must travel with any quantitative claim.
