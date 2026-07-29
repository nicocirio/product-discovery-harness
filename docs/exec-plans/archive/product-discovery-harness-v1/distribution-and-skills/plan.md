# Distribution and Skills - Delivery Plan

Scope and reference artifacts:
- PRD: `prd.md`
- FDD: `fdd.md`

## Scope
Ship all agent workflows, shared guidance, global installer operations, and bilingual documentation.

## Clarifications & Default Assumptions
- Stable channel uses the latest semantic tag when present and otherwise default branch.

## Phase 1: Skills and Shared Guidance
- Goal: make all required names operational and consistent.
- Tasks:
  - [x] Create persona/reference documents and 17 SKILL.md files.
  - [x] Add complete external-design prompts and templates.
- Testing Tasks:
  - [x] Verify frontmatter names and referenced resources exist.
  - Command(s): `pytest tests/test_skills.py`
- Definition of Done:
  - AC-001 skill catalog and bilingual guides are complete.
- Gate:
  - Every skill is installable and self-locating.
- Dependencies:
  - Core contract Phase 1.
- Parallelizable Work:
  - README translation and skill authoring.

## Phase 2: Installer Lifecycle
- Goal: safely install, update, repair, and report global skills.
- Tasks:
  - [x] Implement shared shell library and command wrappers.
  - [x] Implement curl-friendly installer delegation.
- Testing Tasks:
  - [x] Run temporary-home install/reinstall/repair/status cases.
  - Command(s): `pytest tests/test_installation.py`
- Definition of Done:
  - AC-002 is idempotent and AC-003 reports selected channel and targets.
- Gate:
  - Temporary-home integration tests pass.
- Dependencies:
  - Phase 1.
- Parallelizable Work:
  - Shell implementation and documentation examples.

## Parallelization Notes
- Skills can be authored in parallel with installer helpers once layout is established.

## Phase Gate Summary
- Gate A: operational skill catalog.
- Gate B: safe installer lifecycle proven.
