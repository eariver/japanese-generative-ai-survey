# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://openai.com/index/astra-for-law/
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured, curl blocked)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date_on_page: September 17, 2026
- authority_class: PRIMARY_OFFICIAL (OpenAI first-party announcement)

# Introducing Astra for Law (excerpt)

Today, we're introducing Astra for Law: a new foundation for law firms and legal technology companies to build AI products and workflows around their expertise. It combines GPT-6 Astra, our latest and most powerful model, with settings, tools, and context tailored for professional legal work.

API customers including Harvey and Legora will be able to build on Astra for Law. As our frontier models advance, we'll bring these legal capabilities to our latest models.

We are also expanding our work on privacy and governance to give law firms specific controls for confidential client work. Firms can also customize Astra for Law using our 26 new ecosystem plugins that connect ChatGPT to specialist tools firms already use, like Relativity and Clio.

## Legal research: from facts to a supported answer

Our new legal search index is one of the tools Astra for Law can use. By using the legal search index, Astra for Law can search U.S. case law, statutes, regulations, court rules, and administrative decisions across a corpus of more than 230 million URLs, with sources added daily. Our work with Free Law Project, the nonprofit behind CourtListener, brings its case-law collection covering more than 99.9% of published U.S. precedential case law into this research experience.

Benchmark: Vals AI's Legal Research Bench private validation set (200 U.S. legal research questions). At the highest reasoning effort for both systems, Astra for Law passed overall correctness on 54.0% of questions vs 38.7% for GPT-6 Astra with web search alone (40% relative improvement). On case-law-focused questions, 24% more reference cases; up to 54% more relevant passages from correct court opinions at same reasoning effort.

## End-to-end legal workflows

Custom instructions for legal analysis and writing guide Astra for Law in applying research to client facts. Astra for Law will be initially offered to selected law firms through Trusted Access in ChatGPT and Codex, and coming soon to the API. Model picker: "GPT-6 Astra Law"; API: gpt-6-astra-law.

Early testers: Sullivan & Cromwell (agreement analyzer), Ropes & Gray (deal diligence), Cooley (GO Public capital-markets tool), Skadden (regulatory risk suite).

## Legal-grade trust and controls

Trusted Access Program for eligible law firms: Zero Data Retention (ZDR) on API; ChatGPT Enterprise usage excluded from human review by default. Collaboration with Latham & Watkins on information permissions, ethical walls, client instructions, firm oversight.

## Ecosystem

26 partner-built plugins (iManage, Intapp, DeepJudge, Thomson Reuters HighQ/CoCounsel Legal connector preview); 9 community plugins (LegalQuants, LECG, Skills.law) with 47 custom skills. ChatGPT for Word generally available. Forward-deployed work with Wachtell, Lipton, Rosen & Katz.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: existence/launch date (Sep 17 2026) of Astra for Law; GPT-6 Astra as base model; 230M+ URL legal index; Free Law Project/CourtListener coverage claim (vendor-stated); Vals bench numbers (vendor-reported, methodology stated, private set not independently reproduced); Trusted Access + ZDR offering; plugin counts (26 partner / 9 community / 47 skills); named firm collaborations (first-party testimonials).
- NOT verified here: benchmark reproducibility; "most powerful model" superlative; privilege/discoverability risk for public legal AI (raised by X independent post @pjdisney — retained as counter-signal context, not technical fact).
