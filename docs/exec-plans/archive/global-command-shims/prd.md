# Global command shims - Product Requirements Document

## 1. Overview
Make the documented maintenance commands available after installation.

## 2. Background & Problem Statement
The installer omitted shell-command links, causing `command not found`.

## 3. Goals & Non-Goals
### Goals
- Link public commands safely in `~/.local/bin`.
### Non-Goals
- Change product-discovery behavior.

## 4. Users & Use Cases
- Installer user: runs `product-harness-status` directly.

## 5. UX / UI Requirements
- Documentation names the command directory and PATH requirement.

## 6. Functional Requirements
Requirements are found in requirements.yml

## 7. Acceptance Criteria (Testable)
Requirements are found in requirements.yml

## 8. Non-Functional Requirements
- Refuse to replace unmanaged commands.

## 9. Data, Interfaces & Dependencies
- Local symlinks only.

## 10. Repository & Platform Considerations
- POSIX shell and temporary-home integration tests.

## 11. Feature Flagging, Rollout & Migration
No feature flags present in this work item

## 12. Telemetry & Success Metrics
N/A

## 13. Risks & Mitigations
- Command collision: fail rather than overwrite a non-managed path.

## 14. Open Questions & Assumptions
### Open Questions
- None.
### Assumptions
- Users add `~/.local/bin` to PATH when their shell does not already include it.

## 15. QA Plan
- Automated regression test executes the installed status command.

## 16. Definition of Done
- [x] Regression coverage and validation pass for AC-001 and AC-002.
