# README Learning Guide - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Create a coherent English-first learning README and equivalent Spanish guide.

## Clarifications & Default Assumptions
- Illustrative outputs are labeled and never imply automatic acceptance or paths that do not exist.

## Phase 1: English Learning Guide
- Goal: explain the mental model, workflows, skills, outputs, ownership, and integration.
- Tasks:
  - [x] Draft concise narrative, diagrams, examples, and skill catalog.
  - [x] Verify every invocation and link.
- Testing Tasks:
  - [x] Run local link/catalog checks.
  - Command(s): `python3 -m product_discovery_harness.cli --help`
- Definition of Done:
  - AC-001/AC-002 guide a reader through implemented behavior.
- Gate:
  - No false CLI/skill claims.
- Dependencies:
  - Current skills and modules.
- Parallelizable Work:
  - Spanish translation outline.

## Phase 2: Spanish Counterpart and Verification
- Goal: preserve equivalent operational guidance in Spanish.
- Tasks:
  - [x] Translate all material workflow/safety/catalog content.
  - [x] Add documentation tests and evidence.
- Testing Tasks:
  - [x] Run full tests and validators.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-003 and all gates pass.
- Gate:
  - README references resolve and documentation is consistent.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - Link validation.

## Parallelization Notes
- Translation follows the established English structure.

## Phase Gate Summary
- Gate A: accurate English learning path.
- Gate B: complete Spanish counterpart and validated docs.
