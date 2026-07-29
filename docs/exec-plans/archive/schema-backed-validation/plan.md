# Schema-backed validation - Delivery Plan

Scope and reference artifacts:
- PRD: `docs/exec-plans/current/schema-backed-validation/prd.md`
- FDD: `docs/exec-plans/current/schema-backed-validation/fdd.md`

## Scope
Activate the existing JSON Schemas in local validation and cover the behavior with focused tests.

## Clarifications & Default Assumptions
- Use the existing Draft 2020-12-compatible `jsonschema` dependency.
- Keep semantic validation alongside structural schema validation.

## Phase 1: Add schema-validation boundary
- Goal: Load local schemas and return deterministic violations.
- Tasks:
  - [x] Add the schema helper and map each target YAML document to its schema.
  - [x] Validate export frontmatter before atomic write.
- Testing Tasks:
  - [x] Add focused unit tests for structural failure and handoff protection.
  - Command(s): `make test`
- Definition of Done:
  - Runtime validation executes schemas without network access.
- Gate:
  - AC-001 and AC-003 are represented by passing tests.
- Dependencies:
  - None.
- Parallelizable Work:
  - Test cases can be written alongside the helper.

## Phase 2: Verify and close documentation
- Goal: Confirm regression safety and record implementation evidence.
- Tasks:
  - [x] Run the repository gates and review the diff for diagnostic regressions (AC-002).
- Testing Tasks:
  - [x] Run target validation tests and full test suite.
  - Command(s): `make validate && make test && git diff --check`
- Definition of Done:
  - All requirements have implementation and test evidence.
- Gate:
  - Harness validation and repository gates pass.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - None.

## Parallelization Notes
- The scope is small and tightly coupled; sequential execution is clearer.

## Phase Gate Summary
- Gate A: schemas execute against target data and handoff frontmatter.
- Gate B: all tests, review, and work-item validation pass.
