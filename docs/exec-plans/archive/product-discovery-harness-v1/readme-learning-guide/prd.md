# README Learning Guide - Product Requirements Document

## 1. Overview
Create accurate, approachable bilingual documentation that teaches a product
owner how to learn and use Product Discovery Harness.

## 2. Background & Problem Statement
The current README describes components but does not sufficiently teach the
conversation-to-spec workflow, truth layers, consistency guardrails, or the
distinction between agent skills and local commands.

## 3. Goals & Non-Goals
### Goals
- Make English README the primary practical entry point and Spanish a complete counterpart.
- Explain core concepts with minimal useful Mermaid diagrams and realistic outputs.
- Document every skill and the optional Simon Initiative complement accurately.

### Non-Goals
- Claim automatic semantic decisions or make Engineering Harness required.

## 4. Users & Use Cases
- New product owner: learn the first session and typical workflow.
- Returning owner: find the correct skill and durable document quickly.

## 5. UX / UI Requirements
- Scan-friendly headings, compact tables, exact invocations, and limited diagrams.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Markdown must render on GitHub and remain accurate to installed skill names/CLI.

## 9. Data, Interfaces & Dependencies
- Links local skills/docs and the public Simon Initiative Harness repository.

## 10. Repository & Platform Considerations
- README distinguishes `$product-*` conversational skills from `product-harness` CLI commands.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- A reader can start greenfield/brownfield and locate a skill/document without source inspection.

## 13. Risks & Mitigations
- Documentation drift: validate skill names and command examples against the repository.

## 14. Open Questions & Assumptions
### Open Questions
- None; the README documents current v0.1.0 behavior.

### Assumptions
- Mermaid renders in the primary GitHub documentation viewer.

## 15. QA Plan
- Validate Markdown links, skill coverage, command names, and English/Spanish section parity.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
