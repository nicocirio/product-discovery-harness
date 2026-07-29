# Product Reconciliation - Functional Design Document

## 1. Executive Summary
Add explicit, validated relation records to opportunity/feature indexes and
render focused/global reconciliation reports without mutating canonical data.

## 2. Requirements & Assumptions
- FR-001 validates relationship and alignment references.
- FR-002 renders focused/global reports.
- FR-003 guides promotion through explicit human confirmation.

## 3. Repository Context Summary
- Existing sessions hold raw ideas; OPP/FEATURE indexes hold durable records;
  CURRENT inventory and decision log provide evidence/intent references.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`reconciliation.py` loads known IDs, validates relation objects, and writes
`CONSISTENCY_REPORT.md` or an ID-focused report. `$product-reconcile` guides
semantic comparison; agent conclusions are proposed until owner confirmation.

### 4.2 State & Data Flow
Session idea → agent comparison → owner decision → canonical relation entry →
derived report. No raw idea becomes an ID automatically.

### 4.3 Lifecycle & Ownership
Indexes own accepted/proposed relations. Reports are derived. Current evidence
describes present behavior; it never silently changes future intent.

### 4.4 Alternatives Considered
An IDEA index was rejected; a generic update-docs skill was rejected because
specific promotion/reconciliation workflows preserve intent and traceability.

## 5. Interfaces
- `generate_reconciliation_report(root, record_id=None) -> ReconciliationReport`
- `product-harness reconcile <target> [--record ID]`

## 6. Data Model & Storage
- `related_records`: id, relation, rationale, status (`proposed|confirmed`).
- `decision_refs`, `current_capability_refs`, and `alignment_status`.

## 7. Consistency & Transactions
- Validation rejects unknown/self/duplicate relations. Reports write atomically.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Reads small local indexes and current inventory only.

## 10. Failure Modes & Resilience
- Invalid references are diagnostics; reports never repair or remove data.

## 11. Observability
- Report unresolved proposed relations and alignment statuses.

## 12. Security & Privacy
- Local read-only comparison outside generated report paths.

## 13. Testing Strategy
- AC-001 relation validation; AC-002 report/no mutation; AC-003 skill contract checks.

## 14. Backwards Compatibility
- All relation fields are optional; existing indexes remain valid.

## 15. Risks & Mitigations
- Semantic false positives are owner-confirmed proposals, not automated facts.

## 16. Open Questions & Follow-ups
- Later add optional heuristic similarity as advisory only.

## 17. References
- `prd.md`, record indexes, sessions, decision log, current-state inventory.
