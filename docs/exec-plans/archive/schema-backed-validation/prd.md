# Schema-backed validation - Product Requirements Document

## 1. Overview
Make the repository's published JSON Schemas an executable part of target validation.

## 2. Background & Problem Statement
The schemas currently describe a durable contract but the runtime validator does not load them, allowing schema and executable behavior to drift.

## 3. Goals & Non-Goals
### Goals
- Enforce the existing configuration and discovery-document schemas.
- Retain clear, domain-specific validation diagnostics.
- Reject an invalid generated Engineering Harness export before it is written.

### Non-Goals
- Redesign the target document model or add remote schema resolution.
- Replace semantic cross-reference validation with JSON Schema.

## 4. Users & Use Cases
- Harness maintainers: change a schema knowing tests exercise it at runtime.
- Target-repository users: receive a file-scoped explanation when their contract is structurally invalid.

## 5. UX / UI Requirements
- CLI errors name the affected target-relative file and the schema failure.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Validation stays local, deterministic, and linear in the already-scoped target files.

## 9. Data, Interfaces & Dependencies
- Uses the existing `jsonschema` runtime dependency and JSON files bundled in `schemas/`.

## 10. Repository & Platform Considerations
- Python 3.10+; preserve the package's filesystem-only boundary.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- Local validation errors remain directly observable through CLI output; no telemetry is emitted.

## 13. Risks & Mitigations
- Schema errors may be less familiar than custom messages: prefix them with target-relative paths and retain semantic checks.

## 14. Open Questions & Assumptions
### Open Questions
- None.

### Assumptions
- The checked-in schemas are the intended public structural contract.

## 15. QA Plan
- Automated validation:
  - Add focused validation and handoff tests, then run `make test` and `make validate`.
- Manual validation:
  - Inspect a CLI validation error for an invalid target document.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
