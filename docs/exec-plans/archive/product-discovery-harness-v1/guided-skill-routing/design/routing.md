# Guided Skill Routing - Detailed Design

Source Artifacts:
- PRD: `../prd.md`
- FDD: `../fdd.md`
- Plan: `../plan.md`

## 1. Slice Summary
- Objective: make every product skill finish with a context-aware route.
- In scope: skill protocol text, facilitator guidance, and regression tests.
- Out of scope: runtime command routing or automatic durable-record changes.

## 2. Requirements Coverage
- FR-001 / AC-001: stable next-focus label in every output contract.
- FR-002 / AC-002: explicit recovery paths for setup, IDs, raw thoughts, and
  specialist prerequisites.
- FR-003 / AC-003: safety language preserves owner confirmation.
- FR-004 / AC-004 / AC-005: automated coverage and validation gates.

## 3. Responsibilities & Boundaries
- Skill protocol: contextual work and recovery instructions.
- Facilitator: plain-language question, minimal next action, no invented state.
- Tests: contract coverage; they do not simulate an agent.

## 4. Interfaces & Signatures
- Required output line: `Recommended next focus: <one action and why>.`
- Recovery routes: `$product-bootstrap`, `$product-talk`,
  `$product-landscape`, or the immediately preceding discovery skill.

## 5. Data Flow & Edge Cases
- Unknown ID → landscape; raw thought → talk; no opportunity outcome →
  opportunity exploration; no concepts → experience exploration; incomplete
  feature → crystallization or the specific missing product decision.

## 6. Test Plan
- Glob every `skills/*/SKILL.md` and assert the contract.
- Assert explicit recovery and safety phrases in the relevant skill docs.
- Run all standard validation commands.

## 7. Risks & Open Questions
- Risk: protocol drift. Mitigation: file-discovery-based tests.
- Open question: defer automated runtime routing.

## 8. Definition of Done
- [x] Requirement coverage is explicit
- [x] Interfaces are concrete
- [x] Test plan covers main and edge paths
- [x] Validation passes
