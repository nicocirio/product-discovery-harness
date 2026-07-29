# Distribution and Skills - Product Requirements Document

## 1. Overview
Package the complete Product Discovery Harness so agents can install and invoke consistent, collision-safe workflows from any target repository.

## 2. Background & Problem Statement
Reusable skills must be globally available while target product context stays versioned in the target repository.

## 3. Goals & Non-Goals
### Goals
- Supply all 17 operational skills and shared personas.
- Install, update, inspect, and repair namespaced skill symlinks.
- Document the workflow completely in English and Spanish.

### Non-Goals
- Require Engineering Harness or copy this repository into every target.

## 4. Users & Use Cases
- Agent user: globally install skills for Codex and Claude roots.
- Product facilitator: follow conversation-first skills with one primary question.

## 5. UX / UI Requirements
- Commands state selected channel, version, targets, and broken links; skills give concrete next steps.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Shell scripts quote paths and resolve their own repository root through symlinks.

## 9. Data, Interfaces & Dependencies
- Git is used only for installer acquisition/update; package CLI supplies validation.

## 10. Repository & Platform Considerations
- Supports existing Codex, Claude, both, or neither initial target roots.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- Status output reports all installed namespaces and broken links locally.

## 13. Risks & Mitigations
- Unrelated skill collision: never replace a non-owned namespace.
- Stale link: repair only owned broken symlinks.

## 14. Open Questions & Assumptions
### Open Questions
- Release tags are optional in a local checkout; stable falls back to default branch.

### Assumptions
- Git is installed when network-based installation/update is requested.

## 15. QA Plan
- Automated validation: temporary-home installer tests and skill catalog checks.
- Manual validation: run status after a local installation.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
