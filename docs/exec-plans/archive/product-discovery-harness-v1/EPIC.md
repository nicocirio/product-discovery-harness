# Product Discovery Harness v1 — Epic

Informal source: [`Product Discovery Harness Build Spec.md`](../../../../Product%20Discovery%20Harness%20Build%20Spec.md).

## Outcome

Ship an installable, stack-agnostic product-discovery harness that turns
conversation and repository evidence into durable product records and a
decoupled Engineering Harness handoff.

## Feature lanes

1. `core-contract`: Python package, target contract, safe seeding, detection,
   records, IDs, schemas, and validation.
2. `discovery-workflows`: brownfield archaeology, session persistence,
   opportunity/feature lifecycle, external-design briefs, and handoff.
3. `distribution-and-skills`: complete agent skill pack, personas, installer,
   update/status commands, templates, and bilingual documentation.
4. `quality-and-release`: fixtures, automated tests, CI, and release evidence.

## Dependency order

Core contract establishes the stable API and template package. Discovery
workflows and distribution can then proceed, while quality/release completes
after their executable surfaces exist. Each lane has its own PRD, FDD,
requirements traceability, plan, detailed design where useful, execution
record, validation report, and review evidence.

## Decisions

- Initial version is `0.1.0`.
- Python is the single implementation language to keep validation portable.
- YAML uses PyYAML and JSON Schema uses jsonschema; no external service is
  required at runtime.
- The unavailable `$harness-epic` skill is represented by this equivalent
  artifact. All available mandatory Engineering Harness skills are followed
  for every child lane.
