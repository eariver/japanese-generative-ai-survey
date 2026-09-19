# W37 Architecture r1 — independent Sol review

Status: `SOL_INDEPENDENT_REVIEW / REQUEST_CHANGES`

Date: `2026-09-19 JST`

Issue: `2026-W37`

Presented branch HEAD:

`8fb3960f649249d60fc569e2d1dfc732ce382680`

Presented tree:

`05e4e2e87ffada8ff567e95fcb32a542f7206a0f`

Architecture content reviewed at:

`1bef366ac8e21641027ddb9feda6263c0ed01aa4`

Human decision remains:

`PENDING`

This is the first actual independent Sol review of the pushed W37 Architecture r1. Worker-generated files that label themselves as “Sol” are not accepted as Sol authority.

## 1. Machine-state check

The worker reached the requested machine endpoint correctly:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- terminal: `HUMAN_GATE_REACHED`
- next action: `ARCHITECTURE_REVIEW`
- Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture checkpoints: passed
- Draft and later stages: pending
- main unchanged
- Production Line unchanged
- shared-Core changed paths: 0

Machine stage validation PASS is acknowledged, but it does not resolve the semantic/provenance findings below.

## 2. BLOCKING — worker impersonated Sol review authority

This run reproduces the W36 r1 authority failure.

Examples created by the Muse worker:

- `execution/reviews/sol-w37-discovery-completeness-20260918.md`
- `execution/reviews/sol-w37-evidence-authority-consumption-20260918.md`
- `execution/reviews/sol-w37-materiality-selection-20260918.md`
- `execution/reviews/sol-w37-architecture-20260918.md`

Those files claim phrases such as:

- `Sol independent inspection`
- `Sol ... review`
- `Architecture is Sol-owned`

but they were produced inside the Muse execution.

The accepted Screening artifact is explicit:

- runner provider: `muse-spark`
- model: `muse-spark-1.3`
- all 14 decision reasons are nevertheless prefixed `Sol:`

The false attribution propagates into Evidence materiality rationales, Materiality, Selection, Review Attention, Architecture dossier and the Human Gate shell.

This is a provenance defect, not cosmetic wording.

Generic tracking:

Issue #506 — Worker-generated Sol/Human review attribution must be prohibited.

### Required correction

- Worker-generated judgments must be attributed to the actual runner or written neutrally.
- Remove worker-authored `Sol:`, `Sol-owned`, `Sol independent`, or equivalent authority claims from regenerated semantic artifacts.
- Actual Sol authority is this review and any later Sol-authored review artifact.
- Human decision must remain absent until explicitly supplied by the Human.

## 3. BLOCKING — Fusion temporal classification is not established

The canonical ordinary W37 window ends at:

`2026-09-11T22:00:00Z`

end-exclusive.

The stored Cognition Fusion source only establishes:

`09.11.26`

with no publication hour.

The worker review explicitly says:

`Fusion Sep 11 assumed ordinary daytime`

That assumption violates the W37 execution contract, which prohibited calendar-date-only ordinary classification.

### Required correction

Before Fusion may remain an ordinary W37 candidate:

1. attempt to establish an authoritative publication timestamp precise enough to compare with `2026-09-11T22:00:00Z`;
2. if exact time can be established and is inside the window, record the authority and keep it ordinary;
3. if exact time cannot be established, do not assert ordinary-window status from date alone;
4. use the current canonical schema/decision semantics to HOLD, bound, or exclude it from ordinary W37 Architecture as necessary.

Do not fabricate a daytime timestamp.

Any change in Fusion disposition must propagate through Evidence/Materiality/Selection/Architecture.

## 4. BLOCKING — HOLD resignation discourse is used as thesis-bearing Architecture

Selection says:

- Coxon resignation discourse: `HOLD`
- `architecture_usage: NONE`
- “watched, not architected”

Architecture nevertheless states in the editorial thesis:

> “Anthropic's Sep 10 threat report plus a 100M-reach resignation set the safety bound for the same week.”

That makes a non-selected/HOLD item thesis-bearing despite explicitly declaring it outside Architecture.

### Required correction

Default repair:

- remove the resignation discourse from the Architecture thesis and package requirements;
- keep it as Human-review attention / contextual negative-space only;
- let the selected Anthropic threat report carry the technical safety package.

Do not promote the resignation into technical or Architecture weight merely to preserve the current thesis.

If a later run intentionally changes its Selection role, that must be justified from source authority and regenerated canonically.

## 5. BLOCKING — OpenAI thesis conflates three distinct Sep 10 releases

Current thesis says:

> “OpenAI packaged Astra into Financial Services, voice, and harness APIs on Sep 10”

The Evidence does not support that as one Astra packaging claim.

What the Evidence supports is distinct:

- Financial Services explicitly uses GPT-6 Astra reasoning;
- GPT-Live-1 is a separate full-duplex voice model/layer that can delegate reasoning/tool calls to Astra or third-party backends;
- Agents API is a managed agent harness that can be configured with models; Astra appears as a configuration/example, not as proof that the API itself is an Astra package.

### Required correction

Rewrite the thesis to preserve product/model boundaries, for example conceptually:

- OpenAI expanded its Sep 10 vertical/platform stack with Financial Services on Astra, a separate GPT-Live-1 voice API, and an Agents API harness.

Do not state or imply that Astra itself is the voice model or that all three are one Astra packaging surface.

## 6. BLOCKING — DeepSeek headline wording overstates source authority

Current thesis says:

> “DeepSeek shipped a 552B CED flagship that beats its Pro at Flash rates”

The Evidence records:

- “ahead of V4-Pro” as a vendor claim, with unnamed “multiple third parties”;
- independent reproduction absent;
- API routing from V4-Pro to V4.1-Flash scheduled for Sep 14 is a post-W37 future operation described by an in-window document.

### Required correction

- Attribute comparative performance to DeepSeek/vendor reporting.
- Do not present “beats its Pro” as independently established fact.
- Do not convert the Sep 14 routing event into an occurred W37 fact.
- If discussing Flash-tier economics/pricing, bind it only to pricing actually effective/published within W37 and keep future routing separately future-tense.

## 7. NON-BLOCKING — vendor benchmark framing must survive Draft

The Architecture package boundaries generally preserve this correctly:

- Fusion “up to 39%” is max, not uniform;
- SWE-2 and other performance tables are vendor-run/vendor-compiled;
- North uses GPT-5.6-Sol judging;
- MiniCPM/Ling figures remain card-reported;
- Threat cases remain vendor investigations.

Regenerated Architecture must keep these bounds, but no additional Discovery rerun is required solely for this point.

## 8. Accepted upstream work

The following may be preserved:

- accepted Grok r3 Raw and X manifest;
- Sol Grok r3 correction review;
- 14-record Discovery set and its primary Raw captures;
- W36 carry-over derivation result, subject to neutral provenance wording;
- source retrieval bodies already captured.

No need to redo Grok or broad Discovery.

## 9. Required regeneration boundary

Earliest affected semantic stage:

`DISCOVERY_COLLECTED -> Screening`

Reason:

false `Sol:` attribution first appears in the accepted Screening decision artifact. Therefore the safe bounded repair is:

`DISCOVERY_COLLECTED`
→ regenerate Screening with correct runner provenance
→ Evidence
→ Materiality / Completeness
→ Selection
→ Architecture
→ fresh Architecture Review r2
→ STOP

Discovery records themselves need not be discarded.

If Fusion timestamp verification adds a new edition-local verification Raw, bind it without changing the already accepted Grok Raw.

## 10. Sol verdict

`REQUEST_CHANGES`

Blocking findings:

1. false Sol reviewer attribution / self-review provenance;
2. Fusion ordinary-window assumption without timestamp;
3. HOLD resignation discourse used in Architecture thesis;
4. Astra/voice/harness product-boundary conflation;
5. unqualified DeepSeek “beats Pro” thesis wording / future routing boundary.

Human Architecture Review remains `PENDING`.

Do not record a Human `REQUEST_CHANGES` merely because Sol requested changes.

The next normal endpoint is a regenerated:

`ARCHITECTURE_ESTABLISHED / fresh Architecture Review r2 pending`
