# Guided Skill Routing - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Harden all skill protocols so they guide owners through unknown context and end
with one clear next focus; add regression tests without changing runtime logic.

## Clarifications & Default Assumptions
- Guidance is advisory and contextual, not automatic routing or record mutation.

## Phase 1: Protocol Contract and Recovery Routes
- Goal: make every skill understandable without workflow expertise.
- Tasks:
  - [x] Add a shared next-focus expectation to facilitator guidance.
  - [x] Update all nineteen SKILL.md files with contextual output and recovery
    routes.
- Testing Tasks:
  - [x] Inspect raw idea, unknown-ID, and unmet-prerequisite flows.
  - Command(s): `python3 -m pytest tests/test_skill_guidance.py -q`
- Definition of Done:
  - AC-001, AC-002, and AC-003 are represented in every affected protocol.
- Gate:
  - No automatic promotion, acceptance, or ownership-boundary change.
- Dependencies:
  - Completed guidance audit.
- Parallelizable Work:
  - Route wording can be cross-checked after output contracts are drafted.

## Phase 2: Contract Tests and Validation
- Goal: protect the protocols and README promise from drift.
- Tasks:
  - [x] Add tests for contract coverage, recovery routes, and safety language.
  - [x] Sync the README only if protocol wording materially changes its claim.
- Testing Tasks:
  - [x] Run full tests, product validation, traceability, and work-item checks.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-004 and AC-005 pass.
- Gate:
  - Tests cover every installed skill by discovery rather than a stale hand list.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - None.

## Parallelization Notes
- All protocol changes are documentation-only but must land coherently.

## Phase Gate Summary
- Gate A: consistent, safe guidance.
- Gate B: tested and validated contract.
