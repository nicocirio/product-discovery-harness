# Product Reconciliation - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Add durable relation tracing and non-destructive reconciliation reports.

## Clarifications & Default Assumptions
- Only the owner confirms a relation; agent-detected overlap starts proposed.

## Phase 1: Canonical Relation Contract
- Goal: validate cross-record relationships and alignment links.
- Tasks:
  - [x] Add record relation rules and optional templates.
  - [x] Extend target validation.
- Testing Tasks:
  - [x] Add invalid/missing/self/duplicate relation tests.
  - Command(s): `.venv/bin/python -m pytest tests/test_reconciliation.py`
- Definition of Done:
  - AC-001 validates durable links.
- Gate:
  - Existing empty indexes remain valid.
- Dependencies:
  - Existing record/ID validation.
- Parallelizable Work:
  - Skill and report template drafting.

## Phase 2: Reports and Workflow Integration
- Goal: give owner actionable reports and promotion guardrails.
- Tasks:
  - [x] Add renderer, CLI, reconcile skill, and workflow updates.
  - [x] Integrate landscape/review visibility.
- Testing Tasks:
  - [x] Test focused/global report and no input mutation.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-002/AC-003 pass.
- Gate:
  - Full validators and review pass.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - README translations.

## Parallelization Notes
- Report wording follows the relation vocabulary.

## Phase Gate Summary
- Gate A: valid canonical relationships.
- Gate B: actionable, non-destructive reconciliation flow.
