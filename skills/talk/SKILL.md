---
name: product-talk
description: Facilitate iterative open-ended product discovery.
examples: ["$product-talk"]
when_to_use: ["The owner wants to explore product intent."]
when_not_to_use: ["A deterministic validator is needed instead."]
---
## Purpose
Use conversation as interface while repository files remain memory.
## Preconditions
A bootstrapped target so the conversation has durable local memory. If context
is absent, explain that plainly and route to `$product-bootstrap`; do not invent
repository state.
## Required Resources
Read `agents/product-facilitator.md`, STATUS, last session, decisions, and questions.
## Workflow
State current understanding, ask one significant question, distinguish
idea/assumption/question/proposal/decision, summarize checkpoints, and persist
a concise session. Keep raw brainstorms in the session. Before promoting one to
OPP/FEATURE, invoke `$product-reconcile` and obtain explicit owner resolution.
## Documentation Rules
Require explicit acceptance before an important decision becomes accepted.
## Output Contract
Report changed files, tensions, and open questions. End with exactly one
`Recommended next focus:` that names the smallest useful next action; for a raw
thought, this can remain another focused conversation. Never imply automatic promotion,
acceptance, or ID allocation.
