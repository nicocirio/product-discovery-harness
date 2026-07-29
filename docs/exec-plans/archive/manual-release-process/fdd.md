# Manual release process - Functional Design Document

## 1. Executive Summary
Add a primary English manual-release section, equivalent Spanish guidance, and an operations reference. No executable release automation is introduced.

## 2. Requirements & Assumptions
- Functional requirements: FR-001, FR-002, FR-003 in `requirements.yml`; AC-001, AC-002, and AC-003 verify the documented procedure, channel explanation, and bilingual parity.
- Non-functional requirements: documentation accurately reflects existing shell installer behavior.
- Assumptions: tags use the `vX.Y.Z` convention accepted by the installer.

## 3. Repository Context Summary
- What we know: `stable` chooses the newest tag and `latest` follows the default branch; CI runs the documented gates.
- Unknowns to confirm: none.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
README gives maintainers the main procedure; `docs/OPERATIONS.md` records the operational policy; Spanish README mirrors the procedure.

### 4.2 State & Data Flow
No runtime state changes. A maintainer updates version metadata and changelog, validates, commits, creates a tag, then pushes commit and tag.

### 4.3 Lifecycle & Ownership
Maintainer-owned manual process; GitHub automation remains out of scope.

### 4.4 Alternatives Considered
Release automation was deferred because a manual first release is easier to inspect and does not require new credentials or workflow permissions.

## 5. Interfaces
- Git commands: `git tag -a vX.Y.Z -m ...` and `git push origin main --follow-tags`.

## 6. Data Model & Storage
- Version metadata and changelog are updated before tagging.

## 7. Consistency & Transactions
- Pushing with `--follow-tags` makes the verified commit and its annotated tag available together.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- N/A.

## 10. Failure Modes & Resilience
- If validation fails, do not tag; fix and rerun gates.

## 11. Observability
- CI and local commands provide release evidence; `product-harness-status` exposes installed version.

## 12. Security & Privacy
- No tokens are documented or stored.

## 13. Testing Strategy
- README tests verify documented skills remain covered; manually inspect exact command consistency.

## 14. Backwards Compatibility
- Existing installer channels remain unchanged.

## 15. Risks & Mitigations
- Stable users may not receive untagged commits: document `latest` as the intentional alternative.

## 16. Open Questions & Follow-ups
- Add post-publication remote installation smoke coverage from the tech-debt tracker.

## 17. References
- `prd.md`; `docs/OPERATIONS.md`; `bin/libproductharness.sh`.
