---
name: product-feature-crystallize
description: Convert a selected opportunity direction into a feature candidate.
examples: ["$product-feature-crystallize OPP-001"]
when_to_use: ["An opportunity has explored experience direction."]
when_not_to_use: ["Architecture or implementation design is requested."]
---
## Purpose
Create a FEATURE record with sources, users, problem, outcome, why now, experience, interaction model, journey, states, invariants, flexible areas, scope, non-goals, success signals, dependencies, constraints, questions, prototypes, alternatives, and status.
## Preconditions
A resolvable opportunity and an owner-selected product direction. If the ID is
unknown, route to `$product-landscape`; if the thought is raw, route to
`$product-talk`; if interaction alternatives remain unresolved, route to
`$product-experience-evaluate <opportunity-id>`.
## Workflow
Allocate a stable FEATURE ID; create
`docs/product-discovery/features/<FEATURE-ID>/feature.md` from the template;
add title, target-relative path, created_at, last_updated_at, and
last_reviewed_at to the canonical index record; and start at candidate unless
explicitly accepted.
Run `$product-reconcile` before promotion and record confirmed source,
overlap/conflict, decision, and current-capability relationships.
## Documentation Rules
Exclude modules, migrations, architecture, and implementation steps.
## Validation
Validate sources and acceptance metadata.
## Output Contract
Update feature index and feature directory. Update `last_reviewed_at` only after
 a meaningful product review, then regenerate `$product-landscape`. End with
 exactly one `Recommended next focus:`; normally reconcile the candidate or
 prepare slicing only after owner acceptance.
