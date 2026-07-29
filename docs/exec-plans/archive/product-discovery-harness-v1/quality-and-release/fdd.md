# Quality and Release - Functional Design Document

## 1. Executive Summary
Pytest fixtures model target states and temporary homes; Make and GitHub Actions execute the package tests and local target validation.

## 2. Requirements & Assumptions
- Functional requirements: FR-001 test coverage, FR-002 CI, FR-003 release evidence.
- Non-functional requirements: tests never use the real home directory.
- Assumptions: CI can install package extras from `pyproject.toml`.

## 3. Repository Context Summary
- What we know: test and validation commands are documented in `docs/TOOLING.md`.
- Unknowns to confirm: release tagging is a maintainer action after CI passes.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
Fixtures contain empty, boilerplate, and application examples. Unit tests call public functions/CLI; installation tests set a temporary HOME. CI runs Make targets.

### 4.2 State & Data Flow
Fixture or temp repo → package command → assertions over files/output/exit status → CI artifact log.

### 4.3 Lifecycle & Ownership
Test fixtures are immutable inputs; per-test temporary copies are the only mutated targets.

### 4.4 Alternatives Considered
End-to-end tests against real agent directories were rejected to avoid developer-home mutation.

## 5. Interfaces
- `make test`, `make validate`, and `.github/workflows/test.yml`.

## 6. Data Model & Storage
- Version metadata and changelog are release-owned repository files.

## 7. Consistency & Transactions
- Each test isolates filesystem mutations using pytest `tmp_path`.

## 8. Caching Strategy
- CI may cache pip downloads only; test outputs are never cache-dependent.

## 9. Performance & Scalability Posture
- Tests use tiny fixtures and no network calls.

## 10. Failure Modes & Resilience
- Assertions surface generated validation diagnostics to make regressions actionable.

## 11. Observability
- Validation and pytest exit codes are CI gates; evidence reports record exact commands.

## 12. Security & Privacy
- Temp home isolates installation metadata and symlinks from personal files.

## 13. Testing Strategy
- AC-001 maps to test modules by behavior; AC-002 reads workflow commands; AC-003 asserts version/changelog evidence.

## 14. Backwards Compatibility
- CI uses declared minimum supported Python and the test suite is local-only.

## 15. Risks & Mitigations
- Installer tests can be platform-sensitive: use portable Python subprocess and POSIX shell conditions.

## 16. Open Questions & Follow-ups
- Windows support is not a v0.1.0 requirement.

## 17. References
- `prd.md`; build specification sections 17, 24, and 26.
