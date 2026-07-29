# Product Landscape - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Implement a derived landscape command and index/path/date contract without an
Engineering Harness dependency.

## Clarifications & Default Assumptions
- “Old” means no meaningful review for 30 days; it is a prompt, never a decision.

## Phase 1: Contract and Renderer
- Goal: normalize index records and render safe Markdown.
- Tasks:
  - [x] Add metadata helpers and path/date validation.
  - [x] Add renderer, CLI command, template, and documentation.
- Testing Tasks:
  - [x] Add complete, missing, and stale record tests.
  - Command(s): `.venv/bin/python -m pytest tests/test_landscape.py`
- Definition of Done:
  - AC-001 and AC-002 provide correct links, markers, statuses, and ages.
- Gate:
  - Target validation remains backwards-compatible.
- Dependencies:
  - Existing index contract.
- Parallelizable Work:
  - Skill wording and fixture preparation.

## Phase 2: Workflow Integration and Safety
- Goal: connect skills and prove stale records are non-destructive.
- Tasks:
  - [x] Add `$product-landscape` and update resume/review/validate guidance.
  - [x] Add stale and preservation tests.
- Testing Tasks:
  - [x] Run full repository and work-item validation.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-003 is proven and output is derived.
- Gate:
  - Full tests, validators, and review pass.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - README language edits.

## Parallelization Notes
- Renderer and documentation proceed independently after metadata is agreed.

## Phase Gate Summary
- Gate A: real paths and deterministic rendering.
- Gate B: no lifecycle mutation and complete workflow guidance.
