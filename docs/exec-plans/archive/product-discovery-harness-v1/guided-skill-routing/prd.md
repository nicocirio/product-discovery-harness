# Guided Skill Routing - Product Requirements Document

## 1. Overview
Turn the skill-guidance audit into consistent, agent-facing protocols. Every
product skill must close with one recommended next focus and route a user back
to a natural entry point when required context is unavailable.

## 2. Background & Problem Statement
The onboarding guide correctly tells owners to start with `$product-talk` and
let the harness guide them. The audit found uneven support for that promise:
some specialist skills stop at a precondition, and several outputs do not name
the next useful action. This leaks the harness's internal workflow to users.

## 3. Goals & Non-Goals
### Goals
- Establish a uniform next-focus output across all nineteen skills.
- Make precondition failures actionable and friendly.
- Preserve human approval for promotions, decisions, relations, and acceptance.
- Test the protocol contract so future skill additions cannot drift.

### Non-Goals
- Add a CLI router, automatic record promotion, or automatic decision making.
- Change product schemas, lifecycle semantics, or engineering handoff ownership.
- Turn every discussion into a durable record.

## 4. Users & Use Cases
- New owner with a raw thought: starts with talk instead of needing an ID.
- Returning owner who supplies an unknown ID: is sent to landscape.
- Owner who invokes an advanced skill too early: is told the smallest useful
  next discovery action.
- Maintainer adding a skill: follows a test-enforced contract.

## 5. UX / UI Requirements
- Protocol wording must be plain, direct, and recommend exactly one next focus.
- Recovery messages distinguish a missing prerequisite from a rejected idea or
  a failed product decision.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- No network access, application-code mutation, or ownership-boundary expansion.
- Skill Markdown remains concise and readable when installed independently.

## 9. Data, Interfaces & Dependencies
- Affected interfaces: `agents/product-facilitator.md`, all `skills/*/SKILL.md`,
  README wording where needed, and protocol tests.

## 10. Repository & Platform Considerations
- Skills are symlinked as standalone directories; required routing guidance must
  live in each skill rather than rely only on a repository-global document.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- No telemetry. Contract tests demonstrate coverage of all installed skills.

## 13. Risks & Mitigations
- Uniform wording can become boilerplate: each skill retains a contextual
  recommendation while using a stable label.
- Friendly routing can bypass safety: routes only suggest an action and preserve
  owner confirmation requirements.

## 14. Open Questions & Assumptions
### Open Questions
- Whether a future CLI command should compute routing remains out of scope.

### Assumptions
- Agent-facing skill protocols are the appropriate interface for this guidance
  because no interactive CLI router currently exists.

## 15. QA Plan
- Automated validation:
  - Test every skill for a next-focus contract and contextual recovery wording.
  - Run repository, product-contract, Harness, and traceability gates.
- Manual validation:
  - Follow raw-idea, unknown-ID, and unmet-prerequisite paths as a new owner.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
