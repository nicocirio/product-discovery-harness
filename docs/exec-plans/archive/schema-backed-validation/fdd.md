# Schema-backed validation - Functional Design Document

## 1. Executive Summary
Introduce a small local schema-validation module. `validate_target` will validate each schema-mapped YAML document, then continue with existing record and relationship checks. Engineering handoff creation will validate its generated frontmatter before writing.

## 2. Requirements & Assumptions
- Functional requirements: FR-001, FR-002, and FR-003 in `requirements.yml`.
- Non-functional requirements: deterministic, offline validation with useful errors.
- Assumptions: schemas are packaged beside the source checkout.

## 3. Repository Context Summary
- What we know:
  - `validation.py` owns target diagnostics; `handoff.py` owns atomic export writes.
  - `jsonschema` is already a runtime dependency and `schemas/` is declared package data.
- Unknowns to confirm:
  - None; tests will prove schema loading in the source checkout.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`schema_validation.py` loads a named schema from `schemas/`, runs Draft 2020-12 validation, and formats deterministic errors. Callers select a schema name and add the formatted results to their existing error flow.

### 4.2 State & Data Flow
Target YAML is parsed once per document. Its mapping is validated against its mapped schema, then index records receive existing semantic checks. Handoff frontmatter is validated in memory before `_atomic_write`.

### 4.3 Lifecycle & Ownership
Schemas remain repository-owned package data. The module has no writes and no network access.

### 4.4 Alternatives Considered
Duplicating schema constraints in Python was rejected because it preserves two drifting contracts. Replacing all semantic checks was rejected because relationships and target-relative paths are clearer as domain logic.

## 5. Interfaces
- `validate_schema(schema_name, instance) -> list[str]` returns stable, human-readable schema violations.

## 6. Data Model & Storage
- No migrations; existing target YAML and Markdown formats remain unchanged.

## 7. Consistency & Transactions
- Handoff validation completes before its existing atomic write.

## 8. Caching Strategy
- N/A; these small local schemas may be cached in-process only if it keeps implementation simple.

## 9. Performance & Scalability Posture
- Five small target documents are validated once each; no repository-wide scan is added.

## 10. Failure Modes & Resilience
- Invalid JSON schema files or target instances surface explicit local errors; malformed YAML keeps its existing handling.

## 11. Observability
- CLI return errors identify the affected target-relative document; no external telemetry.

## 12. Security & Privacy
- Schemas are loaded only from the installed package checkout; no remote references are fetched.

## 13. Testing Strategy
- AC-001: mutate a seeded schema-constrained document and assert file-scoped schema error.
- AC-002: preserve seeded-target and semantic validation coverage.
- AC-003: test invalid handoff frontmatter through the schema helper and assert no write.

## 14. Backwards Compatibility
- Existing valid targets remain valid; invalid structures become correctly rejected.

## 15. Risks & Mitigations
- Generic jsonschema paths can be noisy: normalize them into compact messages.

## 16. Open Questions & Follow-ups
- None.

## 17. References
- `prd.md`; `schemas/`; `src/product_discovery_harness/validation.py`; `src/product_discovery_harness/handoff.py`.
