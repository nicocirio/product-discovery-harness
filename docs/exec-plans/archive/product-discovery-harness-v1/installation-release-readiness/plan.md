# Installation Release Readiness - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Implement a checkout-based public installer, resource resolution, docs, and
temporary-HOME verification.

## Clarifications & Default Assumptions
- Git checkout is v0.1.0 distribution; PyPI is not advertised.

## Phase 1: Distribution Runtime
- Goal: provide self-contained install/update/status/CLI behavior.
- Tasks:
  - [x] Add shared installer library and checkout-local CLI wrapper.
  - [x] Rewrite install/update/status and curl bootstrap around channels.
  - [x] Add checkout-root resource link beside installed skills.
- Testing Tasks:
  - [x] Test temporary-HOME install and CLI invocation.
  - Command(s): `pytest tests/test_installation.py -q`
- Definition of Done:
  - AC-001, AC-002, and AC-003 pass.
- Gate:
  - No unowned namespace is changed.
- Dependencies:
  - Git and Python.
- Parallelizable Work:
  - README copy after command contract stabilizes.

## Phase 2: Public Documentation and Gates
- Goal: make public use unambiguous and verified.
- Tasks:
  - [x] Update both READMEs with install/update/status/bootstrap flow.
  - [x] Add installation regression coverage.
- Testing Tasks:
  - [x] Run full test and validation gates.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-004 and AC-005 pass.
- Gate:
  - Documentation does not promise wheel/PyPI use.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - None.

## Parallelization Notes
- Runtime first, documentation second.

## Phase Gate Summary
- Gate A: installable checkout.
- Gate B: documented and validated public path.
