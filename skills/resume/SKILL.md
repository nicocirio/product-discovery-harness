---
name: product-resume
description: Re-enter discovery from repository-local memory.
examples: ["$product-resume"]
when_to_use: ["A discovery session is resumed."]
when_not_to_use: ["Bootstrap has not run."]
---
## Purpose
Summarize mode, phase, decisions, hypotheses, tensions, questions, last session, and recommended focus.
## Preconditions
A bootstrapped target with discovery context. If it is absent, route to
`$product-bootstrap`.
## Required Resources
Read config, STATUS, questions, decision log, product/experience sense, active
records, and `PRODUCT_LANDSCAPE.md` when it exists.
Also read `CONSISTENCY_REPORT.md` when it exists.
## Workflow
Produce a concise re-entry synthesis, including stale/missing-document signals,
then ask one high-leverage question or recommend `$product-landscape`.
## Conversation Protocol
Use `agents/product-facilitator.md`.
## Output Contract
Do not change accepted content without confirmation. End with exactly one
`Recommended next focus:`; use the high-leverage question or `$product-landscape`.
