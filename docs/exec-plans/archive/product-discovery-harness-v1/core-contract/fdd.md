# Core Contract - Functional Design Document

## 1. Executive Summary
A typed Python package centralizes paths, detection, seed preservation, record IDs, and validation behind a small CLI.

## 2. Requirements & Assumptions
- Functional requirements: FR-001, FR-002, and FR-003 are implemented by detection, seeding, and validation modules.
- Non-functional requirements: deterministic local behavior and actionable diagnostics.
- Assumptions: PyYAML and jsonschema are available through declared package dependencies.

## 3. Repository Context Summary
- What we know: the repository starts as a reusable Harness distribution with Engineering Harness contract docs.
- Unknowns to confirm: target applications may use arbitrary stacks, so detection remains heuristic.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`cli` delegates to pure modules. `paths` resolves the target, `detection` returns a structured result, `seeding` writes only absent/marker files, `ids` owns a registry, and `validation` aggregates errors.

### 4.2 State & Data Flow
CLI input → resolved target/config → read templates and records → atomic documentation writes → validation result.

### 4.3 Lifecycle & Ownership
The target owns all generated discovery files. The installed package owns templates and schemas; bootstrap never silently upgrades substantive target content.

### 4.4 Alternatives Considered
A shell-only implementation was rejected because YAML/schema/record validation needs reliable cross-platform parsing.

## 5. Interfaces
- `detect_mode(root, explicit_mode)` returns mode, status, and evidence.
- `seed_target(root, mode, scope)` returns created, preserved, and updated paths.
- `validate_target(root)` returns structured diagnostics and exit status.

## 6. Data Model & Storage
- YAML config and indexes; JSON Schema documents; `.product-harness-seed` markers; an ID registry YAML file.

## 7. Consistency & Transactions
- Atomic replace is used for generated YAML/Markdown metadata. A lock file prevents normal local ID allocation races.

## 8. Caching Strategy
- N/A; all reads are local and fast.

## 9. Performance & Scalability Posture
- Scope-aware scanning excludes dependency/build directories and stops at a bounded evidence count.

## 10. Failure Modes & Resilience
- Invalid YAML, conflicting paths, or failed schemas return accumulated errors without partial forced overwrite.

## 11. Observability
- Commands print writes/preservations and validation paths; no remote metrics are emitted.

## 12. Security & Privacy
- Paths are resolved under the caller-selected target. Discovery never executes untrusted application code.

## 13. Testing Strategy
- AC-001 fixture detection tests; AC-002 seeding/preservation tests; AC-003 invalid config/reference/lifecycle tests.

## 14. Backwards Compatibility
- Config and handoff versions begin at 1; templates carry a marker to enable future migration guidance.

## 15. Risks & Mitigations
- Heuristic false positives: return pending when signals conflict or are only boilerplate.

## 16. Open Questions & Follow-ups
- A future migration command may upgrade intentionally selected seeded placeholders.

## 17. References
- `prd.md`; build specification section 4, 9, 10, 15, and 16.
