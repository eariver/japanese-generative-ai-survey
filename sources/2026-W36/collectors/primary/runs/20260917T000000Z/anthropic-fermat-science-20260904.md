# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://www.anthropic.com/research/formalizing-fermats-last-theorem
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-04
- retrieval: webfetch markdown of Anthropic Formalizing Fermat's Last Theorem research article; stored verbatim as returned.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

Formalizing Fermat's Last Theorem \\ Anthropic

[Skip to main content](#main-content)[Skip to footer](#footer)

[

](/)

-   Research
-   [Policy](/policy)
-   Commitments
-   Learn
-   [News](/news)

[Try Claude](https://claude.ai/)

Science

# Formalizing Fermat's Last Theorem

Sep 4, 2026

*We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

*Around 1637, Pierre de Fermat jotted down a claim in the margin of his copy of Diophantus’s Arithmetica that would become one of the most famous mathematical conjectures of all time: no positive integers a, b, c satisfy aⁿ + bⁿ = cⁿ for any n > 2. [Fermat’s Last Theorem](https://www.youtube.com/watch?v=1BSFyEIY2BY) (FLT), as the conjecture became known, turned out to be incredibly difficult to prove. The first proof, from Sir Andrew Wiles in 1995, ran to 129 pages and required months of painstaking work to verify.

A decade later, Dutch computer scientist Jan Bergstra proposed “formalizing” Wiles’s proof: converting the mathematical reasoning into a form computers can check automatically. Since then, mathematicians have been developing the methods needed to encode such a complex proof, including a multi-year community effort kicked off in 2024 by Kevin Buzzard at Imperial College London [to complete the formalization](https://lean-lang.org/use-cases/flt/) using the [Lean proof assistant](https://en.wikipedia.org/wiki/Lean_\(proof_assistant\)).

Recently, Tianyi Peng, an Anthropic researcher whose group at Columbia University builds tools for AI formalization, set out to test whether Claude could make progress on formalizing FLT.[1](#footnote-1) The result went further than he expected. In 11 days, working largely autonomously, Claude produced the first end-to-end, computer-checked proof of FLT. Along the way, it wrote 13 million lines of Lean and proved 29,500 intermediate theorems.

We shared the [resulting proof](https://github.com/anthropics/fermats-last-theorem) with Kevin Buzzard, who said:

> This extraordinary autoformalization achievement, which Anthropic researchers say only took 11 days, proves Fermat’s Last Theorem with no assumptions other than the axioms of mathematics. Along the way we see autoformalization of algebra, harmonic analysis, geometry and number theory, and we learn that AI autoformalization artefacts are now robust enough to be built upon; the proof is multi-layered.

Automatically formalizing a proof as complex as FLT is a significant step towards a future in which all of mathematics can be readily checked. As AI produces ever more proofs, the ability to easily formalize work can lighten the burden of evaluating new results (a process that can take years).

## The challenge of verifying mathematical proofs

Unlike [recent AI-driven](https://www.anthropic.com/research/riemann-zeta) work on the Riemann hypothesis, which produced novel *mathematics*, what’s novel here is the *verification*—checking a mathematical proof as one would check a mathematical computation with a calculator. Proving math theorems requires assembling complex logical chains, and if a single link is broken, everything that follows it might turn out to be false.

Fermat wrote down the theorem’s statement in the margin of a book, alongside a tantalizing note:

> I have discovered a truly marvelous proof of this, which this margin is too narrow to contain.

In June 1993, Wiles presented what he believed to be the first correct proof of FLT in a three-day series of lectures. Two months into verification, a reviewer found a critical gap. Wiles spent a year trying to fix it, first alone and then with Richard Taylor. Wiles published the first correct proof of FLT in May 1995; it relied on modern mathematical techniques far beyond what Fermat knew in 1637.

## Formalizing Fermat’s Last Theorem

One way to check a proof’s correctness is to ask a computer to do it. Proof assistants like Lean verify the logic of a proof algorithmically. The difficult part for humans is rewriting the proof so Lean can understand it. While a proof written for human readers will skip many obvious steps, Lean needs to see every step, no matter how trivial.

For FLT, the formalization process was expected to take years. Just the [blueprint](https://imperialcollegelondon.github.io/FLT/blueprint.pdf) the mathematical community has been using runs to 86 pages.

Claude completed the proof in 11 days, producing computer-verifiable proofs of 30,300 theorems along the way (using 29,500 in the final proof). Dozens of Claude agents collaborated to define concepts, prove intermediate theorems, and use those theorems to prove ever harder statements. At 13 million lines of Lean code, Claude’s proof is over 5x the size of Mathlib, the principal community library of mathematical proofs this theorem builds on.[3](#footnote-3)

Claude’s proof follows [a simplified version of Wiles’s proof from Darmon, Diamond, and Taylor](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf). Mathematical input from humans was limited to occasional high-level instructions from Tianyi: “Jacobian as a scheme sounds high priority,” “push \[the\] Mazur \[theorem\] to be done soon.”

```
“THE FLT root reads Proved on the site. Historic moment (modulo re-check).”

“!!! The FLT ROOT 62eb32c0 reads PROVED. R = T closed and cascaded to the root. This is the campaign's goal: e2e FLT on prove2me.”

“🏁🏁🏁The FLT root reads PROVED on prove2me at 02:00:57Z Aug-18 (10:00:57pm ET Aug-17). Historic moment for this campaign.”
```

*Excerpts of Claude’s thinking as it realizes what it has just accomplished.*

A number of Claude’s initial attempts failed: while agents had some early success, they quickly lost track of the project’s state and stopped collaborating effectively. Their failed efforts contributed ~7% of the non-boilerplate lines in the final proof.

The effort succeeded when we switched to using [Prove2Me](https://prove2me.vercel.app/), an open collaborative platform for formalizing mathematics designed by Tianyi Peng and his collaborators at Columbia University. Prove2Me helped by:

1.  **Maintaining a directed acyclic graph (DAG) of theorem statements** that agents used to decide what proofs they should attempt next.
2.  **Speeding up Lean compilation and minimizing resource consumption** by separating theorem statements and proofs into different files.
3.  **Enabling search and reuse** by maintaining a natural-language description of each theorem statement, resulting in a simpler proof path.

With Prove2Me and a Claude Code-based multi-agent harness, a team of agents completed the proof in a little under two weeks, consuming about six billion output tokens from a general-purpose internal research model roughly comparable to Claude Fable 5.1. The finished proof was checked by Lean; it uses just Lean’s three standard axioms, and a [comparator](https://github.com/leanprover/comparator) confirmed that the theorem’s statement matches Mathlib’s own statement of FLT.

## Reducing the burden of formal verification

After reviewing Claude’s Lean proof, Kevin Buzzard told us:

> If the automatic formalization of FLT is possible now, then we have taken a big step towards automatic formalization of the modern mathematical literature. Such autoformalization techniques will lead to new tools, rooting out errors in the current mathematical corpus and lightening the load of referees.

Formalization is also a major factor in how humans can gain confidence in AI-generated mathematical results. As AI and AI-assisted mathematicians produce more (purported) proofs than ever before, AI-assisted formalization takes part of the load off human reviewers.

Writing Lean also seems to help Claude prove novel results. Many of our recent Claude-authored results have been formalized in parallel with their proofs, and Claude appears to use these partial proofs to independently check its hypotheses much like it writes numerical simulations to check that it’s on the right track.

The full proof is available on [GitHub](https://github.com/anthropics/fermats-last-theorem) along with a written walk-through of the proof.

[truncated for edition-local storage]
