# Installer - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: install all skills idempotently into safe Codex/Claude namespaces.
- In scope: checkout/channel selection, namespace markers, links, metadata, status, repair.
- Out of scope: modifying unowned skills or target repository content.

## 2. Requirements Coverage
- FR-002 / AC-002: owned namespace links are idempotent and repairable.
- FR-003 / AC-003: channel selection and status report local state.

## 3. Responsibilities & Boundaries
- Shell library owns installer mechanics; package CLI is not responsible for global link management.

## 4. Interfaces & Signatures
- `product-harness-install [stable|latest]`
- `product-harness-update [stable|latest]`
- `product-harness-status`

## 5. Data Flow & Edge Cases
- Main flow:
  1. Resolve checkout, channel, and target roots.
  2. Choose or verify owned namespace.
  3. Link skill directories named from frontmatter.
- Edge cases:
  - An unrelated namespace is left untouched and a suffix namespace is selected.
  - A broken owned symlink is replaced.

## 6. Test Plan
- Unit or component tests:
  - Frontmatter names and namespace selection.
- Integration tests:
  - Temporary-home install, reinstall, unlink, update, and status.
- Manual checks:
  - Run status against a checkout with a path containing spaces.

## 7. Risks & Open Questions
- Risks:
  - Gitless local source checkout; provide `PRODUCT_HARNESS_REPO_PATH` for local install tests.
- Open questions:
  - None.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
