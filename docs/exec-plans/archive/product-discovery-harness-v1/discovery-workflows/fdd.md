# Discovery Workflows - Functional Design Document

## 1. Executive Summary
Workflow services create evidence-labeled current-state documents, concise sessions, product records, design briefs, and public handoff files.

## 2. Requirements & Assumptions
- Functional requirements: FR-001 through FR-003 use core contract primitives.
- Non-functional requirements: audit is source-code read-only and handoff remains Engineering Harness independent.
- Assumptions: accepted records have a human-provided `accepted_by` value.

## 3. Repository Context Summary
- What we know: current/future/execution truth must remain separate in target docs.
- Unknowns to confirm: runtime inspection is deliberately omitted unless explicitly authorized.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`audit` scans scoped text files and renders provisional inventory; `sessions` writes bounded summaries; `records` validates sources and transition metadata; `handoff` checks readiness and renders Markdown from feature data.

### 4.2 State & Data Flow
Evidence → current-state inventory → human review → opportunities/concepts/features → accepted feature → informal handoff.

### 4.3 Lifecycle & Ownership
Only the human-confirmed record can enter accepted. The feature directory owns source data; a handoff links it rather than duplicating every detail.

### 4.4 Alternatives Considered
Embedding workflows in skills only was rejected because executable readiness and audit behavior need testable code.

## 5. Interfaces
- `audit_repository(root, scope)` returns evidence records.
- `create_session(root, focus, summary)` allocates a dated unique file.
- `create_handoff(root, feature_id, epic)` returns output path or readiness errors.

## 6. Data Model & Storage
- YAML indexes/records and Markdown narrative files under `docs/product-discovery`; Markdown frontmatter for handoffs.

## 7. Consistency & Transactions
- Each writer validates before atomic output. Handoff has no side effect when readiness is incomplete.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Audit honors inclusion/exclusion scope and scans text extensions only.

## 10. Failure Modes & Resilience
- Missing evidence or readiness fields is reported with field names; unknown feature IDs are rejected.

## 11. Observability
- Audit records confidence and paths. Handoff reports whether `$harness-analyze` is recommended when available.

## 12. Security & Privacy
- No network access; audit reads only local scoped content and writes documentation only.

## 13. Testing Strategy
- AC-001 verifies no application mutation and inference labels; AC-002 verifies session/acceptance metadata; AC-003 verifies handoff failure/success and sections.

## 14. Backwards Compatibility
- Handoff declares `contract_version: 1`; future versions can coexist by frontmatter version.

## 15. Risks & Mitigations
- Overconfident archaeology: default all semantic findings to provisional with confidence.

## 16. Open Questions & Follow-ups
- Rich runtime observation can be added as an explicit opt-in adapter.

## 17. References
- `prd.md`; build specification sections 8.3–8.16 and 22.
