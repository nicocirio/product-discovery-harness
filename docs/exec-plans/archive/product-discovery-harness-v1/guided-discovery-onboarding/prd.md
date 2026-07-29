# Guided Discovery Onboarding - Product Requirements Document

## 1. Overview
Rework the English-first README and Spanish counterpart so a newcomer can use
the harness naturally: start a conversation, receive a recommended next step,
and reach specialized skills only when the discovery calls for them. Audit the
installed product-skill protocols against that promise.

## 2. Background & Problem Statement
The existing skill catalog accurately enumerates the tools but can look like a
required linear workflow. Examples introduced durable IDs before explaining how
they are created or found. This asks users to become experts in the harness
before the harness has helped them.

## 3. Goals & Non-Goals
### Goals
- Make `$product-talk` the approachable default entry point.
- Explain simple versus deeper discovery as conditional paths.
- Use a familiar appointment-booking scenario to show ID creation and recovery.
- Produce a complete, evidence-backed audit of skill guidance.

### Non-Goals
- Change skill behavior during this work item.
- Alter product record schemas, CLI behavior, or target documents.
- Claim that a conversation can silently promote or accept a durable record.

## 4. Users & Use Cases
- New product owner: starts with an unformed idea and needs the next question,
  not a list of commands.
- Returning owner: finds a named durable record through the landscape before
  using its harness-assigned ID.
- Maintainer: uses the audit to decide which skill protocols need a later
  behavior change.

## 5. UX / UI Requirements
- Teach with a continuous, plain-language appointment-booking example.
- Place specialist skills behind intent-based paths and explicitly mark deeper
  exploration as optional.
- Use IDs only after showing the harness-assigned creation output and landscape
  retrieval mechanism.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Documentation must be accurate, concise, readable in common Markdown
  renderers, and equal in operational meaning across English and Spanish.

## 9. Data, Interfaces & Dependencies
- README files, installed `skills/*/SKILL.md` protocols, and
  `tests/test_readme.py` are the affected interfaces.
- The audit is a read-only documentation artifact.

## 10. Repository & Platform Considerations
- Preserve the product/engineering ownership boundary and the optional,
  marked Engineering Harness export described in the repository contract.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- No telemetry is emitted. Automated checks evidence the documented entry path,
  examples, and language parity.

## 13. Risks & Mitigations
- A simplified guide could hide important controls: retain the full catalog as
  a reference after intent-based onboarding.
- An audit could be mistaken for a behavior change: label it as findings and
  follow-up recommendations only.

## 14. Open Questions & Assumptions
### Open Questions
- Which audit recommendations should become a separate behavior-change work
  item is intentionally deferred until the review is complete.

### Assumptions
- The appointment-booking scenario is sufficiently familiar and neutral for a
  primary learning example.

## 15. QA Plan
- Automated validation:
  - Extend README tests for guided entry, ID progression, and conditional paths.
  - Run repository tests, target validation, work-item validation, and
    requirements traceability checks.
- Manual validation:
  - Read both guides in order as a first-time user.
  - Inspect the audit for all 19 installed skills.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
