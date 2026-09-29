# Collector raw — Cursor: Rollouts + Security Review bots (Sep 23)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:40:00Z (webfetch excerpt of live page)
- source_url: https://cursor.com/blog/rollouts-and-security-reviewer
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-23; author Rustam Lalkaka

## Consumed claims

1. EVENT: Two Teams/Enterprise bots launched Sep 23: Rollouts (PR→production deploy monitoring, regression flagging, ping/pause/revert-PR actions; no autonomous merge/rollback today) and Security Reviewer (per-PR vuln reports with severity/attack-path/one-click fix; review time 4.8→3.8 min, acceptance 45–50%→60–70% per vendor chart). (PRIMARY_FACT as launch/availability; metrics VENDOR_CLAIM)
2. AVAILABILITY: Teams + Enterprise via automations tab; 10-day trial credits for Rollouts. (PRIMARY_FACT)
3. SCOPE: Rollouts needs source control + deploy + telemetry (Datadog/Grafana/Honeycomb); feature-flag integration + release-train awareness "coming soon" (not shipped). (PRIMARY_FACT)

## Boundaries

- Measured review-effect claims are vendor-reported; independent reproduction absent.
- Distinct from March open-source security-agent templates (different artifact).
