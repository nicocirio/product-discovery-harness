# Quality and Release - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Add fixtures, tests, CI, version metadata, changelog, and final validation evidence.

## Clarifications & Default Assumptions
- Quality lane begins fixture scaffolding early but its final gate follows all executable lanes.

## Phase 1: Fixture and Test Coverage
- Goal: codify acceptance behavior in isolated tests.
- Tasks:
  - [x] Build target fixtures and temporary-home helpers.
  - [x] Add unit and integration tests for every mandatory behavior.
- Testing Tasks:
  - [x] Run the full pytest suite.
  - Command(s): `make test`
- Definition of Done:
  - AC-001 maps to passing behavior tests.
- Gate:
  - No test accesses the real HOME.
- Dependencies:
  - Core, workflow, and installer interfaces.
- Parallelizable Work:
  - Fixture assembly while features are implemented.

## Phase 2: CI and Release Evidence
- Goal: make repeatable verification the release gate.
- Tasks:
  - [x] Add GitHub Actions and Make targets.
  - [x] Add version/changelog and validation reports.
- Testing Tasks:
  - [x] Run CI-equivalent commands locally.
  - Command(s): `make test && make validate && git diff --check`
- Definition of Done:
  - AC-002 CI commands exist and AC-003 release metadata/evidence are current.
- Gate:
  - All local checks pass.
- Dependencies:
  - Phase 1 and completed executable lanes.
- Parallelizable Work:
  - CI YAML and release documentation.

## Parallelization Notes
- Tests are added alongside each lane; final evidence is collected after all code is present.

## Phase Gate Summary
- Gate A: isolated tests cover required behavior.
- Gate B: CI-equivalent release gate passes.
