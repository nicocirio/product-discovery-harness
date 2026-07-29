# Product Landscape - Functional Design Document

## 1. Executive Summary
Extend opportunity and feature indexes with normalized record metadata, then
render `docs/product-discovery/PRODUCT_LANDSCAPE.md` as a derived view.

## 2. Requirements & Assumptions
- Functional requirements: FR-001 defines metadata; FR-002 renders; FR-003 surfaces review signals safely.
- Non-functional requirements: local-only, stable diffs, and no lifecycle mutations.
- Assumptions: dates use ISO `YYYY-MM-DD` in the target owner's local calendar.

## 3. Repository Context Summary
- What we know: indexes exist but do not enforce per-record paths or review timestamps.
- Unknowns to confirm: a configurable stale threshold is deferred; default is 30 days.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`landscape.py` loads indexed records, verifies target-relative paths, calculates
review age, groups results, and atomically writes the view. `validation.py`
validates paths/dates. `cli.py` exposes `landscape`; relevant skills invoke it.

### 4.2 State & Data Flow
Index records → validation/normalization → document existence check → derived
Markdown table and summary. Generation never modifies input records.

### 4.3 Lifecycle & Ownership
Record authors update `last_reviewed_at` after meaningful review. Generation
records no review and never changes a lifecycle status because an item is old.

### 4.4 Alternatives Considered
Parsing every Markdown file was rejected because the index is the stable registry.
Adding `IDEA-*` was rejected: the existing record types and IDs remain sufficient.

## 5. Interfaces
- `generate_landscape(root, stale_after_days=30) -> LandscapeReport`
- `product-harness landscape <target> [--stale-after-days N]`

## 6. Data Model & Storage
- Add optional `title`, `path`, `created_at`, `last_updated_at`,
  `last_reviewed_at`, and `review_after` to index records.

## 7. Consistency & Transactions
- Validate paths before output and write derived Markdown through temp-file replacement.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Reads only two indexes and checks bounded local paths.

## 10. Failure Modes & Resilience
- Invalid date/path returns diagnostics; missing documents render a marker, not a link.

## 11. Observability
- Report total records, stale records, missing documents, and output path.

## 12. Security & Privacy
- Reject absolute/out-of-target paths; no network or Engineering Harness calls.

## 13. Testing Strategy
- AC-001 covers paths, AC-002 covers output/age, and AC-003 covers stale preservation.

## 14. Backwards Compatibility
- Additive optional fields keep existing empty indexes valid.

## 15. Risks & Mitigations
- Generated timestamps could create noisy diffs; unchanged output is not rewritten.

## 16. Open Questions & Follow-ups
- Configurable threshold may be added later.

## 17. References
- `prd.md`, opportunity index, and feature index.
