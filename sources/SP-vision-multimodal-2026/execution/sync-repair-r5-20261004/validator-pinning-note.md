# Validator-pinning note (Core-controlled constraint on P09 scoping)

Fact (verified read-only): the string
`Weight/code licenses remain unresolved in canonical Evidence.`
is VM-D075's card limitation text (VERIFIED card, Qwen3-Omni repository) and therefore
a matrix `remaining_boundaries` entry. `validate_architecture` requires every matrix
remaining_boundary to be present VERBATIM in the placing package's boundaries.

Consequence: the string CANNOT be replaced or removed while VM-D075's card is unchanged
(card change is out of scope: no Evidence change this run). §2 scoping is therefore
implemented as an ADDED candidate-scoped companion line; the exact matrix-pinned string
is retained SOLELY as byte-exact authority propagation (Core validator requirement),
with its package-wide misreading neutralized by the explicit scoped companion.
Reported transparently as a known residual (see execution report + worker QA).
