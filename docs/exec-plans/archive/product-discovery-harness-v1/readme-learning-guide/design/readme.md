# README Learning Guide - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: teach the harness as a coherent product-thinking practice.
- In scope: diagrams, examples, catalog, workflows, ownership, installation.
- Out of scope: changing skill behavior.

## 2. Requirements Coverage
- FR-001 / AC-001: mental model and valid syntax distinction.
- FR-002 / AC-002: all skills, examples, safety, and optional complement.
- FR-003 / AC-003: aligned Spanish counterpart.

## 3. Responsibilities & Boundaries
- README describes; SKILL.md files define operational detail.

## 4. Interfaces & Signatures
- Markdown headings, Mermaid fences, tables, and local links.

## 5. Data Flow & Edge Cases
- Main flow: choose mode → conversation → durable promotion → reconcile → handoff.
- Edge case: Engineering Harness absent; canonical product specs still work.

## 6. Test Plan
- Unit: catalog names match skill frontmatter.
- Integration: command examples expose help and links exist.
- Manual: scan English/Spanish rendering on GitHub.

## 7. Risks & Open Questions
- Risks: long catalog; group skills and keep details linked.
- Open questions: none.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
