# Test Matrix - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: prove every public behavior with isolated local tests and CI.
- In scope: fixtures, pytest modules, Make targets, GitHub Actions, evidence.
- Out of scope: remote vendor integration tests.

## 2. Requirements Coverage
- FR-001 / AC-001: behavior test modules cover mandatory acceptance groups.
- FR-002 / AC-002: workflow invokes make test and make validate.
- FR-003 / AC-003: metadata/evidence checks assert v0.1.0 release files.

## 3. Responsibilities & Boundaries
- Fixtures are copied to temporary paths; installation tests override HOME and never use the actual account home.

## 4. Interfaces & Signatures
- `make test`, `make validate`, and `pytest` are the supported verification interfaces.

## 5. Data Flow & Edge Cases
- Main flow:
  1. Copy fixture/create temp target.
  2. Invoke public function or command.
  3. Assert files, content, error code, and preservation.
- Edge cases:
  - Broken link repair and incomplete handoff use isolated paths.

## 6. Test Plan
- Unit or component tests:
  - IDs, schemas, lifecycle rules, path resolution.
- Integration tests:
  - Bootstrap/audit/handoff/installer lifecycle.
- Manual checks:
  - Confirm CI file runs declared commands.

## 7. Risks & Open Questions
- Risks:
  - Tests that inspect real configuration; temp environment prevents it.
- Open questions:
  - None.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
