# Manual release process - Product Requirements Document

## 1. Overview
Give maintainers a concise manual release procedure that matches the installer’s stable/latest channel behavior.

## 2. Background & Problem Statement
Without a documented procedure, version tags can be forgotten or pushed before repository gates pass, making stable installation ambiguous.

## 3. Goals & Non-Goals
### Goals
- Document validation, version update, commit, tag, and push steps.
- Explain stable/latest behavior and post-publication remote smoke-test follow-up.
- Keep English primary with an equivalent Spanish guide.

### Non-Goals
- Automate releases or publish packages.

## 4. Users & Use Cases
- Maintainer: publish `v0.1.0` and later releases safely.

## 5. UX / UI Requirements
- Commands are copyable and ordered.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Documentation-only change; no network or repository mutation during validation.

## 9. Data, Interfaces & Dependencies
- README, Spanish README, and operations documentation.

## 10. Repository & Platform Considerations
- Release gates are `make test`, `make validate`, and whitespace checks.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
N/A

## 13. Risks & Mitigations
- Manual error: use an explicit preflight and annotated tag commands.

## 14. Open Questions & Assumptions
### Open Questions
- None.

### Assumptions
- The maintainer has push permission and the repository will be public at release time.

## 15. QA Plan
- Automated validation: README assertions and repository gates.
- Manual validation: read each command in order against installer behavior.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
