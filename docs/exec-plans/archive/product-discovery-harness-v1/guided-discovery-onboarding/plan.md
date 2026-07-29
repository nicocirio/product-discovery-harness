# Guided Discovery Onboarding - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Teach the harness through guided, conditional product discovery in both README
languages; protect the claims with tests; then audit each product skill without
changing its behavior.

## Clarifications & Default Assumptions
- “Guides the next step” means the agent recommends a context-sensitive action,
  not that it automatically creates, accepts, or promotes durable records.
- The audit is documentation and evidence, not a skill implementation change.

## Phase 1: Guided README Narrative
- Goal: make a newcomer start naturally with conversation rather than command
  selection.
- Tasks:
  - [x] Replace catalog-first orientation with an intent-first start section.
  - [x] Add the continuous appointment-booking story, generated-ID output, and
    landscape retrieval.
  - [x] Show separate simple and optional deeper paths.
  - [x] Mirror operational meaning in Spanish and retain the catalog as grouped
    reference.
- Testing Tasks:
  - [x] Inspect both guides as a newcomer and verify no ID appears before its
    origin is explained.
  - Command(s): `python3 -m pytest tests/test_readme.py -q`
- Definition of Done:
  - AC-001, AC-002, and AC-003 are visibly satisfied without changing behavior.
- Gate:
  - No claim of automatic promotion or a required skill sequence.
- Dependencies:
  - Existing README and installed skills.
- Parallelizable Work:
  - Spanish copy can follow the English information architecture.

## Phase 2: Regression Coverage
- Goal: make the onboarding promise resistant to catalog or prose drift.
- Tasks:
  - [x] Extend README tests for guided entry, ID creation/retrieval, conditional
    paths, and language parity.
- Testing Tasks:
  - [x] Run the complete repository suite and target validation.
  - Command(s): `make test && make validate`
- Definition of Done:
  - AC-005 is covered by automated tests and all repository gates pass.
- Gate:
  - Tests assert real behavior and do not hard-code incidental formatting.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - None; assertions need final wording and structure.

## Phase 3: Skill Guidance Audit
- Goal: determine whether every protocol fulfills the README promise.
- Tasks:
  - [x] Read all nineteen SKILL.md files and the shared facilitator guidance.
  - [x] Create a durable audit table with guidance posture, assumed expertise,
    evidence, and follow-up recommendation per skill.
  - [x] Add an automated coverage check for the audit.
- Testing Tasks:
  - [x] Validate audit coverage and run work-item traceability gates.
  - Command(s): `python3 -m pytest -q`
- Definition of Done:
  - AC-004 is evidenced; findings distinguish immediate guidance gaps from
    appropriate specialist prerequisites.
- Gate:
  - No behavior change is smuggled into the audit.
- Dependencies:
  - Phase 1, because audit evaluates the stated onboarding promise.
- Parallelizable Work:
  - Skill reading and audit-table drafting can be independently cross-checked.

## Parallelization Notes
- Phase 3 remains read-only and follows the completed documentation design.

## Phase Gate Summary
- Gate A: newcomer-readable, conditional onboarding.
- Gate B: automated README regression coverage.
- Gate C: complete, evidence-backed skill guidance audit.
