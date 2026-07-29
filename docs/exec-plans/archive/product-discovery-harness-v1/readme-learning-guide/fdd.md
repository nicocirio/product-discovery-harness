# README Learning Guide - Functional Design Document

## 1. Executive Summary
Replace the terse README with an English-first learning guide and a complete
Spanish counterpart, grounded only in implemented behavior.

## 2. Requirements & Assumptions
- FR-001 explains durable truth layers and workflow.
- FR-002 covers every skill, commands, outputs, safety, and Simon complement.
- FR-003 preserves equivalent Spanish guidance.
- AC-001 verifies valid skill-versus-CLI examples; AC-002 verifies full skill
  coverage and workflow/output examples; AC-003 verifies equivalent Spanish guidance.

## 3. Repository Context Summary
- 19 skills exist; CLI supports bootstrap, detect, validate, landscape, and reconcile.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
README uses two Mermaid diagrams, grouped catalog tables, exact examples, and
links to individual skill sources. Spanish mirrors the operational content.

### 4.2 State & Data Flow
Reader learns free session → promotion → reconciliation → product spec → optional export.

### 4.3 Lifecycle & Ownership
README is explanatory only; target docs and skill files remain canonical behavior.

### 4.4 Alternatives Considered
An exhaustive prose copy of every SKILL.md was rejected; grouped tables link to
skills while examples teach the common paths.

## 5. Interfaces
- `README.md` and `README.es.md`.

## 6. Data Model & Storage
- N/A.

## 7. Consistency & Transactions
- Update both language versions in one change and test referenced local paths.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- N/A.

## 10. Failure Modes & Resilience
- Invalid examples are prevented by repository checks.

## 11. Observability
- Development commands are documented and executable.

## 12. Security & Privacy
- Safety/non-goals explain no private service or code mutation during discovery.

## 13. Testing Strategy
- Check skills/catalog coverage, local links, CLI help, and README section parity.

## 14. Backwards Compatibility
- Existing install and target paths remain unchanged.

## 15. Risks & Mitigations
- Mermaid is supplemental; prose conveys the same critical relationships.

## 16. Open Questions & Follow-ups
- Keep examples updated when skill behavior changes.

## 17. References
- Existing skills, CLI, templates, and Simon Initiative public repository.
