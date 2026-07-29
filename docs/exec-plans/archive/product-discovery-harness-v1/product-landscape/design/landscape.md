# Product Landscape - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: render a trustworthy orientation table from durable records.
- In scope: real document links, status/next action, review age, stale grouping.
- Out of scope: automatic lifecycle changes and delivery tracking.

## 2. Requirements Coverage
- FR-001 / AC-001: `path` is target-relative and checked before links render.
- FR-002 / AC-002: title/ID, document, status/next action, and review age render.
- FR-003 / AC-003: stale records are marked for review and retain status.

## 3. Responsibilities & Boundaries
- Indexes and detail documents are canonical; PRODUCT_LANDSCAPE is regenerated.
- Only meaningful review changes `last_reviewed_at`.

## 4. Interfaces & Signatures
- `load_index_records(root) -> list[LandscapeItem]`
- `generate_landscape(root, stale_after_days: int = 30) -> LandscapeReport`

## 5. Data Flow & Edge Cases
- Main flow:
  1. Load opportunities/features in stable ID order.
  2. Validate paths and parse dates.
  3. Render grouped Markdown and write only if changed.
- Edge cases:
  - Missing path renders “Missing document path”.
  - Missing review date renders “Never reviewed”.
  - Deferred records remain deferred when stale.

## 6. Test Plan
- Unit tests: relative age, next-action strings, path containment.
- Integration tests: complete/missing documents, stale output, no input changes.
- Manual checks: open generated links in a Markdown viewer.

## 7. Risks & Open Questions
- Risks: intentionally deferred records can be old; language says review, not discard.
- Open questions: configurable policy thresholds are future work.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
