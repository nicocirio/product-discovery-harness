---
name: product-slice
description: Organize accepted features into vertical outcome-oriented releases.
examples: ["$product-slice"]
when_to_use: ["Accepted features need release definition."]
when_not_to_use: ["Technical-layer sequencing is the only available plan."]
---
## Purpose
Define releases by target user and end-to-end outcome, with features, exclusions, dependencies, risks, learning goals, success signals, and progression condition.
## Preconditions
Accepted features with resolvable IDs. If no accepted feature exists, route to
`$product-landscape` to find candidates, then to the missing feature decision;
do not invent a release.
## Documentation Rules
Do not create database/backend/frontend-only releases.
## Output Contract
Update releases and dependencies with feature links. End with exactly one
`Recommended next focus:`; normally validate handoff readiness for the next
accepted feature.
