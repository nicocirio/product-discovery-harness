# Target Contract - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: make target initialization and validation safe, deterministic, and machine-checkable.
- In scope: config, templates, detection, preservation, IDs, and validators.
- Out of scope: product conversation or application-code modification.

## 2. Requirements Coverage
- FR-001 / AC-001: evidence-weighted detector returns greenfield, brownfield, or pending.
- FR-002 / AC-002: seed markers and content classifier preserve user text.
- FR-003 / AC-003: aggregate schema/reference/lifecycle errors with path prefixes.

## 3. Responsibilities & Boundaries
- Package assets remain immutable; target writers own generated files.
- A target write may create only contract/documentation paths.

## 4. Interfaces & Signatures
- `bootstrap(root: Path, mode: str = "auto", scope: Scope | None = None) -> BootstrapReport`
- `validate_target(root: Path) -> list[Diagnostic]`

## 5. Data Flow & Edge Cases
- Main flow:
  1. Resolve root and load existing config if present.
  2. Detect or honor explicit mode.
  3. Create absent template paths and preserve substantive paths.
  4. Validate the result.
- Edge cases:
  - A template path occupied by a directory is an error, not an overwrite.
  - A manifest-only repository stays pending.

## 6. Test Plan
- Unit or component tests:
  - Detection weighting, marker classification, ID parsing, transition rules.
- Integration tests:
  - Bootstrap a temp target twice and validate it.
- Manual checks:
  - Inspect a generated STATUS.md for mode and next skill.

## 7. Risks & Open Questions
- Risks:
  - A source directory could be generated boilerplate; pending mode protects the owner.
- Open questions:
  - None for v0.1.0.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
