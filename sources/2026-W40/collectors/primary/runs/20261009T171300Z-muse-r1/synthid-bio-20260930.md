# Collector raw — DeepMind: SynthID Bio (Sep 30; X Oct 1 is momentum)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://deepmind.google/blog/introducing-synthid-bio/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-30 (DeepMind blog header; Nature paper same date; X thread 2026-10-01T11:43:33Z is circulation, NOT first publication)

## Consumed claims (claim-level)

1. EVENT: DeepMind introduced SynthID Bio Sep 30, 2026: family of watermarking methods for synthetic biology (protein sequences + predicted 3D structures), extending SynthID to bio. (PRIMARY_FACT: introduction, date)
2. METHOD: Sequence = amino-acid choice guidance (ProteinMPNN + SynthID-text tournament sampling + AF3/wm-detectability filtering); structure = fine-tuned small part of AlphaFold 3 diffusion network, watermark in weights. Imperceptible signature verifiable on synthesized physical protein. (PRIMARY_FACT as vendor method description; full protocol in Nature paper)
3. RESULTS (vendor-reported lab tests): Watermarked binders (AlphaProteo + SynthID-enabled ProteinMPNN) matched hit rate, binding affinity (KD), natural diversity of unwatermarked across 3 targets (VEGF-A, SARS-CoV-2 RBD, PD-L1); first watermarked functional binders claimed; structure preserves AF3 accuracy with near-perfect detectability, robust to noise/minor coordinate changes. (VENDOR_CLAIM: lab results, not general biological neutrality)
4. PAPER: Nature "Function-preserving watermarking of AI-generated proteins" published Sep 30, 2026 (open access); Evo 2 bacteriophage genome watermarking with Hie lab/Arc noted as ongoing, early bacterial-culture function confirmed. Code + in vitro data + weights released per blog. (PRIMARY_FACT as publication record)
5. PURPOSE (vendor framing): Biosecurity/DNA-synthesis screening signal + database integrity (PDB/UniProt/GenBank); Swiss-cheese layer, not silver bullet; tamper-robustness is future work. Carter/Twist quotes are vendor-published. (VENDOR_CLAIM)

## Boundaries / unresolved

- "Without affecting biological function" is bounded to tested binders/targets; do not generalize to all proteins/genomes.
- Grok dates event Oct 1; correct to Sep 30 first publication per blog+N Janet; Oct 1 is X momentum.
- Wet-lab reproduction by third parties is not in this raw.
