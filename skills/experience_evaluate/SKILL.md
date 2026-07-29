---
name: product-experience-evaluate
description: Evaluate experience concepts and record explicit selection.
examples: ["$product-experience-evaluate OPP-001"]
when_to_use: ["Divergent concepts exist."]
when_not_to_use: ["No concepts have been documented."]
---
## Purpose
Compare outcome fit, learnability, repeat efficiency, cognitive load, discoverability, feedback, recovery, trust, accessibility, delight, extensibility, and feasibility.
## Preconditions
Documented divergent concepts for a resolvable opportunity. If concepts are
missing, route to `$product-experience-explore <opportunity-id>`; if the
opportunity ID is unknown, route to `$product-landscape`.
## Workflow
Record tradeoffs, feedback, assumptions, selected/combined/next experiment, rejected alternatives, and invariants. Scores support discussion but do not decide.
## Documentation Rules
Do not mark selection without owner confirmation.
## Output Contract
Update evaluation and decision records only after owner confirmation. End with
exactly one `Recommended next focus:`; name the selected experiment or
`$product-feature-crystallize <opportunity-id>` when a direction is selected.
