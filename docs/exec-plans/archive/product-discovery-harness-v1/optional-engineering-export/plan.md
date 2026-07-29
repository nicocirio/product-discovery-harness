# Optional Engineering Export - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Move canonical product ownership out of exec-plans while retaining a safe optional export.

## Clarifications & Default Assumptions
- Existing non-generated engineering files are never overwritten, renamed, or deleted.

## Phase 1: Canonical Product Contract
- Goal: write full product specs without Engineering Harness paths.
- Tasks:
  - [x] Split rendering and return a handoff report.
  - [x] Make bootstrap/validation product-only by default.
- Testing Tasks:
  - [x] Test product-only target output.
  - Command(s): `.venv/bin/python -m pytest tests/test_handoff.py`
- Definition of Done:
  - AC-001 canonical spec works without exec-plans.
- Gate:
  - Product validation passes after removal of exec-plans.
- Dependencies:
  - Existing readiness validation.
- Parallelizable Work:
  - Navigation docs and config changes.

## Phase 2: Compatibility Export and Migration
- Goal: add opt-in public export with ownership protection.
- Tasks:
  - [x] Add explicit export mode/config and guarded writer.
  - [x] Add docs/README and handoff/validation skill changes.
- Testing Tasks:
  - [x] Test generated export and unowned conflict.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-002/AC-003 pass and old exports remain untouched.
- Gate:
  - All validators and review pass.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - English/Spanish documentation.

## Parallelization Notes
- Documentation may proceed after ownership boundaries are settled.

## Phase Gate Summary
- Gate A: canonical product-only handoff.
- Gate B: safe optional compatibility export.
