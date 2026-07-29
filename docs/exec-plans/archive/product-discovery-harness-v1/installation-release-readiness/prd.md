# Installation Release Readiness - Product Requirements Document

## 1. Overview
Replace the partial installer with a checkout-based distribution flow equivalent
to the Engineering Harness model and document it accurately for public users.

## 2. Background & Problem Statement
The current installer links skills but does not expose the CLI they invoke, and
update does not fetch or apply a channel. That makes the public README promise
unreliable after a clean install.

## 3. Goals & Non-Goals
### Goals
- Clone/fetch a self-contained checkout, select stable/latest, link skills, and
  expose a checkout-local CLI wrapper.
- Make shared agents/resources discoverable from each installed skill.
- Provide English-first and Spanish installation documentation.

### Non-Goals
- Publish to PyPI or require wheel installation.
- Change target product-record semantics or add network use during discovery.

## 4. Users & Use Cases
- New owner installs once, then bootstraps many target repositories.
- Existing owner updates a selected channel and repairs skill links.

## 5. UX / UI Requirements
- Commands are copyable and distinguish machine installation from per-target
  bootstrap.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Installer is idempotent, collision-safe, and does not overwrite unowned
  skill namespaces.

## 9. Data, Interfaces & Dependencies
- Bash installer scripts, `bin/product-harness`, skills, README, and tests.

## 10. Repository & Platform Considerations
- Git and Bash are required for distribution; Python 3.10+ is required by the
  checkout-local CLI.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
N/A

## 13. Risks & Mitigations
- Network unavailable: installer fails before mutating links; local checkout
  installs remain supported.

## 14. Open Questions & Assumptions
### Open Questions
- PyPI/wheel distribution remains a future, separately tested channel.

### Assumptions
- Git checkout distribution is the supported public path for v0.1.0.

## 15. QA Plan
- Automated temporary-HOME install/update/status/CLI tests and full gates.

## 16. Definition of Done
- [x] PRD sections complete
- [x] requirements.yml captured and valid
- [x] validation passes
