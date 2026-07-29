---
name: product-bootstrap
description: Safely seed a target repository and establish discovery mode.
examples: ["$product-bootstrap --mode=greenfield"]
when_to_use: ["A target needs the Product Discovery Harness contract."]
when_not_to_use: ["The target is already valid and only needs a focused session."]
---
## Purpose
Create or preserve durable discovery context.
## Required Resources
Read `agents/product-facilitator.md`, config, and target signals.
## Workflow
Run `product-harness bootstrap <target> --mode=<auto|greenfield|brownfield>`. Preserve substantive files, report mode/evidence/writes, validate, then recommend `$product-audit` for brownfield or `$product-talk` otherwise.
## Conversation Protocol
If mode is pending, explain evidence and ask the owner to choose one mode.
## Documentation Rules
Never invent current-state findings; preserve existing product summaries and specs.
## Validation
Run `product-harness validate <target>`.
## Output Contract
Report target, selected mode, files created/preserved, and validation. End with
exactly one `Recommended next focus:`; use `$product-audit` for brownfield or
`$product-talk` for greenfield.
