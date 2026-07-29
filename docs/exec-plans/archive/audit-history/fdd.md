# Audit history - Functional Design Document

## 1. Executive Summary
Extend `audit_repository` to return an `AuditReport` containing current and historical paths. It writes current-state artifacts as before, creates a non-colliding dated report in `audits/`, rebuilds a small local index, and exposes this through a new CLI `audit` command.

## 2. Requirements & Assumptions
- Functional requirements: FR-001, FR-002, FR-003 in `requirements.yml`.
- Non-functional requirements: offline, scoped, filesystem-only output.
- Assumptions: date plus a two-digit sequence is understandable and collision-safe for same-day runs.

## 3. Repository Context Summary
- What we know:
  - `audit.py` owns static repository archaeology and currently writes current-state artifacts.
  - `cli.py` owns user-visible command output; the product-audit skill is the workflow entrypoint.
- Unknowns to confirm:
  - None.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`audit_repository` produces findings, refreshes current-state files, writes `audits/YYYY-MM-DD-NN-repository-audit.md`, and rebuilds `audits/README.md`. CLI invokes it and prints all relevant paths.

### 4.2 State & Data Flow
Scoped source files become provisional findings. The same findings render both the current YAML snapshot and the immutable Markdown report. The audit index links reports newest first.

### 4.3 Lifecycle & Ownership
All writes stay in `docs/product-discovery/`; application code remains read-only. Existing historical reports are never edited.

### 4.4 Alternatives Considered
Appending to one report was rejected because it blurs run boundaries. Git history alone was rejected because the durable product artifact should be readable without git commands.

## 5. Interfaces
- `AuditReport(findings, feature_inventory_path, repository_map_path, historical_report_path, index_path)`.
- `product-harness audit <target>` prints these paths and a recommended next focus.

## 6. Data Model & Storage
- Markdown reports contain date, scope, provisional notice, current-snapshot links, and a findings table.

## 7. Consistency & Transactions
- Each report is assigned an unused filename before write; the current snapshot reflects the same findings.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Reuses the existing scoped static scan; index rebuild only reads local report filenames.

## 10. Failure Modes & Resilience
- Missing target config remains a CLI error; a same-day collision increments the sequence.

## 11. Observability
- Returned paths and CLI output identify generated evidence.

## 12. Security & Privacy
- No network calls or application execution; only target documentation is written.

## 13. Testing Strategy
- AC-001: fixed-date repeated audit test.
- AC-002: verify snapshots and scope-derived findings.
- AC-003: exercise CLI output and audit index links.

## 14. Backwards Compatibility
- Existing current-state paths are preserved; audits add a new discoverable directory.

## 15. Risks & Mitigations
- Too many reports may grow the index: Markdown index remains inexpensive and is human-managed like other discovery records.

## 16. Open Questions & Follow-ups
- None.

## 17. References
- `prd.md`; `src/product_discovery_harness/audit.py`; `skills/audit/SKILL.md`.
