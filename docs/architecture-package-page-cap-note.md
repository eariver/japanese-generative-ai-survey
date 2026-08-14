# Architecture package page-cap validator alignment

The Issue Architecture JSON schema already limits each package `page_target` to 8 pages. The Python Architecture validator now enforces the same limit so a workflow cannot report success for a plan that the schema would reject.

This was discovered while preparing SP-2024-H2 Architecture Review. The editorial plan itself is repaired separately on its canonical Special work branch; this note records only the reusable contract alignment.
