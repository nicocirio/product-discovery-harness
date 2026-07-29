# Installation Release Readiness - Functional Design Document

## 1. Executive Summary
Use a Git checkout as the single reusable distribution root. Bash wrappers run
the CLI from that checkout; skills point to shared resources relative to it.

## 2. Requirements & Assumptions
- FR-001/AC-001: checkout-local CLI works after install.
- FR-002/AC-002: stable/latest are resolved with Git during install/update.
- FR-003/AC-003: skill resources resolve from the checkout.
- FR-004/AC-004/AC-005: docs and temporary-HOME tests protect the flow.

## 3. Repository Context Summary
- The Engineering Harness uses clone/fetch/channel checkout and skill symlinks.
- This repository's Python sources run correctly when `PYTHONPATH` is the
  checkout `src/` directory.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
- `bin/libproductharness.sh` owns Git/channel/config/link helpers.
- `bin/product-harness` is a Python module wrapper rooted at its checkout.
- install/update/status use the shared library; install links a CLI wrapper in
  each owned namespace in addition to product skills.
- Skills state that the checkout root is two directories above their real
  `SKILL.md` path.

### 4.2 State & Data Flow
Install → clone/fetch → checkout channel → link skills/CLI → persist metadata.
Update → load metadata → fetch/checkout → repair owned links → persist version.

### 4.3 Lifecycle & Ownership
Only owned namespaces marked by the installer are modified. Target repositories
remain untouched until the owner runs bootstrap.

### 4.4 Alternatives Considered
Wheel/PyPI is deferred because templates/resources require a separately tested
package-data design.

## 5. Interfaces
- `product-harness`, `product-harness-install`, `product-harness-update`, and
  `product-harness-status`.

## 6. Data Model & Storage
- `.install-config` stores checkout path channel URL namespaces and version.

## 7. Consistency & Transactions
- Fetch/checkout occurs before links are changed; temporary config writes are
  atomic.

## 8. Caching Strategy
- Git checkout is the local update cache.

## 9. Performance & Scalability Posture
- N/A.

## 10. Failure Modes & Resilience
- Git/Python absence or failed checkout exits without creating/repairing links.

## 11. Observability
- Status reports selected ref version targets and broken links.

## 12. Security & Privacy
- No `source` of untrusted config; config is parsed as key/value data.

## 13. Testing Strategy
- Temporary HOME tests cover install CLI update metadata and link repair.

## 14. Backwards Compatibility
- Existing local checkout invocation remains supported.

## 15. Risks & Mitigations
- Unavailable remote: explicit failure; local checkout still works.

## 16. Open Questions & Follow-ups
- Wheel distribution is deferred.

## 17. References
- Simon Initiative Engineering Harness installer model.
