# Product Reconciliation - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: reveal and persist product-record overlap/contradiction context.
- In scope: relationship fields, validation, derived reports, agent workflow.
- Out of scope: automatic semantic resolution or IDEA IDs.

## 2. Requirements Coverage
- FR-001 / AC-001: relation IDs/types/rationales are checked.
- FR-002 / AC-002: reports cite canonical records and do not mutate them.
- FR-003 / AC-003: promotion remains session-first and owner-confirmed.

## 3. Responsibilities & Boundaries
- Agent identifies semantic candidates; index records hold confirmed/proposed links.
- Current IDs are evidence, decisions are intent, OPP/FEATURE are future product.

## 4. Interfaces & Signatures
- `validate_relationships(records, known_ids) -> list[str]`
- `generate_reconciliation_report(root, record_id=None) -> ReconciliationReport`

## 5. Data Flow & Edge Cases
- Main flow: load records, validate links, render unresolved/confirmed relation tables.
- Edge cases: self reference, duplicate relation, unknown CURRENT/DEC, missing rationale.

## 6. Test Plan
- Unit: relation validation and vocabulary.
- Integration: focused/global report and source-index preservation.
- Manual: agent cites conflicting docs before asking a resolution question.

## 7. Risks & Open Questions
- Risks: relation clutter; use small fixed vocabulary and only persist meaningful links.
- Open questions: heuristic suggestion remains future work.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
