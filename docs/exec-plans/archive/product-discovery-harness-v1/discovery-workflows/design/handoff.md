# Handoff - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: convert only accepted, ready feature records into a public Engineering Harness informal contract.
- In scope: readiness checks, frontmatter, required sections, product-spec link.
- Out of scope: architecture, migration, or implementation plan generation.

## 2. Requirements Coverage
- FR-003 / AC-003: missing Definition-of-Ready fields block output; valid input creates exact work-item path.

## 3. Responsibilities & Boundaries
- `handoff` reads feature records and writes only `docs/product-specs` and `docs/exec-plans/current`.

## 4. Interfaces & Signatures
- `create_handoff(root: Path, feature_id: str, epic: str | None = None) -> HandoffReport`

## 5. Data Flow & Edge Cases
- Main flow:
  1. Locate feature by index/ID.
  2. Validate accepted state, metadata, and required fields.
  3. Render frontmatter and ordered sections.
- Edge cases:
  - Unknown source opportunity fails cross-reference validation.
  - A missing epic writes the allowed non-epic path.

## 6. Test Plan
- Unit or component tests:
  - Readiness error list and section renderer.
- Integration tests:
  - Valid fixture generates and validates informal.md.
- Manual checks:
  - Run displayed `$harness-analyze` command when Engineering Harness is installed.

## 7. Risks & Open Questions
- Risks:
  - Duplication drifts; use source links for long content.
- Open questions:
  - None.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
