# Global command shims - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Phase 1: Regression-first command links
- Goal: make documented commands available after install and migration.
- Tasks:
  - [x] Add failing temporary-home regression coverage for AC-001.
  - [x] Link safe command shims and make shell entrypoints symlink-aware.
  - [x] Add installer-refresh coverage for AC-002.
- Testing Tasks:
  - [x] Run `pytest tests/test_installation.py`.
- Definition of Done:
  - Both acceptance criteria pass.
- Gate:
  - Full repository gates pass.
- Dependencies:
  - None.
- Parallelizable Work:
  - None.

## Phase Gate Summary
- Gate A: installed direct commands execute and legacy reinstall migrates links.
