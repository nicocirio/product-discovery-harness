# Distribution and Skills - Functional Design Document

## 1. Executive Summary
Bash entrypoints locate a repository checkout, select a Git channel, and create owned namespace directories containing skill symlinks; skills reference shared operational files.

## 2. Requirements & Assumptions
- Functional requirements: FR-001 supplies artifacts, FR-002 installs namespaces, FR-003 selects/updates channels.
- Non-functional requirements: paths with spaces work and unrelated namespace entries remain untouched.
- Assumptions: Git supports `clone`, `fetch`, and symbolic refs when update is requested.

## 3. Repository Context Summary
- What we know: Engineering Harness demonstrates an installer model and skills must be self-locating.
- Unknowns to confirm: external release tags may not exist for a development checkout.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
`libproductharness.sh` supplies shared safe functions. `install` clones/fetches then links skills. `update` repairs owned links. `status` reads metadata and lists broken links.

### 4.2 State & Data Flow
Environment override/argument → repository checkout/channel → target roots → namespace marker → symlink set → install config.

### 4.3 Lifecycle & Ownership
Namespace marker ties a directory to one repository path. Symlinks use parsed skill frontmatter names.

### 4.4 Alternatives Considered
Copying skills into each root was rejected because it makes updates divergent and loses source ownership.

## 5. Interfaces
- `product-harness-install [stable|latest]`, `product-harness-update [channel]`, and `product-harness-status`.
- `install.sh [channel]` delegates to the installed checkout.

## 6. Data Model & Storage
- `version.json`, `.install-config`, and `.product-harness-install-root` plaintext metadata.

## 7. Consistency & Transactions
- Link replacement happens only for an owned/broken link; config is written after successful target processing.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- Enumerates only direct `skills/*/SKILL.md` entries.

## 10. Failure Modes & Resilience
- Missing Git, unknown channels, and missing metadata fail clearly; stable falls back when no tag exists.

## 11. Observability
- AC-003 command output includes channel, selected ref, repository/installed versions, targets, and broken links.

## 12. Security & Privacy
- Installer never overwrites unrelated entries and uses user-selected environment paths only.

## 13. Testing Strategy
- AC-001 checks skill names and docs; AC-002 temporary-home link lifecycle; AC-003 channel/status assertions.

## 14. Backwards Compatibility
- Namespaced layout permits new skills without colliding with Engineering Harness names.

## 15. Risks & Mitigations
- Symlink resolution differs across platforms: scripts use physical `pwd` and `BASH_SOURCE`.

## 16. Open Questions & Follow-ups
- Package-manager distribution is intentionally outside 0.1.0.

## 17. References
- `prd.md`; build specification sections 7, 14, 18, and 19.
