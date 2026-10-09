# Collector raw — OpenAI: Towards safety cases for frontier AI training (Sep 28)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://openai.com/index/towards-safety-cases-for-frontier-ai-training/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-28 (vendor page header)

## Consumed claims (claim-level)

1. EVENT: OpenAI published proposed evidence-based safety-case guidelines for frontier RL training runs. (PRIMARY_FACT: publication occurred, date)
2. POSTURE: Safety cases are "aspirational north star", not assertion every current run uses certified case; framework being codified; practices evolving. (PRIMARY_FACT as vendor posture; do not present as deployed guarantee)
3. TECHNICAL (guidance, not proof): alignment training (dataset reviews, grader tuning, prior-run analysis, alignment evals/backtesting/eval-gaming tracking/worst-case stress, no CoT to graders); containment (sandbox hardening, red-teaming with frontier checkpoints, cross-sample limits, immutable transcripts); monitoring (monitorability thresholds, held-out recall, fresh evals, SLA paging/auto-pause). (VENDOR_CLAIM as guidance content)
4. OPERATIONAL (guidance): dissents/pre-mortems, senior-leadership veto, accountability, pausing runbooks, internal transparency, audits, escalation/on-call to CEO, fail-closed technical controls, rollback lineage, residual-risk enumeration. (VENDOR_CLAIM)
5. INCIDENT (guidance): periodic internal updates, root-cause ablations, postmortems, regression evals without hillclimbing on incident, public disclosure + third-party notification. (VENDOR_CLAIM)

## Boundaries / unresolved

- Guidance document, not empirical safety demonstration; no incident-free or coverage claim can be derived.
- Applies to frontier RL training; deployment requires broader alignment properties per page.
