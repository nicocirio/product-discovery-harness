# README Learning Guide - Execution Record

## Delivered
- Rewrote `README.md` as the English-first learning guide for the product
  discovery harness.
- Added `README.es.md` as the aligned Spanish guide.
- Explained durable product truth, conversational skills, local CLI commands,
  ownership boundaries, and the optional Simon Initiative Engineering Harness
  handoff.
- Added Mermaid workflow and ownership diagrams, realistic command/output
  examples, and an indexed catalog of all 19 installed product skills.
- Added regression tests that keep both README catalogs, command examples,
  Simon link, and Mermaid guidance aligned with the repository.

## Decisions
- The English README is the primary entry point; Spanish is a full operational
  counterpart rather than an abbreviated translation.
- The guide treats skill invocations as conversational agent prompts and
  `product-harness` as the local deterministic CLI, avoiding a false claim that
  every skill is a shell command.
- Engineering integration remains optional and export is explicitly described
  as a narrow, marked boundary.

## Evidence
- `tests/test_readme.py` exercises AC-001, AC-002, and AC-003.
- Product CLI validation, repository tests, the Harness contract check, and
  work-item traceability checks passed on 2026-07-29.
