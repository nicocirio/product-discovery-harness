# Guided Discovery Onboarding - Functional Design Document

## 1. Executive Summary
Replace a catalog-first README journey with intent-first onboarding and add a
read-only audit of the nineteen product skills. The change keeps specialist
skills available while making guided conversation the natural entry point.

## 2. Requirements & Assumptions
- FR-001: `$product-talk` is the default entry in both guides; AC-001 confirms
  the stated guidance behavior.
- FR-002: simple and deeper paths are conditional rather than linear; AC-003
  verifies this distinction.
- FR-003: the booking story reveals IDs as generated records and retrieves them
  with landscape; AC-002 verifies the sequence.
- FR-004: a durable audit covers all skills; AC-004 verifies coverage and
  follow-up recommendations.
- AC-005 requires regression coverage for the new README claims.
- Assumption: the audit records protocol behavior as written, not inferred agent
  behavior or a promise of an implementation change.

## 3. Repository Context Summary
- `skills/*/SKILL.md` defines agent-facing workflow behavior.
- `README.md` is English-first; `README.es.md` is its operational counterpart.
- `tests/test_readme.py` already guards the skill catalog and CLI examples.
- The repository owns no product UI; Markdown is the user interface.

## 4. Proposed Design
### 4.1 Component Roles & Interactions
- README onboarding begins with one user intent and `$product-talk`.
- A continuous appointment-booking story exposes the harness recommendation,
  an explicit durable-record creation, landscape retrieval, and optional deeper
  exploration.
- The existing catalog becomes a grouped reference, not the decision interface.
- `skill-guidance-audit.md` records one row per installed skill: initial
  user-friendly entry, whether it recommends a next step, assumed knowledge,
  and a recommendation.

### 4.2 State & Data Flow
User intent → `$product-talk` → clarified problem → owner-approved promotion
when appropriate → harness-assigned `OPP-*` → `$product-landscape` retrieves
the ID → an optional specialist skill. No documentation path implies automatic
promotion, acceptance, or a mandatory sequence.

### 4.3 Lifecycle & Ownership
README text is explanatory. Skills remain behavioral source of truth. The audit
is a maintainership artifact; it does not alter skills. Future behavior changes
must be implemented in a new work item.

### 4.4 Alternatives Considered
- Retain a linear command chain: rejected because it makes simple work appear
  ceremonial.
- Remove the catalog: rejected because experienced users still need a complete
  reference.
- Change skills before auditing: rejected because it would conceal the actual
  gap this work item must assess.

## 5. Interfaces
- `README.md`, `README.es.md`, and `tests/test_readme.py`.
- `skill-guidance-audit.md` with a stable Markdown table keyed by the nineteen
  skill names.

## 6. Data Model & Storage
- No runtime data changes. The audit stores text only in its work-item folder.

## 7. Consistency & Transactions
- English and Spanish changes land together.
- Tests assert the shared behavioral claims rather than exact prose.

## 8. Caching Strategy
- N/A.

## 9. Performance & Scalability Posture
- N/A; static Markdown and small test reads.

## 10. Failure Modes & Resilience
- If the story becomes inconsistent with a skill, tests and review expose the
  discrepancy; the audit explicitly records it instead of silently changing
  behavior.

## 11. Observability
- Existing repository tests and validation commands provide evidence. No
  product telemetry is emitted.

## 12. Security & Privacy
- No external requests, credentials, or target-repository mutation are added.

## 13. Testing Strategy
- Extend README tests for AC-001, AC-002, AC-003, and AC-005.
- Check audit coverage and required columns for AC-004.
- Run the complete repository and Harness validation gates.

## 14. Backwards Compatibility
- Existing skill names, CLI commands, installation instructions, and handoff
  boundary remain documented and unchanged.

## 15. Risks & Mitigations
- Risk: “guided” could overpromise automation. Mitigation: say the harness
  recommends a next useful step and require explicit promotion/acceptance.
- Risk: deeper work is hidden. Mitigation: retain grouped catalog and a clearly
  labeled optional deep path.

## 16. Open Questions & Follow-ups
- Audit findings will determine the scope of a later skill-behavior work item.

## 17. References
- `skills/*/SKILL.md`, `README.md`, `README.es.md`, and `tests/test_readme.py`.
