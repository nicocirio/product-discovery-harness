# Audit history - Product Requirements Document

## 1. Overview
Preserve durable historical evidence for every brownfield repository audit while retaining a replaceable view of the current product baseline.

## 2. Background & Problem Statement
The existing audit overwrites current-state artifacts. Users cannot later tell what the audit found on an earlier run or compare evolving repository evidence.

## 3. Goals & Non-Goals
### Goals
- Write a unique dated report for every audit execution.
- Keep `current-state/feature-inventory.yml` and `repository-map.md` as the up-to-date snapshot.
- Make the latest and prior reports discoverable locally.

### Non-Goals
- Interpret product changes automatically or modify application code.
- Create a database, remote service, or git history dependency.

## 4. Users & Use Cases
- Product owner: reruns audit after development and compares repository evidence over time.
- Facilitator: routes review-current-state to the newest evidence while retaining prior context.

## 5. UX / UI Requirements
- CLI output names the current snapshot and the newly created historical report.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Local-only writes, deterministic report names, and no application-code mutation.

## 9. Data, Interfaces & Dependencies
- New Markdown reports and an index live in `docs/product-discovery/audits/`.

## 10. Repository & Platform Considerations
- Preserve configured scope and existing static-file detection.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- CLI output makes report paths observable; no external telemetry.

## 13. Risks & Mitigations
- Repeated same-day reports could collide: use a sequential suffix rather than overwriting.

## 14. Open Questions & Assumptions
### Open Questions
- None.

### Assumptions
- Current-state snapshots are intentionally replaceable; historical reports are immutable evidence.

## 15. QA Plan
- Automated validation: audit twice with fixed date and assert separate reports, snapshot refresh, index, and CLI output.
- Manual validation: open the generated audit index in a seeded brownfield target.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
