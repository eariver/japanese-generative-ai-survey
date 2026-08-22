#!/usr/bin/env python3
"""Execute the W33 Core v2 compiler with session-audited source-intake corrections.

The original one-shot compiler was committed before fresh primary-source reconciliation
found that Grok 4.6 was a real GitHub Copilot event and before the W33 intake was
expanded with Ultrafast, Gemini 3.7 Flash, and MAI-Code-1.1-Flash.  This wrapper
applies exact fail-closed source transformations in memory, then executes the corrected
compiler.  The source file on disk is not mutated.
"""
from __future__ import annotations

from pathlib import Path

SOURCE = Path("automation/w33_v2_compile_once.py")
text = SOURCE.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source match, found {count}")
    text = text.replace(old, new, 1)


# Expand current-window primary intake before raw collection.
marker = "\n    }\n\n    raw_by_id: dict[str, Path] = {}"
addition = r'''
        'w33-ultrafast': {
            'title': 'OpenAI GPT-5.6 Sol Ultrafast mode',
            'url': 'https://openai.com/index/previewing-ultrafast/',
            'published_at': '2026-08-13T00:00:00Z',
            'note': 'OpenAI first-party Aug 13 limited API preview; speed figures remain OpenAI claims and the service is not general availability.',
            'canonical_name': 'OpenAI GPT-5.6 Sol Ultrafast mode', 'entity_type': 'API', 'artifact_type': 'API', 'organization': 'OpenAI',
            'event_type': 'limited-preview', 'source_title': 'Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed',
            'claims': [
                ('OpenAI introduced Ultrafast as a new GPT-5.6 Sol service tier in a limited OpenAI API preview during W33, powered by Cerebras.', 'PRIMARY_FACT', 'First-party product and availability chronology.'),
                ('OpenAI reports that Ultrafast can run GPT-5.6 Sol up to 14 times faster than Standard processing and generate up to 750 output tokens per second.', 'VENDOR_CLAIM', 'Speed figures are OpenAI-reported, not independently reproduced.'),
            ],
            'limitations': [
                ('Ultrafast was a limited preview for selected customers, not general availability.', 'PRIMARY_FACT', 'Availability boundary must travel with the speed claim.'),
                ('The up-to-14x and up-to-750-output-token/s figures are vendor-reported and should not be generalized to every workload.', 'VENDOR_CLAIM', 'No independent matched-workload reproduction in this issue.'),
            ],
            'verification_finding': 'OpenAI first-party material establishes the Aug 13 limited-preview event, Cerebras deployment, and explicitly attributed speed claims.',
            'materiality': 'MATERIAL', 'why': 'It adds a first-party serving-service event to the same week in which open serving runtimes and kernels were also moving, strengthening the systems-level story.',
            'dimensions': ['current relevance', 'technical significance'],
        },
        'w33-grok46-copilot': {
            'title': 'Grok 4.6 in GitHub Copilot',
            'url': 'https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/',
            'published_at': '2026-08-14',
            'note': 'Fresh v2 reconciliation corrected the legacy/X rejection: GitHub published a first-party Grok 4.6 Copilot rollout on Aug 14. Exact publication time relative to the 18:00 EDT cutoff remains unresolved.',
            'canonical_name': 'Grok 4.6 in GitHub Copilot', 'entity_type': 'MODEL', 'artifact_type': 'INTEGRATION', 'organization': 'GitHub / xAI',
            'event_type': 'rollout', 'source_title': 'Grok 4.6 is now available in GitHub Copilot',
            'status': 'PARTIAL', 'verification_status': 'UNRESOLVED',
            'claims': [
                ('GitHub announced a gradual Grok 4.6 rollout across multiple GitHub Copilot surfaces on August 14, 2026.', 'PRIMARY_FACT', 'First-party GitHub integration event.'),
                ('GitHub describes Grok 4.6 as suited to agentic coding and complex multi-step workflows based on its internal testing.', 'VENDOR_CLAIM', 'Capability assessment is GitHub-reported.'),
            ],
            'limitations': [
                ('The GitHub page exposes the publication date but not a verified publication time, so this cutoff-day event cannot be safely classified as before or after the W33 18:00 EDT cutoff.', 'PRIMARY_FACT', 'Timing uncertainty is the reason for HOLD/INSPECT, not lack of first-party identity.'),
                ('GitHub internal-testing claims are not independent benchmark evidence.', 'VENDOR_CLAIM', 'Keep capability wording attributed.'),
            ],
            'unresolved_questions': ['Was the GitHub changelog item published before or after the 2026-08-14 18:00 EDT W33 cutoff?'],
            'verification_finding': 'First-party identity and rollout are established, correcting the earlier X-only rejection; exact cutoff relation remains unresolved.',
            'materiality': 'HOLD', 'why': 'The event is real and potentially relevant, but cutoff-day timing cannot be resolved safely from the available primary metadata.',
            'dimensions': ['current relevance'],
        },
        'w33-gemini37flash-copilot': {
            'title': 'Gemini 3.7 Flash in GitHub Copilot',
            'url': 'https://github.blog/changelog/2026-08-13-gemini-3-7-flash-is-now-available-in-github-copilot/',
            'published_at': '2026-08-13T00:00:00Z',
            'note': 'GitHub first-party Aug 13 rollout. Retain as explicit model-catalog context rather than silently omitting it.',
            'canonical_name': 'Gemini 3.7 Flash in GitHub Copilot', 'entity_type': 'MODEL', 'artifact_type': 'INTEGRATION', 'organization': 'GitHub / Google',
            'event_type': 'rollout', 'source_title': 'Gemini 3.7 Flash is now available in GitHub Copilot',
            'claims': [
                ('GitHub began rolling out Gemini 3.7 Flash across multiple GitHub Copilot surfaces during W33.', 'PRIMARY_FACT', 'First-party GitHub integration chronology.'),
                ('GitHub reports improvements in web/app development, agentic coding, code quality, codebase research, and verification in its early testing.', 'VENDOR_CLAIM', 'Platform-reported capability assessment.'),
            ],
            'limitations': [('GitHub early-testing claims are not independent model evaluation, and a Copilot catalog rollout is less structurally significant than the issue lead/system changes.', 'VENDOR_CLAIM', 'Retain as context/HOLD unless architecture needs model-routing breadth.')],
            'verification_finding': 'GitHub first-party material establishes the Aug 13 rollout and attributed platform claims.',
            'materiality': 'CONTEXT', 'why': 'A real W33 model-routing/catalog event, but redundant as a standalone feature given stronger system and agent-infrastructure developments.',
            'dimensions': ['current relevance'],
        },
        'w33-maicode11flash-copilot': {
            'title': 'MAI-Code-1.1-Flash in GitHub Copilot',
            'url': 'https://github.blog/changelog/2026-08-11-mai-code-1-1-flash-available-in-github-copilot/',
            'published_at': '2026-08-11T00:00:00Z',
            'note': 'GitHub first-party Aug 11 rollout; native vision and price/performance claims remain platform/vendor claims.',
            'canonical_name': 'MAI-Code-1.1-Flash in GitHub Copilot', 'entity_type': 'MODEL', 'artifact_type': 'INTEGRATION', 'organization': 'GitHub / Microsoft',
            'event_type': 'rollout', 'source_title': 'MAI-Code-1.1-Flash available in GitHub Copilot',
            'claims': [
                ('GitHub began rolling out Microsoft MAI-Code-1.1-Flash in Copilot during W33 and describes native image understanding as a model capability.', 'PRIMARY_FACT', 'First-party GitHub product/integration chronology.'),
                ('GitHub reports coding, instruction-following, tool-use and performance improvements and a 73 percent lower list price than MAI-Code-1-Flash.', 'VENDOR_CLAIM', 'Platform/vendor-reported comparative claims.'),
            ],
            'limitations': [('Capability and 73-percent price comparison statements are GitHub/Microsoft claims rather than independent matched evaluation.', 'VENDOR_CLAIM', 'Do not turn into an unqualified leaderboard or cost-performance conclusion.')],
            'verification_finding': 'GitHub first-party material establishes the Aug 11 rollout and attributed capability/price claims.',
            'materiality': 'CONTEXT', 'why': 'Useful evidence that coding-model routing and efficiency tiers were changing in W33, but not strong enough for a standalone feature in the proposed architecture.',
            'dimensions': ['current relevance', 'technical significance'],
        },
'''
replace_once(marker, "\n" + addition + "    }\n\n    raw_by_id: dict[str, Path] = {}", "primary_specs expansion")

# Grok 4.6 is no longer an X-only rejected identity after first-party reconciliation.
replace_once(
    "    x_ids = ['x-grok46-unverified', 'x-qwen38-unverified', 'x-anthropic-risk-report-unverified']",
    "    x_ids = ['x-qwen38-unverified', 'x-anthropic-risk-report-unverified']",
    "x discovery ids",
)
replace_once(
    "        ('x-grok46-unverified', 'Grok 4.6 social claim', 'Exact first-party Grok 4.6 W33 identity/launch was not corroborated; social salience cannot establish the event.'),\n",
    "",
    "remove stale Grok rejection",
)

# Keep completeness rationale true after intake expansion.
replace_once(
    "'rationale': 'Eight date-specific primary-source developments were verified and assigned explicit edition-level materiality; X-only false positives were explicitly dropped.'",
    "'rationale': 'Date-specific primary-source developments were verified and assigned explicit edition-level materiality; cutoff uncertainty and X-only false positives receive explicit downstream dispositions rather than silent omission.'",
    "completeness current-relevance rationale",
)

# Every newly evidenced Matrix row must receive exactly one internal Selection assignment.
selection_anchor = "        'ComfyUI W33 media integrations': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:WATCHLIST', 'WEEKLY:WATCHLIST'),\n        'W32→W33 carry-over disposition ledger': ('HOLD', 'NONE', None, None),"
selection_new = "        'ComfyUI W33 media integrations': ('SELECTED', 'PRIMARY', 'WEEKLY_MAGAZINE:WATCHLIST', 'WEEKLY:WATCHLIST'),\n        'OpenAI GPT-5.6 Sol Ultrafast mode': ('SELECTED', 'SUPPORTING', 'WEEKLY_MAGAZINE:SYSTEMS_SUPPORT', 'WEEKLY:SERVING_STACK_SUPPORT'),\n        'Grok 4.6 in GitHub Copilot': ('INSPECT', 'NONE', None, None),\n        'Gemini 3.7 Flash in GitHub Copilot': ('HOLD', 'NONE', None, None),\n        'MAI-Code-1.1-Flash in GitHub Copilot': ('HOLD', 'NONE', None, None),\n        'W32→W33 carry-over disposition ledger': ('HOLD', 'NONE', None, None),"
replace_once(selection_anchor, selection_new, "selection expansion")

old_rationale = """        if disp == 'SELECTED':
            rationale = 'Selected because validated edition materiality is MATERIAL/CONTEXT and the candidate has a defined non-duplicative Architecture destination.'
        else:
            rationale = 'Held as audit/completeness provenance: it closes carry-over obligations but is NON_MATERIAL as a W33 technical story.'
"""
new_rationale = """        if disp == 'SELECTED':
            rationale = 'Selected because validated edition materiality is MATERIAL/CONTEXT and the candidate has a defined non-duplicative Architecture destination.'
        elif row['title'] == 'Grok 4.6 in GitHub Copilot':
            rationale = 'INSPECT: first-party rollout identity is now verified, correcting the earlier X-only rejection, but the Aug 14 page lacks an exact publication time relative to the 18:00 EDT cutoff.'
        elif row['title'] in {'Gemini 3.7 Flash in GitHub Copilot', 'MAI-Code-1.1-Flash in GitHub Copilot'}:
            rationale = 'HOLD: verified W33 Copilot model-catalog event retained for explicit coverage accounting, but redundant as standalone architecture material beside stronger systems and agent-infrastructure changes.'
        else:
            rationale = 'HOLD: audit/completeness provenance closes carry-over obligations but is NON_MATERIAL as a W33 technical story.'
"""
replace_once(old_rationale, new_rationale, "selection rationales")

# Ultrafast is supporting evidence in the serving-stack package, not a separate release-note article.
old_serving = """         [row('SGLang v0.5.17'), row('vLLM v0.27.0–v0.27.1'), row('FlashInfer v0.6.17')], [],
         ['Compare layers and responsibilities, not incomparable project benchmark numbers.', 'Make project-reported performance/resource claims explicitly attributed.', 'Show why simultaneous runtime/kernel adaptation matters for new model architectures.']),
"""
new_serving = """         [row('SGLang v0.5.17'), row('vLLM v0.27.0–v0.27.1'), row('FlashInfer v0.6.17')], [row('OpenAI GPT-5.6 Sol Ultrafast mode')],
         ['Compare layers and responsibilities, not incomparable project benchmark numbers.', 'Make project/vendor-reported performance/resource claims explicitly attributed.', 'Use Ultrafast as a first-party service-tier counterpoint while retaining its limited-preview and vendor-speed boundaries.', 'Show why simultaneous runtime/kernel/service-tier adaptation matters for new model architectures.']),
"""
replace_once(old_serving, new_serving, "serving package expansion")

# Correct reviewer-facing narrative and semantic audit counts.
replace_once(
    "- **Grok 4.6 / Qwen3.8-27B / alleged Anthropic Aug-14 Risk Report**: preserved in review attention as X-derived false positives rejected after primary-source reconciliation.",
    "- **Grok 4.6**: fresh first-party GitHub reconciliation corrected the earlier rejection; retained for Architecture Review inspection because its Aug-14 publication time relative to the 18:00 EDT cutoff is unresolved.\n- **Qwen3.8-27B / alleged Anthropic Aug-14 Risk Report**: preserved in review attention as X-derived false positives rejected after primary-source reconciliation.\n- **Gemini 3.7 Flash / MAI-Code-1.1-Flash in Copilot**: verified current-window catalog events retained as HOLD so omission from the proposed article flow is explicit rather than silent.\n- **OpenAI Ultrafast**: selected as supporting serving-stack evidence, with limited-preview and vendor-speed boundaries preserved.",
    "editorial note reconciliation",
)
replace_once(
    "'Discovery contains eight current first-party technical events, one explicit carry-over ledger, and three X-only claims retained for rejection; X manifest is complete and all raw paths are hash-bound.'",
    "'Discovery contains a broadened current-window primary-source corpus, one explicit carry-over ledger, and two representative X-only claims retained for rejection; Grok 4.6 is corrected to first-party cutoff-day inspection. X manifest is complete and all raw paths are hash-bound.'",
    "discovery review evidence",
)
replace_once(
    "'Every Discovery record has exactly one profile-neutral disposition. The three X false positives are DROP with primary-source reconciliation reasons; all current-window/carry-over records proceed to Evidence without Weekly why-now fields in Screening.'",
    "'Every Discovery record has exactly one profile-neutral disposition. Two X-only false positives are DROP with primary-source reconciliation reasons; verified current-window/carry-over records proceed to Evidence without Weekly why-now fields in Screening, including a cutoff-day Grok 4.6 record retained for later inspection.'",
    "screening review evidence",
)

# Execute transformed source as the canonical session compiler input.
code = compile(text, "automation/w33_v2_compile_current.py::<transformed-w33-compiler>", "exec")
namespace = {"__name__": "__main__", "__file__": str(SOURCE)}
exec(code, namespace, namespace)
