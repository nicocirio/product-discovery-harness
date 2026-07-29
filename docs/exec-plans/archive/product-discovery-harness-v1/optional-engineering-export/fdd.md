# Optional Engineering Export - Functional Design Document

## 1. Executive Summary
Split handoff rendering into a product-owned canonical spec writer and a guarded,
opt-in Engineering Harness export writer.

## 2. Requirements & Assumptions
- Functional requirements: FR-001 canonical spec, FR-002 optional export, FR-003 safe ownership boundary.
- Non-functional requirements: no default Engineering Harness directory requirement or mutation.
- Assumptions: generated exports can be recognized by handoff frontmatter.

## 3. Repository Context Summary
- What we know: handoff currently writes informal first and bootstrap/validation require exec-plans.
- Unknowns to confirm: direct feature loading CLI remains outside this migration.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`write_product_spec` writes complete product content to `docs/product-specs`.
`export_engineering_handoff` renders a public v1 projection only when requested.
`create_handoff` orchestrates both and returns a report. Bootstrap/validation
treat `product-specs` as product-owned and `exec-plans` as optional.

### 4.2 State & Data Flow
Accepted feature → canonical spec → optional export request → ownership check →
generated informal.md. Existing engineering files are read only for conflict checks.

### 4.3 Lifecycle & Ownership
Product Harness owns specs and generated exports it marks. Engineering Harness
owns all other files under exec-plans, including non-marked informal files.

### 4.4 Alternatives Considered
Copying all specs into exec-plans was rejected because it duplicates canonical
content. Deleting/migrating old exports was rejected because it would alter
engineering-owned history.

## 5. Interfaces
- `create_handoff(repo, feature, epic=None, export_engineering=False) -> HandoffReport`
- `export_engineering_handoff(...)` raises a conflict for an unowned target.

## 6. Data Model & Storage
- Canonical spec frontmatter has `document_type: product-feature-spec`.
- Export has existing `product-feature-handoff` frontmatter and `canonical_spec`.

## 7. Consistency & Transactions
- Validate readiness before any write; write each generated document atomically.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Single feature rendering and bounded path checks.

## 10. Failure Modes & Resilience
- Export conflict leaves canonical spec intact and reports the exact target path.

## 11. Observability
- Report canonical path and optional export path separately.

## 12. Security & Privacy
- Export paths are target-relative and never inspect or execute engineering code.

## 13. Testing Strategy
- AC-001 product-only; AC-002 export frontmatter/link; AC-003 conflict and validation independence.

## 14. Backwards Compatibility
- Existing exported informal files remain valid and untouched; export remains available explicitly.

## 15. Risks & Mitigations
- Callers expecting a Path: report exposes `canonical_spec_path` and an optional export path explicitly.

## 16. Open Questions & Follow-ups
- Add a command-level feature resolver in a later feature.

## 17. References
- `prd.md`, existing handoff module, and public Engineering Harness informal contract.
