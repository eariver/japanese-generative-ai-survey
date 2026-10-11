# SOURCE EXCERPT (bounded) — NVIDIA Nemotron Saudi-ASR tutorial (Sep 30, full body READ)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://developer.nvidia.com/blog/?p=122986 (Fine-Tuning NVIDIA Nemotron for Saudi Arabic Dialects)
- retrieved_at: 2026-10-10T04:39:30Z (Muse webfetch text; rendered markdown, NOT byte-identical HTML)
- access_mode: webfetch-read full body incl. tables/code; bounded excerpt archived; upgrades r1 LOCATOR_GRADE note
- redistribution: bounded quotation only

## Bounded quotes

> "Sep 30, 2026" / "By Imane Khaouja, Amine El Khair, Meshari Alaeena, Zahra Al-Kaf and Abdulrahman Alkhamees"
> "NVIDIA Nemotron 3.5 ASR supports multilingual streaming transcription across 40 language-locales"
> "These checks retained 103,559 of 125,490 utterances: 133.7 hours, or 82.5% of the starting set."
> "Test split Before After: SADA Najdi + Hijazi WER 55.05% -> 29.96%; CER 31.63% -> 12.18%; FLEURS English WER 11.04% -> 10.42%"
> "The model has 24 encoder layers." / "In the recorded top-eight recipe, 230.4 million parameters were trainable" / all-24 29.96% vs top-8 32.32% vs top-6 33.42%
> "over 12,000 steps and about 4.5 hours on two GPUs" (2x RTX PRO 6000 Blackwell Workstation Edition)
> "Switching to the highest-lookahead context reduced WER by 1.31 absolute points" / "MALSD beam-8 ... 27.25% (-2.71)" / "approximately 800 ms of additional latency"
> "NVIDIA Nemotron 3 Diarization, just released, extends this workflow ... for up to 8 speakers. It is an open model"
> "These are not universal defaults." / "this workflow doesn't generalize into evidence for every Arabic dialect or deployment environment."

## Boundaries

- Practitioner tutorial on SADA 2022 + FLEURS splits with NeMo defaults mostly untuned; publisher-measured, NOT external reproduction or universal performance. Notebook/skill/HF diarization blog linked but not consumed here.
