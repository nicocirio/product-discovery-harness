# Guided Skill Routing - Functional Design Document

## 1. Executive Summary
Standardize all installed skill protocols around one actionable next focus and
contextual recovery routes, while leaving the existing product record semantics
and human-approval boundaries unchanged.

## 2. Requirements & Assumptions
- FR-001 / AC-001: every SKILL.md output contract requires exactly one
  `Recommended next focus:`.
- FR-002 / AC-002: stateful or ID-taking skills route missing setup to
  bootstrap, unresolved IDs to landscape, raw ideas to talk, and premature
  specialist requests to the prerequisite discovery activity.
- FR-003 / AC-003: no route creates or accepts a record automatically; talk and
  resume remain no-expertise entry points.
- FR-004 / AC-004: tests cover all skill protocols and README alignment.
- AC-005: all validation gates pass.

## 3. Repository Context Summary
- Each `skills/<name>/SKILL.md` is installed as a standalone skill directory.
- `product-talk`, `product-resume`, and `product-landscape` already contain
  significant routing behavior.
- No runtime router exists; Markdown protocols are the behavioral interface.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
- Every skill gets a concise `Guidance Contract` section near its output
  contract: report the result, explain a blocker if present, and recommend one
  next focus.
- Skills that require an ID, accepted record, concepts, or a baseline gain an
  explicit precondition recovery route.
- `agents/product-facilitator.md` defines the agent's shared conversational
  posture: offer the smallest helpful next action and never manufacture state.
- Tests parse all skill Markdown and assert the stable contract and the key
  recovery routes.

### 4.2 State & Data Flow
Raw thought → talk → explicit owner decision to promote → reconciliation and
record creation as applicable → landscape recovers an ID → specialist skill.
An unmet step returns the user to the immediately preceding useful action;
nothing mutates until the existing protocols allow it.

### 4.3 Lifecycle & Ownership
This changes instruction text only. Canonical indexes, sessions, acceptance
metadata, product specs, and Engineering Harness boundaries retain ownership.

### 4.4 Alternatives Considered
- A new CLI router was rejected: it would add behavior and data inference beyond
  this protocol-hardening scope.
- A shared external instruction document was rejected: installed skills must
  remain understandable independently.

## 5. Interfaces
- All `skills/*/SKILL.md` output contracts and precondition text.
- `agents/product-facilitator.md` and `tests/test_skill_guidance.py`.

## 6. Data Model & Storage
- No schema or storage changes.

## 7. Consistency & Transactions
- Every route is advisory; owner acceptance remains the only path to durable
  acceptance or relation resolution.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- N/A; static Markdown protocol checks.

## 10. Failure Modes & Resilience
- If context cannot resolve, say why and point to one recovery action rather
  than continuing with fabricated IDs or assumptions.

## 11. Observability
- Protocol tests make omissions visible in CI.

## 12. Security & Privacy
- No network, credentials, or application mutation.

## 13. Testing Strategy
- Assert nineteen skills use the next-focus contract.
- Assert required recovery strings and human-approval safeguards.
- Run all repository and Harness gates.

## 14. Backwards Compatibility
- Skill names, existing commands, and file locations do not change.

## 15. Risks & Mitigations
- Overly generic recommendations: each protocol provides context-specific next
  routes while tests verify only stable labels and critical recoveries.

## 16. Open Questions & Follow-ups
- A computed CLI router can be evaluated only after this guidance contract is
  used in real discovery sessions.

## 17. References
- `skill-guidance-audit.md` in the preceding onboarding work item.
