# Installation Release Readiness - Detailed Design

Source Artifacts: `../prd.md`, `../fdd.md`, `../plan.md`.

## 1. Slice Summary
- Objective: one checkout, one CLI wrapper, linked skills and resources.

## 2. Requirements Coverage
- FR-001/AC-001: wrapper and temporary-HOME test.
- FR-002/AC-002: shared Git channel helpers.
- FR-003/AC-003: explicit checkout-root skill instruction.
- FR-004/AC-004/AC-005: README and validation tests.

## 3. Responsibilities & Boundaries
- Bash owns Git/linking; Python owns product commands; target changes happen
  only through explicit CLI/skill actions.

## 4. Interfaces & Signatures
- `bin/product-harness <command>` sets `PYTHONPATH=<checkout>/src`.

## 5. Data Flow & Edge Cases
- Stable selects newest tag; latest selects origin default branch; no tag is an
  explicit stable-channel error.

## 6. Test Plan
- Local checkout installation, status, CLI bootstrap, update/repair, README.

## 7. Risks & Open Questions
- PyPI packaging deferred.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
