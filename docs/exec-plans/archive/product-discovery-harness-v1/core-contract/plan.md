# Core Contract - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Implement the package foundation, target templates/schemas, safe bootstrap, detection, IDs, and validation.

## Clarifications & Default Assumptions
- The package uses `src/` layout and Python 3.10+; accepted target records carry explicit human metadata.

## Phase 1: Package and Contract Assets
- Goal: establish the importable package, package metadata, templates, and schemas.
- Tasks:
  - [x] Create package modules and public CLI skeleton.
  - [x] Add all target templates and schemas.
- Testing Tasks:
  - [x] Verify package data resolution.
  - Command(s): `pytest tests/test_seeding.py`
- Definition of Done:
  - AC-001 fixture mode detection can be invoked through the package.
- Gate:
  - Package imports and asset paths resolve.
- Dependencies:
  - None.
- Parallelizable Work:
  - Template and schema authoring.

## Phase 2: Safe Target Operations
- Goal: implement detection, seeding, registry IDs, and validation.
- Tasks:
  - [x] Implement preservation markers and atomic writes.
  - [x] Implement schema, reference, lifecycle, and readiness checks.
- Testing Tasks:
  - [x] Add idempotence and invalid-record coverage.
  - Command(s): `pytest tests/test_detection.py tests/test_seeding.py tests/test_ids.py tests/test_validation.py`
- Definition of Done:
  - AC-002 preserves substantive content and AC-003 rejects invalid contracts.
- Gate:
  - Full target validation passes on valid fixture.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - Detection and ID unit tests.

## Parallelization Notes
- Asset creation can proceed with module scaffolding; safe writes and validation depend on shared paths.

## Phase Gate Summary
- Gate A: importable package and contract assets.
- Gate B: valid and invalid fixture behavior proven.
