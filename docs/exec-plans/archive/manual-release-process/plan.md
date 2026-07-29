# Manual release process - Delivery Plan

Scope and reference artifacts:
- PRD: `docs/exec-plans/current/manual-release-process/prd.md`
- FDD: `docs/exec-plans/current/manual-release-process/fdd.md`

## Scope
Document the maintainer-owned manual release workflow and its installer-channel semantics.

## Clarifications & Default Assumptions
- Use annotated `vX.Y.Z` tags and push only after all required gates pass.

## Phase 1: Write and align release guidance
- Goal: Give maintainers an accurate, bilingual manual procedure.
- Tasks:
  - [x] Update English README, Spanish README, and operations policy with FR-001, FR-002, and FR-003.
- Testing Tasks:
  - [x] Inspect commands against installer behavior and run documentation-related tests.
  - Command(s): `make test`
- Definition of Done:
  - Release flow is explicit and bilingual.
- Gate:
  - AC-001, AC-002, and AC-003 are documented.
- Dependencies:
  - None.
- Parallelizable Work:
  - English and Spanish drafting can be checked independently.

## Phase 2: Verify and record evidence
- Goal: Run repository and Harness validation gates.
- Tasks:
  - [x] Run tests and local review.
- Testing Tasks:
  - [x] Verify requirements traceability.
  - Command(s): `make validate && make test && git diff --check`
- Definition of Done:
  - All gates pass.
- Gate:
  - Work-item validation passes.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - None.

## Parallelization Notes
- Documentation changes are small; sequential review keeps terms consistent.

## Phase Gate Summary
- Gate A: accurate manual release instructions exist in both languages.
- Gate B: repository and Harness gates pass.
