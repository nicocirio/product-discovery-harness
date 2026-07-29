# Discovery Workflows - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Implement auditable archaeology, sessions, record helpers, external briefs, and Engineering Harness handoff.

## Clarifications & Default Assumptions
- Audit is static and non-destructive; runtime verification is explicitly opt-in future work.

## Phase 1: Current State and Durable Records
- Goal: create scoped audit and session/record workflows.
- Tasks:
  - [x] Render evidence-labeled inventory from source signals.
  - [x] Create deterministic session summaries and record updates.
- Testing Tasks:
  - [x] Assert application source remains unchanged.
  - Command(s): `pytest tests/test_audit.py tests/test_sessions.py`
- Definition of Done:
  - AC-001 emits provisional evidence and AC-002 preserves session/acceptance metadata.
- Gate:
  - Brownfield fixture validation passes.
- Dependencies:
  - Core contract Phase 2.
- Parallelizable Work:
  - Session and record rendering.

## Phase 2: Experience and Handoff
- Goal: produce tool-neutral exploration briefs and guarded handoff output.
- Tasks:
  - [x] Generate design prompts from opportunity context.
  - [x] Enforce feature readiness and render public informal.md.
- Testing Tasks:
  - [x] Test incomplete and accepted feature paths.
  - Command(s): `pytest tests/test_handoff.py`
- Definition of Done:
  - AC-003 rejects incomplete feature data and emits a schema-valid handoff when ready.
- Gate:
  - Handoff validation passes.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - Prompt adapters and Markdown rendering.

## Parallelization Notes
- Prompt templates can be written while handoff readiness checks are implemented.

## Phase Gate Summary
- Gate A: non-mutating archaeology and record persistence.
- Gate B: valid handoff contract and failed readiness path.
