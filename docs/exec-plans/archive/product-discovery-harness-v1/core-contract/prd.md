# Core Contract - Product Requirements Document

## 1. Overview
Provide a safe, portable target-repository contract and local CLI foundation for Product Discovery Harness v0.1.0.

## 2. Background & Problem Statement
Agents need durable discovery memory that can be initialized and checked without overwriting product-owner context.

## 3. Goals & Non-Goals
### Goals
- Detect greenfield, brownfield, and ambiguous repositories.
- Seed and validate the complete target contract while preserving substantive files.
- Enforce stable IDs, lifecycle states, schemas, and cross-reference integrity.

### Non-Goals
- Modify application code or contact remote product systems.

## 4. Users & Use Cases
- Product owner: initialize or validate a target repository safely.
- Agent: allocate durable record IDs and identify contract defects.

## 5. UX / UI Requirements
- CLI errors name the file, path, and remediation; generated documents are plain Markdown/YAML.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Work on macOS and Linux using Python 3.10+; writes are atomic where practical.

## 9. Data, Interfaces & Dependencies
- Uses templates and JSON schemas packaged with the project; PyYAML and jsonschema are explicit dependencies.

## 10. Repository & Platform Considerations
- Follow `ARCHITECTURE.md` and preserve target files by default.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
- Local command output and validation results provide observable success; no external telemetry is sent.

## 13. Risks & Mitigations
- Mistaking boilerplate for a product: classify as pending and require human choice.
- Accidental overwrite: use seeded markers and backup before forced replacement.

## 14. Open Questions & Assumptions
### Open Questions
- None for the initial local contract.

### Assumptions
- Target repositories permit documentation and metadata writes.

## 15. QA Plan
- Automated validation: pytest detection, seeding, IDs, and validator tests.
- Manual validation: inspect a seeded greenfield and brownfield target.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
