# Guided Discovery Onboarding - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: make the natural first interaction a guided conversation, then
  expose specialist skills only when useful.
- In scope: README narrative, examples, tests, and a read-only skill audit.
- Out of scope: skill behavior, record schema, and CLI changes.

## 2. Requirements Coverage
- FR-001 / AC-001: lead with `$product-talk` and honest next-step guidance.
- FR-002 / AC-003: show conditional simple and deeper routes.
- FR-003 / AC-002: reveal `OPP-001` only after the creation example, then use
  `$product-landscape` before an ID-taking skill.
- FR-004 / AC-004: table-audit all skills with actionable classifications.
- AC-005: tests assert the stable learning promises.

## 3. Responsibilities & Boundaries
- README: approachable mental model and scenario.
- Skill catalog: complete reference, grouped by intent.
- Tests: stable promises, not stylistic prose.
- Audit: behavioral evidence and follow-up recommendations only.

## 4. Interfaces & Signatures
- Agent prompt: `$product-talk`.
- Deterministic lookup: `product-harness landscape .`.
- Durable record use: `$product-opportunity-explore OPP-001` only after the
  example makes its source clear.

## 5. Data Flow & Edge Cases
- A simple change can move from conversation to a feature candidate once the
  owner has explicitly accepted enough product direction.
- A consequential or uncertain direction can branch into opportunity and
  experience exploration; it is not a mandatory branch.
- A returning user runs landscape instead of memorizing identifiers.

## 6. Test Plan
- Assert both languages include the conversational entry, guidance statement,
  ID creation and landscape sequence, and simple/deep headings.
- Assert audit lists every installed skill and its required columns.
- Run repository and Harness validation.

## 7. Risks & Open Questions
- Risk: story reads as a prescribed lifecycle. Mitigation: explicitly label
  branches as optional and context-dependent.
- Open question: which audit findings warrant behavior changes is deferred.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
