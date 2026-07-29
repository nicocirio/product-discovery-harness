# Guided Skill Routing - Execution Record

## Delivered
- Added a shared guidance contract to `agents/product-facilitator.md`: do not
  expect workflow expertise or memorized IDs; state one smallest helpful next
  action; never manufacture durable state.
- Updated all nineteen product SKILL.md protocols to require exactly one
  `Recommended next focus:` in their output contract.
- Added recovery routes for uninitialized targets, raw thoughts, unknown IDs,
  missing opportunities, absent experience concepts, incomplete features, and
  unavailable brownfield baseline evidence.
- Added `tests/test_skill_guidance.py`, which discovers every installed skill
  and validates contract coverage, safety, and recovery routing.

## Design Decisions
- Guidance remains agent-facing Markdown, not a new CLI router. This preserves
  the existing local, deterministic CLI scope and avoids inventing product state.
- All routes are advisory. They never bypass explicit owner confirmation for
  promotion, acceptance, merge, supersession, rejection, or handoff.
- The README promise remains accurate without changing its prose: `$product-talk`
  is now explicitly able to recover an uninitialized target through bootstrap.

## Review Loop
- Local diff review followed `docs/CODEREVIEW.md` and focused on preservation
  safety, contract completeness, cross-skill coherence, and test coverage.
- Finding resolved during review: specialist recovery text must be declared in
  `## Preconditions`, not only embedded in workflow prose. `focus` and
  `reconcile` were corrected and tests enforce the shape.

## Evidence
- Targeted skill and README tests: 12 passed.
- Full repository suite: 24 passed.
- Product target, Harness contract, work-item, detailed-design, and traceability
  validations passed on 2026-07-29.
