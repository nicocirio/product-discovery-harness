---
name: product-handoff
description: Create a canonical product spec and optionally export an Engineering Harness contract.
examples: ["$product-handoff FEATURE-001", "$product-handoff FEATURE-001 --export-engineering"]
when_to_use: ["An accepted feature is ready for engineering analysis."]
when_not_to_use: ["Definition of Ready is incomplete."]
---
## Purpose
Write the canonical product-owned spec without doing engineering design; export
an Engineering Harness `informal.md` only through explicit opt-in.
## Preconditions
A resolvable accepted feature with Definition of Ready evidence. If the feature
ID is unknown, route to `$product-landscape`; if the direction is not yet a
feature, route to `$product-feature-crystallize <opportunity-id>`; if it is a
raw thought, route to `$product-talk`.
## Required Resources
Read feature, opportunities, decisions, product/experience summaries, and `handoff-frontmatter.schema.json`.
## Workflow
Require stable accepted feature, alignment, user, problem, outcome, experience,
interaction model, scope, non-goals, invariants, states, dependencies, signals,
no strategic blockers, and source links. First create/update
`docs/product-specs/<feature>.md`, the canonical product source. Export to
`docs/exec-plans/current/<epic>/<feature>/informal.md` only when the owner uses
`--export-engineering` or explicitly enables it in config. Refuse to overwrite
an unmarked engineering `informal.md`; never modify PRD, FDD, plan, design, or evidence.
## Validation
Validate frontmatter and all required sections.
## Output Contract
Print canonical spec path and export path separately. Print `$harness-analyze`
only after a successful optional export; never require Engineering Harness. End
with exactly one `Recommended next focus:`; name the highest-priority missing
product condition when not ready.
