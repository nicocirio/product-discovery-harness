---
name: product-focus
description: Facilitate discovery around one topic or durable record.
examples: ["$product-focus OPP-001"]
when_to_use: ["A user group, opportunity, capability, tension, or feature needs depth."]
when_not_to_use: ["No resolvable focus exists."]
---
## Purpose
Apply product-talk protocol to a resolved topic.
## Preconditions
A resolvable ID or topic. If an ID cannot resolve, route to
`$product-landscape`; if no durable topic exists yet, route to `$product-talk`.
## Workflow
Resolve the ID/topic, update active focus in STATUS, read its sources, ask one
high-leverage question, and persist only confirmed synthesis.
## Output Contract
Report resolved focus, changes, and next question. End with exactly one
`Recommended next focus:`.
