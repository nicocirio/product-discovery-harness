# Product Landscape - Product Requirements Document

## 1. Overview
Create an outcome-oriented generated view that helps a product owner orient,
prioritize, revisit, defer, or discard durable product records.

## 2. Background & Problem Statement
Existing indexes do not yet prescribe per-record paths or review metadata, so a
table could otherwise fabricate links and hide stale thinking.

## 3. Goals & Non-Goals
### Goals
- Formalize index-owned record paths and review timestamps for opportunities and features.
- Generate a Markdown landscape with idea, real document link, status/next action, and age.
- Highlight stale records for conversation without making automatic decisions.

### Non-Goals
- Synchronize implementation status with Engineering Harness or auto-reject records.

## 4. Users & Use Cases
- Product owner: ask “how are we with our ideas?” and locate the relevant context.
- Product facilitator: choose the highest-leverage stale or incomplete thread.

## 5. UX / UI Requirements
- Default output is compact, grouped by attention state, and uses readable relative ages.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- The command is deterministic, local-only, idempotent, and preserves owner-authored records.

## 9. Data, Interfaces & Dependencies
- Uses target `opportunities/index.yml` and `features/index.yml`; no Engineering Harness dependency.

## 10. Repository & Platform Considerations
- Additive schema evolution must keep existing empty indexes and target repositories valid.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- Report record count, missing documents, and stale review count in the generated summary.

## 13. Risks & Mitigations
- False link confidence: render a missing-document marker instead of an invented link.
- Treating age as rejection: present a review prompt, never a lifecycle mutation.

## 14. Open Questions & Assumptions
### Open Questions
- Default stale threshold is 30 days and may become configurable later.

### Assumptions
- `last_reviewed_at` reflects a meaningful human/product review, not merely generated output.

## 15. QA Plan
- Automated validation: path, date, status, grouping, stale, preservation, and CLI tests.
- Manual validation: inspect a target with active, deferred, and incomplete records.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
