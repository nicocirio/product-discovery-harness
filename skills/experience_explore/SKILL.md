---
name: product-experience-explore
description: Generate divergent interaction models for an opportunity.
examples: ["$product-experience-explore OPP-001"]
when_to_use: ["An opportunity and experience direction need alternatives."]
when_not_to_use: ["The opportunity lacks an outcome."]
---
## Purpose
Create three to five materially different concepts, not cosmetic variants.
## Preconditions
A resolvable opportunity with a stated outcome. If the ID is unknown, route to
`$product-landscape`; if the outcome is still unclear, route to
`$product-opportunity-explore <opportunity-id>` or `$product-talk` for a raw
thought.
## Required Resources
Read opportunity, product north, experience north, current evidence, constraints, users, realistic data, `agents/experience-strategist.md`, and external-design templates.
## Workflow
Document mental model, flows, first/repeat use, empty/loading/error/ambiguity/permission/large-data/mobile states, advantages, risks, assumptions, and technical questions. Create vendor-neutral plus optional Claude/Figma/code prompts.
## Documentation Rules
Store external links in `prototypes.md`; repository remains source of truth.
## Output Contract
Report concepts and one next evaluation question. End with exactly one
`Recommended next focus:`; normally `$product-experience-evaluate
<opportunity-id>` when concepts are ready.
