# Optional Engineering Export - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: preserve product ownership while exporting a compatible handoff on demand.
- In scope: canonical spec, opt-in export, ownership conflict, config, navigation.
- Out of scope: Engineering Harness PRD/FDD/plan manipulation.

## 2. Requirements Coverage
- FR-001 / AC-001: canonical spec exists without exec-plans.
- FR-002 / AC-002: explicit export generates linked v1 informal.md.
- FR-003 / AC-003: unowned informal is preserved and product validator is independent.

## 3. Responsibilities & Boundaries
- Product owns product-specs and product-discovery.
- Engineering owns exec-plans except a generated export explicitly marked as product-owned.

## 4. Interfaces & Signatures
- `create_handoff(..., export_engineering: bool = False)`.
- `HandoffReport(canonical_spec_path, engineering_export_path | None)`.

## 5. Data Flow & Edge Cases
- Main flow:
  1. Validate accepted feature.
  2. Write canonical spec.
  3. Export only when requested and destination is absent or generated.
- Edge cases:
  - Existing unmarked informal causes export failure and no overwrite.
  - Existing old generated export can remain or be explicitly regenerated.

## 6. Test Plan
- Unit tests: rendering and ownership marker.
- Integration tests: no exec-plans target, safe export, conflict preservation.
- Manual checks: read docs/README ownership map.

## 7. Risks & Open Questions
- Risks: callers relying on old Path return; report object makes paths explicit.
- Open questions: CLI feature resolution is deferred.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
