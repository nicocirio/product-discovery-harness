# Global command shims - Functional Design Document

## 1. Executive Summary
The installer and updater create safe symlinks in `~/.local/bin`; all linked
shell entrypoints resolve their own symlinks before locating shared code.

## 2. Requirements & Assumptions
- FR-001 / AC-001: install and execute the documented command through PATH.
- AC-002: run the refreshed installer after an existing checkout is updated.

## 3. Repository Context Summary
- Existing installer already maintains skill symlinks and local metadata.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
- `product_harness_link_commands` creates or refreshes only managed symlinks.

### 4.2 State & Data Flow
- Install/update link commands; status resolves itself back to the checkout.

### 4.3 Lifecycle & Ownership
- User-owned non-symlink commands are never replaced.

### 4.4 Alternatives Considered
- Requiring checkout-relative commands was rejected because it contradicts the documented direct command.

## 5. Interfaces
- `~/.local/bin/product-harness-status`.

## 6. Data Model & Storage
- Symlinks only.

## 7. Consistency & Transactions
- Existing safe link behavior is retained.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- N/A.

## 10. Failure Modes & Resilience
- Unmanaged collisions return a clear error.

## 11. Observability
- Installer prints the command directory.

## 12. Security & Privacy
- No network or secret changes.

## 13. Testing Strategy
- AC-001: temporary-home test invokes command through PATH.

## 14. Backwards Compatibility
- Existing checkout-relative entrypoints continue to work.

## 15. Risks & Mitigations
- Missing PATH entry: README states the requirement.

## 16. Open Questions & Follow-ups
- None.

## 17. References
- `tests/test_installation.py`.
