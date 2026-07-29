# Optional Engineering Export - Product Requirements Document

## 1. Overview
Separate product-owned canonical feature specs from an optional compatibility
export for Engineering Harness.

## 2. Background & Problem Statement
The current handoff makes an Engineering Harness path mandatory, blurring
ownership and preventing product-only targets from remaining self-contained.

## 3. Goals & Non-Goals
### Goals
- Write a full canonical product spec under `docs/product-specs/`.
- Export compatible `informal.md` only when explicitly requested/configured.
- Preserve all pre-existing Engineering Harness artifacts.

### Non-Goals
- Change Engineering Harness code, formats, or work-item lifecycle.

## 4. Users & Use Cases
- Product owner: define and maintain features without an engineering workflow.
- Engineering team: receive an explicit compatibility export when desired.

## 5. UX / UI Requirements
- Reports identify canonical spec, export state, and any non-owned file conflict.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- No product command requires or mutates Engineering Harness folders by default.

## 9. Data, Interfaces & Dependencies
- Product spec is local canonical Markdown; export uses public contract v1 only.

## 10. Repository & Platform Considerations
- Existing `docs/exec-plans` remains untouched unless an explicit export is safe.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- Handoff report distinguishes generated canonical specs from optional exports.

## 13. Risks & Mitigations
- Export overwrites engineering work: refuse an unmarked existing `informal.md`.

## 14. Open Questions & Assumptions
### Open Questions
- Explicit export is controlled by a method argument; a full target CLI loader is future work.

### Assumptions
- Existing generated exports include the product-harness frontmatter marker.

## 15. QA Plan
- Test product-only targets, safe export, conflict refusal, and old export preservation.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
